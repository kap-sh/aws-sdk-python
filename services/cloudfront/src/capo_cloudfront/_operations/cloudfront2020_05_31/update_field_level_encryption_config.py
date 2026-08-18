"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateFieldLevelEncryptionConfig``."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_cloudfront._auth._signers
import capo_cloudfront._auth._sigv4
import capo_cloudfront._protocol.eventstream
import capo_cloudfront.errors.access_denied
import capo_cloudfront.errors.illegal_update
import capo_cloudfront.errors.inconsistent_quantities
import capo_cloudfront.errors.invalid_argument
import capo_cloudfront.errors.invalid_if_match_version
import capo_cloudfront.errors.no_such_field_level_encryption_config
import capo_cloudfront.errors.no_such_field_level_encryption_profile
import capo_cloudfront.errors.precondition_failed
import capo_cloudfront.errors.query_arg_profile_empty
import capo_cloudfront.errors.too_many_field_level_encryption_content_type_profiles
import capo_cloudfront.errors.too_many_field_level_encryption_query_arg_profiles
import capo_cloudfront.types.field_level_encryption
import capo_cloudfront.types.field_level_encryption_config
import capo_cloudfront.types.update_field_level_encryption_config_request
import capo_cloudfront.types.update_field_level_encryption_config_result
from capo_cloudfront._protocol.errors import find_error_element, parse_error_metadata
from capo_cloudfront._protocol.xml import Element, fromstring, tostring
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
        case "IllegalUpdate":
            raise capo_cloudfront.errors.illegal_update.IllegalUpdate.from_xml(
                error_el, message
            )
        case "InconsistentQuantities":
            raise capo_cloudfront.errors.inconsistent_quantities.InconsistentQuantities.from_xml(
                error_el, message
            )
        case "InvalidArgument":
            raise capo_cloudfront.errors.invalid_argument.InvalidArgument.from_xml(
                error_el, message
            )
        case "InvalidIfMatchVersion":
            raise capo_cloudfront.errors.invalid_if_match_version.InvalidIfMatchVersion.from_xml(
                error_el, message
            )
        case "NoSuchFieldLevelEncryptionConfig":
            raise capo_cloudfront.errors.no_such_field_level_encryption_config.NoSuchFieldLevelEncryptionConfig.from_xml(
                error_el, message
            )
        case "NoSuchFieldLevelEncryptionProfile":
            raise capo_cloudfront.errors.no_such_field_level_encryption_profile.NoSuchFieldLevelEncryptionProfile.from_xml(
                error_el, message
            )
        case "PreconditionFailed":
            raise capo_cloudfront.errors.precondition_failed.PreconditionFailed.from_xml(
                error_el, message
            )
        case "QueryArgProfileEmpty":
            raise capo_cloudfront.errors.query_arg_profile_empty.QueryArgProfileEmpty.from_xml(
                error_el, message
            )
        case "TooManyFieldLevelEncryptionContentTypeProfiles":
            raise capo_cloudfront.errors.too_many_field_level_encryption_content_type_profiles.TooManyFieldLevelEncryptionContentTypeProfiles.from_xml(
                error_el, message
            )
        case "TooManyFieldLevelEncryptionQueryArgProfiles":
            raise capo_cloudfront.errors.too_many_field_level_encryption_query_arg_profiles.TooManyFieldLevelEncryptionQueryArgProfiles.from_xml(
                error_el, message
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.update_field_level_encryption_config_result.UpdateFieldLevelEncryptionConfigResult:
    out: capo_cloudfront.types.update_field_level_encryption_config_result.UpdateFieldLevelEncryptionConfigResult = {
        "field_level_encryption": capo_cloudfront.types.field_level_encryption.deserialize_xml(
            fromstring(response.read())
        )
    }  # type: ignore[typeddict-item]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_cloudfront.types.update_field_level_encryption_config_result.UpdateFieldLevelEncryptionConfigResult:
    out: capo_cloudfront.types.update_field_level_encryption_config_result.UpdateFieldLevelEncryptionConfigResult = {
        "field_level_encryption": capo_cloudfront.types.field_level_encryption.deserialize_xml(
            fromstring(await response.aread())
        )
    }  # type: ignore[typeddict-item]
    if "ETag" in response.headers:
        out["e_tag"] = response.headers["ETag"]
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
    input_: capo_cloudfront.types.update_field_level_encryption_config_request.UpdateFieldLevelEncryptionConfigRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/2020-05-31/field-level-encryption/{Id}/config"
    url = url.replace("{Id}", quote(input_["id"], safe=""))
    params: list[tuple[str, str]] = []
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    if "if_match" in input_:
        headers["If-Match"] = input_["if_match"]
    payload_root = Element("_")
    capo_cloudfront.types.field_level_encryption_config.serialize_xml(
        input_["field_level_encryption_config"],
        payload_root,
        "FieldLevelEncryptionConfig",
    )
    body: bytes | None = tostring(payload_root[0])
    headers["content-type"] = "application/xml"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    for k, v in params:
        normalized_url.search_params.append(k, v)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def update_field_level_encryption_config(
    options: OperationOptions,
    input_: capo_cloudfront.types.update_field_level_encryption_config_request.UpdateFieldLevelEncryptionConfigRequest,
) -> tuple[
    capo_cloudfront.types.update_field_level_encryption_config_result.UpdateFieldLevelEncryptionConfigResult,
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


async def async_update_field_level_encryption_config(
    options: AsyncOperationOptions,
    input_: capo_cloudfront.types.update_field_level_encryption_config_request.UpdateFieldLevelEncryptionConfigRequest,
) -> tuple[
    capo_cloudfront.types.update_field_level_encryption_config_result.UpdateFieldLevelEncryptionConfigResult,
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
