"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.flywheel_status
    import capo_comprehend.types.timestamp


class FlywheelFilter(TypedDict, closed=True):
    status: NotRequired["capo_comprehend.types.flywheel_status.FlywheelStatus"]
    """<p>Filter the flywheels based on the flywheel status.</p>"""
    creation_time_after: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Filter the flywheels to include flywheels created after the specified time.</p>"""
    creation_time_before: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Filter the flywheels to include flywheels created before the specified time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_comprehend.types.flywheel_status

        out["Status"] = capo_comprehend.types.flywheel_status.serialize_aws_json_1_1(
            value["status"]
        )
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


def deserialize_aws_json_1_1(data: dict) -> FlywheelFilter:
    out: FlywheelFilter = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_comprehend.types.flywheel_status

        out["status"] = capo_comprehend.types.flywheel_status.deserialize_aws_json_1_1(
            data["Status"]
        )
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
