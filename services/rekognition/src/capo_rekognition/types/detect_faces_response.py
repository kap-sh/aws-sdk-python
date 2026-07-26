"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectFacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.face_detail_list
    import capo_rekognition.types.orientation_correction


class DetectFacesResponse(TypedDict, closed=True):
    face_details: NotRequired["capo_rekognition.types.face_detail_list.FaceDetailList"]
    """<p>Details of each face found in the image. </p>"""
    orientation_correction: NotRequired[
        "capo_rekognition.types.orientation_correction.OrientationCorrection"
    ]
    """<p>The value of <code>OrientationCorrection</code> is always null.</p> <p>If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don't contain Exif metadata.</p> <p>Amazon Rekognition doesn’t perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates aren't translated and represent the object locations before the image is rotated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectFacesResponse) -> dict:
    out: dict = {}
    if "face_details" in value:
        import capo_rekognition.types.face_detail_list

        out["FaceDetails"] = (
            capo_rekognition.types.face_detail_list.serialize_aws_json_1_1(
                value["face_details"]
            )
        )
    if "orientation_correction" in value:
        import capo_rekognition.types.orientation_correction

        out["OrientationCorrection"] = (
            capo_rekognition.types.orientation_correction.serialize_aws_json_1_1(
                value["orientation_correction"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectFacesResponse:
    out: DetectFacesResponse = {}  # type: ignore[typeddict-item]
    if "FaceDetails" in data:
        import capo_rekognition.types.face_detail_list

        out["face_details"] = (
            capo_rekognition.types.face_detail_list.deserialize_aws_json_1_1(
                data["FaceDetails"]
            )
        )
    if "OrientationCorrection" in data:
        import capo_rekognition.types.orientation_correction

        out["orientation_correction"] = (
            capo_rekognition.types.orientation_correction.deserialize_aws_json_1_1(
                data["OrientationCorrection"]
            )
        )
    return out
