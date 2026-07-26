"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeUpdateDirectory``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_directory_service._auth._signers
import capo_directory_service._auth._sigv4
import capo_directory_service.errors.access_denied_exception
import capo_directory_service.errors.client_exception
import capo_directory_service.errors.directory_does_not_exist_exception
import capo_directory_service.errors.invalid_next_token_exception
import capo_directory_service.errors.invalid_parameter_exception
import capo_directory_service.errors.service_exception
import capo_directory_service.types.describe_update_directory_request
import capo_directory_service.types.describe_update_directory_result
import capo_directory_service.types.update_activities
import capo_directory_service.types.update_type
from capo_directory_service._protocol.errors import parse_error_metadata_json
from capo_directory_service._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_directory_service._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_directory_service.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_directory_service.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "ClientException":
            raise capo_directory_service.errors.client_exception.ClientException.from_aws_json_1_1(
                data
            )
        case "DirectoryDoesNotExistException":
            raise capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "InvalidNextTokenException":
            raise capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "ServiceException":
            raise capo_directory_service.errors.service_exception.ServiceException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_directory_service.types.describe_update_directory_result.DescribeUpdateDirectoryResult:
    out: capo_directory_service.types.describe_update_directory_result.DescribeUpdateDirectoryResult = capo_directory_service.types.describe_update_directory_result.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_directory_service.types.describe_update_directory_result.DescribeUpdateDirectoryResult:
    out: capo_directory_service.types.describe_update_directory_result.DescribeUpdateDirectoryResult = capo_directory_service.types.describe_update_directory_result.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_directory_service._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_directory_service._auth._sigv4.build_sigv4_auth_scheme(
                "ds", options.region
            )
        )
        if sigv4_config is not None:
            return capo_directory_service._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_directory_service.types.describe_update_directory_request.DescribeUpdateDirectoryRequest,
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
    headers["X-Amz-Target"] = "DirectoryService_20150416.DescribeUpdateDirectory"
    body: bytes | None = json.dumps(
        capo_directory_service.types.describe_update_directory_request.serialize_aws_json_1_1(
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


def describe_update_directory(
    options: OperationOptions,
    input_: capo_directory_service.types.describe_update_directory_request.DescribeUpdateDirectoryRequest,
) -> tuple[
    capo_directory_service.types.describe_update_directory_result.DescribeUpdateDirectoryResult,
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


async def async_describe_update_directory(
    options: AsyncOperationOptions,
    input_: capo_directory_service.types.describe_update_directory_request.DescribeUpdateDirectoryRequest,
) -> tuple[
    capo_directory_service.types.describe_update_directory_result.DescribeUpdateDirectoryResult,
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
