"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateAssetModelCompositeModel``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_iotsitewise._auth._signers
import aws_sdk_iotsitewise._auth._sigv4
import aws_sdk_iotsitewise.errors.conflicting_operation_exception
import aws_sdk_iotsitewise.errors.internal_failure_exception
import aws_sdk_iotsitewise.errors.invalid_request_exception
import aws_sdk_iotsitewise.errors.limit_exceeded_exception
import aws_sdk_iotsitewise.errors.precondition_failed_exception
import aws_sdk_iotsitewise.errors.resource_already_exists_exception
import aws_sdk_iotsitewise.errors.resource_not_found_exception
import aws_sdk_iotsitewise.errors.throttling_exception
import aws_sdk_iotsitewise.types.asset_model_composite_model_path
import aws_sdk_iotsitewise.types.asset_model_property_definitions
import aws_sdk_iotsitewise.types.asset_model_status
import aws_sdk_iotsitewise.types.asset_model_version_type
import aws_sdk_iotsitewise.types.create_asset_model_composite_model_request
import aws_sdk_iotsitewise.types.create_asset_model_composite_model_response
from aws_sdk_iotsitewise._protocol.errors import parse_error_metadata_json
from aws_sdk_iotsitewise._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_iotsitewise._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_iotsitewise.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictingOperationException":
            raise aws_sdk_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException.from_json(
                data
            )
        case "InternalFailureException":
            raise aws_sdk_iotsitewise.errors.internal_failure_exception.InternalFailureException.from_json(
                data
            )
        case "InvalidRequestException":
            raise aws_sdk_iotsitewise.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "LimitExceededException":
            raise aws_sdk_iotsitewise.errors.limit_exceeded_exception.LimitExceededException.from_json(
                data
            )
        case "PreconditionFailedException":
            raise aws_sdk_iotsitewise.errors.precondition_failed_exception.PreconditionFailedException.from_json(
                data
            )
        case "ResourceAlreadyExistsException":
            raise aws_sdk_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_iotsitewise.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_iotsitewise.types.create_asset_model_composite_model_response.CreateAssetModelCompositeModelResponse:
    out: aws_sdk_iotsitewise.types.create_asset_model_composite_model_response.CreateAssetModelCompositeModelResponse = aws_sdk_iotsitewise.types.create_asset_model_composite_model_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_iotsitewise.types.create_asset_model_composite_model_response.CreateAssetModelCompositeModelResponse:
    out: aws_sdk_iotsitewise.types.create_asset_model_composite_model_response.CreateAssetModelCompositeModelResponse = aws_sdk_iotsitewise.types.create_asset_model_composite_model_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_iotsitewise._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_iotsitewise._auth._sigv4.build_sigv4_auth_scheme(
                "iotsitewise", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_iotsitewise._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_iotsitewise.types.create_asset_model_composite_model_request.CreateAssetModelCompositeModelRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/asset-models/{assetModelId}/composite-models"
    url = url.replace("{assetModelId}", quote(str(input_["asset_model_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "if_match" in input_:
        headers["If-Match"] = str(input_["if_match"])
    if "if_none_match" in input_:
        headers["If-None-Match"] = str(input_["if_none_match"])
    if "match_for_version_type" in input_:
        headers["Match-For-Version-Type"] = str(input_["match_for_version_type"])
    body: bytes | None = json.dumps(
        aws_sdk_iotsitewise.types.create_asset_model_composite_model_request.serialize_json(
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


def create_asset_model_composite_model(
    options: OperationOptions,
    input_: aws_sdk_iotsitewise.types.create_asset_model_composite_model_request.CreateAssetModelCompositeModelRequest,
) -> tuple[
    aws_sdk_iotsitewise.types.create_asset_model_composite_model_response.CreateAssetModelCompositeModelResponse,
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


async def async_create_asset_model_composite_model(
    options: AsyncOperationOptions,
    input_: aws_sdk_iotsitewise.types.create_asset_model_composite_model_request.CreateAssetModelCompositeModelRequest,
) -> tuple[
    aws_sdk_iotsitewise.types.create_asset_model_composite_model_response.CreateAssetModelCompositeModelResponse,
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
