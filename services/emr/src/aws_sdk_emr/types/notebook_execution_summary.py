"""Generated from Smithy shape ``com.amazonaws.emr#NotebookExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.notebook_execution_status
    import aws_sdk_emr.types.notebook_s3_location_for_output
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_max_len256


class NotebookExecutionSummary(TypedDict, closed=True):
    notebook_execution_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The unique identifier of the notebook execution.</p>"""
    editor_id: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The unique identifier of the editor associated with the notebook execution.</p>"""
    notebook_execution_name: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The name of the notebook execution.</p>"""
    status: NotRequired[
        "aws_sdk_emr.types.notebook_execution_status.NotebookExecutionStatus"
    ]
    """<p>The status of the notebook execution.</p> <ul> <li> <p> <code>START_PENDING</code> indicates that the cluster has received the execution request but execution has not begun.</p> </li> <li> <p> <code>STARTING</code> indicates that the execution is starting on the cluster.</p> </li> <li> <p> <code>RUNNING</code> indicates that the execution is being processed by the cluster.</p> </li> <li> <p> <code>FINISHING</code> indicates that execution processing is in the final stages.</p> </li> <li> <p> <code>FINISHED</code> indicates that the execution has completed without error.</p> </li> <li> <p> <code>FAILING</code> indicates that the execution is failing and will not finish successfully.</p> </li> <li> <p> <code>FAILED</code> indicates that the execution failed.</p> </li> <li> <p> <code>STOP_PENDING</code> indicates that the cluster has received a <code>StopNotebookExecution</code> request and the stop is pending.</p> </li> <li> <p> <code>STOPPING</code> indicates that the cluster is in the process of stopping the execution as a result of a <code>StopNotebookExecution</code> request.</p> </li> <li> <p> <code>STOPPED</code> indicates that the execution stopped because of a <code>StopNotebookExecution</code> request.</p> </li> </ul>"""
    start_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The timestamp when notebook execution started.</p>"""
    end_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The timestamp when notebook execution started.</p>"""
    notebook_s3_location: NotRequired[
        "aws_sdk_emr.types.notebook_s3_location_for_output.NotebookS3LocationForOutput"
    ]
    """<p>The Amazon S3 location that stores the notebook execution input.</p>"""
    execution_engine_id: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The unique ID of the execution engine for the notebook execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookExecutionSummary) -> dict:
    out: dict = {}
    if "notebook_execution_id" in value:
        out["NotebookExecutionId"] = value["notebook_execution_id"]
    if "editor_id" in value:
        out["EditorId"] = value["editor_id"]
    if "notebook_execution_name" in value:
        out["NotebookExecutionName"] = value["notebook_execution_name"]
    if "status" in value:
        import aws_sdk_emr.types.notebook_execution_status

        out["Status"] = (
            aws_sdk_emr.types.notebook_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "start_time" in value:
        import aws_sdk_emr.types.date

        out["StartTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_emr.types.date

        out["EndTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "notebook_s3_location" in value:
        import aws_sdk_emr.types.notebook_s3_location_for_output

        out["NotebookS3Location"] = (
            aws_sdk_emr.types.notebook_s3_location_for_output.serialize_aws_json_1_1(
                value["notebook_s3_location"]
            )
        )
    if "execution_engine_id" in value:
        out["ExecutionEngineId"] = value["execution_engine_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotebookExecutionSummary:
    out: NotebookExecutionSummary = {}  # type: ignore[typeddict-item]
    if "NotebookExecutionId" in data:
        out["notebook_execution_id"] = data["NotebookExecutionId"]
    if "EditorId" in data:
        out["editor_id"] = data["EditorId"]
    if "NotebookExecutionName" in data:
        out["notebook_execution_name"] = data["NotebookExecutionName"]
    if "Status" in data:
        import aws_sdk_emr.types.notebook_execution_status

        out["status"] = (
            aws_sdk_emr.types.notebook_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_emr.types.date

        out["start_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_emr.types.date

        out["end_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "NotebookS3Location" in data:
        import aws_sdk_emr.types.notebook_s3_location_for_output

        out["notebook_s3_location"] = (
            aws_sdk_emr.types.notebook_s3_location_for_output.deserialize_aws_json_1_1(
                data["NotebookS3Location"]
            )
        )
    if "ExecutionEngineId" in data:
        out["execution_engine_id"] = data["ExecutionEngineId"]
    return out
