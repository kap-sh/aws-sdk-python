"""Generated from Smithy shape ``com.amazonaws.sfn#ListExecutions``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_sfn._auth._signers
import aws_sdk_sfn._auth._sigv4
from aws_sdk_sfn._protocol.errors import parse_error_metadata_json
from aws_sdk_sfn._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_sfn._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_sfn.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.list_executions_input
    import aws_sdk_sfn.types.list_executions_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidArn":
            import aws_sdk_sfn.errors.invalid_arn

            raise aws_sdk_sfn.errors.invalid_arn.InvalidArn.from_aws_json_1_0(data)
        case "InvalidToken":
            import aws_sdk_sfn.errors.invalid_token

            raise aws_sdk_sfn.errors.invalid_token.InvalidToken.from_aws_json_1_0(data)
        case "ResourceNotFound":
            import aws_sdk_sfn.errors.resource_not_found

            raise aws_sdk_sfn.errors.resource_not_found.ResourceNotFound.from_aws_json_1_0(
                data
            )
        case "StateMachineDoesNotExist":
            import aws_sdk_sfn.errors.state_machine_does_not_exist

            raise aws_sdk_sfn.errors.state_machine_does_not_exist.StateMachineDoesNotExist.from_aws_json_1_0(
                data
            )
        case "StateMachineTypeNotSupported":
            import aws_sdk_sfn.errors.state_machine_type_not_supported

            raise aws_sdk_sfn.errors.state_machine_type_not_supported.StateMachineTypeNotSupported.from_aws_json_1_0(
                data
            )
        case "ValidationException":
            import aws_sdk_sfn.errors.validation_exception

            raise aws_sdk_sfn.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_sfn.types.list_executions_output.ListExecutionsOutput:
    import aws_sdk_sfn.types.list_executions_output

    out: aws_sdk_sfn.types.list_executions_output.ListExecutionsOutput = (
        aws_sdk_sfn.types.list_executions_output.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sfn._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input: aws_sdk_sfn.types.list_executions_input.ListExecutionsInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSStepFunctions.ListExecutions"
    import aws_sdk_sfn.types.list_executions_input

    body: bytes | None = json.dumps(
        aws_sdk_sfn.types.list_executions_input.serialize_aws_json_1_0(input)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def list_executions(
    options: OperationOptions,
    input: aws_sdk_sfn.types.list_executions_input.ListExecutionsInput,
) -> tuple[
    aws_sdk_sfn.types.list_executions_output.ListExecutionsOutput, zapros.Response
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_list_executions(
    options: AsyncOperationOptions,
    input: aws_sdk_sfn.types.list_executions_input.ListExecutionsInput,
) -> tuple[
    aws_sdk_sfn.types.list_executions_output.ListExecutionsOutput, zapros.Response
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
