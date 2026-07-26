"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StartQuery``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudtrail._auth._signers
import capo_cloudtrail._auth._sigv4
import capo_cloudtrail.errors.event_data_store_arn_invalid_exception
import capo_cloudtrail.errors.event_data_store_not_found_exception
import capo_cloudtrail.errors.inactive_event_data_store_exception
import capo_cloudtrail.errors.insufficient_encryption_policy_exception
import capo_cloudtrail.errors.insufficient_s3_bucket_policy_exception
import capo_cloudtrail.errors.invalid_parameter_exception
import capo_cloudtrail.errors.invalid_query_statement_exception
import capo_cloudtrail.errors.invalid_s3_bucket_name_exception
import capo_cloudtrail.errors.invalid_s3_prefix_exception
import capo_cloudtrail.errors.max_concurrent_queries_exception
import capo_cloudtrail.errors.no_management_account_slr_exists_exception
import capo_cloudtrail.errors.operation_not_permitted_exception
import capo_cloudtrail.errors.s3_bucket_does_not_exist_exception
import capo_cloudtrail.errors.unsupported_operation_exception
import capo_cloudtrail.types.query_parameters
import capo_cloudtrail.types.start_query_request
import capo_cloudtrail.types.start_query_response
from capo_cloudtrail._protocol.errors import parse_error_metadata_json
from capo_cloudtrail._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudtrail._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_cloudtrail.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "EventDataStoreARNInvalidException":
            raise capo_cloudtrail.errors.event_data_store_arn_invalid_exception.EventDataStoreARNInvalidException.from_aws_json_1_1(
                data
            )
        case "EventDataStoreNotFoundException":
            raise capo_cloudtrail.errors.event_data_store_not_found_exception.EventDataStoreNotFoundException.from_aws_json_1_1(
                data
            )
        case "InactiveEventDataStoreException":
            raise capo_cloudtrail.errors.inactive_event_data_store_exception.InactiveEventDataStoreException.from_aws_json_1_1(
                data
            )
        case "InsufficientEncryptionPolicyException":
            raise capo_cloudtrail.errors.insufficient_encryption_policy_exception.InsufficientEncryptionPolicyException.from_aws_json_1_1(
                data
            )
        case "InsufficientS3BucketPolicyException":
            raise capo_cloudtrail.errors.insufficient_s3_bucket_policy_exception.InsufficientS3BucketPolicyException.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise capo_cloudtrail.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "InvalidQueryStatementException":
            raise capo_cloudtrail.errors.invalid_query_statement_exception.InvalidQueryStatementException.from_aws_json_1_1(
                data
            )
        case "InvalidS3BucketNameException":
            raise capo_cloudtrail.errors.invalid_s3_bucket_name_exception.InvalidS3BucketNameException.from_aws_json_1_1(
                data
            )
        case "InvalidS3PrefixException":
            raise capo_cloudtrail.errors.invalid_s3_prefix_exception.InvalidS3PrefixException.from_aws_json_1_1(
                data
            )
        case "MaxConcurrentQueriesException":
            raise capo_cloudtrail.errors.max_concurrent_queries_exception.MaxConcurrentQueriesException.from_aws_json_1_1(
                data
            )
        case "NoManagementAccountSLRExistsException":
            raise capo_cloudtrail.errors.no_management_account_slr_exists_exception.NoManagementAccountSLRExistsException.from_aws_json_1_1(
                data
            )
        case "OperationNotPermittedException":
            raise capo_cloudtrail.errors.operation_not_permitted_exception.OperationNotPermittedException.from_aws_json_1_1(
                data
            )
        case "S3BucketDoesNotExistException":
            raise capo_cloudtrail.errors.s3_bucket_does_not_exist_exception.S3BucketDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "UnsupportedOperationException":
            raise capo_cloudtrail.errors.unsupported_operation_exception.UnsupportedOperationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudtrail.types.start_query_response.StartQueryResponse:
    out: capo_cloudtrail.types.start_query_response.StartQueryResponse = (
        capo_cloudtrail.types.start_query_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudtrail.types.start_query_response.StartQueryResponse:
    out: capo_cloudtrail.types.start_query_response.StartQueryResponse = (
        capo_cloudtrail.types.start_query_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudtrail._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_cloudtrail._auth._sigv4.build_sigv4_auth_scheme(
                "cloudtrail", options.region
            )
        )
        if sigv4_config is not None:
            return capo_cloudtrail._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudtrail.types.start_query_request.StartQueryRequest,
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
    headers["X-Amz-Target"] = "CloudTrail_20131101.StartQuery"
    body: bytes | None = json.dumps(
        capo_cloudtrail.types.start_query_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def start_query(
    options: OperationOptions,
    input_: capo_cloudtrail.types.start_query_request.StartQueryRequest,
) -> tuple[
    capo_cloudtrail.types.start_query_response.StartQueryResponse, zapros.Response
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


async def async_start_query(
    options: AsyncOperationOptions,
    input_: capo_cloudtrail.types.start_query_request.StartQueryRequest,
) -> tuple[
    capo_cloudtrail.types.start_query_response.StartQueryResponse, zapros.Response
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
