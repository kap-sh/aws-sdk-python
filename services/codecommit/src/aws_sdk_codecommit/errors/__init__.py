from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    SerializationError as SerializationError,
)
from ._base import (
    ServiceError as ServiceError,
)
from ._base import (
    UnknownServiceError as UnknownServiceError,
)
from ._base import (
    WaiterFailedError as WaiterFailedError,
)
from ._base import (
    WaiterTimeoutError as WaiterTimeoutError,
)
from .actor_does_not_exist_exception import (
    ActorDoesNotExistException as ActorDoesNotExistException,
)
from .approval_rule_content_required_exception import (
    ApprovalRuleContentRequiredException as ApprovalRuleContentRequiredException,
)
from .approval_rule_does_not_exist_exception import (
    ApprovalRuleDoesNotExistException as ApprovalRuleDoesNotExistException,
)
from .approval_rule_name_already_exists_exception import (
    ApprovalRuleNameAlreadyExistsException as ApprovalRuleNameAlreadyExistsException,
)
from .approval_rule_name_required_exception import (
    ApprovalRuleNameRequiredException as ApprovalRuleNameRequiredException,
)
from .approval_rule_template_content_required_exception import (
    ApprovalRuleTemplateContentRequiredException as ApprovalRuleTemplateContentRequiredException,
)
from .approval_rule_template_does_not_exist_exception import (
    ApprovalRuleTemplateDoesNotExistException as ApprovalRuleTemplateDoesNotExistException,
)
from .approval_rule_template_in_use_exception import (
    ApprovalRuleTemplateInUseException as ApprovalRuleTemplateInUseException,
)
from .approval_rule_template_name_already_exists_exception import (
    ApprovalRuleTemplateNameAlreadyExistsException as ApprovalRuleTemplateNameAlreadyExistsException,
)
from .approval_rule_template_name_required_exception import (
    ApprovalRuleTemplateNameRequiredException as ApprovalRuleTemplateNameRequiredException,
)
from .approval_state_required_exception import (
    ApprovalStateRequiredException as ApprovalStateRequiredException,
)
from .author_does_not_exist_exception import (
    AuthorDoesNotExistException as AuthorDoesNotExistException,
)
from .before_commit_id_and_after_commit_id_are_same_exception import (
    BeforeCommitIdAndAfterCommitIdAreSameException as BeforeCommitIdAndAfterCommitIdAreSameException,
)
from .blob_id_does_not_exist_exception import (
    BlobIdDoesNotExistException as BlobIdDoesNotExistException,
)
from .blob_id_required_exception import (
    BlobIdRequiredException as BlobIdRequiredException,
)
from .branch_does_not_exist_exception import (
    BranchDoesNotExistException as BranchDoesNotExistException,
)
from .branch_name_exists_exception import (
    BranchNameExistsException as BranchNameExistsException,
)
from .branch_name_is_tag_name_exception import (
    BranchNameIsTagNameException as BranchNameIsTagNameException,
)
from .branch_name_required_exception import (
    BranchNameRequiredException as BranchNameRequiredException,
)
from .cannot_delete_approval_rule_from_template_exception import (
    CannotDeleteApprovalRuleFromTemplateException as CannotDeleteApprovalRuleFromTemplateException,
)
from .cannot_modify_approval_rule_from_template_exception import (
    CannotModifyApprovalRuleFromTemplateException as CannotModifyApprovalRuleFromTemplateException,
)
from .client_request_token_required_exception import (
    ClientRequestTokenRequiredException as ClientRequestTokenRequiredException,
)
from .comment_content_required_exception import (
    CommentContentRequiredException as CommentContentRequiredException,
)
from .comment_content_size_limit_exceeded_exception import (
    CommentContentSizeLimitExceededException as CommentContentSizeLimitExceededException,
)
from .comment_deleted_exception import (
    CommentDeletedException as CommentDeletedException,
)
from .comment_does_not_exist_exception import (
    CommentDoesNotExistException as CommentDoesNotExistException,
)
from .comment_id_required_exception import (
    CommentIdRequiredException as CommentIdRequiredException,
)
from .comment_not_created_by_caller_exception import (
    CommentNotCreatedByCallerException as CommentNotCreatedByCallerException,
)
from .commit_does_not_exist_exception import (
    CommitDoesNotExistException as CommitDoesNotExistException,
)
from .commit_id_does_not_exist_exception import (
    CommitIdDoesNotExistException as CommitIdDoesNotExistException,
)
from .commit_id_required_exception import (
    CommitIdRequiredException as CommitIdRequiredException,
)
from .commit_ids_limit_exceeded_exception import (
    CommitIdsLimitExceededException as CommitIdsLimitExceededException,
)
from .commit_ids_list_required_exception import (
    CommitIdsListRequiredException as CommitIdsListRequiredException,
)
from .commit_message_length_exceeded_exception import (
    CommitMessageLengthExceededException as CommitMessageLengthExceededException,
)
from .commit_required_exception import (
    CommitRequiredException as CommitRequiredException,
)
from .concurrent_reference_update_exception import (
    ConcurrentReferenceUpdateException as ConcurrentReferenceUpdateException,
)
from .default_branch_cannot_be_deleted_exception import (
    DefaultBranchCannotBeDeletedException as DefaultBranchCannotBeDeletedException,
)
from .directory_name_conflicts_with_file_name_exception import (
    DirectoryNameConflictsWithFileNameException as DirectoryNameConflictsWithFileNameException,
)
from .encryption_integrity_checks_failed_exception import (
    EncryptionIntegrityChecksFailedException as EncryptionIntegrityChecksFailedException,
)
from .encryption_key_access_denied_exception import (
    EncryptionKeyAccessDeniedException as EncryptionKeyAccessDeniedException,
)
from .encryption_key_disabled_exception import (
    EncryptionKeyDisabledException as EncryptionKeyDisabledException,
)
from .encryption_key_invalid_id_exception import (
    EncryptionKeyInvalidIdException as EncryptionKeyInvalidIdException,
)
from .encryption_key_invalid_usage_exception import (
    EncryptionKeyInvalidUsageException as EncryptionKeyInvalidUsageException,
)
from .encryption_key_not_found_exception import (
    EncryptionKeyNotFoundException as EncryptionKeyNotFoundException,
)
from .encryption_key_required_exception import (
    EncryptionKeyRequiredException as EncryptionKeyRequiredException,
)
from .encryption_key_unavailable_exception import (
    EncryptionKeyUnavailableException as EncryptionKeyUnavailableException,
)
from .file_content_and_source_file_specified_exception import (
    FileContentAndSourceFileSpecifiedException as FileContentAndSourceFileSpecifiedException,
)
from .file_content_required_exception import (
    FileContentRequiredException as FileContentRequiredException,
)
from .file_content_size_limit_exceeded_exception import (
    FileContentSizeLimitExceededException as FileContentSizeLimitExceededException,
)
from .file_does_not_exist_exception import (
    FileDoesNotExistException as FileDoesNotExistException,
)
from .file_entry_required_exception import (
    FileEntryRequiredException as FileEntryRequiredException,
)
from .file_mode_required_exception import (
    FileModeRequiredException as FileModeRequiredException,
)
from .file_name_conflicts_with_directory_name_exception import (
    FileNameConflictsWithDirectoryNameException as FileNameConflictsWithDirectoryNameException,
)
from .file_path_conflicts_with_submodule_path_exception import (
    FilePathConflictsWithSubmodulePathException as FilePathConflictsWithSubmodulePathException,
)
from .file_too_large_exception import FileTooLargeException as FileTooLargeException
from .folder_content_size_limit_exceeded_exception import (
    FolderContentSizeLimitExceededException as FolderContentSizeLimitExceededException,
)
from .folder_does_not_exist_exception import (
    FolderDoesNotExistException as FolderDoesNotExistException,
)
from .idempotency_parameter_mismatch_exception import (
    IdempotencyParameterMismatchException as IdempotencyParameterMismatchException,
)
from .invalid_actor_arn_exception import (
    InvalidActorArnException as InvalidActorArnException,
)
from .invalid_approval_rule_content_exception import (
    InvalidApprovalRuleContentException as InvalidApprovalRuleContentException,
)
from .invalid_approval_rule_name_exception import (
    InvalidApprovalRuleNameException as InvalidApprovalRuleNameException,
)
from .invalid_approval_rule_template_content_exception import (
    InvalidApprovalRuleTemplateContentException as InvalidApprovalRuleTemplateContentException,
)
from .invalid_approval_rule_template_description_exception import (
    InvalidApprovalRuleTemplateDescriptionException as InvalidApprovalRuleTemplateDescriptionException,
)
from .invalid_approval_rule_template_name_exception import (
    InvalidApprovalRuleTemplateNameException as InvalidApprovalRuleTemplateNameException,
)
from .invalid_approval_state_exception import (
    InvalidApprovalStateException as InvalidApprovalStateException,
)
from .invalid_author_arn_exception import (
    InvalidAuthorArnException as InvalidAuthorArnException,
)
from .invalid_blob_id_exception import InvalidBlobIdException as InvalidBlobIdException
from .invalid_branch_name_exception import (
    InvalidBranchNameException as InvalidBranchNameException,
)
from .invalid_client_request_token_exception import (
    InvalidClientRequestTokenException as InvalidClientRequestTokenException,
)
from .invalid_comment_id_exception import (
    InvalidCommentIdException as InvalidCommentIdException,
)
from .invalid_commit_exception import InvalidCommitException as InvalidCommitException
from .invalid_commit_id_exception import (
    InvalidCommitIdException as InvalidCommitIdException,
)
from .invalid_conflict_detail_level_exception import (
    InvalidConflictDetailLevelException as InvalidConflictDetailLevelException,
)
from .invalid_conflict_resolution_exception import (
    InvalidConflictResolutionException as InvalidConflictResolutionException,
)
from .invalid_conflict_resolution_strategy_exception import (
    InvalidConflictResolutionStrategyException as InvalidConflictResolutionStrategyException,
)
from .invalid_continuation_token_exception import (
    InvalidContinuationTokenException as InvalidContinuationTokenException,
)
from .invalid_deletion_parameter_exception import (
    InvalidDeletionParameterException as InvalidDeletionParameterException,
)
from .invalid_description_exception import (
    InvalidDescriptionException as InvalidDescriptionException,
)
from .invalid_destination_commit_specifier_exception import (
    InvalidDestinationCommitSpecifierException as InvalidDestinationCommitSpecifierException,
)
from .invalid_email_exception import InvalidEmailException as InvalidEmailException
from .invalid_file_location_exception import (
    InvalidFileLocationException as InvalidFileLocationException,
)
from .invalid_file_mode_exception import (
    InvalidFileModeException as InvalidFileModeException,
)
from .invalid_file_position_exception import (
    InvalidFilePositionException as InvalidFilePositionException,
)
from .invalid_max_conflict_files_exception import (
    InvalidMaxConflictFilesException as InvalidMaxConflictFilesException,
)
from .invalid_max_merge_hunks_exception import (
    InvalidMaxMergeHunksException as InvalidMaxMergeHunksException,
)
from .invalid_max_results_exception import (
    InvalidMaxResultsException as InvalidMaxResultsException,
)
from .invalid_merge_option_exception import (
    InvalidMergeOptionException as InvalidMergeOptionException,
)
from .invalid_order_exception import InvalidOrderException as InvalidOrderException
from .invalid_override_status_exception import (
    InvalidOverrideStatusException as InvalidOverrideStatusException,
)
from .invalid_parent_commit_id_exception import (
    InvalidParentCommitIdException as InvalidParentCommitIdException,
)
from .invalid_path_exception import InvalidPathException as InvalidPathException
from .invalid_pull_request_event_type_exception import (
    InvalidPullRequestEventTypeException as InvalidPullRequestEventTypeException,
)
from .invalid_pull_request_id_exception import (
    InvalidPullRequestIdException as InvalidPullRequestIdException,
)
from .invalid_pull_request_status_exception import (
    InvalidPullRequestStatusException as InvalidPullRequestStatusException,
)
from .invalid_pull_request_status_update_exception import (
    InvalidPullRequestStatusUpdateException as InvalidPullRequestStatusUpdateException,
)
from .invalid_reaction_user_arn_exception import (
    InvalidReactionUserArnException as InvalidReactionUserArnException,
)
from .invalid_reaction_value_exception import (
    InvalidReactionValueException as InvalidReactionValueException,
)
from .invalid_reference_name_exception import (
    InvalidReferenceNameException as InvalidReferenceNameException,
)
from .invalid_relative_file_version_enum_exception import (
    InvalidRelativeFileVersionEnumException as InvalidRelativeFileVersionEnumException,
)
from .invalid_replacement_content_exception import (
    InvalidReplacementContentException as InvalidReplacementContentException,
)
from .invalid_replacement_type_exception import (
    InvalidReplacementTypeException as InvalidReplacementTypeException,
)
from .invalid_repository_description_exception import (
    InvalidRepositoryDescriptionException as InvalidRepositoryDescriptionException,
)
from .invalid_repository_name_exception import (
    InvalidRepositoryNameException as InvalidRepositoryNameException,
)
from .invalid_repository_trigger_branch_name_exception import (
    InvalidRepositoryTriggerBranchNameException as InvalidRepositoryTriggerBranchNameException,
)
from .invalid_repository_trigger_custom_data_exception import (
    InvalidRepositoryTriggerCustomDataException as InvalidRepositoryTriggerCustomDataException,
)
from .invalid_repository_trigger_destination_arn_exception import (
    InvalidRepositoryTriggerDestinationArnException as InvalidRepositoryTriggerDestinationArnException,
)
from .invalid_repository_trigger_events_exception import (
    InvalidRepositoryTriggerEventsException as InvalidRepositoryTriggerEventsException,
)
from .invalid_repository_trigger_name_exception import (
    InvalidRepositoryTriggerNameException as InvalidRepositoryTriggerNameException,
)
from .invalid_repository_trigger_region_exception import (
    InvalidRepositoryTriggerRegionException as InvalidRepositoryTriggerRegionException,
)
from .invalid_resource_arn_exception import (
    InvalidResourceArnException as InvalidResourceArnException,
)
from .invalid_revision_id_exception import (
    InvalidRevisionIdException as InvalidRevisionIdException,
)
from .invalid_rule_content_sha256_exception import (
    InvalidRuleContentSha256Exception as InvalidRuleContentSha256Exception,
)
from .invalid_sort_by_exception import InvalidSortByException as InvalidSortByException
from .invalid_source_commit_specifier_exception import (
    InvalidSourceCommitSpecifierException as InvalidSourceCommitSpecifierException,
)
from .invalid_system_tag_usage_exception import (
    InvalidSystemTagUsageException as InvalidSystemTagUsageException,
)
from .invalid_tag_keys_list_exception import (
    InvalidTagKeysListException as InvalidTagKeysListException,
)
from .invalid_tags_map_exception import (
    InvalidTagsMapException as InvalidTagsMapException,
)
from .invalid_target_branch_exception import (
    InvalidTargetBranchException as InvalidTargetBranchException,
)
from .invalid_target_exception import InvalidTargetException as InvalidTargetException
from .invalid_targets_exception import (
    InvalidTargetsException as InvalidTargetsException,
)
from .invalid_title_exception import InvalidTitleException as InvalidTitleException
from .manual_merge_required_exception import (
    ManualMergeRequiredException as ManualMergeRequiredException,
)
from .maximum_branches_exceeded_exception import (
    MaximumBranchesExceededException as MaximumBranchesExceededException,
)
from .maximum_conflict_resolution_entries_exceeded_exception import (
    MaximumConflictResolutionEntriesExceededException as MaximumConflictResolutionEntriesExceededException,
)
from .maximum_file_content_to_load_exceeded_exception import (
    MaximumFileContentToLoadExceededException as MaximumFileContentToLoadExceededException,
)
from .maximum_file_entries_exceeded_exception import (
    MaximumFileEntriesExceededException as MaximumFileEntriesExceededException,
)
from .maximum_items_to_compare_exceeded_exception import (
    MaximumItemsToCompareExceededException as MaximumItemsToCompareExceededException,
)
from .maximum_number_of_approvals_exceeded_exception import (
    MaximumNumberOfApprovalsExceededException as MaximumNumberOfApprovalsExceededException,
)
from .maximum_open_pull_requests_exceeded_exception import (
    MaximumOpenPullRequestsExceededException as MaximumOpenPullRequestsExceededException,
)
from .maximum_repository_names_exceeded_exception import (
    MaximumRepositoryNamesExceededException as MaximumRepositoryNamesExceededException,
)
from .maximum_repository_triggers_exceeded_exception import (
    MaximumRepositoryTriggersExceededException as MaximumRepositoryTriggersExceededException,
)
from .maximum_rule_templates_associated_with_repository_exception import (
    MaximumRuleTemplatesAssociatedWithRepositoryException as MaximumRuleTemplatesAssociatedWithRepositoryException,
)
from .merge_option_required_exception import (
    MergeOptionRequiredException as MergeOptionRequiredException,
)
from .multiple_conflict_resolution_entries_exception import (
    MultipleConflictResolutionEntriesException as MultipleConflictResolutionEntriesException,
)
from .multiple_repositories_in_pull_request_exception import (
    MultipleRepositoriesInPullRequestException as MultipleRepositoriesInPullRequestException,
)
from .name_length_exceeded_exception import (
    NameLengthExceededException as NameLengthExceededException,
)
from .no_change_exception import NoChangeException as NoChangeException
from .number_of_rule_templates_exceeded_exception import (
    NumberOfRuleTemplatesExceededException as NumberOfRuleTemplatesExceededException,
)
from .number_of_rules_exceeded_exception import (
    NumberOfRulesExceededException as NumberOfRulesExceededException,
)
from .operation_not_allowed_exception import (
    OperationNotAllowedException as OperationNotAllowedException,
)
from .override_already_set_exception import (
    OverrideAlreadySetException as OverrideAlreadySetException,
)
from .override_status_required_exception import (
    OverrideStatusRequiredException as OverrideStatusRequiredException,
)
from .parent_commit_does_not_exist_exception import (
    ParentCommitDoesNotExistException as ParentCommitDoesNotExistException,
)
from .parent_commit_id_outdated_exception import (
    ParentCommitIdOutdatedException as ParentCommitIdOutdatedException,
)
from .parent_commit_id_required_exception import (
    ParentCommitIdRequiredException as ParentCommitIdRequiredException,
)
from .path_does_not_exist_exception import (
    PathDoesNotExistException as PathDoesNotExistException,
)
from .path_required_exception import PathRequiredException as PathRequiredException
from .pull_request_already_closed_exception import (
    PullRequestAlreadyClosedException as PullRequestAlreadyClosedException,
)
from .pull_request_approval_rules_not_satisfied_exception import (
    PullRequestApprovalRulesNotSatisfiedException as PullRequestApprovalRulesNotSatisfiedException,
)
from .pull_request_cannot_be_approved_by_author_exception import (
    PullRequestCannotBeApprovedByAuthorException as PullRequestCannotBeApprovedByAuthorException,
)
from .pull_request_does_not_exist_exception import (
    PullRequestDoesNotExistException as PullRequestDoesNotExistException,
)
from .pull_request_id_required_exception import (
    PullRequestIdRequiredException as PullRequestIdRequiredException,
)
from .pull_request_status_required_exception import (
    PullRequestStatusRequiredException as PullRequestStatusRequiredException,
)
from .put_file_entry_conflict_exception import (
    PutFileEntryConflictException as PutFileEntryConflictException,
)
from .reaction_limit_exceeded_exception import (
    ReactionLimitExceededException as ReactionLimitExceededException,
)
from .reaction_value_required_exception import (
    ReactionValueRequiredException as ReactionValueRequiredException,
)
from .reference_does_not_exist_exception import (
    ReferenceDoesNotExistException as ReferenceDoesNotExistException,
)
from .reference_name_required_exception import (
    ReferenceNameRequiredException as ReferenceNameRequiredException,
)
from .reference_type_not_supported_exception import (
    ReferenceTypeNotSupportedException as ReferenceTypeNotSupportedException,
)
from .replacement_content_required_exception import (
    ReplacementContentRequiredException as ReplacementContentRequiredException,
)
from .replacement_type_required_exception import (
    ReplacementTypeRequiredException as ReplacementTypeRequiredException,
)
from .repository_does_not_exist_exception import (
    RepositoryDoesNotExistException as RepositoryDoesNotExistException,
)
from .repository_limit_exceeded_exception import (
    RepositoryLimitExceededException as RepositoryLimitExceededException,
)
from .repository_name_exists_exception import (
    RepositoryNameExistsException as RepositoryNameExistsException,
)
from .repository_name_required_exception import (
    RepositoryNameRequiredException as RepositoryNameRequiredException,
)
from .repository_names_required_exception import (
    RepositoryNamesRequiredException as RepositoryNamesRequiredException,
)
from .repository_not_associated_with_pull_request_exception import (
    RepositoryNotAssociatedWithPullRequestException as RepositoryNotAssociatedWithPullRequestException,
)
from .repository_trigger_branch_name_list_required_exception import (
    RepositoryTriggerBranchNameListRequiredException as RepositoryTriggerBranchNameListRequiredException,
)
from .repository_trigger_destination_arn_required_exception import (
    RepositoryTriggerDestinationArnRequiredException as RepositoryTriggerDestinationArnRequiredException,
)
from .repository_trigger_events_list_required_exception import (
    RepositoryTriggerEventsListRequiredException as RepositoryTriggerEventsListRequiredException,
)
from .repository_trigger_name_required_exception import (
    RepositoryTriggerNameRequiredException as RepositoryTriggerNameRequiredException,
)
from .repository_triggers_list_required_exception import (
    RepositoryTriggersListRequiredException as RepositoryTriggersListRequiredException,
)
from .resource_arn_required_exception import (
    ResourceArnRequiredException as ResourceArnRequiredException,
)
from .restricted_source_file_exception import (
    RestrictedSourceFileException as RestrictedSourceFileException,
)
from .revision_id_required_exception import (
    RevisionIdRequiredException as RevisionIdRequiredException,
)
from .revision_not_current_exception import (
    RevisionNotCurrentException as RevisionNotCurrentException,
)
from .same_file_content_exception import (
    SameFileContentException as SameFileContentException,
)
from .same_path_request_exception import (
    SamePathRequestException as SamePathRequestException,
)
from .source_and_destination_are_same_exception import (
    SourceAndDestinationAreSameException as SourceAndDestinationAreSameException,
)
from .source_file_or_content_required_exception import (
    SourceFileOrContentRequiredException as SourceFileOrContentRequiredException,
)
from .tag_keys_list_required_exception import (
    TagKeysListRequiredException as TagKeysListRequiredException,
)
from .tag_policy_exception import TagPolicyException as TagPolicyException
from .tags_map_required_exception import (
    TagsMapRequiredException as TagsMapRequiredException,
)
from .target_required_exception import (
    TargetRequiredException as TargetRequiredException,
)
from .targets_required_exception import (
    TargetsRequiredException as TargetsRequiredException,
)
from .tip_of_source_reference_is_different_exception import (
    TipOfSourceReferenceIsDifferentException as TipOfSourceReferenceIsDifferentException,
)
from .tips_divergence_exceeded_exception import (
    TipsDivergenceExceededException as TipsDivergenceExceededException,
)
from .title_required_exception import TitleRequiredException as TitleRequiredException
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
