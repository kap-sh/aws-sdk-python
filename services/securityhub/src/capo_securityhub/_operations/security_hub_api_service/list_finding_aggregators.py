"""Generated from Smithy shape ``com.amazonaws.securityhub#ListFindingAggregators``."""

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
import capo_securityhub.types.finding_aggregator_list
import capo_securityhub.types.list_finding_aggregators_request
import capo_securityhub.types.list_finding_aggregators_response
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
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_securityhub.types.list_finding_aggregators_response.ListFindingAggregatorsResponse:
    out: capo_securityhub.types.list_finding_aggregators_response.ListFindingAggregatorsResponse = capo_securityhub.types.list_finding_aggregators_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_securityhub.types.list_finding_aggregators_response.ListFindingAggregatorsResponse:
    out: capo_securityhub.types.list_finding_aggregators_response.ListFindingAggregatorsResponse = capo_securityhub.types.list_finding_aggregators_response.deserialize_json(
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
    input_: capo_securityhub.types.list_finding_aggregators_request.ListFindingAggregatorsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/findingAggregator/list"
    params: dict[str, str] = {}
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    if "max_results" in input_:
        params["MaxResults"] = str(input_["max_results"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_finding_aggregators(
    options: OperationOptions,
    input_: capo_securityhub.types.list_finding_aggregators_request.ListFindingAggregatorsRequest,
) -> tuple[
    capo_securityhub.types.list_finding_aggregators_response.ListFindingAggregatorsResponse,
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


async def async_list_finding_aggregators(
    options: AsyncOperationOptions,
    input_: capo_securityhub.types.list_finding_aggregators_request.ListFindingAggregatorsRequest,
) -> tuple[
    capo_securityhub.types.list_finding_aggregators_response.ListFindingAggregatorsResponse,
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
