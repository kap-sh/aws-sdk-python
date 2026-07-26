"""Generated from Smithy shape ``com.amazonaws.apigateway#FlushStageCache``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_api_gateway._auth._signers
import capo_api_gateway._auth._sigv4
import capo_api_gateway.errors.bad_request_exception
import capo_api_gateway.errors.conflict_exception
import capo_api_gateway.errors.limit_exceeded_exception
import capo_api_gateway.errors.not_found_exception
import capo_api_gateway.errors.too_many_requests_exception
import capo_api_gateway.errors.unauthorized_exception
import capo_api_gateway.types.flush_stage_cache_request
from capo_api_gateway._protocol.errors import parse_error_metadata_json
from capo_api_gateway._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_api_gateway._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_api_gateway.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_api_gateway.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ConflictException":
            raise capo_api_gateway.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "LimitExceededException":
            raise capo_api_gateway.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "NotFoundException":
            raise capo_api_gateway.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise capo_api_gateway.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case "UnauthorizedException":
            raise capo_api_gateway.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_api_gateway._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_api_gateway._auth._sigv4.build_sigv4_auth_scheme(
                "apigateway", options.region
            )
        )
        if sigv4_config is not None:
            return capo_api_gateway._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_api_gateway.types.flush_stage_cache_request.FlushStageCacheRequest,
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
        endpoint.url.rstrip("/") + "/restapis/{restApiId}/stages/{stageName}/cache/data"
    )
    url = url.replace("{restApiId}", quote(str(input_["rest_api_id"]), safe=""))
    url = url.replace("{stageName}", quote(str(input_["stage_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def flush_stage_cache(
    options: OperationOptions,
    input_: capo_api_gateway.types.flush_stage_cache_request.FlushStageCacheRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_flush_stage_cache(
    options: AsyncOperationOptions,
    input_: capo_api_gateway.types.flush_stage_cache_request.FlushStageCacheRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
