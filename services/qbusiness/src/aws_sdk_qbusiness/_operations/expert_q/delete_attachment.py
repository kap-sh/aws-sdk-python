"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteAttachment``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_qbusiness._auth._signers
import aws_sdk_qbusiness._auth._sigv4
import aws_sdk_qbusiness.errors.access_denied_exception
import aws_sdk_qbusiness.errors.internal_server_exception
import aws_sdk_qbusiness.errors.license_not_found_exception
import aws_sdk_qbusiness.errors.resource_not_found_exception
import aws_sdk_qbusiness.errors.throttling_exception
import aws_sdk_qbusiness.errors.validation_exception
import aws_sdk_qbusiness.types.delete_attachment_request
import aws_sdk_qbusiness.types.delete_attachment_response
from aws_sdk_qbusiness._protocol.errors import parse_error_metadata_json
from aws_sdk_qbusiness._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_qbusiness._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_qbusiness.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_qbusiness.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_qbusiness.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "LicenseNotFoundException":
            raise aws_sdk_qbusiness.errors.license_not_found_exception.LicenseNotFoundException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_qbusiness.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_qbusiness.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_qbusiness.types.delete_attachment_response.DeleteAttachmentResponse:
    out: aws_sdk_qbusiness.types.delete_attachment_response.DeleteAttachmentResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_qbusiness.types.delete_attachment_response.DeleteAttachmentResponse:
    out: aws_sdk_qbusiness.types.delete_attachment_response.DeleteAttachmentResponse = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_qbusiness._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_qbusiness._auth._sigv4.build_sigv4_auth_scheme(
                "qbusiness", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_qbusiness._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_qbusiness.types.delete_attachment_request.DeleteAttachmentRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region, UseFIPS=options.use_fips, Endpoint=options.endpoint
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/applications/{applicationId}/conversations/{conversationId}/attachments/{attachmentId}"
    )
    url = url.replace("{applicationId}", quote(str(input_["application_id"]), safe=""))
    url = url.replace(
        "{conversationId}", quote(str(input_["conversation_id"]), safe="")
    )
    url = url.replace("{attachmentId}", quote(str(input_["attachment_id"]), safe=""))
    params: dict[str, str] = {}
    if "user_id" in input_:
        params["userId"] = str(input_["user_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_attachment(
    options: OperationOptions,
    input_: aws_sdk_qbusiness.types.delete_attachment_request.DeleteAttachmentRequest,
) -> tuple[
    aws_sdk_qbusiness.types.delete_attachment_response.DeleteAttachmentResponse,
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


async def async_delete_attachment(
    options: AsyncOperationOptions,
    input_: aws_sdk_qbusiness.types.delete_attachment_request.DeleteAttachmentRequest,
) -> tuple[
    aws_sdk_qbusiness.types.delete_attachment_response.DeleteAttachmentResponse,
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
