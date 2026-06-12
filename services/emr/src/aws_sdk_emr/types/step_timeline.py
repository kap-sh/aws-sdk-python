"""Generated from Smithy shape ``com.amazonaws.emr#StepTimeline``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.date


class StepTimeline(TypedDict):
    creation_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time when the cluster step was created.</p>"""
    start_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time when the cluster step execution started.</p>"""
    end_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time when the cluster step execution completed or failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepTimeline) -> dict:
    out: dict = {}
    if "creation_date_time" in value:
        import aws_sdk_emr.types.date

        out["CreationDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "start_date_time" in value:
        import aws_sdk_emr.types.date

        out["StartDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["start_date_time"]
        )
    if "end_date_time" in value:
        import aws_sdk_emr.types.date

        out["EndDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["end_date_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepTimeline:
    out: StepTimeline = {}  # type: ignore[typeddict-item]
    if "CreationDateTime" in data:
        import aws_sdk_emr.types.date

        out["creation_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreationDateTime"]
        )
    if "StartDateTime" in data:
        import aws_sdk_emr.types.date

        out["start_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["StartDateTime"]
        )
    if "EndDateTime" in data:
        import aws_sdk_emr.types.date

        out["end_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["EndDateTime"]
        )
    return out
