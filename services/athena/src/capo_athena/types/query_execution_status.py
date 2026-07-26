"""Generated from Smithy shape ``com.amazonaws.athena#QueryExecutionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.athena_error
    import capo_athena.types.date
    import capo_athena.types.query_execution_state
    import capo_athena.types.string


class QueryExecutionStatus(TypedDict, closed=True):
    state: NotRequired["capo_athena.types.query_execution_state.QueryExecutionState"]
    """<p>The state of query execution. <code>QUEUED</code> indicates that the query has been submitted to the service, and Athena will execute the query as soon as resources are available. <code>RUNNING</code> indicates that the query is in execution phase. <code>SUCCEEDED</code> indicates that the query completed without errors. <code>FAILED</code> indicates that the query experienced an error and did not complete processing. <code>CANCELLED</code> indicates that a user input interrupted query execution.</p> <note> <p>For queries that experience certain transient errors, the state transitions from <code>RUNNING</code> back to <code>QUEUED</code>. The <code>FAILED</code> state is always terminal with no automatic retry. </p> </note>"""
    state_change_reason: NotRequired["capo_athena.types.string.String"]
    """<p>Further detail about the status of the query.</p>"""
    submission_date_time: NotRequired["capo_athena.types.date.Date"]
    """<p>The date and time that the query was submitted.</p>"""
    completion_date_time: NotRequired["capo_athena.types.date.Date"]
    """<p>The date and time that the query completed.</p>"""
    athena_error: NotRequired["capo_athena.types.athena_error.AthenaError"]
    """<p>Provides information about an Athena query error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryExecutionStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_athena.types.query_execution_state

        out["State"] = capo_athena.types.query_execution_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_change_reason" in value:
        out["StateChangeReason"] = value["state_change_reason"]
    if "submission_date_time" in value:
        import capo_athena.types.date

        out["SubmissionDateTime"] = capo_athena.types.date.serialize_aws_json_1_1(
            value["submission_date_time"]
        )
    if "completion_date_time" in value:
        import capo_athena.types.date

        out["CompletionDateTime"] = capo_athena.types.date.serialize_aws_json_1_1(
            value["completion_date_time"]
        )
    if "athena_error" in value:
        import capo_athena.types.athena_error

        out["AthenaError"] = capo_athena.types.athena_error.serialize_aws_json_1_1(
            value["athena_error"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryExecutionStatus:
    out: QueryExecutionStatus = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import capo_athena.types.query_execution_state

        out["state"] = capo_athena.types.query_execution_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateChangeReason" in data:
        out["state_change_reason"] = data["StateChangeReason"]
    if "SubmissionDateTime" in data:
        import capo_athena.types.date

        out["submission_date_time"] = capo_athena.types.date.deserialize_aws_json_1_1(
            data["SubmissionDateTime"]
        )
    if "CompletionDateTime" in data:
        import capo_athena.types.date

        out["completion_date_time"] = capo_athena.types.date.deserialize_aws_json_1_1(
            data["CompletionDateTime"]
        )
    if "AthenaError" in data:
        import capo_athena.types.athena_error

        out["athena_error"] = capo_athena.types.athena_error.deserialize_aws_json_1_1(
            data["AthenaError"]
        )
    return out
