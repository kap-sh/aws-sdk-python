"""Generated from Smithy shape ``com.amazonaws.rekognition#ListFacesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.collection_id
    import aws_sdk_rekognition.types.face_id_list
    import aws_sdk_rekognition.types.page_size
    import aws_sdk_rekognition.types.pagination_token
    import aws_sdk_rekognition.types.user_id


class ListFacesRequest(TypedDict):
    collection_id: "aws_sdk_rekognition.types.collection_id.CollectionId"
    """<p>ID of the collection from which to list the faces.</p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.pagination_token.PaginationToken"
    ]
    """<p>If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of faces.</p>"""
    max_results: NotRequired["aws_sdk_rekognition.types.page_size.PageSize"]
    """<p>Maximum number of faces to return.</p>"""
    user_id: NotRequired["aws_sdk_rekognition.types.user_id.UserId"]
    """<p>An array of user IDs to filter results with when listing faces in a collection.</p>"""
    face_ids: NotRequired["aws_sdk_rekognition.types.face_id_list.FaceIdList"]
    """<p>An array of face IDs to filter results with when listing faces in a collection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFacesRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "face_ids" in value:
        import aws_sdk_rekognition.types.face_id_list

        out["FaceIds"] = aws_sdk_rekognition.types.face_id_list.serialize_aws_json_1_1(
            value["face_ids"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFacesRequest:
    out: ListFacesRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("ListFacesRequest.collection_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "FaceIds" in data:
        import aws_sdk_rekognition.types.face_id_list

        out["face_ids"] = (
            aws_sdk_rekognition.types.face_id_list.deserialize_aws_json_1_1(
                data["FaceIds"]
            )
        )
    return out
