"""Generated from Smithy shape ``com.amazonaws.kinesis#RemoveTagsFromStream``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_kinesis._auth._signers
import capo_kinesis._auth._sigv4
import capo_kinesis.errors.access_denied_exception
import capo_kinesis.errors.invalid_argument_exception
import capo_kinesis.errors.limit_exceeded_exception
import capo_kinesis.errors.resource_in_use_exception
import capo_kinesis.errors.resource_not_found_exception
import capo_kinesis.types.remove_tags_from_stream_input
import capo_kinesis.types.tag_key_list
from capo_kinesis._protocol.errors import parse_error_metadata_json
from capo_kinesis._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_kinesis._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_kinesis.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_kinesis.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_1(
                data
            )
        case "InvalidArgumentException":
            raise capo_kinesis.errors.invalid_argument_exception.InvalidArgumentException.from_aws_json_1_1(
                data
            )
        case "LimitExceededException":
            raise capo_kinesis.errors.limit_exceeded_exception.LimitExceededException.from_aws_json_1_1(
                data
            )
        case "ResourceInUseException":
            raise capo_kinesis.errors.resource_in_use_exception.ResourceInUseException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise capo_kinesis.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_kinesis._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_kinesis._auth._sigv4.build_sigv4_auth_scheme(
                "kinesis", options.region
            )
        )
        if sigv4_config is not None:
            return capo_kinesis._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_kinesis.types.remove_tags_from_stream_input.RemoveTagsFromStreamInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            StreamId=input_.get("stream_id"),
            StreamARN=input_.get("stream_arn"),
            OperationType="control",
            ConsumerARN=options.consumer_arn,
            ResourceARN=options.resource_arn,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "Kinesis_20131202.RemoveTagsFromStream"
    body: bytes | None = json.dumps(
        capo_kinesis.types.remove_tags_from_stream_input.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def remove_tags_from_stream(
    options: OperationOptions,
    input_: capo_kinesis.types.remove_tags_from_stream_input.RemoveTagsFromStreamInput,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_remove_tags_from_stream(
    options: AsyncOperationOptions,
    input_: capo_kinesis.types.remove_tags_from_stream_input.RemoveTagsFromStreamInput,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
