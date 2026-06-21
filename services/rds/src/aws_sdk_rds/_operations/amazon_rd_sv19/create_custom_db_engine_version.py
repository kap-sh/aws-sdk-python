"""Generated from Smithy shape ``com.amazonaws.rds#CreateCustomDBEngineVersion``."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import zapros
from typing_extensions import Never

import aws_sdk_rds._auth._signers
import aws_sdk_rds._auth._sigv4
import aws_sdk_rds.errors.create_custom_db_engine_version_fault
import aws_sdk_rds.errors.custom_db_engine_version_already_exists_fault
import aws_sdk_rds.errors.custom_db_engine_version_not_found_fault
import aws_sdk_rds.errors.custom_db_engine_version_quota_exceeded_fault
import aws_sdk_rds.errors.ec2_image_properties_not_supported_fault
import aws_sdk_rds.errors.invalid_custom_db_engine_version_state_fault
import aws_sdk_rds.errors.kms_key_not_accessible_fault
import aws_sdk_rds.types.ca_certificate_identifiers_list
import aws_sdk_rds.types.character_set
import aws_sdk_rds.types.create_custom_db_engine_version_message
import aws_sdk_rds.types.custom_db_engine_version_ami
import aws_sdk_rds.types.db_engine_version
import aws_sdk_rds.types.engine_mode_list
import aws_sdk_rds.types.feature_name_list
import aws_sdk_rds.types.log_type_list
import aws_sdk_rds.types.serverless_v2_features_support
import aws_sdk_rds.types.string_list
import aws_sdk_rds.types.supported_character_sets_list
import aws_sdk_rds.types.supported_timezones_list
import aws_sdk_rds.types.t_stamp
import aws_sdk_rds.types.tag_list
import aws_sdk_rds.types.valid_upgrade_target_list
from aws_sdk_rds._protocol.errors import parse_error_metadata
from aws_sdk_rds._protocol.xml import fromstring
from aws_sdk_rds._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_rds._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_rds.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    root = fromstring(response.read())
    code, message = parse_error_metadata(root)
    match code:
        case "CreateCustomDBEngineVersionFault":
            raise aws_sdk_rds.errors.create_custom_db_engine_version_fault.CreateCustomDBEngineVersionFault.from_query(
                root
            )
        case "CustomDBEngineVersionAlreadyExistsFault":
            raise aws_sdk_rds.errors.custom_db_engine_version_already_exists_fault.CustomDBEngineVersionAlreadyExistsFault.from_query(
                root
            )
        case "CustomDBEngineVersionNotFoundFault":
            raise aws_sdk_rds.errors.custom_db_engine_version_not_found_fault.CustomDBEngineVersionNotFoundFault.from_query(
                root
            )
        case "CustomDBEngineVersionQuotaExceededFault":
            raise aws_sdk_rds.errors.custom_db_engine_version_quota_exceeded_fault.CustomDBEngineVersionQuotaExceededFault.from_query(
                root
            )
        case "Ec2ImagePropertiesNotSupportedFault":
            raise aws_sdk_rds.errors.ec2_image_properties_not_supported_fault.Ec2ImagePropertiesNotSupportedFault.from_query(
                root
            )
        case "InvalidCustomDBEngineVersionStateFault":
            raise aws_sdk_rds.errors.invalid_custom_db_engine_version_state_fault.InvalidCustomDBEngineVersionStateFault.from_query(
                root
            )
        case "KMSKeyNotAccessibleFault":
            raise aws_sdk_rds.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault.from_query(
                root
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_rds.types.db_engine_version.DBEngineVersion:
    root = fromstring(response.read())
    result = root.find("CreateCustomDBEngineVersionResult")
    out: aws_sdk_rds.types.db_engine_version.DBEngineVersion = (
        aws_sdk_rds.types.db_engine_version.deserialize_query(
            result if result is not None else root
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_rds.types.db_engine_version.DBEngineVersion:
    root = fromstring(await response.aread())
    result = root.find("CreateCustomDBEngineVersionResult")
    out: aws_sdk_rds.types.db_engine_version.DBEngineVersion = (
        aws_sdk_rds.types.db_engine_version.deserialize_query(
            result if result is not None else root
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_rds._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_rds._auth._sigv4.build_sigv4_auth_scheme("rds", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_rds._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_rds.types.create_custom_db_engine_version_message.CreateCustomDBEngineVersionMessage,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    pairs: list[tuple[str, str]] = []
    pairs.append(("Action", "CreateCustomDBEngineVersion"))
    pairs.append(("Version", "2014-10-31"))
    import aws_sdk_rds.types.create_custom_db_engine_version_message

    aws_sdk_rds.types.create_custom_db_engine_version_message.serialize_query(
        input_, pairs, ""
    )
    body: bytes | None = urlencode(pairs).encode()
    headers["content-type"] = "application/x-www-form-urlencoded"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_custom_db_engine_version(
    options: OperationOptions,
    input_: aws_sdk_rds.types.create_custom_db_engine_version_message.CreateCustomDBEngineVersionMessage,
) -> tuple[aws_sdk_rds.types.db_engine_version.DBEngineVersion, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_create_custom_db_engine_version(
    options: AsyncOperationOptions,
    input_: aws_sdk_rds.types.create_custom_db_engine_version_message.CreateCustomDBEngineVersionMessage,
) -> tuple[aws_sdk_rds.types.db_engine_version.DBEngineVersion, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
