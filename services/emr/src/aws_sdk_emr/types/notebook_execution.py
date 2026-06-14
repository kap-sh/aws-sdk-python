"""Generated from Smithy shape ``com.amazonaws.emr#NotebookExecution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.environment_variables_map
    import aws_sdk_emr.types.execution_engine_config
    import aws_sdk_emr.types.notebook_execution_status
    import aws_sdk_emr.types.notebook_s3_location_for_output
    import aws_sdk_emr.types.output_notebook_format
    import aws_sdk_emr.types.output_notebook_s3_location_for_output
    import aws_sdk_emr.types.tag_list
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_max_len256


class NotebookExecution(TypedDict):
    notebook_execution_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The unique identifier of a notebook execution.</p>"""
    editor_id: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The unique identifier of the Amazon EMR Notebook that is used for the notebook execution.</p>"""
    execution_engine: NotRequired[
        "aws_sdk_emr.types.execution_engine_config.ExecutionEngineConfig"
    ]
    """<p>The execution engine, such as an Amazon EMR cluster, used to run the Amazon EMR notebook and perform the notebook execution.</p>"""
    notebook_execution_name: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>A name for the notebook execution.</p>"""
    notebook_params: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>Input parameters in JSON format passed to the Amazon EMR Notebook at runtime for execution.</p>"""
    status: NotRequired[
        "aws_sdk_emr.types.notebook_execution_status.NotebookExecutionStatus"
    ]
    """<p>The status of the notebook execution.</p> <ul> <li> <p> <code>START_PENDING</code> indicates that the cluster has received the execution request but execution has not begun.</p> </li> <li> <p> <code>STARTING</code> indicates that the execution is starting on the cluster.</p> </li> <li> <p> <code>RUNNING</code> indicates that the execution is being processed by the cluster.</p> </li> <li> <p> <code>FINISHING</code> indicates that execution processing is in the final stages.</p> </li> <li> <p> <code>FINISHED</code> indicates that the execution has completed without error.</p> </li> <li> <p> <code>FAILING</code> indicates that the execution is failing and will not finish successfully.</p> </li> <li> <p> <code>FAILED</code> indicates that the execution failed.</p> </li> <li> <p> <code>STOP_PENDING</code> indicates that the cluster has received a <code>StopNotebookExecution</code> request and the stop is pending.</p> </li> <li> <p> <code>STOPPING</code> indicates that the cluster is in the process of stopping the execution as a result of a <code>StopNotebookExecution</code> request.</p> </li> <li> <p> <code>STOPPED</code> indicates that the execution stopped because of a <code>StopNotebookExecution</code> request.</p> </li> </ul>"""
    start_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The timestamp when notebook execution started.</p>"""
    end_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The timestamp when notebook execution ended.</p>"""
    arn: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The Amazon Resource Name (ARN) of the notebook execution.</p>"""
    output_notebook_uri: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The location of the notebook execution's output file in Amazon S3.</p>"""
    last_state_change_reason: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The reason for the latest status change of the notebook execution.</p>"""
    notebook_instance_security_group_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    r"""<p>The unique identifier of the Amazon EC2 security group associated with the Amazon EMR Notebook instance. For more information see <a href=\"https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-security-groups.html\">Specifying Amazon EC2 Security Groups for Amazon EMR Notebooks</a> in the <i>Amazon EMR Management Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_emr.types.tag_list.TagList"]
    """<p>A list of tags associated with a notebook execution. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters and an optional value string with a maximum of 256 characters.</p>"""
    notebook_s3_location: NotRequired[
        "aws_sdk_emr.types.notebook_s3_location_for_output.NotebookS3LocationForOutput"
    ]
    """<p>The Amazon S3 location that stores the notebook execution input.</p>"""
    output_notebook_s3_location: NotRequired[
        "aws_sdk_emr.types.output_notebook_s3_location_for_output.OutputNotebookS3LocationForOutput"
    ]
    """<p>The Amazon S3 location for the notebook execution output.</p>"""
    output_notebook_format: NotRequired[
        "aws_sdk_emr.types.output_notebook_format.OutputNotebookFormat"
    ]
    """<p>The output format for the notebook execution.</p>"""
    environment_variables: NotRequired[
        "aws_sdk_emr.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>The environment variables associated with the notebook execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookExecution) -> dict:
    out: dict = {}
    if "notebook_execution_id" in value:
        out["NotebookExecutionId"] = value["notebook_execution_id"]
    if "editor_id" in value:
        out["EditorId"] = value["editor_id"]
    if "execution_engine" in value:
        import aws_sdk_emr.types.execution_engine_config

        out["ExecutionEngine"] = (
            aws_sdk_emr.types.execution_engine_config.serialize_aws_json_1_1(
                value["execution_engine"]
            )
        )
    if "notebook_execution_name" in value:
        out["NotebookExecutionName"] = value["notebook_execution_name"]
    if "notebook_params" in value:
        out["NotebookParams"] = value["notebook_params"]
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
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "output_notebook_uri" in value:
        out["OutputNotebookURI"] = value["output_notebook_uri"]
    if "last_state_change_reason" in value:
        out["LastStateChangeReason"] = value["last_state_change_reason"]
    if "notebook_instance_security_group_id" in value:
        out["NotebookInstanceSecurityGroupId"] = value[
            "notebook_instance_security_group_id"
        ]
    if "tags" in value:
        import aws_sdk_emr.types.tag_list

        out["Tags"] = aws_sdk_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "notebook_s3_location" in value:
        import aws_sdk_emr.types.notebook_s3_location_for_output

        out["NotebookS3Location"] = (
            aws_sdk_emr.types.notebook_s3_location_for_output.serialize_aws_json_1_1(
                value["notebook_s3_location"]
            )
        )
    if "output_notebook_s3_location" in value:
        import aws_sdk_emr.types.output_notebook_s3_location_for_output

        out["OutputNotebookS3Location"] = (
            aws_sdk_emr.types.output_notebook_s3_location_for_output.serialize_aws_json_1_1(
                value["output_notebook_s3_location"]
            )
        )
    if "output_notebook_format" in value:
        import aws_sdk_emr.types.output_notebook_format

        out["OutputNotebookFormat"] = (
            aws_sdk_emr.types.output_notebook_format.serialize_aws_json_1_1(
                value["output_notebook_format"]
            )
        )
    if "environment_variables" in value:
        import aws_sdk_emr.types.environment_variables_map

        out["EnvironmentVariables"] = (
            aws_sdk_emr.types.environment_variables_map.serialize_aws_json_1_1(
                value["environment_variables"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotebookExecution:
    out: NotebookExecution = {}  # type: ignore[typeddict-item]
    if "NotebookExecutionId" in data:
        out["notebook_execution_id"] = data["NotebookExecutionId"]
    if "EditorId" in data:
        out["editor_id"] = data["EditorId"]
    if "ExecutionEngine" in data:
        import aws_sdk_emr.types.execution_engine_config

        out["execution_engine"] = (
            aws_sdk_emr.types.execution_engine_config.deserialize_aws_json_1_1(
                data["ExecutionEngine"]
            )
        )
    if "NotebookExecutionName" in data:
        out["notebook_execution_name"] = data["NotebookExecutionName"]
    if "NotebookParams" in data:
        out["notebook_params"] = data["NotebookParams"]
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
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "OutputNotebookURI" in data:
        out["output_notebook_uri"] = data["OutputNotebookURI"]
    if "LastStateChangeReason" in data:
        out["last_state_change_reason"] = data["LastStateChangeReason"]
    if "NotebookInstanceSecurityGroupId" in data:
        out["notebook_instance_security_group_id"] = data[
            "NotebookInstanceSecurityGroupId"
        ]
    if "Tags" in data:
        import aws_sdk_emr.types.tag_list

        out["tags"] = aws_sdk_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if "NotebookS3Location" in data:
        import aws_sdk_emr.types.notebook_s3_location_for_output

        out["notebook_s3_location"] = (
            aws_sdk_emr.types.notebook_s3_location_for_output.deserialize_aws_json_1_1(
                data["NotebookS3Location"]
            )
        )
    if "OutputNotebookS3Location" in data:
        import aws_sdk_emr.types.output_notebook_s3_location_for_output

        out["output_notebook_s3_location"] = (
            aws_sdk_emr.types.output_notebook_s3_location_for_output.deserialize_aws_json_1_1(
                data["OutputNotebookS3Location"]
            )
        )
    if "OutputNotebookFormat" in data:
        import aws_sdk_emr.types.output_notebook_format

        out["output_notebook_format"] = (
            aws_sdk_emr.types.output_notebook_format.deserialize_aws_json_1_1(
                data["OutputNotebookFormat"]
            )
        )
    if "EnvironmentVariables" in data:
        import aws_sdk_emr.types.environment_variables_map

        out["environment_variables"] = (
            aws_sdk_emr.types.environment_variables_map.deserialize_aws_json_1_1(
                data["EnvironmentVariables"]
            )
        )
    return out
