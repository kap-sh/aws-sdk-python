"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyStreamingProperties``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any, cast
from aws_sdk_workspaces._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_workspaces._rule_engine._endpoint_runtime import apply_label
import jmespath
import zapros
from urllib.parse import quote, urlencode
from aws_sdk_workspaces.errors import ServiceError, UnknownServiceError
from aws_sdk_workspaces._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_workspaces._auth._signers
import aws_sdk_workspaces._auth._sigv4
from aws_sdk_workspaces._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
import datetime
from email.utils import parsedate_to_datetime as _parse_http_date

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.modify_streaming_properties_request
    import aws_sdk_workspaces.types.modify_streaming_properties_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_workspaces.errors.access_denied_exception

            raise aws_sdk_workspaces.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterValuesException":
            import aws_sdk_workspaces.errors.invalid_parameter_values_exception

            raise aws_sdk_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException.from_aws_json_1_1(
                data
            )
        case "OperationNotSupportedException":
            import aws_sdk_workspaces.errors.operation_not_supported_exception

            raise aws_sdk_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_workspaces.errors.resource_not_found_exception

            raise aws_sdk_workspaces.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_workspaces.types.modify_streaming_properties_result.ModifyStreamingPropertiesResult:
    out: aws_sdk_workspaces.types.modify_streaming_properties_result.ModifyStreamingPropertiesResult = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_workspaces._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_workspaces._auth._sigv4.build_sigv4_auth_scheme(
                "workspaces", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_workspaces._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_workspaces.types.modify_streaming_properties_request.ModifyStreamingPropertiesRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "WorkspacesService.ModifyStreamingProperties"
    import aws_sdk_workspaces.types.modify_streaming_properties_request

    body: bytes | None = json.dumps(
        aws_sdk_workspaces.types.modify_streaming_properties_request.serialize_aws_json_1_1(
            input
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def modify_streaming_properties(
    options: OperationOptions,
    input: aws_sdk_workspaces.types.modify_streaming_properties_request.ModifyStreamingPropertiesRequest,
) -> tuple[
    aws_sdk_workspaces.types.modify_streaming_properties_result.ModifyStreamingPropertiesResult,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_modify_streaming_properties(
    options: AsyncOperationOptions,
    input: aws_sdk_workspaces.types.modify_streaming_properties_request.ModifyStreamingPropertiesRequest,
) -> tuple[
    aws_sdk_workspaces.types.modify_streaming_properties_result.ModifyStreamingPropertiesResult,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
