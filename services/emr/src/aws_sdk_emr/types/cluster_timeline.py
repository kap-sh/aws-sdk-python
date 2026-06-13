"""Generated from Smithy shape ``com.amazonaws.emr#ClusterTimeline``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.date


class ClusterTimeline(TypedDict):
    creation_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The creation date and time of the cluster.</p>"""
    ready_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time when the cluster was ready to run steps.</p>"""
    end_date_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The date and time when the cluster was terminated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterTimeline) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ClusterTimeline:
    out: ClusterTimeline = {}  # type: ignore[typeddict-item]
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
