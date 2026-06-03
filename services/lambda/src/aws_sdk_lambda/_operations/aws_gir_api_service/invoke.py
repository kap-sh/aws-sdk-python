"""Generated from Smithy shape ``com.amazonaws.lambda#Invoke``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Never, Any
from aws_sdk_lambda._rule_engine._endpoint_rule_set import EndpointParams, resolve
import zapros
from urllib.parse import quote
from aws_sdk_lambda.errors import UnknownServiceError
from aws_sdk_lambda._protocol.errors import parse_error_metadata_json
import json
import aws_sdk_lambda._auth._signers
from aws_sdk_lambda._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_lambda.types.invocation_request
    import aws_sdk_lambda.types.invocation_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "DurableExecutionAlreadyStartedException":
            import aws_sdk_lambda.errors.durable_execution_already_started_exception

            raise aws_sdk_lambda.errors.durable_execution_already_started_exception.DurableExecutionAlreadyStartedException.from_json(
                data
            )
        case "EC2AccessDeniedException":
            import aws_sdk_lambda.errors.ec2_access_denied_exception

            raise aws_sdk_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException.from_json(
                data
            )
        case "EC2ThrottledException":
            import aws_sdk_lambda.errors.ec2_throttled_exception

            raise aws_sdk_lambda.errors.ec2_throttled_exception.EC2ThrottledException.from_json(
                data
            )
        case "EC2UnexpectedException":
            import aws_sdk_lambda.errors.ec2_unexpected_exception

            raise aws_sdk_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException.from_json(
                data
            )
        case "EFSIOException":
            import aws_sdk_lambda.errors.efsio_exception

            raise aws_sdk_lambda.errors.efsio_exception.EFSIOException.from_json(data)
        case "EFSMountConnectivityException":
            import aws_sdk_lambda.errors.efs_mount_connectivity_exception

            raise aws_sdk_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException.from_json(
                data
            )
        case "EFSMountFailureException":
            import aws_sdk_lambda.errors.efs_mount_failure_exception

            raise aws_sdk_lambda.errors.efs_mount_failure_exception.EFSMountFailureException.from_json(
                data
            )
        case "EFSMountTimeoutException":
            import aws_sdk_lambda.errors.efs_mount_timeout_exception

            raise aws_sdk_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException.from_json(
                data
            )
        case "ENILimitReachedException":
            import aws_sdk_lambda.errors.eni_limit_reached_exception

            raise aws_sdk_lambda.errors.eni_limit_reached_exception.ENILimitReachedException.from_json(
                data
            )
        case "InvalidParameterValueException":
            import aws_sdk_lambda.errors.invalid_parameter_value_exception

            raise aws_sdk_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "InvalidRequestContentException":
            import aws_sdk_lambda.errors.invalid_request_content_exception

            raise aws_sdk_lambda.errors.invalid_request_content_exception.InvalidRequestContentException.from_json(
                data
            )
        case "InvalidRuntimeException":
            import aws_sdk_lambda.errors.invalid_runtime_exception

            raise aws_sdk_lambda.errors.invalid_runtime_exception.InvalidRuntimeException.from_json(
                data
            )
        case "InvalidSecurityGroupIDException":
            import aws_sdk_lambda.errors.invalid_security_group_id_exception

            raise aws_sdk_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException.from_json(
                data
            )
        case "InvalidSubnetIDException":
            import aws_sdk_lambda.errors.invalid_subnet_id_exception

            raise aws_sdk_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException.from_json(
                data
            )
        case "InvalidZipFileException":
            import aws_sdk_lambda.errors.invalid_zip_file_exception

            raise aws_sdk_lambda.errors.invalid_zip_file_exception.InvalidZipFileException.from_json(
                data
            )
        case "KMSAccessDeniedException":
            import aws_sdk_lambda.errors.kms_access_denied_exception

            raise aws_sdk_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException.from_json(
                data
            )
        case "KMSDisabledException":
            import aws_sdk_lambda.errors.kms_disabled_exception

            raise aws_sdk_lambda.errors.kms_disabled_exception.KMSDisabledException.from_json(
                data
            )
        case "KMSInvalidStateException":
            import aws_sdk_lambda.errors.kms_invalid_state_exception

            raise aws_sdk_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException.from_json(
                data
            )
        case "KMSNotFoundException":
            import aws_sdk_lambda.errors.kms_not_found_exception

            raise aws_sdk_lambda.errors.kms_not_found_exception.KMSNotFoundException.from_json(
                data
            )
        case "NoPublishedVersionException":
            import aws_sdk_lambda.errors.no_published_version_exception

            raise aws_sdk_lambda.errors.no_published_version_exception.NoPublishedVersionException.from_json(
                data
            )
        case "RecursiveInvocationException":
            import aws_sdk_lambda.errors.recursive_invocation_exception

            raise aws_sdk_lambda.errors.recursive_invocation_exception.RecursiveInvocationException.from_json(
                data
            )
        case "RequestTooLargeException":
            import aws_sdk_lambda.errors.request_too_large_exception

            raise aws_sdk_lambda.errors.request_too_large_exception.RequestTooLargeException.from_json(
                data
            )
        case "ResourceConflictException":
            import aws_sdk_lambda.errors.resource_conflict_exception

            raise aws_sdk_lambda.errors.resource_conflict_exception.ResourceConflictException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_lambda.errors.resource_not_found_exception

            raise aws_sdk_lambda.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ResourceNotReadyException":
            import aws_sdk_lambda.errors.resource_not_ready_exception

            raise aws_sdk_lambda.errors.resource_not_ready_exception.ResourceNotReadyException.from_json(
                data
            )
        case "S3FilesMountConnectivityException":
            import aws_sdk_lambda.errors.s3_files_mount_connectivity_exception

            raise aws_sdk_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException.from_json(
                data
            )
        case "S3FilesMountFailureException":
            import aws_sdk_lambda.errors.s3_files_mount_failure_exception

            raise aws_sdk_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException.from_json(
                data
            )
        case "S3FilesMountTimeoutException":
            import aws_sdk_lambda.errors.s3_files_mount_timeout_exception

            raise aws_sdk_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException.from_json(
                data
            )
        case "SerializedRequestEntityTooLargeException":
            import aws_sdk_lambda.errors.serialized_request_entity_too_large_exception

            raise aws_sdk_lambda.errors.serialized_request_entity_too_large_exception.SerializedRequestEntityTooLargeException.from_json(
                data
            )
        case "ServiceException":
            import aws_sdk_lambda.errors.service_exception

            raise aws_sdk_lambda.errors.service_exception.ServiceException.from_json(
                data
            )
        case "SnapStartException":
            import aws_sdk_lambda.errors.snap_start_exception

            raise aws_sdk_lambda.errors.snap_start_exception.SnapStartException.from_json(
                data
            )
        case "SnapStartNotReadyException":
            import aws_sdk_lambda.errors.snap_start_not_ready_exception

            raise aws_sdk_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException.from_json(
                data
            )
        case "SnapStartTimeoutException":
            import aws_sdk_lambda.errors.snap_start_timeout_exception

            raise aws_sdk_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException.from_json(
                data
            )
        case "SubnetIPAddressLimitReachedException":
            import aws_sdk_lambda.errors.subnet_ip_address_limit_reached_exception

            raise aws_sdk_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_lambda.errors.too_many_requests_exception

            raise aws_sdk_lambda.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case "UnsupportedMediaTypeException":
            import aws_sdk_lambda.errors.unsupported_media_type_exception

            raise aws_sdk_lambda.errors.unsupported_media_type_exception.UnsupportedMediaTypeException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_lambda.types.invocation_response.InvocationResponse:
    import aws_sdk_lambda.types.blob

    out: aws_sdk_lambda.types.invocation_response.InvocationResponse = {
        "payload": aws_sdk_lambda.types.blob.deserialize_json(
            json.loads(response.read())
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
) -> aws_sdk_lambda._auth._signers.Signer | None:
    if auth_schemes:
        for scheme in auth_schemes:
            match scheme["name"]:
                case "sigv4" | "sigv4a" | "sigv4-s3express" if (
                    options.credentials_provider is not None
                ):
                    return aws_sdk_lambda._auth._signers.SigV4Signer(
                        options.credentials_provider, auth_scheme=scheme
                    )
                case "none":
                    return None
                case _:
                    raise RuntimeError(
                        f"Could not find provider for auth scheme {scheme['name']!r}"
                    )
    if options.credentials_provider is not None:
        if options.region is None:
            raise RuntimeError("options.region is required for SigV4 signing")
        return aws_sdk_lambda._auth._signers.SigV4Signer(
            options.credentials_provider,
            auth_scheme={
                "name": "sigv4",
                "signingName": "lambda",
                "signingRegion": options.region,
                "disableDoubleEncoding": False,
                "disableNormalizePath": False,
            },
        )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_lambda.types.invocation_request.InvocationRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/2015-03-31/functions/{FunctionName}/invocations"
    url = url.replace("{FunctionName}", quote(str(input["function_name"]), safe=""))
    params: dict[str, str] = {}
    if "qualifier" in input:
        params["Qualifier"] = str(input["qualifier"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "invocation_type" in input:
        headers["X-Amz-Invocation-Type"] = str(input["invocation_type"])
    if "log_type" in input:
        headers["X-Amz-Log-Type"] = str(input["log_type"])
    if "client_context" in input:
        headers["X-Amz-Client-Context"] = str(input["client_context"])
    if "durable_execution_name" in input:
        headers["X-Amz-Durable-Execution-Name"] = str(input["durable_execution_name"])
    if "tenant_id" in input:
        headers["X-Amz-Tenant-Id"] = str(input["tenant_id"])
    if "payload" in input:
        import aws_sdk_lambda.types.blob

        body: bytes | None = json.dumps(
            aws_sdk_lambda.types.blob.serialize_json(input["payload"])
        ).encode()
        headers["content-type"] = "application/json"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,  # type: ignore
        context={"signer": signer},  # type: ignore
    )


def invoke(
    options: OperationOptions,
    input: aws_sdk_lambda.types.invocation_request.InvocationRequest,
) -> tuple[
    aws_sdk_lambda.types.invocation_response.InvocationResponse, zapros.Response
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


async def async_invoke(
    options: AsyncOperationOptions,
    input: aws_sdk_lambda.types.invocation_request.InvocationRequest,
) -> tuple[
    aws_sdk_lambda.types.invocation_response.InvocationResponse, zapros.Response
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
