"""Generated from Smithy shape ``com.amazonaws.fsx#CreateAndAttachS3AccessPoint``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_fsx._auth._signers
import capo_fsx._auth._sigv4
import capo_fsx.errors.access_point_already_owned_by_you
import capo_fsx.errors.bad_request
import capo_fsx.errors.incompatible_parameter_error
import capo_fsx.errors.internal_server_error
import capo_fsx.errors.invalid_access_point
import capo_fsx.errors.invalid_request
import capo_fsx.errors.too_many_access_points
import capo_fsx.errors.unsupported_operation
import capo_fsx.errors.volume_not_found
import capo_fsx.types.create_and_attach_s3_access_point_ontap_configuration
import capo_fsx.types.create_and_attach_s3_access_point_open_zfs_configuration
import capo_fsx.types.create_and_attach_s3_access_point_request
import capo_fsx.types.create_and_attach_s3_access_point_response
import capo_fsx.types.create_and_attach_s3_access_point_s3_configuration
import capo_fsx.types.s3_access_point_attachment
import capo_fsx.types.s3_access_point_attachment_type
from capo_fsx._protocol.errors import parse_error_metadata_json
from capo_fsx._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_fsx._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_fsx.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessPointAlreadyOwnedByYou":
            raise capo_fsx.errors.access_point_already_owned_by_you.AccessPointAlreadyOwnedByYou.from_aws_json_1_1(
                data
            )
        case "BadRequest":
            raise capo_fsx.errors.bad_request.BadRequest.from_aws_json_1_1(data)
        case "IncompatibleParameterError":
            raise capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError.from_aws_json_1_1(
                data
            )
        case "InternalServerError":
            raise capo_fsx.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case "InvalidAccessPoint":
            raise capo_fsx.errors.invalid_access_point.InvalidAccessPoint.from_aws_json_1_1(
                data
            )
        case "InvalidRequest":
            raise capo_fsx.errors.invalid_request.InvalidRequest.from_aws_json_1_1(data)
        case "TooManyAccessPoints":
            raise capo_fsx.errors.too_many_access_points.TooManyAccessPoints.from_aws_json_1_1(
                data
            )
        case "UnsupportedOperation":
            raise capo_fsx.errors.unsupported_operation.UnsupportedOperation.from_aws_json_1_1(
                data
            )
        case "VolumeNotFound":
            raise capo_fsx.errors.volume_not_found.VolumeNotFound.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_fsx.types.create_and_attach_s3_access_point_response.CreateAndAttachS3AccessPointResponse:
    out: capo_fsx.types.create_and_attach_s3_access_point_response.CreateAndAttachS3AccessPointResponse = capo_fsx.types.create_and_attach_s3_access_point_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_fsx.types.create_and_attach_s3_access_point_response.CreateAndAttachS3AccessPointResponse:
    out: capo_fsx.types.create_and_attach_s3_access_point_response.CreateAndAttachS3AccessPointResponse = capo_fsx.types.create_and_attach_s3_access_point_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_fsx._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_fsx._auth._sigv4.build_sigv4_auth_scheme("fsx", options.region)
        )
        if sigv4_config is not None:
            return capo_fsx._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_fsx.types.create_and_attach_s3_access_point_request.CreateAndAttachS3AccessPointRequest,
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
    headers["X-Amz-Target"] = (
        "AWSSimbaAPIService_v20180301.CreateAndAttachS3AccessPoint"
    )
    body: bytes | None = json.dumps(
        capo_fsx.types.create_and_attach_s3_access_point_request.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_and_attach_s3_access_point(
    options: OperationOptions,
    input_: capo_fsx.types.create_and_attach_s3_access_point_request.CreateAndAttachS3AccessPointRequest,
) -> tuple[
    capo_fsx.types.create_and_attach_s3_access_point_response.CreateAndAttachS3AccessPointResponse,
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


async def async_create_and_attach_s3_access_point(
    options: AsyncOperationOptions,
    input_: capo_fsx.types.create_and_attach_s3_access_point_request.CreateAndAttachS3AccessPointRequest,
) -> tuple[
    capo_fsx.types.create_and_attach_s3_access_point_response.CreateAndAttachS3AccessPointResponse,
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
