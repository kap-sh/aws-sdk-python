"""Generated from Smithy shape ``com.amazonaws.devicefarm#Project``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.amazon_role_resource_name
    import capo_device_farm.types.date_time
    import capo_device_farm.types.environment_variables
    import capo_device_farm.types.job_timeout_minutes
    import capo_device_farm.types.name
    import capo_device_farm.types.vpc_config


class Project(TypedDict, closed=True):
    arn: NotRequired["capo_device_farm.types.amazon_resource_name.AmazonResourceName"]
    """<p>The project's ARN.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The project's name.</p>"""
    default_job_timeout_minutes: NotRequired[
        "capo_device_farm.types.job_timeout_minutes.JobTimeoutMinutes"
    ]
    """<p>The default number of minutes (at the project level) a test run executes before it times out. The default value is 150 minutes.</p>"""
    created: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>When the project was created.</p>"""
    vpc_config: NotRequired["capo_device_farm.types.vpc_config.VpcConfig"]
    """<p>The VPC security groups and subnets that are attached to a project.</p>"""
    environment_variables: NotRequired[
        "capo_device_farm.types.environment_variables.EnvironmentVariables"
    ]
    """<p>Environment variables associated with the project.</p>"""
    execution_role_arn: NotRequired[
        "capo_device_farm.types.amazon_role_resource_name.AmazonRoleResourceName"
    ]
    """<p>The IAM execution role associated with the project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Project) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "default_job_timeout_minutes" in value:
        out["defaultJobTimeoutMinutes"] = value["default_job_timeout_minutes"]
    if "created" in value:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["created"]
        )
    if "vpc_config" in value:
        import capo_device_farm.types.vpc_config

        out["vpcConfig"] = capo_device_farm.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "environment_variables" in value:
        import capo_device_farm.types.environment_variables

        out["environmentVariables"] = (
            capo_device_farm.types.environment_variables.serialize_aws_json_1_1(
                value["environment_variables"]
            )
        )
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Project:
    out: Project = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "defaultJobTimeoutMinutes" in data:
        out["default_job_timeout_minutes"] = data["defaultJobTimeoutMinutes"]
    if "created" in data:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["created"]
        )
    if "vpcConfig" in data:
        import capo_device_farm.types.vpc_config

        out["vpc_config"] = capo_device_farm.types.vpc_config.deserialize_aws_json_1_1(
            data["vpcConfig"]
        )
    if "environmentVariables" in data:
        import capo_device_farm.types.environment_variables

        out["environment_variables"] = (
            capo_device_farm.types.environment_variables.deserialize_aws_json_1_1(
                data["environmentVariables"]
            )
        )
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    return out
