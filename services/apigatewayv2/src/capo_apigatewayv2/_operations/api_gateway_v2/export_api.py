"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ExportApi``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_apigatewayv2._auth._signers
import capo_apigatewayv2._auth._sigv4
import capo_apigatewayv2.errors.bad_request_exception
import capo_apigatewayv2.errors.not_found_exception
import capo_apigatewayv2.errors.too_many_requests_exception
import capo_apigatewayv2.types.export_api_request
import capo_apigatewayv2.types.export_api_response
import capo_apigatewayv2.types.exported_api
from capo_apigatewayv2._protocol.errors import parse_error_metadata_json
from capo_apigatewayv2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_apigatewayv2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_apigatewayv2.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_apigatewayv2.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "NotFoundException":
            raise capo_apigatewayv2.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_apigatewayv2.types.export_api_response.ExportApiResponse:
    out: capo_apigatewayv2.types.export_api_response.ExportApiResponse = {
        "body": capo_apigatewayv2.types.exported_api.deserialize_json(
            json.loads(response.read())
        )
    }  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_apigatewayv2.types.export_api_response.ExportApiResponse:
    out: capo_apigatewayv2.types.export_api_response.ExportApiResponse = {
        "body": capo_apigatewayv2.types.exported_api.deserialize_json(
            json.loads(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_apigatewayv2._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_apigatewayv2._auth._sigv4.build_sigv4_auth_scheme(
                "apigateway", options.region
            )
        )
        if sigv4_config is not None:
            return capo_apigatewayv2._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_apigatewayv2.types.export_api_request.ExportApiRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v2/apis/{ApiId}/exports/{Specification}"
    url = url.replace("{ApiId}", quote(str(input_["api_id"]), safe=""))
    url = url.replace("{Specification}", quote(str(input_["specification"]), safe=""))
    params: dict[str, str] = {}
    if "export_version" in input_:
        params["exportVersion"] = str(input_["export_version"])
    if "include_extensions" in input_:
        params["includeExtensions"] = str(input_["include_extensions"])
    if "output_type" in input_:
        params["outputType"] = str(input_["output_type"])
    if "stage_name" in input_:
        params["stageName"] = str(input_["stage_name"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def export_api(
    options: OperationOptions,
    input_: capo_apigatewayv2.types.export_api_request.ExportApiRequest,
) -> tuple[
    capo_apigatewayv2.types.export_api_response.ExportApiResponse, zapros.Response
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


async def async_export_api(
    options: AsyncOperationOptions,
    input_: capo_apigatewayv2.types.export_api_request.ExportApiRequest,
) -> tuple[
    capo_apigatewayv2.types.export_api_response.ExportApiResponse, zapros.Response
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
