"""Generated from Smithy shape ``com.amazonaws.ivs#BatchStartViewerSessionRevocation``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_ivs._auth._signers
import capo_ivs._auth._sigv4
import capo_ivs.errors.access_denied_exception
import capo_ivs.errors.pending_verification
import capo_ivs.errors.throttling_exception
import capo_ivs.errors.validation_exception
import capo_ivs.types.batch_start_viewer_session_revocation_errors
import capo_ivs.types.batch_start_viewer_session_revocation_request
import capo_ivs.types.batch_start_viewer_session_revocation_response
import capo_ivs.types.batch_start_viewer_session_revocation_viewer_session_list
from capo_ivs._protocol.errors import parse_error_metadata_json
from capo_ivs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_ivs._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_ivs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_ivs.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "PendingVerification":
            raise capo_ivs.errors.pending_verification.PendingVerification.from_json(
                data
            )
        case "ThrottlingException":
            raise capo_ivs.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise capo_ivs.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_ivs.types.batch_start_viewer_session_revocation_response.BatchStartViewerSessionRevocationResponse:
    out: capo_ivs.types.batch_start_viewer_session_revocation_response.BatchStartViewerSessionRevocationResponse = capo_ivs.types.batch_start_viewer_session_revocation_response.deserialize_json(
        json.loads(response.read())
    )
    if "Access-Control-Allow-Origin" in response.headers:
        out["access_control_allow_origin"] = str(
            response.headers["Access-Control-Allow-Origin"]
        )
    if "Access-Control-Expose-Headers" in response.headers:
        out["access_control_expose_headers"] = str(
            response.headers["Access-Control-Expose-Headers"]
        )
    if "Cache-Control" in response.headers:
        out["cache_control"] = str(response.headers["Cache-Control"])
    if "Content-Security-Policy" in response.headers:
        out["content_security_policy"] = str(
            response.headers["Content-Security-Policy"]
        )
    if "Strict-Transport-Security" in response.headers:
        out["strict_transport_security"] = str(
            response.headers["Strict-Transport-Security"]
        )
    if "X-Content-Type-Options" in response.headers:
        out["x_content_type_options"] = str(response.headers["X-Content-Type-Options"])
    if "X-Frame-Options" in response.headers:
        out["x_frame_options"] = str(response.headers["X-Frame-Options"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ivs.types.batch_start_viewer_session_revocation_response.BatchStartViewerSessionRevocationResponse:
    out: capo_ivs.types.batch_start_viewer_session_revocation_response.BatchStartViewerSessionRevocationResponse = capo_ivs.types.batch_start_viewer_session_revocation_response.deserialize_json(
        json.loads(await response.aread())
    )
    if "Access-Control-Allow-Origin" in response.headers:
        out["access_control_allow_origin"] = str(
            response.headers["Access-Control-Allow-Origin"]
        )
    if "Access-Control-Expose-Headers" in response.headers:
        out["access_control_expose_headers"] = str(
            response.headers["Access-Control-Expose-Headers"]
        )
    if "Cache-Control" in response.headers:
        out["cache_control"] = str(response.headers["Cache-Control"])
    if "Content-Security-Policy" in response.headers:
        out["content_security_policy"] = str(
            response.headers["Content-Security-Policy"]
        )
    if "Strict-Transport-Security" in response.headers:
        out["strict_transport_security"] = str(
            response.headers["Strict-Transport-Security"]
        )
    if "X-Content-Type-Options" in response.headers:
        out["x_content_type_options"] = str(response.headers["X-Content-Type-Options"])
    if "X-Frame-Options" in response.headers:
        out["x_frame_options"] = str(response.headers["X-Frame-Options"])
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_ivs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_ivs._auth._sigv4.build_sigv4_auth_scheme("ivs", options.region)
        )
        if sigv4_config is not None:
            return capo_ivs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ivs.types.batch_start_viewer_session_revocation_request.BatchStartViewerSessionRevocationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/BatchStartViewerSessionRevocation"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        capo_ivs.types.batch_start_viewer_session_revocation_request.serialize_json(
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


def batch_start_viewer_session_revocation(
    options: OperationOptions,
    input_: capo_ivs.types.batch_start_viewer_session_revocation_request.BatchStartViewerSessionRevocationRequest,
) -> tuple[
    capo_ivs.types.batch_start_viewer_session_revocation_response.BatchStartViewerSessionRevocationResponse,
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


async def async_batch_start_viewer_session_revocation(
    options: AsyncOperationOptions,
    input_: capo_ivs.types.batch_start_viewer_session_revocation_request.BatchStartViewerSessionRevocationRequest,
) -> tuple[
    capo_ivs.types.batch_start_viewer_session_revocation_response.BatchStartViewerSessionRevocationResponse,
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
