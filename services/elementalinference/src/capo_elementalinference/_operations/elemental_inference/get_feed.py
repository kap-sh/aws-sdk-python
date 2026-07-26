"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetFeed``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_elementalinference._auth._signers
import capo_elementalinference._auth._sigv4
import capo_elementalinference.errors.access_denied_exception
import capo_elementalinference.errors.internal_server_error_exception
import capo_elementalinference.errors.resource_not_found_exception
import capo_elementalinference.errors.too_many_request_exception
import capo_elementalinference.types.feed_association
import capo_elementalinference.types.feed_status
import capo_elementalinference.types.get_feed_request
import capo_elementalinference.types.get_feed_response
import capo_elementalinference.types.get_output_list
import capo_elementalinference.types.string_list
import capo_elementalinference.types.tag_map
from capo_elementalinference._protocol.errors import parse_error_metadata_json
from capo_elementalinference._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_elementalinference._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_elementalinference.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_elementalinference.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerErrorException":
            raise capo_elementalinference.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_elementalinference.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "TooManyRequestException":
            raise capo_elementalinference.errors.too_many_request_exception.TooManyRequestException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_elementalinference.types.get_feed_response.GetFeedResponse:
    out: capo_elementalinference.types.get_feed_response.GetFeedResponse = (
        capo_elementalinference.types.get_feed_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_elementalinference.types.get_feed_response.GetFeedResponse:
    out: capo_elementalinference.types.get_feed_response.GetFeedResponse = (
        capo_elementalinference.types.get_feed_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_elementalinference._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_elementalinference._auth._sigv4.build_sigv4_auth_scheme(
                "elemental-inference", options.region
            )
        )
        if sigv4_config is not None:
            return capo_elementalinference._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_elementalinference.types.get_feed_request.GetFeedRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/feed/{id}"
    url = url.replace("{id}", quote(str(input_["id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_feed(
    options: OperationOptions,
    input_: capo_elementalinference.types.get_feed_request.GetFeedRequest,
) -> tuple[
    capo_elementalinference.types.get_feed_response.GetFeedResponse, zapros.Response
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


async def async_get_feed(
    options: AsyncOperationOptions,
    input_: capo_elementalinference.types.get_feed_request.GetFeedRequest,
) -> tuple[
    capo_elementalinference.types.get_feed_response.GetFeedResponse, zapros.Response
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
