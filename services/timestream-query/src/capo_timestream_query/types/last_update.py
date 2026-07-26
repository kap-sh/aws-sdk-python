"""Generated from Smithy shape ``com.amazonaws.timestreamquery#LastUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.last_update_status
    import capo_timestream_query.types.query_tcu
    import capo_timestream_query.types.string


class LastUpdate(TypedDict, closed=True):
    target_query_tcu: NotRequired["capo_timestream_query.types.query_tcu.QueryTCU"]
    """<p>The number of TimeStream Compute Units (TCUs) requested in the last account settings update.</p>"""
    status: NotRequired[
        "capo_timestream_query.types.last_update_status.LastUpdateStatus"
    ]
    """<p>The status of the last update. Can be either <code>PENDING</code>, <code>FAILED</code>, or <code>SUCCEEDED</code>.</p>"""
    status_message: NotRequired["capo_timestream_query.types.string.String"]
    """<p>Error message describing the last account settings update status, visible only if an error occurred.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LastUpdate) -> dict:
    out: dict = {}
    if "target_query_tcu" in value:
        out["TargetQueryTCU"] = value["target_query_tcu"]
    if "status" in value:
        import capo_timestream_query.types.last_update_status

        out["Status"] = (
            capo_timestream_query.types.last_update_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LastUpdate:
    out: LastUpdate = {}  # type: ignore[typeddict-item]
    if "TargetQueryTCU" in data:
        out["target_query_tcu"] = data["TargetQueryTCU"]
    if "Status" in data:
        import capo_timestream_query.types.last_update_status

        out["status"] = (
            capo_timestream_query.types.last_update_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
