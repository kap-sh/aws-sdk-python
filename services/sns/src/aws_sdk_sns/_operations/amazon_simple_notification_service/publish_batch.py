"""Generated from Smithy shape ``com.amazonaws.sns#PublishBatch``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_sns._auth._signers
import aws_sdk_sns._auth._sigv4
import aws_sdk_sns.errors.authorization_error_exception
import aws_sdk_sns.errors.batch_entry_ids_not_distinct_exception
import aws_sdk_sns.errors.batch_request_too_long_exception
import aws_sdk_sns.errors.empty_batch_request_exception
import aws_sdk_sns.errors.endpoint_disabled_exception
import aws_sdk_sns.errors.internal_error_exception
import aws_sdk_sns.errors.invalid_batch_entry_id_exception
import aws_sdk_sns.errors.invalid_parameter_exception
import aws_sdk_sns.errors.invalid_parameter_value_exception
import aws_sdk_sns.errors.invalid_security_exception
import aws_sdk_sns.errors.kms_access_denied_exception
import aws_sdk_sns.errors.kms_disabled_exception
import aws_sdk_sns.errors.kms_invalid_state_exception
import aws_sdk_sns.errors.kms_not_found_exception
import aws_sdk_sns.errors.kms_opt_in_required
import aws_sdk_sns.errors.kms_throttling_exception
import aws_sdk_sns.errors.not_found_exception
import aws_sdk_sns.errors.platform_application_disabled_exception
import aws_sdk_sns.errors.too_many_entries_in_batch_request_exception
import aws_sdk_sns.errors.validation_exception
import aws_sdk_sns.types.batch_result_error_entry_list
import aws_sdk_sns.types.publish_batch_input
import aws_sdk_sns.types.publish_batch_request_entry_list
import aws_sdk_sns.types.publish_batch_response
import aws_sdk_sns.types.publish_batch_result_entry_list
from aws_sdk_sns._protocol.errors import parse_error_metadata
from aws_sdk_sns._protocol.xml import fromstring
from aws_sdk_sns._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_sns._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_sns.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AuthorizationErrorException":
            raise aws_sdk_sns.errors.authorization_error_exception.AuthorizationErrorException.from_query(
                root
            )
        case "BatchEntryIdsNotDistinctException":
            raise aws_sdk_sns.errors.batch_entry_ids_not_distinct_exception.BatchEntryIdsNotDistinctException.from_query(
                root
            )
        case "BatchRequestTooLongException":
            raise aws_sdk_sns.errors.batch_request_too_long_exception.BatchRequestTooLongException.from_query(
                root
            )
        case "EmptyBatchRequestException":
            raise aws_sdk_sns.errors.empty_batch_request_exception.EmptyBatchRequestException.from_query(
                root
            )
        case "EndpointDisabledException":
            raise aws_sdk_sns.errors.endpoint_disabled_exception.EndpointDisabledException.from_query(
                root
            )
        case "InternalErrorException":
            raise aws_sdk_sns.errors.internal_error_exception.InternalErrorException.from_query(
                root
            )
        case "InvalidBatchEntryIdException":
            raise aws_sdk_sns.errors.invalid_batch_entry_id_exception.InvalidBatchEntryIdException.from_query(
                root
            )
        case "InvalidParameterException":
            raise aws_sdk_sns.errors.invalid_parameter_exception.InvalidParameterException.from_query(
                root
            )
        case "InvalidParameterValueException":
            raise aws_sdk_sns.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_query(
                root
            )
        case "InvalidSecurityException":
            raise aws_sdk_sns.errors.invalid_security_exception.InvalidSecurityException.from_query(
                root
            )
        case "KMSAccessDeniedException":
            raise aws_sdk_sns.errors.kms_access_denied_exception.KMSAccessDeniedException.from_query(
                root
            )
        case "KMSDisabledException":
            raise aws_sdk_sns.errors.kms_disabled_exception.KMSDisabledException.from_query(
                root
            )
        case "KMSInvalidStateException":
            raise aws_sdk_sns.errors.kms_invalid_state_exception.KMSInvalidStateException.from_query(
                root
            )
        case "KMSNotFoundException":
            raise aws_sdk_sns.errors.kms_not_found_exception.KMSNotFoundException.from_query(
                root
            )
        case "KMSOptInRequired":
            raise aws_sdk_sns.errors.kms_opt_in_required.KMSOptInRequired.from_query(
                root
            )
        case "KMSThrottlingException":
            raise aws_sdk_sns.errors.kms_throttling_exception.KMSThrottlingException.from_query(
                root
            )
        case "NotFoundException":
            raise aws_sdk_sns.errors.not_found_exception.NotFoundException.from_query(
                root
            )
        case "PlatformApplicationDisabledException":
            raise aws_sdk_sns.errors.platform_application_disabled_exception.PlatformApplicationDisabledException.from_query(
                root
            )
        case "TooManyEntriesInBatchRequestException":
            raise aws_sdk_sns.errors.too_many_entries_in_batch_request_exception.TooManyEntriesInBatchRequestException.from_query(
                root
            )
        case "ValidationException":
            raise aws_sdk_sns.errors.validation_exception.ValidationException.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_sns.types.publish_batch_response.PublishBatchResponse:
    root = fromstring(response.read())
    result = root.find("PublishBatchResult")
    out: aws_sdk_sns.types.publish_batch_response.PublishBatchResponse = (
        aws_sdk_sns.types.publish_batch_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_sns.types.publish_batch_response.PublishBatchResponse:
    root = fromstring(await response.aread())
    result = root.find("PublishBatchResult")
    out: aws_sdk_sns.types.publish_batch_response.PublishBatchResponse = (
        aws_sdk_sns.types.publish_batch_response.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sns._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sns._auth._sigv4.build_sigv4_auth_scheme("sns", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_sns._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_sns.types.publish_batch_input.PublishBatchInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "PublishBatch"))
    pairs.append(("Version", "2010-03-31"))
    import aws_sdk_sns.types.publish_batch_input

    aws_sdk_sns.types.publish_batch_input.serialize_query(input_, pairs, "")
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def publish_batch(
    options: OperationOptions,
    input_: aws_sdk_sns.types.publish_batch_input.PublishBatchInput,
) -> tuple[
    aws_sdk_sns.types.publish_batch_response.PublishBatchResponse, zapros.Response
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


async def async_publish_batch(
    options: AsyncOperationOptions,
    input_: aws_sdk_sns.types.publish_batch_input.PublishBatchInput,
) -> tuple[
    aws_sdk_sns.types.publish_batch_response.PublishBatchResponse, zapros.Response
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
