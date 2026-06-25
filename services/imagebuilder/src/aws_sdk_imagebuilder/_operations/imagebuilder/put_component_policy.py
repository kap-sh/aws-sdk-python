"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PutComponentPolicy``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_imagebuilder._auth._signers
import aws_sdk_imagebuilder._auth._sigv4
import aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception
import aws_sdk_imagebuilder.errors.client_exception
import aws_sdk_imagebuilder.errors.forbidden_exception
import aws_sdk_imagebuilder.errors.invalid_parameter_value_exception
import aws_sdk_imagebuilder.errors.invalid_request_exception
import aws_sdk_imagebuilder.errors.resource_not_found_exception
import aws_sdk_imagebuilder.errors.service_exception
import aws_sdk_imagebuilder.errors.service_unavailable_exception
import aws_sdk_imagebuilder.types.put_component_policy_request
import aws_sdk_imagebuilder.types.put_component_policy_response
from aws_sdk_imagebuilder._protocol.errors import parse_error_metadata_json
from aws_sdk_imagebuilder._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_imagebuilder._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_imagebuilder.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CallRateLimitExceededException":
            raise aws_sdk_imagebuilder.errors.call_rate_limit_exceeded_exception.CallRateLimitExceededException.from_json(
                data
            )
        case "ClientException":
            raise aws_sdk_imagebuilder.errors.client_exception.ClientException.from_json(
                data
            )
        case "ForbiddenException":
            raise aws_sdk_imagebuilder.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "InvalidParameterValueException":
            raise aws_sdk_imagebuilder.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "InvalidRequestException":
            raise aws_sdk_imagebuilder.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_imagebuilder.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceException":
            raise aws_sdk_imagebuilder.errors.service_exception.ServiceException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_imagebuilder.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_imagebuilder.types.put_component_policy_response.PutComponentPolicyResponse
):
    out: aws_sdk_imagebuilder.types.put_component_policy_response.PutComponentPolicyResponse = aws_sdk_imagebuilder.types.put_component_policy_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_imagebuilder.types.put_component_policy_response.PutComponentPolicyResponse
):
    out: aws_sdk_imagebuilder.types.put_component_policy_response.PutComponentPolicyResponse = aws_sdk_imagebuilder.types.put_component_policy_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_imagebuilder._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_imagebuilder._auth._sigv4.build_sigv4_auth_scheme(
                "imagebuilder", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_imagebuilder._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_imagebuilder.types.put_component_policy_request.PutComponentPolicyRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/PutComponentPolicy"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_imagebuilder.types.put_component_policy_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def put_component_policy(
    options: OperationOptions,
    input_: aws_sdk_imagebuilder.types.put_component_policy_request.PutComponentPolicyRequest,
) -> tuple[
    aws_sdk_imagebuilder.types.put_component_policy_response.PutComponentPolicyResponse,
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


async def async_put_component_policy(
    options: AsyncOperationOptions,
    input_: aws_sdk_imagebuilder.types.put_component_policy_request.PutComponentPolicyRequest,
) -> tuple[
    aws_sdk_imagebuilder.types.put_component_policy_response.PutComponentPolicyResponse,
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
