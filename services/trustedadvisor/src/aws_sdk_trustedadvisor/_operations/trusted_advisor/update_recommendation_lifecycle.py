"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#UpdateRecommendationLifecycle``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_trustedadvisor._auth._signers
import aws_sdk_trustedadvisor._auth._sigv4
import aws_sdk_trustedadvisor.errors.access_denied_exception
import aws_sdk_trustedadvisor.errors.conflict_exception
import aws_sdk_trustedadvisor.errors.internal_server_exception
import aws_sdk_trustedadvisor.errors.resource_not_found_exception
import aws_sdk_trustedadvisor.errors.throttling_exception
import aws_sdk_trustedadvisor.errors.validation_exception
import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_request
import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage
import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_stage_reason_code
from aws_sdk_trustedadvisor._protocol.errors import parse_error_metadata_json
from aws_sdk_trustedadvisor._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_trustedadvisor._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_trustedadvisor.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_trustedadvisor.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            raise aws_sdk_trustedadvisor.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_trustedadvisor.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_trustedadvisor.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_trustedadvisor.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_trustedadvisor.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_trustedadvisor._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_trustedadvisor._auth._sigv4.build_sigv4_auth_scheme(
                "trustedadvisor", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_trustedadvisor._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_request.UpdateRecommendationLifecycleRequest,
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
        endpoint.url.rstrip("/")
        + "/v1/recommendations/{recommendationIdentifier}/lifecycle"
    )
    url = url.replace(
        "{recommendationIdentifier}",
        quote(str(input_["recommendation_identifier"]), safe=""),
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_request

    body: bytes | None = json.dumps(
        aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def update_recommendation_lifecycle(
    options: OperationOptions,
    input_: aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_request.UpdateRecommendationLifecycleRequest,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_update_recommendation_lifecycle(
    options: AsyncOperationOptions,
    input_: aws_sdk_trustedadvisor.types.update_recommendation_lifecycle_request.UpdateRecommendationLifecycleRequest,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
