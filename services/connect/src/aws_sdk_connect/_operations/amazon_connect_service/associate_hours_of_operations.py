"""Generated from Smithy shape ``com.amazonaws.connect#AssociateHoursOfOperations``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_connect._auth._signers
import aws_sdk_connect._auth._sigv4
import aws_sdk_connect.errors.conditional_operation_failed_exception
import aws_sdk_connect.errors.internal_service_exception
import aws_sdk_connect.errors.invalid_parameter_exception
import aws_sdk_connect.errors.invalid_request_exception
import aws_sdk_connect.errors.resource_not_found_exception
import aws_sdk_connect.errors.service_quota_exceeded_exception
import aws_sdk_connect.errors.throttling_exception
import aws_sdk_connect.types.associate_hours_of_operations_request
import aws_sdk_connect.types.parent_hours_of_operation_config_list
from aws_sdk_connect._protocol.errors import parse_error_metadata_json
from aws_sdk_connect._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_connect._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_connect.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConditionalOperationFailedException":
            raise aws_sdk_connect.errors.conditional_operation_failed_exception.ConditionalOperationFailedException.from_json(
                data
            )
        case "InternalServiceException":
            raise aws_sdk_connect.errors.internal_service_exception.InternalServiceException.from_json(
                data
            )
        case "InvalidParameterException":
            raise aws_sdk_connect.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "InvalidRequestException":
            raise aws_sdk_connect.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_connect.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise aws_sdk_connect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_connect.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_connect._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_connect._auth._sigv4.build_sigv4_auth_scheme(
                "connect", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_connect._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_connect.types.associate_hours_of_operations_request.AssociateHoursOfOperationsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/hours-of-operations/{InstanceId}/{HoursOfOperationId}/associate-hours"
    )
    url = url.replace("{InstanceId}", quote(str(input_["instance_id"]), safe=""))
    url = url.replace(
        "{HoursOfOperationId}", quote(str(input_["hours_of_operation_id"]), safe="")
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_connect.types.associate_hours_of_operations_request

    body: bytes | None = json.dumps(
        aws_sdk_connect.types.associate_hours_of_operations_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def associate_hours_of_operations(
    options: OperationOptions,
    input_: aws_sdk_connect.types.associate_hours_of_operations_request.AssociateHoursOfOperationsRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_associate_hours_of_operations(
    options: AsyncOperationOptions,
    input_: aws_sdk_connect.types.associate_hours_of_operations_request.AssociateHoursOfOperationsRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
