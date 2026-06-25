"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateDirectorySetup``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_directory_service._auth._signers
import aws_sdk_directory_service._auth._sigv4
import aws_sdk_directory_service.errors.access_denied_exception
import aws_sdk_directory_service.errors.client_exception
import aws_sdk_directory_service.errors.directory_does_not_exist_exception
import aws_sdk_directory_service.errors.directory_in_desired_state_exception
import aws_sdk_directory_service.errors.directory_unavailable_exception
import aws_sdk_directory_service.errors.invalid_parameter_exception
import aws_sdk_directory_service.errors.service_exception
import aws_sdk_directory_service.errors.snapshot_limit_exceeded_exception
import aws_sdk_directory_service.errors.unsupported_operation_exception
import aws_sdk_directory_service.types.directory_size_update_settings
import aws_sdk_directory_service.types.network_update_settings
import aws_sdk_directory_service.types.os_update_settings
import aws_sdk_directory_service.types.update_directory_setup_request
import aws_sdk_directory_service.types.update_directory_setup_result
import aws_sdk_directory_service.types.update_type
from aws_sdk_directory_service._protocol.errors import parse_error_metadata_json
from aws_sdk_directory_service._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_directory_service._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_directory_service.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_directory_service.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "ClientException":
            raise aws_sdk_directory_service.errors.client_exception.ClientException.from_aws_json_1_1(
                data
            )
        case "DirectoryDoesNotExistException":
            raise aws_sdk_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "DirectoryInDesiredStateException":
            raise aws_sdk_directory_service.errors.directory_in_desired_state_exception.DirectoryInDesiredStateException.from_aws_json_1_1(
                data
            )
        case "DirectoryUnavailableException":
            raise aws_sdk_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise aws_sdk_directory_service.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "ServiceException":
            raise aws_sdk_directory_service.errors.service_exception.ServiceException.from_aws_json_1_1(
                data
            )
        case "SnapshotLimitExceededException":
            raise aws_sdk_directory_service.errors.snapshot_limit_exceeded_exception.SnapshotLimitExceededException.from_aws_json_1_1(
                data
            )
        case "UnsupportedOperationException":
            raise aws_sdk_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_directory_service.types.update_directory_setup_result.UpdateDirectorySetupResult:
    out: aws_sdk_directory_service.types.update_directory_setup_result.UpdateDirectorySetupResult = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_directory_service.types.update_directory_setup_result.UpdateDirectorySetupResult:
    out: aws_sdk_directory_service.types.update_directory_setup_result.UpdateDirectorySetupResult = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_directory_service._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_directory_service._auth._sigv4.build_sigv4_auth_scheme(
                "ds", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_directory_service._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_directory_service.types.update_directory_setup_request.UpdateDirectorySetupRequest,
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
    headers["X-Amz-Target"] = "DirectoryService_20150416.UpdateDirectorySetup"
    body: bytes | None = json.dumps(
        aws_sdk_directory_service.types.update_directory_setup_request.serialize_aws_json_1_1(
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


def update_directory_setup(
    options: OperationOptions,
    input_: aws_sdk_directory_service.types.update_directory_setup_request.UpdateDirectorySetupRequest,
) -> tuple[
    aws_sdk_directory_service.types.update_directory_setup_result.UpdateDirectorySetupResult,
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


async def async_update_directory_setup(
    options: AsyncOperationOptions,
    input_: aws_sdk_directory_service.types.update_directory_setup_request.UpdateDirectorySetupRequest,
) -> tuple[
    aws_sdk_directory_service.types.update_directory_setup_result.UpdateDirectorySetupResult,
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
