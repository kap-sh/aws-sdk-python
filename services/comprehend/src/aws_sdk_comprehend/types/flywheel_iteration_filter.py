"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelIterationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.timestamp


class FlywheelIterationFilter(TypedDict, closed=True):
    creation_time_after: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Filter the flywheel iterations to include iterations created after the specified time.</p>"""
    creation_time_before: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Filter the flywheel iterations to include iterations created before the specified time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelIterationFilter) -> dict:
    out: dict = {}
    if "creation_time_after" in value:
        import aws_sdk_comprehend.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_comprehend.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FlywheelIterationFilter:
    out: FlywheelIterationFilter = {}  # type: ignore[typeddict-item]
    if "CreationTimeAfter" in data:
        import aws_sdk_comprehend.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_comprehend.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    return out
