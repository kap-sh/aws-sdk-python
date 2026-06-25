"""Generated from Smithy shape ``com.amazonaws.s3control#SubmitMultiRegionAccessPointRoutes``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_s3_control._auth._signers
import aws_sdk_s3_control._auth._sigv4
import aws_sdk_s3_control.types.route_list
import aws_sdk_s3_control.types.submit_multi_region_access_point_routes_request
import aws_sdk_s3_control.types.submit_multi_region_access_point_routes_result
from aws_sdk_s3_control._protocol.errors import parse_error_metadata
from aws_sdk_s3_control._protocol.xml import Element, fromstring, tostring
from aws_sdk_s3_control._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3_control._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_s3_control.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_s3_control.types.submit_multi_region_access_point_routes_result.SubmitMultiRegionAccessPointRoutesResult:
    out: aws_sdk_s3_control.types.submit_multi_region_access_point_routes_result.SubmitMultiRegionAccessPointRoutesResult = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_s3_control.types.submit_multi_region_access_point_routes_result.SubmitMultiRegionAccessPointRoutesResult:
    out: aws_sdk_s3_control.types.submit_multi_region_access_point_routes_result.SubmitMultiRegionAccessPointRoutesResult = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_s3_control._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
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
    input_: aws_sdk_s3_control.types.submit_multi_region_access_point_routes_request.SubmitMultiRegionAccessPointRoutesRequest,
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
            UseS3ExpressControlEndpoint=options.use_s3_express_control_endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v20180820/mrap/instances/{Mrap+}/routes"
    url = url.replace("{Mrap+}", quote(str(input_["mrap"]), safe="/"))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "account_id" in input_:
        headers["x-amz-account-id"] = str(input_["account_id"])
    root = Element("SubmitMultiRegionAccessPointRoutesRequest")
    if "route_updates" in input_:
        aws_sdk_s3_control.types.route_list.serialize_xml(
            input_["route_updates"], root, "RouteUpdates"
        )
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PATCH", headers=headers, body=body, context={"signer": signer}
    )


def submit_multi_region_access_point_routes(
    options: OperationOptions,
    input_: aws_sdk_s3_control.types.submit_multi_region_access_point_routes_request.SubmitMultiRegionAccessPointRoutesRequest,
) -> tuple[
    aws_sdk_s3_control.types.submit_multi_region_access_point_routes_result.SubmitMultiRegionAccessPointRoutesResult,
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


async def async_submit_multi_region_access_point_routes(
    options: AsyncOperationOptions,
    input_: aws_sdk_s3_control.types.submit_multi_region_access_point_routes_request.SubmitMultiRegionAccessPointRoutesRequest,
) -> tuple[
    aws_sdk_s3_control.types.submit_multi_region_access_point_routes_result.SubmitMultiRegionAccessPointRoutesResult,
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
