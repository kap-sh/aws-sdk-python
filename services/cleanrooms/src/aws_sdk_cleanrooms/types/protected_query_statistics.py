"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.billed_resource_utilization


class ProtectedQueryStatistics(TypedDict, closed=True):
    total_duration_in_millis: NotRequired["int"]
    """<p>The duration of the protected query, from creation until query completion, in milliseconds.</p>"""
    billed_resource_utilization: NotRequired[
        "aws_sdk_cleanrooms.types.billed_resource_utilization.BilledResourceUtilization"
    ]
    """<p> The billed resource utilization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryStatistics) -> dict:
    out: dict = {}
    if "total_duration_in_millis" in value:
        out["totalDurationInMillis"] = value["total_duration_in_millis"]
    if "billed_resource_utilization" in value:
        import aws_sdk_cleanrooms.types.billed_resource_utilization

        out["billedResourceUtilization"] = (
            aws_sdk_cleanrooms.types.billed_resource_utilization.serialize_json(
                value["billed_resource_utilization"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProtectedQueryStatistics:
    out: ProtectedQueryStatistics = {}  # type: ignore[typeddict-item]
    if "totalDurationInMillis" in data:
        out["total_duration_in_millis"] = data["totalDurationInMillis"]
    if "billedResourceUtilization" in data:
        import aws_sdk_cleanrooms.types.billed_resource_utilization

        out["billed_resource_utilization"] = (
            aws_sdk_cleanrooms.types.billed_resource_utilization.deserialize_json(
                data["billedResourceUtilization"]
            )
        )
    return out
