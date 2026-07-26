"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DescribeAccountSettings``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_timestream_query._auth._signers
import capo_timestream_query._auth._sigv4
import capo_timestream_query.errors.access_denied_exception
import capo_timestream_query.errors.internal_server_exception
import capo_timestream_query.errors.invalid_endpoint_exception
import capo_timestream_query.errors.throttling_exception
import capo_timestream_query.types.describe_account_settings_request
import capo_timestream_query.types.describe_account_settings_response
import capo_timestream_query.types.query_compute_response
import capo_timestream_query.types.query_pricing_model
from capo_timestream_query._protocol.errors import parse_error_metadata_json
from capo_timestream_query._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_timestream_query._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_timestream_query.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_timestream_query.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data
            )
        case "InternalServerException":
            raise capo_timestream_query.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data
            )
        case "InvalidEndpointException":
            raise capo_timestream_query.errors.invalid_endpoint_exception.InvalidEndpointException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            raise capo_timestream_query.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_timestream_query.types.describe_account_settings_response.DescribeAccountSettingsResponse:
    out: capo_timestream_query.types.describe_account_settings_response.DescribeAccountSettingsResponse = capo_timestream_query.types.describe_account_settings_response.deserialize_aws_json_1_0(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_timestream_query.types.describe_account_settings_response.DescribeAccountSettingsResponse:
    out: capo_timestream_query.types.describe_account_settings_response.DescribeAccountSettingsResponse = capo_timestream_query.types.describe_account_settings_response.deserialize_aws_json_1_0(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_timestream_query._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_timestream_query._auth._sigv4.build_sigv4_auth_scheme(
                "timestream", options.region
            )
        )
        if sigv4_config is not None:
            return capo_timestream_query._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_timestream_query.types.describe_account_settings_request.DescribeAccountSettingsRequest,
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
    headers["X-Amz-Target"] = "Timestream_20181101.DescribeAccountSettings"
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def describe_account_settings(
    options: OperationOptions,
    input_: capo_timestream_query.types.describe_account_settings_request.DescribeAccountSettingsRequest,
) -> tuple[
    capo_timestream_query.types.describe_account_settings_response.DescribeAccountSettingsResponse,
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


async def async_describe_account_settings(
    options: AsyncOperationOptions,
    input_: capo_timestream_query.types.describe_account_settings_request.DescribeAccountSettingsRequest,
) -> tuple[
    capo_timestream_query.types.describe_account_settings_response.DescribeAccountSettingsResponse,
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
