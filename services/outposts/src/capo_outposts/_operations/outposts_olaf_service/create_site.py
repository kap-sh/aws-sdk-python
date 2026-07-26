"""Generated from Smithy shape ``com.amazonaws.outposts#CreateSite``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_outposts._auth._signers
import capo_outposts._auth._sigv4
import capo_outposts.errors.access_denied_exception
import capo_outposts.errors.conflict_exception
import capo_outposts.errors.internal_server_exception
import capo_outposts.errors.service_quota_exceeded_exception
import capo_outposts.errors.validation_exception
import capo_outposts.types.address
import capo_outposts.types.create_site_input
import capo_outposts.types.create_site_output
import capo_outposts.types.rack_physical_properties
import capo_outposts.types.site
import capo_outposts.types.tag_map
from capo_outposts._protocol.errors import parse_error_metadata_json
from capo_outposts._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_outposts._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_outposts.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_outposts.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            raise capo_outposts.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_outposts.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise capo_outposts.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ValidationException":
            raise capo_outposts.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_outposts.types.create_site_output.CreateSiteOutput:
    out: capo_outposts.types.create_site_output.CreateSiteOutput = (
        capo_outposts.types.create_site_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_outposts.types.create_site_output.CreateSiteOutput:
    out: capo_outposts.types.create_site_output.CreateSiteOutput = (
        capo_outposts.types.create_site_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_outposts._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_outposts._auth._sigv4.build_sigv4_auth_scheme(
                "outposts", options.region
            )
        )
        if sigv4_config is not None:
            return capo_outposts._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_outposts.types.create_site_input.CreateSiteInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/sites"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_outposts.types.create_site_input.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_site(
    options: OperationOptions,
    input_: capo_outposts.types.create_site_input.CreateSiteInput,
) -> tuple[capo_outposts.types.create_site_output.CreateSiteOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_create_site(
    options: AsyncOperationOptions,
    input_: capo_outposts.types.create_site_input.CreateSiteInput,
) -> tuple[capo_outposts.types.create_site_output.CreateSiteOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
