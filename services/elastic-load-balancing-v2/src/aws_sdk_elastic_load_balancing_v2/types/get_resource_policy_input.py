"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#GetResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.resource_arn


class GetResourcePolicyInput(TypedDict, closed=True):
    resource_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetResourcePolicyInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))


def deserialize_query(el: Element) -> GetResourcePolicyInput:
    out: GetResourcePolicyInput = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    return out
