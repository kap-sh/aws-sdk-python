"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeploymentConfig``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_codedeploy._auth._signers
import capo_codedeploy._auth._sigv4
import capo_codedeploy.errors.deployment_config_already_exists_exception
import capo_codedeploy.errors.deployment_config_limit_exceeded_exception
import capo_codedeploy.errors.deployment_config_name_required_exception
import capo_codedeploy.errors.invalid_compute_platform_exception
import capo_codedeploy.errors.invalid_deployment_config_name_exception
import capo_codedeploy.errors.invalid_minimum_healthy_host_value_exception
import capo_codedeploy.errors.invalid_traffic_routing_configuration_exception
import capo_codedeploy.errors.invalid_zonal_deployment_configuration_exception
import capo_codedeploy.types.compute_platform
import capo_codedeploy.types.create_deployment_config_input
import capo_codedeploy.types.create_deployment_config_output
import capo_codedeploy.types.minimum_healthy_hosts
import capo_codedeploy.types.traffic_routing_config
import capo_codedeploy.types.zonal_config
from capo_codedeploy._protocol.errors import parse_error_metadata_json
from capo_codedeploy._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_codedeploy._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_codedeploy.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DeploymentConfigAlreadyExistsException":
            raise capo_codedeploy.errors.deployment_config_already_exists_exception.DeploymentConfigAlreadyExistsException.from_aws_json_1_1(
                data
            )
        case "DeploymentConfigLimitExceededException":
            raise capo_codedeploy.errors.deployment_config_limit_exceeded_exception.DeploymentConfigLimitExceededException.from_aws_json_1_1(
                data
            )
        case "DeploymentConfigNameRequiredException":
            raise capo_codedeploy.errors.deployment_config_name_required_exception.DeploymentConfigNameRequiredException.from_aws_json_1_1(
                data
            )
        case "InvalidComputePlatformException":
            raise capo_codedeploy.errors.invalid_compute_platform_exception.InvalidComputePlatformException.from_aws_json_1_1(
                data
            )
        case "InvalidDeploymentConfigNameException":
            raise capo_codedeploy.errors.invalid_deployment_config_name_exception.InvalidDeploymentConfigNameException.from_aws_json_1_1(
                data
            )
        case "InvalidMinimumHealthyHostValueException":
            raise capo_codedeploy.errors.invalid_minimum_healthy_host_value_exception.InvalidMinimumHealthyHostValueException.from_aws_json_1_1(
                data
            )
        case "InvalidTrafficRoutingConfigurationException":
            raise capo_codedeploy.errors.invalid_traffic_routing_configuration_exception.InvalidTrafficRoutingConfigurationException.from_aws_json_1_1(
                data
            )
        case "InvalidZonalDeploymentConfigurationException":
            raise capo_codedeploy.errors.invalid_zonal_deployment_configuration_exception.InvalidZonalDeploymentConfigurationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_codedeploy.types.create_deployment_config_output.CreateDeploymentConfigOutput:
    out: capo_codedeploy.types.create_deployment_config_output.CreateDeploymentConfigOutput = capo_codedeploy.types.create_deployment_config_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_codedeploy.types.create_deployment_config_output.CreateDeploymentConfigOutput:
    out: capo_codedeploy.types.create_deployment_config_output.CreateDeploymentConfigOutput = capo_codedeploy.types.create_deployment_config_output.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_codedeploy._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_codedeploy._auth._sigv4.build_sigv4_auth_scheme(
                "codedeploy", options.region
            )
        )
        if sigv4_config is not None:
            return capo_codedeploy._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_codedeploy.types.create_deployment_config_input.CreateDeploymentConfigInput,
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
    headers["X-Amz-Target"] = "CodeDeploy_20141006.CreateDeploymentConfig"
    body: bytes | None = json.dumps(
        capo_codedeploy.types.create_deployment_config_input.serialize_aws_json_1_1(
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


def create_deployment_config(
    options: OperationOptions,
    input_: capo_codedeploy.types.create_deployment_config_input.CreateDeploymentConfigInput,
) -> tuple[
    capo_codedeploy.types.create_deployment_config_output.CreateDeploymentConfigOutput,
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


async def async_create_deployment_config(
    options: AsyncOperationOptions,
    input_: capo_codedeploy.types.create_deployment_config_input.CreateDeploymentConfigInput,
) -> tuple[
    capo_codedeploy.types.create_deployment_config_output.CreateDeploymentConfigOutput,
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
