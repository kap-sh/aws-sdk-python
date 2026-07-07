"""Generated from Smithy shape ``com.amazonaws.wafv2#ListResourcesForWebACLResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.resource_arns


class ListResourcesForWebACLResponse(TypedDict, closed=True):
    resource_arns: NotRequired["aws_sdk_wafv2.types.resource_arns.ResourceArns"]
    """<p>The array of Amazon Resource Names (ARNs) of the associated resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesForWebACLResponse) -> dict:
    out: dict = {}
    if "resource_arns" in value:
        import aws_sdk_wafv2.types.resource_arns

        out["ResourceArns"] = aws_sdk_wafv2.types.resource_arns.serialize_aws_json_1_1(
            value["resource_arns"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesForWebACLResponse:
    out: ListResourcesForWebACLResponse = {}  # type: ignore[typeddict-item]
    if "ResourceArns" in data:
        import aws_sdk_wafv2.types.resource_arns

        out["resource_arns"] = (
            aws_sdk_wafv2.types.resource_arns.deserialize_aws_json_1_1(
                data["ResourceArns"]
            )
        )
    return out
