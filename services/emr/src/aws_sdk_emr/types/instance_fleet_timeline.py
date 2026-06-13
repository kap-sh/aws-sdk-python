"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetTimeline``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.date


class InstanceFleetTimeline(TypedDict):
    creation_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The time and date the instance fleet was created.</p>"""
    ready_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The time and date the instance fleet was ready to run jobs.</p>"""
    end_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The time and date the instance fleet terminated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetTimeline) -> dict:
    out: dict = {}
    if "creation_date_time" in value:
        import aws_sdk_emr.types.date

        out["CreationDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "ready_date_time" in value:
        import aws_sdk_emr.types.date

        out["ReadyDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["ready_date_time"]
        )
    if "end_date_time" in value:
        import aws_sdk_emr.types.date

        out["EndDateTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["end_date_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceFleetTimeline:
    out: InstanceFleetTimeline = {}  # type: ignore[typeddict-item]
    if "CreationDateTime" in data:
        import aws_sdk_emr.types.date

        out["creation_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreationDateTime"]
        )
    if "ReadyDateTime" in data:
        import aws_sdk_emr.types.date

        out["ready_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["ReadyDateTime"]
        )
    if "EndDateTime" in data:
        import aws_sdk_emr.types.date

        out["end_date_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["EndDateTime"]
        )
    return out
