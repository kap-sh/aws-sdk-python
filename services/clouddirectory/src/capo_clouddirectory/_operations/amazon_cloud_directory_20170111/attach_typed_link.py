"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttachTypedLink``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_clouddirectory._auth._signers
import capo_clouddirectory._auth._sigv4
import capo_clouddirectory.errors.access_denied_exception
import capo_clouddirectory.errors.directory_not_enabled_exception
import capo_clouddirectory.errors.facet_validation_exception
import capo_clouddirectory.errors.internal_service_exception
import capo_clouddirectory.errors.invalid_arn_exception
import capo_clouddirectory.errors.invalid_attachment_exception
import capo_clouddirectory.errors.limit_exceeded_exception
import capo_clouddirectory.errors.resource_not_found_exception
import capo_clouddirectory.errors.retryable_conflict_exception
import capo_clouddirectory.errors.validation_exception
import capo_clouddirectory.types.attach_typed_link_request
import capo_clouddirectory.types.attach_typed_link_response
import capo_clouddirectory.types.attribute_name_and_value_list
import capo_clouddirectory.types.object_reference
import capo_clouddirectory.types.typed_link_schema_and_facet_name
import capo_clouddirectory.types.typed_link_specifier
from capo_clouddirectory._protocol.errors import parse_error_metadata_json
from capo_clouddirectory._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_clouddirectory._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_clouddirectory.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_clouddirectory.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "DirectoryNotEnabledException":
            raise capo_clouddirectory.errors.directory_not_enabled_exception.DirectoryNotEnabledException.from_json(
                data
            )
        case "FacetValidationException":
            raise capo_clouddirectory.errors.facet_validation_exception.FacetValidationException.from_json(
                data
            )
        case "InternalServiceException":
            raise capo_clouddirectory.errors.internal_service_exception.InternalServiceException.from_json(
                data
            )
        case "InvalidArnException":
            raise capo_clouddirectory.errors.invalid_arn_exception.InvalidArnException.from_json(
                data
            )
        case "InvalidAttachmentException":
            raise capo_clouddirectory.errors.invalid_attachment_exception.InvalidAttachmentException.from_json(
                data
            )
        case "LimitExceededException":
            raise capo_clouddirectory.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_clouddirectory.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "RetryableConflictException":
            raise capo_clouddirectory.errors.retryable_conflict_exception.RetryableConflictException.from_json(
                data
            )
        case "ValidationException":
            raise capo_clouddirectory.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_clouddirectory.types.attach_typed_link_response.AttachTypedLinkResponse:
    out: capo_clouddirectory.types.attach_typed_link_response.AttachTypedLinkResponse = capo_clouddirectory.types.attach_typed_link_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_clouddirectory.types.attach_typed_link_response.AttachTypedLinkResponse:
    out: capo_clouddirectory.types.attach_typed_link_response.AttachTypedLinkResponse = capo_clouddirectory.types.attach_typed_link_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_clouddirectory._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_clouddirectory._auth._sigv4.build_sigv4_auth_scheme(
                "clouddirectory", options.region
            )
        )
        if sigv4_config is not None:
            return capo_clouddirectory._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_clouddirectory.types.attach_typed_link_request.AttachTypedLinkRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/amazonclouddirectory/2017-01-11/typedlink/attach"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "directory_arn" in input_:
        headers["x-amz-data-partition"] = str(input_["directory_arn"])
    body: bytes | None = json.dumps(
        capo_clouddirectory.types.attach_typed_link_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def attach_typed_link(
    options: OperationOptions,
    input_: capo_clouddirectory.types.attach_typed_link_request.AttachTypedLinkRequest,
) -> tuple[
    capo_clouddirectory.types.attach_typed_link_response.AttachTypedLinkResponse,
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


async def async_attach_typed_link(
    options: AsyncOperationOptions,
    input_: capo_clouddirectory.types.attach_typed_link_request.AttachTypedLinkRequest,
) -> tuple[
    capo_clouddirectory.types.attach_typed_link_response.AttachTypedLinkResponse,
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
