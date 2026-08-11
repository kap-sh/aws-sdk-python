"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateKeyValueStore``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import capo_cloudfront._auth._signers
import capo_cloudfront._auth._sigv4
import capo_cloudfront.errors.access_denied
import capo_cloudfront.errors.entity_already_exists
import capo_cloudfront.errors.entity_limit_exceeded
import capo_cloudfront.errors.entity_size_limit_exceeded
import capo_cloudfront.errors.invalid_argument
import capo_cloudfront.errors.unsupported_operation
import capo_cloudfront.types.create_key_value_store_request
import capo_cloudfront.types.create_key_value_store_result
import capo_cloudfront.types.import_source
import capo_cloudfront.types.key_value_store
import capo_cloudfront.types.tags
from capo_cloudfront._protocol.errors import find_error_element, parse_error_metadata
from capo_cloudfront._protocol.xml import Element, SubElement, fromstring, tostring
from capo_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_cloudfront._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_cloudfront.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    error_el = find_error_element(root)
    match code:
        case "AccessDenied":
            raise capo_cloudfront.errors.access_denied.AccessDenied.from_xml(
                error_el, message
            )
        case "EntityAlreadyExists":
            raise capo_cloudfront.errors.entity_already_exists.EntityAlreadyExists.from_xml(
                error_el, message
            )
        case "EntityLimitExceeded":
            raise capo_cloudfront.errors.entity_limit_exceeded.EntityLimitExceeded.from_xml(
                error_el, message
            )
        case "EntitySizeLimitExceeded":
            raise capo_cloudfront.errors.entity_size_limit_exceeded.EntitySizeLimitExceeded.from_xml(
                error_el, message
            )
        case "InvalidArgument":
            raise capo_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                error_el, message
            )
        case "UnsupportedOperation":
            raise capo_cloudfront.errors.unsupported_operation.UnsupportedOperation.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.create_key_value_store_result.CreateKeyValueStoreResult:
    out: capo_cloudfront.types.create_key_value_store_result.CreateKeyValueStoreResult = {
        "key_value_store": capo_cloudfront.types.key_value_store.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.create_key_value_store_result.CreateKeyValueStoreResult:
    out: capo_cloudfront.types.create_key_value_store_result.CreateKeyValueStoreResult = {
        "key_value_store": capo_cloudfront.types.key_value_store.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    if "Location" in response.headers:
        out["location"] = response.headers["Location"]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_cloudfront._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_cloudfront._auth._sigv4.build_sigv4_auth_scheme(
                "cloudfront", options.region
            )
        )
        if sigv4_config is not None:
            return capo_cloudfront._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_cloudfront.types.create_key_value_store_request.CreateKeyValueStoreRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/key-value-store"
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    import capo_cloudfront.types.import_source
    import capo_cloudfront.types.tags

    root = Element("CreateKeyValueStoreRequest")
    if "name" in input_:
        SubElement(root, "Name").text = input_["name"]
    if "comment" in input_:
        SubElement(root, "Comment").text = input_["comment"]
    if "import_source" in input_:
        capo_cloudfront.types.import_source.serialize_xml(
            input_["import_source"], root, "ImportSource"
        )
    if "tags" in input_:
        capo_cloudfront.types.tags.serialize_xml(input_["tags"], root, "Tags")
    body: bytes | None = tostring(root)
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_key_value_store(
    options: OperationOptions,
    input_: capo_cloudfront.types.create_key_value_store_request.CreateKeyValueStoreRequest,
) -> tuple[
    capo_cloudfront.types.create_key_value_store_result.CreateKeyValueStoreResult,
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


async def async_create_key_value_store(
    options: AsyncOperationOptions,
    input_: capo_cloudfront.types.create_key_value_store_request.CreateKeyValueStoreRequest,
) -> tuple[
    capo_cloudfront.types.create_key_value_store_result.CreateKeyValueStoreResult,
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
