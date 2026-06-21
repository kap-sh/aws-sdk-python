"""Generated from Smithy shape ``com.amazonaws.opensearch#ListVpcEndpoints``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_opensearch._auth._signers
import aws_sdk_opensearch._auth._sigv4
import aws_sdk_opensearch.errors.base_exception
import aws_sdk_opensearch.errors.disabled_operation_exception
import aws_sdk_opensearch.errors.internal_exception
import aws_sdk_opensearch.types.list_vpc_endpoints_request
import aws_sdk_opensearch.types.list_vpc_endpoints_response
import aws_sdk_opensearch.types.vpc_endpoint_summary_list
from aws_sdk_opensearch._protocol.errors import parse_error_metadata_json
from aws_sdk_opensearch._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_opensearch._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_opensearch.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BaseException":
            raise aws_sdk_opensearch.errors.base_exception.BaseException.from_json(data)
        case "DisabledOperationException":
            raise aws_sdk_opensearch.errors.disabled_operation_exception.DisabledOperationException.from_json(
                data
            )
        case "InternalException":
            raise aws_sdk_opensearch.errors.internal_exception.InternalException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_opensearch.types.list_vpc_endpoints_response.ListVpcEndpointsResponse:
    out: aws_sdk_opensearch.types.list_vpc_endpoints_response.ListVpcEndpointsResponse = aws_sdk_opensearch.types.list_vpc_endpoints_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_opensearch.types.list_vpc_endpoints_response.ListVpcEndpointsResponse:
    out: aws_sdk_opensearch.types.list_vpc_endpoints_response.ListVpcEndpointsResponse = aws_sdk_opensearch.types.list_vpc_endpoints_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_opensearch._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_opensearch._auth._sigv4.build_sigv4_auth_scheme(
                "es", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_opensearch._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_opensearch.types.list_vpc_endpoints_request.ListVpcEndpointsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2021-01-01/opensearch/vpcEndpoints"
    params: dict[str, str] = {}
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_vpc_endpoints(
    options: OperationOptions,
    input_: aws_sdk_opensearch.types.list_vpc_endpoints_request.ListVpcEndpointsRequest,
) -> tuple[
    aws_sdk_opensearch.types.list_vpc_endpoints_response.ListVpcEndpointsResponse,
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


async def async_list_vpc_endpoints(
    options: AsyncOperationOptions,
    input_: aws_sdk_opensearch.types.list_vpc_endpoints_request.ListVpcEndpointsRequest,
) -> tuple[
    aws_sdk_opensearch.types.list_vpc_endpoints_response.ListVpcEndpointsResponse,
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
