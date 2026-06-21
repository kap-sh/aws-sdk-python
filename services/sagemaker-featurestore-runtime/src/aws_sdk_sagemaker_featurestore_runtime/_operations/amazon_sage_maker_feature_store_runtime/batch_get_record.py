"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchGetRecord``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_sagemaker_featurestore_runtime._auth._signers
import aws_sdk_sagemaker_featurestore_runtime._auth._sigv4
import aws_sdk_sagemaker_featurestore_runtime.errors.access_forbidden
import aws_sdk_sagemaker_featurestore_runtime.errors.internal_failure
import aws_sdk_sagemaker_featurestore_runtime.errors.service_unavailable
import aws_sdk_sagemaker_featurestore_runtime.errors.validation_error
import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_errors
import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_identifiers
import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_request
import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response
import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_result_details
import aws_sdk_sagemaker_featurestore_runtime.types.expiration_time_response
import aws_sdk_sagemaker_featurestore_runtime.types.unprocessed_identifiers
from aws_sdk_sagemaker_featurestore_runtime._protocol.errors import (
    parse_error_metadata_json,
)
from aws_sdk_sagemaker_featurestore_runtime._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_sagemaker_featurestore_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_sagemaker_featurestore_runtime.errors import (
    UnknownServiceError,
)


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessForbidden":
            raise aws_sdk_sagemaker_featurestore_runtime.errors.access_forbidden.AccessForbidden.from_json(
                data
            )
        case "InternalFailure":
            raise aws_sdk_sagemaker_featurestore_runtime.errors.internal_failure.InternalFailure.from_json(
                data
            )
        case "ServiceUnavailable":
            raise aws_sdk_sagemaker_featurestore_runtime.errors.service_unavailable.ServiceUnavailable.from_json(
                data
            )
        case "ValidationError":
            raise aws_sdk_sagemaker_featurestore_runtime.errors.validation_error.ValidationError.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response.BatchGetRecordResponse:
    out: aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response.BatchGetRecordResponse = aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response.BatchGetRecordResponse:
    out: aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response.BatchGetRecordResponse = aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sagemaker_featurestore_runtime._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sagemaker_featurestore_runtime._auth._sigv4.build_sigv4_auth_scheme(
                "sagemaker", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_sagemaker_featurestore_runtime._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_request.BatchGetRecordRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/BatchGetRecord"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_request

    body: bytes | None = json.dumps(
        aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_request.serialize_json(
            input_
        )
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def batch_get_record(
    options: OperationOptions,
    input_: aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_request.BatchGetRecordRequest,
) -> tuple[
    aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response.BatchGetRecordResponse,
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


async def async_batch_get_record(
    options: AsyncOperationOptions,
    input_: aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_request.BatchGetRecordRequest,
) -> tuple[
    aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response.BatchGetRecordResponse,
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
