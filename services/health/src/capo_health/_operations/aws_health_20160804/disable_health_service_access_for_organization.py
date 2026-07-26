"""Generated from Smithy shape ``com.amazonaws.health#DisableHealthServiceAccessForOrganization``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_health._auth._signers
import capo_health._auth._sigv4
import capo_health.errors.concurrent_modification_exception
from capo_health._protocol.errors import parse_error_metadata_json
from capo_health._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_health._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_health.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConcurrentModificationException":
            raise capo_health.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_health._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_health._auth._sigv4.build_sigv4_auth_scheme(
                "health", options.region
            )
        )
        if sigv4_config is not None:
            return capo_health._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(options: OperationOptions | AsyncOperationOptions) -> zapros.Request:
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
    headers["X-Amz-Target"] = (
        "AWSHealth_20160804.DisableHealthServiceAccessForOrganization"
    )
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def disable_health_service_access_for_organization(
    options: OperationOptions,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_disable_health_service_access_for_organization(
    options: AsyncOperationOptions,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
