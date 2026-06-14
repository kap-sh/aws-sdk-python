"""Generated from Smithy shape ``com.amazonaws.greengrass#ListResourceDefinitions``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_greengrass._auth._signers
import aws_sdk_greengrass._auth._sigv4
from aws_sdk_greengrass._protocol.errors import parse_error_metadata_json
from aws_sdk_greengrass._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_greengrass._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_greengrass.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.list_resource_definitions_request
    import aws_sdk_greengrass.types.list_resource_definitions_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_greengrass.types.list_resource_definitions_response.ListResourceDefinitionsResponse:
    import aws_sdk_greengrass.types.list_resource_definitions_response

    out: aws_sdk_greengrass.types.list_resource_definitions_response.ListResourceDefinitionsResponse = aws_sdk_greengrass.types.list_resource_definitions_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_greengrass._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_greengrass._auth._sigv4.build_sigv4_auth_scheme(
                "greengrass", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_greengrass._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_greengrass.types.list_resource_definitions_request.ListResourceDefinitionsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/greengrass/definition/resources"
    params: dict[str, str] = {}
    if "max_results" in input_:
        params["MaxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_resource_definitions(
    options: OperationOptions,
    input_: aws_sdk_greengrass.types.list_resource_definitions_request.ListResourceDefinitionsRequest,
) -> tuple[
    aws_sdk_greengrass.types.list_resource_definitions_response.ListResourceDefinitionsResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_list_resource_definitions(
    options: AsyncOperationOptions,
    input_: aws_sdk_greengrass.types.list_resource_definitions_request.ListResourceDefinitionsRequest,
) -> tuple[
    aws_sdk_greengrass.types.list_resource_definitions_response.ListResourceDefinitionsResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
