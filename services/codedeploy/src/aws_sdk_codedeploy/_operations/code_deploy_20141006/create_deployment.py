"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeployment``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_codedeploy._auth._signers
import aws_sdk_codedeploy._auth._sigv4
from aws_sdk_codedeploy._protocol.errors import parse_error_metadata_json
from aws_sdk_codedeploy._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codedeploy._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codedeploy.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.create_deployment_input
    import aws_sdk_codedeploy.types.create_deployment_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AlarmsLimitExceededException":
            import aws_sdk_codedeploy.errors.alarms_limit_exceeded_exception

            raise aws_sdk_codedeploy.errors.alarms_limit_exceeded_exception.AlarmsLimitExceededException.from_aws_json_1_1(
                data
            )
        case "ApplicationDoesNotExistException":
            import aws_sdk_codedeploy.errors.application_does_not_exist_exception

            raise aws_sdk_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "ApplicationNameRequiredException":
            import aws_sdk_codedeploy.errors.application_name_required_exception

            raise aws_sdk_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException.from_aws_json_1_1(
                data
            )
        case "DeploymentConfigDoesNotExistException":
            import aws_sdk_codedeploy.errors.deployment_config_does_not_exist_exception

            raise aws_sdk_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "DeploymentGroupDoesNotExistException":
            import aws_sdk_codedeploy.errors.deployment_group_does_not_exist_exception

            raise aws_sdk_codedeploy.errors.deployment_group_does_not_exist_exception.DeploymentGroupDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "DeploymentGroupNameRequiredException":
            import aws_sdk_codedeploy.errors.deployment_group_name_required_exception

            raise aws_sdk_codedeploy.errors.deployment_group_name_required_exception.DeploymentGroupNameRequiredException.from_aws_json_1_1(
                data
            )
        case "DeploymentLimitExceededException":
            import aws_sdk_codedeploy.errors.deployment_limit_exceeded_exception

            raise aws_sdk_codedeploy.errors.deployment_limit_exceeded_exception.DeploymentLimitExceededException.from_aws_json_1_1(
                data
            )
        case "DescriptionTooLongException":
            import aws_sdk_codedeploy.errors.description_too_long_exception

            raise aws_sdk_codedeploy.errors.description_too_long_exception.DescriptionTooLongException.from_aws_json_1_1(
                data
            )
        case "InvalidAlarmConfigException":
            import aws_sdk_codedeploy.errors.invalid_alarm_config_exception

            raise aws_sdk_codedeploy.errors.invalid_alarm_config_exception.InvalidAlarmConfigException.from_aws_json_1_1(
                data
            )
        case "InvalidApplicationNameException":
            import aws_sdk_codedeploy.errors.invalid_application_name_exception

            raise aws_sdk_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException.from_aws_json_1_1(
                data
            )
        case "InvalidAutoRollbackConfigException":
            import aws_sdk_codedeploy.errors.invalid_auto_rollback_config_exception

            raise aws_sdk_codedeploy.errors.invalid_auto_rollback_config_exception.InvalidAutoRollbackConfigException.from_aws_json_1_1(
                data
            )
        case "InvalidAutoScalingGroupException":
            import aws_sdk_codedeploy.errors.invalid_auto_scaling_group_exception

            raise aws_sdk_codedeploy.errors.invalid_auto_scaling_group_exception.InvalidAutoScalingGroupException.from_aws_json_1_1(
                data
            )
        case "InvalidDeploymentConfigNameException":
            import aws_sdk_codedeploy.errors.invalid_deployment_config_name_exception

            raise aws_sdk_codedeploy.errors.invalid_deployment_config_name_exception.InvalidDeploymentConfigNameException.from_aws_json_1_1(
                data
            )
        case "InvalidDeploymentGroupNameException":
            import aws_sdk_codedeploy.errors.invalid_deployment_group_name_exception

            raise aws_sdk_codedeploy.errors.invalid_deployment_group_name_exception.InvalidDeploymentGroupNameException.from_aws_json_1_1(
                data
            )
        case "InvalidFileExistsBehaviorException":
            import aws_sdk_codedeploy.errors.invalid_file_exists_behavior_exception

            raise aws_sdk_codedeploy.errors.invalid_file_exists_behavior_exception.InvalidFileExistsBehaviorException.from_aws_json_1_1(
                data
            )
        case "InvalidGitHubAccountTokenException":
            import aws_sdk_codedeploy.errors.invalid_git_hub_account_token_exception

            raise aws_sdk_codedeploy.errors.invalid_git_hub_account_token_exception.InvalidGitHubAccountTokenException.from_aws_json_1_1(
                data
            )
        case "InvalidIgnoreApplicationStopFailuresValueException":
            import aws_sdk_codedeploy.errors.invalid_ignore_application_stop_failures_value_exception

            raise aws_sdk_codedeploy.errors.invalid_ignore_application_stop_failures_value_exception.InvalidIgnoreApplicationStopFailuresValueException.from_aws_json_1_1(
                data
            )
        case "InvalidLoadBalancerInfoException":
            import aws_sdk_codedeploy.errors.invalid_load_balancer_info_exception

            raise aws_sdk_codedeploy.errors.invalid_load_balancer_info_exception.InvalidLoadBalancerInfoException.from_aws_json_1_1(
                data
            )
        case "InvalidRevisionException":
            import aws_sdk_codedeploy.errors.invalid_revision_exception

            raise aws_sdk_codedeploy.errors.invalid_revision_exception.InvalidRevisionException.from_aws_json_1_1(
                data
            )
        case "InvalidRoleException":
            import aws_sdk_codedeploy.errors.invalid_role_exception

            raise aws_sdk_codedeploy.errors.invalid_role_exception.InvalidRoleException.from_aws_json_1_1(
                data
            )
        case "InvalidTargetInstancesException":
            import aws_sdk_codedeploy.errors.invalid_target_instances_exception

            raise aws_sdk_codedeploy.errors.invalid_target_instances_exception.InvalidTargetInstancesException.from_aws_json_1_1(
                data
            )
        case "InvalidTrafficRoutingConfigurationException":
            import aws_sdk_codedeploy.errors.invalid_traffic_routing_configuration_exception

            raise aws_sdk_codedeploy.errors.invalid_traffic_routing_configuration_exception.InvalidTrafficRoutingConfigurationException.from_aws_json_1_1(
                data
            )
        case "InvalidUpdateOutdatedInstancesOnlyValueException":
            import aws_sdk_codedeploy.errors.invalid_update_outdated_instances_only_value_exception

            raise aws_sdk_codedeploy.errors.invalid_update_outdated_instances_only_value_exception.InvalidUpdateOutdatedInstancesOnlyValueException.from_aws_json_1_1(
                data
            )
        case "RevisionDoesNotExistException":
            import aws_sdk_codedeploy.errors.revision_does_not_exist_exception

            raise aws_sdk_codedeploy.errors.revision_does_not_exist_exception.RevisionDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "RevisionRequiredException":
            import aws_sdk_codedeploy.errors.revision_required_exception

            raise aws_sdk_codedeploy.errors.revision_required_exception.RevisionRequiredException.from_aws_json_1_1(
                data
            )
        case "ThrottlingException":
            import aws_sdk_codedeploy.errors.throttling_exception

            raise aws_sdk_codedeploy.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_codedeploy.types.create_deployment_output.CreateDeploymentOutput:
    import aws_sdk_codedeploy.types.create_deployment_output

    out: aws_sdk_codedeploy.types.create_deployment_output.CreateDeploymentOutput = (
        aws_sdk_codedeploy.types.create_deployment_output.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codedeploy._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_codedeploy._auth._sigv4.build_sigv4_auth_scheme(
                "codedeploy", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_codedeploy._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_codedeploy.types.create_deployment_input.CreateDeploymentInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "CodeDeploy_20141006.CreateDeployment"
    import aws_sdk_codedeploy.types.create_deployment_input

    body: bytes | None = json.dumps(
        aws_sdk_codedeploy.types.create_deployment_input.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_deployment(
    options: OperationOptions,
    input_: aws_sdk_codedeploy.types.create_deployment_input.CreateDeploymentInput,
) -> tuple[
    aws_sdk_codedeploy.types.create_deployment_output.CreateDeploymentOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_create_deployment(
    options: AsyncOperationOptions,
    input_: aws_sdk_codedeploy.types.create_deployment_input.CreateDeploymentInput,
) -> tuple[
    aws_sdk_codedeploy.types.create_deployment_output.CreateDeploymentOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
