"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutPermission``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_eventbridge._auth._signers
import aws_sdk_eventbridge._auth._sigv4
from aws_sdk_eventbridge._protocol.errors import parse_error_metadata_json
from aws_sdk_eventbridge._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_eventbridge._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_eventbridge.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.put_permission_request


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConcurrentModificationException":
            import aws_sdk_eventbridge.errors.concurrent_modification_exception

            raise aws_sdk_eventbridge.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data
            )
        case "InternalException":
            import aws_sdk_eventbridge.errors.internal_exception

            raise aws_sdk_eventbridge.errors.internal_exception.InternalException.from_aws_json_1_1(
                data
            )
        case "OperationDisabledException":
            import aws_sdk_eventbridge.errors.operation_disabled_exception

            raise aws_sdk_eventbridge.errors.operation_disabled_exception.OperationDisabledException.from_aws_json_1_1(
                data
            )
        case "PolicyLengthExceededException":
            import aws_sdk_eventbridge.errors.policy_length_exceeded_exception

            raise aws_sdk_eventbridge.errors.policy_length_exceeded_exception.PolicyLengthExceededException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_eventbridge.errors.resource_not_found_exception

            raise aws_sdk_eventbridge.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_eventbridge._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_eventbridge._auth._sigv4.build_sigv4_auth_scheme(
                "events", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_eventbridge._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_eventbridge.types.put_permission_request.PutPermissionRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            EndpointId=options.endpoint_id,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSEvents.PutPermission"
    import aws_sdk_eventbridge.types.put_permission_request

    body: bytes | None = json.dumps(
        aws_sdk_eventbridge.types.put_permission_request.serialize_aws_json_1_1(input)
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


def put_permission(
    options: OperationOptions,
    input: aws_sdk_eventbridge.types.put_permission_request.PutPermissionRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_put_permission(
    options: AsyncOperationOptions,
    input: aws_sdk_eventbridge.types.put_permission_request.PutPermissionRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
