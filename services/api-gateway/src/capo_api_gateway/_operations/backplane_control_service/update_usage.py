"""Generated from Smithy shape ``com.amazonaws.apigateway#UpdateUsage``."""

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
import capo_api_gateway.types.list_of_patch_operation
import capo_api_gateway.types.map_of_key_usages
import capo_api_gateway.types.update_usage_request
import capo_api_gateway.types.usage
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


def handle_response(response: zapros.Response) -> capo_api_gateway.types.usage.Usage:
    out: capo_api_gateway.types.usage.Usage = (
        capo_api_gateway.types.usage.deserialize_json(json.loads(response.read()))
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_api_gateway.types.usage.Usage:
    out: capo_api_gateway.types.usage.Usage = (
        capo_api_gateway.types.usage.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


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
    input_: capo_api_gateway.types.update_usage_request.UpdateUsageRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/usageplans/{usagePlanId}/keys/{keyId}/usage"
    url = url.replace("{usagePlanId}", quote(str(input_["usage_plan_id"]), safe=""))
    url = url.replace("{keyId}", quote(str(input_["key_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_api_gateway.types.update_usage_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PATCH", headers=headers, body=body, context={"signer": signer}
    )


def update_usage(
    options: OperationOptions,
    input_: capo_api_gateway.types.update_usage_request.UpdateUsageRequest,
) -> tuple[capo_api_gateway.types.usage.Usage, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_update_usage(
    options: AsyncOperationOptions,
    input_: capo_api_gateway.types.update_usage_request.UpdateUsageRequest,
) -> tuple[capo_api_gateway.types.usage.Usage, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
