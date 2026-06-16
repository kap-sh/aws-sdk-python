"""Generated from Smithy shape ``com.amazonaws.kafka#ListClustersV2``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_kafka._auth._signers
import aws_sdk_kafka._auth._sigv4
from aws_sdk_kafka._protocol.errors import parse_error_metadata_json
from aws_sdk_kafka._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_kafka._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_kafka.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_kafka.types.list_clusters_v2_request
    import aws_sdk_kafka.types.list_clusters_v2_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            import aws_sdk_kafka.errors.bad_request_exception

            raise aws_sdk_kafka.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ForbiddenException":
            import aws_sdk_kafka.errors.forbidden_exception

            raise aws_sdk_kafka.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "InternalServerErrorException":
            import aws_sdk_kafka.errors.internal_server_error_exception

            raise aws_sdk_kafka.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "UnauthorizedException":
            import aws_sdk_kafka.errors.unauthorized_exception

            raise aws_sdk_kafka.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_kafka.types.list_clusters_v2_response.ListClustersV2Response:
    import aws_sdk_kafka.types.list_clusters_v2_response

    out: aws_sdk_kafka.types.list_clusters_v2_response.ListClustersV2Response = (
        aws_sdk_kafka.types.list_clusters_v2_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_kafka._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_kafka._auth._sigv4.build_sigv4_auth_scheme(
                "kafka", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_kafka._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_kafka.types.list_clusters_v2_request.ListClustersV2Request,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/api/v2/clusters"
    params: dict[str, str] = {}
    if "cluster_name_filter" in input_:
        params["clusterNameFilter"] = str(input_["cluster_name_filter"])
    if "cluster_type_filter" in input_:
        params["clusterTypeFilter"] = str(input_["cluster_type_filter"])
    if "max_results" in input_:
        params["maxResults"] = str(input_["max_results"])
    if "next_token" in input_:
        params["nextToken"] = str(input_["next_token"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_clusters_v2(
    options: OperationOptions,
    input_: aws_sdk_kafka.types.list_clusters_v2_request.ListClustersV2Request,
) -> tuple[
    aws_sdk_kafka.types.list_clusters_v2_response.ListClustersV2Response,
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


async def async_list_clusters_v2(
    options: AsyncOperationOptions,
    input_: aws_sdk_kafka.types.list_clusters_v2_request.ListClustersV2Request,
) -> tuple[
    aws_sdk_kafka.types.list_clusters_v2_response.ListClustersV2Response,
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
