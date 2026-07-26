"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateResolverEndpoint``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_route53resolver._auth._signers
import capo_route53resolver._auth._sigv4
import capo_route53resolver.errors.access_denied_exception
import capo_route53resolver.errors.internal_service_error_exception
import capo_route53resolver.errors.invalid_parameter_exception
import capo_route53resolver.errors.invalid_request_exception
import capo_route53resolver.errors.limit_exceeded_exception
import capo_route53resolver.errors.resource_exists_exception
import capo_route53resolver.errors.resource_not_found_exception
import capo_route53resolver.errors.throttling_exception
import capo_route53resolver.types.create_resolver_endpoint_request
import capo_route53resolver.types.create_resolver_endpoint_response
import capo_route53resolver.types.ip_addresses_request
import capo_route53resolver.types.protocol_list
import capo_route53resolver.types.resolver_endpoint
import capo_route53resolver.types.resolver_endpoint_direction
import capo_route53resolver.types.resolver_endpoint_type
import capo_route53resolver.types.security_group_ids
import capo_route53resolver.types.tag_list
from capo_route53resolver._protocol.errors import parse_error_metadata_json
from capo_route53resolver._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_route53resolver._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_route53resolver.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_route53resolver.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "InternalServiceErrorException":
            raise capo_route53resolver.errors.internal_service_error_exception.InternalServiceErrorException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise capo_route53resolver.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "InvalidRequestException":
            raise capo_route53resolver.errors.invalid_request_exception.InvalidRequestException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            raise capo_route53resolver.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "ResourceExistsException":
            raise capo_route53resolver.errors.resource_exists_exception.ResourceExistsException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise capo_route53resolver.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case "ThrottlingException":
            raise capo_route53resolver.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_route53resolver.types.create_resolver_endpoint_response.CreateResolverEndpointResponse:
    out: capo_route53resolver.types.create_resolver_endpoint_response.CreateResolverEndpointResponse = capo_route53resolver.types.create_resolver_endpoint_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_route53resolver.types.create_resolver_endpoint_response.CreateResolverEndpointResponse:
    out: capo_route53resolver.types.create_resolver_endpoint_response.CreateResolverEndpointResponse = capo_route53resolver.types.create_resolver_endpoint_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_route53resolver._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_route53resolver._auth._sigv4.build_sigv4_auth_scheme(
                "route53resolver", options.region
            )
        )
        if sigv4_config is not None:
            return capo_route53resolver._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_route53resolver.types.create_resolver_endpoint_request.CreateResolverEndpointRequest,
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
    headers["X-Amz-Target"] = "Route53Resolver.CreateResolverEndpoint"
    body: bytes | None = json.dumps(
        capo_route53resolver.types.create_resolver_endpoint_request.serialize_aws_json_1_1(
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


def create_resolver_endpoint(
    options: OperationOptions,
    input_: capo_route53resolver.types.create_resolver_endpoint_request.CreateResolverEndpointRequest,
) -> tuple[
    capo_route53resolver.types.create_resolver_endpoint_response.CreateResolverEndpointResponse,
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


async def async_create_resolver_endpoint(
    options: AsyncOperationOptions,
    input_: capo_route53resolver.types.create_resolver_endpoint_request.CreateResolverEndpointRequest,
) -> tuple[
    capo_route53resolver.types.create_resolver_endpoint_response.CreateResolverEndpointResponse,
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
