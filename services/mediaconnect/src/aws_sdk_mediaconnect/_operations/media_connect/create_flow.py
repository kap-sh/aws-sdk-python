"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateFlow``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_mediaconnect._auth._signers
import aws_sdk_mediaconnect._auth._sigv4
import aws_sdk_mediaconnect.errors.bad_request_exception
import aws_sdk_mediaconnect.errors.create_flow420_exception
import aws_sdk_mediaconnect.errors.forbidden_exception
import aws_sdk_mediaconnect.errors.internal_server_error_exception
import aws_sdk_mediaconnect.errors.service_unavailable_exception
import aws_sdk_mediaconnect.errors.too_many_requests_exception
import aws_sdk_mediaconnect.types.__list_of_add_media_stream_request
import aws_sdk_mediaconnect.types.__list_of_add_output_request
import aws_sdk_mediaconnect.types.__list_of_grant_entitlement_request
import aws_sdk_mediaconnect.types.__list_of_set_source_request
import aws_sdk_mediaconnect.types.__list_of_vpc_interface_request
import aws_sdk_mediaconnect.types.__map_of_string
import aws_sdk_mediaconnect.types.add_maintenance
import aws_sdk_mediaconnect.types.create_flow_request
import aws_sdk_mediaconnect.types.create_flow_response
import aws_sdk_mediaconnect.types.encoding_config
import aws_sdk_mediaconnect.types.failover_config
import aws_sdk_mediaconnect.types.flow
import aws_sdk_mediaconnect.types.flow_size
import aws_sdk_mediaconnect.types.monitoring_config
import aws_sdk_mediaconnect.types.ndi_config
import aws_sdk_mediaconnect.types.set_source_request
from aws_sdk_mediaconnect._protocol.errors import parse_error_metadata_json
from aws_sdk_mediaconnect._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_mediaconnect._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_mediaconnect.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise aws_sdk_mediaconnect.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "CreateFlow420Exception":
            raise aws_sdk_mediaconnect.errors.create_flow420_exception.CreateFlow420Exception.from_json(
                data
            )
        case "ForbiddenException":
            raise aws_sdk_mediaconnect.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "InternalServerErrorException":
            raise aws_sdk_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_mediaconnect.types.create_flow_response.CreateFlowResponse:
    out: aws_sdk_mediaconnect.types.create_flow_response.CreateFlowResponse = (
        aws_sdk_mediaconnect.types.create_flow_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_mediaconnect.types.create_flow_response.CreateFlowResponse:
    out: aws_sdk_mediaconnect.types.create_flow_response.CreateFlowResponse = (
        aws_sdk_mediaconnect.types.create_flow_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_mediaconnect._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_mediaconnect._auth._sigv4.build_sigv4_auth_scheme(
                "mediaconnect", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_mediaconnect._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_mediaconnect.types.create_flow_request.CreateFlowRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/flows"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_mediaconnect.types.create_flow_request

    body: bytes | None = json.dumps(
        aws_sdk_mediaconnect.types.create_flow_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_flow(
    options: OperationOptions,
    input_: aws_sdk_mediaconnect.types.create_flow_request.CreateFlowRequest,
) -> tuple[
    aws_sdk_mediaconnect.types.create_flow_response.CreateFlowResponse, zapros.Response
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


async def async_create_flow(
    options: AsyncOperationOptions,
    input_: aws_sdk_mediaconnect.types.create_flow_request.CreateFlowRequest,
) -> tuple[
    aws_sdk_mediaconnect.types.create_flow_response.CreateFlowResponse, zapros.Response
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
