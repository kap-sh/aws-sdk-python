"""Generated from Smithy shape ``com.amazonaws.wafregional#ListResourcesForWebACLResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_arns


class ListResourcesForWebACLResponse(TypedDict, closed=True):
    resource_arns: NotRequired["capo_waf_regional.types.resource_arns.ResourceArns"]
    """<p>An array of ARNs (Amazon Resource Names) of the resources associated with the specified web ACL. An array with zero elements is returned if there are no resources associated with the web ACL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesForWebACLResponse) -> dict:
    out: dict = {}
    if "resource_arns" in value:
        import capo_waf_regional.types.resource_arns

        out["ResourceArns"] = (
            capo_waf_regional.types.resource_arns.serialize_aws_json_1_1(
                value["resource_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesForWebACLResponse:
    out: ListResourcesForWebACLResponse = {}  # type: ignore[typeddict-item]
    if "ResourceArns" in data:
        import capo_waf_regional.types.resource_arns

        out["resource_arns"] = (
            capo_waf_regional.types.resource_arns.deserialize_aws_json_1_1(
                data["ResourceArns"]
            )
        )
    return out
