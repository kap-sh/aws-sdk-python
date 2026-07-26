"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateFacet``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_clouddirectory._auth._signers
import capo_clouddirectory._auth._sigv4
import capo_clouddirectory.errors.access_denied_exception
import capo_clouddirectory.errors.facet_not_found_exception
import capo_clouddirectory.errors.facet_validation_exception
import capo_clouddirectory.errors.internal_service_exception
import capo_clouddirectory.errors.invalid_arn_exception
import capo_clouddirectory.errors.invalid_facet_update_exception
import capo_clouddirectory.errors.invalid_rule_exception
import capo_clouddirectory.errors.limit_exceeded_exception
import capo_clouddirectory.errors.resource_not_found_exception
import capo_clouddirectory.errors.retryable_conflict_exception
import capo_clouddirectory.errors.validation_exception
import capo_clouddirectory.types.facet_attribute_update_list
import capo_clouddirectory.types.object_type
import capo_clouddirectory.types.update_facet_request
import capo_clouddirectory.types.update_facet_response
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
        case "FacetNotFoundException":
            raise capo_clouddirectory.errors.facet_not_found_exception.FacetNotFoundException.from_json(
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
        case "InvalidFacetUpdateException":
            raise capo_clouddirectory.errors.invalid_facet_update_exception.InvalidFacetUpdateException.from_json(
                data
            )
        case "InvalidRuleException":
            raise capo_clouddirectory.errors.invalid_rule_exception.InvalidRuleException.from_json(
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
) -> capo_clouddirectory.types.update_facet_response.UpdateFacetResponse:
    out: capo_clouddirectory.types.update_facet_response.UpdateFacetResponse = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_clouddirectory.types.update_facet_response.UpdateFacetResponse:
    out: capo_clouddirectory.types.update_facet_response.UpdateFacetResponse = {}  # type: ignore[typeddict-item]
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
    input_: capo_clouddirectory.types.update_facet_request.UpdateFacetRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/amazonclouddirectory/2017-01-11/facet"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "schema_arn" in input_:
        headers["x-amz-data-partition"] = str(input_["schema_arn"])
    body: bytes | None = json.dumps(
        capo_clouddirectory.types.update_facet_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def update_facet(
    options: OperationOptions,
    input_: capo_clouddirectory.types.update_facet_request.UpdateFacetRequest,
) -> tuple[
    capo_clouddirectory.types.update_facet_response.UpdateFacetResponse, zapros.Response
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


async def async_update_facet(
    options: AsyncOperationOptions,
    input_: capo_clouddirectory.types.update_facet_request.UpdateFacetRequest,
) -> tuple[
    capo_clouddirectory.types.update_facet_response.UpdateFacetResponse, zapros.Response
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
