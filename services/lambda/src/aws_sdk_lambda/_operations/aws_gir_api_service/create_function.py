"""Generated from Smithy shape ``com.amazonaws.lambda#CreateFunction``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_lambda._auth._signers
import aws_sdk_lambda._auth._sigv4
import aws_sdk_lambda.errors.code_signing_config_not_found_exception
import aws_sdk_lambda.errors.code_storage_exceeded_exception
import aws_sdk_lambda.errors.code_verification_failed_exception
import aws_sdk_lambda.errors.function_versions_per_capacity_provider_limit_exceeded_exception
import aws_sdk_lambda.errors.invalid_code_signature_exception
import aws_sdk_lambda.errors.invalid_parameter_value_exception
import aws_sdk_lambda.errors.resource_conflict_exception
import aws_sdk_lambda.errors.resource_not_found_exception
import aws_sdk_lambda.errors.service_exception
import aws_sdk_lambda.errors.too_many_requests_exception
import aws_sdk_lambda.types.architectures_list
import aws_sdk_lambda.types.capacity_provider_config
import aws_sdk_lambda.types.create_function_request
import aws_sdk_lambda.types.dead_letter_config
import aws_sdk_lambda.types.durable_config
import aws_sdk_lambda.types.environment
import aws_sdk_lambda.types.environment_response
import aws_sdk_lambda.types.ephemeral_storage
import aws_sdk_lambda.types.file_system_config_list
import aws_sdk_lambda.types.function_code
import aws_sdk_lambda.types.function_configuration
import aws_sdk_lambda.types.function_version_latest_published
import aws_sdk_lambda.types.image_config
import aws_sdk_lambda.types.image_config_response
import aws_sdk_lambda.types.last_update_status
import aws_sdk_lambda.types.last_update_status_reason_code
import aws_sdk_lambda.types.layer_list
import aws_sdk_lambda.types.layers_reference_list
import aws_sdk_lambda.types.logging_config
import aws_sdk_lambda.types.package_type
import aws_sdk_lambda.types.runtime
import aws_sdk_lambda.types.runtime_version_config
import aws_sdk_lambda.types.snap_start
import aws_sdk_lambda.types.snap_start_response
import aws_sdk_lambda.types.state
import aws_sdk_lambda.types.state_reason_code
import aws_sdk_lambda.types.tags
import aws_sdk_lambda.types.tenancy_config
import aws_sdk_lambda.types.tracing_config
import aws_sdk_lambda.types.tracing_config_response
import aws_sdk_lambda.types.vpc_config
import aws_sdk_lambda.types.vpc_config_response
from aws_sdk_lambda._protocol.errors import parse_error_metadata_json
from aws_sdk_lambda._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_lambda._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_lambda.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CodeSigningConfigNotFoundException":
            raise aws_sdk_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException.from_json(
                data
            )
        case "CodeStorageExceededException":
            raise aws_sdk_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException.from_json(
                data
            )
        case "CodeVerificationFailedException":
            raise aws_sdk_lambda.errors.code_verification_failed_exception.CodeVerificationFailedException.from_json(
                data
            )
        case "FunctionVersionsPerCapacityProviderLimitExceededException":
            raise aws_sdk_lambda.errors.function_versions_per_capacity_provider_limit_exceeded_exception.FunctionVersionsPerCapacityProviderLimitExceededException.from_json(
                data
            )
        case "InvalidCodeSignatureException":
            raise aws_sdk_lambda.errors.invalid_code_signature_exception.InvalidCodeSignatureException.from_json(
                data
            )
        case "InvalidParameterValueException":
            raise aws_sdk_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "ResourceConflictException":
            raise aws_sdk_lambda.errors.resource_conflict_exception.ResourceConflictException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_lambda.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceException":
            raise aws_sdk_lambda.errors.service_exception.ServiceException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_lambda.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_lambda.types.function_configuration.FunctionConfiguration:
    out: aws_sdk_lambda.types.function_configuration.FunctionConfiguration = (
        aws_sdk_lambda.types.function_configuration.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_lambda.types.function_configuration.FunctionConfiguration:
    out: aws_sdk_lambda.types.function_configuration.FunctionConfiguration = (
        aws_sdk_lambda.types.function_configuration.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_lambda._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_lambda._auth._sigv4.build_sigv4_auth_scheme(
                "lambda", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_lambda._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_lambda.types.create_function_request.CreateFunctionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2015-03-31/functions"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_lambda.types.create_function_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_function(
    options: OperationOptions,
    input_: aws_sdk_lambda.types.create_function_request.CreateFunctionRequest,
) -> tuple[
    aws_sdk_lambda.types.function_configuration.FunctionConfiguration, zapros.Response
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


async def async_create_function(
    options: AsyncOperationOptions,
    input_: aws_sdk_lambda.types.create_function_request.CreateFunctionRequest,
) -> tuple[
    aws_sdk_lambda.types.function_configuration.FunctionConfiguration, zapros.Response
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
