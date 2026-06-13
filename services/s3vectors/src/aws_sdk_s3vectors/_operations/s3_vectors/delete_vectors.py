"""Generated from Smithy shape ``com.amazonaws.s3vectors#DeleteVectors``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_s3vectors._auth._signers
import aws_sdk_s3vectors._auth._sigv4
from aws_sdk_s3vectors._protocol.errors import parse_error_metadata_json
from aws_sdk_s3vectors._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3vectors._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_s3vectors.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.delete_vectors_input
    import aws_sdk_s3vectors.types.delete_vectors_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_s3vectors.errors.access_denied_exception

            raise aws_sdk_s3vectors.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_s3vectors.errors.internal_server_exception

            raise aws_sdk_s3vectors.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "RequestTimeoutException":
            import aws_sdk_s3vectors.errors.request_timeout_exception

            raise aws_sdk_s3vectors.errors.request_timeout_exception.RequestTimeoutException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_s3vectors.errors.too_many_requests_exception

            raise aws_sdk_s3vectors.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_s3vectors.errors.validation_exception

            raise aws_sdk_s3vectors.errors.validation_exception.ValidationException.from_json(
                data
            )
        case "KmsDisabledException":
            import aws_sdk_s3vectors.errors.kms_disabled_exception

            raise aws_sdk_s3vectors.errors.kms_disabled_exception.KmsDisabledException.from_json(
                data
            )
        case "KmsInvalidKeyUsageException":
            import aws_sdk_s3vectors.errors.kms_invalid_key_usage_exception

            raise aws_sdk_s3vectors.errors.kms_invalid_key_usage_exception.KmsInvalidKeyUsageException.from_json(
                data
            )
        case "KmsInvalidStateException":
            import aws_sdk_s3vectors.errors.kms_invalid_state_exception

            raise aws_sdk_s3vectors.errors.kms_invalid_state_exception.KmsInvalidStateException.from_json(
                data
            )
        case "KmsNotFoundException":
            import aws_sdk_s3vectors.errors.kms_not_found_exception

            raise aws_sdk_s3vectors.errors.kms_not_found_exception.KmsNotFoundException.from_json(
                data
            )
        case "NotFoundException":
            import aws_sdk_s3vectors.errors.not_found_exception

            raise aws_sdk_s3vectors.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_s3vectors.errors.service_unavailable_exception

            raise aws_sdk_s3vectors.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_s3vectors.types.delete_vectors_output.DeleteVectorsOutput:
    out: aws_sdk_s3vectors.types.delete_vectors_output.DeleteVectorsOutput = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_s3vectors._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_s3vectors._auth._sigv4.build_sigv4_auth_scheme(
                "s3vectors", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_s3vectors._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_s3vectors.types.delete_vectors_input.DeleteVectorsInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = endpoint.url.rstrip("/") + "/DeleteVectors"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_s3vectors.types.delete_vectors_input

    body: bytes | None = json.dumps(
        aws_sdk_s3vectors.types.delete_vectors_input.serialize_json(input)
    ).encode()
    headers["content-type"] = "application/json"
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


def delete_vectors(
    options: OperationOptions,
    input: aws_sdk_s3vectors.types.delete_vectors_input.DeleteVectorsInput,
) -> tuple[
    aws_sdk_s3vectors.types.delete_vectors_output.DeleteVectorsOutput, zapros.Response
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


async def async_delete_vectors(
    options: AsyncOperationOptions,
    input: aws_sdk_s3vectors.types.delete_vectors_input.DeleteVectorsInput,
) -> tuple[
    aws_sdk_s3vectors.types.delete_vectors_output.DeleteVectorsOutput, zapros.Response
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
