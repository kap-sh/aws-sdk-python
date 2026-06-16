"""Generated from Smithy shape ``com.amazonaws.eks#DescribeClusterVersions``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_eks._auth._signers
import aws_sdk_eks._auth._sigv4
from aws_sdk_eks._protocol.errors import parse_error_metadata_json
from aws_sdk_eks._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_eks._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_eks.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_eks.types.describe_cluster_versions_request
    import aws_sdk_eks.types.describe_cluster_versions_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterException":
            import aws_sdk_eks.errors.invalid_parameter_exception

            raise aws_sdk_eks.errors.invalid_parameter_exception.InvalidParameterException.from_json(
                data
            )
        case "InvalidRequestException":
            import aws_sdk_eks.errors.invalid_request_exception

            raise aws_sdk_eks.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "ServerException":
            import aws_sdk_eks.errors.server_exception

            raise aws_sdk_eks.errors.server_exception.ServerException.from_json(data)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> (
    aws_sdk_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse
):
    import aws_sdk_eks.types.describe_cluster_versions_response

    out: aws_sdk_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse = aws_sdk_eks.types.describe_cluster_versions_response.deserialize_json(
        json.loads(response.read())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_eks._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_eks._auth._sigv4.build_sigv4_auth_scheme("eks", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_eks._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_eks.types.describe_cluster_versions_request.DescribeClusterVersionsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/cluster-versions"
    params: dict[str, str] = {}
    if "cluster_type" in input_:
        params["clusterType"] = str(input_["cluster_type"])
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    if "default_only" in input_:
        params["defaultOnly"] = str(input_["default_only"])
    if "include_all" in input_:
        params["includeAll"] = str(input_["include_all"])
    if "cluster_versions" in input_:
        params["clusterVersions"] = str(input_["cluster_versions"])
    if "status" in input_:
        params["status"] = str(input_["status"])
    if "version_status" in input_:
        params["versionStatus"] = str(input_["version_status"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def describe_cluster_versions(
    options: OperationOptions,
    input_: aws_sdk_eks.types.describe_cluster_versions_request.DescribeClusterVersionsRequest,
) -> tuple[
    aws_sdk_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse,
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


async def async_describe_cluster_versions(
    options: AsyncOperationOptions,
    input_: aws_sdk_eks.types.describe_cluster_versions_request.DescribeClusterVersionsRequest,
) -> tuple[
    aws_sdk_eks.types.describe_cluster_versions_response.DescribeClusterVersionsResponse,
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
