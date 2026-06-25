"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateFieldLevelEncryptionProfile``."""

from __future__ import annotations

from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_cloudfront._auth._signers
import aws_sdk_cloudfront._auth._sigv4
import aws_sdk_cloudfront.errors.field_level_encryption_profile_already_exists
import aws_sdk_cloudfront.errors.field_level_encryption_profile_size_exceeded
import aws_sdk_cloudfront.errors.inconsistent_quantities
import aws_sdk_cloudfront.errors.invalid_argument
import aws_sdk_cloudfront.errors.no_such_public_key
import aws_sdk_cloudfront.errors.too_many_field_level_encryption_encryption_entities
import aws_sdk_cloudfront.errors.too_many_field_level_encryption_field_patterns
import aws_sdk_cloudfront.errors.too_many_field_level_encryption_profiles
import aws_sdk_cloudfront.types.create_field_level_encryption_profile_request
import aws_sdk_cloudfront.types.create_field_level_encryption_profile_result
import aws_sdk_cloudfront.types.field_level_encryption_profile
import aws_sdk_cloudfront.types.field_level_encryption_profile_config
from aws_sdk_cloudfront._protocol.errors import parse_error_metadata
from aws_sdk_cloudfront._protocol.xml import Element, fromstring, tostring
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
        case "FieldLevelEncryptionProfileAlreadyExists":
            raise aws_sdk_cloudfront.errors.field_level_encryption_profile_already_exists.FieldLevelEncryptionProfileAlreadyExists.from_xml(
                root
            )
        case "FieldLevelEncryptionProfileSizeExceeded":
            raise aws_sdk_cloudfront.errors.field_level_encryption_profile_size_exceeded.FieldLevelEncryptionProfileSizeExceeded.from_xml(
                root
            )
        case "InconsistentQuantities":
            raise aws_sdk_cloudfront.errors.inconsistent_quantities.InconsistentQuantities.from_xml(
                root
            )
        case "InvalidArgument":
            raise aws_sdk_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                root
            )
        case "NoSuchPublicKey":
            raise aws_sdk_cloudfront.errors.no_such_public_key.NoSuchPublicKey.from_xml(
                root
            )
        case "TooManyFieldLevelEncryptionEncryptionEntities":
            raise aws_sdk_cloudfront.errors.too_many_field_level_encryption_encryption_entities.TooManyFieldLevelEncryptionEncryptionEntities.from_xml(
                root
            )
        case "TooManyFieldLevelEncryptionFieldPatterns":
            raise aws_sdk_cloudfront.errors.too_many_field_level_encryption_field_patterns.TooManyFieldLevelEncryptionFieldPatterns.from_xml(
                root
            )
        case "TooManyFieldLevelEncryptionProfiles":
            raise aws_sdk_cloudfront.errors.too_many_field_level_encryption_profiles.TooManyFieldLevelEncryptionProfiles.from_xml(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_cloudfront.types.create_field_level_encryption_profile_result.CreateFieldLevelEncryptionProfileResult:
    out: aws_sdk_cloudfront.types.create_field_level_encryption_profile_result.CreateFieldLevelEncryptionProfileResult = {
        "field_level_encryption_profile": aws_sdk_cloudfront.types.field_level_encryption_profile.deserialize_xml(
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
) -> aws_sdk_cloudfront.types.create_field_level_encryption_profile_result.CreateFieldLevelEncryptionProfileResult:
    out: aws_sdk_cloudfront.types.create_field_level_encryption_profile_result.CreateFieldLevelEncryptionProfileResult = {
        "field_level_encryption_profile": aws_sdk_cloudfront.types.field_level_encryption_profile.deserialize_xml(
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
    input_: aws_sdk_cloudfront.types.create_field_level_encryption_profile_request.CreateFieldLevelEncryptionProfileRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/field-level-encryption-profile"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "field_level_encryption_profile_config" in input_:
        payload_root = Element("_")
        aws_sdk_cloudfront.types.field_level_encryption_profile_config.serialize_xml(
            input_["field_level_encryption_profile_config"],
            payload_root,
            "FieldLevelEncryptionProfileConfig",
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


def create_field_level_encryption_profile(
    options: OperationOptions,
    input_: aws_sdk_cloudfront.types.create_field_level_encryption_profile_request.CreateFieldLevelEncryptionProfileRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_field_level_encryption_profile_result.CreateFieldLevelEncryptionProfileResult,
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


async def async_create_field_level_encryption_profile(
    options: AsyncOperationOptions,
    input_: aws_sdk_cloudfront.types.create_field_level_encryption_profile_request.CreateFieldLevelEncryptionProfileRequest,
) -> tuple[
    aws_sdk_cloudfront.types.create_field_level_encryption_profile_result.CreateFieldLevelEncryptionProfileResult,
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
