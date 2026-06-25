"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeWithResponseStream``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_lambda._auth._signers
import aws_sdk_lambda._auth._sigv4
import aws_sdk_lambda.errors.ec2_access_denied_exception
import aws_sdk_lambda.errors.ec2_throttled_exception
import aws_sdk_lambda.errors.ec2_unexpected_exception
import aws_sdk_lambda.errors.efs_mount_connectivity_exception
import aws_sdk_lambda.errors.efs_mount_failure_exception
import aws_sdk_lambda.errors.efs_mount_timeout_exception
import aws_sdk_lambda.errors.efsio_exception
import aws_sdk_lambda.errors.eni_limit_reached_exception
import aws_sdk_lambda.errors.invalid_parameter_value_exception
import aws_sdk_lambda.errors.invalid_request_content_exception
import aws_sdk_lambda.errors.invalid_runtime_exception
import aws_sdk_lambda.errors.invalid_security_group_id_exception
import aws_sdk_lambda.errors.invalid_subnet_id_exception
import aws_sdk_lambda.errors.invalid_zip_file_exception
import aws_sdk_lambda.errors.kms_access_denied_exception
import aws_sdk_lambda.errors.kms_disabled_exception
import aws_sdk_lambda.errors.kms_invalid_state_exception
import aws_sdk_lambda.errors.kms_not_found_exception
import aws_sdk_lambda.errors.no_published_version_exception
import aws_sdk_lambda.errors.recursive_invocation_exception
import aws_sdk_lambda.errors.request_too_large_exception
import aws_sdk_lambda.errors.resource_conflict_exception
import aws_sdk_lambda.errors.resource_not_found_exception
import aws_sdk_lambda.errors.resource_not_ready_exception
import aws_sdk_lambda.errors.s3_files_mount_connectivity_exception
import aws_sdk_lambda.errors.s3_files_mount_failure_exception
import aws_sdk_lambda.errors.s3_files_mount_timeout_exception
import aws_sdk_lambda.errors.serialized_request_entity_too_large_exception
import aws_sdk_lambda.errors.service_exception
import aws_sdk_lambda.errors.snap_start_exception
import aws_sdk_lambda.errors.snap_start_not_ready_exception
import aws_sdk_lambda.errors.snap_start_timeout_exception
import aws_sdk_lambda.errors.subnet_ip_address_limit_reached_exception
import aws_sdk_lambda.errors.too_many_requests_exception
import aws_sdk_lambda.errors.unsupported_media_type_exception
import aws_sdk_lambda.types.blob
import aws_sdk_lambda.types.invoke_with_response_stream_request
import aws_sdk_lambda.types.invoke_with_response_stream_response
import aws_sdk_lambda.types.invoke_with_response_stream_response_event
import aws_sdk_lambda.types.log_type
import aws_sdk_lambda.types.response_streaming_invocation_type
from aws_sdk_lambda._protocol.errors import parse_error_metadata_json
from aws_sdk_lambda._protocol.eventstream import (
    MessageDecoder,
    async_raw_stream_to_events,
    raw_stream_to_events,
)
from aws_sdk_lambda._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_lambda._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_lambda.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "EC2AccessDeniedException":
            raise aws_sdk_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException.from_json(
                data
            )
        case "EC2ThrottledException":
            raise aws_sdk_lambda.errors.ec2_throttled_exception.EC2ThrottledException.from_json(
                data
            )
        case "EC2UnexpectedException":
            raise aws_sdk_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException.from_json(
                data
            )
        case "EFSIOException":
            raise aws_sdk_lambda.errors.efsio_exception.EFSIOException.from_json(data)
        case "EFSMountConnectivityException":
            raise aws_sdk_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException.from_json(
                data
            )
        case "EFSMountFailureException":
            raise aws_sdk_lambda.errors.efs_mount_failure_exception.EFSMountFailureException.from_json(
                data
            )
        case "EFSMountTimeoutException":
            raise aws_sdk_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException.from_json(
                data
            )
        case "ENILimitReachedException":
            raise aws_sdk_lambda.errors.eni_limit_reached_exception.ENILimitReachedException.from_json(
                data
            )
        case "InvalidParameterValueException":
            raise aws_sdk_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "InvalidRequestContentException":
            raise aws_sdk_lambda.errors.invalid_request_content_exception.InvalidRequestContentException.from_json(
                data
            )
        case "InvalidRuntimeException":
            raise aws_sdk_lambda.errors.invalid_runtime_exception.InvalidRuntimeException.from_json(
                data
            )
        case "InvalidSecurityGroupIDException":
            raise aws_sdk_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException.from_json(
                data
            )
        case "InvalidSubnetIDException":
            raise aws_sdk_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException.from_json(
                data
            )
        case "InvalidZipFileException":
            raise aws_sdk_lambda.errors.invalid_zip_file_exception.InvalidZipFileException.from_json(
                data
            )
        case "KMSAccessDeniedException":
            raise aws_sdk_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException.from_json(
                data
            )
        case "KMSDisabledException":
            raise aws_sdk_lambda.errors.kms_disabled_exception.KMSDisabledException.from_json(
                data
            )
        case "KMSInvalidStateException":
            raise aws_sdk_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException.from_json(
                data
            )
        case "KMSNotFoundException":
            raise aws_sdk_lambda.errors.kms_not_found_exception.KMSNotFoundException.from_json(
                data
            )
        case "NoPublishedVersionException":
            raise aws_sdk_lambda.errors.no_published_version_exception.NoPublishedVersionException.from_json(
                data
            )
        case "RecursiveInvocationException":
            raise aws_sdk_lambda.errors.recursive_invocation_exception.RecursiveInvocationException.from_json(
                data
            )
        case "RequestTooLargeException":
            raise aws_sdk_lambda.errors.request_too_large_exception.RequestTooLargeException.from_json(
                data
            )
        case "ResourceConflictException":
            raise aws_sdk_lambda.errors.resource_conflict_exception.ResourceConflictException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_lambda.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ResourceNotReadyException":
            raise aws_sdk_lambda.errors.resource_not_ready_exception.ResourceNotReadyException.from_json(
                data
            )
        case "S3FilesMountConnectivityException":
            raise aws_sdk_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException.from_json(
                data
            )
        case "S3FilesMountFailureException":
            raise aws_sdk_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException.from_json(
                data
            )
        case "S3FilesMountTimeoutException":
            raise aws_sdk_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException.from_json(
                data
            )
        case "SerializedRequestEntityTooLargeException":
            raise aws_sdk_lambda.errors.serialized_request_entity_too_large_exception.SerializedRequestEntityTooLargeException.from_json(
                data
            )
        case "ServiceException":
            raise aws_sdk_lambda.errors.service_exception.ServiceException.from_json(
                data
            )
        case "SnapStartException":
            raise aws_sdk_lambda.errors.snap_start_exception.SnapStartException.from_json(
                data
            )
        case "SnapStartNotReadyException":
            raise aws_sdk_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException.from_json(
                data
            )
        case "SnapStartTimeoutException":
            raise aws_sdk_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException.from_json(
                data
            )
        case "SubnetIPAddressLimitReachedException":
            raise aws_sdk_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise aws_sdk_lambda.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case "UnsupportedMediaTypeException":
            raise aws_sdk_lambda.errors.unsupported_media_type_exception.UnsupportedMediaTypeException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse:
    _message_decoder = MessageDecoder()
    _union_deser = aws_sdk_lambda.types.invoke_with_response_stream_response_event.deserialize_event_json
    _iter = cast(Any, response.iter_bytes())
    out: aws_sdk_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse = {
        "event_stream": cast(
            Any, raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "X-Amz-Executed-Version" in response.headers:
        out["executed_version"] = str(response.headers["X-Amz-Executed-Version"])
    if "Content-Type" in response.headers:
        out["response_stream_content_type"] = str(response.headers["Content-Type"])
    out["status_code"] = response.status
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse:
    _message_decoder = MessageDecoder()
    _union_deser = aws_sdk_lambda.types.invoke_with_response_stream_response_event.deserialize_event_json
    _iter = cast(Any, response.async_iter_bytes())
    out: aws_sdk_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse = {
        "event_stream": cast(
            Any, async_raw_stream_to_events(_iter, _message_decoder, _union_deser)
        )
    }  # type: ignore[reportAssignmentType]
    if "X-Amz-Executed-Version" in response.headers:
        out["executed_version"] = str(response.headers["X-Amz-Executed-Version"])
    if "Content-Type" in response.headers:
        out["response_stream_content_type"] = str(response.headers["Content-Type"])
    out["status_code"] = response.status
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_lambda._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_lambda._auth._sigv4.build_sigv4_auth_scheme(
                "lambda", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_lambda._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/2021-11-15/functions/{FunctionName}/response-streaming-invocations"
    )
    url = url.replace("{FunctionName}", quote(str(input_["function_name"]), safe=""))
    params: dict[str, str] = {}
    if "qualifier" in input_:
        params["Qualifier"] = str(input_["qualifier"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "invocation_type" in input_:
        headers["X-Amz-Invocation-Type"] = str(input_["invocation_type"])
    if "log_type" in input_:
        headers["X-Amz-Log-Type"] = str(input_["log_type"])
    if "client_context" in input_:
        headers["X-Amz-Client-Context"] = str(input_["client_context"])
    if "tenant_id" in input_:
        headers["X-Amz-Tenant-Id"] = str(input_["tenant_id"])
    if "payload" in input_:
        body: bytes | None = json.dumps(
            aws_sdk_lambda.types.blob.serialize_json(input_["payload"])
        ).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def invoke_with_response_stream(
    options: OperationOptions,
    input_: aws_sdk_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest,
) -> tuple[
    aws_sdk_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse,
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


async def async_invoke_with_response_stream(
    options: AsyncOperationOptions,
    input_: aws_sdk_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest,
) -> tuple[
    aws_sdk_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse,
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
