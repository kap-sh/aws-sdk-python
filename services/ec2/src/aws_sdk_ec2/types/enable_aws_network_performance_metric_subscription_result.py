"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAwsNetworkPerformanceMetricSubscriptionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class EnableAwsNetworkPerformanceMetricSubscriptionResult(TypedDict):
    output: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the subscribe action was successful.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableAwsNetworkPerformanceMetricSubscriptionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "output" in value:
        pairs.append((f"{prefix}.Output", "true" if value["output"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> EnableAwsNetworkPerformanceMetricSubscriptionResult:
    out: EnableAwsNetworkPerformanceMetricSubscriptionResult = {}  # type: ignore[typeddict-item]
    child_output = el.find("Output")
    if child_output is not None:
        out["output"] = (child_output.text or "").lower() == "true"
    return out
