"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateProjectRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.amazon_role_resource_name
    import aws_sdk_device_farm.types.environment_variables
    import aws_sdk_device_farm.types.job_timeout_minutes
    import aws_sdk_device_farm.types.name
    import aws_sdk_device_farm.types.vpc_config


class UpdateProjectRequest(TypedDict):
    arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the project whose name to update.</p>"""
    name: NotRequired["aws_sdk_device_farm.types.name.Name"]
    """<p>A string that represents the new name of the project that you are updating.</p>"""
    default_job_timeout_minutes: NotRequired[
        "aws_sdk_device_farm.types.job_timeout_minutes.JobTimeoutMinutes"
    ]
    """<p>The number of minutes a test run in the project executes before it times out.</p>"""
    vpc_config: NotRequired["aws_sdk_device_farm.types.vpc_config.VpcConfig"]
    """<p>The VPC security groups and subnets that are attached to a project.</p>"""
    environment_variables: NotRequired[
        "aws_sdk_device_farm.types.environment_variables.EnvironmentVariables"
    ]
    r"""<p> A set of environment variables which are used by default for all runs in the project. These environment variables are applied to the test run during the execution of a test spec file. </p> <p> For more information about using test spec files, please see <a href=\"https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments.html\">Custom test environments </a> in <i>AWS Device Farm.</i> </p>"""
    execution_role_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_role_resource_name.AmazonRoleResourceName"
    ]
    """<p>An IAM role to be assumed by the test host for all runs in the project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "default_job_timeout_minutes" in value:
        out["defaultJobTimeoutMinutes"] = value["default_job_timeout_minutes"]
    if "vpc_config" in value:
        import aws_sdk_device_farm.types.vpc_config

        out["vpcConfig"] = aws_sdk_device_farm.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "environment_variables" in value:
        import aws_sdk_device_farm.types.environment_variables

        out["environmentVariables"] = (
            aws_sdk_device_farm.types.environment_variables.serialize_aws_json_1_1(
                value["environment_variables"]
            )
        )
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectRequest:
    out: UpdateProjectRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateProjectRequest.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "defaultJobTimeoutMinutes" in data:
        out["default_job_timeout_minutes"] = data["defaultJobTimeoutMinutes"]
    if "vpcConfig" in data:
        import aws_sdk_device_farm.types.vpc_config

        out["vpc_config"] = (
            aws_sdk_device_farm.types.vpc_config.deserialize_aws_json_1_1(
                data["vpcConfig"]
            )
        )
    if "environmentVariables" in data:
        import aws_sdk_device_farm.types.environment_variables

        out["environment_variables"] = (
            aws_sdk_device_farm.types.environment_variables.deserialize_aws_json_1_1(
                data["environmentVariables"]
            )
        )
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    return out
