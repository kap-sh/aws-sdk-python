"""Generated from Smithy shape ``com.amazonaws.connecthealth#ListDomains``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_connecthealth._auth._signers
import aws_sdk_connecthealth._auth._sigv4
import aws_sdk_connecthealth.types.domain_status
import aws_sdk_connecthealth.types.domain_summary_list
import aws_sdk_connecthealth.types.list_domains_input
import aws_sdk_connecthealth.types.list_domains_output
from aws_sdk_connecthealth._protocol.errors import parse_error_metadata_json
from aws_sdk_connecthealth._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_connecthealth._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_connecthealth.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_connecthealth.types.list_domains_output.ListDomainsOutput:
    out: aws_sdk_connecthealth.types.list_domains_output.ListDomainsOutput = (
        aws_sdk_connecthealth.types.list_domains_output.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_connecthealth.types.list_domains_output.ListDomainsOutput:
    out: aws_sdk_connecthealth.types.list_domains_output.ListDomainsOutput = (
        aws_sdk_connecthealth.types.list_domains_output.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_connecthealth._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_connecthealth._auth._sigv4.build_sigv4_auth_scheme(
                "health-agent", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_connecthealth._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_connecthealth.types.list_domains_input.ListDomainsInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/domain"
    params: dict[str, str] = {}
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


def list_domains(
    options: OperationOptions,
    input_: aws_sdk_connecthealth.types.list_domains_input.ListDomainsInput,
) -> tuple[
    aws_sdk_connecthealth.types.list_domains_output.ListDomainsOutput, zapros.Response
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


async def async_list_domains(
    options: AsyncOperationOptions,
    input_: aws_sdk_connecthealth.types.list_domains_input.ListDomainsInput,
) -> tuple[
    aws_sdk_connecthealth.types.list_domains_output.ListDomainsOutput, zapros.Response
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
