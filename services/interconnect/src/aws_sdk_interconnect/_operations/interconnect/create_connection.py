"""Generated from Smithy shape ``com.amazonaws.interconnect#CreateConnection``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_interconnect._auth._signers
import aws_sdk_interconnect._auth._sigv4
import aws_sdk_interconnect.errors.access_denied_exception
import aws_sdk_interconnect.errors.interconnect_client_exception
import aws_sdk_interconnect.errors.interconnect_server_exception
import aws_sdk_interconnect.errors.interconnect_validation_exception
import aws_sdk_interconnect.errors.resource_not_found_exception
import aws_sdk_interconnect.errors.service_quota_exceeded_exception
import aws_sdk_interconnect.errors.throttling_exception
import aws_sdk_interconnect.types.attach_point
import aws_sdk_interconnect.types.connection
import aws_sdk_interconnect.types.create_connection_request
import aws_sdk_interconnect.types.create_connection_response
import aws_sdk_interconnect.types.remote_account_identifier
import aws_sdk_interconnect.types.tag_map
from aws_sdk_interconnect._protocol.errors import parse_error_metadata_json
from aws_sdk_interconnect._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_interconnect._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_interconnect.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_interconnect.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data
            )
        case "InterconnectClientException":
            raise aws_sdk_interconnect.errors.interconnect_client_exception.InterconnectClientException.from_aws_json_1_0(
                data
            )
        case "InterconnectServerException":
            raise aws_sdk_interconnect.errors.interconnect_server_exception.InterconnectServerException.from_aws_json_1_0(
                data
            )
        case "InterconnectValidationException":
            raise aws_sdk_interconnect.errors.interconnect_validation_exception.InterconnectValidationException.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_interconnect.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ServiceQuotaExceededException":
            raise aws_sdk_interconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_interconnect.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_interconnect.types.create_connection_response.CreateConnectionResponse:
    out: aws_sdk_interconnect.types.create_connection_response.CreateConnectionResponse = aws_sdk_interconnect.types.create_connection_response.deserialize_aws_json_1_0(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_interconnect.types.create_connection_response.CreateConnectionResponse:
    out: aws_sdk_interconnect.types.create_connection_response.CreateConnectionResponse = aws_sdk_interconnect.types.create_connection_response.deserialize_aws_json_1_0(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_interconnect._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_interconnect._auth._sigv4.build_sigv4_auth_scheme(
                "interconnect", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_interconnect._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_interconnect.types.create_connection_request.CreateConnectionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "Interconnect.CreateConnection"
    body: bytes | None = json.dumps(
        aws_sdk_interconnect.types.create_connection_request.serialize_aws_json_1_0(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_connection(
    options: OperationOptions,
    input_: aws_sdk_interconnect.types.create_connection_request.CreateConnectionRequest,
) -> tuple[
    aws_sdk_interconnect.types.create_connection_response.CreateConnectionResponse,
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


async def async_create_connection(
    options: AsyncOperationOptions,
    input_: aws_sdk_interconnect.types.create_connection_request.CreateConnectionRequest,
) -> tuple[
    aws_sdk_interconnect.types.create_connection_response.CreateConnectionResponse,
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
