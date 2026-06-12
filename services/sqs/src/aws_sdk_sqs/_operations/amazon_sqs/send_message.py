"""Generated from Smithy shape ``com.amazonaws.sqs#SendMessage``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_sqs._auth._signers
import aws_sdk_sqs._auth._sigv4
from aws_sdk_sqs._protocol.errors import parse_error_metadata_json
from aws_sdk_sqs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_sqs._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_sqs.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.send_message_request
    import aws_sdk_sqs.types.send_message_result


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidAddress":
            import aws_sdk_sqs.errors.invalid_address

            raise aws_sdk_sqs.errors.invalid_address.InvalidAddress.from_aws_json_1_0(
                data
            )
        case "InvalidMessageContents":
            import aws_sdk_sqs.errors.invalid_message_contents

            raise aws_sdk_sqs.errors.invalid_message_contents.InvalidMessageContents.from_aws_json_1_0(
                data
            )
        case "InvalidSecurity":
            import aws_sdk_sqs.errors.invalid_security

            raise aws_sdk_sqs.errors.invalid_security.InvalidSecurity.from_aws_json_1_0(
                data
            )
        case "KmsAccessDenied":
            import aws_sdk_sqs.errors.kms_access_denied

            raise aws_sdk_sqs.errors.kms_access_denied.KmsAccessDenied.from_aws_json_1_0(
                data
            )
        case "KmsDisabled":
            import aws_sdk_sqs.errors.kms_disabled

            raise aws_sdk_sqs.errors.kms_disabled.KmsDisabled.from_aws_json_1_0(data)
        case "KmsInvalidKeyUsage":
            import aws_sdk_sqs.errors.kms_invalid_key_usage

            raise aws_sdk_sqs.errors.kms_invalid_key_usage.KmsInvalidKeyUsage.from_aws_json_1_0(
                data
            )
        case "KmsInvalidState":
            import aws_sdk_sqs.errors.kms_invalid_state

            raise aws_sdk_sqs.errors.kms_invalid_state.KmsInvalidState.from_aws_json_1_0(
                data
            )
        case "KmsNotFound":
            import aws_sdk_sqs.errors.kms_not_found

            raise aws_sdk_sqs.errors.kms_not_found.KmsNotFound.from_aws_json_1_0(data)
        case "KmsOptInRequired":
            import aws_sdk_sqs.errors.kms_opt_in_required

            raise aws_sdk_sqs.errors.kms_opt_in_required.KmsOptInRequired.from_aws_json_1_0(
                data
            )
        case "KmsThrottled":
            import aws_sdk_sqs.errors.kms_throttled

            raise aws_sdk_sqs.errors.kms_throttled.KmsThrottled.from_aws_json_1_0(data)
        case "QueueDoesNotExist":
            import aws_sdk_sqs.errors.queue_does_not_exist

            raise aws_sdk_sqs.errors.queue_does_not_exist.QueueDoesNotExist.from_aws_json_1_0(
                data
            )
        case "RequestThrottled":
            import aws_sdk_sqs.errors.request_throttled

            raise aws_sdk_sqs.errors.request_throttled.RequestThrottled.from_aws_json_1_0(
                data
            )
        case "UnsupportedOperation":
            import aws_sdk_sqs.errors.unsupported_operation

            raise aws_sdk_sqs.errors.unsupported_operation.UnsupportedOperation.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_sqs.types.send_message_result.SendMessageResult:
    import aws_sdk_sqs.types.send_message_result

    out: aws_sdk_sqs.types.send_message_result.SendMessageResult = (
        aws_sdk_sqs.types.send_message_result.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sqs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sqs._auth._sigv4.build_sigv4_auth_scheme("sqs", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_sqs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_sqs.types.send_message_request.SendMessageRequest,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AmazonSQS.SendMessage"
    import aws_sdk_sqs.types.send_message_request

    body: bytes | None = json.dumps(
        aws_sdk_sqs.types.send_message_request.serialize_aws_json_1_0(input)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def send_message(
    options: OperationOptions,
    input: aws_sdk_sqs.types.send_message_request.SendMessageRequest,
) -> tuple[aws_sdk_sqs.types.send_message_result.SendMessageResult, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_send_message(
    options: AsyncOperationOptions,
    input: aws_sdk_sqs.types.send_message_request.SendMessageRequest,
) -> tuple[aws_sdk_sqs.types.send_message_result.SendMessageResult, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
