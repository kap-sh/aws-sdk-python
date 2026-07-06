"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Milestone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.milestone_name
    import aws_sdk_wellarchitected.types.milestone_number
    import aws_sdk_wellarchitected.types.timestamp
    import aws_sdk_wellarchitected.types.workload


class Milestone(TypedDict, closed=True):
    milestone_number: NotRequired[
        "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
    ]
    milestone_name: NotRequired[
        "aws_sdk_wellarchitected.types.milestone_name.MilestoneName"
    ]
    recorded_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    workload: NotRequired["aws_sdk_wellarchitected.types.workload.Workload"]


# --- restJson1 ser/de ---
def serialize_json(value: Milestone) -> dict:
    out: dict = {}
    if "milestone_number" in value:
        out["MilestoneNumber"] = value["milestone_number"]
    if "milestone_name" in value:
        out["MilestoneName"] = value["milestone_name"]
    if "recorded_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["RecordedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["recorded_at"]
        )
    if "workload" in value:
        import aws_sdk_wellarchitected.types.workload

        out["Workload"] = aws_sdk_wellarchitected.types.workload.serialize_json(
            value["workload"]
        )
    return out


def deserialize_json(data: dict) -> Milestone:
    out: Milestone = {}  # type: ignore[typeddict-item]
    if "MilestoneNumber" in data:
        out["milestone_number"] = data["MilestoneNumber"]
    if "MilestoneName" in data:
        out["milestone_name"] = data["MilestoneName"]
    if "RecordedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["recorded_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["RecordedAt"]
        )
    if "Workload" in data:
        import aws_sdk_wellarchitected.types.workload

        out["workload"] = aws_sdk_wellarchitected.types.workload.deserialize_json(
            data["Workload"]
        )
    return out
