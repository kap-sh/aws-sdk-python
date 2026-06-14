"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateUnreferencedMergeCommit``."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Never

import zapros

import aws_sdk_codecommit._auth._signers
import aws_sdk_codecommit._auth._sigv4
from aws_sdk_codecommit._protocol.errors import parse_error_metadata_json
from aws_sdk_codecommit._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_codecommit._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_codecommit.errors import UnknownServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.create_unreferenced_merge_commit_input
    import aws_sdk_codecommit.types.create_unreferenced_merge_commit_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "CommitDoesNotExistException":
            import aws_sdk_codecommit.errors.commit_does_not_exist_exception

            raise aws_sdk_codecommit.errors.commit_does_not_exist_exception.CommitDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "CommitMessageLengthExceededException":
            import aws_sdk_codecommit.errors.commit_message_length_exceeded_exception

            raise aws_sdk_codecommit.errors.commit_message_length_exceeded_exception.CommitMessageLengthExceededException.from_aws_json_1_1(
                data
            )
        case "CommitRequiredException":
            import aws_sdk_codecommit.errors.commit_required_exception

            raise aws_sdk_codecommit.errors.commit_required_exception.CommitRequiredException.from_aws_json_1_1(
                data
            )
        case "ConcurrentReferenceUpdateException":
            import aws_sdk_codecommit.errors.concurrent_reference_update_exception

            raise aws_sdk_codecommit.errors.concurrent_reference_update_exception.ConcurrentReferenceUpdateException.from_aws_json_1_1(
                data
            )
        case "EncryptionIntegrityChecksFailedException":
            import aws_sdk_codecommit.errors.encryption_integrity_checks_failed_exception

            raise aws_sdk_codecommit.errors.encryption_integrity_checks_failed_exception.EncryptionIntegrityChecksFailedException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyAccessDeniedException":
            import aws_sdk_codecommit.errors.encryption_key_access_denied_exception

            raise aws_sdk_codecommit.errors.encryption_key_access_denied_exception.EncryptionKeyAccessDeniedException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyDisabledException":
            import aws_sdk_codecommit.errors.encryption_key_disabled_exception

            raise aws_sdk_codecommit.errors.encryption_key_disabled_exception.EncryptionKeyDisabledException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyNotFoundException":
            import aws_sdk_codecommit.errors.encryption_key_not_found_exception

            raise aws_sdk_codecommit.errors.encryption_key_not_found_exception.EncryptionKeyNotFoundException.from_aws_json_1_1(
                data
            )
        case "EncryptionKeyUnavailableException":
            import aws_sdk_codecommit.errors.encryption_key_unavailable_exception

            raise aws_sdk_codecommit.errors.encryption_key_unavailable_exception.EncryptionKeyUnavailableException.from_aws_json_1_1(
                data
            )
        case "FileContentSizeLimitExceededException":
            import aws_sdk_codecommit.errors.file_content_size_limit_exceeded_exception

            raise aws_sdk_codecommit.errors.file_content_size_limit_exceeded_exception.FileContentSizeLimitExceededException.from_aws_json_1_1(
                data
            )
        case "FileModeRequiredException":
            import aws_sdk_codecommit.errors.file_mode_required_exception

            raise aws_sdk_codecommit.errors.file_mode_required_exception.FileModeRequiredException.from_aws_json_1_1(
                data
            )
        case "FolderContentSizeLimitExceededException":
            import aws_sdk_codecommit.errors.folder_content_size_limit_exceeded_exception

            raise aws_sdk_codecommit.errors.folder_content_size_limit_exceeded_exception.FolderContentSizeLimitExceededException.from_aws_json_1_1(
                data
            )
        case "InvalidCommitException":
            import aws_sdk_codecommit.errors.invalid_commit_exception

            raise aws_sdk_codecommit.errors.invalid_commit_exception.InvalidCommitException.from_aws_json_1_1(
                data
            )
        case "InvalidConflictDetailLevelException":
            import aws_sdk_codecommit.errors.invalid_conflict_detail_level_exception

            raise aws_sdk_codecommit.errors.invalid_conflict_detail_level_exception.InvalidConflictDetailLevelException.from_aws_json_1_1(
                data
            )
        case "InvalidConflictResolutionException":
            import aws_sdk_codecommit.errors.invalid_conflict_resolution_exception

            raise aws_sdk_codecommit.errors.invalid_conflict_resolution_exception.InvalidConflictResolutionException.from_aws_json_1_1(
                data
            )
        case "InvalidConflictResolutionStrategyException":
            import aws_sdk_codecommit.errors.invalid_conflict_resolution_strategy_exception

            raise aws_sdk_codecommit.errors.invalid_conflict_resolution_strategy_exception.InvalidConflictResolutionStrategyException.from_aws_json_1_1(
                data
            )
        case "InvalidEmailException":
            import aws_sdk_codecommit.errors.invalid_email_exception

            raise aws_sdk_codecommit.errors.invalid_email_exception.InvalidEmailException.from_aws_json_1_1(
                data
            )
        case "InvalidFileModeException":
            import aws_sdk_codecommit.errors.invalid_file_mode_exception

            raise aws_sdk_codecommit.errors.invalid_file_mode_exception.InvalidFileModeException.from_aws_json_1_1(
                data
            )
        case "InvalidMergeOptionException":
            import aws_sdk_codecommit.errors.invalid_merge_option_exception

            raise aws_sdk_codecommit.errors.invalid_merge_option_exception.InvalidMergeOptionException.from_aws_json_1_1(
                data
            )
        case "InvalidPathException":
            import aws_sdk_codecommit.errors.invalid_path_exception

            raise aws_sdk_codecommit.errors.invalid_path_exception.InvalidPathException.from_aws_json_1_1(
                data
            )
        case "InvalidReplacementContentException":
            import aws_sdk_codecommit.errors.invalid_replacement_content_exception

            raise aws_sdk_codecommit.errors.invalid_replacement_content_exception.InvalidReplacementContentException.from_aws_json_1_1(
                data
            )
        case "InvalidReplacementTypeException":
            import aws_sdk_codecommit.errors.invalid_replacement_type_exception

            raise aws_sdk_codecommit.errors.invalid_replacement_type_exception.InvalidReplacementTypeException.from_aws_json_1_1(
                data
            )
        case "InvalidRepositoryNameException":
            import aws_sdk_codecommit.errors.invalid_repository_name_exception

            raise aws_sdk_codecommit.errors.invalid_repository_name_exception.InvalidRepositoryNameException.from_aws_json_1_1(
                data
            )
        case "ManualMergeRequiredException":
            import aws_sdk_codecommit.errors.manual_merge_required_exception

            raise aws_sdk_codecommit.errors.manual_merge_required_exception.ManualMergeRequiredException.from_aws_json_1_1(
                data
            )
        case "MaximumConflictResolutionEntriesExceededException":
            import aws_sdk_codecommit.errors.maximum_conflict_resolution_entries_exceeded_exception

            raise aws_sdk_codecommit.errors.maximum_conflict_resolution_entries_exceeded_exception.MaximumConflictResolutionEntriesExceededException.from_aws_json_1_1(
                data
            )
        case "MaximumFileContentToLoadExceededException":
            import aws_sdk_codecommit.errors.maximum_file_content_to_load_exceeded_exception

            raise aws_sdk_codecommit.errors.maximum_file_content_to_load_exceeded_exception.MaximumFileContentToLoadExceededException.from_aws_json_1_1(
                data
            )
        case "MaximumItemsToCompareExceededException":
            import aws_sdk_codecommit.errors.maximum_items_to_compare_exceeded_exception

            raise aws_sdk_codecommit.errors.maximum_items_to_compare_exceeded_exception.MaximumItemsToCompareExceededException.from_aws_json_1_1(
                data
            )
        case "MergeOptionRequiredException":
            import aws_sdk_codecommit.errors.merge_option_required_exception

            raise aws_sdk_codecommit.errors.merge_option_required_exception.MergeOptionRequiredException.from_aws_json_1_1(
                data
            )
        case "MultipleConflictResolutionEntriesException":
            import aws_sdk_codecommit.errors.multiple_conflict_resolution_entries_exception

            raise aws_sdk_codecommit.errors.multiple_conflict_resolution_entries_exception.MultipleConflictResolutionEntriesException.from_aws_json_1_1(
                data
            )
        case "NameLengthExceededException":
            import aws_sdk_codecommit.errors.name_length_exceeded_exception

            raise aws_sdk_codecommit.errors.name_length_exceeded_exception.NameLengthExceededException.from_aws_json_1_1(
                data
            )
        case "PathRequiredException":
            import aws_sdk_codecommit.errors.path_required_exception

            raise aws_sdk_codecommit.errors.path_required_exception.PathRequiredException.from_aws_json_1_1(
                data
            )
        case "ReplacementContentRequiredException":
            import aws_sdk_codecommit.errors.replacement_content_required_exception

            raise aws_sdk_codecommit.errors.replacement_content_required_exception.ReplacementContentRequiredException.from_aws_json_1_1(
                data
            )
        case "ReplacementTypeRequiredException":
            import aws_sdk_codecommit.errors.replacement_type_required_exception

            raise aws_sdk_codecommit.errors.replacement_type_required_exception.ReplacementTypeRequiredException.from_aws_json_1_1(
                data
            )
        case "RepositoryDoesNotExistException":
            import aws_sdk_codecommit.errors.repository_does_not_exist_exception

            raise aws_sdk_codecommit.errors.repository_does_not_exist_exception.RepositoryDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "RepositoryNameRequiredException":
            import aws_sdk_codecommit.errors.repository_name_required_exception

            raise aws_sdk_codecommit.errors.repository_name_required_exception.RepositoryNameRequiredException.from_aws_json_1_1(
                data
            )
        case "TipsDivergenceExceededException":
            import aws_sdk_codecommit.errors.tips_divergence_exceeded_exception

            raise aws_sdk_codecommit.errors.tips_divergence_exceeded_exception.TipsDivergenceExceededException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_codecommit.types.create_unreferenced_merge_commit_output.CreateUnreferencedMergeCommitOutput:
    import aws_sdk_codecommit.types.create_unreferenced_merge_commit_output

    out: aws_sdk_codecommit.types.create_unreferenced_merge_commit_output.CreateUnreferencedMergeCommitOutput = aws_sdk_codecommit.types.create_unreferenced_merge_commit_output.deserialize_aws_json_1_1(
        json.loads(response.read())
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
    input_: aws_sdk_codecommit.types.create_unreferenced_merge_commit_input.CreateUnreferencedMergeCommitInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.CreateUnreferencedMergeCommit"
    import aws_sdk_codecommit.types.create_unreferenced_merge_commit_input

    body: bytes | None = json.dumps(
        aws_sdk_codecommit.types.create_unreferenced_merge_commit_input.serialize_aws_json_1_1(
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


def create_unreferenced_merge_commit(
    options: OperationOptions,
    input_: aws_sdk_codecommit.types.create_unreferenced_merge_commit_input.CreateUnreferencedMergeCommitInput,
) -> tuple[
    aws_sdk_codecommit.types.create_unreferenced_merge_commit_output.CreateUnreferencedMergeCommitOutput,
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


async def async_create_unreferenced_merge_commit(
    options: AsyncOperationOptions,
    input_: aws_sdk_codecommit.types.create_unreferenced_merge_commit_input.CreateUnreferencedMergeCommitInput,
) -> tuple[
    aws_sdk_codecommit.types.create_unreferenced_merge_commit_output.CreateUnreferencedMergeCommitOutput,
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
