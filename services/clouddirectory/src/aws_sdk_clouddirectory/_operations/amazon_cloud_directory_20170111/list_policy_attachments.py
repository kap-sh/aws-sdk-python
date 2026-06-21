"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListPolicyAttachments``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_clouddirectory._auth._signers
import aws_sdk_clouddirectory._auth._sigv4
import aws_sdk_clouddirectory.errors.access_denied_exception
import aws_sdk_clouddirectory.errors.directory_not_enabled_exception
import aws_sdk_clouddirectory.errors.internal_service_exception
import aws_sdk_clouddirectory.errors.invalid_arn_exception
import aws_sdk_clouddirectory.errors.invalid_next_token_exception
import aws_sdk_clouddirectory.errors.limit_exceeded_exception
import aws_sdk_clouddirectory.errors.not_policy_exception
import aws_sdk_clouddirectory.errors.resource_not_found_exception
import aws_sdk_clouddirectory.errors.retryable_conflict_exception
import aws_sdk_clouddirectory.errors.validation_exception
import aws_sdk_clouddirectory.types.consistency_level
import aws_sdk_clouddirectory.types.list_policy_attachments_request
import aws_sdk_clouddirectory.types.list_policy_attachments_response
import aws_sdk_clouddirectory.types.object_identifier_list
import aws_sdk_clouddirectory.types.object_reference
from aws_sdk_clouddirectory._protocol.errors import parse_error_metadata_json
from aws_sdk_clouddirectory._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_clouddirectory._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_clouddirectory.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_clouddirectory.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "DirectoryNotEnabledException":
            raise aws_sdk_clouddirectory.errors.directory_not_enabled_exception.DirectoryNotEnabledException.from_json(
                data
            )
        case "InternalServiceException":
            raise aws_sdk_clouddirectory.errors.internal_service_exception.InternalServiceException.from_json(
                data
            )
        case "InvalidArnException":
            raise aws_sdk_clouddirectory.errors.invalid_arn_exception.InvalidArnException.from_json(
                data
            )
        case "InvalidNextTokenException":
            raise aws_sdk_clouddirectory.errors.invalid_next_token_exception.InvalidNextTokenException.from_json(
                data
            )
        case "LimitExceededException":
            raise aws_sdk_clouddirectory.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "NotPolicyException":
            raise aws_sdk_clouddirectory.errors.not_policy_exception.NotPolicyException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_clouddirectory.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "RetryableConflictException":
            raise aws_sdk_clouddirectory.errors.retryable_conflict_exception.RetryableConflictException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_clouddirectory.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_clouddirectory.types.list_policy_attachments_response.ListPolicyAttachmentsResponse:
    out: aws_sdk_clouddirectory.types.list_policy_attachments_response.ListPolicyAttachmentsResponse = aws_sdk_clouddirectory.types.list_policy_attachments_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_clouddirectory.types.list_policy_attachments_response.ListPolicyAttachmentsResponse:
    out: aws_sdk_clouddirectory.types.list_policy_attachments_response.ListPolicyAttachmentsResponse = aws_sdk_clouddirectory.types.list_policy_attachments_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_clouddirectory._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_clouddirectory._auth._sigv4.build_sigv4_auth_scheme(
                "clouddirectory", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_clouddirectory._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_clouddirectory.types.list_policy_attachments_request.ListPolicyAttachmentsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/") + "/amazonclouddirectory/2017-01-11/policy/attachment"
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "directory_arn" in input_:
        headers["x-amz-data-partition"] = str(input_["directory_arn"])
    if "consistency_level" in input_:
        headers["x-amz-consistency-level"] = str(input_["consistency_level"])
    import aws_sdk_clouddirectory.types.list_policy_attachments_request

    body: bytes | None = json.dumps(
        aws_sdk_clouddirectory.types.list_policy_attachments_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_policy_attachments(
    options: OperationOptions,
    input_: aws_sdk_clouddirectory.types.list_policy_attachments_request.ListPolicyAttachmentsRequest,
) -> tuple[
    aws_sdk_clouddirectory.types.list_policy_attachments_response.ListPolicyAttachmentsResponse,
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


async def async_list_policy_attachments(
    options: AsyncOperationOptions,
    input_: aws_sdk_clouddirectory.types.list_policy_attachments_request.ListPolicyAttachmentsRequest,
) -> tuple[
    aws_sdk_clouddirectory.types.list_policy_attachments_response.ListPolicyAttachmentsResponse,
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
