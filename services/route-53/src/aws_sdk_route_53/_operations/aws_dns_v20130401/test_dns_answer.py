"""Generated from Smithy shape ``com.amazonaws.route53#TestDNSAnswer``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_route_53._auth._signers
import aws_sdk_route_53._auth._sigv4
import aws_sdk_route_53.errors.invalid_input
import aws_sdk_route_53.errors.no_such_hosted_zone
import aws_sdk_route_53.types.record_data
import aws_sdk_route_53.types.rr_type
import aws_sdk_route_53.types.test_dns_answer_request
import aws_sdk_route_53.types.test_dns_answer_response
from aws_sdk_route_53._protocol.errors import parse_error_metadata
from aws_sdk_route_53._protocol.xml import fromstring
from aws_sdk_route_53._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_route_53._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_route_53.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidInput":
            raise aws_sdk_route_53.errors.invalid_input.InvalidInput.from_xml(root)
        case "NoSuchHostedZone":
            raise aws_sdk_route_53.errors.no_such_hosted_zone.NoSuchHostedZone.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_route_53.types.test_dns_answer_response.TestDNSAnswerResponse:
    out: aws_sdk_route_53.types.test_dns_answer_response.TestDNSAnswerResponse = (
        aws_sdk_route_53.types.test_dns_answer_response.deserialize_xml(
            fromstring(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_route_53.types.test_dns_answer_response.TestDNSAnswerResponse:
    out: aws_sdk_route_53.types.test_dns_answer_response.TestDNSAnswerResponse = (
        aws_sdk_route_53.types.test_dns_answer_response.deserialize_xml(
            fromstring(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_route_53._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_route_53._auth._sigv4.build_sigv4_auth_scheme(
                "route53", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_route_53._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_route_53.types.test_dns_answer_request.TestDNSAnswerRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2013-04-01/testdnsanswer"
    params: dict[str, str] = {}
    if "hosted_zone_id" in input_:
        params["hostedzoneid"] = str(input_["hosted_zone_id"])
    if "record_name" in input_:
        params["recordname"] = str(input_["record_name"])
    if "record_type" in input_:
        params["recordtype"] = str(input_["record_type"])
    if "resolver_ip" in input_:
        params["resolverip"] = str(input_["resolver_ip"])
    if "edns0_client_subnet_ip" in input_:
        params["edns0clientsubnetip"] = str(input_["edns0_client_subnet_ip"])
    if "edns0_client_subnet_mask" in input_:
        params["edns0clientsubnetmask"] = str(input_["edns0_client_subnet_mask"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def test_dns_answer(
    options: OperationOptions,
    input_: aws_sdk_route_53.types.test_dns_answer_request.TestDNSAnswerRequest,
) -> tuple[
    aws_sdk_route_53.types.test_dns_answer_response.TestDNSAnswerResponse,
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


async def async_test_dns_answer(
    options: AsyncOperationOptions,
    input_: aws_sdk_route_53.types.test_dns_answer_request.TestDNSAnswerRequest,
) -> tuple[
    aws_sdk_route_53.types.test_dns_answer_response.TestDNSAnswerResponse,
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
