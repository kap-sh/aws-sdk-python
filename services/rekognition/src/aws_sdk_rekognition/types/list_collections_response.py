"""Generated from Smithy shape ``com.amazonaws.rekognition#ListCollectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.collection_id_list
    import aws_sdk_rekognition.types.face_model_version_list
    import aws_sdk_rekognition.types.pagination_token


class ListCollectionsResponse(TypedDict, closed=True):
    collection_ids: NotRequired[
        "aws_sdk_rekognition.types.collection_id_list.CollectionIdList"
    ]
    """<p>An array of collection IDs.</p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.pagination_token.PaginationToken"
    ]
    """<p>If the result is truncated, the response provides a <code>NextToken</code> that you can use in the subsequent request to fetch the next set of collection IDs.</p>"""
    face_model_versions: NotRequired[
        "aws_sdk_rekognition.types.face_model_version_list.FaceModelVersionList"
    ]
    """<p>Version numbers of the face detection models associated with the collections in the array <code>CollectionIds</code>. For example, the value of <code>FaceModelVersions[2]</code> is the version number for the face detection model used by the collection in <code>CollectionId[2]</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCollectionsResponse) -> dict:
    out: dict = {}
    if "collection_ids" in value:
        import aws_sdk_rekognition.types.collection_id_list

        out["CollectionIds"] = (
            aws_sdk_rekognition.types.collection_id_list.serialize_aws_json_1_1(
                value["collection_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "face_model_versions" in value:
        import aws_sdk_rekognition.types.face_model_version_list

        out["FaceModelVersions"] = (
            aws_sdk_rekognition.types.face_model_version_list.serialize_aws_json_1_1(
                value["face_model_versions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCollectionsResponse:
    out: ListCollectionsResponse = {}  # type: ignore[typeddict-item]
    if "CollectionIds" in data:
        import aws_sdk_rekognition.types.collection_id_list

        out["collection_ids"] = (
            aws_sdk_rekognition.types.collection_id_list.deserialize_aws_json_1_1(
                data["CollectionIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "FaceModelVersions" in data:
        import aws_sdk_rekognition.types.face_model_version_list

        out["face_model_versions"] = (
            aws_sdk_rekognition.types.face_model_version_list.deserialize_aws_json_1_1(
                data["FaceModelVersions"]
            )
        )
    return out
