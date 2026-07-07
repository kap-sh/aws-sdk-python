"""Generated from Smithy shape ``com.amazonaws.wafregional#ListResourcesForWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.resource_id
    import aws_sdk_waf_regional.types.resource_type


class ListResourcesForWebACLRequest(TypedDict, closed=True):
    web_acl_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The unique identifier (ID) of the web ACL for which to list the associated resources.</p>"""
    resource_type: NotRequired["aws_sdk_waf_regional.types.resource_type.ResourceType"]
    """<p>The type of resource to list, either an application load balancer or Amazon API Gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesForWebACLRequest) -> dict:
    out: dict = {}
    out["WebACLId"] = value["web_acl_id"]
    if "resource_type" in value:
        import aws_sdk_waf_regional.types.resource_type

        out["ResourceType"] = (
            aws_sdk_waf_regional.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesForWebACLRequest:
    out: ListResourcesForWebACLRequest = {}  # type: ignore[typeddict-item]
    if "WebACLId" in data:
        out["web_acl_id"] = data["WebACLId"]
    else:
        raise DeserializationError("ListResourcesForWebACLRequest.web_acl_id required")
    if "ResourceType" in data:
        import aws_sdk_waf_regional.types.resource_type

        out["resource_type"] = (
            aws_sdk_waf_regional.types.resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    return out
