"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateConfigurationPolicy``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_securityhub._auth._signers
import capo_securityhub._auth._sigv4
import capo_securityhub.errors.access_denied_exception
import capo_securityhub.errors.internal_exception
import capo_securityhub.errors.invalid_access_exception
import capo_securityhub.errors.invalid_input_exception
import capo_securityhub.errors.limit_exceeded_exception
import capo_securityhub.errors.resource_conflict_exception
import capo_securityhub.types.create_configuration_policy_request
import capo_securityhub.types.create_configuration_policy_response
import capo_securityhub.types.policy
import capo_securityhub.types.tag_map
import capo_securityhub.types.timestamp
from capo_securityhub._protocol.errors import parse_error_metadata_json
from capo_securityhub._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_securityhub._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_securityhub.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_securityhub.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalException":
            raise capo_securityhub.errors.internal_exception.InternalException.from_json(
                data
            )
        case "InvalidAccessException":
            raise capo_securityhub.errors.invalid_access_exception.InvalidAccessException.from_json(
                data
            )
        case "InvalidInputException":
            raise capo_securityhub.errors.invalid_input_exception.InvalidInputException.from_json(
                data
            )
        case "LimitExceededException":
            raise capo_securityhub.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "ResourceConflictException":
            raise capo_securityhub.errors.resource_conflict_exception.ResourceConflictException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_securityhub.types.create_configuration_policy_response.CreateConfigurationPolicyResponse:
    out: capo_securityhub.types.create_configuration_policy_response.CreateConfigurationPolicyResponse = capo_securityhub.types.create_configuration_policy_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_securityhub.types.create_configuration_policy_response.CreateConfigurationPolicyResponse:
    out: capo_securityhub.types.create_configuration_policy_response.CreateConfigurationPolicyResponse = capo_securityhub.types.create_configuration_policy_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_securityhub._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_securityhub._auth._sigv4.build_sigv4_auth_scheme(
                "securityhub", options.region
            )
        )
        if sigv4_config is not None:
            return capo_securityhub._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_securityhub.types.create_configuration_policy_request.CreateConfigurationPolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/configurationPolicy/create"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_securityhub.types.create_configuration_policy_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_configuration_policy(
    options: OperationOptions,
    input_: capo_securityhub.types.create_configuration_policy_request.CreateConfigurationPolicyRequest,
) -> tuple[
    capo_securityhub.types.create_configuration_policy_response.CreateConfigurationPolicyResponse,
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


async def async_create_configuration_policy(
    options: AsyncOperationOptions,
    input_: capo_securityhub.types.create_configuration_policy_request.CreateConfigurationPolicyRequest,
) -> tuple[
    capo_securityhub.types.create_configuration_policy_response.CreateConfigurationPolicyResponse,
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
