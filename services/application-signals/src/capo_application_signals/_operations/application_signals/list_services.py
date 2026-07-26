"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServices``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_application_signals._auth._signers
import capo_application_signals._auth._sigv4
import capo_application_signals.errors.throttling_exception
import capo_application_signals.errors.validation_exception
import capo_application_signals.types.list_services_input
import capo_application_signals.types.list_services_output
import capo_application_signals.types.service_summaries
from capo_application_signals._protocol.errors import parse_error_metadata_json
from capo_application_signals._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_application_signals._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_application_signals.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ThrottlingException":
            raise capo_application_signals.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_application_signals.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_application_signals.types.list_services_output.ListServicesOutput:
    out: capo_application_signals.types.list_services_output.ListServicesOutput = (
        capo_application_signals.types.list_services_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_application_signals.types.list_services_output.ListServicesOutput:
    out: capo_application_signals.types.list_services_output.ListServicesOutput = (
        capo_application_signals.types.list_services_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_application_signals._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_application_signals._auth._sigv4.build_sigv4_auth_scheme(
                "application-signals", options.region
            )
        )
        if sigv4_config is not None:
            return capo_application_signals._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_application_signals.types.list_services_input.ListServicesInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/services"
    params: dict[str, str] = {}
    if "start_time" in input_:
        params["StartTime"] = str(input_["start_time"])
    if "end_time" in input_:
        params["EndTime"] = str(input_["end_time"])
    params["MaxResults"] = str(input_.get("max_results", 50))
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    params["IncludeLinkedAccounts"] = str(input_.get("include_linked_accounts", False))
    if "aws_account_id" in input_:
        params["AwsAccountId"] = str(input_["aws_account_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_services(
    options: OperationOptions,
    input_: capo_application_signals.types.list_services_input.ListServicesInput,
) -> tuple[
    capo_application_signals.types.list_services_output.ListServicesOutput,
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


async def async_list_services(
    options: AsyncOperationOptions,
    input_: capo_application_signals.types.list_services_input.ListServicesInput,
) -> tuple[
    capo_application_signals.types.list_services_output.ListServicesOutput,
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
