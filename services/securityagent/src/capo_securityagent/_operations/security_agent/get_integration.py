"""Generated from Smithy shape ``com.amazonaws.securityagent#GetIntegration``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_securityagent._auth._signers
import capo_securityagent._auth._sigv4
import capo_securityagent.errors.access_denied_exception
import capo_securityagent.errors.internal_server_exception
import capo_securityagent.errors.resource_not_found_exception
import capo_securityagent.errors.throttling_exception
import capo_securityagent.errors.validation_exception
import capo_securityagent.types.get_integration_input
import capo_securityagent.types.get_integration_output
import capo_securityagent.types.provider
import capo_securityagent.types.provider_type
from capo_securityagent._protocol.errors import parse_error_metadata_json
from capo_securityagent._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_securityagent._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_securityagent.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_securityagent.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_securityagent.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_securityagent.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_securityagent.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_securityagent.types.get_integration_output.GetIntegrationOutput:
    out: capo_securityagent.types.get_integration_output.GetIntegrationOutput = (
        capo_securityagent.types.get_integration_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_securityagent.types.get_integration_output.GetIntegrationOutput:
    out: capo_securityagent.types.get_integration_output.GetIntegrationOutput = (
        capo_securityagent.types.get_integration_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_securityagent._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_securityagent._auth._sigv4.build_sigv4_auth_scheme(
                "securityagent", options.region
            )
        )
        if sigv4_config is not None:
            return capo_securityagent._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_securityagent.types.get_integration_input.GetIntegrationInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/GetIntegration"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_securityagent.types.get_integration_input.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def get_integration(
    options: OperationOptions,
    input_: capo_securityagent.types.get_integration_input.GetIntegrationInput,
) -> tuple[
    capo_securityagent.types.get_integration_output.GetIntegrationOutput,
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


async def async_get_integration(
    options: AsyncOperationOptions,
    input_: capo_securityagent.types.get_integration_input.GetIntegrationInput,
) -> tuple[
    capo_securityagent.types.get_integration_output.GetIntegrationOutput,
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
