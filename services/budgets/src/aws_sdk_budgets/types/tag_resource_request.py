"""Generated from Smithy shape ``com.amazonaws.budgets#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.amazon_resource_name
    import aws_sdk_budgets.types.resource_tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_budgets.types.amazon_resource_name.AmazonResourceName"
    """<p>The unique identifier for the resource.</p>"""
    resource_tags: "aws_sdk_budgets.types.resource_tag_list.ResourceTagList"
    """<p>The tags associated with the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_budgets.types.resource_tag_list

    out["ResourceTags"] = (
        aws_sdk_budgets.types.resource_tag_list.serialize_aws_json_1_1(
            value["resource_tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "ResourceTags" in data:
        import aws_sdk_budgets.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_budgets.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.resource_tags required")
    return out
