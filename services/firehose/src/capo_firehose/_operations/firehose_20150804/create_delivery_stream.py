"""Generated from Smithy shape ``com.amazonaws.firehose#CreateDeliveryStream``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_firehose._auth._signers
import capo_firehose._auth._sigv4
import capo_firehose.errors.invalid_argument_exception
import capo_firehose.errors.invalid_kms_resource_exception
import capo_firehose.errors.limit_exceeded_exception
import capo_firehose.errors.resource_in_use_exception
import capo_firehose.types.amazon_open_search_serverless_destination_configuration
import capo_firehose.types.amazonopensearchservice_destination_configuration
import capo_firehose.types.create_delivery_stream_input
import capo_firehose.types.create_delivery_stream_output
import capo_firehose.types.database_source_configuration
import capo_firehose.types.delivery_stream_encryption_configuration_input
import capo_firehose.types.delivery_stream_type
import capo_firehose.types.direct_put_source_configuration
import capo_firehose.types.elasticsearch_destination_configuration
import capo_firehose.types.extended_s3_destination_configuration
import capo_firehose.types.http_endpoint_destination_configuration
import capo_firehose.types.iceberg_destination_configuration
import capo_firehose.types.kinesis_stream_source_configuration
import capo_firehose.types.msk_source_configuration
import capo_firehose.types.redshift_destination_configuration
import capo_firehose.types.s3_destination_configuration
import capo_firehose.types.snowflake_destination_configuration
import capo_firehose.types.splunk_destination_configuration
import capo_firehose.types.tag_delivery_stream_input_tag_list
from capo_firehose._protocol.errors import parse_error_metadata_json
from capo_firehose._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_firehose._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_firehose.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidArgumentException":
            raise capo_firehose.errors.invalid_argument_exception.InvalidArgumentException.from_aws_json_1_1(
                data
            )
        case "InvalidKMSResourceException":
            raise capo_firehose.errors.invalid_kms_resource_exception.InvalidKMSResourceException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            raise capo_firehose.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "ResourceInUseException":
            raise capo_firehose.errors.resource_in_use_exception.ResourceInUseException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_firehose.types.create_delivery_stream_output.CreateDeliveryStreamOutput:
    out: capo_firehose.types.create_delivery_stream_output.CreateDeliveryStreamOutput = capo_firehose.types.create_delivery_stream_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_firehose.types.create_delivery_stream_output.CreateDeliveryStreamOutput:
    out: capo_firehose.types.create_delivery_stream_output.CreateDeliveryStreamOutput = capo_firehose.types.create_delivery_stream_output.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_firehose._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_firehose._auth._sigv4.build_sigv4_auth_scheme(
                "firehose", options.region
            )
        )
        if sigv4_config is not None:
            return capo_firehose._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_firehose.types.create_delivery_stream_input.CreateDeliveryStreamInput,
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
    headers["X-Amz-Target"] = "Firehose_20150804.CreateDeliveryStream"
    body: bytes | None = json.dumps(
        capo_firehose.types.create_delivery_stream_input.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_delivery_stream(
    options: OperationOptions,
    input_: capo_firehose.types.create_delivery_stream_input.CreateDeliveryStreamInput,
) -> tuple[
    capo_firehose.types.create_delivery_stream_output.CreateDeliveryStreamOutput,
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


async def async_create_delivery_stream(
    options: AsyncOperationOptions,
    input_: capo_firehose.types.create_delivery_stream_input.CreateDeliveryStreamInput,
) -> tuple[
    capo_firehose.types.create_delivery_stream_output.CreateDeliveryStreamOutput,
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
