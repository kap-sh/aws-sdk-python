"""Generated from Smithy shape ``com.amazonaws.s3control#ListAccessPointsForDirectoryBuckets``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_s3_control._auth._signers
import aws_sdk_s3_control._auth._sigv4
from aws_sdk_s3_control._protocol.errors import parse_error_metadata
from aws_sdk_s3_control._protocol.xml import fromstring
from aws_sdk_s3_control._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3_control._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_s3_control.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.list_access_points_for_directory_buckets_request
    import aws_sdk_s3_control.types.list_access_points_for_directory_buckets_result


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_s3_control.types.list_access_points_for_directory_buckets_result.ListAccessPointsForDirectoryBucketsResult:
    import aws_sdk_s3_control.types.list_access_points_for_directory_buckets_result

    out: aws_sdk_s3_control.types.list_access_points_for_directory_buckets_result.ListAccessPointsForDirectoryBucketsResult = aws_sdk_s3_control.types.list_access_points_for_directory_buckets_result.deserialize_xml(
        fromstring(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_s3_control._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_s3_control._auth._sigv4.build_sigv4_auth_scheme(
                "s3", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_s3_control._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_s3_control.types.list_access_points_for_directory_buckets_request.ListAccessPointsForDirectoryBucketsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            AccountId=input_.get("account_id"),
            RequiresAccountId=True,
            OutpostId=options.outpost_id,
            Bucket=options.bucket,
            AccessPointName=options.access_point_name,
            UseArnRegion=options.use_arn_region,
            ResourceArn=options.resource_arn,
            UseS3ExpressControlEndpoint=True,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v20180820/accesspointfordirectory"
    params: dict[str, str] = {}
    if "directory_bucket" in input_:
        params["directoryBucket"] = str(input_["directory_bucket"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    params["maxResults"] = str(input_.get("max_results", 0))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "account_id" in input_:
        headers["x-amz-account-id"] = str(input_["account_id"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_access_points_for_directory_buckets(
    options: OperationOptions,
    input_: aws_sdk_s3_control.types.list_access_points_for_directory_buckets_request.ListAccessPointsForDirectoryBucketsRequest,
) -> tuple[
    aws_sdk_s3_control.types.list_access_points_for_directory_buckets_result.ListAccessPointsForDirectoryBucketsResult,
    zapros.Response,
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


async def async_list_access_points_for_directory_buckets(
    options: AsyncOperationOptions,
    input_: aws_sdk_s3_control.types.list_access_points_for_directory_buckets_request.ListAccessPointsForDirectoryBucketsRequest,
) -> tuple[
    aws_sdk_s3_control.types.list_access_points_for_directory_buckets_result.ListAccessPointsForDirectoryBucketsResult,
    zapros.Response,
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
