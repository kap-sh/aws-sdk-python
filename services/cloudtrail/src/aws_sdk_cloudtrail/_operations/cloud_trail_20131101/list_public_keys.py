"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListPublicKeys``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_cloudtrail._auth._signers
import aws_sdk_cloudtrail._auth._sigv4
from aws_sdk_cloudtrail._protocol.errors import parse_error_metadata_json
from aws_sdk_cloudtrail._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudtrail._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudtrail.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.list_public_keys_request
    import aws_sdk_cloudtrail.types.list_public_keys_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidTimeRangeException":
            import aws_sdk_cloudtrail.errors.invalid_time_range_exception

            raise aws_sdk_cloudtrail.errors.invalid_time_range_exception.InvalidTimeRangeException.from_aws_json_1_1(
                data
            )
        case "InvalidTokenException":
            import aws_sdk_cloudtrail.errors.invalid_token_exception

            raise aws_sdk_cloudtrail.errors.invalid_token_exception.InvalidTokenException.from_aws_json_1_1(
                data
            )
        case "OperationNotPermittedException":
            import aws_sdk_cloudtrail.errors.operation_not_permitted_exception

            raise aws_sdk_cloudtrail.errors.operation_not_permitted_exception.OperationNotPermittedException.from_aws_json_1_1(
                data
            )
        case "UnsupportedOperationException":
            import aws_sdk_cloudtrail.errors.unsupported_operation_exception

            raise aws_sdk_cloudtrail.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudtrail.types.list_public_keys_response.ListPublicKeysResponse:
    import aws_sdk_cloudtrail.types.list_public_keys_response

    out: aws_sdk_cloudtrail.types.list_public_keys_response.ListPublicKeysResponse = (
        aws_sdk_cloudtrail.types.list_public_keys_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudtrail._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudtrail._auth._sigv4.build_sigv4_auth_scheme(
                "cloudtrail", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudtrail._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cloudtrail.types.list_public_keys_request.ListPublicKeysRequest,
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
    headers["X-Amz-Target"] = "CloudTrail_20131101.ListPublicKeys"
    import aws_sdk_cloudtrail.types.list_public_keys_request

    body: bytes | None = json.dumps(
        aws_sdk_cloudtrail.types.list_public_keys_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_public_keys(
    options: OperationOptions,
    input_: aws_sdk_cloudtrail.types.list_public_keys_request.ListPublicKeysRequest,
) -> tuple[
    aws_sdk_cloudtrail.types.list_public_keys_response.ListPublicKeysResponse,
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


async def async_list_public_keys(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudtrail.types.list_public_keys_request.ListPublicKeysRequest,
) -> tuple[
    aws_sdk_cloudtrail.types.list_public_keys_response.ListPublicKeysResponse,
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
