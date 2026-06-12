"""Generated from Smithy shape ``com.amazonaws.ssm#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_id
    import aws_sdk_ssm.types.resource_type_for_tagging


class ListTagsForResourceRequest(TypedDict):
    resource_type: "aws_sdk_ssm.types.resource_type_for_tagging.ResourceTypeForTagging"
    """<p>Returns a list of tags for a specific resource type.</p>"""
    resource_id: "aws_sdk_ssm.types.resource_id.ResourceId"
    """<p>The resource ID for which you want to see a list of tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.resource_type_for_tagging

    out["ResourceType"] = (
        aws_sdk_ssm.types.resource_type_for_tagging.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import aws_sdk_ssm.types.resource_type_for_tagging

        out["resource_type"] = (
            aws_sdk_ssm.types.resource_type_for_tagging.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_type required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_id required")
    return out
