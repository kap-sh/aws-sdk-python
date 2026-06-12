"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerLog``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_lightsail._auth._signers
import aws_sdk_lightsail._auth._sigv4
from aws_sdk_lightsail._protocol.errors import parse_error_metadata_json
from aws_sdk_lightsail._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_lightsail._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_lightsail.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.get_container_log_request
    import aws_sdk_lightsail.types.get_container_log_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_lightsail.errors.access_denied_exception

            raise aws_sdk_lightsail.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "InvalidInputException":
            import aws_sdk_lightsail.errors.invalid_input_exception

            raise aws_sdk_lightsail.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_1(
                data
            )
        case "NotFoundException":
            import aws_sdk_lightsail.errors.not_found_exception

            raise aws_sdk_lightsail.errors.not_found_exception.NotFoundException.from_aws_json_1_1(
                data
            )
        case "RegionSetupInProgressException":
            import aws_sdk_lightsail.errors.region_setup_in_progress_exception

            raise aws_sdk_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException.from_aws_json_1_1(
                data
            )
        case "ServiceException":
            import aws_sdk_lightsail.errors.service_exception

            raise aws_sdk_lightsail.errors.service_exception.ServiceException.from_aws_json_1_1(
                data
            )
        case "UnauthenticatedException":
            import aws_sdk_lightsail.errors.unauthenticated_exception

            raise aws_sdk_lightsail.errors.unauthenticated_exception.UnauthenticatedException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_lightsail.types.get_container_log_result.GetContainerLogResult:
    import aws_sdk_lightsail.types.get_container_log_result

    out: aws_sdk_lightsail.types.get_container_log_result.GetContainerLogResult = (
        aws_sdk_lightsail.types.get_container_log_result.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_lightsail._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_lightsail._auth._sigv4.build_sigv4_auth_scheme(
                "lightsail", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_lightsail._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_lightsail.types.get_container_log_request.GetContainerLogRequest,
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
        + "/ls/api/2016-11-28/container-services/{serviceName}/containers/{containerName}/log"
    )
    url = url.replace("{serviceName}", quote(str(input["service_name"]), safe=""))
    url = url.replace("{containerName}", quote(str(input["container_name"]), safe=""))
    params: dict[str, str] = {}
    if "start_time" in input:
        params["startTime"] = str(input["start_time"])
    if "end_time" in input:
        params["endTime"] = str(input["end_time"])
    if "filter_pattern" in input:
        params["filterPattern"] = str(input["filter_pattern"])
    if "page_token" in input:
        params["pageToken"] = str(input["page_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "Lightsail_20161128.GetContainerLog"
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "GET",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def get_container_log(
    options: OperationOptions,
    input: aws_sdk_lightsail.types.get_container_log_request.GetContainerLogRequest,
) -> tuple[
    aws_sdk_lightsail.types.get_container_log_result.GetContainerLogResult,
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


async def async_get_container_log(
    options: AsyncOperationOptions,
    input: aws_sdk_lightsail.types.get_container_log_request.GetContainerLogRequest,
) -> tuple[
    aws_sdk_lightsail.types.get_container_log_result.GetContainerLogResult,
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
