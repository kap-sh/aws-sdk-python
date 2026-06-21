"""Generated from Smithy shape ``com.amazonaws.sfn#StartExecution``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_sfn._auth._signers
import aws_sdk_sfn._auth._sigv4
import aws_sdk_sfn.errors.execution_already_exists
import aws_sdk_sfn.errors.execution_limit_exceeded
import aws_sdk_sfn.errors.invalid_arn
import aws_sdk_sfn.errors.invalid_execution_input
import aws_sdk_sfn.errors.invalid_name
import aws_sdk_sfn.errors.kms_access_denied_exception
import aws_sdk_sfn.errors.kms_invalid_state_exception
import aws_sdk_sfn.errors.kms_throttling_exception
import aws_sdk_sfn.errors.state_machine_deleting
import aws_sdk_sfn.errors.state_machine_does_not_exist
import aws_sdk_sfn.errors.validation_exception
import aws_sdk_sfn.types.start_execution_input
import aws_sdk_sfn.types.start_execution_output
import aws_sdk_sfn.types.timestamp
from aws_sdk_sfn._protocol.errors import parse_error_metadata_json
from aws_sdk_sfn._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_sfn._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_sfn.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ExecutionAlreadyExists":
            raise aws_sdk_sfn.errors.execution_already_exists.ExecutionAlreadyExists.from_aws_json_1_0(
                data
            )
        case "ExecutionLimitExceeded":
            raise aws_sdk_sfn.errors.execution_limit_exceeded.ExecutionLimitExceeded.from_aws_json_1_0(
                data
            )
        case "InvalidArn":
            raise aws_sdk_sfn.errors.invalid_arn.InvalidArn.from_aws_json_1_0(data)
        case "InvalidExecutionInput":
            raise aws_sdk_sfn.errors.invalid_execution_input.InvalidExecutionInput.from_aws_json_1_0(
                data
            )
        case "InvalidName":
            raise aws_sdk_sfn.errors.invalid_name.InvalidName.from_aws_json_1_0(data)
        case "KmsAccessDeniedException":
            raise aws_sdk_sfn.errors.kms_access_denied_exception.KmsAccessDeniedException.from_aws_json_1_0(
                data
            )
        case "KmsInvalidStateException":
            raise aws_sdk_sfn.errors.kms_invalid_state_exception.KmsInvalidStateException.from_aws_json_1_0(
                data
            )
        case "KmsThrottlingException":
            raise aws_sdk_sfn.errors.kms_throttling_exception.KmsThrottlingException.from_aws_json_1_0(
                data
            )
        case "StateMachineDeleting":
            raise aws_sdk_sfn.errors.state_machine_deleting.StateMachineDeleting.from_aws_json_1_0(
                data
            )
        case "StateMachineDoesNotExist":
            raise aws_sdk_sfn.errors.state_machine_does_not_exist.StateMachineDoesNotExist.from_aws_json_1_0(
                data
            )
        case "ValidationException":
            raise aws_sdk_sfn.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_sfn.types.start_execution_output.StartExecutionOutput:
    out: aws_sdk_sfn.types.start_execution_output.StartExecutionOutput = (
        aws_sdk_sfn.types.start_execution_output.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_sfn.types.start_execution_output.StartExecutionOutput:
    out: aws_sdk_sfn.types.start_execution_output.StartExecutionOutput = (
        aws_sdk_sfn.types.start_execution_output.deserialize_aws_json_1_0(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sfn._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sfn._auth._sigv4.build_sigv4_auth_scheme(
                "states", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_sfn._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_sfn.types.start_execution_input.StartExecutionInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSStepFunctions.StartExecution"
    import aws_sdk_sfn.types.start_execution_input

    body: bytes | None = json.dumps(
        aws_sdk_sfn.types.start_execution_input.serialize_aws_json_1_0(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_execution(
    options: OperationOptions,
    input_: aws_sdk_sfn.types.start_execution_input.StartExecutionInput,
) -> tuple[
    aws_sdk_sfn.types.start_execution_output.StartExecutionOutput, zapros.Response
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


async def async_start_execution(
    options: AsyncOperationOptions,
    input_: aws_sdk_sfn.types.start_execution_input.StartExecutionInput,
) -> tuple[
    aws_sdk_sfn.types.start_execution_output.StartExecutionOutput, zapros.Response
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
