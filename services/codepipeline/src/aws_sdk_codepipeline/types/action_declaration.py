"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionDeclaration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_configuration_map
    import aws_sdk_codepipeline.types.action_name
    import aws_sdk_codepipeline.types.action_namespace
    import aws_sdk_codepipeline.types.action_run_order
    import aws_sdk_codepipeline.types.action_timeout
    import aws_sdk_codepipeline.types.action_type_id
    import aws_sdk_codepipeline.types.aws_region_name
    import aws_sdk_codepipeline.types.command_list
    import aws_sdk_codepipeline.types.environment_variable_list
    import aws_sdk_codepipeline.types.input_artifact_list
    import aws_sdk_codepipeline.types.output_artifact_list
    import aws_sdk_codepipeline.types.output_variable_list
    import aws_sdk_codepipeline.types.role_arn


class ActionDeclaration(TypedDict):
    name: "aws_sdk_codepipeline.types.action_name.ActionName"
    """<p>The action declaration's name.</p>"""
    action_type_id: "aws_sdk_codepipeline.types.action_type_id.ActionTypeId"
    """<p>Specifies the action type and the provider of the action.</p>"""
    run_order: NotRequired["aws_sdk_codepipeline.types.action_run_order.ActionRunOrder"]
    """<p>The order in which actions are run.</p>"""
    configuration: NotRequired[
        "aws_sdk_codepipeline.types.action_configuration_map.ActionConfigurationMap"
    ]
    r"""<p>The action's configuration. These are key-value pairs that specify input values for an action. For more information, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements\">Action Structure Requirements in CodePipeline</a>. For the list of configuration properties for the CloudFormation action type in CodePipeline, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-action-reference.html\">Configuration Properties Reference</a> in the <i>CloudFormation User Guide</i>. For template snippets with examples, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-parameter-override-functions.html\">Using Parameter Override Functions with CodePipeline Pipelines</a> in the <i>CloudFormation User Guide</i>.</p> <p>The values can be represented in either JSON or YAML format. For example, the JSON configuration item format is as follows: </p> <p> <i>JSON:</i> </p> <p> <code>\"Configuration\" : { Key : Value },</code> </p>"""
    commands: NotRequired["aws_sdk_codepipeline.types.command_list.CommandList"]
    """<p>The shell commands to run with your compute action in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.</p> <note> <p>Using compute time for this action will incur separate charges in CodeBuild.</p> </note>"""
    output_artifacts: NotRequired[
        "aws_sdk_codepipeline.types.output_artifact_list.OutputArtifactList"
    ]
    """<p>The name or ID of the result of the action declaration, such as a test or build artifact.</p>"""
    input_artifacts: NotRequired[
        "aws_sdk_codepipeline.types.input_artifact_list.InputArtifactList"
    ]
    """<p>The name or ID of the artifact consumed by the action, such as a test or build artifact.</p>"""
    output_variables: NotRequired[
        "aws_sdk_codepipeline.types.output_variable_list.OutputVariableList"
    ]
    """<p>The list of variables that are to be exported from the compute action. This is specifically CodeBuild environment variables as used for that action.</p>"""
    role_arn: NotRequired["aws_sdk_codepipeline.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline.</p>"""
    region: NotRequired["aws_sdk_codepipeline.types.aws_region_name.AWSRegionName"]
    """<p>The action declaration's Amazon Web Services Region, such as us-east-1.</p>"""
    namespace: NotRequired[
        "aws_sdk_codepipeline.types.action_namespace.ActionNamespace"
    ]
    """<p>The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.</p>"""
    timeout_in_minutes: NotRequired[
        "aws_sdk_codepipeline.types.action_timeout.ActionTimeout"
    ]
    r"""<p>A timeout duration in minutes that can be applied against the ActionType’s default timeout value specified in <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/limits.html\">Quotas for CodePipeline </a>. This attribute is available only to the manual approval ActionType.</p>"""
    environment_variables: NotRequired[
        "aws_sdk_codepipeline.types.environment_variable_list.EnvironmentVariableList"
    ]
    """<p>The environment variables for the action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionDeclaration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_codepipeline.types.action_type_id

    out["actionTypeId"] = (
        aws_sdk_codepipeline.types.action_type_id.serialize_aws_json_1_1(
            value["action_type_id"]
        )
    )
    if "run_order" in value:
        out["runOrder"] = value["run_order"]
    if "configuration" in value:
        import aws_sdk_codepipeline.types.action_configuration_map

        out["configuration"] = (
            aws_sdk_codepipeline.types.action_configuration_map.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "commands" in value:
        import aws_sdk_codepipeline.types.command_list

        out["commands"] = (
            aws_sdk_codepipeline.types.command_list.serialize_aws_json_1_1(
                value["commands"]
            )
        )
    if "output_artifacts" in value:
        import aws_sdk_codepipeline.types.output_artifact_list

        out["outputArtifacts"] = (
            aws_sdk_codepipeline.types.output_artifact_list.serialize_aws_json_1_1(
                value["output_artifacts"]
            )
        )
    if "input_artifacts" in value:
        import aws_sdk_codepipeline.types.input_artifact_list

        out["inputArtifacts"] = (
            aws_sdk_codepipeline.types.input_artifact_list.serialize_aws_json_1_1(
                value["input_artifacts"]
            )
        )
    if "output_variables" in value:
        import aws_sdk_codepipeline.types.output_variable_list

        out["outputVariables"] = (
            aws_sdk_codepipeline.types.output_variable_list.serialize_aws_json_1_1(
                value["output_variables"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "region" in value:
        out["region"] = value["region"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "timeout_in_minutes" in value:
        out["timeoutInMinutes"] = value["timeout_in_minutes"]
    if "environment_variables" in value:
        import aws_sdk_codepipeline.types.environment_variable_list

        out["environmentVariables"] = (
            aws_sdk_codepipeline.types.environment_variable_list.serialize_aws_json_1_1(
                value["environment_variables"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionDeclaration:
    out: ActionDeclaration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ActionDeclaration.name required")
    if "actionTypeId" in data:
        import aws_sdk_codepipeline.types.action_type_id

        out["action_type_id"] = (
            aws_sdk_codepipeline.types.action_type_id.deserialize_aws_json_1_1(
                data["actionTypeId"]
            )
        )
    else:
        raise DeserializationError("ActionDeclaration.action_type_id required")
    if "runOrder" in data:
        out["run_order"] = data["runOrder"]
    if "configuration" in data:
        import aws_sdk_codepipeline.types.action_configuration_map

        out["configuration"] = (
            aws_sdk_codepipeline.types.action_configuration_map.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if "commands" in data:
        import aws_sdk_codepipeline.types.command_list

        out["commands"] = (
            aws_sdk_codepipeline.types.command_list.deserialize_aws_json_1_1(
                data["commands"]
            )
        )
    if "outputArtifacts" in data:
        import aws_sdk_codepipeline.types.output_artifact_list

        out["output_artifacts"] = (
            aws_sdk_codepipeline.types.output_artifact_list.deserialize_aws_json_1_1(
                data["outputArtifacts"]
            )
        )
    if "inputArtifacts" in data:
        import aws_sdk_codepipeline.types.input_artifact_list

        out["input_artifacts"] = (
            aws_sdk_codepipeline.types.input_artifact_list.deserialize_aws_json_1_1(
                data["inputArtifacts"]
            )
        )
    if "outputVariables" in data:
        import aws_sdk_codepipeline.types.output_variable_list

        out["output_variables"] = (
            aws_sdk_codepipeline.types.output_variable_list.deserialize_aws_json_1_1(
                data["outputVariables"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "region" in data:
        out["region"] = data["region"]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "timeoutInMinutes" in data:
        out["timeout_in_minutes"] = data["timeoutInMinutes"]
    if "environmentVariables" in data:
        import aws_sdk_codepipeline.types.environment_variable_list

        out["environment_variables"] = (
            aws_sdk_codepipeline.types.environment_variable_list.deserialize_aws_json_1_1(
                data["environmentVariables"]
            )
        )
    return out
