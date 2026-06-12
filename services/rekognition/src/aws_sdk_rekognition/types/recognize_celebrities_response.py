"""Generated from Smithy shape ``com.amazonaws.rekognition#RecognizeCelebritiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.celebrity_list
    import aws_sdk_rekognition.types.compared_face_list
    import aws_sdk_rekognition.types.orientation_correction


class RecognizeCelebritiesResponse(TypedDict):
    celebrity_faces: NotRequired[
        "aws_sdk_rekognition.types.celebrity_list.CelebrityList"
    ]
    """<p>Details about each celebrity found in the image. Amazon Rekognition can detect a maximum of 64 celebrities in an image. Each celebrity object includes the following attributes: <code>Face</code>, <code>Confidence</code>, <code>Emotions</code>, <code>Landmarks</code>, <code>Pose</code>, <code>Quality</code>, <code>Smile</code>, <code>Id</code>, <code>KnownGender</code>, <code>MatchConfidence</code>, <code>Name</code>, <code>Urls</code>.</p>"""
    unrecognized_faces: NotRequired[
        "aws_sdk_rekognition.types.compared_face_list.ComparedFaceList"
    ]
    """<p>Details about each unrecognized face in the image.</p>"""
    orientation_correction: NotRequired[
        "aws_sdk_rekognition.types.orientation_correction.OrientationCorrection"
    ]
    """<note> <p>Support for estimating image orientation using the the OrientationCorrection field has ceased as of August 2021. Any returned values for this field included in an API response will always be NULL.</p> </note> <p>The orientation of the input image (counterclockwise direction). If your application displays the image, you can use this value to correct the orientation. The bounding box coordinates returned in <code>CelebrityFaces</code> and <code>UnrecognizedFaces</code> represent face locations before the image orientation is corrected. </p> <note> <p>If the input image is in .jpeg format, it might contain exchangeable image (Exif) metadata that includes the image's orientation. If so, and the Exif metadata for the input image populates the orientation field, the value of <code>OrientationCorrection</code> is null. The <code>CelebrityFaces</code> and <code>UnrecognizedFaces</code> bounding box coordinates represent face locations after Exif metadata is used to correct the image orientation. Images in .png format don't contain Exif metadata. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecognizeCelebritiesResponse) -> dict:
    out: dict = {}
    if "celebrity_faces" in value:
        import aws_sdk_rekognition.types.celebrity_list

        out["CelebrityFaces"] = (
            aws_sdk_rekognition.types.celebrity_list.serialize_aws_json_1_1(
                value["celebrity_faces"]
            )
        )
    if "unrecognized_faces" in value:
        import aws_sdk_rekognition.types.compared_face_list

        out["UnrecognizedFaces"] = (
            aws_sdk_rekognition.types.compared_face_list.serialize_aws_json_1_1(
                value["unrecognized_faces"]
            )
        )
    if "orientation_correction" in value:
        import aws_sdk_rekognition.types.orientation_correction

        out["OrientationCorrection"] = (
            aws_sdk_rekognition.types.orientation_correction.serialize_aws_json_1_1(
                value["orientation_correction"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecognizeCelebritiesResponse:
    out: RecognizeCelebritiesResponse = {}  # type: ignore[typeddict-item]
    if "CelebrityFaces" in data:
        import aws_sdk_rekognition.types.celebrity_list

        out["celebrity_faces"] = (
            aws_sdk_rekognition.types.celebrity_list.deserialize_aws_json_1_1(
                data["CelebrityFaces"]
            )
        )
    if "UnrecognizedFaces" in data:
        import aws_sdk_rekognition.types.compared_face_list

        out["unrecognized_faces"] = (
            aws_sdk_rekognition.types.compared_face_list.deserialize_aws_json_1_1(
                data["UnrecognizedFaces"]
            )
        )
    if "OrientationCorrection" in data:
        import aws_sdk_rekognition.types.orientation_correction

        out["orientation_correction"] = (
            aws_sdk_rekognition.types.orientation_correction.deserialize_aws_json_1_1(
                data["OrientationCorrection"]
            )
        )
    return out
