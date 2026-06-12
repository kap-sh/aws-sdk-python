"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateTopic``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_kafka._auth._signers
import aws_sdk_kafka._auth._sigv4
from aws_sdk_kafka._protocol.errors import parse_error_metadata_json
from aws_sdk_kafka._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_kafka._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_kafka.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_kafka.types.update_topic_request
    import aws_sdk_kafka.types.update_topic_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            import aws_sdk_kafka.errors.bad_request_exception

            raise aws_sdk_kafka.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ClusterConnectivityException":
            import aws_sdk_kafka.errors.cluster_connectivity_exception

            raise aws_sdk_kafka.errors.cluster_connectivity_exception.ClusterConnectivityException.from_json(
                data
            )
        case "ControllerMovedException":
            import aws_sdk_kafka.errors.controller_moved_exception

            raise aws_sdk_kafka.errors.controller_moved_exception.ControllerMovedException.from_json(
                data
            )
        case "ForbiddenException":
            import aws_sdk_kafka.errors.forbidden_exception

            raise aws_sdk_kafka.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "GroupSubscribedToTopicException":
            import aws_sdk_kafka.errors.group_subscribed_to_topic_exception

            raise aws_sdk_kafka.errors.group_subscribed_to_topic_exception.GroupSubscribedToTopicException.from_json(
                data
            )
        case "InternalServerErrorException":
            import aws_sdk_kafka.errors.internal_server_error_exception

            raise aws_sdk_kafka.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "KafkaRequestException":
            import aws_sdk_kafka.errors.kafka_request_exception

            raise aws_sdk_kafka.errors.kafka_request_exception.KafkaRequestException.from_json(
                data
            )
        case "KafkaTimeoutException":
            import aws_sdk_kafka.errors.kafka_timeout_exception

            raise aws_sdk_kafka.errors.kafka_timeout_exception.KafkaTimeoutException.from_json(
                data
            )
        case "NotControllerException":
            import aws_sdk_kafka.errors.not_controller_exception

            raise aws_sdk_kafka.errors.not_controller_exception.NotControllerException.from_json(
                data
            )
        case "NotFoundException":
            import aws_sdk_kafka.errors.not_found_exception

            raise aws_sdk_kafka.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "ReassignmentInProgressException":
            import aws_sdk_kafka.errors.reassignment_in_progress_exception

            raise aws_sdk_kafka.errors.reassignment_in_progress_exception.ReassignmentInProgressException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_kafka.errors.service_unavailable_exception

            raise aws_sdk_kafka.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "UnauthorizedException":
            import aws_sdk_kafka.errors.unauthorized_exception

            raise aws_sdk_kafka.errors.unauthorized_exception.UnauthorizedException.from_json(
                data
            )
        case "UnknownTopicOrPartitionException":
            import aws_sdk_kafka.errors.unknown_topic_or_partition_exception

            raise aws_sdk_kafka.errors.unknown_topic_or_partition_exception.UnknownTopicOrPartitionException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_kafka.types.update_topic_response.UpdateTopicResponse:
    import aws_sdk_kafka.types.update_topic_response

    out: aws_sdk_kafka.types.update_topic_response.UpdateTopicResponse = (
        aws_sdk_kafka.types.update_topic_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_kafka._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input: aws_sdk_kafka.types.update_topic_request.UpdateTopicRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )
    url = endpoint.url.rstrip("/") + "/v1/clusters/{ClusterArn}/topics/{TopicName}"
    url = url.replace("{ClusterArn}", quote(str(input["cluster_arn"]), safe=""))
    url = url.replace("{TopicName}", quote(str(input["topic_name"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_kafka.types.update_topic_request

    body: bytes | None = json.dumps(
        aws_sdk_kafka.types.update_topic_request.serialize_json(input)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "PUT",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def update_topic(
    options: OperationOptions,
    input: aws_sdk_kafka.types.update_topic_request.UpdateTopicRequest,
) -> tuple[
    aws_sdk_kafka.types.update_topic_response.UpdateTopicResponse, zapros.Response
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


async def async_update_topic(
    options: AsyncOperationOptions,
    input: aws_sdk_kafka.types.update_topic_request.UpdateTopicRequest,
) -> tuple[
    aws_sdk_kafka.types.update_topic_response.UpdateTopicResponse, zapros.Response
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
