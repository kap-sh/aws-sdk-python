"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#CreateResource``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_cloudcontrol._auth._signers
import aws_sdk_cloudcontrol._auth._sigv4
from aws_sdk_cloudcontrol._protocol.errors import parse_error_metadata_json
from aws_sdk_cloudcontrol._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudcontrol._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudcontrol.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.create_resource_input
    import aws_sdk_cloudcontrol.types.create_resource_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AlreadyExistsException":
            import aws_sdk_cloudcontrol.errors.already_exists_exception

            raise aws_sdk_cloudcontrol.errors.already_exists_exception.AlreadyExistsException.from_aws_json_1_0(
                data
            )
        case "ClientTokenConflictException":
            import aws_sdk_cloudcontrol.errors.client_token_conflict_exception

            raise aws_sdk_cloudcontrol.errors.client_token_conflict_exception.ClientTokenConflictException.from_aws_json_1_0(
                data
            )
        case "ConcurrentOperationException":
            import aws_sdk_cloudcontrol.errors.concurrent_operation_exception

            raise aws_sdk_cloudcontrol.errors.concurrent_operation_exception.ConcurrentOperationException.from_aws_json_1_0(
                data
            )
        case "GeneralServiceException":
            import aws_sdk_cloudcontrol.errors.general_service_exception

            raise aws_sdk_cloudcontrol.errors.general_service_exception.GeneralServiceException.from_aws_json_1_0(
                data
            )
        case "HandlerFailureException":
            import aws_sdk_cloudcontrol.errors.handler_failure_exception

            raise aws_sdk_cloudcontrol.errors.handler_failure_exception.HandlerFailureException.from_aws_json_1_0(
                data
            )
        case "HandlerInternalFailureException":
            import aws_sdk_cloudcontrol.errors.handler_internal_failure_exception

            raise aws_sdk_cloudcontrol.errors.handler_internal_failure_exception.HandlerInternalFailureException.from_aws_json_1_0(
                data
            )
        case "InvalidCredentialsException":
            import aws_sdk_cloudcontrol.errors.invalid_credentials_exception

            raise aws_sdk_cloudcontrol.errors.invalid_credentials_exception.InvalidCredentialsException.from_aws_json_1_0(
                data
            )
        case "InvalidRequestException":
            import aws_sdk_cloudcontrol.errors.invalid_request_exception

            raise aws_sdk_cloudcontrol.errors.invalid_request_exception.InvalidRequestException.from_aws_json_1_0(
                data
            )
        case "NetworkFailureException":
            import aws_sdk_cloudcontrol.errors.network_failure_exception

            raise aws_sdk_cloudcontrol.errors.network_failure_exception.NetworkFailureException.from_aws_json_1_0(
                data
            )
        case "NotStabilizedException":
            import aws_sdk_cloudcontrol.errors.not_stabilized_exception

            raise aws_sdk_cloudcontrol.errors.not_stabilized_exception.NotStabilizedException.from_aws_json_1_0(
                data
            )
        case "NotUpdatableException":
            import aws_sdk_cloudcontrol.errors.not_updatable_exception

            raise aws_sdk_cloudcontrol.errors.not_updatable_exception.NotUpdatableException.from_aws_json_1_0(
                data
            )
        case "PrivateTypeException":
            import aws_sdk_cloudcontrol.errors.private_type_exception

            raise aws_sdk_cloudcontrol.errors.private_type_exception.PrivateTypeException.from_aws_json_1_0(
                data
            )
        case "ResourceConflictException":
            import aws_sdk_cloudcontrol.errors.resource_conflict_exception

            raise aws_sdk_cloudcontrol.errors.resource_conflict_exception.ResourceConflictException.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_cloudcontrol.errors.resource_not_found_exception

            raise aws_sdk_cloudcontrol.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ServiceInternalErrorException":
            import aws_sdk_cloudcontrol.errors.service_internal_error_exception

            raise aws_sdk_cloudcontrol.errors.service_internal_error_exception.ServiceInternalErrorException.from_aws_json_1_0(
                data
            )
        case "ServiceLimitExceededException":
            import aws_sdk_cloudcontrol.errors.service_limit_exceeded_exception

            raise aws_sdk_cloudcontrol.errors.service_limit_exceeded_exception.ServiceLimitExceededException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            import aws_sdk_cloudcontrol.errors.throttling_exception

            raise aws_sdk_cloudcontrol.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case "TypeNotFoundException":
            import aws_sdk_cloudcontrol.errors.type_not_found_exception

            raise aws_sdk_cloudcontrol.errors.type_not_found_exception.TypeNotFoundException.from_aws_json_1_0(
                data
            )
        case "UnsupportedActionException":
            import aws_sdk_cloudcontrol.errors.unsupported_action_exception

            raise aws_sdk_cloudcontrol.errors.unsupported_action_exception.UnsupportedActionException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudcontrol.types.create_resource_output.CreateResourceOutput:
    import aws_sdk_cloudcontrol.types.create_resource_output

    out: aws_sdk_cloudcontrol.types.create_resource_output.CreateResourceOutput = (
        aws_sdk_cloudcontrol.types.create_resource_output.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudcontrol._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudcontrol._auth._sigv4.build_sigv4_auth_scheme(
                "cloudcontrolapi", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudcontrol._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cloudcontrol.types.create_resource_input.CreateResourceInput,
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
    headers["X-Amz-Target"] = "CloudApiService.CreateResource"
    import aws_sdk_cloudcontrol.types.create_resource_input

    body: bytes | None = json.dumps(
        aws_sdk_cloudcontrol.types.create_resource_input.serialize_aws_json_1_0(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_resource(
    options: OperationOptions,
    input_: aws_sdk_cloudcontrol.types.create_resource_input.CreateResourceInput,
) -> tuple[
    aws_sdk_cloudcontrol.types.create_resource_output.CreateResourceOutput,
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


async def async_create_resource(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudcontrol.types.create_resource_input.CreateResourceInput,
) -> tuple[
    aws_sdk_cloudcontrol.types.create_resource_output.CreateResourceOutput,
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
