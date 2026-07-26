"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLookupTable``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudwatch_logs._auth._signers
import capo_cloudwatch_logs._auth._sigv4
import capo_cloudwatch_logs.errors.access_denied_exception
import capo_cloudwatch_logs.errors.invalid_parameter_exception
import capo_cloudwatch_logs.errors.resource_not_found_exception
import capo_cloudwatch_logs.errors.service_unavailable_exception
import capo_cloudwatch_logs.types.get_lookup_table_request
import capo_cloudwatch_logs.types.get_lookup_table_response
from capo_cloudwatch_logs._protocol.errors import parse_error_metadata_json
from capo_cloudwatch_logs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudwatch_logs._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_cloudwatch_logs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case "ServiceUnavailableException":
            raise capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudwatch_logs.types.get_lookup_table_response.GetLookupTableResponse:
    out: capo_cloudwatch_logs.types.get_lookup_table_response.GetLookupTableResponse = (
        capo_cloudwatch_logs.types.get_lookup_table_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudwatch_logs.types.get_lookup_table_response.GetLookupTableResponse:
    out: capo_cloudwatch_logs.types.get_lookup_table_response.GetLookupTableResponse = (
        capo_cloudwatch_logs.types.get_lookup_table_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudwatch_logs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_cloudwatch_logs._auth._sigv4.build_sigv4_auth_scheme(
                "logs", options.region
            )
        )
        if sigv4_config is not None:
            return capo_cloudwatch_logs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudwatch_logs.types.get_lookup_table_request.GetLookupTableRequest,
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
    headers["X-Amz-Target"] = "Logs_20140328.GetLookupTable"
    body: bytes | None = json.dumps(
        capo_cloudwatch_logs.types.get_lookup_table_request.serialize_aws_json_1_1(
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


def get_lookup_table(
    options: OperationOptions,
    input_: capo_cloudwatch_logs.types.get_lookup_table_request.GetLookupTableRequest,
) -> tuple[
    capo_cloudwatch_logs.types.get_lookup_table_response.GetLookupTableResponse,
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


async def async_get_lookup_table(
    options: AsyncOperationOptions,
    input_: capo_cloudwatch_logs.types.get_lookup_table_request.GetLookupTableRequest,
) -> tuple[
    capo_cloudwatch_logs.types.get_lookup_table_response.GetLookupTableResponse,
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
