"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DeleteGroupingConfiguration``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_application_signals._auth._signers
import aws_sdk_application_signals._auth._sigv4
import aws_sdk_application_signals.errors.access_denied_exception
import aws_sdk_application_signals.errors.throttling_exception
import aws_sdk_application_signals.errors.validation_exception
import aws_sdk_application_signals.types.delete_grouping_configuration_output
from aws_sdk_application_signals._protocol.errors import parse_error_metadata_json
from aws_sdk_application_signals._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_application_signals._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_application_signals.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_application_signals.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_application_signals.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_application_signals.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_application_signals.types.delete_grouping_configuration_output.DeleteGroupingConfigurationOutput:
    out: aws_sdk_application_signals.types.delete_grouping_configuration_output.DeleteGroupingConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_application_signals.types.delete_grouping_configuration_output.DeleteGroupingConfigurationOutput:
    out: aws_sdk_application_signals.types.delete_grouping_configuration_output.DeleteGroupingConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_application_signals._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_application_signals._auth._sigv4.build_sigv4_auth_scheme(
                "application-signals", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_application_signals._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(options: OperationOptions | AsyncOperationOptions) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseFIPS=options.use_fips, Endpoint=options.endpoint, Region=options.region
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/grouping-configuration"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_grouping_configuration(
    options: OperationOptions,
) -> tuple[
    aws_sdk_application_signals.types.delete_grouping_configuration_output.DeleteGroupingConfigurationOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_delete_grouping_configuration(
    options: AsyncOperationOptions,
) -> tuple[
    aws_sdk_application_signals.types.delete_grouping_configuration_output.DeleteGroupingConfigurationOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
