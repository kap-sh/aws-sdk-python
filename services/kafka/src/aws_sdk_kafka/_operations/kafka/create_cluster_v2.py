"""Generated from Smithy shape ``com.amazonaws.kafka#CreateClusterV2``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_kafka._auth._signers
import aws_sdk_kafka._auth._sigv4
import aws_sdk_kafka.errors.bad_request_exception
import aws_sdk_kafka.errors.conflict_exception
import aws_sdk_kafka.errors.forbidden_exception
import aws_sdk_kafka.errors.internal_server_error_exception
import aws_sdk_kafka.errors.service_unavailable_exception
import aws_sdk_kafka.errors.too_many_requests_exception
import aws_sdk_kafka.errors.unauthorized_exception
import aws_sdk_kafka.types.__map_of__string
import aws_sdk_kafka.types.cluster_state
import aws_sdk_kafka.types.cluster_type
import aws_sdk_kafka.types.create_cluster_v2_request
import aws_sdk_kafka.types.create_cluster_v2_response
import aws_sdk_kafka.types.provisioned_request
import aws_sdk_kafka.types.serverless_request
from aws_sdk_kafka._protocol.errors import parse_error_metadata_json
from aws_sdk_kafka._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_kafka._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_kafka.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            raise aws_sdk_kafka.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ConflictException":
            raise aws_sdk_kafka.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "ForbiddenException":
            raise aws_sdk_kafka.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "InternalServerErrorException":
            raise aws_sdk_kafka.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise aws_sdk_kafka.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_kafka.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case "UnauthorizedException":
            raise aws_sdk_kafka.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_kafka.types.create_cluster_v2_response.CreateClusterV2Response:
    out: aws_sdk_kafka.types.create_cluster_v2_response.CreateClusterV2Response = (
        aws_sdk_kafka.types.create_cluster_v2_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_kafka.types.create_cluster_v2_response.CreateClusterV2Response:
    out: aws_sdk_kafka.types.create_cluster_v2_response.CreateClusterV2Response = (
        aws_sdk_kafka.types.create_cluster_v2_response.deserialize_json(
            json.loads(await response.aread())
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
    input_: aws_sdk_kafka.types.create_cluster_v2_request.CreateClusterV2Request,
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
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_kafka.types.create_cluster_v2_request

    body: bytes | None = json.dumps(
        aws_sdk_kafka.types.create_cluster_v2_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_cluster_v2(
    options: OperationOptions,
    input_: aws_sdk_kafka.types.create_cluster_v2_request.CreateClusterV2Request,
) -> tuple[
    aws_sdk_kafka.types.create_cluster_v2_response.CreateClusterV2Response,
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


async def async_create_cluster_v2(
    options: AsyncOperationOptions,
    input_: aws_sdk_kafka.types.create_cluster_v2_request.CreateClusterV2Request,
) -> tuple[
    aws_sdk_kafka.types.create_cluster_v2_response.CreateClusterV2Response,
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
