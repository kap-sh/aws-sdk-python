"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateKeyGroup``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
from aws_sdk_cloudfront._protocol.errors import parse_error_metadata
from aws_sdk_cloudfront._protocol.xml import Element, fromstring, tostring
from aws_sdk_cloudfront._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_cloudfront._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_cloudfront.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.create_key_group_request
    import aws_sdk_cloudfront.types.create_key_group_result


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "InvalidArgument":
            import aws_sdk_cloudfront.errors.invalid_argument

            raise aws_sdk_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                root
            )
        case "KeyGroupAlreadyExists":
            import aws_sdk_cloudfront.errors.key_group_already_exists

            raise aws_sdk_cloudfront.errors.key_group_already_exists.KeyGroupAlreadyExists.from_xml(
                root
            )
        case "TooManyKeyGroups":
            import aws_sdk_cloudfront.errors.too_many_key_groups

            raise aws_sdk_cloudfront.errors.too_many_key_groups.TooManyKeyGroups.from_xml(
                root
            )
        case "TooManyPublicKeysInKeyGroup":
            import aws_sdk_cloudfront.errors.too_many_public_keys_in_key_group

            raise aws_sdk_cloudfront.errors.too_many_public_keys_in_key_group.TooManyPublicKeysInKeyGroup.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_cloudfront.types.create_key_group_result.CreateKeyGroupResult:
    import aws_sdk_cloudfront.types.key_group

    out: aws_sdk_cloudfront.types.create_key_group_result.CreateKeyGroupResult = {
        "key_group": aws_sdk_cloudfront.types.key_group.deserialize_xml(
            fromstring(response.read())
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
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input_: aws_sdk_cloudfront.types.create_key_group_request.CreateKeyGroupRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/key-group"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "key_group_config" in input_:
        import aws_sdk_cloudfront.types.key_group_config

        payload_root = Element("_")
        aws_sdk_cloudfront.types.key_group_config.serialize_xml(
            input_["key_group_config"], payload_root, "KeyGroupConfig"
        )
        body: bytes | None = tostring(payload_root[0])
        headers["content-type"] = "application/xml"
    else:
        body = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_key_group(
    options: OperationOptions,
    input_: aws_sdk_cloudfront.types.create_key_group_request.CreateKeyGroupRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_key_group_result.CreateKeyGroupResult,
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


async def async_create_key_group(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.create_key_group_request.CreateKeyGroupRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_key_group_result.CreateKeyGroupResult,
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
