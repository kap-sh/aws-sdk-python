"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateFunction``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
import aws_sdk_cloudfront.errors.function_already_exists
import aws_sdk_cloudfront.errors.function_size_limit_exceeded
import aws_sdk_cloudfront.errors.invalid_argument
import aws_sdk_cloudfront.errors.too_many_functions
import aws_sdk_cloudfront.errors.unsupported_operation
import aws_sdk_cloudfront.types.create_function_request
import aws_sdk_cloudfront.types.create_function_result
import aws_sdk_cloudfront.types.function_blob
import aws_sdk_cloudfront.types.function_config
import aws_sdk_cloudfront.types.function_summary
import aws_sdk_cloudfront.types.tags
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
        case "FunctionAlreadyExists":
            raise aws_sdk_cloudfront.errors.function_already_exists.FunctionAlreadyExists.from_xml(
                root
            )
        case "FunctionSizeLimitExceeded":
            raise aws_sdk_cloudfront.errors.function_size_limit_exceeded.FunctionSizeLimitExceeded.from_xml(
                root
            )
        case "InvalidArgument":
            raise aws_sdk_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                root
            )
        case "TooManyFunctions":
            raise aws_sdk_cloudfront.errors.too_many_functions.TooManyFunctions.from_xml(
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
) -> aws_sdk_cloudfront.types.create_function_result.CreateFunctionResult:
    out: aws_sdk_cloudfront.types.create_function_result.CreateFunctionResult = {
        "function_summary": aws_sdk_cloudfront.types.function_summary.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = str(response.headers["Location"])
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudfront.types.create_function_result.CreateFunctionResult:
    out: aws_sdk_cloudfront.types.create_function_result.CreateFunctionResult = {
        "function_summary": aws_sdk_cloudfront.types.function_summary.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "Location" in response.headers:
        out["location"] = str(response.headers["Location"])
    if "ETag" in response.headers:
        out["e_tag"] = str(response.headers["ETag"])
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
    input_: aws_sdk_cloudfront.types.create_function_request.CreateFunctionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/function"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    root = Element("CreateFunctionRequest")
    if "name" in input_:
        SubElement(root, "Name").text = str(input_["name"])
    if "function_config" in input_:
        aws_sdk_cloudfront.types.function_config.serialize_xml(
            input_["function_config"], root, "FunctionConfig"
        )
    if "function_code" in input_:
        aws_sdk_cloudfront.types.function_blob.serialize_xml(
            input_["function_code"], root, "FunctionCode"
        )
    if "tags" in input_:
        aws_sdk_cloudfront.types.tags.serialize_xml(input_["tags"], root, "Tags")
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_function(
    options: OperationOptions,
    input_: aws_sdk_cloudfront.types.create_function_request.CreateFunctionRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_function_result.CreateFunctionResult,
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


async def async_create_function(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.create_function_request.CreateFunctionRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_function_result.CreateFunctionResult,
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
