"""Generated from Smithy shape ``com.amazonaws.kendra#ListIndices``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_kendra._auth._signers
import capo_kendra._auth._sigv4
import capo_kendra.errors.access_denied_exception
import capo_kendra.errors.internal_server_exception
import capo_kendra.errors.throttling_exception
import capo_kendra.errors.validation_exception
import capo_kendra.types.index_configuration_summary_list
import capo_kendra.types.list_indices_request
import capo_kendra.types.list_indices_response
from capo_kendra._protocol.errors import parse_error_metadata_json
from capo_kendra._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_kendra._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_kendra.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_kendra.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "InternalServerException":
            raise capo_kendra.errors.internal_server_exception.InternalServerException.from_aws_json_1_1(
                data
            )
        case "ThrottlingException":
            raise capo_kendra.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data
            )
        case "ValidationException":
            raise capo_kendra.errors.validation_exception.ValidationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_kendra.types.list_indices_response.ListIndicesResponse:
    out: capo_kendra.types.list_indices_response.ListIndicesResponse = (
        capo_kendra.types.list_indices_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_kendra.types.list_indices_response.ListIndicesResponse:
    out: capo_kendra.types.list_indices_response.ListIndicesResponse = (
        capo_kendra.types.list_indices_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_kendra._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_kendra._auth._sigv4.build_sigv4_auth_scheme(
                "kendra", options.region
            )
        )
        if sigv4_config is not None:
            return capo_kendra._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_kendra.types.list_indices_request.ListIndicesRequest,
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
    headers["X-Amz-Target"] = "AWSKendraFrontendService.ListIndices"
    body: bytes | None = json.dumps(
        capo_kendra.types.list_indices_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_indices(
    options: OperationOptions,
    input_: capo_kendra.types.list_indices_request.ListIndicesRequest,
) -> tuple[
    capo_kendra.types.list_indices_response.ListIndicesResponse, zapros.Response
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


async def async_list_indices(
    options: AsyncOperationOptions,
    input_: capo_kendra.types.list_indices_request.ListIndicesRequest,
) -> tuple[
    capo_kendra.types.list_indices_response.ListIndicesResponse, zapros.Response
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
