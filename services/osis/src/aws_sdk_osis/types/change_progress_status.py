"""Generated from Smithy shape ``com.amazonaws.osis#ChangeProgressStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_osis.types.change_progress_stage_list
    import aws_sdk_osis.types.change_progress_statuses
    import aws_sdk_osis.types.integer
    import aws_sdk_osis.types.timestamp


class ChangeProgressStatus(TypedDict):
    start_time: NotRequired["aws_sdk_osis.types.timestamp.Timestamp"]
    """<p>The time at which the configuration change is made on the pipeline.</p>"""
    status: NotRequired[
        "aws_sdk_osis.types.change_progress_statuses.ChangeProgressStatuses"
    ]
    """<p>The overall status of the pipeline configuration change.</p>"""
    total_number_of_stages: "aws_sdk_osis.types.integer.Integer"
    """<p>The total number of stages required for the pipeline configuration change.</p>"""
    change_progress_stages: NotRequired[
        "aws_sdk_osis.types.change_progress_stage_list.ChangeProgressStageList"
    ]
    """<p>Information about the stages that the pipeline is going through to perform the configuration change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressStatus) -> dict:
    out: dict = {}
    if "start_time" in value:
        import aws_sdk_osis.types.timestamp

        out["StartTime"] = aws_sdk_osis.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "status" in value:
        import aws_sdk_osis.types.change_progress_statuses

        out["Status"] = aws_sdk_osis.types.change_progress_statuses.serialize_json(
            value["status"]
        )
    out["TotalNumberOfStages"] = value.get("total_number_of_stages", 0)
    if "change_progress_stages" in value:
        import aws_sdk_osis.types.change_progress_stage_list

        out["ChangeProgressStages"] = (
            aws_sdk_osis.types.change_progress_stage_list.serialize_json(
                value["change_progress_stages"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChangeProgressStatus:
    out: ChangeProgressStatus = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import aws_sdk_osis.types.timestamp

        out["start_time"] = aws_sdk_osis.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "Status" in data:
        import aws_sdk_osis.types.change_progress_statuses

        out["status"] = aws_sdk_osis.types.change_progress_statuses.deserialize_json(
            data["Status"]
        )
    if "TotalNumberOfStages" in data:
        out["total_number_of_stages"] = data["TotalNumberOfStages"]
    else:
        out["total_number_of_stages"] = 0
    if "ChangeProgressStages" in data:
        import aws_sdk_osis.types.change_progress_stage_list

        out["change_progress_stages"] = (
            aws_sdk_osis.types.change_progress_stage_list.deserialize_json(
                data["ChangeProgressStages"]
            )
        )
    return out
