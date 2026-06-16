"""Generated from Smithy shape ``com.amazonaws.fsx#CreateSnapshot``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_fsx._auth._signers
import aws_sdk_fsx._auth._sigv4
from aws_sdk_fsx._protocol.errors import parse_error_metadata_json
from aws_sdk_fsx._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_fsx._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_fsx.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.create_snapshot_request
    import aws_sdk_fsx.types.create_snapshot_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequest":
            import aws_sdk_fsx.errors.bad_request

            raise aws_sdk_fsx.errors.bad_request.BadRequest.from_aws_json_1_1(data)
        case "InternalServerError":
            import aws_sdk_fsx.errors.internal_server_error

            raise aws_sdk_fsx.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case "ServiceLimitExceeded":
            import aws_sdk_fsx.errors.service_limit_exceeded

            raise aws_sdk_fsx.errors.service_limit_exceeded.ServiceLimitExceeded.from_aws_json_1_1(
                data
            )
        case "VolumeNotFound":
            import aws_sdk_fsx.errors.volume_not_found

            raise aws_sdk_fsx.errors.volume_not_found.VolumeNotFound.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_fsx.types.create_snapshot_response.CreateSnapshotResponse:
    import aws_sdk_fsx.types.create_snapshot_response

    out: aws_sdk_fsx.types.create_snapshot_response.CreateSnapshotResponse = (
        aws_sdk_fsx.types.create_snapshot_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_fsx._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_fsx._auth._sigv4.build_sigv4_auth_scheme("fsx", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_fsx._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_fsx.types.create_snapshot_request.CreateSnapshotRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSSimbaAPIService_v20180301.CreateSnapshot"
    import aws_sdk_fsx.types.create_snapshot_request

    body: bytes | None = json.dumps(
        aws_sdk_fsx.types.create_snapshot_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_snapshot(
    options: OperationOptions,
    input_: aws_sdk_fsx.types.create_snapshot_request.CreateSnapshotRequest,
) -> tuple[
    aws_sdk_fsx.types.create_snapshot_response.CreateSnapshotResponse, zapros.Response
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_create_snapshot(
    options: AsyncOperationOptions,
    input_: aws_sdk_fsx.types.create_snapshot_request.CreateSnapshotRequest,
) -> tuple[
    aws_sdk_fsx.types.create_snapshot_response.CreateSnapshotResponse, zapros.Response
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
