"""Generated from Smithy shape ``com.amazonaws.pi#DescribeDimensionKeys``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_pi._auth._signers
import aws_sdk_pi._auth._sigv4
import aws_sdk_pi.errors.internal_service_error
import aws_sdk_pi.errors.invalid_argument_exception
import aws_sdk_pi.errors.not_authorized_exception
import aws_sdk_pi.types.additional_metrics_list
import aws_sdk_pi.types.describe_dimension_keys_request
import aws_sdk_pi.types.describe_dimension_keys_response
import aws_sdk_pi.types.dimension_group
import aws_sdk_pi.types.dimension_key_description_list
import aws_sdk_pi.types.iso_timestamp
import aws_sdk_pi.types.metric_query_filter_map
import aws_sdk_pi.types.response_partition_key_list
import aws_sdk_pi.types.service_type
from aws_sdk_pi._protocol.errors import parse_error_metadata_json
from aws_sdk_pi._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_pi._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_pi.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServiceError":
            raise aws_sdk_pi.errors.internal_service_error.InternalServiceError.from_aws_json_1_1(
                data
            )
        case "InvalidArgumentException":
            raise aws_sdk_pi.errors.invalid_argument_exception.InvalidArgumentException.from_aws_json_1_1(
                data
            )
        case "NotAuthorizedException":
            raise aws_sdk_pi.errors.not_authorized_exception.NotAuthorizedException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_pi.types.describe_dimension_keys_response.DescribeDimensionKeysResponse:
    out: aws_sdk_pi.types.describe_dimension_keys_response.DescribeDimensionKeysResponse = aws_sdk_pi.types.describe_dimension_keys_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_pi.types.describe_dimension_keys_response.DescribeDimensionKeysResponse:
    out: aws_sdk_pi.types.describe_dimension_keys_response.DescribeDimensionKeysResponse = aws_sdk_pi.types.describe_dimension_keys_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_pi._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_pi._auth._sigv4.build_sigv4_auth_scheme("pi", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_pi._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_pi.types.describe_dimension_keys_request.DescribeDimensionKeysRequest,
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
    headers["X-Amz-Target"] = "PerformanceInsightsv20180227.DescribeDimensionKeys"
    body: bytes | None = json.dumps(
        aws_sdk_pi.types.describe_dimension_keys_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def describe_dimension_keys(
    options: OperationOptions,
    input_: aws_sdk_pi.types.describe_dimension_keys_request.DescribeDimensionKeysRequest,
) -> tuple[
    aws_sdk_pi.types.describe_dimension_keys_response.DescribeDimensionKeysResponse,
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


async def async_describe_dimension_keys(
    options: AsyncOperationOptions,
    input_: aws_sdk_pi.types.describe_dimension_keys_request.DescribeDimensionKeysRequest,
) -> tuple[
    aws_sdk_pi.types.describe_dimension_keys_response.DescribeDimensionKeysResponse,
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
