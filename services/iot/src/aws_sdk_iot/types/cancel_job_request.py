"""Generated from Smithy shape ``com.amazonaws.iot#CancelJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.comment
    import aws_sdk_iot.types.force_flag
    import aws_sdk_iot.types.job_id
    import aws_sdk_iot.types.reason_code


class CancelJobRequest(TypedDict):
    job_id: "aws_sdk_iot.types.job_id.JobId"
    """<p>The unique identifier you assigned to this job when it was created.</p>"""
    reason_code: NotRequired["aws_sdk_iot.types.reason_code.ReasonCode"]
    """<p>(Optional)A reason code string that explains why the job was canceled.</p>"""
    comment: NotRequired["aws_sdk_iot.types.comment.Comment"]
    """<p>An optional comment string describing why the job was canceled.</p>"""
    force: "aws_sdk_iot.types.force_flag.ForceFlag"
    r"""<p>(Optional) If <code>true</code> job executions with status \"IN_PROGRESS\" and \"QUEUED\" are canceled, otherwise only job executions with status \"QUEUED\" are canceled. The default is <code>false</code>.</p> <p>Canceling a job which is \"IN_PROGRESS\", will cause a device which is executing the job to be unable to update the job execution status. Use caution and ensure that each device executing a job which is canceled is able to recover to a valid state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRequest) -> dict:
    out: dict = {}
    if "reason_code" in value:
        out["reasonCode"] = value["reason_code"]
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> CancelJobRequest:
    out: CancelJobRequest = {}  # type: ignore[typeddict-item]
    if "reasonCode" in data:
        out["reason_code"] = data["reasonCode"]
    if "comment" in data:
        out["comment"] = data["comment"]
    return out
