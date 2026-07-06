"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.tag_list
    import aws_sdk_partnercentral_account.types.taggable_resource_arn


class ListTagsForResourceResponse(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_partnercentral_account.types.taggable_resource_arn.TaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource that the tags are associated with.</p>"""
    tags: NotRequired["aws_sdk_partnercentral_account.types.tag_list.TagList"]
    """<p>A list of tags associated with the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import aws_sdk_partnercentral_account.types.tag_list

        out["Tags"] = (
            aws_sdk_partnercentral_account.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceResponse.resource_arn required")
    if "Tags" in data:
        import aws_sdk_partnercentral_account.types.tag_list

        out["tags"] = (
            aws_sdk_partnercentral_account.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
