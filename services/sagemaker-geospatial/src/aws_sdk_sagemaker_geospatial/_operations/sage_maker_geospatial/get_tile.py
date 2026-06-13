"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetTile``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never, cast
from urllib.parse import quote

import zapros

import aws_sdk_sagemaker_geospatial._auth._signers
import aws_sdk_sagemaker_geospatial._auth._sigv4
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

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.get_tile_input
    import aws_sdk_sagemaker_geospatial.types.get_tile_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_sagemaker_geospatial.errors.access_denied_exception

            raise aws_sdk_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_sagemaker_geospatial.errors.internal_server_exception

            raise aws_sdk_sagemaker_geospatial.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_sagemaker_geospatial.errors.resource_not_found_exception

            raise aws_sdk_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ThrottlingException":
            import aws_sdk_sagemaker_geospatial.errors.throttling_exception

            raise aws_sdk_sagemaker_geospatial.errors.throttling_exception.ThrottlingException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_sagemaker_geospatial.errors.validation_exception

            raise aws_sdk_sagemaker_geospatial.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput:
    _iter = cast(
        Any, response.async_iter_bytes() if is_async else response.iter_bytes()
    )
    out: aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput = {
        "binary_file": _iter
    }
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_sagemaker_geospatial._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input: aws_sdk_sagemaker_geospatial.types.get_tile_input.GetTileInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + "/tile/{z}/{x}/{y}"
    url = url.replace("{x}", quote(str(input["x"]), safe=""))
    url = url.replace("{y}", quote(str(input["y"]), safe=""))
    url = url.replace("{z}", quote(str(input["z"]), safe=""))
    params: dict[str, str] = {}
    if "image_assets" in input:
        params["ImageAssets"] = str(input["image_assets"])
    if "target" in input:
        params["Target"] = str(input["target"])
    if "arn" in input:
        params["Arn"] = str(input["arn"])
    if "image_mask" in input:
        params["ImageMask"] = str(input["image_mask"])
    if "output_format" in input:
        params["OutputFormat"] = str(input["output_format"])
    if "time_range_filter" in input:
        params["TimeRangeFilter"] = str(input["time_range_filter"])
    if "property_filters" in input:
        params["PropertyFilters"] = str(input["property_filters"])
    if "output_data_type" in input:
        params["OutputDataType"] = str(input["output_data_type"])
    if "execution_role_arn" in input:
        params["ExecutionRoleArn"] = str(input["execution_role_arn"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "GET",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def get_tile(
    options: OperationOptions,
    input: aws_sdk_sagemaker_geospatial.types.get_tile_input.GetTileInput,
) -> tuple[
    aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput, zapros.Response
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


async def async_get_tile(
    options: AsyncOperationOptions,
    input: aws_sdk_sagemaker_geospatial.types.get_tile_input.GetTileInput,
) -> tuple[
    aws_sdk_sagemaker_geospatial.types.get_tile_output.GetTileOutput, zapros.Response
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
