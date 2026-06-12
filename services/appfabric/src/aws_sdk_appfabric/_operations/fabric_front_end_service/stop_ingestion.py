"""Generated from Smithy shape ``com.amazonaws.appfabric#StopIngestion``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_appfabric._auth._signers
import aws_sdk_appfabric._auth._sigv4
from aws_sdk_appfabric._protocol.errors import parse_error_metadata_json
from aws_sdk_appfabric._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_appfabric._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_appfabric.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.stop_ingestion_request
    import aws_sdk_appfabric.types.stop_ingestion_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_appfabric.errors.access_denied_exception

            raise aws_sdk_appfabric.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            import aws_sdk_appfabric.errors.conflict_exception

            raise aws_sdk_appfabric.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_appfabric.errors.internal_server_exception

            raise aws_sdk_appfabric.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_appfabric.errors.resource_not_found_exception

            raise aws_sdk_appfabric.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_appfabric.errors.throttling_exception

            raise aws_sdk_appfabric.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_appfabric.errors.validation_exception

            raise aws_sdk_appfabric.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_appfabric.types.stop_ingestion_response.StopIngestionResponse:
    out: aws_sdk_appfabric.types.stop_ingestion_response.StopIngestionResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_appfabric._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_appfabric._auth._sigv4.build_sigv4_auth_scheme(
                "appfabric", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_appfabric._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_appfabric.types.stop_ingestion_request.StopIngestionRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = (
        endpoint.url.rstrip("/")
        + "/appbundles/{appBundleIdentifier}/ingestions/{ingestionIdentifier}/stop"
    )
    url = url.replace(
        "{ingestionIdentifier}", quote(str(input["ingestion_identifier"]), safe="")
    )
    url = url.replace(
        "{appBundleIdentifier}", quote(str(input["app_bundle_identifier"]), safe="")
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
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


def stop_ingestion(
    options: OperationOptions,
    input: aws_sdk_appfabric.types.stop_ingestion_request.StopIngestionRequest,
) -> tuple[
    aws_sdk_appfabric.types.stop_ingestion_response.StopIngestionResponse,
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


async def async_stop_ingestion(
    options: AsyncOperationOptions,
    input: aws_sdk_appfabric.types.stop_ingestion_request.StopIngestionRequest,
) -> tuple[
    aws_sdk_appfabric.types.stop_ingestion_response.StopIngestionResponse,
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
