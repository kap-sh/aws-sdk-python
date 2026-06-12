"""Generated from Smithy shape ``com.amazonaws.textract#DetectDocumentText``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_textract._auth._signers
import aws_sdk_textract._auth._sigv4
from aws_sdk_textract._protocol.errors import parse_error_metadata_json
from aws_sdk_textract._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_textract._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_textract.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_textract.types.detect_document_text_request
    import aws_sdk_textract.types.detect_document_text_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_textract.errors.access_denied_exception

            raise aws_sdk_textract.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "BadDocumentException":
            import aws_sdk_textract.errors.bad_document_exception

            raise aws_sdk_textract.errors.bad_document_exception.BadDocumentException.from_aws_json_1_1(
                data
            )
        case "DocumentTooLargeException":
            import aws_sdk_textract.errors.document_too_large_exception

            raise aws_sdk_textract.errors.document_too_large_exception.DocumentTooLargeException.from_aws_json_1_1(
                data
            )
        case "InternalServerError":
            import aws_sdk_textract.errors.internal_server_error

            raise aws_sdk_textract.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            import aws_sdk_textract.errors.invalid_parameter_exception

            raise aws_sdk_textract.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "InvalidS3ObjectException":
            import aws_sdk_textract.errors.invalid_s3_object_exception

            raise aws_sdk_textract.errors.invalid_s3_object_exception.InvalidS3ObjectException.from_aws_json_1_1(
                data
            )
        case "ProvisionedThroughputExceededException":
            import aws_sdk_textract.errors.provisioned_throughput_exceeded_exception

            raise aws_sdk_textract.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException.from_aws_json_1_1(
                data
            )
        case "ThrottlingException":
            import aws_sdk_textract.errors.throttling_exception

            raise aws_sdk_textract.errors.throttling_exception.ThrottlingException.from_aws_json_1_1(
                data
            )
        case "UnsupportedDocumentException":
            import aws_sdk_textract.errors.unsupported_document_exception

            raise aws_sdk_textract.errors.unsupported_document_exception.UnsupportedDocumentException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_textract.types.detect_document_text_response.DetectDocumentTextResponse:
    import aws_sdk_textract.types.detect_document_text_response

    out: aws_sdk_textract.types.detect_document_text_response.DetectDocumentTextResponse = aws_sdk_textract.types.detect_document_text_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_textract._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_textract._auth._sigv4.build_sigv4_auth_scheme(
                "textract", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_textract._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_textract.types.detect_document_text_request.DetectDocumentTextRequest,
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
    headers["X-Amz-Target"] = "Textract.DetectDocumentText"
    import aws_sdk_textract.types.detect_document_text_request

    body: bytes | None = json.dumps(
        aws_sdk_textract.types.detect_document_text_request.serialize_aws_json_1_1(
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


def detect_document_text(
    options: OperationOptions,
    input: aws_sdk_textract.types.detect_document_text_request.DetectDocumentTextRequest,
) -> tuple[
    aws_sdk_textract.types.detect_document_text_response.DetectDocumentTextResponse,
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


async def async_detect_document_text(
    options: AsyncOperationOptions,
    input: aws_sdk_textract.types.detect_document_text_request.DetectDocumentTextRequest,
) -> tuple[
    aws_sdk_textract.types.detect_document_text_response.DetectDocumentTextResponse,
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
