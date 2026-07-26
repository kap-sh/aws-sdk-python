"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelIterationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.timestamp


class FlywheelIterationFilter(TypedDict, closed=True):
    creation_time_after: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Filter the flywheel iterations to include iterations created after the specified time.</p>"""
    creation_time_before: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Filter the flywheel iterations to include iterations created before the specified time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelIterationFilter) -> dict:
    out: dict = {}
    if "creation_time_after" in value:
        import capo_comprehend.types.timestamp

        out["CreationTimeAfter"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import capo_comprehend.types.timestamp

        out["CreationTimeBefore"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FlywheelIterationFilter:
    out: FlywheelIterationFilter = {}  # type: ignore[typeddict-item]
    if "CreationTimeAfter" in data:
        import capo_comprehend.types.timestamp

        out["creation_time_after"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import capo_comprehend.types.timestamp

        out["creation_time_before"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    return out
