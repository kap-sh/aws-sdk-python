"""Generated from Smithy shape ``com.amazonaws.iot#CreateOTAUpdate``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_iot._auth._signers
import aws_sdk_iot._auth._sigv4
import aws_sdk_iot.errors.internal_failure_exception
import aws_sdk_iot.errors.invalid_request_exception
import aws_sdk_iot.errors.limit_exceeded_exception
import aws_sdk_iot.errors.resource_already_exists_exception
import aws_sdk_iot.errors.resource_not_found_exception
import aws_sdk_iot.errors.service_unavailable_exception
import aws_sdk_iot.errors.throttling_exception
import aws_sdk_iot.errors.unauthorized_exception
import aws_sdk_iot.types.additional_parameter_map
import aws_sdk_iot.types.aws_job_abort_config
import aws_sdk_iot.types.aws_job_executions_rollout_config
import aws_sdk_iot.types.aws_job_presigned_url_config
import aws_sdk_iot.types.aws_job_timeout_config
import aws_sdk_iot.types.create_ota_update_request
import aws_sdk_iot.types.create_ota_update_response
import aws_sdk_iot.types.ota_update_files
import aws_sdk_iot.types.ota_update_status
import aws_sdk_iot.types.protocols
import aws_sdk_iot.types.tag_list
import aws_sdk_iot.types.target_selection
import aws_sdk_iot.types.targets
from aws_sdk_iot._protocol.errors import parse_error_metadata_json
from aws_sdk_iot._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_iot._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_iot.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalFailureException":
            raise aws_sdk_iot.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "InvalidRequestException":
            raise aws_sdk_iot.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "LimitExceededException":
            raise aws_sdk_iot.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "ResourceAlreadyExistsException":
            raise aws_sdk_iot.errors.resource_already_exists_exception.ResourceAlreadyExistsException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_iot.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_iot.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_iot.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "UnauthorizedException":
            raise aws_sdk_iot.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_iot.types.create_ota_update_response.CreateOTAUpdateResponse:
    out: aws_sdk_iot.types.create_ota_update_response.CreateOTAUpdateResponse = (
        aws_sdk_iot.types.create_ota_update_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_iot.types.create_ota_update_response.CreateOTAUpdateResponse:
    out: aws_sdk_iot.types.create_ota_update_response.CreateOTAUpdateResponse = (
        aws_sdk_iot.types.create_ota_update_response.deserialize_json(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_iot._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_iot._auth._sigv4.build_sigv4_auth_scheme("iot", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_iot._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_iot.types.create_ota_update_request.CreateOTAUpdateRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/otaUpdates/{otaUpdateId}"
    url = url.replace("{otaUpdateId}", quote(str(input_["ota_update_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_iot.types.create_ota_update_request

    body: bytes | None = json.dumps(
        aws_sdk_iot.types.create_ota_update_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_ota_update(
    options: OperationOptions,
    input_: aws_sdk_iot.types.create_ota_update_request.CreateOTAUpdateRequest,
) -> tuple[
    aws_sdk_iot.types.create_ota_update_response.CreateOTAUpdateResponse,
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


async def async_create_ota_update(
    options: AsyncOperationOptions,
    input_: aws_sdk_iot.types.create_ota_update_request.CreateOTAUpdateRequest,
) -> tuple[
    aws_sdk_iot.types.create_ota_update_response.CreateOTAUpdateResponse,
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
