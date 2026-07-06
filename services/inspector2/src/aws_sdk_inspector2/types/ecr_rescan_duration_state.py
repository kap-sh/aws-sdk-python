"""Generated from Smithy shape ``com.amazonaws.inspector2#EcrRescanDurationState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.date_time_timestamp
    import aws_sdk_inspector2.types.ecr_pull_date_rescan_duration
    import aws_sdk_inspector2.types.ecr_pull_date_rescan_mode
    import aws_sdk_inspector2.types.ecr_rescan_duration
    import aws_sdk_inspector2.types.ecr_rescan_duration_status


class EcrRescanDurationState(TypedDict, closed=True):
    rescan_duration: NotRequired[
        "aws_sdk_inspector2.types.ecr_rescan_duration.EcrRescanDuration"
    ]
    """<p>The rescan duration configured for image push date. </p>"""
    status: NotRequired[
        "aws_sdk_inspector2.types.ecr_rescan_duration_status.EcrRescanDurationStatus"
    ]
    """<p>The status of changes to the ECR automated re-scan duration.</p>"""
    updated_at: NotRequired[
        "aws_sdk_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>A timestamp representing when the last time the ECR scan duration setting was changed.</p>"""
    pull_date_rescan_duration: NotRequired[
        "aws_sdk_inspector2.types.ecr_pull_date_rescan_duration.EcrPullDateRescanDuration"
    ]
    """<p>The rescan duration configured for image pull date.</p>"""
    pull_date_rescan_mode: NotRequired[
        "aws_sdk_inspector2.types.ecr_pull_date_rescan_mode.EcrPullDateRescanMode"
    ]
    """<p>The pull date for the re-scan mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcrRescanDurationState) -> dict:
    out: dict = {}
    if "rescan_duration" in value:
        out["rescanDuration"] = value["rescan_duration"]
    if "status" in value:
        out["status"] = value["status"]
    if "updated_at" in value:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["updatedAt"] = aws_sdk_inspector2.types.date_time_timestamp.serialize_json(
            value["updated_at"]
        )
    if "pull_date_rescan_duration" in value:
        out["pullDateRescanDuration"] = value["pull_date_rescan_duration"]
    if "pull_date_rescan_mode" in value:
        out["pullDateRescanMode"] = value["pull_date_rescan_mode"]
    return out


def deserialize_json(data: dict) -> EcrRescanDurationState:
    out: EcrRescanDurationState = {}  # type: ignore[typeddict-item]
    if "rescanDuration" in data:
        out["rescan_duration"] = data["rescanDuration"]
    if "status" in data:
        out["status"] = data["status"]
    if "updatedAt" in data:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["updated_at"] = (
            aws_sdk_inspector2.types.date_time_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "pullDateRescanDuration" in data:
        out["pull_date_rescan_duration"] = data["pullDateRescanDuration"]
    if "pullDateRescanMode" in data:
        out["pull_date_rescan_mode"] = data["pullDateRescanMode"]
    return out
