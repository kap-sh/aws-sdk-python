"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketAnalyticsConfiguration``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_s3._auth._signers
import capo_s3._auth._sigv4
import capo_s3._protocol.eventstream
import capo_s3.types.analytics_configuration
import capo_s3.types.get_bucket_analytics_configuration_output
import capo_s3.types.get_bucket_analytics_configuration_request
from capo_s3._protocol.errors import parse_error_metadata
from capo_s3._protocol.xml import fromstring
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._rule_engine._endpoint_runtime import apply_label
from capo_s3._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_s3.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_s3.types.get_bucket_analytics_configuration_output.GetBucketAnalyticsConfigurationOutput:
    out: capo_s3.types.get_bucket_analytics_configuration_output.GetBucketAnalyticsConfigurationOutput = {
        "analytics_configuration": capo_s3.types.analytics_configuration.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_s3.types.get_bucket_analytics_configuration_output.GetBucketAnalyticsConfigurationOutput:
    out: capo_s3.types.get_bucket_analytics_configuration_output.GetBucketAnalyticsConfigurationOutput = {
        "analytics_configuration": capo_s3.types.analytics_configuration.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_s3._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_s3._auth._sigv4.build_sigv4_auth_scheme("s3", options.region)
        )
        if sigv4_config is not None:
            return capo_s3._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_s3.types.get_bucket_analytics_configuration_request.GetBucketAnalyticsConfigurationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Bucket=input_.get("bucket"),
            Region=options.region,
            UseFIPS=options.use_fips,
            UseDualStack=options.use_dual_stack,
            Endpoint=options.endpoint,
            ForcePathStyle=options.force_path_style,
            Accelerate=options.accelerate,
            UseGlobalEndpoint=options.use_global_endpoint,
            UseObjectLambdaEndpoint=options.use_object_lambda_endpoint,
            Key=options.key,
            Prefix=options.prefix,
            CopySource=options.copy_source,
            DisableAccessPoints=options.disable_access_points,
            DisableMultiRegionAccessPoints=options.disable_multi_region_access_points,
            UseArnRegion=options.use_arn_region,
            UseS3ExpressControlEndpoint=True,
            DisableS3ExpressSessionAuth=options.disable_s3_express_session_auth,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/{Bucket}?analytics&x-id=GetBucketAnalyticsConfiguration"
    )
    url = apply_label(url, "{Bucket}", str(input_["bucket"]))
    params: dict[str, str] = {}
    if "id" in input_:
        params["id"] = str(input_["id"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "expected_bucket_owner" in input_:
        headers["x-amz-expected-bucket-owner"] = str(input_["expected_bucket_owner"])
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_bucket_analytics_configuration(
    options: OperationOptions,
    input_: capo_s3.types.get_bucket_analytics_configuration_request.GetBucketAnalyticsConfigurationRequest,
) -> tuple[
    capo_s3.types.get_bucket_analytics_configuration_output.GetBucketAnalyticsConfigurationOutput,
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


async def async_get_bucket_analytics_configuration(
    options: AsyncOperationOptions,
    input_: capo_s3.types.get_bucket_analytics_configuration_request.GetBucketAnalyticsConfigurationRequest,
) -> tuple[
    capo_s3.types.get_bucket_analytics_configuration_output.GetBucketAnalyticsConfigurationOutput,
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
