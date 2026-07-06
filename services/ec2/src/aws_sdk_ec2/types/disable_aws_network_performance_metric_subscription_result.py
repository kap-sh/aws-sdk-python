"""Generated from Smithy shape ``com.amazonaws.ec2#DisableAwsNetworkPerformanceMetricSubscriptionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class DisableAwsNetworkPerformanceMetricSubscriptionResult(TypedDict, closed=True):
    output: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the unsubscribe action was successful.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableAwsNetworkPerformanceMetricSubscriptionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "output" in value:
        pairs.append((f"{prefix}.Output", "true" if value["output"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> DisableAwsNetworkPerformanceMetricSubscriptionResult:
    out: DisableAwsNetworkPerformanceMetricSubscriptionResult = {}  # type: ignore[typeddict-item]
    child_output = el.find("Output")
    if child_output is not None:
        out["output"] = (child_output.text or "").lower() == "true"
    return out
