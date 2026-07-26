"""Generated from Smithy shape ``com.amazonaws.mediastoredata#GetObject``."""

from __future__ import annotations

import json
from email.utils import parsedate_to_datetime as _parse_http_date
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_mediastore_data._auth._signers
import capo_mediastore_data._auth._sigv4
import capo_mediastore_data.errors.container_not_found_exception
import capo_mediastore_data.errors.internal_server_error
import capo_mediastore_data.errors.object_not_found_exception
import capo_mediastore_data.errors.requested_range_not_satisfiable_exception
import capo_mediastore_data.types.get_object_request
import capo_mediastore_data.types.get_object_response
import capo_mediastore_data.types.payload_blob
import capo_mediastore_data.types.time_stamp
from capo_mediastore_data._protocol.errors import parse_error_metadata_json
from capo_mediastore_data._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_mediastore_data._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from capo_mediastore_data.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ContainerNotFoundException":
            raise capo_mediastore_data.errors.container_not_found_exception.ContainerNotFoundException.from_json(
                data
            )
        case "InternalServerError":
            raise capo_mediastore_data.errors.internal_server_error.InternalServerError.from_json(
                data
            )
        case "ObjectNotFoundException":
            raise capo_mediastore_data.errors.object_not_found_exception.ObjectNotFoundException.from_json(
                data
            )
        case "RequestedRangeNotSatisfiableException":
            raise capo_mediastore_data.errors.requested_range_not_satisfiable_exception.RequestedRangeNotSatisfiableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_mediastore_data.types.get_object_response.GetObjectResponse:
    _iter = cast(Any, response.iter_bytes())
    out: capo_mediastore_data.types.get_object_response.GetObjectResponse = {
        "body": _iter
    }  # type: ignore[reportAssignmentType]
    if "Cache-Control" in response.headers:
        out["cache_control"] = str(response.headers["Cache-Control"])
    if "Content-Range" in response.headers:
        out["content_range"] = str(response.headers["Content-Range"])
    if "Content-Length" in response.headers:
        out["content_length"] = int(response.headers["Content-Length"])
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
    if "Last-Modified" in response.headers:
        out["last_modified"] = _parse_http_date(response.headers["Last-Modified"])
    out["status_code"] = response.status
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_mediastore_data.types.get_object_response.GetObjectResponse:
    _iter = cast(Any, response.async_iter_bytes())
    out: capo_mediastore_data.types.get_object_response.GetObjectResponse = {
        "body": _iter
    }  # type: ignore[reportAssignmentType]
    if "Cache-Control" in response.headers:
        out["cache_control"] = str(response.headers["Cache-Control"])
    if "Content-Range" in response.headers:
        out["content_range"] = str(response.headers["Content-Range"])
    if "Content-Length" in response.headers:
        out["content_length"] = int(response.headers["Content-Length"])
    if "Content-Type" in response.headers:
        out["content_type"] = str(response.headers["Content-Type"])
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
    if "Last-Modified" in response.headers:
        out["last_modified"] = _parse_http_date(response.headers["Last-Modified"])
    out["status_code"] = response.status
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_mediastore_data._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_mediastore_data._auth._sigv4.build_sigv4_auth_scheme(
                "mediastore", options.region
            )
        )
        if sigv4_config is not None:
            return capo_mediastore_data._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_mediastore_data.types.get_object_request.GetObjectRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/{Path+}"
    url = url.replace("{Path+}", quote(str(input_["path"]), safe="/"))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "range" in input_:
        headers["Range"] = str(input_["range"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_object(
    options: OperationOptions,
    input_: capo_mediastore_data.types.get_object_request.GetObjectRequest,
) -> tuple[
    capo_mediastore_data.types.get_object_response.GetObjectResponse, zapros.Response
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


async def async_get_object(
    options: AsyncOperationOptions,
    input_: capo_mediastore_data.types.get_object_request.GetObjectRequest,
) -> tuple[
    capo_mediastore_data.types.get_object_response.GetObjectResponse, zapros.Response
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
