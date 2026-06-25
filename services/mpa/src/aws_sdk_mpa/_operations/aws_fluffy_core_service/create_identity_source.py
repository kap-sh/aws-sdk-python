"""Generated from Smithy shape ``com.amazonaws.mpa#CreateIdentitySource``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_mpa._auth._signers
import aws_sdk_mpa._auth._sigv4
import aws_sdk_mpa.errors.access_denied_exception
import aws_sdk_mpa.errors.internal_server_exception
import aws_sdk_mpa.errors.service_quota_exceeded_exception
import aws_sdk_mpa.errors.throttling_exception
import aws_sdk_mpa.errors.validation_exception
import aws_sdk_mpa.types.create_identity_source_request
import aws_sdk_mpa.types.create_identity_source_response
import aws_sdk_mpa.types.identity_source_parameters
import aws_sdk_mpa.types.identity_source_type
import aws_sdk_mpa.types.iso_timestamp
import aws_sdk_mpa.types.tags
from aws_sdk_mpa._protocol.errors import parse_error_metadata_json
from aws_sdk_mpa._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_mpa._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_mpa.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_mpa.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_mpa.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise aws_sdk_mpa.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_mpa.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_mpa.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_mpa.types.create_identity_source_response.CreateIdentitySourceResponse:
    out: aws_sdk_mpa.types.create_identity_source_response.CreateIdentitySourceResponse = aws_sdk_mpa.types.create_identity_source_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_mpa.types.create_identity_source_response.CreateIdentitySourceResponse:
    out: aws_sdk_mpa.types.create_identity_source_response.CreateIdentitySourceResponse = aws_sdk_mpa.types.create_identity_source_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_mpa._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_mpa._auth._sigv4.build_sigv4_auth_scheme("mpa", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_mpa._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_mpa.types.create_identity_source_request.CreateIdentitySourceRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/identity-sources"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_mpa.types.create_identity_source_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_identity_source(
    options: OperationOptions,
    input_: aws_sdk_mpa.types.create_identity_source_request.CreateIdentitySourceRequest,
) -> tuple[
    aws_sdk_mpa.types.create_identity_source_response.CreateIdentitySourceResponse,
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


async def async_create_identity_source(
    options: AsyncOperationOptions,
    input_: aws_sdk_mpa.types.create_identity_source_request.CreateIdentitySourceRequest,
) -> tuple[
    aws_sdk_mpa.types.create_identity_source_response.CreateIdentitySourceResponse,
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
