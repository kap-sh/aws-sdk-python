"""Generated from Smithy shape ``com.amazonaws.codecommit#PostCommentForComparedCommit``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_codecommit._auth._signers
import aws_sdk_codecommit._auth._sigv4
import aws_sdk_codecommit.errors.before_commit_id_and_after_commit_id_are_same_exception
import aws_sdk_codecommit.errors.client_request_token_required_exception
import aws_sdk_codecommit.errors.comment_content_required_exception
import aws_sdk_codecommit.errors.comment_content_size_limit_exceeded_exception
import aws_sdk_codecommit.errors.commit_does_not_exist_exception
import aws_sdk_codecommit.errors.commit_id_required_exception
import aws_sdk_codecommit.errors.encryption_integrity_checks_failed_exception
import aws_sdk_codecommit.errors.encryption_key_access_denied_exception
import aws_sdk_codecommit.errors.encryption_key_disabled_exception
import aws_sdk_codecommit.errors.encryption_key_not_found_exception
import aws_sdk_codecommit.errors.encryption_key_unavailable_exception
import aws_sdk_codecommit.errors.idempotency_parameter_mismatch_exception
import aws_sdk_codecommit.errors.invalid_client_request_token_exception
import aws_sdk_codecommit.errors.invalid_commit_id_exception
import aws_sdk_codecommit.errors.invalid_file_location_exception
import aws_sdk_codecommit.errors.invalid_file_position_exception
import aws_sdk_codecommit.errors.invalid_path_exception
import aws_sdk_codecommit.errors.invalid_relative_file_version_enum_exception
import aws_sdk_codecommit.errors.invalid_repository_name_exception
import aws_sdk_codecommit.errors.path_does_not_exist_exception
import aws_sdk_codecommit.errors.path_required_exception
import aws_sdk_codecommit.errors.repository_does_not_exist_exception
import aws_sdk_codecommit.errors.repository_name_required_exception
import aws_sdk_codecommit.types.comment
import aws_sdk_codecommit.types.location
import aws_sdk_codecommit.types.post_comment_for_compared_commit_input
import aws_sdk_codecommit.types.post_comment_for_compared_commit_output
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
        case "BeforeCommitIdAndAfterCommitIdAreSameException":
            raise aws_sdk_codecommit.errors.before_commit_id_and_after_commit_id_are_same_exception.BeforeCommitIdAndAfterCommitIdAreSameException.from_aws_json_1_1(
                data
            )
        case "ClientRequestTokenRequiredException":
            raise aws_sdk_codecommit.errors.client_request_token_required_exception.ClientRequestTokenRequiredException.from_aws_json_1_1(
                data
            )
        case "CommentContentRequiredException":
            raise aws_sdk_codecommit.errors.comment_content_required_exception.CommentContentRequiredException.from_aws_json_1_1(
                data
            )
        case "CommentContentSizeLimitExceededException":
            raise aws_sdk_codecommit.errors.comment_content_size_limit_exceeded_exception.CommentContentSizeLimitExceededException.from_aws_json_1_1(
                data
            )
        case "CommitDoesNotExistException":
            raise aws_sdk_codecommit.errors.commit_does_not_exist_exception.CommitDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "CommitIdRequiredException":
            raise aws_sdk_codecommit.errors.commit_id_required_exception.CommitIdRequiredException.from_aws_json_1_1(
                data
            )
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
        case "EncryptionKeyNotFoundException":
            raise aws_sdk_codecommit.errors.encryption_key_not_found_exception.EncryptionKeyNotFoundException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyUnavailableException":
            raise aws_sdk_codecommit.errors.encryption_key_unavailable_exception.EncryptionKeyUnavailableException.from_aws_json_1_1(
                data
            )
        case "IdempotencyParameterMismatchException":
            raise aws_sdk_codecommit.errors.idempotency_parameter_mismatch_exception.IdempotencyParameterMismatchException.from_aws_json_1_1(
                data
            )
        case "InvalidClientRequestTokenException":
            raise aws_sdk_codecommit.errors.invalid_client_request_token_exception.InvalidClientRequestTokenException.from_aws_json_1_1(
                data
            )
        case "InvalidCommitIdException":
            raise aws_sdk_codecommit.errors.invalid_commit_id_exception.InvalidCommitIdException.from_aws_json_1_1(
                data
            )
        case "InvalidFileLocationException":
            raise aws_sdk_codecommit.errors.invalid_file_location_exception.InvalidFileLocationException.from_aws_json_1_1(
                data
            )
        case "InvalidFilePositionException":
            raise aws_sdk_codecommit.errors.invalid_file_position_exception.InvalidFilePositionException.from_aws_json_1_1(
                data
            )
        case "InvalidPathException":
            raise aws_sdk_codecommit.errors.invalid_path_exception.InvalidPathException.from_aws_json_1_1(
                data
            )
        case "InvalidRelativeFileVersionEnumException":
            raise aws_sdk_codecommit.errors.invalid_relative_file_version_enum_exception.InvalidRelativeFileVersionEnumException.from_aws_json_1_1(
                data
            )
        case "InvalidRepositoryNameException":
            raise aws_sdk_codecommit.errors.invalid_repository_name_exception.InvalidRepositoryNameException.from_aws_json_1_1(
                data
            )
        case "PathDoesNotExistException":
            raise aws_sdk_codecommit.errors.path_does_not_exist_exception.PathDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "PathRequiredException":
            raise aws_sdk_codecommit.errors.path_required_exception.PathRequiredException.from_aws_json_1_1(
                data
            )
        case "RepositoryDoesNotExistException":
            raise aws_sdk_codecommit.errors.repository_does_not_exist_exception.RepositoryDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "RepositoryNameRequiredException":
            raise aws_sdk_codecommit.errors.repository_name_required_exception.RepositoryNameRequiredException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_codecommit.types.post_comment_for_compared_commit_output.PostCommentForComparedCommitOutput:
    out: aws_sdk_codecommit.types.post_comment_for_compared_commit_output.PostCommentForComparedCommitOutput = aws_sdk_codecommit.types.post_comment_for_compared_commit_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_codecommit.types.post_comment_for_compared_commit_output.PostCommentForComparedCommitOutput:
    out: aws_sdk_codecommit.types.post_comment_for_compared_commit_output.PostCommentForComparedCommitOutput = aws_sdk_codecommit.types.post_comment_for_compared_commit_output.deserialize_aws_json_1_1(
        json.loads(await response.aread())
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
    input_: aws_sdk_codecommit.types.post_comment_for_compared_commit_input.PostCommentForComparedCommitInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.PostCommentForComparedCommit"
    import aws_sdk_codecommit.types.post_comment_for_compared_commit_input

    body: bytes | None = json.dumps(
        aws_sdk_codecommit.types.post_comment_for_compared_commit_input.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def post_comment_for_compared_commit(
    options: OperationOptions,
    input_: aws_sdk_codecommit.types.post_comment_for_compared_commit_input.PostCommentForComparedCommitInput,
) -> tuple[
    aws_sdk_codecommit.types.post_comment_for_compared_commit_output.PostCommentForComparedCommitOutput,
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


async def async_post_comment_for_compared_commit(
    options: AsyncOperationOptions,
    input_: aws_sdk_codecommit.types.post_comment_for_compared_commit_input.PostCommentForComparedCommitInput,
) -> tuple[
    aws_sdk_codecommit.types.post_comment_for_compared_commit_output.PostCommentForComparedCommitOutput,
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
