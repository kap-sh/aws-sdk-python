"""Generated from Smithy shape ``com.amazonaws.appstream#CreateFleet``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_appstream._auth._signers
import aws_sdk_appstream._auth._sigv4
import aws_sdk_appstream.errors.concurrent_modification_exception
import aws_sdk_appstream.errors.incompatible_image_exception
import aws_sdk_appstream.errors.invalid_account_status_exception
import aws_sdk_appstream.errors.invalid_parameter_combination_exception
import aws_sdk_appstream.errors.invalid_role_exception
import aws_sdk_appstream.errors.limit_exceeded_exception
import aws_sdk_appstream.errors.operation_not_permitted_exception
import aws_sdk_appstream.errors.request_limit_exceeded_exception
import aws_sdk_appstream.errors.resource_already_exists_exception
import aws_sdk_appstream.errors.resource_not_available_exception
import aws_sdk_appstream.errors.resource_not_found_exception
import aws_sdk_appstream.types.compute_capacity
import aws_sdk_appstream.types.create_fleet_request
import aws_sdk_appstream.types.create_fleet_result
import aws_sdk_appstream.types.domain_join_info
import aws_sdk_appstream.types.fleet
import aws_sdk_appstream.types.fleet_type
import aws_sdk_appstream.types.platform_type
import aws_sdk_appstream.types.s3_location
import aws_sdk_appstream.types.stream_view
import aws_sdk_appstream.types.tags
import aws_sdk_appstream.types.usb_device_filter_strings
import aws_sdk_appstream.types.volume_config
import aws_sdk_appstream.types.vpc_config
from aws_sdk_appstream._protocol.errors import parse_error_metadata_json
from aws_sdk_appstream._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_appstream._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_appstream.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConcurrentModificationException":
            raise aws_sdk_appstream.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data
            )
        case "IncompatibleImageException":
            raise aws_sdk_appstream.errors.incompatible_image_exception.IncompatibleImageException.from_aws_json_1_1(
                data
            )
        case "InvalidAccountStatusException":
            raise aws_sdk_appstream.errors.invalid_account_status_exception.InvalidAccountStatusException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterCombinationException":
            raise aws_sdk_appstream.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException.from_aws_json_1_1(
                data
            )
        case "InvalidRoleException":
            raise aws_sdk_appstream.errors.invalid_role_exception.InvalidRoleException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            raise aws_sdk_appstream.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "OperationNotPermittedException":
            raise aws_sdk_appstream.errors.operation_not_permitted_exception.OperationNotPermittedException.from_aws_json_1_1(
                data
            )
        case "RequestLimitExceededException":
            raise aws_sdk_appstream.errors.request_limit_exceeded_exception.RequestLimitExceededException.from_aws_json_1_1(
                data
            )
        case "ResourceAlreadyExistsException":
            raise aws_sdk_appstream.errors.resource_already_exists_exception.ResourceAlreadyExistsException.from_aws_json_1_1(
                data
            )
        case "ResourceNotAvailableException":
            raise aws_sdk_appstream.errors.resource_not_available_exception.ResourceNotAvailableException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_appstream.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_appstream.types.create_fleet_result.CreateFleetResult:
    out: aws_sdk_appstream.types.create_fleet_result.CreateFleetResult = (
        aws_sdk_appstream.types.create_fleet_result.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_appstream.types.create_fleet_result.CreateFleetResult:
    out: aws_sdk_appstream.types.create_fleet_result.CreateFleetResult = (
        aws_sdk_appstream.types.create_fleet_result.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_appstream._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_appstream._auth._sigv4.build_sigv4_auth_scheme(
                "appstream", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_appstream._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_appstream.types.create_fleet_request.CreateFleetRequest,
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
    headers["X-Amz-Target"] = "PhotonAdminProxyService.CreateFleet"
    body: bytes | None = json.dumps(
        aws_sdk_appstream.types.create_fleet_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_fleet(
    options: OperationOptions,
    input_: aws_sdk_appstream.types.create_fleet_request.CreateFleetRequest,
) -> tuple[
    aws_sdk_appstream.types.create_fleet_result.CreateFleetResult, zapros.Response
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


async def async_create_fleet(
    options: AsyncOperationOptions,
    input_: aws_sdk_appstream.types.create_fleet_request.CreateFleetRequest,
) -> tuple[
    aws_sdk_appstream.types.create_fleet_result.CreateFleetResult, zapros.Response
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
