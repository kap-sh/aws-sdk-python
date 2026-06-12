"""Generated from Smithy shape ``com.amazonaws.efs#DescribeAccessPoints``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_efs._auth._signers
import aws_sdk_efs._auth._sigv4
from aws_sdk_efs._protocol.errors import parse_error_metadata_json
from aws_sdk_efs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_efs._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_efs.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_efs.types.describe_access_points_request
    import aws_sdk_efs.types.describe_access_points_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessPointNotFound":
            import aws_sdk_efs.errors.access_point_not_found

            raise aws_sdk_efs.errors.access_point_not_found.AccessPointNotFound.from_json(
                data
            )
        case "BadRequest":
            import aws_sdk_efs.errors.bad_request

            raise aws_sdk_efs.errors.bad_request.BadRequest.from_json(data)
        case "FileSystemNotFound":
            import aws_sdk_efs.errors.file_system_not_found

            raise aws_sdk_efs.errors.file_system_not_found.FileSystemNotFound.from_json(
                data
            )
        case "InternalServerError":
            import aws_sdk_efs.errors.internal_server_error

            raise aws_sdk_efs.errors.internal_server_error.InternalServerError.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_efs.types.describe_access_points_response.DescribeAccessPointsResponse:
    import aws_sdk_efs.types.describe_access_points_response

    out: aws_sdk_efs.types.describe_access_points_response.DescribeAccessPointsResponse = aws_sdk_efs.types.describe_access_points_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_efs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_efs._auth._sigv4.build_sigv4_auth_scheme(
                "elasticfilesystem", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_efs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_efs.types.describe_access_points_request.DescribeAccessPointsRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = endpoint.url.rstrip("/") + "/2015-02-01/access-points"
    params: dict[str, str] = {}
    if "max_results" in input:
        params["MaxResults"] = str(input["max_results"])
    if "next_token" in input:
        params["NextToken"] = str(input["next_token"])
    if "access_point_id" in input:
        params["AccessPointId"] = str(input["access_point_id"])
    if "file_system_id" in input:
        params["FileSystemId"] = str(input["file_system_id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
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


def describe_access_points(
    options: OperationOptions,
    input: aws_sdk_efs.types.describe_access_points_request.DescribeAccessPointsRequest,
) -> tuple[
    aws_sdk_efs.types.describe_access_points_response.DescribeAccessPointsResponse,
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


async def async_describe_access_points(
    options: AsyncOperationOptions,
    input: aws_sdk_efs.types.describe_access_points_request.DescribeAccessPointsRequest,
) -> tuple[
    aws_sdk_efs.types.describe_access_points_response.DescribeAccessPointsResponse,
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
