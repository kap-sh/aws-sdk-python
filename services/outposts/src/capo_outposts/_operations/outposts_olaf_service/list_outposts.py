"""Generated from Smithy shape ``com.amazonaws.outposts#ListOutposts``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_outposts._auth._signers
import capo_outposts._auth._sigv4
import capo_outposts.errors.access_denied_exception
import capo_outposts.errors.internal_server_exception
import capo_outposts.errors.validation_exception
import capo_outposts.types.availability_zone_id_list
import capo_outposts.types.availability_zone_list
import capo_outposts.types.life_cycle_status_list
import capo_outposts.types.list_outposts_input
import capo_outposts.types.list_outposts_output
import capo_outposts.types.outpost_list_definition
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
        case "InternalServerException":
            raise capo_outposts.errors.internal_server_exception.InternalServerException.from_json(
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
) -> capo_outposts.types.list_outposts_output.ListOutpostsOutput:
    out: capo_outposts.types.list_outposts_output.ListOutpostsOutput = (
        capo_outposts.types.list_outposts_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_outposts.types.list_outposts_output.ListOutpostsOutput:
    out: capo_outposts.types.list_outposts_output.ListOutpostsOutput = (
        capo_outposts.types.list_outposts_output.deserialize_json(
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
    input_: capo_outposts.types.list_outposts_input.ListOutpostsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/outposts"
    params: dict[str, str] = {}
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    if "max_results" in input_:
        params["MaxResults"] = str(input_["max_results"])
    if "life_cycle_status_filter" in input_:
        params["LifeCycleStatusFilter"] = str(input_["life_cycle_status_filter"])
    if "availability_zone_filter" in input_:
        params["AvailabilityZoneFilter"] = str(input_["availability_zone_filter"])
    if "availability_zone_id_filter" in input_:
        params["AvailabilityZoneIdFilter"] = str(input_["availability_zone_id_filter"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_outposts(
    options: OperationOptions,
    input_: capo_outposts.types.list_outposts_input.ListOutpostsInput,
) -> tuple[
    capo_outposts.types.list_outposts_output.ListOutpostsOutput, zapros.Response
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


async def async_list_outposts(
    options: AsyncOperationOptions,
    input_: capo_outposts.types.list_outposts_input.ListOutpostsInput,
) -> tuple[
    capo_outposts.types.list_outposts_output.ListOutpostsOutput, zapros.Response
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
