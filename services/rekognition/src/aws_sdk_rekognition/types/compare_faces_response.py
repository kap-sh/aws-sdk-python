"""Generated from Smithy shape ``com.amazonaws.rekognition#CompareFacesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.compare_faces_match_list
    import aws_sdk_rekognition.types.compare_faces_unmatch_list
    import aws_sdk_rekognition.types.compared_source_image_face
    import aws_sdk_rekognition.types.orientation_correction


class CompareFacesResponse(TypedDict):
    source_image_face: NotRequired[
        "aws_sdk_rekognition.types.compared_source_image_face.ComparedSourceImageFace"
    ]
    """<p>The face in the source image that was used for comparison.</p>"""
    face_matches: NotRequired[
        "aws_sdk_rekognition.types.compare_faces_match_list.CompareFacesMatchList"
    ]
    """<p>An array of faces in the target image that match the source image face. Each <code>CompareFacesMatch</code> object provides the bounding box, the confidence level that the bounding box contains a face, and the similarity score for the face in the bounding box and the face in the source image.</p>"""
    unmatched_faces: NotRequired[
        "aws_sdk_rekognition.types.compare_faces_unmatch_list.CompareFacesUnmatchList"
    ]
    """<p>An array of faces in the target image that did not match the source image face.</p>"""
    source_image_orientation_correction: NotRequired[
        "aws_sdk_rekognition.types.orientation_correction.OrientationCorrection"
    ]
    """<p>The value of <code>SourceImageOrientationCorrection</code> is always null.</p> <p>If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don't contain Exif metadata.</p> <p>Amazon Rekognition doesn’t perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates aren't translated and represent the object locations before the image is rotated. </p>"""
    target_image_orientation_correction: NotRequired[
        "aws_sdk_rekognition.types.orientation_correction.OrientationCorrection"
    ]
    """<p>The value of <code>TargetImageOrientationCorrection</code> is always null.</p> <p>If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this orientation information to perform image correction. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don't contain Exif metadata.</p> <p>Amazon Rekognition doesn’t perform image correction for images in .png format and .jpeg images without orientation information in the image Exif metadata. The bounding box coordinates aren't translated and represent the object locations before the image is rotated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompareFacesResponse) -> dict:
    out: dict = {}
    if "source_image_face" in value:
        import aws_sdk_rekognition.types.compared_source_image_face

        out["SourceImageFace"] = (
            aws_sdk_rekognition.types.compared_source_image_face.serialize_aws_json_1_1(
                value["source_image_face"]
            )
        )
    if "face_matches" in value:
        import aws_sdk_rekognition.types.compare_faces_match_list

        out["FaceMatches"] = (
            aws_sdk_rekognition.types.compare_faces_match_list.serialize_aws_json_1_1(
                value["face_matches"]
            )
        )
    if "unmatched_faces" in value:
        import aws_sdk_rekognition.types.compare_faces_unmatch_list

        out["UnmatchedFaces"] = (
            aws_sdk_rekognition.types.compare_faces_unmatch_list.serialize_aws_json_1_1(
                value["unmatched_faces"]
            )
        )
    if "source_image_orientation_correction" in value:
        import aws_sdk_rekognition.types.orientation_correction

        out["SourceImageOrientationCorrection"] = (
            aws_sdk_rekognition.types.orientation_correction.serialize_aws_json_1_1(
                value["source_image_orientation_correction"]
            )
        )
    if "target_image_orientation_correction" in value:
        import aws_sdk_rekognition.types.orientation_correction

        out["TargetImageOrientationCorrection"] = (
            aws_sdk_rekognition.types.orientation_correction.serialize_aws_json_1_1(
                value["target_image_orientation_correction"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompareFacesResponse:
    out: CompareFacesResponse = {}  # type: ignore[typeddict-item]
    if "SourceImageFace" in data:
        import aws_sdk_rekognition.types.compared_source_image_face

        out["source_image_face"] = (
            aws_sdk_rekognition.types.compared_source_image_face.deserialize_aws_json_1_1(
                data["SourceImageFace"]
            )
        )
    if "FaceMatches" in data:
        import aws_sdk_rekognition.types.compare_faces_match_list

        out["face_matches"] = (
            aws_sdk_rekognition.types.compare_faces_match_list.deserialize_aws_json_1_1(
                data["FaceMatches"]
            )
        )
    if "UnmatchedFaces" in data:
        import aws_sdk_rekognition.types.compare_faces_unmatch_list

        out["unmatched_faces"] = (
            aws_sdk_rekognition.types.compare_faces_unmatch_list.deserialize_aws_json_1_1(
                data["UnmatchedFaces"]
            )
        )
    if "SourceImageOrientationCorrection" in data:
        import aws_sdk_rekognition.types.orientation_correction

        out["source_image_orientation_correction"] = (
            aws_sdk_rekognition.types.orientation_correction.deserialize_aws_json_1_1(
                data["SourceImageOrientationCorrection"]
            )
        )
    if "TargetImageOrientationCorrection" in data:
        import aws_sdk_rekognition.types.orientation_correction

        out["target_image_orientation_correction"] = (
            aws_sdk_rekognition.types.orientation_correction.deserialize_aws_json_1_1(
                data["TargetImageOrientationCorrection"]
            )
        )
    return out
