"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecord``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_kinesis._auth._signers
import aws_sdk_kinesis._auth._sigv4
from aws_sdk_kinesis._protocol.errors import parse_error_metadata_json
from aws_sdk_kinesis._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_kinesis._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_kinesis.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.put_record_input
    import aws_sdk_kinesis.types.put_record_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_kinesis.errors.access_denied_exception

            raise aws_sdk_kinesis.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "InternalFailureException":
            import aws_sdk_kinesis.errors.internal_failure_exception

            raise aws_sdk_kinesis.errors.internal_failure_exception.InternalFailureException.from_aws_json_1_1(
                data
            )
        case "InvalidArgumentException":
            import aws_sdk_kinesis.errors.invalid_argument_exception

            raise aws_sdk_kinesis.errors.invalid_argument_exception.InvalidArgumentException.from_aws_json_1_1(
                data
            )
        case "KMSAccessDeniedException":
            import aws_sdk_kinesis.errors.kms_access_denied_exception

            raise aws_sdk_kinesis.errors.kms_access_denied_exception.KMSAccessDeniedException.from_aws_json_1_1(
                data
            )
        case "KMSDisabledException":
            import aws_sdk_kinesis.errors.kms_disabled_exception

            raise aws_sdk_kinesis.errors.kms_disabled_exception.KMSDisabledException.from_aws_json_1_1(
                data
            )
        case "KMSInvalidStateException":
            import aws_sdk_kinesis.errors.kms_invalid_state_exception

            raise aws_sdk_kinesis.errors.kms_invalid_state_exception.KMSInvalidStateException.from_aws_json_1_1(
                data
            )
        case "KMSNotFoundException":
            import aws_sdk_kinesis.errors.kms_not_found_exception

            raise aws_sdk_kinesis.errors.kms_not_found_exception.KMSNotFoundException.from_aws_json_1_1(
                data
            )
        case "KMSOptInRequired":
            import aws_sdk_kinesis.errors.kms_opt_in_required

            raise aws_sdk_kinesis.errors.kms_opt_in_required.KMSOptInRequired.from_aws_json_1_1(
                data
            )
        case "KMSThrottlingException":
            import aws_sdk_kinesis.errors.kms_throttling_exception

            raise aws_sdk_kinesis.errors.kms_throttling_exception.KMSThrottlingException.from_aws_json_1_1(
                data
            )
        case "ProvisionedThroughputExceededException":
            import aws_sdk_kinesis.errors.provisioned_throughput_exceeded_exception

            raise aws_sdk_kinesis.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_kinesis.errors.resource_not_found_exception

            raise aws_sdk_kinesis.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_kinesis.types.put_record_output.PutRecordOutput:
    import aws_sdk_kinesis.types.put_record_output

    out: aws_sdk_kinesis.types.put_record_output.PutRecordOutput = (
        aws_sdk_kinesis.types.put_record_output.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_kinesis._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_kinesis._auth._sigv4.build_sigv4_auth_scheme(
                "kinesis", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_kinesis._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_kinesis.types.put_record_input.PutRecordInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            StreamId=input_.get("stream_id"),
            StreamARN=input_.get("stream_arn"),
            OperationType="data",
            ConsumerARN=options.consumer_arn,
            ResourceARN=options.resource_arn,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "Kinesis_20131202.PutRecord"
    import aws_sdk_kinesis.types.put_record_input

    body: bytes | None = json.dumps(
        aws_sdk_kinesis.types.put_record_input.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def put_record(
    options: OperationOptions,
    input_: aws_sdk_kinesis.types.put_record_input.PutRecordInput,
) -> tuple[aws_sdk_kinesis.types.put_record_output.PutRecordOutput, zapros.Response]:
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


async def async_put_record(
    options: AsyncOperationOptions,
    input_: aws_sdk_kinesis.types.put_record_input.PutRecordInput,
) -> tuple[aws_sdk_kinesis.types.put_record_output.PutRecordOutput, zapros.Response]:
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
