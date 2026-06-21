"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DescribeSecret``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_secrets_manager._auth._signers
import aws_sdk_secrets_manager._auth._sigv4
import aws_sdk_secrets_manager.errors.internal_service_error
import aws_sdk_secrets_manager.errors.invalid_parameter_exception
import aws_sdk_secrets_manager.errors.resource_not_found_exception
import aws_sdk_secrets_manager.types.deleted_date_type
import aws_sdk_secrets_manager.types.describe_secret_request
import aws_sdk_secrets_manager.types.describe_secret_response
import aws_sdk_secrets_manager.types.external_secret_rotation_metadata_type
import aws_sdk_secrets_manager.types.last_accessed_date_type
import aws_sdk_secrets_manager.types.last_changed_date_type
import aws_sdk_secrets_manager.types.last_rotated_date_type
import aws_sdk_secrets_manager.types.next_rotation_date_type
import aws_sdk_secrets_manager.types.replication_status_list_type
import aws_sdk_secrets_manager.types.rotation_rules_type
import aws_sdk_secrets_manager.types.secret_versions_to_stages_map_type
import aws_sdk_secrets_manager.types.tag_list_type
import aws_sdk_secrets_manager.types.timestamp_type
from aws_sdk_secrets_manager._protocol.errors import parse_error_metadata_json
from aws_sdk_secrets_manager._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_secrets_manager.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InternalServiceError":
            raise aws_sdk_secrets_manager.errors.internal_service_error.InternalServiceError.from_aws_json_1_1(
                data
            )
        case "InvalidParameterException":
            raise aws_sdk_secrets_manager.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_secrets_manager.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_secrets_manager.types.describe_secret_response.DescribeSecretResponse:
    out: aws_sdk_secrets_manager.types.describe_secret_response.DescribeSecretResponse = aws_sdk_secrets_manager.types.describe_secret_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_secrets_manager.types.describe_secret_response.DescribeSecretResponse:
    out: aws_sdk_secrets_manager.types.describe_secret_response.DescribeSecretResponse = aws_sdk_secrets_manager.types.describe_secret_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_secrets_manager._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_secrets_manager._auth._sigv4.build_sigv4_auth_scheme(
                "secretsmanager", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_secrets_manager._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_secrets_manager.types.describe_secret_request.DescribeSecretRequest,
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
    headers["X-Amz-Target"] = "secretsmanager.DescribeSecret"
    import aws_sdk_secrets_manager.types.describe_secret_request

    body: bytes | None = json.dumps(
        aws_sdk_secrets_manager.types.describe_secret_request.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def describe_secret(
    options: OperationOptions,
    input_: aws_sdk_secrets_manager.types.describe_secret_request.DescribeSecretRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.describe_secret_response.DescribeSecretResponse,
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


async def async_describe_secret(
    options: AsyncOperationOptions,
    input_: aws_sdk_secrets_manager.types.describe_secret_request.DescribeSecretRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.describe_secret_response.DescribeSecretResponse,
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
