"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateVpcAttachment``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_networkmanager._auth._signers
import aws_sdk_networkmanager._auth._sigv4
import aws_sdk_networkmanager.errors.access_denied_exception
import aws_sdk_networkmanager.errors.conflict_exception
import aws_sdk_networkmanager.errors.internal_server_exception
import aws_sdk_networkmanager.errors.resource_not_found_exception
import aws_sdk_networkmanager.errors.throttling_exception
import aws_sdk_networkmanager.errors.validation_exception
import aws_sdk_networkmanager.types.subnet_arn_list
import aws_sdk_networkmanager.types.update_vpc_attachment_request
import aws_sdk_networkmanager.types.update_vpc_attachment_response
import aws_sdk_networkmanager.types.vpc_attachment
import aws_sdk_networkmanager.types.vpc_options
from aws_sdk_networkmanager._protocol.errors import parse_error_metadata_json
from aws_sdk_networkmanager._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_networkmanager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_networkmanager.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_networkmanager.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            raise aws_sdk_networkmanager.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_networkmanager.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_networkmanager.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_networkmanager.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_networkmanager.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_networkmanager.types.update_vpc_attachment_response.UpdateVpcAttachmentResponse:
    out: aws_sdk_networkmanager.types.update_vpc_attachment_response.UpdateVpcAttachmentResponse = aws_sdk_networkmanager.types.update_vpc_attachment_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_networkmanager.types.update_vpc_attachment_response.UpdateVpcAttachmentResponse:
    out: aws_sdk_networkmanager.types.update_vpc_attachment_response.UpdateVpcAttachmentResponse = aws_sdk_networkmanager.types.update_vpc_attachment_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_networkmanager._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_networkmanager._auth._sigv4.build_sigv4_auth_scheme(
                "networkmanager", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_networkmanager._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_networkmanager.types.update_vpc_attachment_request.UpdateVpcAttachmentRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/vpc-attachments/{AttachmentId}"
    url = url.replace("{AttachmentId}", quote(str(input_["attachment_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_networkmanager.types.update_vpc_attachment_request

    body: bytes | None = json.dumps(
        aws_sdk_networkmanager.types.update_vpc_attachment_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PATCH", headers=headers, body=body, context={"signer": signer}
    )


def update_vpc_attachment(
    options: OperationOptions,
    input_: aws_sdk_networkmanager.types.update_vpc_attachment_request.UpdateVpcAttachmentRequest,
) -> tuple[
    aws_sdk_networkmanager.types.update_vpc_attachment_response.UpdateVpcAttachmentResponse,
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


async def async_update_vpc_attachment(
    options: AsyncOperationOptions,
    input_: aws_sdk_networkmanager.types.update_vpc_attachment_request.UpdateVpcAttachmentRequest,
) -> tuple[
    aws_sdk_networkmanager.types.update_vpc_attachment_response.UpdateVpcAttachmentResponse,
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
