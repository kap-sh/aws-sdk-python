"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegisterCertificate``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_directory_service._auth._signers
import aws_sdk_directory_service._auth._sigv4
from aws_sdk_directory_service._protocol.errors import parse_error_metadata_json
from aws_sdk_directory_service._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_directory_service._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_directory_service.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.register_certificate_request
    import aws_sdk_directory_service.types.register_certificate_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CertificateAlreadyExistsException":
            import aws_sdk_directory_service.errors.certificate_already_exists_exception

            raise aws_sdk_directory_service.errors.certificate_already_exists_exception.CertificateAlreadyExistsException.from_aws_json_1_1(
                data
            )
        case "CertificateLimitExceededException":
            import aws_sdk_directory_service.errors.certificate_limit_exceeded_exception

            raise aws_sdk_directory_service.errors.certificate_limit_exceeded_exception.CertificateLimitExceededException.from_aws_json_1_1(
                data
            )
        case "ClientException":
            import aws_sdk_directory_service.errors.client_exception

            raise aws_sdk_directory_service.errors.client_exception.ClientException.from_aws_json_1_1(
                data
            )
        case "DirectoryDoesNotExistException":
            import aws_sdk_directory_service.errors.directory_does_not_exist_exception

            raise aws_sdk_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "DirectoryUnavailableException":
            import aws_sdk_directory_service.errors.directory_unavailable_exception

            raise aws_sdk_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException.from_aws_json_1_1(
                data
            )
        case "InvalidCertificateException":
            import aws_sdk_directory_service.errors.invalid_certificate_exception

            raise aws_sdk_directory_service.errors.invalid_certificate_exception.InvalidCertificateException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            import aws_sdk_directory_service.errors.invalid_parameter_exception

            raise aws_sdk_directory_service.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "ServiceException":
            import aws_sdk_directory_service.errors.service_exception

            raise aws_sdk_directory_service.errors.service_exception.ServiceException.from_aws_json_1_1(
                data
            )
        case "UnsupportedOperationException":
            import aws_sdk_directory_service.errors.unsupported_operation_exception

            raise aws_sdk_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_directory_service.types.register_certificate_result.RegisterCertificateResult:
    import aws_sdk_directory_service.types.register_certificate_result

    out: aws_sdk_directory_service.types.register_certificate_result.RegisterCertificateResult = aws_sdk_directory_service.types.register_certificate_result.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_directory_service._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_directory_service._auth._sigv4.build_sigv4_auth_scheme(
                "ds", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_directory_service._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_directory_service.types.register_certificate_request.RegisterCertificateRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "DirectoryService_20150416.RegisterCertificate"
    import aws_sdk_directory_service.types.register_certificate_request

    body: bytes | None = json.dumps(
        aws_sdk_directory_service.types.register_certificate_request.serialize_aws_json_1_1(
            input
        )
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


def register_certificate(
    options: OperationOptions,
    input: aws_sdk_directory_service.types.register_certificate_request.RegisterCertificateRequest,
) -> tuple[
    aws_sdk_directory_service.types.register_certificate_result.RegisterCertificateResult,
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


async def async_register_certificate(
    options: AsyncOperationOptions,
    input: aws_sdk_directory_service.types.register_certificate_request.RegisterCertificateRequest,
) -> tuple[
    aws_sdk_directory_service.types.register_certificate_result.RegisterCertificateResult,
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
