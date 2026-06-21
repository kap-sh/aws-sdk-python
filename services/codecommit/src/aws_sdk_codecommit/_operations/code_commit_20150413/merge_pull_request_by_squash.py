"""Generated from Smithy shape ``com.amazonaws.codecommit#MergePullRequestBySquash``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_codecommit._auth._signers
import aws_sdk_codecommit._auth._sigv4
import aws_sdk_codecommit.errors.commit_message_length_exceeded_exception
import aws_sdk_codecommit.errors.concurrent_reference_update_exception
import aws_sdk_codecommit.errors.encryption_integrity_checks_failed_exception
import aws_sdk_codecommit.errors.encryption_key_access_denied_exception
import aws_sdk_codecommit.errors.encryption_key_disabled_exception
import aws_sdk_codecommit.errors.encryption_key_not_found_exception
import aws_sdk_codecommit.errors.encryption_key_unavailable_exception
import aws_sdk_codecommit.errors.file_content_size_limit_exceeded_exception
import aws_sdk_codecommit.errors.folder_content_size_limit_exceeded_exception
import aws_sdk_codecommit.errors.invalid_commit_id_exception
import aws_sdk_codecommit.errors.invalid_conflict_detail_level_exception
import aws_sdk_codecommit.errors.invalid_conflict_resolution_exception
import aws_sdk_codecommit.errors.invalid_conflict_resolution_strategy_exception
import aws_sdk_codecommit.errors.invalid_email_exception
import aws_sdk_codecommit.errors.invalid_file_mode_exception
import aws_sdk_codecommit.errors.invalid_path_exception
import aws_sdk_codecommit.errors.invalid_pull_request_id_exception
import aws_sdk_codecommit.errors.invalid_replacement_content_exception
import aws_sdk_codecommit.errors.invalid_replacement_type_exception
import aws_sdk_codecommit.errors.invalid_repository_name_exception
import aws_sdk_codecommit.errors.manual_merge_required_exception
import aws_sdk_codecommit.errors.maximum_conflict_resolution_entries_exceeded_exception
import aws_sdk_codecommit.errors.maximum_file_content_to_load_exceeded_exception
import aws_sdk_codecommit.errors.maximum_items_to_compare_exceeded_exception
import aws_sdk_codecommit.errors.multiple_conflict_resolution_entries_exception
import aws_sdk_codecommit.errors.name_length_exceeded_exception
import aws_sdk_codecommit.errors.path_required_exception
import aws_sdk_codecommit.errors.pull_request_already_closed_exception
import aws_sdk_codecommit.errors.pull_request_approval_rules_not_satisfied_exception
import aws_sdk_codecommit.errors.pull_request_does_not_exist_exception
import aws_sdk_codecommit.errors.pull_request_id_required_exception
import aws_sdk_codecommit.errors.replacement_content_required_exception
import aws_sdk_codecommit.errors.replacement_type_required_exception
import aws_sdk_codecommit.errors.repository_does_not_exist_exception
import aws_sdk_codecommit.errors.repository_name_required_exception
import aws_sdk_codecommit.errors.repository_not_associated_with_pull_request_exception
import aws_sdk_codecommit.errors.tip_of_source_reference_is_different_exception
import aws_sdk_codecommit.errors.tips_divergence_exceeded_exception
import aws_sdk_codecommit.types.conflict_detail_level_type_enum
import aws_sdk_codecommit.types.conflict_resolution
import aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum
import aws_sdk_codecommit.types.merge_pull_request_by_squash_input
import aws_sdk_codecommit.types.merge_pull_request_by_squash_output
import aws_sdk_codecommit.types.pull_request
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
        case "CommitMessageLengthExceededException":
            raise aws_sdk_codecommit.errors.commit_message_length_exceeded_exception.CommitMessageLengthExceededException.from_aws_json_1_1(
                data
            )
        case "ConcurrentReferenceUpdateException":
            raise aws_sdk_codecommit.errors.concurrent_reference_update_exception.ConcurrentReferenceUpdateException.from_aws_json_1_1(
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
        case "FileContentSizeLimitExceededException":
            raise aws_sdk_codecommit.errors.file_content_size_limit_exceeded_exception.FileContentSizeLimitExceededException.from_aws_json_1_1(
                data
            )
        case "FolderContentSizeLimitExceededException":
            raise aws_sdk_codecommit.errors.folder_content_size_limit_exceeded_exception.FolderContentSizeLimitExceededException.from_aws_json_1_1(
                data
            )
        case "InvalidCommitIdException":
            raise aws_sdk_codecommit.errors.invalid_commit_id_exception.InvalidCommitIdException.from_aws_json_1_1(
                data
            )
        case "InvalidConflictDetailLevelException":
            raise aws_sdk_codecommit.errors.invalid_conflict_detail_level_exception.InvalidConflictDetailLevelException.from_aws_json_1_1(
                data
            )
        case "InvalidConflictResolutionException":
            raise aws_sdk_codecommit.errors.invalid_conflict_resolution_exception.InvalidConflictResolutionException.from_aws_json_1_1(
                data
            )
        case "InvalidConflictResolutionStrategyException":
            raise aws_sdk_codecommit.errors.invalid_conflict_resolution_strategy_exception.InvalidConflictResolutionStrategyException.from_aws_json_1_1(
                data
            )
        case "InvalidEmailException":
            raise aws_sdk_codecommit.errors.invalid_email_exception.InvalidEmailException.from_aws_json_1_1(
                data
            )
        case "InvalidFileModeException":
            raise aws_sdk_codecommit.errors.invalid_file_mode_exception.InvalidFileModeException.from_aws_json_1_1(
                data
            )
        case "InvalidPathException":
            raise aws_sdk_codecommit.errors.invalid_path_exception.InvalidPathException.from_aws_json_1_1(
                data
            )
        case "InvalidPullRequestIdException":
            raise aws_sdk_codecommit.errors.invalid_pull_request_id_exception.InvalidPullRequestIdException.from_aws_json_1_1(
                data
            )
        case "InvalidReplacementContentException":
            raise aws_sdk_codecommit.errors.invalid_replacement_content_exception.InvalidReplacementContentException.from_aws_json_1_1(
                data
            )
        case "InvalidReplacementTypeException":
            raise aws_sdk_codecommit.errors.invalid_replacement_type_exception.InvalidReplacementTypeException.from_aws_json_1_1(
                data
            )
        case "InvalidRepositoryNameException":
            raise aws_sdk_codecommit.errors.invalid_repository_name_exception.InvalidRepositoryNameException.from_aws_json_1_1(
                data
            )
        case "ManualMergeRequiredException":
            raise aws_sdk_codecommit.errors.manual_merge_required_exception.ManualMergeRequiredException.from_aws_json_1_1(
                data
            )
        case "MaximumConflictResolutionEntriesExceededException":
            raise aws_sdk_codecommit.errors.maximum_conflict_resolution_entries_exceeded_exception.MaximumConflictResolutionEntriesExceededException.from_aws_json_1_1(
                data
            )
        case "MaximumFileContentToLoadExceededException":
            raise aws_sdk_codecommit.errors.maximum_file_content_to_load_exceeded_exception.MaximumFileContentToLoadExceededException.from_aws_json_1_1(
                data
            )
        case "MaximumItemsToCompareExceededException":
            raise aws_sdk_codecommit.errors.maximum_items_to_compare_exceeded_exception.MaximumItemsToCompareExceededException.from_aws_json_1_1(
                data
            )
        case "MultipleConflictResolutionEntriesException":
            raise aws_sdk_codecommit.errors.multiple_conflict_resolution_entries_exception.MultipleConflictResolutionEntriesException.from_aws_json_1_1(
                data
            )
        case "NameLengthExceededException":
            raise aws_sdk_codecommit.errors.name_length_exceeded_exception.NameLengthExceededException.from_aws_json_1_1(
                data
            )
        case "PathRequiredException":
            raise aws_sdk_codecommit.errors.path_required_exception.PathRequiredException.from_aws_json_1_1(
                data
            )
        case "PullRequestAlreadyClosedException":
            raise aws_sdk_codecommit.errors.pull_request_already_closed_exception.PullRequestAlreadyClosedException.from_aws_json_1_1(
                data
            )
        case "PullRequestApprovalRulesNotSatisfiedException":
            raise aws_sdk_codecommit.errors.pull_request_approval_rules_not_satisfied_exception.PullRequestApprovalRulesNotSatisfiedException.from_aws_json_1_1(
                data
            )
        case "PullRequestDoesNotExistException":
            raise aws_sdk_codecommit.errors.pull_request_does_not_exist_exception.PullRequestDoesNotExistException.from_aws_json_1_1(
                data
            )
        case "PullRequestIdRequiredException":
            raise aws_sdk_codecommit.errors.pull_request_id_required_exception.PullRequestIdRequiredException.from_aws_json_1_1(
                data
            )
        case "ReplacementContentRequiredException":
            raise aws_sdk_codecommit.errors.replacement_content_required_exception.ReplacementContentRequiredException.from_aws_json_1_1(
                data
            )
        case "ReplacementTypeRequiredException":
            raise aws_sdk_codecommit.errors.replacement_type_required_exception.ReplacementTypeRequiredException.from_aws_json_1_1(
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
        case "RepositoryNotAssociatedWithPullRequestException":
            raise aws_sdk_codecommit.errors.repository_not_associated_with_pull_request_exception.RepositoryNotAssociatedWithPullRequestException.from_aws_json_1_1(
                data
            )
        case "TipOfSourceReferenceIsDifferentException":
            raise aws_sdk_codecommit.errors.tip_of_source_reference_is_different_exception.TipOfSourceReferenceIsDifferentException.from_aws_json_1_1(
                data
            )
        case "TipsDivergenceExceededException":
            raise aws_sdk_codecommit.errors.tips_divergence_exceeded_exception.TipsDivergenceExceededException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput:
    out: aws_sdk_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput = aws_sdk_codecommit.types.merge_pull_request_by_squash_output.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput:
    out: aws_sdk_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput = aws_sdk_codecommit.types.merge_pull_request_by_squash_output.deserialize_aws_json_1_1(
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
    input_: aws_sdk_codecommit.types.merge_pull_request_by_squash_input.MergePullRequestBySquashInput,
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
    headers["X-Amz-Target"] = "CodeCommit_20150413.MergePullRequestBySquash"
    import aws_sdk_codecommit.types.merge_pull_request_by_squash_input

    body: bytes | None = json.dumps(
        aws_sdk_codecommit.types.merge_pull_request_by_squash_input.serialize_aws_json_1_1(
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


def merge_pull_request_by_squash(
    options: OperationOptions,
    input_: aws_sdk_codecommit.types.merge_pull_request_by_squash_input.MergePullRequestBySquashInput,
) -> tuple[
    aws_sdk_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput,
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


async def async_merge_pull_request_by_squash(
    options: AsyncOperationOptions,
    input_: aws_sdk_codecommit.types.merge_pull_request_by_squash_input.MergePullRequestBySquashInput,
) -> tuple[
    aws_sdk_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput,
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
