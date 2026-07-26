"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateResponderGateway``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_rtbfabric._auth._signers
import capo_rtbfabric._auth._sigv4
import capo_rtbfabric.errors.access_denied_exception
import capo_rtbfabric.errors.internal_server_exception
import capo_rtbfabric.errors.resource_not_found_exception
import capo_rtbfabric.errors.service_quota_exceeded_exception
import capo_rtbfabric.errors.throttling_exception
import capo_rtbfabric.errors.validation_exception
import capo_rtbfabric.types.create_responder_gateway_request
import capo_rtbfabric.types.create_responder_gateway_response
import capo_rtbfabric.types.gateway_type
import capo_rtbfabric.types.listener_config
import capo_rtbfabric.types.managed_endpoint_configuration
import capo_rtbfabric.types.protocol
import capo_rtbfabric.types.responder_gateway_status
import capo_rtbfabric.types.security_group_id_list
import capo_rtbfabric.types.subnet_id_list
import capo_rtbfabric.types.tags_map
import capo_rtbfabric.types.trust_store_configuration
from capo_rtbfabric._protocol.errors import parse_error_metadata_json
from capo_rtbfabric._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_rtbfabric._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_rtbfabric.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_rtbfabric.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_rtbfabric.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_rtbfabric.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_rtbfabric.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse:
    out: capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse = capo_rtbfabric.types.create_responder_gateway_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse:
    out: capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse = capo_rtbfabric.types.create_responder_gateway_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_rtbfabric._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_rtbfabric._auth._sigv4.build_sigv4_auth_scheme(
                "rtbfabric", options.region
            )
        )
        if sigv4_config is not None:
            return capo_rtbfabric._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/responder-gateway"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_rtbfabric.types.create_responder_gateway_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_responder_gateway(
    options: OperationOptions,
    input_: capo_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest,
) -> tuple[
    capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse,
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


async def async_create_responder_gateway(
    options: AsyncOperationOptions,
    input_: capo_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest,
) -> tuple[
    capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse,
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
