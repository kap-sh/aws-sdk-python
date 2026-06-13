"""Generated from Smithy shape ``com.amazonaws.emr#StartNotebookExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.environment_variables_map
    import aws_sdk_emr.types.execution_engine_config
    import aws_sdk_emr.types.notebook_s3_location_from_input
    import aws_sdk_emr.types.output_notebook_format
    import aws_sdk_emr.types.output_notebook_s3_location_from_input
    import aws_sdk_emr.types.tag_list
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_max_len256


class StartNotebookExecutionInput(TypedDict):
    editor_id: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The unique identifier of the Amazon EMR Notebook to use for notebook execution.</p>"""
    relative_path: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The path and file name of the notebook file for this execution, relative to the path specified for the Amazon EMR Notebook. For example, if you specify a path of <code>s3://MyBucket/MyNotebooks</code> when you create an Amazon EMR Notebook for a notebook with an ID of <code>e-ABCDEFGHIJK1234567890ABCD</code> (the <code>EditorID</code> of this request), and you specify a <code>RelativePath</code> of <code>my_notebook_executions/notebook_execution.ipynb</code>, the location of the file for the notebook execution is <code>s3://MyBucket/MyNotebooks/e-ABCDEFGHIJK1234567890ABCD/my_notebook_executions/notebook_execution.ipynb</code>.</p>"""
    notebook_execution_name: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>An optional name for the notebook execution.</p>"""
    notebook_params: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>Input parameters in JSON format passed to the Amazon EMR Notebook at runtime for execution.</p>"""
    execution_engine: NotRequired[
        "aws_sdk_emr.types.execution_engine_config.ExecutionEngineConfig"
    ]
    """<p>Specifies the execution engine (cluster) that runs the notebook execution.</p>"""
    service_role: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The name or ARN of the IAM role that is used as the service role for Amazon EMR (the Amazon EMR role) for the notebook execution.</p>"""
    notebook_instance_security_group_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The unique identifier of the Amazon EC2 security group to associate with the Amazon EMR Notebook for this notebook execution.</p>"""
    tags: NotRequired["aws_sdk_emr.types.tag_list.TagList"]
    """<p>A list of tags associated with a notebook execution. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters and an optional value string with a maximum of 256 characters.</p>"""
    notebook_s3_location: NotRequired[
        "aws_sdk_emr.types.notebook_s3_location_from_input.NotebookS3LocationFromInput"
    ]
    """<p>The Amazon S3 location for the notebook execution input.</p>"""
    output_notebook_s3_location: NotRequired[
        "aws_sdk_emr.types.output_notebook_s3_location_from_input.OutputNotebookS3LocationFromInput"
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
def serialize_aws_json_1_1(value: StartNotebookExecutionInput) -> dict:
    out: dict = {}
    if "editor_id" in value:
        out["EditorId"] = value["editor_id"]
    if "relative_path" in value:
        out["RelativePath"] = value["relative_path"]
    if "notebook_execution_name" in value:
        out["NotebookExecutionName"] = value["notebook_execution_name"]
    if "notebook_params" in value:
        out["NotebookParams"] = value["notebook_params"]
    if "execution_engine" in value:
        import aws_sdk_emr.types.execution_engine_config

        out["ExecutionEngine"] = (
            aws_sdk_emr.types.execution_engine_config.serialize_aws_json_1_1(
                value["execution_engine"]
            )
        )
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "notebook_instance_security_group_id" in value:
        out["NotebookInstanceSecurityGroupId"] = value[
            "notebook_instance_security_group_id"
        ]
    if "tags" in value:
        import aws_sdk_emr.types.tag_list

        out["Tags"] = aws_sdk_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "notebook_s3_location" in value:
        import aws_sdk_emr.types.notebook_s3_location_from_input

        out["NotebookS3Location"] = (
            aws_sdk_emr.types.notebook_s3_location_from_input.serialize_aws_json_1_1(
                value["notebook_s3_location"]
            )
        )
    if "output_notebook_s3_location" in value:
        import aws_sdk_emr.types.output_notebook_s3_location_from_input

        out["OutputNotebookS3Location"] = (
            aws_sdk_emr.types.output_notebook_s3_location_from_input.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> StartNotebookExecutionInput:
    out: StartNotebookExecutionInput = {}  # type: ignore[typeddict-item]
    if "EditorId" in data:
        out["editor_id"] = data["EditorId"]
    if "RelativePath" in data:
        out["relative_path"] = data["RelativePath"]
    if "NotebookExecutionName" in data:
        out["notebook_execution_name"] = data["NotebookExecutionName"]
    if "NotebookParams" in data:
        out["notebook_params"] = data["NotebookParams"]
    if "ExecutionEngine" in data:
        import aws_sdk_emr.types.execution_engine_config

        out["execution_engine"] = (
            aws_sdk_emr.types.execution_engine_config.deserialize_aws_json_1_1(
                data["ExecutionEngine"]
            )
        )
    if "ServiceRole" in data:
        out["service_role"] = data["ServiceRole"]
    if "NotebookInstanceSecurityGroupId" in data:
        out["notebook_instance_security_group_id"] = data[
            "NotebookInstanceSecurityGroupId"
        ]
    if "Tags" in data:
        import aws_sdk_emr.types.tag_list

        out["tags"] = aws_sdk_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if "NotebookS3Location" in data:
        import aws_sdk_emr.types.notebook_s3_location_from_input

        out["notebook_s3_location"] = (
            aws_sdk_emr.types.notebook_s3_location_from_input.deserialize_aws_json_1_1(
                data["NotebookS3Location"]
            )
        )
    if "OutputNotebookS3Location" in data:
        import aws_sdk_emr.types.output_notebook_s3_location_from_input

        out["output_notebook_s3_location"] = (
            aws_sdk_emr.types.output_notebook_s3_location_from_input.deserialize_aws_json_1_1(
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
