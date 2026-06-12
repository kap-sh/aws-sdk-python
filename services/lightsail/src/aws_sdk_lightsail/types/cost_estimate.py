"""Generated from Smithy shape ``com.amazonaws.lightsail#CostEstimate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.estimates_by_time
    import aws_sdk_lightsail.types.non_empty_string


class CostEstimate(TypedDict):
    usage_type: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The types of usage that are included in the estimate, such as costs, usage, or data transfer.</p>"""
    results_by_time: NotRequired[
        "aws_sdk_lightsail.types.estimates_by_time.EstimatesByTime"
    ]
    """<p>The cost estimate result that's associated with a time period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostEstimate) -> dict:
    out: dict = {}
    if "usage_type" in value:
        out["usageType"] = value["usage_type"]
    if "results_by_time" in value:
        import aws_sdk_lightsail.types.estimates_by_time

        out["resultsByTime"] = (
            aws_sdk_lightsail.types.estimates_by_time.serialize_aws_json_1_1(
                value["results_by_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostEstimate:
    out: CostEstimate = {}  # type: ignore[typeddict-item]
    if "usageType" in data:
        out["usage_type"] = data["usageType"]
    if "resultsByTime" in data:
        import aws_sdk_lightsail.types.estimates_by_time

        out["results_by_time"] = (
            aws_sdk_lightsail.types.estimates_by_time.deserialize_aws_json_1_1(
                data["resultsByTime"]
            )
        )
    return out
