"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetKey``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_payment_cryptography._auth._signers
import aws_sdk_payment_cryptography._auth._sigv4
import aws_sdk_payment_cryptography.errors.access_denied_exception
import aws_sdk_payment_cryptography.errors.internal_server_exception
import aws_sdk_payment_cryptography.errors.resource_not_found_exception
import aws_sdk_payment_cryptography.errors.service_unavailable_exception
import aws_sdk_payment_cryptography.errors.throttling_exception
import aws_sdk_payment_cryptography.errors.validation_exception
import aws_sdk_payment_cryptography.types.get_key_input
import aws_sdk_payment_cryptography.types.get_key_output
import aws_sdk_payment_cryptography.types.key
from aws_sdk_payment_cryptography._protocol.errors import parse_error_metadata_json
from aws_sdk_payment_cryptography._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_payment_cryptography._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_payment_cryptography.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_payment_cryptography.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data
            )
        case "InternalServerException":
            raise aws_sdk_payment_cryptography.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_payment_cryptography.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_payment_cryptography.errors.service_unavailable_exception.ServiceUnavailableException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_payment_cryptography.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case "ValidationException":
            raise aws_sdk_payment_cryptography.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_payment_cryptography.types.get_key_output.GetKeyOutput:
    out: aws_sdk_payment_cryptography.types.get_key_output.GetKeyOutput = (
        aws_sdk_payment_cryptography.types.get_key_output.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_payment_cryptography.types.get_key_output.GetKeyOutput:
    out: aws_sdk_payment_cryptography.types.get_key_output.GetKeyOutput = (
        aws_sdk_payment_cryptography.types.get_key_output.deserialize_aws_json_1_0(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_payment_cryptography._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_payment_cryptography._auth._sigv4.build_sigv4_auth_scheme(
                "payment-cryptography", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_payment_cryptography._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_payment_cryptography.types.get_key_input.GetKeyInput,
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
    headers["X-Amz-Target"] = "PaymentCryptographyControlPlane.GetKey"
    import aws_sdk_payment_cryptography.types.get_key_input

    body: bytes | None = json.dumps(
        aws_sdk_payment_cryptography.types.get_key_input.serialize_aws_json_1_0(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def get_key(
    options: OperationOptions,
    input_: aws_sdk_payment_cryptography.types.get_key_input.GetKeyInput,
) -> tuple[
    aws_sdk_payment_cryptography.types.get_key_output.GetKeyOutput, zapros.Response
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


async def async_get_key(
    options: AsyncOperationOptions,
    input_: aws_sdk_payment_cryptography.types.get_key_input.GetKeyInput,
) -> tuple[
    aws_sdk_payment_cryptography.types.get_key_output.GetKeyOutput, zapros.Response
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
