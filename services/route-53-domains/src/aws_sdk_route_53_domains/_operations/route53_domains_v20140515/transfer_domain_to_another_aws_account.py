"""Generated from Smithy shape ``com.amazonaws.route53domains#TransferDomainToAnotherAwsAccount``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_route_53_domains._auth._signers
import aws_sdk_route_53_domains._auth._sigv4
import aws_sdk_route_53_domains.errors.duplicate_request
import aws_sdk_route_53_domains.errors.invalid_input
import aws_sdk_route_53_domains.errors.operation_limit_exceeded
import aws_sdk_route_53_domains.errors.unsupported_tld
import aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_request
import aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_response
from aws_sdk_route_53_domains._protocol.errors import parse_error_metadata_json
from aws_sdk_route_53_domains._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_route_53_domains._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_route_53_domains.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DuplicateRequest":
            raise aws_sdk_route_53_domains.errors.duplicate_request.DuplicateRequest.from_aws_json_1_1(
                data
            )
        case "InvalidInput":
            raise aws_sdk_route_53_domains.errors.invalid_input.InvalidInput.from_aws_json_1_1(
                data
            )
        case "OperationLimitExceeded":
            raise aws_sdk_route_53_domains.errors.operation_limit_exceeded.OperationLimitExceeded.from_aws_json_1_1(
                data
            )
        case "UnsupportedTLD":
            raise aws_sdk_route_53_domains.errors.unsupported_tld.UnsupportedTLD.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_response.TransferDomainToAnotherAwsAccountResponse:
    out: aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_response.TransferDomainToAnotherAwsAccountResponse = aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_response.TransferDomainToAnotherAwsAccountResponse:
    out: aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_response.TransferDomainToAnotherAwsAccountResponse = aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_route_53_domains._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_route_53_domains._auth._sigv4.build_sigv4_auth_scheme(
                "route53domains", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_route_53_domains._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_request.TransferDomainToAnotherAwsAccountRequest,
) -> zapros.Request:
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
        "Route53Domains_v20140515.TransferDomainToAnotherAwsAccount"
    )
    import aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_request

    body: bytes | None = json.dumps(
        aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_request.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def transfer_domain_to_another_aws_account(
    options: OperationOptions,
    input_: aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_request.TransferDomainToAnotherAwsAccountRequest,
) -> tuple[
    aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_response.TransferDomainToAnotherAwsAccountResponse,
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


async def async_transfer_domain_to_another_aws_account(
    options: AsyncOperationOptions,
    input_: aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_request.TransferDomainToAnotherAwsAccountRequest,
) -> tuple[
    aws_sdk_route_53_domains.types.transfer_domain_to_another_aws_account_response.TransferDomainToAnotherAwsAccountResponse,
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
