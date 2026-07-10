import cv2
import mediapipe as mp


mp_drawing=mp.solutions.drawing_utils
mp_drawing_style=mp.solutions.drawing_styles
my_drawing_specs=mp_drawing.DrawingSpec(color=(255,0,0), circle_radius=5)

cap = cv2.VideoCapture(0)

mp_face_mesh=mp.solutions.face_mesh

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5

)as face_mesh:



    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break
        result =face_mesh.process(image)
        for face_landmarks in result.multi_face_landmarks:
            mp_drawing.draw_landmarks(image=image,
                                        landmark_list=face_landmarks,
                                        connections=mp_face_mesh.FACEMESH_TESSELATION,
                                      landmark_drawing_spec=None,
                                      connection_drawing_spec=mp_drawing_style.get_default_face_mesh_tesselation_style()
                                      )
            mp_drawing.draw_landmarks(image=image,
                                      landmark_list=face_landmarks,
                                      connections=mp_face_mesh.FACEMESH_CONTOURS,
                                      landmark_drawing_spec=None,
                                      connection_drawing_spec=my_drawing_specs#.get_default_face_mesh_contours_style()
                                      )




        cv2.imshow("my captured video", cv2.flip(image, 1))


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()