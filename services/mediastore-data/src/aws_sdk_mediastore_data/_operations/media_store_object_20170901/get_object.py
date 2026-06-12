"""Generated from Smithy shape ``com.amazonaws.mediastoredata#GetObject``."""

from __future__ import annotations

import json
from email.utils import parsedate_to_datetime as _parse_http_date
from typing import TYPE_CHECKING, Any, Never, cast
from urllib.parse import quote

import zapros

import aws_sdk_mediastore_data._auth._signers
import aws_sdk_mediastore_data._auth._sigv4
from aws_sdk_mediastore_data._protocol.errors import parse_error_metadata_json
from aws_sdk_mediastore_data._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_mediastore_data._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_mediastore_data.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_mediastore_data.types.get_object_request
    import aws_sdk_mediastore_data.types.get_object_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ContainerNotFoundException":
            import aws_sdk_mediastore_data.errors.container_not_found_exception

            raise aws_sdk_mediastore_data.errors.container_not_found_exception.ContainerNotFoundException.from_json(
                data
            )
        case "InternalServerError":
            import aws_sdk_mediastore_data.errors.internal_server_error

            raise aws_sdk_mediastore_data.errors.internal_server_error.InternalServerError.from_json(
                data
            )
        case "ObjectNotFoundException":
            import aws_sdk_mediastore_data.errors.object_not_found_exception

            raise aws_sdk_mediastore_data.errors.object_not_found_exception.ObjectNotFoundException.from_json(
                data
            )
        case "RequestedRangeNotSatisfiableException":
            import aws_sdk_mediastore_data.errors.requested_range_not_satisfiable_exception

            raise aws_sdk_mediastore_data.errors.requested_range_not_satisfiable_exception.RequestedRangeNotSatisfiableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_mediastore_data.types.get_object_response.GetObjectResponse:
    _iter = cast(
        Any, response.async_iter_bytes() if is_async else response.iter_bytes()
    )
    out: aws_sdk_mediastore_data.types.get_object_response.GetObjectResponse = {
        "body": _iter
    }
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
) -> aws_sdk_mediastore_data._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_mediastore_data._auth._sigv4.build_sigv4_auth_scheme(
                "mediastore", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_mediastore_data._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_mediastore_data.types.get_object_request.GetObjectRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/{Path+}"
    url = url.replace("{Path+}", quote(str(input["path"]), safe="/"))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "range" in input:
        headers["Range"] = str(input["range"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "GET",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def get_object(
    options: OperationOptions,
    input: aws_sdk_mediastore_data.types.get_object_request.GetObjectRequest,
) -> tuple[
    aws_sdk_mediastore_data.types.get_object_response.GetObjectResponse, zapros.Response
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


async def async_get_object(
    options: AsyncOperationOptions,
    input: aws_sdk_mediastore_data.types.get_object_request.GetObjectRequest,
) -> tuple[
    aws_sdk_mediastore_data.types.get_object_response.GetObjectResponse, zapros.Response
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
