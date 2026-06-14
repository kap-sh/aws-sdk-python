"""Generated from Smithy shape ``com.amazonaws.location#GetMapSprites``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_location._auth._signers
import aws_sdk_location._auth._sigv4
from aws_sdk_location._protocol.errors import parse_error_metadata_json
from aws_sdk_location._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_location._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_location.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_location.types.get_map_sprites_request
    import aws_sdk_location.types.get_map_sprites_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_location.errors.access_denied_exception

            raise aws_sdk_location.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_location.errors.internal_server_exception

            raise aws_sdk_location.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_location.errors.resource_not_found_exception

            raise aws_sdk_location.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_location.errors.throttling_exception

            raise aws_sdk_location.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_location.errors.validation_exception

            raise aws_sdk_location.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_location.types.get_map_sprites_response.GetMapSpritesResponse:
    out: aws_sdk_location.types.get_map_sprites_response.GetMapSpritesResponse = {
        "blob": response.read()
    }  # type: ignore[typeddict-item]
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "Cache-Control" in response.headers:
        out["cache_control"] = str(response.headers["Cache-Control"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_location._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_location._auth._sigv4.build_sigv4_auth_scheme(
                "geo", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_location._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_location.types.get_map_sprites_request.GetMapSpritesRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/maps/v0/maps/{MapName}/sprites/{FileName}"
    url = url.replace("{MapName}", quote(str(input_["map_name"]), safe=""))
    url = url.replace("{FileName}", quote(str(input_["file_name"]), safe=""))
    params: dict[str, str] = {}
    if "key" in input_:
        params["key"] = str(input_["key"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_map_sprites(
    options: OperationOptions,
    input_: aws_sdk_location.types.get_map_sprites_request.GetMapSpritesRequest,
) -> tuple[
    aws_sdk_location.types.get_map_sprites_response.GetMapSpritesResponse,
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


async def async_get_map_sprites(
    options: AsyncOperationOptions,
    input_: aws_sdk_location.types.get_map_sprites_request.GetMapSpritesRequest,
) -> tuple[
    aws_sdk_location.types.get_map_sprites_response.GetMapSpritesResponse,
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
