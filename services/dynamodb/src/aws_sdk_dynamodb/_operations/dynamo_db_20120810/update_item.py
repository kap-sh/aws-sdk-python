"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateItem``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_dynamodb._auth._signers
import aws_sdk_dynamodb._auth._sigv4
import aws_sdk_dynamodb.errors.conditional_check_failed_exception
import aws_sdk_dynamodb.errors.internal_server_error
import aws_sdk_dynamodb.errors.invalid_endpoint_exception
import aws_sdk_dynamodb.errors.item_collection_size_limit_exceeded_exception
import aws_sdk_dynamodb.errors.provisioned_throughput_exceeded_exception
import aws_sdk_dynamodb.errors.replicated_write_conflict_exception
import aws_sdk_dynamodb.errors.request_limit_exceeded
import aws_sdk_dynamodb.errors.resource_not_found_exception
import aws_sdk_dynamodb.errors.throttling_exception
import aws_sdk_dynamodb.errors.transaction_conflict_exception
import aws_sdk_dynamodb.types.attribute_map
import aws_sdk_dynamodb.types.attribute_updates
import aws_sdk_dynamodb.types.conditional_operator
import aws_sdk_dynamodb.types.consumed_capacity
import aws_sdk_dynamodb.types.expected_attribute_map
import aws_sdk_dynamodb.types.expression_attribute_name_map
import aws_sdk_dynamodb.types.expression_attribute_value_map
import aws_sdk_dynamodb.types.item_collection_metrics
import aws_sdk_dynamodb.types.key
import aws_sdk_dynamodb.types.return_consumed_capacity
import aws_sdk_dynamodb.types.return_item_collection_metrics
import aws_sdk_dynamodb.types.return_value
import aws_sdk_dynamodb.types.return_values_on_condition_check_failure
import aws_sdk_dynamodb.types.update_item_input
import aws_sdk_dynamodb.types.update_item_output
from aws_sdk_dynamodb._protocol.errors import parse_error_metadata_json
from aws_sdk_dynamodb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_dynamodb.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConditionalCheckFailedException":
            raise aws_sdk_dynamodb.errors.conditional_check_failed_exception.ConditionalCheckFailedException.from_aws_json_1_0(
                data
            )
        case "InternalServerError":
            raise aws_sdk_dynamodb.errors.internal_server_error.InternalServerError.from_aws_json_1_0(
                data
            )
        case "InvalidEndpointException":
            raise aws_sdk_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException.from_aws_json_1_0(
                data
            )
        case "ItemCollectionSizeLimitExceededException":
            raise aws_sdk_dynamodb.errors.item_collection_size_limit_exceeded_exception.ItemCollectionSizeLimitExceededException.from_aws_json_1_0(
                data
            )
        case "ProvisionedThroughputExceededException":
            raise aws_sdk_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException.from_aws_json_1_0(
                data
            )
        case "ReplicatedWriteConflictException":
            raise aws_sdk_dynamodb.errors.replicated_write_conflict_exception.ReplicatedWriteConflictException.from_aws_json_1_0(
                data
            )
        case "RequestLimitExceeded":
            raise aws_sdk_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_dynamodb.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case "TransactionConflictException":
            raise aws_sdk_dynamodb.errors.transaction_conflict_exception.TransactionConflictException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_dynamodb.types.update_item_output.UpdateItemOutput:
    out: aws_sdk_dynamodb.types.update_item_output.UpdateItemOutput = (
        aws_sdk_dynamodb.types.update_item_output.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_dynamodb.types.update_item_output.UpdateItemOutput:
    out: aws_sdk_dynamodb.types.update_item_output.UpdateItemOutput = (
        aws_sdk_dynamodb.types.update_item_output.deserialize_aws_json_1_0(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_dynamodb._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_dynamodb._auth._sigv4.build_sigv4_auth_scheme(
                "dynamodb", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_dynamodb._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_dynamodb.types.update_item_input.UpdateItemInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            AccountId=options.account_id,
            AccountIdEndpointMode=options.account_id_endpoint_mode,
            ResourceArn=input_.get("table_name"),
            ResourceArnList=options.resource_arn_list,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "DynamoDB_20120810.UpdateItem"
    body: bytes | None = json.dumps(
        aws_sdk_dynamodb.types.update_item_input.serialize_aws_json_1_0(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.0"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def update_item(
    options: OperationOptions,
    input_: aws_sdk_dynamodb.types.update_item_input.UpdateItemInput,
) -> tuple[aws_sdk_dynamodb.types.update_item_output.UpdateItemOutput, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_update_item(
    options: AsyncOperationOptions,
    input_: aws_sdk_dynamodb.types.update_item_input.UpdateItemInput,
) -> tuple[aws_sdk_dynamodb.types.update_item_output.UpdateItemOutput, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
