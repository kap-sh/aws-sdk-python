"""Generated from Smithy shape ``com.amazonaws.ssm#StartChangeRequestExecution``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_ssm._auth._signers
import aws_sdk_ssm._auth._sigv4
import aws_sdk_ssm.errors.automation_definition_not_approved_exception
import aws_sdk_ssm.errors.automation_definition_not_found_exception
import aws_sdk_ssm.errors.automation_definition_version_not_found_exception
import aws_sdk_ssm.errors.automation_execution_limit_exceeded_exception
import aws_sdk_ssm.errors.idempotent_parameter_mismatch
import aws_sdk_ssm.errors.internal_server_error
import aws_sdk_ssm.errors.invalid_automation_execution_parameters_exception
import aws_sdk_ssm.errors.no_longer_supported_exception
import aws_sdk_ssm.types.automation_parameter_map
import aws_sdk_ssm.types.date_time
import aws_sdk_ssm.types.runbooks
import aws_sdk_ssm.types.start_change_request_execution_request
import aws_sdk_ssm.types.start_change_request_execution_result
import aws_sdk_ssm.types.tag_list
from aws_sdk_ssm._protocol.errors import parse_error_metadata_json
from aws_sdk_ssm._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_ssm._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_ssm.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AutomationDefinitionNotApprovedException":
            raise aws_sdk_ssm.errors.automation_definition_not_approved_exception.AutomationDefinitionNotApprovedException.from_aws_json_1_1(
                data
            )
        case "AutomationDefinitionNotFoundException":
            raise aws_sdk_ssm.errors.automation_definition_not_found_exception.AutomationDefinitionNotFoundException.from_aws_json_1_1(
                data
            )
        case "AutomationDefinitionVersionNotFoundException":
            raise aws_sdk_ssm.errors.automation_definition_version_not_found_exception.AutomationDefinitionVersionNotFoundException.from_aws_json_1_1(
                data
            )
        case "AutomationExecutionLimitExceededException":
            raise aws_sdk_ssm.errors.automation_execution_limit_exceeded_exception.AutomationExecutionLimitExceededException.from_aws_json_1_1(
                data
            )
        case "IdempotentParameterMismatch":
            raise aws_sdk_ssm.errors.idempotent_parameter_mismatch.IdempotentParameterMismatch.from_aws_json_1_1(
                data
            )
        case "InternalServerError":
            raise aws_sdk_ssm.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case "InvalidAutomationExecutionParametersException":
            raise aws_sdk_ssm.errors.invalid_automation_execution_parameters_exception.InvalidAutomationExecutionParametersException.from_aws_json_1_1(
                data
            )
        case "NoLongerSupportedException":
            raise aws_sdk_ssm.errors.no_longer_supported_exception.NoLongerSupportedException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_ssm.types.start_change_request_execution_result.StartChangeRequestExecutionResult:
    out: aws_sdk_ssm.types.start_change_request_execution_result.StartChangeRequestExecutionResult = aws_sdk_ssm.types.start_change_request_execution_result.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_ssm.types.start_change_request_execution_result.StartChangeRequestExecutionResult:
    out: aws_sdk_ssm.types.start_change_request_execution_result.StartChangeRequestExecutionResult = aws_sdk_ssm.types.start_change_request_execution_result.deserialize_aws_json_1_1(
        json.loads(await response.aread())
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
    input_: aws_sdk_ssm.types.start_change_request_execution_request.StartChangeRequestExecutionRequest,
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
    headers["X-Amz-Target"] = "AmazonSSM.StartChangeRequestExecution"
    import aws_sdk_ssm.types.start_change_request_execution_request

    body: bytes | None = json.dumps(
        aws_sdk_ssm.types.start_change_request_execution_request.serialize_aws_json_1_1(
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


def start_change_request_execution(
    options: OperationOptions,
    input_: aws_sdk_ssm.types.start_change_request_execution_request.StartChangeRequestExecutionRequest,
) -> tuple[
    aws_sdk_ssm.types.start_change_request_execution_result.StartChangeRequestExecutionResult,
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


async def async_start_change_request_execution(
    options: AsyncOperationOptions,
    input_: aws_sdk_ssm.types.start_change_request_execution_request.StartChangeRequestExecutionRequest,
) -> tuple[
    aws_sdk_ssm.types.start_change_request_execution_result.StartChangeRequestExecutionResult,
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
