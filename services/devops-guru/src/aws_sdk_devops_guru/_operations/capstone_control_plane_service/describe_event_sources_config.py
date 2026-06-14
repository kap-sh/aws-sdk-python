"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeEventSourcesConfig``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_devops_guru._auth._signers
import aws_sdk_devops_guru._auth._sigv4
from aws_sdk_devops_guru._protocol.errors import parse_error_metadata_json
from aws_sdk_devops_guru._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_devops_guru._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_devops_guru.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.describe_event_sources_config_request
    import aws_sdk_devops_guru.types.describe_event_sources_config_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_devops_guru.errors.access_denied_exception

            raise aws_sdk_devops_guru.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_devops_guru.errors.internal_server_exception

            raise aws_sdk_devops_guru.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_devops_guru.errors.throttling_exception

            raise aws_sdk_devops_guru.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_devops_guru.errors.validation_exception

            raise aws_sdk_devops_guru.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_devops_guru.types.describe_event_sources_config_response.DescribeEventSourcesConfigResponse:
    import aws_sdk_devops_guru.types.describe_event_sources_config_response

    out: aws_sdk_devops_guru.types.describe_event_sources_config_response.DescribeEventSourcesConfigResponse = aws_sdk_devops_guru.types.describe_event_sources_config_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_devops_guru._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_devops_guru._auth._sigv4.build_sigv4_auth_scheme(
                "devops-guru", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_devops_guru._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_devops_guru.types.describe_event_sources_config_request.DescribeEventSourcesConfigRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/event-sources"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def describe_event_sources_config(
    options: OperationOptions,
    input_: aws_sdk_devops_guru.types.describe_event_sources_config_request.DescribeEventSourcesConfigRequest,
) -> tuple[
    aws_sdk_devops_guru.types.describe_event_sources_config_response.DescribeEventSourcesConfigResponse,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_describe_event_sources_config(
    options: AsyncOperationOptions,
    input_: aws_sdk_devops_guru.types.describe_event_sources_config_request.DescribeEventSourcesConfigRequest,
) -> tuple[
    aws_sdk_devops_guru.types.describe_event_sources_config_response.DescribeEventSourcesConfigResponse,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
