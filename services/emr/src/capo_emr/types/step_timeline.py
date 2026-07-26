"""Generated from Smithy shape ``com.amazonaws.emr#StepTimeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.date


class StepTimeline(TypedDict, closed=True):
    creation_date_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The date and time when the cluster step was created.</p>"""
    start_date_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The date and time when the cluster step execution started.</p>"""
    end_date_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The date and time when the cluster step execution completed or failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepTimeline) -> dict:
    out: dict = {}
    if "creation_date_time" in value:
        import capo_emr.types.date

        out["CreationDateTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "start_date_time" in value:
        import capo_emr.types.date

        out["StartDateTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["start_date_time"]
        )
    if "end_date_time" in value:
        import capo_emr.types.date

        out["EndDateTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["end_date_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepTimeline:
    out: StepTimeline = {}  # type: ignore[typeddict-item]
    if "CreationDateTime" in data:
        import capo_emr.types.date

        out["creation_date_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["CreationDateTime"]
        )
    if "StartDateTime" in data:
        import capo_emr.types.date

        out["start_date_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["StartDateTime"]
        )
    if "EndDateTime" in data:
        import capo_emr.types.date

        out["end_date_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["EndDateTime"]
        )
    return out
