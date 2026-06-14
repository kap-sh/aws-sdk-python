"""Generated from Smithy shape ``com.amazonaws.appmesh#DescribeVirtualService``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never
from urllib.parse import quote

import zapros

import aws_sdk_app_mesh._auth._signers
import aws_sdk_app_mesh._auth._sigv4
from aws_sdk_app_mesh._protocol.errors import parse_error_metadata_json
from aws_sdk_app_mesh._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_app_mesh._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_app_mesh.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.describe_virtual_service_input
    import aws_sdk_app_mesh.types.describe_virtual_service_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequestException":
            import aws_sdk_app_mesh.errors.bad_request_exception

            raise aws_sdk_app_mesh.errors.bad_request_exception.BadRequestException.from_json(
                data
            )
        case "ForbiddenException":
            import aws_sdk_app_mesh.errors.forbidden_exception

            raise aws_sdk_app_mesh.errors.forbidden_exception.ForbiddenException.from_json(
                data
            )
        case "InternalServerErrorException":
            import aws_sdk_app_mesh.errors.internal_server_error_exception

            raise aws_sdk_app_mesh.errors.internal_server_error_exception.InternalServerErrorException.from_json(
                data
            )
        case "NotFoundException":
            import aws_sdk_app_mesh.errors.not_found_exception

            raise aws_sdk_app_mesh.errors.not_found_exception.NotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            import aws_sdk_app_mesh.errors.service_unavailable_exception

            raise aws_sdk_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case "TooManyRequestsException":
            import aws_sdk_app_mesh.errors.too_many_requests_exception

            raise aws_sdk_app_mesh.errors.too_many_requests_exception.TooManyRequestsException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> (
    aws_sdk_app_mesh.types.describe_virtual_service_output.DescribeVirtualServiceOutput
):
    import aws_sdk_app_mesh.types.virtual_service_data

    out: aws_sdk_app_mesh.types.describe_virtual_service_output.DescribeVirtualServiceOutput = {
        "virtual_service": aws_sdk_app_mesh.types.virtual_service_data.deserialize_json(
            json.loads(response.read())
        )
    }  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_app_mesh._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_app_mesh._auth._sigv4.build_sigv4_auth_scheme(
                "appmesh", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_app_mesh._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_app_mesh.types.describe_virtual_service_input.DescribeVirtualServiceInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/v20190125/meshes/{meshName}/virtualServices/{virtualServiceName}"
    )
    url = url.replace(
        "{virtualServiceName}", quote(str(input_["virtual_service_name"]), safe="")
    )
    url = url.replace("{meshName}", quote(str(input_["mesh_name"]), safe=""))
    params: dict[str, str] = {}
    if "mesh_owner" in input_:
        params["meshOwner"] = str(input_["mesh_owner"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def describe_virtual_service(
    options: OperationOptions,
    input_: aws_sdk_app_mesh.types.describe_virtual_service_input.DescribeVirtualServiceInput,
) -> tuple[
    aws_sdk_app_mesh.types.describe_virtual_service_output.DescribeVirtualServiceOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        response.read()
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_describe_virtual_service(
    options: AsyncOperationOptions,
    input_: aws_sdk_app_mesh.types.describe_virtual_service_input.DescribeVirtualServiceInput,
) -> tuple[
    aws_sdk_app_mesh.types.describe_virtual_service_output.DescribeVirtualServiceOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        await response.aread()
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
