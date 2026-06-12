"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateCommit``."""

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
    import aws_sdk_codecommit.types.create_commit_input
    import aws_sdk_codecommit.types.create_commit_output


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BranchDoesNotExistException":
            import aws_sdk_codecommit.errors.branch_does_not_exist_exception

            raise aws_sdk_codecommit.errors.branch_does_not_exist_exception.BranchDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "BranchNameIsTagNameException":
            import aws_sdk_codecommit.errors.branch_name_is_tag_name_exception

            raise aws_sdk_codecommit.errors.branch_name_is_tag_name_exception.BranchNameIsTagNameException.from_aws_json_1_1(
                data
            )
        case "BranchNameRequiredException":
            import aws_sdk_codecommit.errors.branch_name_required_exception

            raise aws_sdk_codecommit.errors.branch_name_required_exception.BranchNameRequiredException.from_aws_json_1_1(
                data
            )
        case "CommitMessageLengthExceededException":
            import aws_sdk_codecommit.errors.commit_message_length_exceeded_exception

            raise aws_sdk_codecommit.errors.commit_message_length_exceeded_exception.CommitMessageLengthExceededException.from_aws_json_1_1(
                data
            )
        case "DirectoryNameConflictsWithFileNameException":
            import aws_sdk_codecommit.errors.directory_name_conflicts_with_file_name_exception

            raise aws_sdk_codecommit.errors.directory_name_conflicts_with_file_name_exception.DirectoryNameConflictsWithFileNameException.from_aws_json_1_1(
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
        case "FileContentAndSourceFileSpecifiedException":
            import aws_sdk_codecommit.errors.file_content_and_source_file_specified_exception

            raise aws_sdk_codecommit.errors.file_content_and_source_file_specified_exception.FileContentAndSourceFileSpecifiedException.from_aws_json_1_1(
                data
            )
        case "FileContentSizeLimitExceededException":
            import aws_sdk_codecommit.errors.file_content_size_limit_exceeded_exception

            raise aws_sdk_codecommit.errors.file_content_size_limit_exceeded_exception.FileContentSizeLimitExceededException.from_aws_json_1_1(
                data
            )
        case "FileDoesNotExistException":
            import aws_sdk_codecommit.errors.file_does_not_exist_exception

            raise aws_sdk_codecommit.errors.file_does_not_exist_exception.FileDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "FileEntryRequiredException":
            import aws_sdk_codecommit.errors.file_entry_required_exception

            raise aws_sdk_codecommit.errors.file_entry_required_exception.FileEntryRequiredException.from_aws_json_1_1(
                data
            )
        case "FileModeRequiredException":
            import aws_sdk_codecommit.errors.file_mode_required_exception

            raise aws_sdk_codecommit.errors.file_mode_required_exception.FileModeRequiredException.from_aws_json_1_1(
                data
            )
        case "FileNameConflictsWithDirectoryNameException":
            import aws_sdk_codecommit.errors.file_name_conflicts_with_directory_name_exception

            raise aws_sdk_codecommit.errors.file_name_conflicts_with_directory_name_exception.FileNameConflictsWithDirectoryNameException.from_aws_json_1_1(
                data
            )
        case "FilePathConflictsWithSubmodulePathException":
            import aws_sdk_codecommit.errors.file_path_conflicts_with_submodule_path_exception

            raise aws_sdk_codecommit.errors.file_path_conflicts_with_submodule_path_exception.FilePathConflictsWithSubmodulePathException.from_aws_json_1_1(
                data
            )
        case "FolderContentSizeLimitExceededException":
            import aws_sdk_codecommit.errors.folder_content_size_limit_exceeded_exception

            raise aws_sdk_codecommit.errors.folder_content_size_limit_exceeded_exception.FolderContentSizeLimitExceededException.from_aws_json_1_1(
                data
            )
        case "InvalidBranchNameException":
            import aws_sdk_codecommit.errors.invalid_branch_name_exception

            raise aws_sdk_codecommit.errors.invalid_branch_name_exception.InvalidBranchNameException.from_aws_json_1_1(
                data
            )
        case "InvalidDeletionParameterException":
            import aws_sdk_codecommit.errors.invalid_deletion_parameter_exception

            raise aws_sdk_codecommit.errors.invalid_deletion_parameter_exception.InvalidDeletionParameterException.from_aws_json_1_1(
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
        case "InvalidParentCommitIdException":
            import aws_sdk_codecommit.errors.invalid_parent_commit_id_exception

            raise aws_sdk_codecommit.errors.invalid_parent_commit_id_exception.InvalidParentCommitIdException.from_aws_json_1_1(
                data
            )
        case "InvalidPathException":
            import aws_sdk_codecommit.errors.invalid_path_exception

            raise aws_sdk_codecommit.errors.invalid_path_exception.InvalidPathException.from_aws_json_1_1(
                data
            )
        case "InvalidRepositoryNameException":
            import aws_sdk_codecommit.errors.invalid_repository_name_exception

            raise aws_sdk_codecommit.errors.invalid_repository_name_exception.InvalidRepositoryNameException.from_aws_json_1_1(
                data
            )
        case "MaximumFileEntriesExceededException":
            import aws_sdk_codecommit.errors.maximum_file_entries_exceeded_exception

            raise aws_sdk_codecommit.errors.maximum_file_entries_exceeded_exception.MaximumFileEntriesExceededException.from_aws_json_1_1(
                data
            )
        case "NameLengthExceededException":
            import aws_sdk_codecommit.errors.name_length_exceeded_exception

            raise aws_sdk_codecommit.errors.name_length_exceeded_exception.NameLengthExceededException.from_aws_json_1_1(
                data
            )
        case "NoChangeException":
            import aws_sdk_codecommit.errors.no_change_exception

            raise aws_sdk_codecommit.errors.no_change_exception.NoChangeException.from_aws_json_1_1(
                data
            )
        case "ParentCommitDoesNotExistException":
            import aws_sdk_codecommit.errors.parent_commit_does_not_exist_exception

            raise aws_sdk_codecommit.errors.parent_commit_does_not_exist_exception.ParentCommitDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "ParentCommitIdOutdatedException":
            import aws_sdk_codecommit.errors.parent_commit_id_outdated_exception

            raise aws_sdk_codecommit.errors.parent_commit_id_outdated_exception.ParentCommitIdOutdatedException.from_aws_json_1_1(
                data
            )
        case "ParentCommitIdRequiredException":
            import aws_sdk_codecommit.errors.parent_commit_id_required_exception

            raise aws_sdk_codecommit.errors.parent_commit_id_required_exception.ParentCommitIdRequiredException.from_aws_json_1_1(
                data
            )
        case "PathRequiredException":
            import aws_sdk_codecommit.errors.path_required_exception

            raise aws_sdk_codecommit.errors.path_required_exception.PathRequiredException.from_aws_json_1_1(
                data
            )
        case "PutFileEntryConflictException":
            import aws_sdk_codecommit.errors.put_file_entry_conflict_exception

            raise aws_sdk_codecommit.errors.put_file_entry_conflict_exception.PutFileEntryConflictException.from_aws_json_1_1(
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
        case "RestrictedSourceFileException":
            import aws_sdk_codecommit.errors.restricted_source_file_exception

            raise aws_sdk_codecommit.errors.restricted_source_file_exception.RestrictedSourceFileException.from_aws_json_1_1(
                data
            )
        case "SamePathRequestException":
            import aws_sdk_codecommit.errors.same_path_request_exception

            raise aws_sdk_codecommit.errors.same_path_request_exception.SamePathRequestException.from_aws_json_1_1(
                data
            )
        case "SourceFileOrContentRequiredException":
            import aws_sdk_codecommit.errors.source_file_or_content_required_exception

            raise aws_sdk_codecommit.errors.source_file_or_content_required_exception.SourceFileOrContentRequiredException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response, is_async: bool
) -> aws_sdk_codecommit.types.create_commit_output.CreateCommitOutput:
    import aws_sdk_codecommit.types.create_commit_output

    out: aws_sdk_codecommit.types.create_commit_output.CreateCommitOutput = (
        aws_sdk_codecommit.types.create_commit_output.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_codecommit._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}
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
    input: aws_sdk_codecommit.types.create_commit_input.CreateCommitInput,
) -> zapros.Request:
    endpoint = resolve(  # noqa: F841
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "CodeCommit_20150413.CreateCommit"
    import aws_sdk_codecommit.types.create_commit_input

    body: bytes | None = json.dumps(
        aws_sdk_codecommit.types.create_commit_input.serialize_aws_json_1_1(input)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url,
        "POST",
        headers=headers,
        body=body,
        context={"signer": signer},
    )


def create_commit(
    options: OperationOptions,
    input: aws_sdk_codecommit.types.create_commit_input.CreateCommitInput,
) -> tuple[
    aws_sdk_codecommit.types.create_commit_output.CreateCommitOutput, zapros.Response
]:
    response = options.client.handler.handle(build_request(options, input))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response, is_async=False), response
    except BaseException:
        response.close()
        raise


async def async_create_commit(
    options: AsyncOperationOptions,
    input: aws_sdk_codecommit.types.create_commit_input.CreateCommitInput,
) -> tuple[
    aws_sdk_codecommit.types.create_commit_output.CreateCommitOutput, zapros.Response
]:
    response = await options.client.handler.ahandle(build_request(options, input))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return handle_response(response, is_async=True), response
    except BaseException:
        await response.aclose()
        raise
