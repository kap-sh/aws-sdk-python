"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#MeterUsage``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_marketplace_metering._auth._signers
import aws_sdk_marketplace_metering._auth._sigv4
from aws_sdk_marketplace_metering._protocol.errors import parse_error_metadata_json
from aws_sdk_marketplace_metering._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_marketplace_metering._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_marketplace_metering.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.meter_usage_request
    import aws_sdk_marketplace_metering.types.meter_usage_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CustomerNotEntitledException":
            import aws_sdk_marketplace_metering.errors.customer_not_entitled_exception

            raise aws_sdk_marketplace_metering.errors.customer_not_entitled_exception.CustomerNotEntitledException.from_aws_json_1_1(
                data
            )
        case "DuplicateRequestException":
            import aws_sdk_marketplace_metering.errors.duplicate_request_exception

            raise aws_sdk_marketplace_metering.errors.duplicate_request_exception.DuplicateRequestException.from_aws_json_1_1(
                data
            )
        case "IdempotencyConflictException":
            import aws_sdk_marketplace_metering.errors.idempotency_conflict_exception

            raise aws_sdk_marketplace_metering.errors.idempotency_conflict_exception.IdempotencyConflictException.from_aws_json_1_1(
                data
            )
        case "InternalServiceErrorException":
            import aws_sdk_marketplace_metering.errors.internal_service_error_exception

            raise aws_sdk_marketplace_metering.errors.internal_service_error_exception.InternalServiceErrorException.from_aws_json_1_1(
                data
            )
        case "InvalidEndpointRegionException":
            import aws_sdk_marketplace_metering.errors.invalid_endpoint_region_exception

            raise aws_sdk_marketplace_metering.errors.invalid_endpoint_region_exception.InvalidEndpointRegionException.from_aws_json_1_1(
                data
            )
        case "InvalidProductCodeException":
            import aws_sdk_marketplace_metering.errors.invalid_product_code_exception

            raise aws_sdk_marketplace_metering.errors.invalid_product_code_exception.InvalidProductCodeException.from_aws_json_1_1(
                data
            )
        case "InvalidTagException":
            import aws_sdk_marketplace_metering.errors.invalid_tag_exception

            raise aws_sdk_marketplace_metering.errors.invalid_tag_exception.InvalidTagException.from_aws_json_1_1(
                data
            )
        case "InvalidUsageAllocationsException":
            import aws_sdk_marketplace_metering.errors.invalid_usage_allocations_exception

            raise aws_sdk_marketplace_metering.errors.invalid_usage_allocations_exception.InvalidUsageAllocationsException.from_aws_json_1_1(
                data
            )
        case "InvalidUsageDimensionException":
            import aws_sdk_marketplace_metering.errors.invalid_usage_dimension_exception

            raise aws_sdk_marketplace_metering.errors.invalid_usage_dimension_exception.InvalidUsageDimensionException.from_aws_json_1_1(
                data
            )
        case "ThrottlingException":
            import aws_sdk_marketplace_metering.errors.throttling_exception

            raise aws_sdk_marketplace_metering.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data
            )
        case "TimestampOutOfBoundsException":
            import aws_sdk_marketplace_metering.errors.timestamp_out_of_bounds_exception

            raise aws_sdk_marketplace_metering.errors.timestamp_out_of_bounds_exception.TimestampOutOfBoundsException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_marketplace_metering.types.meter_usage_result.MeterUsageResult:
    import aws_sdk_marketplace_metering.types.meter_usage_result

    out: aws_sdk_marketplace_metering.types.meter_usage_result.MeterUsageResult = (
        aws_sdk_marketplace_metering.types.meter_usage_result.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_marketplace_metering._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_marketplace_metering._auth._sigv4.build_sigv4_auth_scheme(
                "aws-marketplace", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_marketplace_metering._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_marketplace_metering.types.meter_usage_request.MeterUsageRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSMPMeteringService.MeterUsage"
    import aws_sdk_marketplace_metering.types.meter_usage_request

    body: bytes | None = json.dumps(
        aws_sdk_marketplace_metering.types.meter_usage_request.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def meter_usage(
    options: OperationOptions,
    input_: aws_sdk_marketplace_metering.types.meter_usage_request.MeterUsageRequest,
) -> tuple[
    aws_sdk_marketplace_metering.types.meter_usage_result.MeterUsageResult,
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


async def async_meter_usage(
    options: AsyncOperationOptions,
    input_: aws_sdk_marketplace_metering.types.meter_usage_request.MeterUsageRequest,
) -> tuple[
    aws_sdk_marketplace_metering.types.meter_usage_result.MeterUsageResult,
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
