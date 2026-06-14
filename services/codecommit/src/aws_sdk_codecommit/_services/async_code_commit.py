"""Generated from Smithy shape ``com.amazonaws.codecommit#CodeCommit_20150413``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_codecommit._auth._signers
import aws_sdk_codecommit._auth._sigv4
from aws_sdk_codecommit._auth._identity import Credentials
from aws_sdk_codecommit._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_codecommit._auth._zapros_handler import AuthMiddleware
from aws_sdk_codecommit._pagination import resolve_path as _resolve_path
from aws_sdk_codecommit._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_content
    import aws_sdk_codecommit.types.approval_rule_name
    import aws_sdk_codecommit.types.approval_rule_template_content
    import aws_sdk_codecommit.types.approval_rule_template_description
    import aws_sdk_codecommit.types.approval_rule_template_name
    import aws_sdk_codecommit.types.approval_state
    import aws_sdk_codecommit.types.arn
    import aws_sdk_codecommit.types.associate_approval_rule_template_with_repository_input
    import aws_sdk_codecommit.types.batch_associate_approval_rule_template_with_repositories_input
    import aws_sdk_codecommit.types.batch_associate_approval_rule_template_with_repositories_output
    import aws_sdk_codecommit.types.batch_describe_merge_conflicts_input
    import aws_sdk_codecommit.types.batch_describe_merge_conflicts_output
    import aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_input
    import aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_output
    import aws_sdk_codecommit.types.batch_get_commits_input
    import aws_sdk_codecommit.types.batch_get_commits_output
    import aws_sdk_codecommit.types.batch_get_repositories_input
    import aws_sdk_codecommit.types.batch_get_repositories_output
    import aws_sdk_codecommit.types.branch_name
    import aws_sdk_codecommit.types.client_request_token
    import aws_sdk_codecommit.types.comment_id
    import aws_sdk_codecommit.types.commit_id
    import aws_sdk_codecommit.types.commit_ids_input_list
    import aws_sdk_codecommit.types.commit_name
    import aws_sdk_codecommit.types.conflict_detail_level_type_enum
    import aws_sdk_codecommit.types.conflict_resolution
    import aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum
    import aws_sdk_codecommit.types.content
    import aws_sdk_codecommit.types.create_approval_rule_template_input
    import aws_sdk_codecommit.types.create_approval_rule_template_output
    import aws_sdk_codecommit.types.create_branch_input
    import aws_sdk_codecommit.types.create_commit_input
    import aws_sdk_codecommit.types.create_commit_output
    import aws_sdk_codecommit.types.create_pull_request_approval_rule_input
    import aws_sdk_codecommit.types.create_pull_request_approval_rule_output
    import aws_sdk_codecommit.types.create_pull_request_input
    import aws_sdk_codecommit.types.create_pull_request_output
    import aws_sdk_codecommit.types.create_repository_input
    import aws_sdk_codecommit.types.create_repository_output
    import aws_sdk_codecommit.types.create_unreferenced_merge_commit_input
    import aws_sdk_codecommit.types.create_unreferenced_merge_commit_output
    import aws_sdk_codecommit.types.delete_approval_rule_template_input
    import aws_sdk_codecommit.types.delete_approval_rule_template_output
    import aws_sdk_codecommit.types.delete_branch_input
    import aws_sdk_codecommit.types.delete_branch_output
    import aws_sdk_codecommit.types.delete_comment_content_input
    import aws_sdk_codecommit.types.delete_comment_content_output
    import aws_sdk_codecommit.types.delete_file_entries
    import aws_sdk_codecommit.types.delete_file_input
    import aws_sdk_codecommit.types.delete_file_output
    import aws_sdk_codecommit.types.delete_pull_request_approval_rule_input
    import aws_sdk_codecommit.types.delete_pull_request_approval_rule_output
    import aws_sdk_codecommit.types.delete_repository_input
    import aws_sdk_codecommit.types.delete_repository_output
    import aws_sdk_codecommit.types.describe_merge_conflicts_input
    import aws_sdk_codecommit.types.describe_merge_conflicts_output
    import aws_sdk_codecommit.types.describe_pull_request_events_input
    import aws_sdk_codecommit.types.describe_pull_request_events_output
    import aws_sdk_codecommit.types.description
    import aws_sdk_codecommit.types.disassociate_approval_rule_template_from_repository_input
    import aws_sdk_codecommit.types.email
    import aws_sdk_codecommit.types.evaluate_pull_request_approval_rules_input
    import aws_sdk_codecommit.types.evaluate_pull_request_approval_rules_output
    import aws_sdk_codecommit.types.file_content
    import aws_sdk_codecommit.types.file_mode_type_enum
    import aws_sdk_codecommit.types.file_paths
    import aws_sdk_codecommit.types.get_approval_rule_template_input
    import aws_sdk_codecommit.types.get_approval_rule_template_output
    import aws_sdk_codecommit.types.get_blob_input
    import aws_sdk_codecommit.types.get_blob_output
    import aws_sdk_codecommit.types.get_branch_input
    import aws_sdk_codecommit.types.get_branch_output
    import aws_sdk_codecommit.types.get_comment_input
    import aws_sdk_codecommit.types.get_comment_output
    import aws_sdk_codecommit.types.get_comment_reactions_input
    import aws_sdk_codecommit.types.get_comment_reactions_output
    import aws_sdk_codecommit.types.get_comments_for_compared_commit_input
    import aws_sdk_codecommit.types.get_comments_for_compared_commit_output
    import aws_sdk_codecommit.types.get_comments_for_pull_request_input
    import aws_sdk_codecommit.types.get_comments_for_pull_request_output
    import aws_sdk_codecommit.types.get_commit_input
    import aws_sdk_codecommit.types.get_commit_output
    import aws_sdk_codecommit.types.get_differences_input
    import aws_sdk_codecommit.types.get_differences_output
    import aws_sdk_codecommit.types.get_file_input
    import aws_sdk_codecommit.types.get_file_output
    import aws_sdk_codecommit.types.get_folder_input
    import aws_sdk_codecommit.types.get_folder_output
    import aws_sdk_codecommit.types.get_merge_commit_input
    import aws_sdk_codecommit.types.get_merge_commit_output
    import aws_sdk_codecommit.types.get_merge_conflicts_input
    import aws_sdk_codecommit.types.get_merge_conflicts_output
    import aws_sdk_codecommit.types.get_merge_options_input
    import aws_sdk_codecommit.types.get_merge_options_output
    import aws_sdk_codecommit.types.get_pull_request_approval_states_input
    import aws_sdk_codecommit.types.get_pull_request_approval_states_output
    import aws_sdk_codecommit.types.get_pull_request_input
    import aws_sdk_codecommit.types.get_pull_request_output
    import aws_sdk_codecommit.types.get_pull_request_override_state_input
    import aws_sdk_codecommit.types.get_pull_request_override_state_output
    import aws_sdk_codecommit.types.get_repository_input
    import aws_sdk_codecommit.types.get_repository_output
    import aws_sdk_codecommit.types.get_repository_triggers_input
    import aws_sdk_codecommit.types.get_repository_triggers_output
    import aws_sdk_codecommit.types.keep_empty_folders
    import aws_sdk_codecommit.types.kms_key_id
    import aws_sdk_codecommit.types.limit
    import aws_sdk_codecommit.types.list_approval_rule_templates_input
    import aws_sdk_codecommit.types.list_approval_rule_templates_output
    import aws_sdk_codecommit.types.list_associated_approval_rule_templates_for_repository_input
    import aws_sdk_codecommit.types.list_associated_approval_rule_templates_for_repository_output
    import aws_sdk_codecommit.types.list_branches_input
    import aws_sdk_codecommit.types.list_branches_output
    import aws_sdk_codecommit.types.list_file_commit_history_request
    import aws_sdk_codecommit.types.list_file_commit_history_response
    import aws_sdk_codecommit.types.list_pull_requests_input
    import aws_sdk_codecommit.types.list_pull_requests_output
    import aws_sdk_codecommit.types.list_repositories_for_approval_rule_template_input
    import aws_sdk_codecommit.types.list_repositories_for_approval_rule_template_output
    import aws_sdk_codecommit.types.list_repositories_input
    import aws_sdk_codecommit.types.list_repositories_output
    import aws_sdk_codecommit.types.list_tags_for_resource_input
    import aws_sdk_codecommit.types.list_tags_for_resource_output
    import aws_sdk_codecommit.types.location
    import aws_sdk_codecommit.types.max_results
    import aws_sdk_codecommit.types.merge_branches_by_fast_forward_input
    import aws_sdk_codecommit.types.merge_branches_by_fast_forward_output
    import aws_sdk_codecommit.types.merge_branches_by_squash_input
    import aws_sdk_codecommit.types.merge_branches_by_squash_output
    import aws_sdk_codecommit.types.merge_branches_by_three_way_input
    import aws_sdk_codecommit.types.merge_branches_by_three_way_output
    import aws_sdk_codecommit.types.merge_option_type_enum
    import aws_sdk_codecommit.types.merge_pull_request_by_fast_forward_input
    import aws_sdk_codecommit.types.merge_pull_request_by_fast_forward_output
    import aws_sdk_codecommit.types.merge_pull_request_by_squash_input
    import aws_sdk_codecommit.types.merge_pull_request_by_squash_output
    import aws_sdk_codecommit.types.merge_pull_request_by_three_way_input
    import aws_sdk_codecommit.types.merge_pull_request_by_three_way_output
    import aws_sdk_codecommit.types.message
    import aws_sdk_codecommit.types.name
    import aws_sdk_codecommit.types.next_token
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.order_enum
    import aws_sdk_codecommit.types.override_pull_request_approval_rules_input
    import aws_sdk_codecommit.types.override_status
    import aws_sdk_codecommit.types.path
    import aws_sdk_codecommit.types.post_comment_for_compared_commit_input
    import aws_sdk_codecommit.types.post_comment_for_compared_commit_output
    import aws_sdk_codecommit.types.post_comment_for_pull_request_input
    import aws_sdk_codecommit.types.post_comment_for_pull_request_output
    import aws_sdk_codecommit.types.post_comment_reply_input
    import aws_sdk_codecommit.types.post_comment_reply_output
    import aws_sdk_codecommit.types.pull_request_event_type
    import aws_sdk_codecommit.types.pull_request_id
    import aws_sdk_codecommit.types.pull_request_status_enum
    import aws_sdk_codecommit.types.put_comment_reaction_input
    import aws_sdk_codecommit.types.put_file_entries
    import aws_sdk_codecommit.types.put_file_input
    import aws_sdk_codecommit.types.put_file_output
    import aws_sdk_codecommit.types.put_repository_triggers_input
    import aws_sdk_codecommit.types.put_repository_triggers_output
    import aws_sdk_codecommit.types.reaction_value
    import aws_sdk_codecommit.types.repository_description
    import aws_sdk_codecommit.types.repository_name
    import aws_sdk_codecommit.types.repository_name_id_pair
    import aws_sdk_codecommit.types.repository_name_list
    import aws_sdk_codecommit.types.repository_triggers_list
    import aws_sdk_codecommit.types.resource_arn
    import aws_sdk_codecommit.types.revision_id
    import aws_sdk_codecommit.types.rule_content_sha256
    import aws_sdk_codecommit.types.set_file_mode_entries
    import aws_sdk_codecommit.types.sort_by_enum
    import aws_sdk_codecommit.types.tag_keys_list
    import aws_sdk_codecommit.types.tag_resource_input
    import aws_sdk_codecommit.types.tags_map
    import aws_sdk_codecommit.types.target_list
    import aws_sdk_codecommit.types.test_repository_triggers_input
    import aws_sdk_codecommit.types.test_repository_triggers_output
    import aws_sdk_codecommit.types.title
    import aws_sdk_codecommit.types.untag_resource_input
    import aws_sdk_codecommit.types.update_approval_rule_template_content_input
    import aws_sdk_codecommit.types.update_approval_rule_template_content_output
    import aws_sdk_codecommit.types.update_approval_rule_template_description_input
    import aws_sdk_codecommit.types.update_approval_rule_template_description_output
    import aws_sdk_codecommit.types.update_approval_rule_template_name_input
    import aws_sdk_codecommit.types.update_approval_rule_template_name_output
    import aws_sdk_codecommit.types.update_comment_input
    import aws_sdk_codecommit.types.update_comment_output
    import aws_sdk_codecommit.types.update_default_branch_input
    import aws_sdk_codecommit.types.update_pull_request_approval_rule_content_input
    import aws_sdk_codecommit.types.update_pull_request_approval_rule_content_output
    import aws_sdk_codecommit.types.update_pull_request_approval_state_input
    import aws_sdk_codecommit.types.update_pull_request_description_input
    import aws_sdk_codecommit.types.update_pull_request_description_output
    import aws_sdk_codecommit.types.update_pull_request_status_input
    import aws_sdk_codecommit.types.update_pull_request_status_output
    import aws_sdk_codecommit.types.update_pull_request_title_input
    import aws_sdk_codecommit.types.update_pull_request_title_output
    import aws_sdk_codecommit.types.update_repository_description_input
    import aws_sdk_codecommit.types.update_repository_encryption_key_input
    import aws_sdk_codecommit.types.update_repository_encryption_key_output
    import aws_sdk_codecommit.types.update_repository_name_input


class AsyncCodeCommitClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncCodeCommitClient:
    """A client for the ``CodeCommit`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncCodeCommitClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncCodeCommitClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCodeCommitClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def associate_approval_rule_template_with_repository(
        self,
        approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> None:
        """<p>Creates an association between an approval rule template and a specified repository. Then, the next time a pull request is created in the repository where the destination reference (if specified) matches the destination reference (branch) for the pull request, an approval rule that matches the template conditions is automatically created for that pull request. If no destination references are specified in the template, an approval rule that matches the template contents is created for all pull requests in that repository.</p>

        Args:
            approval_rule_template_name: <p>The name for the approval rule template. </p>
            repository_name: <p>The name of the repository that you want to associate with the template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.associate_approval_rule_template_with_repository_input.AssociateApprovalRuleTemplateWithRepositoryInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_codecommit._operations.code_commit_20150413.associate_approval_rule_template_with_repository

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.associate_approval_rule_template_with_repository.async_associate_approval_rule_template_with_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.associate_approval_rule_template_with_repository_input.AssociateApprovalRuleTemplateWithRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["approval_rule_template_name"] = approval_rule_template_name
        input_["repository_name"] = repository_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_associate_approval_rule_template_with_repositories(
        self,
        approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        repository_names: "aws_sdk_codecommit.types.repository_name_list.RepositoryNameList",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.batch_associate_approval_rule_template_with_repositories_output.BatchAssociateApprovalRuleTemplateWithRepositoriesOutput":
        """<p>Creates an association between an approval rule template and one or more specified repositories. </p>

        Args:
            approval_rule_template_name: <p>The name of the template you want to associate with one or more repositories.</p>
            repository_names: <p>The names of the repositories you want to associate with the template.</p> <note> <p>The length constraint limit is for each string in the array. The array itself can be empty.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.batch_associate_approval_rule_template_with_repositories_input.BatchAssociateApprovalRuleTemplateWithRepositoriesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.batch_associate_approval_rule_template_with_repositories_output.BatchAssociateApprovalRuleTemplateWithRepositoriesOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.batch_associate_approval_rule_template_with_repositories

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.batch_associate_approval_rule_template_with_repositories.async_batch_associate_approval_rule_template_with_repositories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.batch_associate_approval_rule_template_with_repositories_input.BatchAssociateApprovalRuleTemplateWithRepositoriesInput = {}  # type: ignore[typeddict-item]
        input_["approval_rule_template_name"] = approval_rule_template_name
        input_["repository_names"] = repository_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_describe_merge_conflicts(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        merge_option: "aws_sdk_codecommit.types.merge_option_type_enum.MergeOptionTypeEnum",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        max_merge_hunks: Optional[
            "aws_sdk_codecommit.types.max_results.MaxResults"
        ] = None,
        max_conflict_files: Optional[
            "aws_sdk_codecommit.types.max_results.MaxResults"
        ] = None,
        file_paths: Optional["aws_sdk_codecommit.types.file_paths.FilePaths"] = None,
        conflict_detail_level: Optional[
            "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
        ] = None,
        conflict_resolution_strategy: Optional[
            "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
        ] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_codecommit.types.batch_describe_merge_conflicts_output.BatchDescribeMergeConflictsOutput":
        """<p>Returns information about one or more merge conflicts in the attempted merge of two commit specifiers using the squash or three-way merge strategy.</p>

        Args:
            repository_name: <p>The name of the repository that contains the merge conflicts you want to review.</p>
            destination_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            source_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            merge_option: <p>The merge option or strategy you want to use to merge the code.</p>
            max_merge_hunks: <p>The maximum number of merge hunks to include in the output.</p>
            max_conflict_files: <p>The maximum number of files to include in the output.</p>
            file_paths: <p>The path of the target files used to describe the conflicts. If not specified, the default is all conflict files.</p>
            conflict_detail_level: <p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>
            conflict_resolution_strategy: <p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.batch_describe_merge_conflicts_input.BatchDescribeMergeConflictsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.batch_describe_merge_conflicts_output.BatchDescribeMergeConflictsOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.batch_describe_merge_conflicts

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.batch_describe_merge_conflicts.async_batch_describe_merge_conflicts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.batch_describe_merge_conflicts_input.BatchDescribeMergeConflictsInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["destination_commit_specifier"] = destination_commit_specifier
        input_["source_commit_specifier"] = source_commit_specifier
        input_["merge_option"] = merge_option
        if max_merge_hunks is not None:
            input_["max_merge_hunks"] = max_merge_hunks
        if max_conflict_files is not None:
            input_["max_conflict_files"] = max_conflict_files
        if file_paths is not None:
            input_["file_paths"] = file_paths
        if conflict_detail_level is not None:
            input_["conflict_detail_level"] = conflict_detail_level
        if conflict_resolution_strategy is not None:
            input_["conflict_resolution_strategy"] = conflict_resolution_strategy
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_disassociate_approval_rule_template_from_repositories(
        self,
        approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        repository_names: "aws_sdk_codecommit.types.repository_name_list.RepositoryNameList",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_output.BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput":
        """<p>Removes the association between an approval rule template and one or more specified repositories. </p>

        Args:
            approval_rule_template_name: <p>The name of the template that you want to disassociate from one or more repositories.</p>
            repository_names: <p>The repository names that you want to disassociate from the approval rule template.</p> <note> <p>The length constraint limit is for each string in the array. The array itself can be empty.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_input.BatchDisassociateApprovalRuleTemplateFromRepositoriesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_output.BatchDisassociateApprovalRuleTemplateFromRepositoriesOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.batch_disassociate_approval_rule_template_from_repositories

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.batch_disassociate_approval_rule_template_from_repositories.async_batch_disassociate_approval_rule_template_from_repositories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_input.BatchDisassociateApprovalRuleTemplateFromRepositoriesInput = {}  # type: ignore[typeddict-item]
        input_["approval_rule_template_name"] = approval_rule_template_name
        input_["repository_names"] = repository_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_commits(
        self,
        commit_ids: "aws_sdk_codecommit.types.commit_ids_input_list.CommitIdsInputList",
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.batch_get_commits_output.BatchGetCommitsOutput":
        """<p>Returns information about the contents of one or more commits in a repository.</p>

        Args:
            commit_ids: <p>The full commit IDs of the commits to get information about.</p> <note> <p>You must supply the full SHA IDs of each commit. You cannot use shortened SHA IDs.</p> </note>
            repository_name: <p>The name of the repository that contains the commits.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.batch_get_commits_input.BatchGetCommitsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.batch_get_commits_output.BatchGetCommitsOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.batch_get_commits

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.batch_get_commits.async_batch_get_commits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.batch_get_commits_input.BatchGetCommitsInput = {}  # type: ignore[typeddict-item]
        input_["commit_ids"] = commit_ids
        input_["repository_name"] = repository_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_repositories(
        self,
        repository_names: "aws_sdk_codecommit.types.repository_name_list.RepositoryNameList",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.batch_get_repositories_output.BatchGetRepositoriesOutput":
        """<p>Returns information about one or more repositories.</p> <note> <p>The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.</p> </note>

        Args:
            repository_names: <p>The names of the repositories to get information about.</p> <note> <p>The length constraint limit is for each string in the array. The array itself can be empty.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.batch_get_repositories_input.BatchGetRepositoriesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.batch_get_repositories_output.BatchGetRepositoriesOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.batch_get_repositories

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.batch_get_repositories.async_batch_get_repositories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.batch_get_repositories_input.BatchGetRepositoriesInput = {}  # type: ignore[typeddict-item]
        input_["repository_names"] = repository_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_approval_rule_template(
        self,
        approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        approval_rule_template_content: "aws_sdk_codecommit.types.approval_rule_template_content.ApprovalRuleTemplateContent",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        approval_rule_template_description: Optional[
            "aws_sdk_codecommit.types.approval_rule_template_description.ApprovalRuleTemplateDescription"
        ] = None,
    ) -> "aws_sdk_codecommit.types.create_approval_rule_template_output.CreateApprovalRuleTemplateOutput":
        """<p>Creates a template for approval rules that can then be associated with one or more repositories in your Amazon Web Services account. When you associate a template with a repository, CodeCommit creates an approval rule that matches the conditions of the template for all pull requests that meet the conditions of the template. For more information, see <a>AssociateApprovalRuleTemplateWithRepository</a>.</p>

        Args:
            approval_rule_template_name: <p>The name of the approval rule template. Provide descriptive names, because this name is applied to the approval rules created automatically in associated repositories.</p>
            approval_rule_template_content: <p>The content of the approval rule that is created on pull requests in associated repositories. If you specify one or more destination references (branches), approval rules are created in an associated repository only if their destination references (branches) match those specified in the template.</p> <note> <p>When you create the content of the approval rule template, you can specify approvers in an approval pool in one of two ways:</p> <ul> <li> <p> <b>CodeCommitApprovers</b>: This option only requires an Amazon Web Services account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the Amazon Web Services account <i>123456789012</i> and <i>Mary_Major</i>, all of the following are counted as approvals coming from that user:</p> <ul> <li> <p>An IAM user in the account (arn:aws:iam::<i>123456789012</i>:user/<i>Mary_Major</i>)</p> </li> <li> <p>A federated user identified in IAM as Mary_Major (arn:aws:sts::<i>123456789012</i>:federated-user/<i>Mary_Major</i>)</p> </li> </ul> <p>This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of <i>Mary_Major</i> (arn:aws:sts::<i>123456789012</i>:assumed-role/CodeCommitReview/<i>Mary_Major</i>) unless you include a wildcard (*Mary_Major).</p> </li> <li> <p> <b>Fully qualified ARN</b>: This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role. </p> </li> </ul> <p>For more information about IAM ARNs, wildcards, and formats, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM Identifiers</a> in the <i>IAM User Guide</i>.</p> </note>
            approval_rule_template_description: <p>The description of the approval rule template. Consider providing a description that explains what this template does and when it might be appropriate to associate it with repositories.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.create_approval_rule_template_input.CreateApprovalRuleTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.create_approval_rule_template_output.CreateApprovalRuleTemplateOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.create_approval_rule_template

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.create_approval_rule_template.async_create_approval_rule_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.create_approval_rule_template_input.CreateApprovalRuleTemplateInput = {}  # type: ignore[typeddict-item]
        input_["approval_rule_template_name"] = approval_rule_template_name
        input_["approval_rule_template_content"] = approval_rule_template_content
        if approval_rule_template_description is not None:
            input_["approval_rule_template_description"] = (
                approval_rule_template_description
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_branch(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        branch_name: "aws_sdk_codecommit.types.branch_name.BranchName",
        commit_id: "aws_sdk_codecommit.types.commit_id.CommitId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> None:
        """<p>Creates a branch in a repository and points the branch to a commit.</p> <note> <p>Calling the create branch operation does not set a repository's default branch. To do this, call the update default branch operation.</p> </note>

        Args:
            repository_name: <p>The name of the repository in which you want to create the new branch.</p>
            branch_name: <p>The name of the new branch to create.</p>
            commit_id: <p>The ID of the commit to point the new branch to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.create_branch_input.CreateBranchInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_codecommit._operations.code_commit_20150413.create_branch

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.create_branch.async_create_branch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.create_branch_input.CreateBranchInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["branch_name"] = branch_name
        input_["commit_id"] = commit_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_commit(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        branch_name: "aws_sdk_codecommit.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        parent_commit_id: Optional[
            "aws_sdk_codecommit.types.commit_id.CommitId"
        ] = None,
        author_name: Optional["aws_sdk_codecommit.types.name.Name"] = None,
        email: Optional["aws_sdk_codecommit.types.email.Email"] = None,
        commit_message: Optional["aws_sdk_codecommit.types.message.Message"] = None,
        keep_empty_folders: Optional[
            "aws_sdk_codecommit.types.keep_empty_folders.KeepEmptyFolders"
        ] = None,
        put_files: Optional[
            "aws_sdk_codecommit.types.put_file_entries.PutFileEntries"
        ] = None,
        delete_files: Optional[
            "aws_sdk_codecommit.types.delete_file_entries.DeleteFileEntries"
        ] = None,
        set_file_modes: Optional[
            "aws_sdk_codecommit.types.set_file_mode_entries.SetFileModeEntries"
        ] = None,
    ) -> "aws_sdk_codecommit.types.create_commit_output.CreateCommitOutput":
        """<p>Creates a commit for a repository on the tip of a specified branch.</p>

        Args:
            repository_name: <p>The name of the repository where you create the commit.</p>
            branch_name: <p>The name of the branch where you create the commit.</p>
            parent_commit_id: <p>The ID of the commit that is the parent of the commit you create. Not required if this is an empty repository.</p>
            author_name: <p>The name of the author who created the commit. This information is used as both the author and committer for the commit.</p>
            email: <p>The email address of the person who created the commit.</p>
            commit_message: <p>The commit message you want to include in the commit. Commit messages are limited to 256 KB. If no message is specified, a default message is used.</p>
            keep_empty_folders: <p>If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a ..gitkeep file is created for empty folders. The default is false.</p>
            put_files: <p>The files to add or update in this commit.</p>
            delete_files: <p>The files to delete in this commit. These files still exist in earlier commits.</p>
            set_file_modes: <p>The file modes to update for files in this commit.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.create_commit_input.CreateCommitInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.create_commit_output.CreateCommitOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.create_commit

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.create_commit.async_create_commit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.create_commit_input.CreateCommitInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["branch_name"] = branch_name
        if parent_commit_id is not None:
            input_["parent_commit_id"] = parent_commit_id
        if author_name is not None:
            input_["author_name"] = author_name
        if email is not None:
            input_["email"] = email
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if keep_empty_folders is not None:
            input_["keep_empty_folders"] = keep_empty_folders
        if put_files is not None:
            input_["put_files"] = put_files
        if delete_files is not None:
            input_["delete_files"] = delete_files
        if set_file_modes is not None:
            input_["set_file_modes"] = set_file_modes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_pull_request(
        self,
        title: "aws_sdk_codecommit.types.title.Title",
        targets: "aws_sdk_codecommit.types.target_list.TargetList",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        description: Optional[
            "aws_sdk_codecommit.types.description.Description"
        ] = None,
        client_request_token: Optional[
            "aws_sdk_codecommit.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "aws_sdk_codecommit.types.create_pull_request_output.CreatePullRequestOutput":
        """<p>Creates a pull request in the specified repository.</p>

        Args:
            title: <p>The title of the pull request. This title is used to identify the pull request to other users in the repository.</p>
            description: <p>A description of the pull request.</p>
            targets: <p>The targets for the pull request, including the source of the code to be reviewed (the source branch) and the destination where the creator of the pull request intends the code to be merged after the pull request is closed (the destination branch).</p>
            client_request_token: <p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p> <note> <p>The Amazon Web ServicesSDKs prepopulate client request tokens. If you are using an Amazon Web ServicesSDK, an idempotency token is created for you.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.create_pull_request_input.CreatePullRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.create_pull_request_output.CreatePullRequestOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.create_pull_request

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.create_pull_request.async_create_pull_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.create_pull_request_input.CreatePullRequestInput = {}  # type: ignore[typeddict-item]
        input_["title"] = title
        if description is not None:
            input_["description"] = description
        input_["targets"] = targets
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_pull_request_approval_rule(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        approval_rule_name: "aws_sdk_codecommit.types.approval_rule_name.ApprovalRuleName",
        approval_rule_content: "aws_sdk_codecommit.types.approval_rule_content.ApprovalRuleContent",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.create_pull_request_approval_rule_output.CreatePullRequestApprovalRuleOutput":
        """<p>Creates an approval rule for a pull request.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request for which you want to create the approval rule.</p>
            approval_rule_name: <p>The name for the approval rule.</p>
            approval_rule_content: <p>The content of the approval rule, including the number of approvals needed and the structure of an approval pool defined for approvals, if any. For more information about approval pools, see the CodeCommit User Guide.</p> <note> <p>When you create the content of the approval rule, you can specify approvers in an approval pool in one of two ways:</p> <ul> <li> <p> <b>CodeCommitApprovers</b>: This option only requires an Amazon Web Services account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the Amazon Web Services account <i>123456789012</i> and <i>Mary_Major</i>, all of the following would be counted as approvals coming from that user:</p> <ul> <li> <p>An IAM user in the account (arn:aws:iam::<i>123456789012</i>:user/<i>Mary_Major</i>)</p> </li> <li> <p>A federated user identified in IAM as Mary_Major (arn:aws:sts::<i>123456789012</i>:federated-user/<i>Mary_Major</i>)</p> </li> </ul> <p>This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of <i>Mary_Major</i> (arn:aws:sts::<i>123456789012</i>:assumed-role/CodeCommitReview/<i>Mary_Major</i>) unless you include a wildcard (*Mary_Major).</p> </li> <li> <p> <b>Fully qualified ARN</b>: This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role. </p> </li> </ul> <p>For more information about IAM ARNs, wildcards, and formats, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM Identifiers</a> in the <i>IAM User Guide</i>.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.create_pull_request_approval_rule_input.CreatePullRequestApprovalRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.create_pull_request_approval_rule_output.CreatePullRequestApprovalRuleOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.create_pull_request_approval_rule

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.create_pull_request_approval_rule.async_create_pull_request_approval_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.create_pull_request_approval_rule_input.CreatePullRequestApprovalRuleInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["approval_rule_name"] = approval_rule_name
        input_["approval_rule_content"] = approval_rule_content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_repository(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        repository_description: Optional[
            "aws_sdk_codecommit.types.repository_description.RepositoryDescription"
        ] = None,
        tags: Optional["aws_sdk_codecommit.types.tags_map.TagsMap"] = None,
        kms_key_id: Optional["aws_sdk_codecommit.types.kms_key_id.KmsKeyId"] = None,
    ) -> "aws_sdk_codecommit.types.create_repository_output.CreateRepositoryOutput":
        """<p>Creates a new, empty repository.</p>

        Args:
            repository_name: <p>The name of the new repository to be created.</p> <note> <p>The repository name must be unique across the calling Amazon Web Services account. Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. For more information about the limits on repository names, see <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html\">Quotas</a> in the <i>CodeCommit User Guide</i>. The suffix .git is prohibited.</p> </note>
            repository_description: <p>A comment or description about the new repository.</p> <note> <p>The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.</p> </note>
            tags: <p>One or more tag key-value pairs to use when tagging this repository.</p>
            kms_key_id: <p>The ID of the encryption key. You can view the ID of an encryption key in the KMS console, or use the KMS APIs to programmatically retrieve a key ID. For more information about acceptable values for kmsKeyID, see <a href=\"https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html#KMS-Decrypt-request-KeyId\">KeyId</a> in the Decrypt API description in the <i>Key Management Service API Reference</i>.</p> <p>If no key is specified, the default <code>aws/codecommit</code> Amazon Web Services managed key is used.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.create_repository_input.CreateRepositoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.create_repository_output.CreateRepositoryOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.create_repository

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.create_repository.async_create_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.create_repository_input.CreateRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        if repository_description is not None:
            input_["repository_description"] = repository_description
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_unreferenced_merge_commit(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        merge_option: "aws_sdk_codecommit.types.merge_option_type_enum.MergeOptionTypeEnum",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        conflict_detail_level: Optional[
            "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
        ] = None,
        conflict_resolution_strategy: Optional[
            "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
        ] = None,
        author_name: Optional["aws_sdk_codecommit.types.name.Name"] = None,
        email: Optional["aws_sdk_codecommit.types.email.Email"] = None,
        commit_message: Optional["aws_sdk_codecommit.types.message.Message"] = None,
        keep_empty_folders: Optional[
            "aws_sdk_codecommit.types.keep_empty_folders.KeepEmptyFolders"
        ] = None,
        conflict_resolution: Optional[
            "aws_sdk_codecommit.types.conflict_resolution.ConflictResolution"
        ] = None,
    ) -> "aws_sdk_codecommit.types.create_unreferenced_merge_commit_output.CreateUnreferencedMergeCommitOutput":
        """<p>Creates an unreferenced commit that represents the result of merging two branches using a specified merge strategy. This can help you determine the outcome of a potential merge. This API cannot be used with the fast-forward merge strategy because that strategy does not create a merge commit.</p> <note> <p>This unreferenced merge commit can only be accessed using the GetCommit API or through git commands such as git fetch. To retrieve this commit, you must specify its commit ID or otherwise reference it.</p> </note>

        Args:
            repository_name: <p>The name of the repository where you want to create the unreferenced merge commit.</p>
            source_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            destination_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            merge_option: <p>The merge option or strategy you want to use to merge the code.</p>
            conflict_detail_level: <p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>
            conflict_resolution_strategy: <p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>
            author_name: <p>The name of the author who created the unreferenced commit. This information is used as both the author and committer for the commit.</p>
            email: <p>The email address for the person who created the unreferenced commit.</p>
            commit_message: <p>The commit message for the unreferenced commit.</p>
            keep_empty_folders: <p>If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If this is specified as true, a .gitkeep file is created for empty folders. The default is false.</p>
            conflict_resolution: <p>If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.create_unreferenced_merge_commit_input.CreateUnreferencedMergeCommitInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.create_unreferenced_merge_commit_output.CreateUnreferencedMergeCommitOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.create_unreferenced_merge_commit

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.create_unreferenced_merge_commit.async_create_unreferenced_merge_commit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.create_unreferenced_merge_commit_input.CreateUnreferencedMergeCommitInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["source_commit_specifier"] = source_commit_specifier
        input_["destination_commit_specifier"] = destination_commit_specifier
        input_["merge_option"] = merge_option
        if conflict_detail_level is not None:
            input_["conflict_detail_level"] = conflict_detail_level
        if conflict_resolution_strategy is not None:
            input_["conflict_resolution_strategy"] = conflict_resolution_strategy
        if author_name is not None:
            input_["author_name"] = author_name
        if email is not None:
            input_["email"] = email
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if keep_empty_folders is not None:
            input_["keep_empty_folders"] = keep_empty_folders
        if conflict_resolution is not None:
            input_["conflict_resolution"] = conflict_resolution

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_approval_rule_template(
        self,
        approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.delete_approval_rule_template_output.DeleteApprovalRuleTemplateOutput":
        """<p>Deletes a specified approval rule template. Deleting a template does not remove approval rules on pull requests already created with the template.</p>

        Args:
            approval_rule_template_name: <p>The name of the approval rule template to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.delete_approval_rule_template_input.DeleteApprovalRuleTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.delete_approval_rule_template_output.DeleteApprovalRuleTemplateOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.delete_approval_rule_template

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.delete_approval_rule_template.async_delete_approval_rule_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.delete_approval_rule_template_input.DeleteApprovalRuleTemplateInput = {}  # type: ignore[typeddict-item]
        input_["approval_rule_template_name"] = approval_rule_template_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_branch(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        branch_name: "aws_sdk_codecommit.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.delete_branch_output.DeleteBranchOutput":
        """<p>Deletes a branch from a repository, unless that branch is the default branch for the repository. </p>

        Args:
            repository_name: <p>The name of the repository that contains the branch to be deleted.</p>
            branch_name: <p>The name of the branch to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.delete_branch_input.DeleteBranchInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.delete_branch_output.DeleteBranchOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.delete_branch

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.delete_branch.async_delete_branch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.delete_branch_input.DeleteBranchInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["branch_name"] = branch_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_comment_content(
        self,
        comment_id: "aws_sdk_codecommit.types.comment_id.CommentId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.delete_comment_content_output.DeleteCommentContentOutput":
        """<p>Deletes the content of a comment made on a change, file, or commit in a repository.</p>

        Args:
            comment_id: <p>The unique, system-generated ID of the comment. To get this ID, use <a>GetCommentsForComparedCommit</a> or <a>GetCommentsForPullRequest</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.delete_comment_content_input.DeleteCommentContentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.delete_comment_content_output.DeleteCommentContentOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.delete_comment_content

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.delete_comment_content.async_delete_comment_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.delete_comment_content_input.DeleteCommentContentInput = {}  # type: ignore[typeddict-item]
        input_["comment_id"] = comment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_file(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        branch_name: "aws_sdk_codecommit.types.branch_name.BranchName",
        file_path: "aws_sdk_codecommit.types.path.Path",
        parent_commit_id: "aws_sdk_codecommit.types.commit_id.CommitId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        keep_empty_folders: Optional[
            "aws_sdk_codecommit.types.keep_empty_folders.KeepEmptyFolders"
        ] = None,
        commit_message: Optional["aws_sdk_codecommit.types.message.Message"] = None,
        name: Optional["aws_sdk_codecommit.types.name.Name"] = None,
        email: Optional["aws_sdk_codecommit.types.email.Email"] = None,
    ) -> "aws_sdk_codecommit.types.delete_file_output.DeleteFileOutput":
        """<p>Deletes a specified file from a specified branch. A commit is created on the branch that contains the revision. The file still exists in the commits earlier to the commit that contains the deletion.</p>

        Args:
            repository_name: <p>The name of the repository that contains the file to delete.</p>
            branch_name: <p>The name of the branch where the commit that deletes the file is made.</p>
            file_path: <p>The fully qualified path to the file that to be deleted, including the full name and extension of that file. For example, /examples/file.md is a fully qualified path to a file named file.md in a folder named examples.</p>
            parent_commit_id: <p>The ID of the commit that is the tip of the branch where you want to create the commit that deletes the file. This must be the HEAD commit for the branch. The commit that deletes the file is created from this commit ID.</p>
            keep_empty_folders: <p>If a file is the only object in the folder or directory, specifies whether to delete the folder or directory that contains the file. By default, empty folders are deleted. This includes empty folders that are part of the directory structure. For example, if the path to a file is dir1/dir2/dir3/dir4, and dir2 and dir3 are empty, deleting the last file in dir4 also deletes the empty folders dir4, dir3, and dir2.</p>
            commit_message: <p>The commit message you want to include as part of deleting the file. Commit messages are limited to 256 KB. If no message is specified, a default message is used.</p>
            name: <p>The name of the author of the commit that deletes the file. If no name is specified, the user's ARN is used as the author name and committer name.</p>
            email: <p>The email address for the commit that deletes the file. If no email address is specified, the email address is left blank.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.delete_file_input.DeleteFileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.delete_file_output.DeleteFileOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.delete_file

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.delete_file.async_delete_file(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.delete_file_input.DeleteFileInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["branch_name"] = branch_name
        input_["file_path"] = file_path
        input_["parent_commit_id"] = parent_commit_id
        if keep_empty_folders is not None:
            input_["keep_empty_folders"] = keep_empty_folders
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if name is not None:
            input_["name"] = name
        if email is not None:
            input_["email"] = email

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_pull_request_approval_rule(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        approval_rule_name: "aws_sdk_codecommit.types.approval_rule_name.ApprovalRuleName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.delete_pull_request_approval_rule_output.DeletePullRequestApprovalRuleOutput":
        """<p>Deletes an approval rule from a specified pull request. Approval rules can be deleted from a pull request only if the pull request is open, and if the approval rule was created specifically for a pull request and not generated from an approval rule template associated with the repository where the pull request was created. You cannot delete an approval rule from a merged or closed pull request.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request that contains the approval rule you want to delete.</p>
            approval_rule_name: <p>The name of the approval rule you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.delete_pull_request_approval_rule_input.DeletePullRequestApprovalRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.delete_pull_request_approval_rule_output.DeletePullRequestApprovalRuleOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.delete_pull_request_approval_rule

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.delete_pull_request_approval_rule.async_delete_pull_request_approval_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.delete_pull_request_approval_rule_input.DeletePullRequestApprovalRuleInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["approval_rule_name"] = approval_rule_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_repository(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.delete_repository_output.DeleteRepositoryOutput":
        """<p>Deletes a repository. If a specified repository was already deleted, a null repository ID is returned.</p> <important> <p>Deleting a repository also deletes all associated objects and metadata. After a repository is deleted, all future push calls to the deleted repository fail.</p> </important>

        Args:
            repository_name: <p>The name of the repository to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.delete_repository_input.DeleteRepositoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.delete_repository_output.DeleteRepositoryOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.delete_repository

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.delete_repository.async_delete_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.delete_repository_input.DeleteRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_merge_conflicts(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        merge_option: "aws_sdk_codecommit.types.merge_option_type_enum.MergeOptionTypeEnum",
        file_path: "aws_sdk_codecommit.types.path.Path",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        max_merge_hunks: Optional[
            "aws_sdk_codecommit.types.max_results.MaxResults"
        ] = None,
        conflict_detail_level: Optional[
            "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
        ] = None,
        conflict_resolution_strategy: Optional[
            "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
        ] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_codecommit.types.describe_merge_conflicts_output.DescribeMergeConflictsOutput":
        """<p>Returns information about one or more merge conflicts in the attempted merge of two commit specifiers using the squash or three-way merge strategy. If the merge option for the attempted merge is specified as FAST_FORWARD_MERGE, an exception is thrown.</p>

        Args:
            repository_name: <p>The name of the repository where you want to get information about a merge conflict.</p>
            destination_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            source_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            merge_option: <p>The merge option or strategy you want to use to merge the code.</p>
            max_merge_hunks: <p>The maximum number of merge hunks to include in the output.</p>
            file_path: <p>The path of the target files used to describe the conflicts. </p>
            conflict_detail_level: <p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>
            conflict_resolution_strategy: <p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.describe_merge_conflicts_input.DescribeMergeConflictsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.describe_merge_conflicts_output.DescribeMergeConflictsOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.describe_merge_conflicts

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.describe_merge_conflicts.async_describe_merge_conflicts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.describe_merge_conflicts_input.DescribeMergeConflictsInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["destination_commit_specifier"] = destination_commit_specifier
        input_["source_commit_specifier"] = source_commit_specifier
        input_["merge_option"] = merge_option
        if max_merge_hunks is not None:
            input_["max_merge_hunks"] = max_merge_hunks
        input_["file_path"] = file_path
        if conflict_detail_level is not None:
            input_["conflict_detail_level"] = conflict_detail_level
        if conflict_resolution_strategy is not None:
            input_["conflict_resolution_strategy"] = conflict_resolution_strategy
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_pull_request_events(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        pull_request_event_type: Optional[
            "aws_sdk_codecommit.types.pull_request_event_type.PullRequestEventType"
        ] = None,
        actor_arn: Optional["aws_sdk_codecommit.types.arn.Arn"] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_codecommit.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_codecommit.types.describe_pull_request_events_output.DescribePullRequestEventsOutput":
        """<p>Returns information about one or more pull request events.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>
            pull_request_event_type: <p>Optional. The pull request event type about which you want to return information.</p>
            actor_arn: <p>The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with more commits or changing the status of a pull request.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results. The default is 100 events, which is also the maximum number of events that can be returned in a result.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.describe_pull_request_events_input.DescribePullRequestEventsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.describe_pull_request_events_output.DescribePullRequestEventsOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.describe_pull_request_events

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.describe_pull_request_events.async_describe_pull_request_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.describe_pull_request_events_input.DescribePullRequestEventsInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        if pull_request_event_type is not None:
            input_["pull_request_event_type"] = pull_request_event_type
        if actor_arn is not None:
            input_["actor_arn"] = actor_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_approval_rule_template_from_repository(
        self,
        approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> None:
        """<p>Removes the association between a template and a repository so that approval rules based on the template are not automatically created when pull requests are created in the specified repository. This does not delete any approval rules previously created for pull requests through the template association.</p>

        Args:
            approval_rule_template_name: <p>The name of the approval rule template to disassociate from a specified repository.</p>
            repository_name: <p>The name of the repository you want to disassociate from the template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.disassociate_approval_rule_template_from_repository_input.DisassociateApprovalRuleTemplateFromRepositoryInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_codecommit._operations.code_commit_20150413.disassociate_approval_rule_template_from_repository

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.disassociate_approval_rule_template_from_repository.async_disassociate_approval_rule_template_from_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.disassociate_approval_rule_template_from_repository_input.DisassociateApprovalRuleTemplateFromRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["approval_rule_template_name"] = approval_rule_template_name
        input_["repository_name"] = repository_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def evaluate_pull_request_approval_rules(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        revision_id: "aws_sdk_codecommit.types.revision_id.RevisionId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.evaluate_pull_request_approval_rules_output.EvaluatePullRequestApprovalRulesOutput":
        """<p>Evaluates whether a pull request has met all the conditions specified in its associated approval rules.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request you want to evaluate.</p>
            revision_id: <p>The system-generated ID for the pull request revision. To retrieve the most recent revision ID for a pull request, use <a>GetPullRequest</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.evaluate_pull_request_approval_rules_input.EvaluatePullRequestApprovalRulesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.evaluate_pull_request_approval_rules_output.EvaluatePullRequestApprovalRulesOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.evaluate_pull_request_approval_rules

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.evaluate_pull_request_approval_rules.async_evaluate_pull_request_approval_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.evaluate_pull_request_approval_rules_input.EvaluatePullRequestApprovalRulesInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_approval_rule_template(
        self,
        approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.get_approval_rule_template_output.GetApprovalRuleTemplateOutput":
        """<p>Returns information about a specified approval rule template.</p>

        Args:
            approval_rule_template_name: <p>The name of the approval rule template for which you want to get information.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_approval_rule_template_input.GetApprovalRuleTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_approval_rule_template_output.GetApprovalRuleTemplateOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_approval_rule_template

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_approval_rule_template.async_get_approval_rule_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_approval_rule_template_input.GetApprovalRuleTemplateInput = {}  # type: ignore[typeddict-item]
        input_["approval_rule_template_name"] = approval_rule_template_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_blob(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        blob_id: "aws_sdk_codecommit.types.object_id.ObjectId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.get_blob_output.GetBlobOutput":
        """<p>Returns the base-64 encoded content of an individual blob in a repository.</p>

        Args:
            repository_name: <p>The name of the repository that contains the blob.</p>
            blob_id: <p>The ID of the blob, which is its SHA-1 pointer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_blob_input.GetBlobInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_blob_output.GetBlobOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_blob

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_blob.async_get_blob(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_blob_input.GetBlobInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["blob_id"] = blob_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_branch(
        self,
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        repository_name: Optional[
            "aws_sdk_codecommit.types.repository_name.RepositoryName"
        ] = None,
        branch_name: Optional["aws_sdk_codecommit.types.branch_name.BranchName"] = None,
    ) -> "aws_sdk_codecommit.types.get_branch_output.GetBranchOutput":
        """<p>Returns information about a repository branch, including its name and the last commit ID.</p>

        Args:
            repository_name: <p>The name of the repository that contains the branch for which you want to retrieve information.</p>
            branch_name: <p>The name of the branch for which you want to retrieve information.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_branch_input.GetBranchInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_branch_output.GetBranchOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_branch

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_branch.async_get_branch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_branch_input.GetBranchInput = {}  # type: ignore[typeddict-item]
        if repository_name is not None:
            input_["repository_name"] = repository_name
        if branch_name is not None:
            input_["branch_name"] = branch_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_comment(
        self,
        comment_id: "aws_sdk_codecommit.types.comment_id.CommentId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.get_comment_output.GetCommentOutput":
        """<p>Returns the content of a comment made on a change, file, or commit in a repository. </p> <note> <p>Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.</p> </note>

        Args:
            comment_id: <p>The unique, system-generated ID of the comment. To get this ID, use <a>GetCommentsForComparedCommit</a> or <a>GetCommentsForPullRequest</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_comment_input.GetCommentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_comment_output.GetCommentOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_comment

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_comment.async_get_comment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_comment_input.GetCommentInput = {}  # type: ignore[typeddict-item]
        input_["comment_id"] = comment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_comment_reactions(
        self,
        comment_id: "aws_sdk_codecommit.types.comment_id.CommentId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        reaction_user_arn: Optional["aws_sdk_codecommit.types.arn.Arn"] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_codecommit.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_codecommit.types.get_comment_reactions_output.GetCommentReactionsOutput":
        """<p>Returns information about reactions to a specified comment ID. Reactions from users who have been deleted will not be included in the count.</p>

        Args:
            comment_id: <p>The ID of the comment for which you want to get reactions information.</p>
            reaction_user_arn: <p>Optional. The Amazon Resource Name (ARN) of the user or identity for which you want to get reaction information.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results. </p>
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results. The default is the same as the allowed maximum, 1,000.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_comment_reactions_input.GetCommentReactionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_comment_reactions_output.GetCommentReactionsOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_comment_reactions

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_comment_reactions.async_get_comment_reactions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_comment_reactions_input.GetCommentReactionsInput = {}  # type: ignore[typeddict-item]
        input_["comment_id"] = comment_id
        if reaction_user_arn is not None:
            input_["reaction_user_arn"] = reaction_user_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_comments_for_compared_commit(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        after_commit_id: "aws_sdk_codecommit.types.commit_id.CommitId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        before_commit_id: Optional[
            "aws_sdk_codecommit.types.commit_id.CommitId"
        ] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_codecommit.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_codecommit.types.get_comments_for_compared_commit_output.GetCommentsForComparedCommitOutput":
        """<p>Returns information about comments made on the comparison between two commits.</p> <note> <p>Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.</p> </note>

        Args:
            repository_name: <p>The name of the repository where you want to compare commits.</p>
            before_commit_id: <p>To establish the directionality of the comparison, the full commit ID of the before commit.</p>
            after_commit_id: <p>To establish the directionality of the comparison, the full commit ID of the after commit.</p>
            next_token: <p>An enumeration token that when provided in a request, returns the next batch of the results. </p>
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results. The default is 100 comments, but you can configure up to 500.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_comments_for_compared_commit_input.GetCommentsForComparedCommitInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_comments_for_compared_commit_output.GetCommentsForComparedCommitOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_comments_for_compared_commit

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_comments_for_compared_commit.async_get_comments_for_compared_commit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_comments_for_compared_commit_input.GetCommentsForComparedCommitInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        if before_commit_id is not None:
            input_["before_commit_id"] = before_commit_id
        input_["after_commit_id"] = after_commit_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_comments_for_pull_request(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        repository_name: Optional[
            "aws_sdk_codecommit.types.repository_name.RepositoryName"
        ] = None,
        before_commit_id: Optional[
            "aws_sdk_codecommit.types.commit_id.CommitId"
        ] = None,
        after_commit_id: Optional["aws_sdk_codecommit.types.commit_id.CommitId"] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_codecommit.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_codecommit.types.get_comments_for_pull_request_output.GetCommentsForPullRequestOutput":
        """<p>Returns comments made on a pull request.</p> <note> <p>Reaction counts might include numbers from user identities who were deleted after the reaction was made. For a count of reactions from active identities, use GetCommentReactions.</p> </note>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>
            repository_name: <p>The name of the repository that contains the pull request. Requirement is conditional: <code>repositoryName</code> must be specified when <code>beforeCommitId</code> and <code>afterCommitId</code> are included.</p>
            before_commit_id: <p>The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created. Requirement is conditional: <code>beforeCommitId</code> must be specified when <code>repositoryName</code> is included.</p>
            after_commit_id: <p>The full commit ID of the commit in the source branch that was the tip of the branch at the time the comment was made. Requirement is conditional: <code>afterCommitId</code> must be specified when <code>repositoryName</code> is included.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results. The default is 100 comments. You can return up to 500 comments with a single request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_comments_for_pull_request_input.GetCommentsForPullRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_comments_for_pull_request_output.GetCommentsForPullRequestOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_comments_for_pull_request

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_comments_for_pull_request.async_get_comments_for_pull_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_comments_for_pull_request_input.GetCommentsForPullRequestInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        if repository_name is not None:
            input_["repository_name"] = repository_name
        if before_commit_id is not None:
            input_["before_commit_id"] = before_commit_id
        if after_commit_id is not None:
            input_["after_commit_id"] = after_commit_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_commit(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        commit_id: "aws_sdk_codecommit.types.object_id.ObjectId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.get_commit_output.GetCommitOutput":
        """<p>Returns information about a commit, including commit message and committer information.</p>

        Args:
            repository_name: <p>The name of the repository to which the commit was made.</p>
            commit_id: <p>The commit ID. Commit IDs are the full SHA ID of the commit.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_commit_input.GetCommitInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_commit_output.GetCommitOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_commit

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_commit.async_get_commit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_commit_input.GetCommitInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["commit_id"] = commit_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_differences(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        after_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        before_commit_specifier: Optional[
            "aws_sdk_codecommit.types.commit_name.CommitName"
        ] = None,
        before_path: Optional["aws_sdk_codecommit.types.path.Path"] = None,
        after_path: Optional["aws_sdk_codecommit.types.path.Path"] = None,
        max_results: Optional["aws_sdk_codecommit.types.limit.Limit"] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_codecommit.types.get_differences_output.GetDifferencesOutput":
        """<p>Returns information about the differences in a valid commit specifier (such as a branch, tag, HEAD, commit ID, or other fully qualified reference). Results can be limited to a specified path.</p>

        Args:
            repository_name: <p>The name of the repository where you want to get differences.</p>
            before_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, the full commit ID). Optional. If not specified, all changes before the <code>afterCommitSpecifier</code> value are shown. If you do not use <code>beforeCommitSpecifier</code> in your request, consider limiting the results with <code>maxResults</code>.</p>
            after_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit.</p>
            before_path: <p>The file path in which to check for differences. Limits the results to this path. Can also be used to specify the previous name of a directory or folder. If <code>beforePath</code> and <code>afterPath</code> are not specified, differences are shown for all paths.</p>
            after_path: <p>The file path in which to check differences. Limits the results to this path. Can also be used to specify the changed name of a directory or folder, if it has changed. If not specified, differences are shown for all paths.</p>
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_differences_input.GetDifferencesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_differences_output.GetDifferencesOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_differences

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_differences.async_get_differences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_differences_input.GetDifferencesInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        if before_commit_specifier is not None:
            input_["before_commit_specifier"] = before_commit_specifier
        input_["after_commit_specifier"] = after_commit_specifier
        if before_path is not None:
            input_["before_path"] = before_path
        if after_path is not None:
            input_["after_path"] = after_path
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_file(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        file_path: "aws_sdk_codecommit.types.path.Path",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        commit_specifier: Optional[
            "aws_sdk_codecommit.types.commit_name.CommitName"
        ] = None,
    ) -> "aws_sdk_codecommit.types.get_file_output.GetFileOutput":
        """<p>Returns the base-64 encoded contents of a specified file and its metadata.</p>

        Args:
            repository_name: <p>The name of the repository that contains the file.</p>
            commit_specifier: <p>The fully quaified reference that identifies the commit that contains the file. For example, you can specify a full commit ID, a tag, a branch name, or a reference such as refs/heads/main. If none is provided, the head commit is used.</p>
            file_path: <p>The fully qualified path to the file, including the full name and extension of the file. For example, /examples/file.md is the fully qualified path to a file named file.md in a folder named examples.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_file_input.GetFileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_file_output.GetFileOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_file

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_file.async_get_file(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_file_input.GetFileInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        if commit_specifier is not None:
            input_["commit_specifier"] = commit_specifier
        input_["file_path"] = file_path

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_folder(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        folder_path: "aws_sdk_codecommit.types.path.Path",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        commit_specifier: Optional[
            "aws_sdk_codecommit.types.commit_name.CommitName"
        ] = None,
    ) -> "aws_sdk_codecommit.types.get_folder_output.GetFolderOutput":
        """<p>Returns the contents of a specified folder in a repository.</p>

        Args:
            repository_name: <p>The name of the repository.</p>
            commit_specifier: <p>A fully qualified reference used to identify a commit that contains the version of the folder's content to return. A fully qualified reference can be a commit ID, branch name, tag, or reference such as HEAD. If no specifier is provided, the folder content is returned as it exists in the HEAD commit.</p>
            folder_path: <p>The fully qualified path to the folder whose contents are returned, including the folder name. For example, /examples is a fully-qualified path to a folder named examples that was created off of the root directory (/) of a repository. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_folder_input.GetFolderInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_folder_output.GetFolderOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_folder

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_folder.async_get_folder(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_folder_input.GetFolderInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        if commit_specifier is not None:
            input_["commit_specifier"] = commit_specifier
        input_["folder_path"] = folder_path

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_merge_commit(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        conflict_detail_level: Optional[
            "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
        ] = None,
        conflict_resolution_strategy: Optional[
            "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
        ] = None,
    ) -> "aws_sdk_codecommit.types.get_merge_commit_output.GetMergeCommitOutput":
        """<p>Returns information about a specified merge commit.</p>

        Args:
            repository_name: <p>The name of the repository that contains the merge commit about which you want to get information.</p>
            source_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            destination_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            conflict_detail_level: <p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>
            conflict_resolution_strategy: <p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_merge_commit_input.GetMergeCommitInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_merge_commit_output.GetMergeCommitOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_merge_commit

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_merge_commit.async_get_merge_commit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_merge_commit_input.GetMergeCommitInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["source_commit_specifier"] = source_commit_specifier
        input_["destination_commit_specifier"] = destination_commit_specifier
        if conflict_detail_level is not None:
            input_["conflict_detail_level"] = conflict_detail_level
        if conflict_resolution_strategy is not None:
            input_["conflict_resolution_strategy"] = conflict_resolution_strategy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_merge_conflicts(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        merge_option: "aws_sdk_codecommit.types.merge_option_type_enum.MergeOptionTypeEnum",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        conflict_detail_level: Optional[
            "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
        ] = None,
        max_conflict_files: Optional[
            "aws_sdk_codecommit.types.max_results.MaxResults"
        ] = None,
        conflict_resolution_strategy: Optional[
            "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
        ] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_codecommit.types.get_merge_conflicts_output.GetMergeConflictsOutput":
        """<p>Returns information about merge conflicts between the before and after commit IDs for a pull request in a repository.</p>

        Args:
            repository_name: <p>The name of the repository where the pull request was created.</p>
            destination_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            source_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            merge_option: <p>The merge option or strategy you want to use to merge the code. </p>
            conflict_detail_level: <p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>
            max_conflict_files: <p>The maximum number of files to include in the output.</p>
            conflict_resolution_strategy: <p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_merge_conflicts_input.GetMergeConflictsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_merge_conflicts_output.GetMergeConflictsOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_merge_conflicts

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_merge_conflicts.async_get_merge_conflicts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_merge_conflicts_input.GetMergeConflictsInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["destination_commit_specifier"] = destination_commit_specifier
        input_["source_commit_specifier"] = source_commit_specifier
        input_["merge_option"] = merge_option
        if conflict_detail_level is not None:
            input_["conflict_detail_level"] = conflict_detail_level
        if max_conflict_files is not None:
            input_["max_conflict_files"] = max_conflict_files
        if conflict_resolution_strategy is not None:
            input_["conflict_resolution_strategy"] = conflict_resolution_strategy
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_merge_options(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        conflict_detail_level: Optional[
            "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
        ] = None,
        conflict_resolution_strategy: Optional[
            "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
        ] = None,
    ) -> "aws_sdk_codecommit.types.get_merge_options_output.GetMergeOptionsOutput":
        """<p>Returns information about the merge options available for merging two specified branches. For details about why a merge option is not available, use GetMergeConflicts or DescribeMergeConflicts.</p>

        Args:
            repository_name: <p>The name of the repository that contains the commits about which you want to get merge options.</p>
            source_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            destination_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            conflict_detail_level: <p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>
            conflict_resolution_strategy: <p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_merge_options_input.GetMergeOptionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_merge_options_output.GetMergeOptionsOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_merge_options

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_merge_options.async_get_merge_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_merge_options_input.GetMergeOptionsInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["source_commit_specifier"] = source_commit_specifier
        input_["destination_commit_specifier"] = destination_commit_specifier
        if conflict_detail_level is not None:
            input_["conflict_detail_level"] = conflict_detail_level
        if conflict_resolution_strategy is not None:
            input_["conflict_resolution_strategy"] = conflict_resolution_strategy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_pull_request(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.get_pull_request_output.GetPullRequestOutput":
        """<p>Gets information about a pull request in a specified repository.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_pull_request_input.GetPullRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_pull_request_output.GetPullRequestOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_pull_request

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_pull_request.async_get_pull_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_pull_request_input.GetPullRequestInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_pull_request_approval_states(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        revision_id: "aws_sdk_codecommit.types.revision_id.RevisionId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.get_pull_request_approval_states_output.GetPullRequestApprovalStatesOutput":
        """<p>Gets information about the approval states for a specified pull request. Approval states only apply to pull requests that have one or more approval rules applied to them.</p>

        Args:
            pull_request_id: <p>The system-generated ID for the pull request.</p>
            revision_id: <p>The system-generated ID for the pull request revision.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_pull_request_approval_states_input.GetPullRequestApprovalStatesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_pull_request_approval_states_output.GetPullRequestApprovalStatesOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_pull_request_approval_states

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_pull_request_approval_states.async_get_pull_request_approval_states(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_pull_request_approval_states_input.GetPullRequestApprovalStatesInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_pull_request_override_state(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        revision_id: "aws_sdk_codecommit.types.revision_id.RevisionId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.get_pull_request_override_state_output.GetPullRequestOverrideStateOutput":
        """<p>Returns information about whether approval rules have been set aside (overridden) for a pull request, and if so, the Amazon Resource Name (ARN) of the user or identity that overrode the rules and their requirements for the pull request.</p>

        Args:
            pull_request_id: <p>The ID of the pull request for which you want to get information about whether approval rules have been set aside (overridden).</p>
            revision_id: <p>The system-generated ID of the revision for the pull request. To retrieve the most recent revision ID, use <a>GetPullRequest</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_pull_request_override_state_input.GetPullRequestOverrideStateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_pull_request_override_state_output.GetPullRequestOverrideStateOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_pull_request_override_state

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_pull_request_override_state.async_get_pull_request_override_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_pull_request_override_state_input.GetPullRequestOverrideStateInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_repository(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.get_repository_output.GetRepositoryOutput":
        """<p>Returns information about a repository.</p> <note> <p>The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.</p> </note>

        Args:
            repository_name: <p>The name of the repository to get information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_repository_input.GetRepositoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_repository_output.GetRepositoryOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_repository

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_repository.async_get_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_repository_input.GetRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_repository_triggers(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.get_repository_triggers_output.GetRepositoryTriggersOutput":
        """<p>Gets information about triggers configured for a repository.</p>

        Args:
            repository_name: <p>The name of the repository for which the trigger is configured.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.get_repository_triggers_input.GetRepositoryTriggersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.get_repository_triggers_output.GetRepositoryTriggersOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.get_repository_triggers

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.get_repository_triggers.async_get_repository_triggers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.get_repository_triggers_input.GetRepositoryTriggersInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_approval_rule_templates(
        self,
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_codecommit.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_codecommit.types.list_approval_rule_templates_output.ListApprovalRuleTemplatesOutput":
        """<p>Lists all approval rule templates in the specified Amazon Web Services Region in your Amazon Web Services account. If an Amazon Web Services Region is not specified, the Amazon Web Services Region where you are signed in is used.</p>

        Args:
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.list_approval_rule_templates_input.ListApprovalRuleTemplatesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.list_approval_rule_templates_output.ListApprovalRuleTemplatesOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.list_approval_rule_templates

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.list_approval_rule_templates.async_list_approval_rule_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.list_approval_rule_templates_input.ListApprovalRuleTemplatesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_associated_approval_rule_templates_for_repository(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_codecommit.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_codecommit.types.list_associated_approval_rule_templates_for_repository_output.ListAssociatedApprovalRuleTemplatesForRepositoryOutput":
        """<p>Lists all approval rule templates that are associated with a specified repository.</p>

        Args:
            repository_name: <p>The name of the repository for which you want to list all associated approval rule templates.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.list_associated_approval_rule_templates_for_repository_input.ListAssociatedApprovalRuleTemplatesForRepositoryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.list_associated_approval_rule_templates_for_repository_output.ListAssociatedApprovalRuleTemplatesForRepositoryOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.list_associated_approval_rule_templates_for_repository

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.list_associated_approval_rule_templates_for_repository.async_list_associated_approval_rule_templates_for_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.list_associated_approval_rule_templates_for_repository_input.ListAssociatedApprovalRuleTemplatesForRepositoryInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_branches(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_codecommit.types.list_branches_output.ListBranchesOutput":
        """<p>Gets information about one or more branches in a repository.</p>

        Args:
            repository_name: <p>The name of the repository that contains the branches.</p>
            next_token: <p>An enumeration token that allows the operation to batch the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.list_branches_input.ListBranchesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.list_branches_output.ListBranchesOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.list_branches

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.list_branches.async_list_branches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.list_branches_input.ListBranchesInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_branches(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_codecommit.types.branch_name.BranchName]":
        _token = next_token
        while True:
            _response = await self.list_branches(
                repository_name,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("branches",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_file_commit_history(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        file_path: "aws_sdk_codecommit.types.path.Path",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        commit_specifier: Optional[
            "aws_sdk_codecommit.types.commit_name.CommitName"
        ] = None,
        max_results: Optional["aws_sdk_codecommit.types.limit.Limit"] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_codecommit.types.list_file_commit_history_response.ListFileCommitHistoryResponse":
        """<p>Retrieves a list of commits and changes to a specified file.</p>

        Args:
            repository_name: <p>The name of the repository that contains the file.</p>
            commit_specifier: <p>The fully quaified reference that identifies the commit that contains the file. For example, you can specify a full commit ID, a tag, a branch name, or a reference such as <code>refs/heads/main</code>. If none is provided, the head commit is used.</p>
            file_path: <p>The full path of the file whose history you want to retrieve, including the name of the file.</p>
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results.</p>
            next_token: <p>An enumeration token that allows the operation to batch the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.list_file_commit_history_request.ListFileCommitHistoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.list_file_commit_history_response.ListFileCommitHistoryResponse"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.list_file_commit_history

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.list_file_commit_history.async_list_file_commit_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.list_file_commit_history_request.ListFileCommitHistoryRequest = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        if commit_specifier is not None:
            input_["commit_specifier"] = commit_specifier
        input_["file_path"] = file_path
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_pull_requests(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        author_arn: Optional["aws_sdk_codecommit.types.arn.Arn"] = None,
        pull_request_status: Optional[
            "aws_sdk_codecommit.types.pull_request_status_enum.PullRequestStatusEnum"
        ] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_codecommit.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_codecommit.types.list_pull_requests_output.ListPullRequestsOutput":
        """<p>Returns a list of pull requests for a specified repository. The return list can be refined by pull request status or pull request author ARN.</p>

        Args:
            repository_name: <p>The name of the repository for which you want to list pull requests.</p>
            author_arn: <p>Optional. The Amazon Resource Name (ARN) of the user who created the pull request. If used, this filters the results to pull requests created by that user.</p>
            pull_request_status: <p>Optional. The status of the pull request. If used, this refines the results to the pull requests that match the specified status.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.list_pull_requests_input.ListPullRequestsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.list_pull_requests_output.ListPullRequestsOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.list_pull_requests

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.list_pull_requests.async_list_pull_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.list_pull_requests_input.ListPullRequestsInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        if author_arn is not None:
            input_["author_arn"] = author_arn
        if pull_request_status is not None:
            input_["pull_request_status"] = pull_request_status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_repositories(
        self,
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
        sort_by: Optional["aws_sdk_codecommit.types.sort_by_enum.SortByEnum"] = None,
        order: Optional["aws_sdk_codecommit.types.order_enum.OrderEnum"] = None,
    ) -> "aws_sdk_codecommit.types.list_repositories_output.ListRepositoriesOutput":
        """<p>Gets information about one or more repositories.</p>

        Args:
            next_token: <p>An enumeration token that allows the operation to batch the results of the operation. Batch sizes are 1,000 for list repository operations. When the client sends the token back to CodeCommit, another page of 1,000 records is retrieved.</p>
            sort_by: <p>The criteria used to sort the results of a list repositories operation.</p>
            order: <p>The order in which to sort the results of a list repositories operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.list_repositories_input.ListRepositoriesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.list_repositories_output.ListRepositoriesOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.list_repositories

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.list_repositories.async_list_repositories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.list_repositories_input.ListRepositoriesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if order is not None:
            input_["order"] = order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_repositories(
        self,
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
        sort_by: Optional["aws_sdk_codecommit.types.sort_by_enum.SortByEnum"] = None,
        order: Optional["aws_sdk_codecommit.types.order_enum.OrderEnum"] = None,
    ) -> "AsyncIterator[aws_sdk_codecommit.types.repository_name_id_pair.RepositoryNameIdPair]":
        _token = next_token
        while True:
            _response = await self.list_repositories(
                config_overrides=config_overrides,
                next_token=_token,
                sort_by=sort_by,
                order=order,
            )
            _page = _resolve_path(_response, ("repositories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_repositories_for_approval_rule_template(
        self,
        approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_codecommit.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_codecommit.types.list_repositories_for_approval_rule_template_output.ListRepositoriesForApprovalRuleTemplateOutput":
        """<p>Lists all repositories associated with the specified approval rule template.</p>

        Args:
            approval_rule_template_name: <p>The name of the approval rule template for which you want to list repositories that are associated with that template.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
            max_results: <p>A non-zero, non-negative integer used to limit the number of returned results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.list_repositories_for_approval_rule_template_input.ListRepositoriesForApprovalRuleTemplateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.list_repositories_for_approval_rule_template_output.ListRepositoriesForApprovalRuleTemplateOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.list_repositories_for_approval_rule_template

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.list_repositories_for_approval_rule_template.async_list_repositories_for_approval_rule_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.list_repositories_for_approval_rule_template_input.ListRepositoriesForApprovalRuleTemplateInput = {}  # type: ignore[typeddict-item]
        input_["approval_rule_template_name"] = approval_rule_template_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_codecommit.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        next_token: Optional["aws_sdk_codecommit.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_codecommit.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Gets information about Amazon Web Servicestags for a specified Amazon Resource Name (ARN) in CodeCommit. For a list of valid resources in CodeCommit, see <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats\">CodeCommit Resources and Operations</a> in the<i> CodeCommit User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to get information about tags, if any.</p>
            next_token: <p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def merge_branches_by_fast_forward(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        target_branch: Optional[
            "aws_sdk_codecommit.types.branch_name.BranchName"
        ] = None,
    ) -> "aws_sdk_codecommit.types.merge_branches_by_fast_forward_output.MergeBranchesByFastForwardOutput":
        """<p>Merges two branches using the fast-forward merge strategy.</p>

        Args:
            repository_name: <p>The name of the repository where you want to merge two branches.</p>
            source_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            destination_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            target_branch: <p>The branch where the merge is applied.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.merge_branches_by_fast_forward_input.MergeBranchesByFastForwardInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.merge_branches_by_fast_forward_output.MergeBranchesByFastForwardOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.merge_branches_by_fast_forward

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.merge_branches_by_fast_forward.async_merge_branches_by_fast_forward(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.merge_branches_by_fast_forward_input.MergeBranchesByFastForwardInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["source_commit_specifier"] = source_commit_specifier
        input_["destination_commit_specifier"] = destination_commit_specifier
        if target_branch is not None:
            input_["target_branch"] = target_branch

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def merge_branches_by_squash(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        target_branch: Optional[
            "aws_sdk_codecommit.types.branch_name.BranchName"
        ] = None,
        conflict_detail_level: Optional[
            "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
        ] = None,
        conflict_resolution_strategy: Optional[
            "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
        ] = None,
        author_name: Optional["aws_sdk_codecommit.types.name.Name"] = None,
        email: Optional["aws_sdk_codecommit.types.email.Email"] = None,
        commit_message: Optional["aws_sdk_codecommit.types.message.Message"] = None,
        keep_empty_folders: Optional[
            "aws_sdk_codecommit.types.keep_empty_folders.KeepEmptyFolders"
        ] = None,
        conflict_resolution: Optional[
            "aws_sdk_codecommit.types.conflict_resolution.ConflictResolution"
        ] = None,
    ) -> "aws_sdk_codecommit.types.merge_branches_by_squash_output.MergeBranchesBySquashOutput":
        """<p>Merges two branches using the squash merge strategy.</p>

        Args:
            repository_name: <p>The name of the repository where you want to merge two branches.</p>
            source_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            destination_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            target_branch: <p>The branch where the merge is applied. </p>
            conflict_detail_level: <p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>
            conflict_resolution_strategy: <p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>
            author_name: <p>The name of the author who created the commit. This information is used as both the author and committer for the commit.</p>
            email: <p>The email address of the person merging the branches. This information is used in the commit information for the merge.</p>
            commit_message: <p>The commit message for the merge.</p>
            keep_empty_folders: <p>If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If this is specified as true, a .gitkeep file is created for empty folders. The default is false.</p>
            conflict_resolution: <p>If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.merge_branches_by_squash_input.MergeBranchesBySquashInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.merge_branches_by_squash_output.MergeBranchesBySquashOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.merge_branches_by_squash

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.merge_branches_by_squash.async_merge_branches_by_squash(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.merge_branches_by_squash_input.MergeBranchesBySquashInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["source_commit_specifier"] = source_commit_specifier
        input_["destination_commit_specifier"] = destination_commit_specifier
        if target_branch is not None:
            input_["target_branch"] = target_branch
        if conflict_detail_level is not None:
            input_["conflict_detail_level"] = conflict_detail_level
        if conflict_resolution_strategy is not None:
            input_["conflict_resolution_strategy"] = conflict_resolution_strategy
        if author_name is not None:
            input_["author_name"] = author_name
        if email is not None:
            input_["email"] = email
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if keep_empty_folders is not None:
            input_["keep_empty_folders"] = keep_empty_folders
        if conflict_resolution is not None:
            input_["conflict_resolution"] = conflict_resolution

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def merge_branches_by_three_way(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        source_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        destination_commit_specifier: "aws_sdk_codecommit.types.commit_name.CommitName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        target_branch: Optional[
            "aws_sdk_codecommit.types.branch_name.BranchName"
        ] = None,
        conflict_detail_level: Optional[
            "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
        ] = None,
        conflict_resolution_strategy: Optional[
            "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
        ] = None,
        author_name: Optional["aws_sdk_codecommit.types.name.Name"] = None,
        email: Optional["aws_sdk_codecommit.types.email.Email"] = None,
        commit_message: Optional["aws_sdk_codecommit.types.message.Message"] = None,
        keep_empty_folders: Optional[
            "aws_sdk_codecommit.types.keep_empty_folders.KeepEmptyFolders"
        ] = None,
        conflict_resolution: Optional[
            "aws_sdk_codecommit.types.conflict_resolution.ConflictResolution"
        ] = None,
    ) -> "aws_sdk_codecommit.types.merge_branches_by_three_way_output.MergeBranchesByThreeWayOutput":
        """<p>Merges two specified branches using the three-way merge strategy.</p>

        Args:
            repository_name: <p>The name of the repository where you want to merge two branches.</p>
            source_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            destination_commit_specifier: <p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).</p>
            target_branch: <p>The branch where the merge is applied. </p>
            conflict_detail_level: <p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>
            conflict_resolution_strategy: <p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>
            author_name: <p>The name of the author who created the commit. This information is used as both the author and committer for the commit.</p>
            email: <p>The email address of the person merging the branches. This information is used in the commit information for the merge.</p>
            commit_message: <p>The commit message to include in the commit information for the merge.</p>
            keep_empty_folders: <p>If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a .gitkeep file is created for empty folders. The default is false.</p>
            conflict_resolution: <p>If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.merge_branches_by_three_way_input.MergeBranchesByThreeWayInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.merge_branches_by_three_way_output.MergeBranchesByThreeWayOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.merge_branches_by_three_way

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.merge_branches_by_three_way.async_merge_branches_by_three_way(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.merge_branches_by_three_way_input.MergeBranchesByThreeWayInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["source_commit_specifier"] = source_commit_specifier
        input_["destination_commit_specifier"] = destination_commit_specifier
        if target_branch is not None:
            input_["target_branch"] = target_branch
        if conflict_detail_level is not None:
            input_["conflict_detail_level"] = conflict_detail_level
        if conflict_resolution_strategy is not None:
            input_["conflict_resolution_strategy"] = conflict_resolution_strategy
        if author_name is not None:
            input_["author_name"] = author_name
        if email is not None:
            input_["email"] = email
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if keep_empty_folders is not None:
            input_["keep_empty_folders"] = keep_empty_folders
        if conflict_resolution is not None:
            input_["conflict_resolution"] = conflict_resolution

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def merge_pull_request_by_fast_forward(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        source_commit_id: Optional[
            "aws_sdk_codecommit.types.object_id.ObjectId"
        ] = None,
    ) -> "aws_sdk_codecommit.types.merge_pull_request_by_fast_forward_output.MergePullRequestByFastForwardOutput":
        """<p>Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the fast-forward merge strategy. If the merge is successful, it closes the pull request.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>
            repository_name: <p>The name of the repository where the pull request was created.</p>
            source_commit_id: <p>The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.merge_pull_request_by_fast_forward_input.MergePullRequestByFastForwardInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.merge_pull_request_by_fast_forward_output.MergePullRequestByFastForwardOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.merge_pull_request_by_fast_forward

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.merge_pull_request_by_fast_forward.async_merge_pull_request_by_fast_forward(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.merge_pull_request_by_fast_forward_input.MergePullRequestByFastForwardInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["repository_name"] = repository_name
        if source_commit_id is not None:
            input_["source_commit_id"] = source_commit_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def merge_pull_request_by_squash(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        source_commit_id: Optional[
            "aws_sdk_codecommit.types.object_id.ObjectId"
        ] = None,
        conflict_detail_level: Optional[
            "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
        ] = None,
        conflict_resolution_strategy: Optional[
            "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
        ] = None,
        commit_message: Optional["aws_sdk_codecommit.types.message.Message"] = None,
        author_name: Optional["aws_sdk_codecommit.types.name.Name"] = None,
        email: Optional["aws_sdk_codecommit.types.email.Email"] = None,
        keep_empty_folders: Optional[
            "aws_sdk_codecommit.types.keep_empty_folders.KeepEmptyFolders"
        ] = None,
        conflict_resolution: Optional[
            "aws_sdk_codecommit.types.conflict_resolution.ConflictResolution"
        ] = None,
    ) -> "aws_sdk_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput":
        """<p>Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the squash merge strategy. If the merge is successful, it closes the pull request.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>
            repository_name: <p>The name of the repository where the pull request was created.</p>
            source_commit_id: <p>The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.</p>
            conflict_detail_level: <p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>
            conflict_resolution_strategy: <p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>
            commit_message: <p>The commit message to include in the commit information for the merge.</p>
            author_name: <p>The name of the author who created the commit. This information is used as both the author and committer for the commit.</p>
            email: <p>The email address of the person merging the branches. This information is used in the commit information for the merge.</p>
            keep_empty_folders: <p>If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a .gitkeep file is created for empty folders. The default is false.</p>
            conflict_resolution: <p>If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.merge_pull_request_by_squash_input.MergePullRequestBySquashInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.merge_pull_request_by_squash_output.MergePullRequestBySquashOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.merge_pull_request_by_squash

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.merge_pull_request_by_squash.async_merge_pull_request_by_squash(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.merge_pull_request_by_squash_input.MergePullRequestBySquashInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["repository_name"] = repository_name
        if source_commit_id is not None:
            input_["source_commit_id"] = source_commit_id
        if conflict_detail_level is not None:
            input_["conflict_detail_level"] = conflict_detail_level
        if conflict_resolution_strategy is not None:
            input_["conflict_resolution_strategy"] = conflict_resolution_strategy
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if author_name is not None:
            input_["author_name"] = author_name
        if email is not None:
            input_["email"] = email
        if keep_empty_folders is not None:
            input_["keep_empty_folders"] = keep_empty_folders
        if conflict_resolution is not None:
            input_["conflict_resolution"] = conflict_resolution

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def merge_pull_request_by_three_way(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        source_commit_id: Optional[
            "aws_sdk_codecommit.types.object_id.ObjectId"
        ] = None,
        conflict_detail_level: Optional[
            "aws_sdk_codecommit.types.conflict_detail_level_type_enum.ConflictDetailLevelTypeEnum"
        ] = None,
        conflict_resolution_strategy: Optional[
            "aws_sdk_codecommit.types.conflict_resolution_strategy_type_enum.ConflictResolutionStrategyTypeEnum"
        ] = None,
        commit_message: Optional["aws_sdk_codecommit.types.message.Message"] = None,
        author_name: Optional["aws_sdk_codecommit.types.name.Name"] = None,
        email: Optional["aws_sdk_codecommit.types.email.Email"] = None,
        keep_empty_folders: Optional[
            "aws_sdk_codecommit.types.keep_empty_folders.KeepEmptyFolders"
        ] = None,
        conflict_resolution: Optional[
            "aws_sdk_codecommit.types.conflict_resolution.ConflictResolution"
        ] = None,
    ) -> "aws_sdk_codecommit.types.merge_pull_request_by_three_way_output.MergePullRequestByThreeWayOutput":
        """<p>Attempts to merge the source commit of a pull request into the specified destination branch for that pull request at the specified commit using the three-way merge strategy. If the merge is successful, it closes the pull request.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>
            repository_name: <p>The name of the repository where the pull request was created.</p>
            source_commit_id: <p>The full commit ID of the original or updated commit in the pull request source branch. Pass this value if you want an exception thrown if the current commit ID of the tip of the source branch does not match this commit ID.</p>
            conflict_detail_level: <p>The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.</p>
            conflict_resolution_strategy: <p>Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.</p>
            commit_message: <p>The commit message to include in the commit information for the merge.</p>
            author_name: <p>The name of the author who created the commit. This information is used as both the author and committer for the commit.</p>
            email: <p>The email address of the person merging the branches. This information is used in the commit information for the merge.</p>
            keep_empty_folders: <p>If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a .gitkeep file is created for empty folders. The default is false.</p>
            conflict_resolution: <p>If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.merge_pull_request_by_three_way_input.MergePullRequestByThreeWayInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.merge_pull_request_by_three_way_output.MergePullRequestByThreeWayOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.merge_pull_request_by_three_way

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.merge_pull_request_by_three_way.async_merge_pull_request_by_three_way(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.merge_pull_request_by_three_way_input.MergePullRequestByThreeWayInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["repository_name"] = repository_name
        if source_commit_id is not None:
            input_["source_commit_id"] = source_commit_id
        if conflict_detail_level is not None:
            input_["conflict_detail_level"] = conflict_detail_level
        if conflict_resolution_strategy is not None:
            input_["conflict_resolution_strategy"] = conflict_resolution_strategy
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if author_name is not None:
            input_["author_name"] = author_name
        if email is not None:
            input_["email"] = email
        if keep_empty_folders is not None:
            input_["keep_empty_folders"] = keep_empty_folders
        if conflict_resolution is not None:
            input_["conflict_resolution"] = conflict_resolution

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def override_pull_request_approval_rules(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        revision_id: "aws_sdk_codecommit.types.revision_id.RevisionId",
        override_status: "aws_sdk_codecommit.types.override_status.OverrideStatus",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> None:
        """<p>Sets aside (overrides) all approval rule requirements for a specified pull request.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request for which you want to override all approval rule requirements. To get this information, use <a>GetPullRequest</a>.</p>
            revision_id: <p>The system-generated ID of the most recent revision of the pull request. You cannot override approval rules for anything but the most recent revision of a pull request. To get the revision ID, use GetPullRequest.</p>
            override_status: <p>Whether you want to set aside approval rule requirements for the pull request (OVERRIDE) or revoke a previous override and apply approval rule requirements (REVOKE). REVOKE status is not stored.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.override_pull_request_approval_rules_input.OverridePullRequestApprovalRulesInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_codecommit._operations.code_commit_20150413.override_pull_request_approval_rules

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.override_pull_request_approval_rules.async_override_pull_request_approval_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.override_pull_request_approval_rules_input.OverridePullRequestApprovalRulesInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["revision_id"] = revision_id
        input_["override_status"] = override_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def post_comment_for_compared_commit(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        after_commit_id: "aws_sdk_codecommit.types.commit_id.CommitId",
        content: "aws_sdk_codecommit.types.content.Content",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        before_commit_id: Optional[
            "aws_sdk_codecommit.types.commit_id.CommitId"
        ] = None,
        location: Optional["aws_sdk_codecommit.types.location.Location"] = None,
        client_request_token: Optional[
            "aws_sdk_codecommit.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "aws_sdk_codecommit.types.post_comment_for_compared_commit_output.PostCommentForComparedCommitOutput":
        """<p>Posts a comment on the comparison between two commits.</p>

        Args:
            repository_name: <p>The name of the repository where you want to post a comment on the comparison between commits.</p>
            before_commit_id: <p>To establish the directionality of the comparison, the full commit ID of the before commit. Required for commenting on any commit unless that commit is the initial commit.</p>
            after_commit_id: <p>To establish the directionality of the comparison, the full commit ID of the after commit.</p>
            location: <p>The location of the comparison where you want to comment.</p>
            content: <p>The content of the comment you want to make.</p>
            client_request_token: <p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.post_comment_for_compared_commit_input.PostCommentForComparedCommitInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.post_comment_for_compared_commit_output.PostCommentForComparedCommitOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.post_comment_for_compared_commit

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.post_comment_for_compared_commit.async_post_comment_for_compared_commit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.post_comment_for_compared_commit_input.PostCommentForComparedCommitInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        if before_commit_id is not None:
            input_["before_commit_id"] = before_commit_id
        input_["after_commit_id"] = after_commit_id
        if location is not None:
            input_["location"] = location
        input_["content"] = content
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def post_comment_for_pull_request(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        before_commit_id: "aws_sdk_codecommit.types.commit_id.CommitId",
        after_commit_id: "aws_sdk_codecommit.types.commit_id.CommitId",
        content: "aws_sdk_codecommit.types.content.Content",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        location: Optional["aws_sdk_codecommit.types.location.Location"] = None,
        client_request_token: Optional[
            "aws_sdk_codecommit.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "aws_sdk_codecommit.types.post_comment_for_pull_request_output.PostCommentForPullRequestOutput":
        """<p>Posts a comment on a pull request.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>
            repository_name: <p>The name of the repository where you want to post a comment on a pull request.</p>
            before_commit_id: <p>The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created.</p>
            after_commit_id: <p>The full commit ID of the commit in the source branch that is the current tip of the branch for the pull request when you post the comment.</p>
            location: <p>The location of the change where you want to post your comment. If no location is provided, the comment is posted as a general comment on the pull request difference between the before commit ID and the after commit ID.</p>
            content: <p>The content of your comment on the change.</p>
            client_request_token: <p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.post_comment_for_pull_request_input.PostCommentForPullRequestInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.post_comment_for_pull_request_output.PostCommentForPullRequestOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.post_comment_for_pull_request

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.post_comment_for_pull_request.async_post_comment_for_pull_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.post_comment_for_pull_request_input.PostCommentForPullRequestInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["repository_name"] = repository_name
        input_["before_commit_id"] = before_commit_id
        input_["after_commit_id"] = after_commit_id
        if location is not None:
            input_["location"] = location
        input_["content"] = content
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def post_comment_reply(
        self,
        in_reply_to: "aws_sdk_codecommit.types.comment_id.CommentId",
        content: "aws_sdk_codecommit.types.content.Content",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        client_request_token: Optional[
            "aws_sdk_codecommit.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "aws_sdk_codecommit.types.post_comment_reply_output.PostCommentReplyOutput":
        """<p>Posts a comment in reply to an existing comment on a comparison between commits or a pull request.</p>

        Args:
            in_reply_to: <p>The system-generated ID of the comment to which you want to reply. To get this ID, use <a>GetCommentsForComparedCommit</a> or <a>GetCommentsForPullRequest</a>.</p>
            client_request_token: <p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p>
            content: <p>The contents of your reply to a comment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.post_comment_reply_input.PostCommentReplyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.post_comment_reply_output.PostCommentReplyOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.post_comment_reply

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.post_comment_reply.async_post_comment_reply(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.post_comment_reply_input.PostCommentReplyInput = {}  # type: ignore[typeddict-item]
        input_["in_reply_to"] = in_reply_to
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        input_["content"] = content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_comment_reaction(
        self,
        comment_id: "aws_sdk_codecommit.types.comment_id.CommentId",
        reaction_value: "aws_sdk_codecommit.types.reaction_value.ReactionValue",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> None:
        """<p>Adds or updates a reaction to a specified comment for the user whose identity is used to make the request. You can only add or update a reaction for yourself. You cannot add, modify, or delete a reaction for another user.</p>

        Args:
            comment_id: <p>The ID of the comment to which you want to add or update a reaction.</p>
            reaction_value: <p>The emoji reaction you want to add or update. To remove a reaction, provide a value of blank or null. You can also provide the value of none. For information about emoji reaction values supported in CodeCommit, see the <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-commit-comment.html#emoji-reaction-table\">CodeCommit User Guide</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.put_comment_reaction_input.PutCommentReactionInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_codecommit._operations.code_commit_20150413.put_comment_reaction

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.put_comment_reaction.async_put_comment_reaction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.put_comment_reaction_input.PutCommentReactionInput = {}  # type: ignore[typeddict-item]
        input_["comment_id"] = comment_id
        input_["reaction_value"] = reaction_value

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_file(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        branch_name: "aws_sdk_codecommit.types.branch_name.BranchName",
        file_content: "aws_sdk_codecommit.types.file_content.FileContent",
        file_path: "aws_sdk_codecommit.types.path.Path",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        file_mode: Optional[
            "aws_sdk_codecommit.types.file_mode_type_enum.FileModeTypeEnum"
        ] = None,
        parent_commit_id: Optional[
            "aws_sdk_codecommit.types.commit_id.CommitId"
        ] = None,
        commit_message: Optional["aws_sdk_codecommit.types.message.Message"] = None,
        name: Optional["aws_sdk_codecommit.types.name.Name"] = None,
        email: Optional["aws_sdk_codecommit.types.email.Email"] = None,
    ) -> "aws_sdk_codecommit.types.put_file_output.PutFileOutput":
        """<p>Adds or updates a file in a branch in an CodeCommit repository, and generates a commit for the addition in the specified branch.</p>

        Args:
            repository_name: <p>The name of the repository where you want to add or update the file.</p>
            branch_name: <p>The name of the branch where you want to add or update the file. If this is an empty repository, this branch is created.</p>
            file_content: <p>The content of the file, in binary object format. </p>
            file_path: <p>The name of the file you want to add or update, including the relative path to the file in the repository.</p> <note> <p>If the path does not currently exist in the repository, the path is created as part of adding the file.</p> </note>
            file_mode: <p>The file mode permissions of the blob. Valid file mode permissions are listed here.</p>
            parent_commit_id: <p>The full commit ID of the head commit in the branch where you want to add or update the file. If this is an empty repository, no commit ID is required. If this is not an empty repository, a commit ID is required. </p> <p>The commit ID must match the ID of the head commit at the time of the operation. Otherwise, an error occurs, and the file is not added or updated.</p>
            commit_message: <p>A message about why this file was added or updated. Although it is optional, a message makes the commit history for your repository more useful.</p>
            name: <p>The name of the person adding or updating the file. Although it is optional, a name makes the commit history for your repository more useful.</p>
            email: <p>An email address for the person adding or updating the file.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.put_file_input.PutFileInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.put_file_output.PutFileOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.put_file

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.put_file.async_put_file(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.put_file_input.PutFileInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["branch_name"] = branch_name
        input_["file_content"] = file_content
        input_["file_path"] = file_path
        if file_mode is not None:
            input_["file_mode"] = file_mode
        if parent_commit_id is not None:
            input_["parent_commit_id"] = parent_commit_id
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if name is not None:
            input_["name"] = name
        if email is not None:
            input_["email"] = email

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_repository_triggers(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        triggers: "aws_sdk_codecommit.types.repository_triggers_list.RepositoryTriggersList",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.put_repository_triggers_output.PutRepositoryTriggersOutput":
        """<p>Replaces all triggers for a repository. Used to create or delete triggers.</p>

        Args:
            repository_name: <p>The name of the repository where you want to create or update the trigger.</p>
            triggers: <p>The JSON block of configuration information for each trigger.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.put_repository_triggers_input.PutRepositoryTriggersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.put_repository_triggers_output.PutRepositoryTriggersOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.put_repository_triggers

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.put_repository_triggers.async_put_repository_triggers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.put_repository_triggers_input.PutRepositoryTriggersInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["triggers"] = triggers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_codecommit.types.resource_arn.ResourceArn",
        tags: "aws_sdk_codecommit.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> None:
        """<p>Adds or updates tags for a resource in CodeCommit. For a list of valid resources in CodeCommit, see <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats\">CodeCommit Resources and Operations</a> in the <i>CodeCommit User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which you want to add or update tags.</p>
            tags: <p>The key-value pair to use when tagging this repository.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_codecommit._operations.code_commit_20150413.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def test_repository_triggers(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        triggers: "aws_sdk_codecommit.types.repository_triggers_list.RepositoryTriggersList",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.test_repository_triggers_output.TestRepositoryTriggersOutput":
        """<p>Tests the functionality of repository triggers by sending information to the trigger target. If real data is available in the repository, the test sends data from the last commit. If no data is available, sample data is generated.</p>

        Args:
            repository_name: <p>The name of the repository in which to test the triggers.</p>
            triggers: <p>The list of triggers to test.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.test_repository_triggers_input.TestRepositoryTriggersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.test_repository_triggers_output.TestRepositoryTriggersOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.test_repository_triggers

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.test_repository_triggers.async_test_repository_triggers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.test_repository_triggers_input.TestRepositoryTriggersInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["triggers"] = triggers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_codecommit.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_codecommit.types.tag_keys_list.TagKeysList",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> None:
        """<p>Removes tags for a resource in CodeCommit. For a list of valid resources in CodeCommit, see <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats\">CodeCommit Resources and Operations</a> in the <i>CodeCommit User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which you want to remove tags.</p>
            tag_keys: <p>The tag key for each tag that you want to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_codecommit._operations.code_commit_20150413.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_approval_rule_template_content(
        self,
        approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        new_rule_content: "aws_sdk_codecommit.types.approval_rule_template_content.ApprovalRuleTemplateContent",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        existing_rule_content_sha256: Optional[
            "aws_sdk_codecommit.types.rule_content_sha256.RuleContentSha256"
        ] = None,
    ) -> "aws_sdk_codecommit.types.update_approval_rule_template_content_output.UpdateApprovalRuleTemplateContentOutput":
        """<p>Updates the content of an approval rule template. You can change the number of required approvals, the membership of the approval rule, and whether an approval pool is defined.</p>

        Args:
            approval_rule_template_name: <p>The name of the approval rule template where you want to update the content of the rule. </p>
            new_rule_content: <p>The content that replaces the existing content of the rule. Content statements must be complete. You cannot provide only the changes.</p>
            existing_rule_content_sha256: <p>The SHA-256 hash signature for the content of the approval rule. You can retrieve this information by using <a>GetPullRequest</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_approval_rule_template_content_input.UpdateApprovalRuleTemplateContentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.update_approval_rule_template_content_output.UpdateApprovalRuleTemplateContentOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_approval_rule_template_content

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_approval_rule_template_content.async_update_approval_rule_template_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_approval_rule_template_content_input.UpdateApprovalRuleTemplateContentInput = {}  # type: ignore[typeddict-item]
        input_["approval_rule_template_name"] = approval_rule_template_name
        input_["new_rule_content"] = new_rule_content
        if existing_rule_content_sha256 is not None:
            input_["existing_rule_content_sha256"] = existing_rule_content_sha256

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_approval_rule_template_description(
        self,
        approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        approval_rule_template_description: "aws_sdk_codecommit.types.approval_rule_template_description.ApprovalRuleTemplateDescription",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.update_approval_rule_template_description_output.UpdateApprovalRuleTemplateDescriptionOutput":
        """<p>Updates the description for a specified approval rule template.</p>

        Args:
            approval_rule_template_name: <p>The name of the template for which you want to update the description.</p>
            approval_rule_template_description: <p>The updated description of the approval rule template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_approval_rule_template_description_input.UpdateApprovalRuleTemplateDescriptionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.update_approval_rule_template_description_output.UpdateApprovalRuleTemplateDescriptionOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_approval_rule_template_description

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_approval_rule_template_description.async_update_approval_rule_template_description(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_approval_rule_template_description_input.UpdateApprovalRuleTemplateDescriptionInput = {}  # type: ignore[typeddict-item]
        input_["approval_rule_template_name"] = approval_rule_template_name
        input_["approval_rule_template_description"] = (
            approval_rule_template_description
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_approval_rule_template_name(
        self,
        old_approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        new_approval_rule_template_name: "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.update_approval_rule_template_name_output.UpdateApprovalRuleTemplateNameOutput":
        """<p>Updates the name of a specified approval rule template.</p>

        Args:
            old_approval_rule_template_name: <p>The current name of the approval rule template.</p>
            new_approval_rule_template_name: <p>The new name you want to apply to the approval rule template.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_approval_rule_template_name_input.UpdateApprovalRuleTemplateNameInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.update_approval_rule_template_name_output.UpdateApprovalRuleTemplateNameOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_approval_rule_template_name

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_approval_rule_template_name.async_update_approval_rule_template_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_approval_rule_template_name_input.UpdateApprovalRuleTemplateNameInput = {}  # type: ignore[typeddict-item]
        input_["old_approval_rule_template_name"] = old_approval_rule_template_name
        input_["new_approval_rule_template_name"] = new_approval_rule_template_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_comment(
        self,
        comment_id: "aws_sdk_codecommit.types.comment_id.CommentId",
        content: "aws_sdk_codecommit.types.content.Content",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.update_comment_output.UpdateCommentOutput":
        """<p>Replaces the contents of a comment.</p>

        Args:
            comment_id: <p>The system-generated ID of the comment you want to update. To get this ID, use <a>GetCommentsForComparedCommit</a> or <a>GetCommentsForPullRequest</a>.</p>
            content: <p>The updated content to replace the existing content of the comment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_comment_input.UpdateCommentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.update_comment_output.UpdateCommentOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_comment

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_comment.async_update_comment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_comment_input.UpdateCommentInput = {}  # type: ignore[typeddict-item]
        input_["comment_id"] = comment_id
        input_["content"] = content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_default_branch(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        default_branch_name: "aws_sdk_codecommit.types.branch_name.BranchName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> None:
        """<p>Sets or changes the default branch name for the specified repository.</p> <note> <p>If you use this operation to change the default branch name to the current default branch name, a success message is returned even though the default branch did not change.</p> </note>

        Args:
            repository_name: <p>The name of the repository for which you want to set or change the default branch.</p>
            default_branch_name: <p>The name of the branch to set as the default branch.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_default_branch_input.UpdateDefaultBranchInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_default_branch

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_default_branch.async_update_default_branch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_default_branch_input.UpdateDefaultBranchInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["default_branch_name"] = default_branch_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_pull_request_approval_rule_content(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        approval_rule_name: "aws_sdk_codecommit.types.approval_rule_name.ApprovalRuleName",
        new_rule_content: "aws_sdk_codecommit.types.approval_rule_content.ApprovalRuleContent",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        existing_rule_content_sha256: Optional[
            "aws_sdk_codecommit.types.rule_content_sha256.RuleContentSha256"
        ] = None,
    ) -> "aws_sdk_codecommit.types.update_pull_request_approval_rule_content_output.UpdatePullRequestApprovalRuleContentOutput":
        """<p>Updates the structure of an approval rule created specifically for a pull request. For example, you can change the number of required approvers and the approval pool for approvers. </p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request.</p>
            approval_rule_name: <p>The name of the approval rule you want to update.</p>
            existing_rule_content_sha256: <p>The SHA-256 hash signature for the content of the approval rule. You can retrieve this information by using <a>GetPullRequest</a>.</p>
            new_rule_content: <p>The updated content for the approval rule.</p> <note> <p>When you update the content of the approval rule, you can specify approvers in an approval pool in one of two ways:</p> <ul> <li> <p> <b>CodeCommitApprovers</b>: This option only requires an Amazon Web Services account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the Amazon Web Services account <i>123456789012</i> and <i>Mary_Major</i>, all of the following are counted as approvals coming from that user:</p> <ul> <li> <p>An IAM user in the account (arn:aws:iam::<i>123456789012</i>:user/<i>Mary_Major</i>)</p> </li> <li> <p>A federated user identified in IAM as Mary_Major (arn:aws:sts::<i>123456789012</i>:federated-user/<i>Mary_Major</i>)</p> </li> </ul> <p>This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of <i>Mary_Major</i> (arn:aws:sts::<i>123456789012</i>:assumed-role/CodeCommitReview/<i>Mary_Major</i>) unless you include a wildcard (*Mary_Major).</p> </li> <li> <p> <b>Fully qualified ARN</b>: This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role. </p> </li> </ul> <p>For more information about IAM ARNs, wildcards, and formats, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM Identifiers</a> in the <i>IAM User Guide</i>.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_pull_request_approval_rule_content_input.UpdatePullRequestApprovalRuleContentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.update_pull_request_approval_rule_content_output.UpdatePullRequestApprovalRuleContentOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_pull_request_approval_rule_content

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_pull_request_approval_rule_content.async_update_pull_request_approval_rule_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_pull_request_approval_rule_content_input.UpdatePullRequestApprovalRuleContentInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["approval_rule_name"] = approval_rule_name
        if existing_rule_content_sha256 is not None:
            input_["existing_rule_content_sha256"] = existing_rule_content_sha256
        input_["new_rule_content"] = new_rule_content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_pull_request_approval_state(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        revision_id: "aws_sdk_codecommit.types.revision_id.RevisionId",
        approval_state: "aws_sdk_codecommit.types.approval_state.ApprovalState",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> None:
        """<p>Updates the state of a user's approval on a pull request. The user is derived from the signed-in account when the request is made.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request.</p>
            revision_id: <p>The system-generated ID of the revision.</p>
            approval_state: <p>The approval state to associate with the user on the pull request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_pull_request_approval_state_input.UpdatePullRequestApprovalStateInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_pull_request_approval_state

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_pull_request_approval_state.async_update_pull_request_approval_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_pull_request_approval_state_input.UpdatePullRequestApprovalStateInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["revision_id"] = revision_id
        input_["approval_state"] = approval_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_pull_request_description(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        description: "aws_sdk_codecommit.types.description.Description",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.update_pull_request_description_output.UpdatePullRequestDescriptionOutput":
        """<p>Replaces the contents of the description of a pull request.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>
            description: <p>The updated content of the description for the pull request. This content replaces the existing description.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_pull_request_description_input.UpdatePullRequestDescriptionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.update_pull_request_description_output.UpdatePullRequestDescriptionOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_pull_request_description

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_pull_request_description.async_update_pull_request_description(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_pull_request_description_input.UpdatePullRequestDescriptionInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_pull_request_status(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        pull_request_status: "aws_sdk_codecommit.types.pull_request_status_enum.PullRequestStatusEnum",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.update_pull_request_status_output.UpdatePullRequestStatusOutput":
        """<p>Updates the status of a pull request. </p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>
            pull_request_status: <p>The status of the pull request. The only valid operations are to update the status from <code>OPEN</code> to <code>OPEN</code>, <code>OPEN</code> to <code>CLOSED</code> or from <code>CLOSED</code> to <code>CLOSED</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_pull_request_status_input.UpdatePullRequestStatusInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.update_pull_request_status_output.UpdatePullRequestStatusOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_pull_request_status

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_pull_request_status.async_update_pull_request_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_pull_request_status_input.UpdatePullRequestStatusInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["pull_request_status"] = pull_request_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_pull_request_title(
        self,
        pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId",
        title: "aws_sdk_codecommit.types.title.Title",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.update_pull_request_title_output.UpdatePullRequestTitleOutput":
        """<p>Replaces the title of a pull request.</p>

        Args:
            pull_request_id: <p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>
            title: <p>The updated title of the pull request. This replaces the existing title.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_pull_request_title_input.UpdatePullRequestTitleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.update_pull_request_title_output.UpdatePullRequestTitleOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_pull_request_title

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_pull_request_title.async_update_pull_request_title(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_pull_request_title_input.UpdatePullRequestTitleInput = {}  # type: ignore[typeddict-item]
        input_["pull_request_id"] = pull_request_id
        input_["title"] = title

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_repository_description(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
        repository_description: Optional[
            "aws_sdk_codecommit.types.repository_description.RepositoryDescription"
        ] = None,
    ) -> None:
        """<p>Sets or changes the comment or description for a repository.</p> <note> <p>The description field for a repository accepts all HTML characters and all valid Unicode characters. Applications that do not HTML-encode the description and display it in a webpage can expose users to potentially malicious code. Make sure that you HTML-encode the description field in any application that uses this API to display the repository description on a webpage.</p> </note>

        Args:
            repository_name: <p>The name of the repository to set or change the comment or description for.</p>
            repository_description: <p>The new comment or description for the specified repository. Repository descriptions are limited to 1,000 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_repository_description_input.UpdateRepositoryDescriptionInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_repository_description

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_repository_description.async_update_repository_description(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_repository_description_input.UpdateRepositoryDescriptionInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        if repository_description is not None:
            input_["repository_description"] = repository_description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_repository_encryption_key(
        self,
        repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        kms_key_id: "aws_sdk_codecommit.types.kms_key_id.KmsKeyId",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> "aws_sdk_codecommit.types.update_repository_encryption_key_output.UpdateRepositoryEncryptionKeyOutput":
        """<p>Updates the Key Management Service encryption key used to encrypt and decrypt a CodeCommit repository.</p>

        Args:
            repository_name: <p>The name of the repository for which you want to update the KMS encryption key used to encrypt and decrypt the repository.</p>
            kms_key_id: <p>The ID of the encryption key. You can view the ID of an encryption key in the KMS console, or use the KMS APIs to programmatically retrieve a key ID. For more information about acceptable values for keyID, see <a href=\"https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html#KMS-Decrypt-request-KeyId\">KeyId</a> in the Decrypt API description in the <i>Key Management Service API Reference</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_repository_encryption_key_input.UpdateRepositoryEncryptionKeyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecommit.types.update_repository_encryption_key_output.UpdateRepositoryEncryptionKeyOutput"
        ]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_repository_encryption_key

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_repository_encryption_key.async_update_repository_encryption_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_repository_encryption_key_input.UpdateRepositoryEncryptionKeyInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_repository_name(
        self,
        old_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        new_name: "aws_sdk_codecommit.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncCodeCommitClientConfig] = None,
    ) -> None:
        """<p>Renames a repository. The repository name must be unique across the calling Amazon Web Services account. Repository names are limited to 100 alphanumeric, dash, and underscore characters, and cannot include certain characters. The suffix .git is prohibited. For more information about the limits on repository names, see <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/limits.html\">Quotas</a> in the CodeCommit User Guide.</p>

        Args:
            old_name: <p>The current name of the repository.</p>
            new_name: <p>The new name for the repository.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecommit.types.update_repository_name_input.UpdateRepositoryNameInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_codecommit._operations.code_commit_20150413.update_repository_name

            (
                output,
                http_response,
            ) = await aws_sdk_codecommit._operations.code_commit_20150413.update_repository_name.async_update_repository_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_codecommit.types.update_repository_name_input.UpdateRepositoryNameInput = {}  # type: ignore[typeddict-item]
        input_["old_name"] = old_name
        input_["new_name"] = new_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
