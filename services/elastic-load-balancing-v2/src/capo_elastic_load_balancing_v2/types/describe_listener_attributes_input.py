"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeListenerAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.listener_arn


class DescribeListenerAttributesInput(TypedDict, closed=True):
    listener_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeListenerAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "listener_arn" in value:
        pairs.append((f"{key_prefix}ListenerArn", str(value["listener_arn"])))


def deserialize_query(el: Element) -> DescribeListenerAttributesInput:
    out: DescribeListenerAttributesInput = {}  # type: ignore[typeddict-item]
    child_listener_arn = el.find("ListenerArn")
    if child_listener_arn is not None:
        out["listener_arn"] = str(child_listener_arn.text or "")
    return out
