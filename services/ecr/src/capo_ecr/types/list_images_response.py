"""Generated from Smithy shape ``com.amazonaws.ecr#ListImagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier_list
    import capo_ecr.types.next_token


class ListImagesResponse(TypedDict, closed=True):
    image_ids: NotRequired["capo_ecr.types.image_identifier_list.ImageIdentifierList"]
    """<p>The list of image IDs for the requested repository.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListImages</code> request. When the results of a <code>ListImages</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImagesResponse) -> dict:
    out: dict = {}
    if "image_ids" in value:
        import capo_ecr.types.image_identifier_list

        out["imageIds"] = capo_ecr.types.image_identifier_list.serialize_aws_json_1_1(
            value["image_ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImagesResponse:
    out: ListImagesResponse = {}  # type: ignore[typeddict-item]
    if data.get("imageIds") is not None:
        import capo_ecr.types.image_identifier_list

        out["image_ids"] = (
            capo_ecr.types.image_identifier_list.deserialize_aws_json_1_1(
                data["imageIds"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
