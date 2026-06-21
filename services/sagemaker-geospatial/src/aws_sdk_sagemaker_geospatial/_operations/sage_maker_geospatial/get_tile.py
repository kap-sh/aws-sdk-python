"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetTile``."""

from __future__ import annotations

import json
from typing import Any, cast
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_sagemaker_geospatial._auth._signers
import aws_sdk_sagemaker_geospatial._auth._sigv4
import aws_sdk_sagemaker_geospatial.errors.access_denied_exception
import aws_sdk_sagemaker_geospatial.errors.internal_server_exception
import aws_sdk_sagemaker_geospatial.errors.resource_not_found_exception
import aws_sdk_sagemaker_geospatial.errors.throttling_exception
import aws_sdk_sagemaker_geospatial.errors.validation_exception
import aws_sdk_sagemaker_geospatial.types.binary_file
import aws_sdk_sagemaker_geospatial.types.get_tile_input
import aws_sdk_sagemaker_geospatial.types.get_tile_output
import aws_sdk_sagemaker_geospatial.types.string_list_input
from aws_sdk_sagemaker_geospatial._protocol.errors import parse_error_metadata_json
from aws_sdk_sagemaker_geospatial._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_sagemaker_geospatial._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_sagemaker_geospatial.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise aws_sdk_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_sagemaker_geospatial.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            raise aws_sdk_sagemaker_geospatial.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_sagemaker_geospatial.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput:
    _iter = cast(Any, response.iter_bytes())
    out: aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput = {
        "binary_file": _iter
    }  # type: ignore[reportAssignmentType]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput:
    _iter = cast(Any, response.async_iter_bytes())
    out: aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput = {
        "binary_file": _iter
    }  # type: ignore[reportAssignmentType]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sagemaker_geospatial._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_sagemaker_geospatial._auth._sigv4.build_sigv4_auth_scheme(
                "sagemaker-geospatial", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_sagemaker_geospatial._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_sagemaker_geospatial.types.get_tile_input.GetTileInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/tile/{z}/{x}/{y}"
    url = url.replace("{x}", quote(str(input_["x"]), safe=""))
    url = url.replace("{y}", quote(str(input_["y"]), safe=""))
    url = url.replace("{z}", quote(str(input_["z"]), safe=""))
    params: dict[str, str] = {}
    if "image_assets" in input_:
        params["ImageAssets"] = str(input_["image_assets"])
    if "target" in input_:
        params["Target"] = str(input_["target"])
    if "arn" in input_:
        params["Arn"] = str(input_["arn"])
    if "image_mask" in input_:
        params["ImageMask"] = str(input_["image_mask"])
    if "output_format" in input_:
        params["OutputFormat"] = str(input_["output_format"])
    if "time_range_filter" in input_:
        params["TimeRangeFilter"] = str(input_["time_range_filter"])
    if "property_filters" in input_:
        params["PropertyFilters"] = str(input_["property_filters"])
    if "output_data_type" in input_:
        params["OutputDataType"] = str(input_["output_data_type"])
    if "execution_role_arn" in input_:
        params["ExecutionRoleArn"] = str(input_["execution_role_arn"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def get_tile(
    options: OperationOptions,
    input_: aws_sdk_sagemaker_geospatial.types.get_tile_input.GetTileInput,
) -> tuple[
    aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput, zapros.Response
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


async def async_get_tile(
    options: AsyncOperationOptions,
    input_: aws_sdk_sagemaker_geospatial.types.get_tile_input.GetTileInput,
) -> tuple[
    aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput, zapros.Response
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
