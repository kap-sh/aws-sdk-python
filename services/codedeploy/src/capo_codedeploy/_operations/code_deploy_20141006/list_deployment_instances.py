"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentInstances``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_codedeploy._auth._signers
import capo_codedeploy._auth._sigv4
import capo_codedeploy.errors.deployment_does_not_exist_exception
import capo_codedeploy.errors.deployment_id_required_exception
import capo_codedeploy.errors.deployment_not_started_exception
import capo_codedeploy.errors.invalid_compute_platform_exception
import capo_codedeploy.errors.invalid_deployment_id_exception
import capo_codedeploy.errors.invalid_deployment_instance_type_exception
import capo_codedeploy.errors.invalid_instance_status_exception
import capo_codedeploy.errors.invalid_instance_type_exception
import capo_codedeploy.errors.invalid_next_token_exception
import capo_codedeploy.errors.invalid_target_filter_name_exception
import capo_codedeploy.types.instance_status_list
import capo_codedeploy.types.instance_type_list
import capo_codedeploy.types.instances_list
import capo_codedeploy.types.list_deployment_instances_input
import capo_codedeploy.types.list_deployment_instances_output
from capo_codedeploy._protocol.errors import parse_error_metadata_json
from capo_codedeploy._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_codedeploy._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_codedeploy.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DeploymentDoesNotExistException":
            raise capo_codedeploy.errors.deployment_does_not_exist_exception.DeploymentDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "DeploymentIdRequiredException":
            raise capo_codedeploy.errors.deployment_id_required_exception.DeploymentIdRequiredException.from_aws_json_1_1(
                data
            )
        case "DeploymentNotStartedException":
            raise capo_codedeploy.errors.deployment_not_started_exception.DeploymentNotStartedException.from_aws_json_1_1(
                data
            )
        case "InvalidComputePlatformException":
            raise capo_codedeploy.errors.invalid_compute_platform_exception.InvalidComputePlatformException.from_aws_json_1_1(
                data
            )
        case "InvalidDeploymentIdException":
            raise capo_codedeploy.errors.invalid_deployment_id_exception.InvalidDeploymentIdException.from_aws_json_1_1(
                data
            )
        case "InvalidDeploymentInstanceTypeException":
            raise capo_codedeploy.errors.invalid_deployment_instance_type_exception.InvalidDeploymentInstanceTypeException.from_aws_json_1_1(
                data
            )
        case "InvalidInstanceStatusException":
            raise capo_codedeploy.errors.invalid_instance_status_exception.InvalidInstanceStatusException.from_aws_json_1_1(
                data
            )
        case "InvalidInstanceTypeException":
            raise capo_codedeploy.errors.invalid_instance_type_exception.InvalidInstanceTypeException.from_aws_json_1_1(
                data
            )
        case "InvalidNextTokenException":
            raise capo_codedeploy.errors.invalid_next_token_exception.InvalidNextTokenException.from_aws_json_1_1(
                data
            )
        case "InvalidTargetFilterNameException":
            raise capo_codedeploy.errors.invalid_target_filter_name_exception.InvalidTargetFilterNameException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput
):
    out: capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput = capo_codedeploy.types.list_deployment_instances_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput
):
    out: capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput = capo_codedeploy.types.list_deployment_instances_output.deserialize_aws_json_1_1(
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
    input_: capo_codedeploy.types.list_deployment_instances_input.ListDeploymentInstancesInput,
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
    headers["X-Amz-Target"] = "CodeDeploy_20141006.ListDeploymentInstances"
    body: bytes | None = json.dumps(
        capo_codedeploy.types.list_deployment_instances_input.serialize_aws_json_1_1(
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


def list_deployment_instances(
    options: OperationOptions,
    input_: capo_codedeploy.types.list_deployment_instances_input.ListDeploymentInstancesInput,
) -> tuple[
    capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput,
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


async def async_list_deployment_instances(
    options: AsyncOperationOptions,
    input_: capo_codedeploy.types.list_deployment_instances_input.ListDeploymentInstancesInput,
) -> tuple[
    capo_codedeploy.types.list_deployment_instances_output.ListDeploymentInstancesOutput,
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
