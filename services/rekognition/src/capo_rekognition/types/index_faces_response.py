"""Generated from Smithy shape ``com.amazonaws.rekognition#IndexFacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.face_record_list
    import capo_rekognition.types.orientation_correction
    import capo_rekognition.types.string
    import capo_rekognition.types.unindexed_faces


class IndexFacesResponse(TypedDict, closed=True):
    face_records: NotRequired["capo_rekognition.types.face_record_list.FaceRecordList"]
    """<p>An array of faces detected and added to the collection. For more information, see Searching Faces in a Collection in the Amazon Rekognition Developer Guide. </p>"""
    orientation_correction: NotRequired[
        "capo_rekognition.types.orientation_correction.OrientationCorrection"
    ]
    """<p>If your collection is associated with a face detection model that's later than version 3.0, the value of <code>OrientationCorrection</code> is always null and no orientation information is returned.</p> <p>If your collection is associated with a face detection model that's version 3.0 or earlier, the following applies:</p> <ul> <li> <p>If the input image is in .jpeg format, it might contain exchangeable image file format (Exif) metadata that includes the image's orientation. Amazon Rekognition uses this orientation information to perform image correction - the bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation. Images in .png format don't contain Exif metadata. The value of <code>OrientationCorrection</code> is null.</p> </li> <li> <p>If the image doesn't contain orientation information in its Exif metadata, Amazon Rekognition returns an estimated orientation (ROTATE_0, ROTATE_90, ROTATE_180, ROTATE_270). Amazon Rekognition doesn’t perform image correction for images. The bounding box coordinates aren't translated and represent the object locations before the image is rotated.</p> </li> </ul> <p>Bounding box information is returned in the <code>FaceRecords</code> array. You can get the version of the face detection model by calling <a>DescribeCollection</a>. </p>"""
    face_model_version: NotRequired["capo_rekognition.types.string.String"]
    """<p>The version number of the face detection model that's associated with the input collection (<code>CollectionId</code>).</p>"""
    unindexed_faces: NotRequired[
        "capo_rekognition.types.unindexed_faces.UnindexedFaces"
    ]
    """<p>An array of faces that were detected in the image but weren't indexed. They weren't indexed because the quality filter identified them as low quality, or the <code>MaxFaces</code> request parameter filtered them out. To use the quality filter, you specify the <code>QualityFilter</code> request parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexFacesResponse) -> dict:
    out: dict = {}
    if "face_records" in value:
        import capo_rekognition.types.face_record_list

        out["FaceRecords"] = (
            capo_rekognition.types.face_record_list.serialize_aws_json_1_1(
                value["face_records"]
            )
        )
    if "orientation_correction" in value:
        import capo_rekognition.types.orientation_correction

        out["OrientationCorrection"] = (
            capo_rekognition.types.orientation_correction.serialize_aws_json_1_1(
                value["orientation_correction"]
            )
        )
    if "face_model_version" in value:
        out["FaceModelVersion"] = value["face_model_version"]
    if "unindexed_faces" in value:
        import capo_rekognition.types.unindexed_faces

        out["UnindexedFaces"] = (
            capo_rekognition.types.unindexed_faces.serialize_aws_json_1_1(
                value["unindexed_faces"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IndexFacesResponse:
    out: IndexFacesResponse = {}  # type: ignore[typeddict-item]
    if "FaceRecords" in data:
        import capo_rekognition.types.face_record_list

        out["face_records"] = (
            capo_rekognition.types.face_record_list.deserialize_aws_json_1_1(
                data["FaceRecords"]
            )
        )
    if "OrientationCorrection" in data:
        import capo_rekognition.types.orientation_correction

        out["orientation_correction"] = (
            capo_rekognition.types.orientation_correction.deserialize_aws_json_1_1(
                data["OrientationCorrection"]
            )
        )
    if "FaceModelVersion" in data:
        out["face_model_version"] = data["FaceModelVersion"]
    if "UnindexedFaces" in data:
        import capo_rekognition.types.unindexed_faces

        out["unindexed_faces"] = (
            capo_rekognition.types.unindexed_faces.deserialize_aws_json_1_1(
                data["UnindexedFaces"]
            )
        )
    return out
