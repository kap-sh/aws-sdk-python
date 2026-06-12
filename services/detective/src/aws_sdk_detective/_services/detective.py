"""Generated from Smithy shape ``com.amazonaws.detective#AmazonDetective``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_detective._auth._signers
import aws_sdk_detective._auth._sigv4
from aws_sdk_detective._auth._identity import Credentials
from aws_sdk_detective._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_detective._auth._zapros_handler import AuthMiddleware
from aws_sdk_detective._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_detective.types.accept_invitation_request
    import aws_sdk_detective.types.account_id
    import aws_sdk_detective.types.account_id_extended_list
    import aws_sdk_detective.types.account_id_list
    import aws_sdk_detective.types.account_list
    import aws_sdk_detective.types.ai_pagination_token
    import aws_sdk_detective.types.batch_get_graph_member_datasources_request
    import aws_sdk_detective.types.batch_get_graph_member_datasources_response
    import aws_sdk_detective.types.batch_get_membership_datasources_request
    import aws_sdk_detective.types.batch_get_membership_datasources_response
    import aws_sdk_detective.types.boolean
    import aws_sdk_detective.types.create_graph_request
    import aws_sdk_detective.types.create_graph_response
    import aws_sdk_detective.types.create_members_request
    import aws_sdk_detective.types.create_members_response
    import aws_sdk_detective.types.datasource_package_list
    import aws_sdk_detective.types.delete_graph_request
    import aws_sdk_detective.types.delete_members_request
    import aws_sdk_detective.types.delete_members_response
    import aws_sdk_detective.types.describe_organization_configuration_request
    import aws_sdk_detective.types.describe_organization_configuration_response
    import aws_sdk_detective.types.disassociate_membership_request
    import aws_sdk_detective.types.email_message
    import aws_sdk_detective.types.enable_organization_admin_account_request
    import aws_sdk_detective.types.entity_arn
    import aws_sdk_detective.types.filter_criteria
    import aws_sdk_detective.types.get_investigation_request
    import aws_sdk_detective.types.get_investigation_response
    import aws_sdk_detective.types.get_members_request
    import aws_sdk_detective.types.get_members_response
    import aws_sdk_detective.types.graph_arn
    import aws_sdk_detective.types.graph_arn_list
    import aws_sdk_detective.types.indicator_type
    import aws_sdk_detective.types.investigation_id
    import aws_sdk_detective.types.list_datasource_packages_request
    import aws_sdk_detective.types.list_datasource_packages_response
    import aws_sdk_detective.types.list_graphs_request
    import aws_sdk_detective.types.list_graphs_response
    import aws_sdk_detective.types.list_indicators_request
    import aws_sdk_detective.types.list_indicators_response
    import aws_sdk_detective.types.list_investigations_request
    import aws_sdk_detective.types.list_investigations_response
    import aws_sdk_detective.types.list_invitations_request
    import aws_sdk_detective.types.list_invitations_response
    import aws_sdk_detective.types.list_members_request
    import aws_sdk_detective.types.list_members_response
    import aws_sdk_detective.types.list_organization_admin_accounts_request
    import aws_sdk_detective.types.list_organization_admin_accounts_response
    import aws_sdk_detective.types.list_tags_for_resource_request
    import aws_sdk_detective.types.list_tags_for_resource_response
    import aws_sdk_detective.types.max_results
    import aws_sdk_detective.types.member_results_limit
    import aws_sdk_detective.types.pagination_token
    import aws_sdk_detective.types.reject_invitation_request
    import aws_sdk_detective.types.sort_criteria
    import aws_sdk_detective.types.start_investigation_request
    import aws_sdk_detective.types.start_investigation_response
    import aws_sdk_detective.types.start_monitoring_member_request
    import aws_sdk_detective.types.state
    import aws_sdk_detective.types.tag_key_list
    import aws_sdk_detective.types.tag_map
    import aws_sdk_detective.types.tag_resource_request
    import aws_sdk_detective.types.tag_resource_response
    import aws_sdk_detective.types.timestamp
    import aws_sdk_detective.types.untag_resource_request
    import aws_sdk_detective.types.untag_resource_response
    import aws_sdk_detective.types.update_datasource_packages_request
    import aws_sdk_detective.types.update_investigation_state_request
    import aws_sdk_detective.types.update_organization_configuration_request


class DetectiveClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class DetectiveClient:
    """A client for the ``Detective`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = DetectiveClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[DetectiveClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DetectiveClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def accept_invitation(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> None:
        """<p>Accepts an invitation for the member account to contribute data to a behavior graph. This operation can only be called by an invited member account. </p> <p>The request provides the ARN of behavior graph.</p> <p>The member account status in the graph must be <code>INVITED</code>.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph that the member account is accepting the invitation for.</p> <p>The member account status in the behavior graph must be <code>INVITED</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.accept_invitation_request.AcceptInvitationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_detective._operations.amazon_detective.accept_invitation

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.accept_invitation.accept_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.accept_invitation_request.AcceptInvitationRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_graph_member_datasources(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        account_ids: "aws_sdk_detective.types.account_id_extended_list.AccountIdExtendedList",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> "aws_sdk_detective.types.batch_get_graph_member_datasources_response.BatchGetGraphMemberDatasourcesResponse":
        """<p>Gets data source package information for the behavior graph.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph.</p>
            account_ids: <p>The list of Amazon Web Services accounts to get data source package information on.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.batch_get_graph_member_datasources_request.BatchGetGraphMemberDatasourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.batch_get_graph_member_datasources_response.BatchGetGraphMemberDatasourcesResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.batch_get_graph_member_datasources

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.batch_get_graph_member_datasources.batch_get_graph_member_datasources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.batch_get_graph_member_datasources_request.BatchGetGraphMemberDatasourcesRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        input["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_membership_datasources(
        self,
        graph_arns: "aws_sdk_detective.types.graph_arn_list.GraphArnList",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> "aws_sdk_detective.types.batch_get_membership_datasources_response.BatchGetMembershipDatasourcesResponse":
        """<p>Gets information on the data source package history for an account.</p>

        Args:
            graph_arns: <p>The ARN of the behavior graph.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.batch_get_membership_datasources_request.BatchGetMembershipDatasourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.batch_get_membership_datasources_response.BatchGetMembershipDatasourcesResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.batch_get_membership_datasources

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.batch_get_membership_datasources.batch_get_membership_datasources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.batch_get_membership_datasources_request.BatchGetMembershipDatasourcesRequest = {}  # type: ignore[typeddict-item]
        input["graph_arns"] = graph_arns

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_graph(
        self,
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
        tags: Optional["aws_sdk_detective.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_detective.types.create_graph_response.CreateGraphResponse":
        """<p>Creates a new behavior graph for the calling account, and sets that account as the administrator account. This operation is called by the account that is enabling Detective.</p> <p>The operation also enables Detective for the calling account in the currently selected Region. It returns the ARN of the new behavior graph.</p> <p> <code>CreateGraph</code> triggers a process to create the corresponding data tables for the new behavior graph.</p> <p>An account can only be the administrator account for one behavior graph within a Region. If the same account calls <code>CreateGraph</code> with the same administrator account, it always returns the same behavior graph ARN. It does not create a new behavior graph.</p>

        Args:
            tags: <p>The tags to assign to the new behavior graph. You can add up to 50 tags. For each tag, you provide the tag key and the tag value. Each tag key can contain up to 128 characters. Each tag value can contain up to 256 characters.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.create_graph_request.CreateGraphRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.create_graph_response.CreateGraphResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.create_graph

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.create_graph.create_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.create_graph_request.CreateGraphRequest = {}  # type: ignore[typeddict-item]
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_members(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        accounts: "aws_sdk_detective.types.account_list.AccountList",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
        message: Optional["aws_sdk_detective.types.email_message.EmailMessage"] = None,
        disable_email_notification: Optional[
            "aws_sdk_detective.types.boolean.Boolean"
        ] = None,
    ) -> "aws_sdk_detective.types.create_members_response.CreateMembersResponse":
        """<p> <code>CreateMembers</code> is used to send invitations to accounts. For the organization behavior graph, the Detective administrator account uses <code>CreateMembers</code> to enable organization accounts as member accounts.</p> <p>For invited accounts, <code>CreateMembers</code> sends a request to invite the specified Amazon Web Services accounts to be member accounts in the behavior graph. This operation can only be called by the administrator account for a behavior graph. </p> <p> <code>CreateMembers</code> verifies the accounts and then invites the verified accounts. The administrator can optionally specify to not send invitation emails to the member accounts. This would be used when the administrator manages their member accounts centrally.</p> <p>For organization accounts in the organization behavior graph, <code>CreateMembers</code> attempts to enable the accounts. The organization accounts do not receive invitations.</p> <p>The request provides the behavior graph ARN and the list of accounts to invite or to enable.</p> <p>The response separates the requested accounts into two lists:</p> <ul> <li> <p>The accounts that <code>CreateMembers</code> was able to process. For invited accounts, includes member accounts that are being verified, that have passed verification and are to be invited, and that have failed verification. For organization accounts in the organization behavior graph, includes accounts that can be enabled and that cannot be enabled.</p> </li> <li> <p>The accounts that <code>CreateMembers</code> was unable to process. This list includes accounts that were already invited to be member accounts in the behavior graph.</p> </li> </ul>

        Args:
            graph_arn: <p>The ARN of the behavior graph.</p>
            message: <p>Customized message text to include in the invitation email message to the invited member accounts.</p>
            disable_email_notification: <p>if set to <code>true</code>, then the invited accounts do not receive email notifications. By default, this is set to <code>false</code>, and the invited accounts receive email notifications.</p> <p>Organization accounts in the organization behavior graph do not receive email notifications.</p>
            accounts: <p>The list of Amazon Web Services accounts to invite or to enable. You can invite or enable up to 50 accounts at a time. For each invited account, the account list contains the account identifier and the Amazon Web Services account root user email address. For organization accounts in the organization behavior graph, the email address is not required.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.create_members_request.CreateMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.create_members_response.CreateMembersResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.create_members

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.create_members.create_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.create_members_request.CreateMembersRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        if message is not None:
            input["message"] = message
        if disable_email_notification is not None:
            input["disable_email_notification"] = disable_email_notification
        input["accounts"] = accounts

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_graph(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> None:
        """<p>Disables the specified behavior graph and queues it to be deleted. This operation removes the behavior graph from each member account's list of behavior graphs.</p> <p> <code>DeleteGraph</code> can only be called by the administrator account for a behavior graph.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph to disable.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.delete_graph_request.DeleteGraphRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_detective._operations.amazon_detective.delete_graph

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.delete_graph.delete_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.delete_graph_request.DeleteGraphRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_members(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        account_ids: "aws_sdk_detective.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> "aws_sdk_detective.types.delete_members_response.DeleteMembersResponse":
        """<p>Removes the specified member accounts from the behavior graph. The removed accounts no longer contribute data to the behavior graph. This operation can only be called by the administrator account for the behavior graph.</p> <p>For invited accounts, the removed accounts are deleted from the list of accounts in the behavior graph. To restore the account, the administrator account must send another invitation.</p> <p>For organization accounts in the organization behavior graph, the Detective administrator account can always enable the organization account again. Organization accounts that are not enabled as member accounts are not included in the <code>ListMembers</code> results for the organization behavior graph.</p> <p>An administrator account cannot use <code>DeleteMembers</code> to remove their own account from the behavior graph. To disable a behavior graph, the administrator account uses the <code>DeleteGraph</code> API method.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph to remove members from.</p>
            account_ids: <p>The list of Amazon Web Services account identifiers for the member accounts to remove from the behavior graph. You can remove up to 50 member accounts at a time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.delete_members_request.DeleteMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.delete_members_response.DeleteMembersResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.delete_members

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.delete_members.delete_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.delete_members_request.DeleteMembersRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        input["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_organization_configuration(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> "aws_sdk_detective.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse":
        """<p>Returns information about the configuration for the organization behavior graph. Currently indicates whether to automatically enable new organization accounts as member accounts.</p> <p>Can only be called by the Detective administrator account for the organization. </p>

        Args:
            graph_arn: <p>The ARN of the organization behavior graph.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.describe_organization_configuration_response.DescribeOrganizationConfigurationResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.describe_organization_configuration

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.describe_organization_configuration.describe_organization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.describe_organization_configuration_request.DescribeOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable_organization_admin_account(
        self, *, config_overrides: Optional[DetectiveClientConfig] = None
    ) -> None:
        """<p>Removes the Detective administrator account in the current Region. Deletes the organization behavior graph.</p> <p>Can only be called by the organization management account.</p> <p>Removing the Detective administrator account does not affect the delegated administrator account for Detective in Organizations.</p> <p>To remove the delegated administrator account in Organizations, use the Organizations API. Removing the delegated administrator account also removes the Detective administrator account in all Regions, except for Regions where the Detective administrator account is the organization management account.</p>"""

        def _handler(req: "OperationRequest[None]") -> OperationResponse[None]:
            import aws_sdk_detective._operations.amazon_detective.disable_organization_admin_account

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.disable_organization_admin_account.disable_organization_admin_account(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_membership(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> None:
        """<p>Removes the member account from the specified behavior graph. This operation can only be called by an invited member account that has the <code>ENABLED</code> status.</p> <p> <code>DisassociateMembership</code> cannot be called by an organization account in the organization behavior graph. For the organization behavior graph, the Detective administrator account determines which organization accounts to enable or disable as member accounts.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph to remove the member account from.</p> <p>The member account's member status in the behavior graph must be <code>ENABLED</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.disassociate_membership_request.DisassociateMembershipRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_detective._operations.amazon_detective.disassociate_membership

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.disassociate_membership.disassociate_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.disassociate_membership_request.DisassociateMembershipRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_organization_admin_account(
        self,
        account_id: "aws_sdk_detective.types.account_id.AccountId",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> None:
        """<p>Designates the Detective administrator account for the organization in the current Region.</p> <p>If the account does not have Detective enabled, then enables Detective for that account and creates a new behavior graph.</p> <p>Can only be called by the organization management account.</p> <p>If the organization has a delegated administrator account in Organizations, then the Detective administrator account must be either the delegated administrator account or the organization management account.</p> <p>If the organization does not have a delegated administrator account in Organizations, then you can choose any account in the organization. If you choose an account other than the organization management account, Detective calls Organizations to make that account the delegated administrator account for Detective. The organization management account cannot be the delegated administrator account.</p>

        Args:
            account_id: <p>The Amazon Web Services account identifier of the account to designate as the Detective administrator account for the organization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_detective._operations.amazon_detective.enable_organization_admin_account

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.enable_organization_admin_account.enable_organization_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.enable_organization_admin_account_request.EnableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
        input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_investigation(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        investigation_id: "aws_sdk_detective.types.investigation_id.InvestigationId",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> "aws_sdk_detective.types.get_investigation_response.GetInvestigationResponse":
        """<p>Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident. <code>GetInvestigation</code> returns the investigation results of an investigation for a behavior graph. </p>

        Args:
            graph_arn: <p>The Amazon Resource Name (ARN) of the behavior graph.</p>
            investigation_id: <p>The investigation ID of the investigation report.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.get_investigation_request.GetInvestigationRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.get_investigation_response.GetInvestigationResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.get_investigation

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.get_investigation.get_investigation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.get_investigation_request.GetInvestigationRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        input["investigation_id"] = investigation_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_members(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        account_ids: "aws_sdk_detective.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> "aws_sdk_detective.types.get_members_response.GetMembersResponse":
        """<p>Returns the membership details for specified member accounts for a behavior graph.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph for which to request the member details.</p>
            account_ids: <p>The list of Amazon Web Services account identifiers for the member account for which to return member details. You can request details for up to 50 member accounts at a time.</p> <p>You cannot use <code>GetMembers</code> to retrieve information about member accounts that were removed from the behavior graph.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.get_members_request.GetMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.get_members_response.GetMembersResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.get_members

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.get_members.get_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.get_members_request.GetMembersRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        input["account_ids"] = account_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_datasource_packages(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
        next_token: Optional[
            "aws_sdk_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "aws_sdk_detective.types.list_datasource_packages_response.ListDatasourcePackagesResponse":
        """<p>Lists data source packages in the behavior graph.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph.</p>
            next_token: <p>For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.list_datasource_packages_request.ListDatasourcePackagesRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.list_datasource_packages_response.ListDatasourcePackagesResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.list_datasource_packages

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.list_datasource_packages.list_datasource_packages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.list_datasource_packages_request.ListDatasourcePackagesRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_graphs(
        self,
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
        next_token: Optional[
            "aws_sdk_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "aws_sdk_detective.types.list_graphs_response.ListGraphsResponse":
        """<p>Returns the list of behavior graphs that the calling account is an administrator account of. This operation can only be called by an administrator account.</p> <p>Because an account can currently only be the administrator of one behavior graph within a Region, the results always contain a single behavior graph.</p>

        Args:
            next_token: <p>For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.</p>
            max_results: <p>The maximum number of graphs to return at a time. The total must be less than the overall limit on the number of results to return, which is currently 200.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.list_graphs_request.ListGraphsRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.list_graphs_response.ListGraphsResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.list_graphs

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.list_graphs.list_graphs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.list_graphs_request.ListGraphsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_indicators(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        investigation_id: "aws_sdk_detective.types.investigation_id.InvestigationId",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
        indicator_type: Optional[
            "aws_sdk_detective.types.indicator_type.IndicatorType"
        ] = None,
        next_token: Optional[
            "aws_sdk_detective.types.ai_pagination_token.AiPaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_detective.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_detective.types.list_indicators_response.ListIndicatorsResponse":
        """<p>Gets the indicators from an investigation. You can use the information from the indicators to determine if an IAM user and/or IAM role is involved in an unusual activity that could indicate malicious behavior and its impact.</p>

        Args:
            graph_arn: <p>The Amazon Resource Name (ARN) of the behavior graph.</p>
            investigation_id: <p>The investigation ID of the investigation report.</p>
            indicator_type: <p>For the list of indicators of compromise that are generated by Detective investigations, see <a href=\"https://docs.aws.amazon.com/detective/latest/userguide/detective-investigation-about.html\">Detective investigations</a>.</p>
            next_token: <p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return a Validation Exception error.</p>
            max_results: <p>Lists the maximum number of indicators in a page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.list_indicators_request.ListIndicatorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.list_indicators_response.ListIndicatorsResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.list_indicators

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.list_indicators.list_indicators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.list_indicators_request.ListIndicatorsRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        input["investigation_id"] = investigation_id
        if indicator_type is not None:
            input["indicator_type"] = indicator_type
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_investigations(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
        next_token: Optional[
            "aws_sdk_detective.types.ai_pagination_token.AiPaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_detective.types.max_results.MaxResults"] = None,
        filter_criteria: Optional[
            "aws_sdk_detective.types.filter_criteria.FilterCriteria"
        ] = None,
        sort_criteria: Optional[
            "aws_sdk_detective.types.sort_criteria.SortCriteria"
        ] = None,
    ) -> "aws_sdk_detective.types.list_investigations_response.ListInvestigationsResponse":
        """<p>Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident. <code>ListInvestigations</code> lists all active Detective investigations.</p>

        Args:
            graph_arn: <p>The Amazon Resource Name (ARN) of the behavior graph.</p>
            next_token: <p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return a Validation Exception error.</p>
            max_results: <p>Lists the maximum number of investigations in a page.</p>
            filter_criteria: <p>Filters the investigation results based on a criteria.</p>
            sort_criteria: <p>Sorts the investigation results based on a criteria.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.list_investigations_request.ListInvestigationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.list_investigations_response.ListInvestigationsResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.list_investigations

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.list_investigations.list_investigations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.list_investigations_request.ListInvestigationsRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if filter_criteria is not None:
            input["filter_criteria"] = filter_criteria
        if sort_criteria is not None:
            input["sort_criteria"] = sort_criteria

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_invitations(
        self,
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
        next_token: Optional[
            "aws_sdk_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "aws_sdk_detective.types.list_invitations_response.ListInvitationsResponse":
        """<p>Retrieves the list of open and accepted behavior graph invitations for the member account. This operation can only be called by an invited member account.</p> <p>Open invitations are invitations that the member account has not responded to.</p> <p>The results do not include behavior graphs for which the member account declined the invitation. The results also do not include behavior graphs that the member account resigned from or was removed from.</p>

        Args:
            next_token: <p>For requests to retrieve the next page of results, the pagination token that was returned with the previous page of results. The initial request does not include a pagination token.</p>
            max_results: <p>The maximum number of behavior graph invitations to return in the response. The total must be less than the overall limit on the number of results to return, which is currently 200.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.list_invitations_request.ListInvitationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.list_invitations_response.ListInvitationsResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.list_invitations

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.list_invitations.list_invitations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.list_invitations_request.ListInvitationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_members(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
        next_token: Optional[
            "aws_sdk_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "aws_sdk_detective.types.list_members_response.ListMembersResponse":
        """<p>Retrieves the list of member accounts for a behavior graph.</p> <p>For invited accounts, the results do not include member accounts that were removed from the behavior graph.</p> <p>For the organization behavior graph, the results do not include organization accounts that the Detective administrator account has not enabled as member accounts.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph for which to retrieve the list of member accounts.</p>
            next_token: <p>For requests to retrieve the next page of member account results, the pagination token that was returned with the previous page of results. The initial request does not include a pagination token.</p>
            max_results: <p>The maximum number of member accounts to include in the response. The total must be less than the overall limit on the number of results to return, which is currently 200.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.list_members_request.ListMembersRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.list_members_response.ListMembersResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.list_members

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.list_members.list_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.list_members_request.ListMembersRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_organization_admin_accounts(
        self,
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
        next_token: Optional[
            "aws_sdk_detective.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_detective.types.member_results_limit.MemberResultsLimit"
        ] = None,
    ) -> "aws_sdk_detective.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse":
        """<p>Returns information about the Detective administrator account for an organization. Can only be called by the organization management account.</p>

        Args:
            next_token: <p>For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.</p>
            max_results: <p>The maximum number of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.list_organization_admin_accounts_response.ListOrganizationAdminAccountsResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.list_organization_admin_accounts

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.list_organization_admin_accounts.list_organization_admin_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.list_organization_admin_accounts_request.ListOrganizationAdminAccountsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> "aws_sdk_detective.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns the tag values that are assigned to a behavior graph.</p>

        Args:
            resource_arn: <p>The ARN of the behavior graph for which to retrieve the tag values.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.list_tags_for_resource

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def reject_invitation(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> None:
        """<p>Rejects an invitation to contribute the account data to a behavior graph. This operation must be called by an invited member account that has the <code>INVITED</code> status.</p> <p> <code>RejectInvitation</code> cannot be called by an organization account in the organization behavior graph. In the organization behavior graph, organization accounts do not receive an invitation.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph to reject the invitation to.</p> <p>The member account's current member status in the behavior graph must be <code>INVITED</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.reject_invitation_request.RejectInvitationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_detective._operations.amazon_detective.reject_invitation

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.reject_invitation.reject_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.reject_invitation_request.RejectInvitationRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_investigation(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        entity_arn: "aws_sdk_detective.types.entity_arn.EntityArn",
        scope_start_time: "aws_sdk_detective.types.timestamp.Timestamp",
        scope_end_time: "aws_sdk_detective.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> "aws_sdk_detective.types.start_investigation_response.StartInvestigationResponse":
        """<p>Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident. <code>StartInvestigation</code> initiates an investigation on an entity in a behavior graph. </p>

        Args:
            graph_arn: <p>The Amazon Resource Name (ARN) of the behavior graph.</p>
            entity_arn: <p>The unique Amazon Resource Name (ARN) of the IAM user and IAM role.</p>
            scope_start_time: <p>The data and time when the investigation began. The value is an UTC ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>
            scope_end_time: <p>The data and time when the investigation ended. The value is an UTC ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.start_investigation_request.StartInvestigationRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.start_investigation_response.StartInvestigationResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.start_investigation

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.start_investigation.start_investigation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.start_investigation_request.StartInvestigationRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        input["entity_arn"] = entity_arn
        input["scope_start_time"] = scope_start_time
        input["scope_end_time"] = scope_end_time

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_monitoring_member(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        account_id: "aws_sdk_detective.types.account_id.AccountId",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> None:
        """<p>Sends a request to enable data ingest for a member account that has a status of <code>ACCEPTED_BUT_DISABLED</code>.</p> <p>For valid member accounts, the status is updated as follows.</p> <ul> <li> <p>If Detective enabled the member account, then the new status is <code>ENABLED</code>.</p> </li> <li> <p>If Detective cannot enable the member account, the status remains <code>ACCEPTED_BUT_DISABLED</code>. </p> </li> </ul>

        Args:
            graph_arn: <p>The ARN of the behavior graph.</p>
            account_id: <p>The account ID of the member account to try to enable.</p> <p>The account must be an invited member account with a status of <code>ACCEPTED_BUT_DISABLED</code>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.start_monitoring_member_request.StartMonitoringMemberRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_detective._operations.amazon_detective.start_monitoring_member

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.start_monitoring_member.start_monitoring_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.start_monitoring_member_request.StartMonitoringMemberRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        tags: "aws_sdk_detective.types.tag_map.TagMap",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> "aws_sdk_detective.types.tag_resource_response.TagResourceResponse":
        """<p>Applies tag values to a behavior graph.</p>

        Args:
            resource_arn: <p>The ARN of the behavior graph to assign the tags to.</p>
            tags: <p>The tags to assign to the behavior graph. You can add up to 50 tags. For each tag, you provide the tag key and the tag value. Each tag key can contain up to 128 characters. Each tag value can contain up to 256 characters.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.tag_resource

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        tag_keys: "aws_sdk_detective.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> "aws_sdk_detective.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a behavior graph.</p>

        Args:
            resource_arn: <p>The ARN of the behavior graph to remove the tags from.</p>
            tag_keys: <p>The tag keys of the tags to remove from the behavior graph. You can remove up to 50 tags at a time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_detective.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_detective._operations.amazon_detective.untag_resource

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_datasource_packages(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        datasource_packages: "aws_sdk_detective.types.datasource_package_list.DatasourcePackageList",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> None:
        """<p>Starts a data source package for the Detective behavior graph.</p>

        Args:
            graph_arn: <p>The ARN of the behavior graph.</p>
            datasource_packages: <p>The data source package to start for the behavior graph.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.update_datasource_packages_request.UpdateDatasourcePackagesRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_detective._operations.amazon_detective.update_datasource_packages

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.update_datasource_packages.update_datasource_packages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.update_datasource_packages_request.UpdateDatasourcePackagesRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        input["datasource_packages"] = datasource_packages

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_investigation_state(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        investigation_id: "aws_sdk_detective.types.investigation_id.InvestigationId",
        state: "aws_sdk_detective.types.state.State",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
    ) -> None:
        """<p>Updates the state of an investigation.</p>

        Args:
            graph_arn: <p>The Amazon Resource Name (ARN) of the behavior graph.</p>
            investigation_id: <p>The investigation ID of the investigation report.</p>
            state: <p>The current state of the investigation. An archived investigation indicates you have completed reviewing the investigation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.update_investigation_state_request.UpdateInvestigationStateRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_detective._operations.amazon_detective.update_investigation_state

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.update_investigation_state.update_investigation_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.update_investigation_state_request.UpdateInvestigationStateRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        input["investigation_id"] = investigation_id
        input["state"] = state

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_organization_configuration(
        self,
        graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn",
        *,
        config_overrides: Optional[DetectiveClientConfig] = None,
        auto_enable: Optional["aws_sdk_detective.types.boolean.Boolean"] = None,
    ) -> None:
        """<p>Updates the configuration for the Organizations integration in the current Region. Can only be called by the Detective administrator account for the organization.</p>

        Args:
            graph_arn: <p>The ARN of the organization behavior graph.</p>
            auto_enable: <p>Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_detective.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_detective._operations.amazon_detective.update_organization_configuration

            output, http_response = (
                aws_sdk_detective._operations.amazon_detective.update_organization_configuration.update_organization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_detective.types.update_organization_configuration_request.UpdateOrganizationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["graph_arn"] = graph_arn
        if auto_enable is not None:
            input["auto_enable"] = auto_enable

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
