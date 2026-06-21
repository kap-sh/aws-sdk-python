"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListConnectionFunctions``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
import aws_sdk_cloudfront.errors.access_denied
import aws_sdk_cloudfront.errors.invalid_argument
import aws_sdk_cloudfront.errors.unsupported_operation
import aws_sdk_cloudfront.types.connection_function_summary_list
import aws_sdk_cloudfront.types.function_stage
import aws_sdk_cloudfront.types.list_connection_functions_request
import aws_sdk_cloudfront.types.list_connection_functions_result
from aws_sdk_cloudfront._protocol.errors import parse_error_metadata
from aws_sdk_cloudfront._protocol.xml import Element, SubElement, fromstring, tostring
from aws_sdk_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudfront.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "AccessDenied":
            raise aws_sdk_cloudfront.errors.access_denied.AccessDenied.from_xml(root)
        case "InvalidArgument":
            raise aws_sdk_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                root
            )
        case "UnsupportedOperation":
            raise aws_sdk_cloudfront.errors.unsupported_operation.UnsupportedOperation.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudfront.types.list_connection_functions_result.ListConnectionFunctionsResult:
    out: aws_sdk_cloudfront.types.list_connection_functions_result.ListConnectionFunctionsResult = aws_sdk_cloudfront.types.list_connection_functions_result.deserialize_xml(
        fromstring(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudfront.types.list_connection_functions_result.ListConnectionFunctionsResult:
    out: aws_sdk_cloudfront.types.list_connection_functions_result.ListConnectionFunctionsResult = aws_sdk_cloudfront.types.list_connection_functions_result.deserialize_xml(
        fromstring(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudfront._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudfront._auth._sigv4.build_sigv4_auth_scheme(
                "cloudfront", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudfront._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.list_connection_functions_request.ListConnectionFunctionsRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/connection-functions"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("ListConnectionFunctionsRequest")
    if "marker" in input_:
        SubElement(root, "Marker").text = str(input_["marker"])
    if "max_items" in input_:
        SubElement(root, "MaxItems").text = str(input_["max_items"])
    if "stage" in input_:
        import aws_sdk_cloudfront.types.function_stage

        aws_sdk_cloudfront.types.function_stage.serialize_xml(
            input_["stage"], root, "Stage"
        )
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def list_connection_functions(
    options: OperationOptions,
    input_: aws_sdk_cloudfront.types.list_connection_functions_request.ListConnectionFunctionsRequest,
) -> tuple[
    aws_sdk_cloudfront.types.list_connection_functions_result.ListConnectionFunctionsResult,
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


async def async_list_connection_functions(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.list_connection_functions_request.ListConnectionFunctionsRequest,
) -> tuple[
    aws_sdk_cloudfront.types.list_connection_functions_result.ListConnectionFunctionsResult,
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
