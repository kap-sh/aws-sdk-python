"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListNodes``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_managedblockchain._auth._signers
import capo_managedblockchain._auth._sigv4
import capo_managedblockchain.errors.access_denied_exception
import capo_managedblockchain.errors.internal_service_error_exception
import capo_managedblockchain.errors.invalid_request_exception
import capo_managedblockchain.errors.throttling_exception
import capo_managedblockchain.types.list_nodes_input
import capo_managedblockchain.types.list_nodes_output
import capo_managedblockchain.types.node_status
import capo_managedblockchain.types.node_summary_list
from capo_managedblockchain._protocol.errors import parse_error_metadata_json
from capo_managedblockchain._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_managedblockchain._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_managedblockchain.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_managedblockchain.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServiceErrorException":
            raise capo_managedblockchain.errors.internal_service_error_exception.InternalServiceErrorException.from_json(
                data
            )
        case "InvalidRequestException":
            raise capo_managedblockchain.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_managedblockchain.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_managedblockchain.types.list_nodes_output.ListNodesOutput:
    out: capo_managedblockchain.types.list_nodes_output.ListNodesOutput = (
        capo_managedblockchain.types.list_nodes_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_managedblockchain.types.list_nodes_output.ListNodesOutput:
    out: capo_managedblockchain.types.list_nodes_output.ListNodesOutput = (
        capo_managedblockchain.types.list_nodes_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_managedblockchain._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_managedblockchain._auth._sigv4.build_sigv4_auth_scheme(
                "managedblockchain", options.region
            )
        )
        if sigv4_config is not None:
            return capo_managedblockchain._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_managedblockchain.types.list_nodes_input.ListNodesInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/networks/{NetworkId}/nodes"
    url = url.replace("{NetworkId}", quote(str(input_["network_id"]), safe=""))
    params: dict[str, str] = {}
    if "member_id" in input_:
        params["memberId"] = str(input_["member_id"])
    if "status" in input_:
        params["status"] = str(input_["status"])
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_nodes(
    options: OperationOptions,
    input_: capo_managedblockchain.types.list_nodes_input.ListNodesInput,
) -> tuple[
    capo_managedblockchain.types.list_nodes_output.ListNodesOutput, zapros.Response
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


async def async_list_nodes(
    options: AsyncOperationOptions,
    input_: capo_managedblockchain.types.list_nodes_input.ListNodesInput,
) -> tuple[
    capo_managedblockchain.types.list_nodes_output.ListNodesOutput, zapros.Response
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
