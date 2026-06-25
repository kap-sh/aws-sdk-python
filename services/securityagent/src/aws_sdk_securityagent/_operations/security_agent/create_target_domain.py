"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateTargetDomain``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_securityagent._auth._signers
import aws_sdk_securityagent._auth._sigv4
import aws_sdk_securityagent.types.create_target_domain_input
import aws_sdk_securityagent.types.create_target_domain_output
import aws_sdk_securityagent.types.domain_verification_method
import aws_sdk_securityagent.types.tag_map
import aws_sdk_securityagent.types.target_domain_status
import aws_sdk_securityagent.types.verification_details
from aws_sdk_securityagent._protocol.errors import parse_error_metadata_json
from aws_sdk_securityagent._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_securityagent._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_securityagent.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_securityagent.types.create_target_domain_output.CreateTargetDomainOutput:
    out: aws_sdk_securityagent.types.create_target_domain_output.CreateTargetDomainOutput = aws_sdk_securityagent.types.create_target_domain_output.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_securityagent.types.create_target_domain_output.CreateTargetDomainOutput:
    out: aws_sdk_securityagent.types.create_target_domain_output.CreateTargetDomainOutput = aws_sdk_securityagent.types.create_target_domain_output.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_securityagent._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_securityagent._auth._sigv4.build_sigv4_auth_scheme(
                "securityagent", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_securityagent._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_securityagent.types.create_target_domain_input.CreateTargetDomainInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/CreateTargetDomain"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_securityagent.types.create_target_domain_input.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_target_domain(
    options: OperationOptions,
    input_: aws_sdk_securityagent.types.create_target_domain_input.CreateTargetDomainInput,
) -> tuple[
    aws_sdk_securityagent.types.create_target_domain_output.CreateTargetDomainOutput,
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


async def async_create_target_domain(
    options: AsyncOperationOptions,
    input_: aws_sdk_securityagent.types.create_target_domain_input.CreateTargetDomainInput,
) -> tuple[
    aws_sdk_securityagent.types.create_target_domain_output.CreateTargetDomainOutput,
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
