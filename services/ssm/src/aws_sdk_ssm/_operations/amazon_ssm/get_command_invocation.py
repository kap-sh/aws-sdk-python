"""Generated from Smithy shape ``com.amazonaws.ssm#GetCommandInvocation``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_ssm._auth._signers
import aws_sdk_ssm._auth._sigv4
import aws_sdk_ssm.errors.internal_server_error
import aws_sdk_ssm.errors.invalid_command_id
import aws_sdk_ssm.errors.invalid_instance_id
import aws_sdk_ssm.errors.invalid_plugin_name
import aws_sdk_ssm.errors.invocation_does_not_exist
import aws_sdk_ssm.types.cloud_watch_output_config
import aws_sdk_ssm.types.command_invocation_status
import aws_sdk_ssm.types.get_command_invocation_request
import aws_sdk_ssm.types.get_command_invocation_result
from aws_sdk_ssm._protocol.errors import parse_error_metadata_json
from aws_sdk_ssm._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_ssm._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_ssm.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerError":
            raise aws_sdk_ssm.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case "InvalidCommandId":
            raise aws_sdk_ssm.errors.invalid_command_id.InvalidCommandId.from_aws_json_1_1(
                data
            )
        case "InvalidInstanceId":
            raise aws_sdk_ssm.errors.invalid_instance_id.InvalidInstanceId.from_aws_json_1_1(
                data
            )
        case "InvalidPluginName":
            raise aws_sdk_ssm.errors.invalid_plugin_name.InvalidPluginName.from_aws_json_1_1(
                data
            )
        case "InvocationDoesNotExist":
            raise aws_sdk_ssm.errors.invocation_does_not_exist.InvocationDoesNotExist.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_ssm.types.get_command_invocation_result.GetCommandInvocationResult:
    out: aws_sdk_ssm.types.get_command_invocation_result.GetCommandInvocationResult = (
        aws_sdk_ssm.types.get_command_invocation_result.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_ssm.types.get_command_invocation_result.GetCommandInvocationResult:
    out: aws_sdk_ssm.types.get_command_invocation_result.GetCommandInvocationResult = (
        aws_sdk_ssm.types.get_command_invocation_result.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_ssm._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_ssm._auth._sigv4.build_sigv4_auth_scheme("ssm", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_ssm._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_ssm.types.get_command_invocation_request.GetCommandInvocationRequest,
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
    headers["X-Amz-Target"] = "AmazonSSM.GetCommandInvocation"
    body: bytes | None = json.dumps(
        aws_sdk_ssm.types.get_command_invocation_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def get_command_invocation(
    options: OperationOptions,
    input_: aws_sdk_ssm.types.get_command_invocation_request.GetCommandInvocationRequest,
) -> tuple[
    aws_sdk_ssm.types.get_command_invocation_result.GetCommandInvocationResult,
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


async def async_get_command_invocation(
    options: AsyncOperationOptions,
    input_: aws_sdk_ssm.types.get_command_invocation_request.GetCommandInvocationRequest,
) -> tuple[
    aws_sdk_ssm.types.get_command_invocation_result.GetCommandInvocationResult,
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
