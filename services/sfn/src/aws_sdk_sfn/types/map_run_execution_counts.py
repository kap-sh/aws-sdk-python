"""Generated from Smithy shape ``com.amazonaws.sfn#MapRunExecutionCounts``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sfn.types.long_object
    import aws_sdk_sfn.types.unsigned_long


class MapRunExecutionCounts(TypedDict):
    pending: "aws_sdk_sfn.types.unsigned_long.UnsignedLong"
    """<p>The total number of child workflow executions that were started by a Map Run, but haven't started executing yet. </p>"""
    running: "aws_sdk_sfn.types.unsigned_long.UnsignedLong"
    """<p>The total number of child workflow executions that were started by a Map Run and are currently in-progress.</p>"""
    succeeded: "aws_sdk_sfn.types.unsigned_long.UnsignedLong"
    """<p>The total number of child workflow executions that were started by a Map Run and have completed successfully.</p>"""
    failed: "aws_sdk_sfn.types.unsigned_long.UnsignedLong"
    """<p>The total number of child workflow executions that were started by a Map Run, but have failed.</p>"""
    timed_out: "aws_sdk_sfn.types.unsigned_long.UnsignedLong"
    """<p>The total number of child workflow executions that were started by a Map Run and have timed out.</p>"""
    aborted: "aws_sdk_sfn.types.unsigned_long.UnsignedLong"
    """<p>The total number of child workflow executions that were started by a Map Run and were running, but were either stopped by the user or by Step Functions because the Map Run failed. </p>"""
    total: "aws_sdk_sfn.types.unsigned_long.UnsignedLong"
    """<p>The total number of child workflow executions that were started by a Map Run.</p>"""
    results_written: "aws_sdk_sfn.types.unsigned_long.UnsignedLong"
    r"""<p>Returns the count of child workflow executions whose results were written by <code>ResultWriter</code>. For more information, see <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultwriter.html\">ResultWriter</a> in the <i>Step Functions Developer Guide</i>.</p>"""
    failures_not_redrivable: NotRequired["aws_sdk_sfn.types.long_object.LongObject"]
    """<p>The number of <code>FAILED</code>, <code>ABORTED</code>, or <code>TIMED_OUT</code> child workflow executions that cannot be redriven because their execution status is terminal. For example, child workflows with an execution status of <code>FAILED</code>, <code>ABORTED</code>, or <code>TIMED_OUT</code> and a <code>redriveStatus</code> of <code>NOT_REDRIVABLE</code>.</p>"""
    pending_redrive: NotRequired["aws_sdk_sfn.types.long_object.LongObject"]
    """<p>The number of unsuccessful child workflow executions currently waiting to be redriven. The status of these child workflow executions could be <code>FAILED</code>, <code>ABORTED</code>, or <code>TIMED_OUT</code> in the original execution attempt or a previous redrive attempt.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MapRunExecutionCounts) -> dict:
    out: dict = {}
    out["pending"] = value.get("pending", 0)
    out["running"] = value.get("running", 0)
    out["succeeded"] = value.get("succeeded", 0)
    out["failed"] = value.get("failed", 0)
    out["timedOut"] = value.get("timed_out", 0)
    out["aborted"] = value.get("aborted", 0)
    out["total"] = value.get("total", 0)
    out["resultsWritten"] = value.get("results_written", 0)
    if "failures_not_redrivable" in value:
        out["failuresNotRedrivable"] = value["failures_not_redrivable"]
    if "pending_redrive" in value:
        out["pendingRedrive"] = value["pending_redrive"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MapRunExecutionCounts:
    out: MapRunExecutionCounts = {}  # type: ignore[typeddict-item]
    if "pending" in data:
        out["pending"] = data["pending"]
    else:
        out["pending"] = 0
    if "running" in data:
        out["running"] = data["running"]
    else:
        out["running"] = 0
    if "succeeded" in data:
        out["succeeded"] = data["succeeded"]
    else:
        out["succeeded"] = 0
    if "failed" in data:
        out["failed"] = data["failed"]
    else:
        out["failed"] = 0
    if "timedOut" in data:
        out["timed_out"] = data["timedOut"]
    else:
        out["timed_out"] = 0
    if "aborted" in data:
        out["aborted"] = data["aborted"]
    else:
        out["aborted"] = 0
    if "total" in data:
        out["total"] = data["total"]
    else:
        out["total"] = 0
    if "resultsWritten" in data:
        out["results_written"] = data["resultsWritten"]
    else:
        out["results_written"] = 0
    if "failuresNotRedrivable" in data:
        out["failures_not_redrivable"] = data["failuresNotRedrivable"]
    if "pendingRedrive" in data:
        out["pending_redrive"] = data["pendingRedrive"]
    return out
