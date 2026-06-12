"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchWriteItem``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import jmespath
import zapros

import aws_sdk_dynamodb._auth._signers
import aws_sdk_dynamodb._auth._sigv4
from aws_sdk_dynamodb._protocol.errors import parse_error_metadata_json
from aws_sdk_dynamodb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_dynamodb._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_dynamodb.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.batch_write_item_input
    import aws_sdk_dynamodb.types.batch_write_item_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServerError":
            import aws_sdk_dynamodb.errors.internal_server_error

            raise aws_sdk_dynamodb.errors.internal_server_error.InternalServerError.from_aws_json_1_0(
                data
            )
        case "InvalidEndpointException":
            import aws_sdk_dynamodb.errors.invalid_endpoint_exception

            raise aws_sdk_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException.from_aws_json_1_0(
                data
            )
        case "ItemCollectionSizeLimitExceededException":
            import aws_sdk_dynamodb.errors.item_collection_size_limit_exceeded_exception

            raise aws_sdk_dynamodb.errors.item_collection_size_limit_exceeded_exception.ItemCollectionSizeLimitExceededException.from_aws_json_1_0(
                data
            )
        case "ProvisionedThroughputExceededException":
            import aws_sdk_dynamodb.errors.provisioned_throughput_exceeded_exception

            raise aws_sdk_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException.from_aws_json_1_0(
                data
            )
        case "ReplicatedWriteConflictException":
            import aws_sdk_dynamodb.errors.replicated_write_conflict_exception

            raise aws_sdk_dynamodb.errors.replicated_write_conflict_exception.ReplicatedWriteConflictException.from_aws_json_1_0(
                data
            )
        case "RequestLimitExceeded":
            import aws_sdk_dynamodb.errors.request_limit_exceeded

            raise aws_sdk_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_dynamodb.errors.resource_not_found_exception

            raise aws_sdk_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            import aws_sdk_dynamodb.errors.throttling_exception

            raise aws_sdk_dynamodb.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_dynamodb.types.batch_write_item_output.BatchWriteItemOutput:
    import aws_sdk_dynamodb.types.batch_write_item_output

    out: aws_sdk_dynamodb.types.batch_write_item_output.BatchWriteItemOutput = (
        aws_sdk_dynamodb.types.batch_write_item_output.deserialize_aws_json_1_0(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_dynamodb._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input: aws_sdk_dynamodb.types.batch_write_item_input.BatchWriteItemInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            AccountId=options.account_id,
            AccountIdEndpointMode=options.account_id_endpoint_mode,
            ResourceArn=options.resource_arn,
            ResourceArnList=jmespath.search("keys(RequestItems)", input),
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "DynamoDB_20120810.BatchWriteItem"
    import aws_sdk_dynamodb.types.batch_write_item_input

    body: bytes | None = json.dumps(
        aws_sdk_dynamodb.types.batch_write_item_input.serialize_aws_json_1_0(input)
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


def batch_write_item(
    options: OperationOptions,
    input: aws_sdk_dynamodb.types.batch_write_item_input.BatchWriteItemInput,
) -> tuple[
    aws_sdk_dynamodb.types.batch_write_item_output.BatchWriteItemOutput, zapros.Response
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


async def async_batch_write_item(
    options: AsyncOperationOptions,
    input: aws_sdk_dynamodb.types.batch_write_item_input.BatchWriteItemInput,
) -> tuple[
    aws_sdk_dynamodb.types.batch_write_item_output.BatchWriteItemOutput, zapros.Response
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
