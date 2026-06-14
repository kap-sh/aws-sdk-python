"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#RegisterUsage``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

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
    import aws_sdk_marketplace_metering.types.register_usage_request
    import aws_sdk_marketplace_metering.types.register_usage_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CustomerNotEntitledException":
            import aws_sdk_marketplace_metering.errors.customer_not_entitled_exception

            raise aws_sdk_marketplace_metering.errors.customer_not_entitled_exception.CustomerNotEntitledException.from_aws_json_1_1(
                data
            )
        case "DisabledApiException":
            import aws_sdk_marketplace_metering.errors.disabled_api_exception

            raise aws_sdk_marketplace_metering.errors.disabled_api_exception.DisabledApiException.from_aws_json_1_1(
                data
            )
        case "InternalServiceErrorException":
            import aws_sdk_marketplace_metering.errors.internal_service_error_exception

            raise aws_sdk_marketplace_metering.errors.internal_service_error_exception.InternalServiceErrorException.from_aws_json_1_1(
                data
            )
        case "InvalidProductCodeException":
            import aws_sdk_marketplace_metering.errors.invalid_product_code_exception

            raise aws_sdk_marketplace_metering.errors.invalid_product_code_exception.InvalidProductCodeException.from_aws_json_1_1(
                data
            )
        case "InvalidPublicKeyVersionException":
            import aws_sdk_marketplace_metering.errors.invalid_public_key_version_exception

            raise aws_sdk_marketplace_metering.errors.invalid_public_key_version_exception.InvalidPublicKeyVersionException.from_aws_json_1_1(
                data
            )
        case "InvalidRegionException":
            import aws_sdk_marketplace_metering.errors.invalid_region_exception

            raise aws_sdk_marketplace_metering.errors.invalid_region_exception.InvalidRegionException.from_aws_json_1_1(
                data
            )
        case "PlatformNotSupportedException":
            import aws_sdk_marketplace_metering.errors.platform_not_supported_exception

            raise aws_sdk_marketplace_metering.errors.platform_not_supported_exception.PlatformNotSupportedException.from_aws_json_1_1(
                data
            )
        case "ThrottlingException":
            import aws_sdk_marketplace_metering.errors.throttling_exception

            raise aws_sdk_marketplace_metering.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_marketplace_metering.types.register_usage_result.RegisterUsageResult:
    import aws_sdk_marketplace_metering.types.register_usage_result

    out: aws_sdk_marketplace_metering.types.register_usage_result.RegisterUsageResult = aws_sdk_marketplace_metering.types.register_usage_result.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_marketplace_metering._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input_: aws_sdk_marketplace_metering.types.register_usage_request.RegisterUsageRequest,
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
    headers["X-Amz-Target"] = "AWSMPMeteringService.RegisterUsage"
    import aws_sdk_marketplace_metering.types.register_usage_request

    body: bytes | None = json.dumps(
        aws_sdk_marketplace_metering.types.register_usage_request.serialize_aws_json_1_1(
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


def register_usage(
    options: OperationOptions,
    input_: aws_sdk_marketplace_metering.types.register_usage_request.RegisterUsageRequest,
) -> tuple[
    aws_sdk_marketplace_metering.types.register_usage_result.RegisterUsageResult,
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


async def async_register_usage(
    options: AsyncOperationOptions,
    input_: aws_sdk_marketplace_metering.types.register_usage_request.RegisterUsageRequest,
) -> tuple[
    aws_sdk_marketplace_metering.types.register_usage_result.RegisterUsageResult,
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
