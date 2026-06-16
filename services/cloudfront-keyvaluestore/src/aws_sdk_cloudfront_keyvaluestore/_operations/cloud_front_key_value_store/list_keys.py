"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#ListKeys``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import Never

import aws_sdk_cloudfront_keyvaluestore._auth._signers
import aws_sdk_cloudfront_keyvaluestore._auth._sigv4
from aws_sdk_cloudfront_keyvaluestore._protocol.errors import parse_error_metadata_json
from aws_sdk_cloudfront_keyvaluestore._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_cloudfront_keyvaluestore._rule_engine._endpoint_runtime import apply_label
from aws_sdk_cloudfront_keyvaluestore._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudfront_keyvaluestore.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront_keyvaluestore.types.list_keys_request
    import aws_sdk_cloudfront_keyvaluestore.types.list_keys_response


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            import aws_sdk_cloudfront_keyvaluestore.errors.access_denied_exception

            raise aws_sdk_cloudfront_keyvaluestore.errors.access_denied_exception.AccessDeniedException.from_json(
                data
            )
        case "ConflictException":
            import aws_sdk_cloudfront_keyvaluestore.errors.conflict_exception

            raise aws_sdk_cloudfront_keyvaluestore.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            import aws_sdk_cloudfront_keyvaluestore.errors.internal_server_exception

            raise aws_sdk_cloudfront_keyvaluestore.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            import aws_sdk_cloudfront_keyvaluestore.errors.resource_not_found_exception

            raise aws_sdk_cloudfront_keyvaluestore.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ValidationException":
            import aws_sdk_cloudfront_keyvaluestore.errors.validation_exception

            raise aws_sdk_cloudfront_keyvaluestore.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudfront_keyvaluestore.types.list_keys_response.ListKeysResponse:
    import aws_sdk_cloudfront_keyvaluestore.types.list_keys_response

    out: aws_sdk_cloudfront_keyvaluestore.types.list_keys_response.ListKeysResponse = (
        aws_sdk_cloudfront_keyvaluestore.types.list_keys_response.deserialize_json(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_cloudfront_keyvaluestore._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_cloudfront_keyvaluestore._auth._sigv4.build_sigv4_auth_scheme(
                "cloudfront-keyvaluestore", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_cloudfront_keyvaluestore._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_cloudfront_keyvaluestore.types.list_keys_request.ListKeysRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            KvsARN=input_.get("kvs_arn"),
            Region=options.region,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/key-value-stores/{KvsARN}/keys"
    url = apply_label(url, "{KvsARN}", str(input_["kvs_arn"]))
    params: dict[str, str] = {}
    if "next_token" in input_:
        params["NextToken"] = str(input_["next_token"])
    params["MaxResults"] = str(input_.get("max_results", 10))
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "GET", headers=headers, body=body, context={"signer": signer}
    )


def list_keys(
    options: OperationOptions,
    input_: aws_sdk_cloudfront_keyvaluestore.types.list_keys_request.ListKeysRequest,
) -> tuple[
    aws_sdk_cloudfront_keyvaluestore.types.list_keys_response.ListKeysResponse,
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


async def async_list_keys(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront_keyvaluestore.types.list_keys_request.ListKeysRequest,
) -> tuple[
    aws_sdk_cloudfront_keyvaluestore.types.list_keys_response.ListKeysResponse,
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
