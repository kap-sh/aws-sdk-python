"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteTopic``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_kafka._auth._signers
import aws_sdk_kafka._auth._sigv4
import aws_sdk_kafka.errors.bad_request_exception
import aws_sdk_kafka.errors.cluster_connectivity_exception
import aws_sdk_kafka.errors.controller_moved_exception
import aws_sdk_kafka.errors.forbidden_exception
import aws_sdk_kafka.errors.group_subscribed_to_topic_exception
import aws_sdk_kafka.errors.internal_server_error_exception
import aws_sdk_kafka.errors.kafka_request_exception
import aws_sdk_kafka.errors.kafka_timeout_exception
import aws_sdk_kafka.errors.not_controller_exception
import aws_sdk_kafka.errors.not_found_exception
import aws_sdk_kafka.errors.reassignment_in_progress_exception
import aws_sdk_kafka.errors.unknown_topic_or_partition_exception
import aws_sdk_kafka.types.delete_topic_request
import aws_sdk_kafka.types.delete_topic_response
import aws_sdk_kafka.types.topic_state
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
        case "ClusterConnectivityException":
            raise aws_sdk_kafka.errors.cluster_connectivity_exception.ClusterConnectivityException.from_json(
                data
            )
        case "ControllerMovedException":
            raise aws_sdk_kafka.errors.controller_moved_exception.ControllerMovedException.from_json(
                data
            )
        case "ForbiddenException":
            raise aws_sdk_kafka.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "GroupSubscribedToTopicException":
            raise aws_sdk_kafka.errors.group_subscribed_to_topic_exception.GroupSubscribedToTopicException.from_json(
                data
            )
        case "InternalServerErrorException":
            raise aws_sdk_kafka.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "KafkaRequestException":
            raise aws_sdk_kafka.errors.kafka_request_exception.KafkaRequestException.from_json(
                data
            )
        case "KafkaTimeoutException":
            raise aws_sdk_kafka.errors.kafka_timeout_exception.KafkaTimeoutException.from_json(
                data
            )
        case "NotControllerException":
            raise aws_sdk_kafka.errors.not_controller_exception.NotControllerException.from_json(
                data
            )
        case "NotFoundException":
            raise aws_sdk_kafka.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "ReassignmentInProgressException":
            raise aws_sdk_kafka.errors.reassignment_in_progress_exception.ReassignmentInProgressException.from_json(
                data
            )
        case "UnknownTopicOrPartitionException":
            raise aws_sdk_kafka.errors.unknown_topic_or_partition_exception.UnknownTopicOrPartitionException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_kafka.types.delete_topic_response.DeleteTopicResponse:
    out: aws_sdk_kafka.types.delete_topic_response.DeleteTopicResponse = (
        aws_sdk_kafka.types.delete_topic_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_kafka.types.delete_topic_response.DeleteTopicResponse:
    out: aws_sdk_kafka.types.delete_topic_response.DeleteTopicResponse = (
        aws_sdk_kafka.types.delete_topic_response.deserialize_json(
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
    input_: aws_sdk_kafka.types.delete_topic_request.DeleteTopicRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/v1/clusters/{ClusterArn}/topics/{TopicName}"
    url = url.replace("{ClusterArn}", quote(str(input_["cluster_arn"]), safe=""))
    url = url.replace("{TopicName}", quote(str(input_["topic_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def delete_topic(
    options: OperationOptions,
    input_: aws_sdk_kafka.types.delete_topic_request.DeleteTopicRequest,
) -> tuple[
    aws_sdk_kafka.types.delete_topic_response.DeleteTopicResponse, zapros.Response
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


async def async_delete_topic(
    options: AsyncOperationOptions,
    input_: aws_sdk_kafka.types.delete_topic_request.DeleteTopicRequest,
) -> tuple[
    aws_sdk_kafka.types.delete_topic_response.DeleteTopicResponse, zapros.Response
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
