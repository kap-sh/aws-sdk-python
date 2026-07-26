"""Generated from Smithy shape ``com.amazonaws.ebs#PutSnapshotBlock``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_ebs._auth._signers
import capo_ebs._auth._sigv4
import capo_ebs.errors.access_denied_exception
import capo_ebs.errors.internal_server_exception
import capo_ebs.errors.request_throttled_exception
import capo_ebs.errors.resource_not_found_exception
import capo_ebs.errors.service_quota_exceeded_exception
import capo_ebs.errors.validation_exception
import capo_ebs.types.block_data
import capo_ebs.types.checksum_algorithm
import capo_ebs.types.put_snapshot_block_request
import capo_ebs.types.put_snapshot_block_response
from capo_ebs._protocol.errors import parse_error_metadata_json
from capo_ebs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_ebs._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_ebs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_ebs.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise capo_ebs.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "RequestThrottledException":
            raise capo_ebs.errors.request_throttled_exception.RequestThrottledException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_ebs.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceQuotaExceededException":
            raise capo_ebs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException.from_json(
                data
            )
        case "ValidationException":
            raise capo_ebs.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse:
    out: capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse = {}  # type: ignore[typeddict-item]
    if "x-amz-Checksum" in response.headers:
        out["checksum"] = str(response.headers["x-amz-Checksum"])
    if "x-amz-Checksum-Algorithm" in response.headers:
        out["checksum_algorithm"] = capo_ebs.types.checksum_algorithm.deserialize_json(
            response.headers["x-amz-Checksum-Algorithm"]
        )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse:
    out: capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse = {}  # type: ignore[typeddict-item]
    if "x-amz-Checksum" in response.headers:
        out["checksum"] = str(response.headers["x-amz-Checksum"])
    if "x-amz-Checksum-Algorithm" in response.headers:
        out["checksum_algorithm"] = capo_ebs.types.checksum_algorithm.deserialize_json(
            response.headers["x-amz-Checksum-Algorithm"]
        )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_ebs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_ebs._auth._sigv4.build_sigv4_auth_scheme("ebs", options.region)
        )
        if sigv4_config is not None:
            return capo_ebs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ebs.types.put_snapshot_block_request.PutSnapshotBlockRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/snapshots/{SnapshotId}/blocks/{BlockIndex}"
    url = url.replace("{SnapshotId}", quote(str(input_["snapshot_id"]), safe=""))
    url = url.replace("{BlockIndex}", quote(str(input_["block_index"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "data_length" in input_:
        headers["x-amz-Data-Length"] = str(input_["data_length"])
    if "progress" in input_:
        headers["x-amz-Progress"] = str(input_["progress"])
    if "checksum" in input_:
        headers["x-amz-Checksum"] = str(input_["checksum"])
    if "checksum_algorithm" in input_:
        headers["x-amz-Checksum-Algorithm"] = str(input_["checksum_algorithm"])
    body = input_["block_data"]
    if isinstance(body, capo_ebs._iter.StaticAnyIterator):
        body = cast(bytes, body.content)
    if not isinstance(body, bytes) and "content-length" not in [
        header.lower() for header in headers
    ]:
        raise ValueError("Content-Length is required for streaming input")
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def put_snapshot_block(
    options: OperationOptions,
    input_: capo_ebs.types.put_snapshot_block_request.PutSnapshotBlockRequest,
) -> tuple[
    capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse, zapros.Response
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


async def async_put_snapshot_block(
    options: AsyncOperationOptions,
    input_: capo_ebs.types.put_snapshot_block_request.PutSnapshotBlockRequest,
) -> tuple[
    capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse, zapros.Response
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
