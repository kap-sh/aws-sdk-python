"""Generated from Smithy shape ``com.amazonaws.emrcontainers#StartJobRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.client_token
    import aws_sdk_emr_containers.types.configuration_overrides
    import aws_sdk_emr_containers.types.iam_role_arn
    import aws_sdk_emr_containers.types.job_driver
    import aws_sdk_emr_containers.types.release_label
    import aws_sdk_emr_containers.types.resource_id_string
    import aws_sdk_emr_containers.types.resource_name_string
    import aws_sdk_emr_containers.types.retry_policy_configuration
    import aws_sdk_emr_containers.types.tag_map
    import aws_sdk_emr_containers.types.template_parameter_input_map


class StartJobRunRequest(TypedDict):
    name: NotRequired[
        "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>The name of the job run.</p>"""
    virtual_cluster_id: (
        "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    )
    """<p>The virtual cluster ID for which the job run request is submitted.</p>"""
    client_token: "aws_sdk_emr_containers.types.client_token.ClientToken"
    """<p>The client idempotency token of the job run request. </p>"""
    execution_role_arn: NotRequired[
        "aws_sdk_emr_containers.types.iam_role_arn.IAMRoleArn"
    ]
    """<p>The execution role ARN for the job run.</p>"""
    release_label: NotRequired[
        "aws_sdk_emr_containers.types.release_label.ReleaseLabel"
    ]
    """<p>The Amazon EMR release version to use for the job run.</p>"""
    job_driver: NotRequired["aws_sdk_emr_containers.types.job_driver.JobDriver"]
    """<p>The job driver for the job run.</p>"""
    configuration_overrides: NotRequired[
        "aws_sdk_emr_containers.types.configuration_overrides.ConfigurationOverrides"
    ]
    """<p>The configuration overrides for the job run.</p>"""
    tags: NotRequired["aws_sdk_emr_containers.types.tag_map.TagMap"]
    """<p>The tags assigned to job runs.</p>"""
    job_template_id: NotRequired[
        "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    ]
    """<p>The job template ID to be used to start the job run.</p>"""
    job_template_parameters: NotRequired[
        "aws_sdk_emr_containers.types.template_parameter_input_map.TemplateParameterInputMap"
    ]
    """<p>The values of job template parameters to start a job run.</p>"""
    retry_policy_configuration: NotRequired[
        "aws_sdk_emr_containers.types.retry_policy_configuration.RetryPolicyConfiguration"
    ]
    """<p>The retry policy configuration for the job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRunRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["clientToken"] = value["client_token"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "release_label" in value:
        out["releaseLabel"] = value["release_label"]
    if "job_driver" in value:
        import aws_sdk_emr_containers.types.job_driver

        out["jobDriver"] = aws_sdk_emr_containers.types.job_driver.serialize_json(
            value["job_driver"]
        )
    if "configuration_overrides" in value:
        import aws_sdk_emr_containers.types.configuration_overrides

        out["configurationOverrides"] = (
            aws_sdk_emr_containers.types.configuration_overrides.serialize_json(
                value["configuration_overrides"]
            )
        )
    if "tags" in value:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.serialize_json(value["tags"])
    if "job_template_id" in value:
        out["jobTemplateId"] = value["job_template_id"]
    if "job_template_parameters" in value:
        import aws_sdk_emr_containers.types.template_parameter_input_map

        out["jobTemplateParameters"] = (
            aws_sdk_emr_containers.types.template_parameter_input_map.serialize_json(
                value["job_template_parameters"]
            )
        )
    if "retry_policy_configuration" in value:
        import aws_sdk_emr_containers.types.retry_policy_configuration

        out["retryPolicyConfiguration"] = (
            aws_sdk_emr_containers.types.retry_policy_configuration.serialize_json(
                value["retry_policy_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartJobRunRequest:
    out: StartJobRunRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("StartJobRunRequest.client_token required")
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    if "releaseLabel" in data:
        out["release_label"] = data["releaseLabel"]
    if "jobDriver" in data:
        import aws_sdk_emr_containers.types.job_driver

        out["job_driver"] = aws_sdk_emr_containers.types.job_driver.deserialize_json(
            data["jobDriver"]
        )
    if "configurationOverrides" in data:
        import aws_sdk_emr_containers.types.configuration_overrides

        out["configuration_overrides"] = (
            aws_sdk_emr_containers.types.configuration_overrides.deserialize_json(
                data["configurationOverrides"]
            )
        )
    if "tags" in data:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "jobTemplateId" in data:
        out["job_template_id"] = data["jobTemplateId"]
    if "jobTemplateParameters" in data:
        import aws_sdk_emr_containers.types.template_parameter_input_map

        out["job_template_parameters"] = (
            aws_sdk_emr_containers.types.template_parameter_input_map.deserialize_json(
                data["jobTemplateParameters"]
            )
        )
    if "retryPolicyConfiguration" in data:
        import aws_sdk_emr_containers.types.retry_policy_configuration

        out["retry_policy_configuration"] = (
            aws_sdk_emr_containers.types.retry_policy_configuration.deserialize_json(
                data["retryPolicyConfiguration"]
            )
        )
    return out
