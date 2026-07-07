"""Generated from Smithy shape ``com.amazonaws.ecr#ListImagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_identifier_list
    import aws_sdk_ecr.types.next_token


class ListImagesResponse(TypedDict, closed=True):
    image_ids: NotRequired[
        "aws_sdk_ecr.types.image_identifier_list.ImageIdentifierList"
    ]
    """<p>The list of image IDs for the requested repository.</p>"""
    next_token: NotRequired["aws_sdk_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListImages</code> request. When the results of a <code>ListImages</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImagesResponse) -> dict:
    out: dict = {}
    if "image_ids" in value:
        import aws_sdk_ecr.types.image_identifier_list

        out["imageIds"] = (
            aws_sdk_ecr.types.image_identifier_list.serialize_aws_json_1_1(
                value["image_ids"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImagesResponse:
    out: ListImagesResponse = {}  # type: ignore[typeddict-item]
    if "imageIds" in data:
        import aws_sdk_ecr.types.image_identifier_list

        out["image_ids"] = (
            aws_sdk_ecr.types.image_identifier_list.deserialize_aws_json_1_1(
                data["imageIds"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
