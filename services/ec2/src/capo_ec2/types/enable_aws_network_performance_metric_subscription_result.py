"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAwsNetworkPerformanceMetricSubscriptionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class EnableAwsNetworkPerformanceMetricSubscriptionResult(TypedDict, closed=True):
    output: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the subscribe action was successful.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableAwsNetworkPerformanceMetricSubscriptionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "output" in value:
        pairs.append((f"{key_prefix}Output", "true" if value["output"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> EnableAwsNetworkPerformanceMetricSubscriptionResult:
    out: EnableAwsNetworkPerformanceMetricSubscriptionResult = {}  # type: ignore[typeddict-item]
    child_output = el.find("Output")
    if child_output is not None:
        out["output"] = (child_output.text or "").lower() == "true"
    return out
