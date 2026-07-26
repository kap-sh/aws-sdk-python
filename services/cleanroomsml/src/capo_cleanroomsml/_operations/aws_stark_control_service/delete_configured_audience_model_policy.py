"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DeleteConfiguredAudienceModelPolicy``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_cleanroomsml._auth._signers
import capo_cleanroomsml._auth._sigv4
import capo_cleanroomsml.errors.access_denied_exception
import capo_cleanroomsml.errors.resource_not_found_exception
import capo_cleanroomsml.errors.validation_exception
import capo_cleanroomsml.types.delete_configured_audience_model_policy_request
from capo_cleanroomsml._protocol.errors import parse_error_metadata_json
from capo_cleanroomsml._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cleanroomsml._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_cleanroomsml.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ValidationException":
            raise capo_cleanroomsml.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cleanroomsml._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_cleanroomsml._auth._sigv4.build_sigv4_auth_scheme(
                "cleanrooms-ml", options.region
            )
        )
        if sigv4_config is not None:
            return capo_cleanroomsml._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/configured-audience-model/{configuredAudienceModelArn}/policy"
    )
    url = url.replace(
        "{configuredAudienceModelArn}",
        quote(str(input_["configured_audience_model_arn"]), safe=""),
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_configured_audience_model_policy(
    options: OperationOptions,
    input_: capo_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_delete_configured_audience_model_policy(
    options: AsyncOperationOptions,
    input_: capo_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
