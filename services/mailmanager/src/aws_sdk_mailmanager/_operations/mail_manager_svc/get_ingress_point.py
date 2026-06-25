"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetIngressPoint``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_mailmanager._auth._signers
import aws_sdk_mailmanager._auth._sigv4
import aws_sdk_mailmanager.errors.resource_not_found_exception
import aws_sdk_mailmanager.errors.validation_exception
import aws_sdk_mailmanager.types.get_ingress_point_request
import aws_sdk_mailmanager.types.get_ingress_point_response
import aws_sdk_mailmanager.types.ingress_point_auth_configuration
import aws_sdk_mailmanager.types.ingress_point_status
import aws_sdk_mailmanager.types.ingress_point_type
import aws_sdk_mailmanager.types.network_configuration
import aws_sdk_mailmanager.types.tls_policy
import aws_sdk_mailmanager.types.trust_store_response_option
from aws_sdk_mailmanager._protocol.errors import parse_error_metadata_json
from aws_sdk_mailmanager._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_mailmanager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_mailmanager.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ResourceNotFoundException":
            raise aws_sdk_mailmanager.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ValidationException":
            raise aws_sdk_mailmanager.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_mailmanager.types.get_ingress_point_response.GetIngressPointResponse:
    out: aws_sdk_mailmanager.types.get_ingress_point_response.GetIngressPointResponse = aws_sdk_mailmanager.types.get_ingress_point_response.deserialize_aws_json_1_0(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_mailmanager.types.get_ingress_point_response.GetIngressPointResponse:
    out: aws_sdk_mailmanager.types.get_ingress_point_response.GetIngressPointResponse = aws_sdk_mailmanager.types.get_ingress_point_response.deserialize_aws_json_1_0(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_mailmanager._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_mailmanager._auth._sigv4.build_sigv4_auth_scheme(
                "ses", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_mailmanager._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_mailmanager.types.get_ingress_point_request.GetIngressPointRequest,
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
    headers["X-Amz-Target"] = "MailManagerSvc.GetIngressPoint"
    body: bytes | None = json.dumps(
        aws_sdk_mailmanager.types.get_ingress_point_request.serialize_aws_json_1_0(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def get_ingress_point(
    options: OperationOptions,
    input_: aws_sdk_mailmanager.types.get_ingress_point_request.GetIngressPointRequest,
) -> tuple[
    aws_sdk_mailmanager.types.get_ingress_point_response.GetIngressPointResponse,
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


async def async_get_ingress_point(
    options: AsyncOperationOptions,
    input_: aws_sdk_mailmanager.types.get_ingress_point_request.GetIngressPointRequest,
) -> tuple[
    aws_sdk_mailmanager.types.get_ingress_point_response.GetIngressPointResponse,
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
