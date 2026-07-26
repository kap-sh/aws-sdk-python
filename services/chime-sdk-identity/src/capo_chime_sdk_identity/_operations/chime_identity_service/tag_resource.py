"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#TagResource``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_chime_sdk_identity._auth._signers
import capo_chime_sdk_identity._auth._sigv4
import capo_chime_sdk_identity.errors.bad_request_exception
import capo_chime_sdk_identity.errors.forbidden_exception
import capo_chime_sdk_identity.errors.resource_limit_exceeded_exception
import capo_chime_sdk_identity.errors.service_failure_exception
import capo_chime_sdk_identity.errors.service_unavailable_exception
import capo_chime_sdk_identity.errors.throttled_client_exception
import capo_chime_sdk_identity.errors.unauthorized_client_exception
import capo_chime_sdk_identity.types.tag_list
import capo_chime_sdk_identity.types.tag_resource_request
from capo_chime_sdk_identity._protocol.errors import parse_error_metadata_json
from capo_chime_sdk_identity._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from capo_chime_sdk_identity._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_chime_sdk_identity.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ForbiddenException":
            raise capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "ResourceLimitExceededException":
            raise capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException.from_json(
                data
            )
        case "ServiceFailureException":
            raise capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "ThrottledClientException":
            raise capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException.from_json(
                data
            )
        case "UnauthorizedClientException":
            raise capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_chime_sdk_identity._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_chime_sdk_identity._auth._sigv4.build_sigv4_auth_scheme(
                "chime", options.region
            )
        )
        if sigv4_config is not None:
            return capo_chime_sdk_identity._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_chime_sdk_identity.types.tag_resource_request.TagResourceRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/tags?operation=tag-resource"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_chime_sdk_identity.types.tag_resource_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def tag_resource(
    options: OperationOptions,
    input_: capo_chime_sdk_identity.types.tag_resource_request.TagResourceRequest,
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


async def async_tag_resource(
    options: AsyncOperationOptions,
    input_: capo_chime_sdk_identity.types.tag_resource_request.TagResourceRequest,
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
