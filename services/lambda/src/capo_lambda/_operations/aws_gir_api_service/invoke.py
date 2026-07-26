"""Generated from Smithy shape ``com.amazonaws.lambda#Invoke``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
import capo_lambda.errors.durable_execution_already_started_exception
import capo_lambda.errors.ec2_access_denied_exception
import capo_lambda.errors.ec2_throttled_exception
import capo_lambda.errors.ec2_unexpected_exception
import capo_lambda.errors.efs_mount_connectivity_exception
import capo_lambda.errors.efs_mount_failure_exception
import capo_lambda.errors.efs_mount_timeout_exception
import capo_lambda.errors.efsio_exception
import capo_lambda.errors.eni_limit_reached_exception
import capo_lambda.errors.invalid_parameter_value_exception
import capo_lambda.errors.invalid_request_content_exception
import capo_lambda.errors.invalid_runtime_exception
import capo_lambda.errors.invalid_security_group_id_exception
import capo_lambda.errors.invalid_subnet_id_exception
import capo_lambda.errors.invalid_zip_file_exception
import capo_lambda.errors.kms_access_denied_exception
import capo_lambda.errors.kms_disabled_exception
import capo_lambda.errors.kms_invalid_state_exception
import capo_lambda.errors.kms_not_found_exception
import capo_lambda.errors.no_published_version_exception
import capo_lambda.errors.recursive_invocation_exception
import capo_lambda.errors.request_too_large_exception
import capo_lambda.errors.resource_conflict_exception
import capo_lambda.errors.resource_not_found_exception
import capo_lambda.errors.resource_not_ready_exception
import capo_lambda.errors.s3_files_mount_connectivity_exception
import capo_lambda.errors.s3_files_mount_failure_exception
import capo_lambda.errors.s3_files_mount_timeout_exception
import capo_lambda.errors.serialized_request_entity_too_large_exception
import capo_lambda.errors.service_exception
import capo_lambda.errors.snap_start_exception
import capo_lambda.errors.snap_start_not_ready_exception
import capo_lambda.errors.snap_start_timeout_exception
import capo_lambda.errors.subnet_ip_address_limit_reached_exception
import capo_lambda.errors.too_many_requests_exception
import capo_lambda.errors.unsupported_media_type_exception
import capo_lambda.types.blob
import capo_lambda.types.invocation_request
import capo_lambda.types.invocation_response
import capo_lambda.types.invocation_type
import capo_lambda.types.log_type
from capo_lambda._protocol.errors import parse_error_metadata_json
from capo_lambda._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_lambda._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_lambda.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DurableExecutionAlreadyStartedException":
            raise capo_lambda.errors.durable_execution_already_started_exception.DurableExecutionAlreadyStartedException.from_json(
                data
            )
        case "EC2AccessDeniedException":
            raise capo_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException.from_json(
                data
            )
        case "EC2ThrottledException":
            raise capo_lambda.errors.ec2_throttled_exception.EC2ThrottledException.from_json(
                data
            )
        case "EC2UnexpectedException":
            raise capo_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException.from_json(
                data
            )
        case "EFSIOException":
            raise capo_lambda.errors.efsio_exception.EFSIOException.from_json(data)
        case "EFSMountConnectivityException":
            raise capo_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException.from_json(
                data
            )
        case "EFSMountFailureException":
            raise capo_lambda.errors.efs_mount_failure_exception.EFSMountFailureException.from_json(
                data
            )
        case "EFSMountTimeoutException":
            raise capo_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException.from_json(
                data
            )
        case "ENILimitReachedException":
            raise capo_lambda.errors.eni_limit_reached_exception.ENILimitReachedException.from_json(
                data
            )
        case "InvalidParameterValueException":
            raise capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "InvalidRequestContentException":
            raise capo_lambda.errors.invalid_request_content_exception.InvalidRequestContentException.from_json(
                data
            )
        case "InvalidRuntimeException":
            raise capo_lambda.errors.invalid_runtime_exception.InvalidRuntimeException.from_json(
                data
            )
        case "InvalidSecurityGroupIDException":
            raise capo_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException.from_json(
                data
            )
        case "InvalidSubnetIDException":
            raise capo_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException.from_json(
                data
            )
        case "InvalidZipFileException":
            raise capo_lambda.errors.invalid_zip_file_exception.InvalidZipFileException.from_json(
                data
            )
        case "KMSAccessDeniedException":
            raise capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException.from_json(
                data
            )
        case "KMSDisabledException":
            raise capo_lambda.errors.kms_disabled_exception.KMSDisabledException.from_json(
                data
            )
        case "KMSInvalidStateException":
            raise capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException.from_json(
                data
            )
        case "KMSNotFoundException":
            raise capo_lambda.errors.kms_not_found_exception.KMSNotFoundException.from_json(
                data
            )
        case "NoPublishedVersionException":
            raise capo_lambda.errors.no_published_version_exception.NoPublishedVersionException.from_json(
                data
            )
        case "RecursiveInvocationException":
            raise capo_lambda.errors.recursive_invocation_exception.RecursiveInvocationException.from_json(
                data
            )
        case "RequestTooLargeException":
            raise capo_lambda.errors.request_too_large_exception.RequestTooLargeException.from_json(
                data
            )
        case "ResourceConflictException":
            raise capo_lambda.errors.resource_conflict_exception.ResourceConflictException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ResourceNotReadyException":
            raise capo_lambda.errors.resource_not_ready_exception.ResourceNotReadyException.from_json(
                data
            )
        case "S3FilesMountConnectivityException":
            raise capo_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException.from_json(
                data
            )
        case "S3FilesMountFailureException":
            raise capo_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException.from_json(
                data
            )
        case "S3FilesMountTimeoutException":
            raise capo_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException.from_json(
                data
            )
        case "SerializedRequestEntityTooLargeException":
            raise capo_lambda.errors.serialized_request_entity_too_large_exception.SerializedRequestEntityTooLargeException.from_json(
                data
            )
        case "ServiceException":
            raise capo_lambda.errors.service_exception.ServiceException.from_json(data)
        case "SnapStartException":
            raise capo_lambda.errors.snap_start_exception.SnapStartException.from_json(
                data
            )
        case "SnapStartNotReadyException":
            raise capo_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException.from_json(
                data
            )
        case "SnapStartTimeoutException":
            raise capo_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException.from_json(
                data
            )
        case "SubnetIPAddressLimitReachedException":
            raise capo_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException.from_json(
                data
            )
        case "TooManyRequestsException":
            raise capo_lambda.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case "UnsupportedMediaTypeException":
            raise capo_lambda.errors.unsupported_media_type_exception.UnsupportedMediaTypeException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_lambda.types.invocation_response.InvocationResponse:
    out: capo_lambda.types.invocation_response.InvocationResponse = {
        "payload": capo_lambda.types.blob.deserialize_json(json.loads(response.read()))
    }  # type: ignore[typeddict-item]
    if "X-Amz-Function-Error" in response.headers:
        out["function_error"] = str(response.headers["X-Amz-Function-Error"])
    if "X-Amz-Log-Result" in response.headers:
        out["log_result"] = str(response.headers["X-Amz-Log-Result"])
    if "X-Amz-Executed-Version" in response.headers:
        out["executed_version"] = str(response.headers["X-Amz-Executed-Version"])
    if "X-Amz-Durable-Execution-Arn" in response.headers:
        out["durable_execution_arn"] = str(
            response.headers["X-Amz-Durable-Execution-Arn"]
        )
    out["status_code"] = response.status
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_lambda.types.invocation_response.InvocationResponse:
    out: capo_lambda.types.invocation_response.InvocationResponse = {
        "payload": capo_lambda.types.blob.deserialize_json(
            json.loads(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "X-Amz-Function-Error" in response.headers:
        out["function_error"] = str(response.headers["X-Amz-Function-Error"])
    if "X-Amz-Log-Result" in response.headers:
        out["log_result"] = str(response.headers["X-Amz-Log-Result"])
    if "X-Amz-Executed-Version" in response.headers:
        out["executed_version"] = str(response.headers["X-Amz-Executed-Version"])
    if "X-Amz-Durable-Execution-Arn" in response.headers:
        out["durable_execution_arn"] = str(
            response.headers["X-Amz-Durable-Execution-Arn"]
        )
    out["status_code"] = response.status
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_lambda._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_lambda._auth._sigv4.build_sigv4_auth_scheme(
                "lambda", options.region
            )
        )
        if sigv4_config is not None:
            return capo_lambda._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_lambda.types.invocation_request.InvocationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2015-03-31/functions/{FunctionName}/invocations"
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
    if "durable_execution_name" in input_:
        headers["X-Amz-Durable-Execution-Name"] = str(input_["durable_execution_name"])
    if "tenant_id" in input_:
        headers["X-Amz-Tenant-Id"] = str(input_["tenant_id"])
    if "payload" in input_:
        body: bytes | None = json.dumps(
            capo_lambda.types.blob.serialize_json(input_["payload"])
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


def invoke(
    options: OperationOptions,
    input_: capo_lambda.types.invocation_request.InvocationRequest,
) -> tuple[capo_lambda.types.invocation_response.InvocationResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_invoke(
    options: AsyncOperationOptions,
    input_: capo_lambda.types.invocation_request.InvocationRequest,
) -> tuple[capo_lambda.types.invocation_response.InvocationResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
