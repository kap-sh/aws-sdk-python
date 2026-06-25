"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeploymentGroup``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_codedeploy._auth._signers
import aws_sdk_codedeploy._auth._sigv4
import aws_sdk_codedeploy.errors.alarms_limit_exceeded_exception
import aws_sdk_codedeploy.errors.application_does_not_exist_exception
import aws_sdk_codedeploy.errors.application_name_required_exception
import aws_sdk_codedeploy.errors.deployment_config_does_not_exist_exception
import aws_sdk_codedeploy.errors.deployment_group_already_exists_exception
import aws_sdk_codedeploy.errors.deployment_group_limit_exceeded_exception
import aws_sdk_codedeploy.errors.deployment_group_name_required_exception
import aws_sdk_codedeploy.errors.ecs_service_mapping_limit_exceeded_exception
import aws_sdk_codedeploy.errors.invalid_alarm_config_exception
import aws_sdk_codedeploy.errors.invalid_application_name_exception
import aws_sdk_codedeploy.errors.invalid_auto_rollback_config_exception
import aws_sdk_codedeploy.errors.invalid_auto_scaling_group_exception
import aws_sdk_codedeploy.errors.invalid_blue_green_deployment_configuration_exception
import aws_sdk_codedeploy.errors.invalid_deployment_config_name_exception
import aws_sdk_codedeploy.errors.invalid_deployment_group_name_exception
import aws_sdk_codedeploy.errors.invalid_deployment_style_exception
import aws_sdk_codedeploy.errors.invalid_ec2_tag_combination_exception
import aws_sdk_codedeploy.errors.invalid_ec2_tag_exception
import aws_sdk_codedeploy.errors.invalid_ecs_service_exception
import aws_sdk_codedeploy.errors.invalid_input_exception
import aws_sdk_codedeploy.errors.invalid_load_balancer_info_exception
import aws_sdk_codedeploy.errors.invalid_on_premises_tag_combination_exception
import aws_sdk_codedeploy.errors.invalid_role_exception
import aws_sdk_codedeploy.errors.invalid_tag_exception
import aws_sdk_codedeploy.errors.invalid_tags_to_add_exception
import aws_sdk_codedeploy.errors.invalid_target_group_pair_exception
import aws_sdk_codedeploy.errors.invalid_traffic_routing_configuration_exception
import aws_sdk_codedeploy.errors.invalid_trigger_config_exception
import aws_sdk_codedeploy.errors.lifecycle_hook_limit_exceeded_exception
import aws_sdk_codedeploy.errors.role_required_exception
import aws_sdk_codedeploy.errors.tag_set_list_limit_exceeded_exception
import aws_sdk_codedeploy.errors.throttling_exception
import aws_sdk_codedeploy.errors.trigger_targets_limit_exceeded_exception
import aws_sdk_codedeploy.types.alarm_configuration
import aws_sdk_codedeploy.types.auto_rollback_configuration
import aws_sdk_codedeploy.types.auto_scaling_group_name_list
import aws_sdk_codedeploy.types.blue_green_deployment_configuration
import aws_sdk_codedeploy.types.create_deployment_group_input
import aws_sdk_codedeploy.types.create_deployment_group_output
import aws_sdk_codedeploy.types.deployment_style
import aws_sdk_codedeploy.types.ec2_tag_filter_list
import aws_sdk_codedeploy.types.ec2_tag_set
import aws_sdk_codedeploy.types.ecs_service_list
import aws_sdk_codedeploy.types.load_balancer_info
import aws_sdk_codedeploy.types.on_premises_tag_set
import aws_sdk_codedeploy.types.outdated_instances_strategy
import aws_sdk_codedeploy.types.tag_filter_list
import aws_sdk_codedeploy.types.tag_list
import aws_sdk_codedeploy.types.trigger_config_list
from aws_sdk_codedeploy._protocol.errors import parse_error_metadata_json
from aws_sdk_codedeploy._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codedeploy._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codedeploy.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AlarmsLimitExceededException":
            raise aws_sdk_codedeploy.errors.alarms_limit_exceeded_exception.AlarmsLimitExceededException.from_aws_json_1_1(
                data
            )
        case "ApplicationDoesNotExistException":
            raise aws_sdk_codedeploy.errors.application_does_not_exist_exception.ApplicationDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "ApplicationNameRequiredException":
            raise aws_sdk_codedeploy.errors.application_name_required_exception.ApplicationNameRequiredException.from_aws_json_1_1(
                data
            )
        case "DeploymentConfigDoesNotExistException":
            raise aws_sdk_codedeploy.errors.deployment_config_does_not_exist_exception.DeploymentConfigDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "DeploymentGroupAlreadyExistsException":
            raise aws_sdk_codedeploy.errors.deployment_group_already_exists_exception.DeploymentGroupAlreadyExistsException.from_aws_json_1_1(
                data
            )
        case "DeploymentGroupLimitExceededException":
            raise aws_sdk_codedeploy.errors.deployment_group_limit_exceeded_exception.DeploymentGroupLimitExceededException.from_aws_json_1_1(
                data
            )
        case "DeploymentGroupNameRequiredException":
            raise aws_sdk_codedeploy.errors.deployment_group_name_required_exception.DeploymentGroupNameRequiredException.from_aws_json_1_1(
                data
            )
        case "ECSServiceMappingLimitExceededException":
            raise aws_sdk_codedeploy.errors.ecs_service_mapping_limit_exceeded_exception.ECSServiceMappingLimitExceededException.from_aws_json_1_1(
                data
            )
        case "InvalidAlarmConfigException":
            raise aws_sdk_codedeploy.errors.invalid_alarm_config_exception.InvalidAlarmConfigException.from_aws_json_1_1(
                data
            )
        case "InvalidApplicationNameException":
            raise aws_sdk_codedeploy.errors.invalid_application_name_exception.InvalidApplicationNameException.from_aws_json_1_1(
                data
            )
        case "InvalidAutoRollbackConfigException":
            raise aws_sdk_codedeploy.errors.invalid_auto_rollback_config_exception.InvalidAutoRollbackConfigException.from_aws_json_1_1(
                data
            )
        case "InvalidAutoScalingGroupException":
            raise aws_sdk_codedeploy.errors.invalid_auto_scaling_group_exception.InvalidAutoScalingGroupException.from_aws_json_1_1(
                data
            )
        case "InvalidBlueGreenDeploymentConfigurationException":
            raise aws_sdk_codedeploy.errors.invalid_blue_green_deployment_configuration_exception.InvalidBlueGreenDeploymentConfigurationException.from_aws_json_1_1(
                data
            )
        case "InvalidDeploymentConfigNameException":
            raise aws_sdk_codedeploy.errors.invalid_deployment_config_name_exception.InvalidDeploymentConfigNameException.from_aws_json_1_1(
                data
            )
        case "InvalidDeploymentGroupNameException":
            raise aws_sdk_codedeploy.errors.invalid_deployment_group_name_exception.InvalidDeploymentGroupNameException.from_aws_json_1_1(
                data
            )
        case "InvalidDeploymentStyleException":
            raise aws_sdk_codedeploy.errors.invalid_deployment_style_exception.InvalidDeploymentStyleException.from_aws_json_1_1(
                data
            )
        case "InvalidEC2TagCombinationException":
            raise aws_sdk_codedeploy.errors.invalid_ec2_tag_combination_exception.InvalidEC2TagCombinationException.from_aws_json_1_1(
                data
            )
        case "InvalidEC2TagException":
            raise aws_sdk_codedeploy.errors.invalid_ec2_tag_exception.InvalidEC2TagException.from_aws_json_1_1(
                data
            )
        case "InvalidECSServiceException":
            raise aws_sdk_codedeploy.errors.invalid_ecs_service_exception.InvalidECSServiceException.from_aws_json_1_1(
                data
            )
        case "InvalidInputException":
            raise aws_sdk_codedeploy.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_1(
                data
            )
        case "InvalidLoadBalancerInfoException":
            raise aws_sdk_codedeploy.errors.invalid_load_balancer_info_exception.InvalidLoadBalancerInfoException.from_aws_json_1_1(
                data
            )
        case "InvalidOnPremisesTagCombinationException":
            raise aws_sdk_codedeploy.errors.invalid_on_premises_tag_combination_exception.InvalidOnPremisesTagCombinationException.from_aws_json_1_1(
                data
            )
        case "InvalidRoleException":
            raise aws_sdk_codedeploy.errors.invalid_role_exception.InvalidRoleException.from_aws_json_1_1(
                data
            )
        case "InvalidTagException":
            raise aws_sdk_codedeploy.errors.invalid_tag_exception.InvalidTagException.from_aws_json_1_1(
                data
            )
        case "InvalidTagsToAddException":
            raise aws_sdk_codedeploy.errors.invalid_tags_to_add_exception.InvalidTagsToAddException.from_aws_json_1_1(
                data
            )
        case "InvalidTargetGroupPairException":
            raise aws_sdk_codedeploy.errors.invalid_target_group_pair_exception.InvalidTargetGroupPairException.from_aws_json_1_1(
                data
            )
        case "InvalidTrafficRoutingConfigurationException":
            raise aws_sdk_codedeploy.errors.invalid_traffic_routing_configuration_exception.InvalidTrafficRoutingConfigurationException.from_aws_json_1_1(
                data
            )
        case "InvalidTriggerConfigException":
            raise aws_sdk_codedeploy.errors.invalid_trigger_config_exception.InvalidTriggerConfigException.from_aws_json_1_1(
                data
            )
        case "LifecycleHookLimitExceededException":
            raise aws_sdk_codedeploy.errors.lifecycle_hook_limit_exceeded_exception.LifecycleHookLimitExceededException.from_aws_json_1_1(
                data
            )
        case "RoleRequiredException":
            raise aws_sdk_codedeploy.errors.role_required_exception.RoleRequiredException.from_aws_json_1_1(
                data
            )
        case "TagSetListLimitExceededException":
            raise aws_sdk_codedeploy.errors.tag_set_list_limit_exceeded_exception.TagSetListLimitExceededException.from_aws_json_1_1(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_codedeploy.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data
            )
        case "TriggerTargetsLimitExceededException":
            raise aws_sdk_codedeploy.errors.trigger_targets_limit_exceeded_exception.TriggerTargetsLimitExceededException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput
):
    out: aws_sdk_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput = aws_sdk_codedeploy.types.create_deployment_group_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput
):
    out: aws_sdk_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput = aws_sdk_codedeploy.types.create_deployment_group_output.deserialize_aws_json_1_1(
        json.loads(await response.aread())
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
    input_: aws_sdk_codedeploy.types.create_deployment_group_input.CreateDeploymentGroupInput,
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
    headers["X-Amz-Target"] = "CodeDeploy_20141006.CreateDeploymentGroup"
    body: bytes | None = json.dumps(
        aws_sdk_codedeploy.types.create_deployment_group_input.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_deployment_group(
    options: OperationOptions,
    input_: aws_sdk_codedeploy.types.create_deployment_group_input.CreateDeploymentGroupInput,
) -> tuple[
    aws_sdk_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_create_deployment_group(
    options: AsyncOperationOptions,
    input_: aws_sdk_codedeploy.types.create_deployment_group_input.CreateDeploymentGroupInput,
) -> tuple[
    aws_sdk_codedeploy.types.create_deployment_group_output.CreateDeploymentGroupOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
