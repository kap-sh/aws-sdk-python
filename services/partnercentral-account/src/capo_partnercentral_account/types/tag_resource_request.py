"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.tag_list
    import capo_partnercentral_account.types.taggable_resource_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_partnercentral_account.types.taggable_resource_arn.TaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "capo_partnercentral_account.types.tag_list.TagList"
    """<p>A list of tags to add or update for the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_partnercentral_account.types.tag_list

    out["Tags"] = capo_partnercentral_account.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import capo_partnercentral_account.types.tag_list

        out["tags"] = (
            capo_partnercentral_account.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
