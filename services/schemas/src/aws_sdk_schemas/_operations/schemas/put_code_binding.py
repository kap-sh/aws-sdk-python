"""Generated from Smithy shape ``com.amazonaws.schemas#PutCodeBinding``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_schemas._auth._signers
import aws_sdk_schemas._auth._sigv4
import aws_sdk_schemas.errors.bad_request_exception
import aws_sdk_schemas.errors.forbidden_exception
import aws_sdk_schemas.errors.gone_exception
import aws_sdk_schemas.errors.internal_server_error_exception
import aws_sdk_schemas.errors.not_found_exception
import aws_sdk_schemas.errors.too_many_requests_exception
import aws_sdk_schemas.errors.unauthorized_exception
import aws_sdk_schemas.types.__timestamp_iso8601
import aws_sdk_schemas.types.code_generation_status
import aws_sdk_schemas.types.put_code_binding_request
import aws_sdk_schemas.types.put_code_binding_response
from aws_sdk_schemas._protocol.errors import parse_error_metadata_json
from aws_sdk_schemas._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_schemas._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_schemas.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise aws_sdk_schemas.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ForbiddenException":
            raise aws_sdk_schemas.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "GoneException":
            raise aws_sdk_schemas.errors.gone_exception.GoneException.from_json(data)
        case "InternalServerErrorException":
            raise aws_sdk_schemas.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "NotFoundException":
            raise aws_sdk_schemas.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_schemas.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case "UnauthorizedException":
            raise aws_sdk_schemas.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_schemas.types.put_code_binding_response.PutCodeBindingResponse:
    out: aws_sdk_schemas.types.put_code_binding_response.PutCodeBindingResponse = (
        aws_sdk_schemas.types.put_code_binding_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_schemas.types.put_code_binding_response.PutCodeBindingResponse:
    out: aws_sdk_schemas.types.put_code_binding_response.PutCodeBindingResponse = (
        aws_sdk_schemas.types.put_code_binding_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_schemas._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_schemas._auth._sigv4.build_sigv4_auth_scheme(
                "schemas", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_schemas._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_schemas.types.put_code_binding_request.PutCodeBindingRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/v1/registries/name/{RegistryName}/schemas/name/{SchemaName}/language/{Language}"
    )
    url = url.replace("{Language}", quote(str(input_["language"]), safe=""))
    url = url.replace("{RegistryName}", quote(str(input_["registry_name"]), safe=""))
    url = url.replace("{SchemaName}", quote(str(input_["schema_name"]), safe=""))
    params: dict[str, str] = {}
    if "schema_version" in input_:
        params["schemaVersion"] = str(input_["schema_version"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def put_code_binding(
    options: OperationOptions,
    input_: aws_sdk_schemas.types.put_code_binding_request.PutCodeBindingRequest,
) -> tuple[
    aws_sdk_schemas.types.put_code_binding_response.PutCodeBindingResponse,
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


async def async_put_code_binding(
    options: AsyncOperationOptions,
    input_: aws_sdk_schemas.types.put_code_binding_request.PutCodeBindingRequest,
) -> tuple[
    aws_sdk_schemas.types.put_code_binding_response.PutCodeBindingResponse,
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
