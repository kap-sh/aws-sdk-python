"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateRepository``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_codecommit._auth._signers
import aws_sdk_codecommit._auth._sigv4
import aws_sdk_codecommit.errors.encryption_integrity_checks_failed_exception
import aws_sdk_codecommit.errors.encryption_key_access_denied_exception
import aws_sdk_codecommit.errors.encryption_key_disabled_exception
import aws_sdk_codecommit.errors.encryption_key_invalid_id_exception
import aws_sdk_codecommit.errors.encryption_key_invalid_usage_exception
import aws_sdk_codecommit.errors.encryption_key_not_found_exception
import aws_sdk_codecommit.errors.encryption_key_unavailable_exception
import aws_sdk_codecommit.errors.invalid_repository_description_exception
import aws_sdk_codecommit.errors.invalid_repository_name_exception
import aws_sdk_codecommit.errors.invalid_system_tag_usage_exception
import aws_sdk_codecommit.errors.invalid_tags_map_exception
import aws_sdk_codecommit.errors.operation_not_allowed_exception
import aws_sdk_codecommit.errors.repository_limit_exceeded_exception
import aws_sdk_codecommit.errors.repository_name_exists_exception
import aws_sdk_codecommit.errors.repository_name_required_exception
import aws_sdk_codecommit.errors.tag_policy_exception
import aws_sdk_codecommit.errors.too_many_tags_exception
import aws_sdk_codecommit.types.create_repository_input
import aws_sdk_codecommit.types.create_repository_output
import aws_sdk_codecommit.types.repository_metadata
import aws_sdk_codecommit.types.tags_map
from aws_sdk_codecommit._protocol.errors import parse_error_metadata_json
from aws_sdk_codecommit._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codecommit._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codecommit.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "EncryptionIntegrityChecksFailedException":
            raise aws_sdk_codecommit.errors.encryption_integrity_checks_failed_exception.EncryptionIntegrityChecksFailedException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyAccessDeniedException":
            raise aws_sdk_codecommit.errors.encryption_key_access_denied_exception.EncryptionKeyAccessDeniedException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyDisabledException":
            raise aws_sdk_codecommit.errors.encryption_key_disabled_exception.EncryptionKeyDisabledException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyInvalidIdException":
            raise aws_sdk_codecommit.errors.encryption_key_invalid_id_exception.EncryptionKeyInvalidIdException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyInvalidUsageException":
            raise aws_sdk_codecommit.errors.encryption_key_invalid_usage_exception.EncryptionKeyInvalidUsageException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyNotFoundException":
            raise aws_sdk_codecommit.errors.encryption_key_not_found_exception.EncryptionKeyNotFoundException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyUnavailableException":
            raise aws_sdk_codecommit.errors.encryption_key_unavailable_exception.EncryptionKeyUnavailableException.from_aws_json_1_1(
                data
            )
        case "InvalidRepositoryDescriptionException":
            raise aws_sdk_codecommit.errors.invalid_repository_description_exception.InvalidRepositoryDescriptionException.from_aws_json_1_1(
                data
            )
        case "InvalidRepositoryNameException":
            raise aws_sdk_codecommit.errors.invalid_repository_name_exception.InvalidRepositoryNameException.from_aws_json_1_1(
                data
            )
        case "InvalidSystemTagUsageException":
            raise aws_sdk_codecommit.errors.invalid_system_tag_usage_exception.InvalidSystemTagUsageException.from_aws_json_1_1(
                data
            )
        case "InvalidTagsMapException":
            raise aws_sdk_codecommit.errors.invalid_tags_map_exception.InvalidTagsMapException.from_aws_json_1_1(
                data
            )
        case "OperationNotAllowedException":
            raise aws_sdk_codecommit.errors.operation_not_allowed_exception.OperationNotAllowedException.from_aws_json_1_1(
                data
            )
        case "RepositoryLimitExceededException":
            raise aws_sdk_codecommit.errors.repository_limit_exceeded_exception.RepositoryLimitExceededException.from_aws_json_1_1(
                data
            )
        case "RepositoryNameExistsException":
            raise aws_sdk_codecommit.errors.repository_name_exists_exception.RepositoryNameExistsException.from_aws_json_1_1(
                data
            )
        case "RepositoryNameRequiredException":
            raise aws_sdk_codecommit.errors.repository_name_required_exception.RepositoryNameRequiredException.from_aws_json_1_1(
                data
            )
        case "TagPolicyException":
            raise aws_sdk_codecommit.errors.tag_policy_exception.TagPolicyException.from_aws_json_1_1(
                data
            )
        case "TooManyTagsException":
            raise aws_sdk_codecommit.errors.too_many_tags_exception.TooManyTagsException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_codecommit.types.create_repository_output.CreateRepositoryOutput:
    out: aws_sdk_codecommit.types.create_repository_output.CreateRepositoryOutput = (
        aws_sdk_codecommit.types.create_repository_output.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_codecommit.types.create_repository_output.CreateRepositoryOutput:
    out: aws_sdk_codecommit.types.create_repository_output.CreateRepositoryOutput = (
        aws_sdk_codecommit.types.create_repository_output.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codecommit._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_codecommit._auth._sigv4.build_sigv4_auth_scheme(
                "codecommit", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_codecommit._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_codecommit.types.create_repository_input.CreateRepositoryInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.CreateRepository"
    import aws_sdk_codecommit.types.create_repository_input

    body: bytes | None = json.dumps(
        aws_sdk_codecommit.types.create_repository_input.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_repository(
    options: OperationOptions,
    input_: aws_sdk_codecommit.types.create_repository_input.CreateRepositoryInput,
) -> tuple[
    aws_sdk_codecommit.types.create_repository_output.CreateRepositoryOutput,
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


async def async_create_repository(
    options: AsyncOperationOptions,
    input_: aws_sdk_codecommit.types.create_repository_input.CreateRepositoryInput,
) -> tuple[
    aws_sdk_codecommit.types.create_repository_output.CreateRepositoryOutput,
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
