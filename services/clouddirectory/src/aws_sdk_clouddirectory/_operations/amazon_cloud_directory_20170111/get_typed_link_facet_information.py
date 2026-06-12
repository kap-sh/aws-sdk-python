"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetTypedLinkFacetInformation``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_clouddirectory._auth._signers
import aws_sdk_clouddirectory._auth._sigv4
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

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.get_typed_link_facet_information_request
    import aws_sdk_clouddirectory.types.get_typed_link_facet_information_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_clouddirectory.errors.access_denied_exception

            raise aws_sdk_clouddirectory.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "FacetNotFoundException":
            import aws_sdk_clouddirectory.errors.facet_not_found_exception

            raise aws_sdk_clouddirectory.errors.facet_not_found_exception.FacetNotFoundException.from_json(
                data
            )
        case "InternalServiceException":
            import aws_sdk_clouddirectory.errors.internal_service_exception

            raise aws_sdk_clouddirectory.errors.internal_service_exception.InternalServiceException.from_json(
                data
            )
        case "InvalidArnException":
            import aws_sdk_clouddirectory.errors.invalid_arn_exception

            raise aws_sdk_clouddirectory.errors.invalid_arn_exception.InvalidArnException.from_json(
                data
            )
        case "InvalidNextTokenException":
            import aws_sdk_clouddirectory.errors.invalid_next_token_exception

            raise aws_sdk_clouddirectory.errors.invalid_next_token_exception.InvalidNextTokenException.from_json(
                data
            )
        case "LimitExceededException":
            import aws_sdk_clouddirectory.errors.limit_exceeded_exception

            raise aws_sdk_clouddirectory.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_clouddirectory.errors.resource_not_found_exception

            raise aws_sdk_clouddirectory.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "RetryableConflictException":
            import aws_sdk_clouddirectory.errors.retryable_conflict_exception

            raise aws_sdk_clouddirectory.errors.retryable_conflict_exception.RetryableConflictException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_clouddirectory.errors.validation_exception

            raise aws_sdk_clouddirectory.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_clouddirectory.types.get_typed_link_facet_information_response.GetTypedLinkFacetInformationResponse:
    import aws_sdk_clouddirectory.types.get_typed_link_facet_information_response

    out: aws_sdk_clouddirectory.types.get_typed_link_facet_information_response.GetTypedLinkFacetInformationResponse = aws_sdk_clouddirectory.types.get_typed_link_facet_information_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_clouddirectory._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input: aws_sdk_clouddirectory.types.get_typed_link_facet_information_request.GetTypedLinkFacetInformationRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = (
        endpoint.url.rstrip("/")
        + "/amazonclouddirectory/2017-01-11/typedlink/facet/get"
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "schema_arn" in input:
        headers["x-amz-data-partition"] = str(input["schema_arn"])
    import aws_sdk_clouddirectory.types.get_typed_link_facet_information_request

    body: bytes | None = json.dumps(
        aws_sdk_clouddirectory.types.get_typed_link_facet_information_request.serialize_json(
            input
        )
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


def get_typed_link_facet_information(
    options: OperationOptions,
    input: aws_sdk_clouddirectory.types.get_typed_link_facet_information_request.GetTypedLinkFacetInformationRequest,
) -> tuple[
    aws_sdk_clouddirectory.types.get_typed_link_facet_information_response.GetTypedLinkFacetInformationResponse,
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


async def async_get_typed_link_facet_information(
    options: AsyncOperationOptions,
    input: aws_sdk_clouddirectory.types.get_typed_link_facet_information_request.GetTypedLinkFacetInformationRequest,
) -> tuple[
    aws_sdk_clouddirectory.types.get_typed_link_facet_information_response.GetTypedLinkFacetInformationResponse,
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
