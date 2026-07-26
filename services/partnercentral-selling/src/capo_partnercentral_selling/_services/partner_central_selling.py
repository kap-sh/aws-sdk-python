"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AWSPartnerCentralSelling``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_partnercentral_selling._auth._signers
import capo_partnercentral_selling._auth._sigv4
from capo_partnercentral_selling._auth._identity import Credentials
from capo_partnercentral_selling._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_partnercentral_selling._auth._zapros_handler import AuthMiddleware
from capo_partnercentral_selling._resources.aws_partner_central_selling.engagement import (
    Engagement,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.engagement_by_accepting_invitation_task import (
    EngagementByAcceptingInvitationTask,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.engagement_from_opportunity_task import (
    EngagementFromOpportunityTask,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.engagement_invitation import (
    EngagementInvitation,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.opportunity import (
    Opportunity,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.opportunity_from_engagement_task import (
    OpportunityFromEngagementTask,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.resource_snapshot import (
    ResourceSnapshot,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.resource_snapshot_job import (
    ResourceSnapshotJob,
)
from capo_partnercentral_selling._resources.aws_partner_central_selling.solution import (
    Solution,
)
from capo_partnercentral_selling._services._aws_config import aws_config
from capo_partnercentral_selling._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.create_engagement_context_request
    import capo_partnercentral_selling.types.create_engagement_context_response
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_arn_or_identifier
    import capo_partnercentral_selling.types.engagement_context_identifier
    import capo_partnercentral_selling.types.engagement_context_payload
    import capo_partnercentral_selling.types.engagement_context_type
    import capo_partnercentral_selling.types.get_selling_system_settings_request
    import capo_partnercentral_selling.types.get_selling_system_settings_response
    import capo_partnercentral_selling.types.list_tags_for_resource_request
    import capo_partnercentral_selling.types.list_tags_for_resource_response
    import capo_partnercentral_selling.types.put_selling_system_settings_request
    import capo_partnercentral_selling.types.put_selling_system_settings_response
    import capo_partnercentral_selling.types.resource_snapshot_job_role_identifier
    import capo_partnercentral_selling.types.tag_key_list
    import capo_partnercentral_selling.types.tag_list
    import capo_partnercentral_selling.types.tag_resource_request
    import capo_partnercentral_selling.types.tag_resource_response
    import capo_partnercentral_selling.types.taggable_resource_arn
    import capo_partnercentral_selling.types.untag_resource_request
    import capo_partnercentral_selling.types.untag_resource_response
    import capo_partnercentral_selling.types.update_engagement_context_payload
    import capo_partnercentral_selling.types.update_engagement_context_request
    import capo_partnercentral_selling.types.update_engagement_context_response


class PartnerCentralSellingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class PartnerCentralSellingClient:
    """A client for the ``PartnerCentralSelling`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = PartnerCentralSellingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.engagement = Engagement(self)
        self.engagement_by_accepting_invitation_task = (
            EngagementByAcceptingInvitationTask(self)
        )
        self.engagement_from_opportunity_task = EngagementFromOpportunityTask(self)
        self.engagement_invitation = EngagementInvitation(self)
        self.opportunity = Opportunity(self)
        self.opportunity_from_engagement_task = OpportunityFromEngagementTask(self)
        self.resource_snapshot = ResourceSnapshot(self)
        self.resource_snapshot_job = ResourceSnapshotJob(self)
        self.solution = Solution(self)

    def operation_options(
        self, config_overrides: Optional[PartnerCentralSellingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PartnerCentralSellingClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def create_engagement_context(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        client_token: "capo_partnercentral_selling.types.client_token.ClientToken",
        type: "capo_partnercentral_selling.types.engagement_context_type.EngagementContextType",
        payload: "capo_partnercentral_selling.types.engagement_context_payload.EngagementContextPayload",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.create_engagement_context_response.CreateEngagementContextResponse":
        """<p>Creates a new context within an existing engagement. This action allows you to add contextual information such as customer projects or documents to an engagement, providing additional details that help facilitate collaboration between engagement members.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the engagement context request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the engagement context is created in. Use <code>AWS</code> to create contexts in the production environment, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            engagement_identifier: <p>The unique identifier of the <code>Engagement</code> for which the context is being created. This parameter ensures the context is associated with the correct engagement and provides the necessary linkage between the engagement and its contextual information.</p>
            client_token: <p>A unique, case-sensitive identifier provided by the client to ensure that the request is handled exactly once. This token helps prevent duplicate context creations and must not exceed sixty-four alphanumeric characters. Use a UUID or other unique string to ensure idempotency.</p>
            type: <p>Specifies the type of context being created for the engagement. This field determines the structure and content of the context payload. Valid values include <code>CustomerProject</code> for customer project-related contexts. The type field ensures that the context is properly categorized and processed according to its intended purpose.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href=\"https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html\">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href=\"https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html\">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.create_engagement_context_request.CreateEngagementContextRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.create_engagement_context_response.CreateEngagementContextResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_context

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_context.create_engagement_context(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.create_engagement_context_request.CreateEngagementContextRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["engagement_identifier"] = engagement_identifier
        input_["client_token"] = client_token
        input_["type"] = type
        input_["payload"] = payload

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_selling_system_settings(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.get_selling_system_settings_response.GetSellingSystemSettingsResponse":
        """<p>Retrieves the currently set system settings, which include the IAM Role used for resource snapshot jobs.</p>

        Args:
            catalog: <p>Specifies the catalog in which the settings are defined. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href=\"https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html\">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.get_selling_system_settings_request.GetSellingSystemSettingsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.get_selling_system_settings_response.GetSellingSystemSettingsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.get_selling_system_settings

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.get_selling_system_settings.get_selling_system_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.get_selling_system_settings_request.GetSellingSystemSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_partnercentral_selling.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to retrieve tags.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href=\"https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html\">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.list_tags_for_resource

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_selling_system_settings(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        resource_snapshot_job_role_identifier: Optional[
            "capo_partnercentral_selling.types.resource_snapshot_job_role_identifier.ResourceSnapshotJobRoleIdentifier"
        ] = None,
    ) -> "capo_partnercentral_selling.types.put_selling_system_settings_response.PutSellingSystemSettingsResponse":
        """<p>Updates the currently set system settings, which include the IAM Role used for resource snapshot jobs.</p>

        Args:
            catalog: <p>Specifies the catalog in which the settings will be updated. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
            resource_snapshot_job_role_identifier: <p>Specifies the ARN of the IAM Role used for resource snapshot job executions.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href=\"https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html\">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.put_selling_system_settings_request.PutSellingSystemSettingsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.put_selling_system_settings_response.PutSellingSystemSettingsResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.put_selling_system_settings

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.put_selling_system_settings.put_selling_system_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.put_selling_system_settings_request.PutSellingSystemSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        if resource_snapshot_job_role_identifier is not None:
            input_["resource_snapshot_job_role_identifier"] = (
                resource_snapshot_job_role_identifier
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_partnercentral_selling.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_partnercentral_selling.types.tag_list.TagList",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href=\"https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html\">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.tag_resource

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_partnercentral_selling.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_partnercentral_selling.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The keys of the key-value pairs for the tag or tags you want to remove from the specified resource.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href=\"https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html\">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.untag_resource

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_engagement_context(
        self,
        catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "capo_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        context_identifier: "capo_partnercentral_selling.types.engagement_context_identifier.EngagementContextIdentifier",
        engagement_last_modified_at: "capo_partnercentral_selling.types.date_time.DateTime",
        type: "capo_partnercentral_selling.types.engagement_context_type.EngagementContextType",
        payload: "capo_partnercentral_selling.types.update_engagement_context_payload.UpdateEngagementContextPayload",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "capo_partnercentral_selling.types.update_engagement_context_response.UpdateEngagementContextResponse":
        """<p>Updates the context information for an existing engagement with new or modified data.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the engagement context update request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the engagement context is updated in.</p>
            engagement_identifier: <p>The unique identifier of the <code>Engagement</code> containing the context to be updated. This parameter ensures the context update is applied to the correct engagement.</p>
            context_identifier: <p>The unique identifier of the specific engagement context to be updated. This ensures that the correct context within the engagement is modified.</p>
            engagement_last_modified_at: <p>The timestamp when the engagement was last modified, used for optimistic concurrency control. This helps prevent conflicts when multiple users attempt to update the same engagement simultaneously.</p>
            type: <p>Specifies the type of context being updated within the engagement. This field determines the structure and content of the context payload being modified.</p>
            payload: <p>Contains the updated contextual information for the engagement. The structure of this payload varies based on the context type specified in the Type field.</p>

        Raises:
            capo_partnercentral_selling.errors.access_denied_exception.AccessDeniedException: <p>This error occurs when you don't have permission to perform the requested action.</p> <p>You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.</p>
            capo_partnercentral_selling.errors.conflict_exception.ConflictException: <p>This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.</p> <p>Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.</p>
            capo_partnercentral_selling.errors.internal_server_exception.InternalServerException: <p>This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.</p> <p>Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.</p>
            capo_partnercentral_selling.errors.resource_not_found_exception.ResourceNotFoundException: <p>This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.</p> <p>Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.</p>
            capo_partnercentral_selling.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.</p> <p>Suggested action: Review the <a href=\"https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html\">Quotas</a> for the resource, and either reduce usage or request a quota increase.</p>
            capo_partnercentral_selling.errors.throttling_exception.ThrottlingException: <p>This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.</p> <p>This error occurs when there are too many requests sent. Review the provided <a href=\"https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html\">Quotas</a> and retry after the provided delay.</p>
            capo_partnercentral_selling.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service or business validation rules.</p> <p>Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.</p>
            capo_partnercentral_selling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_selling.types.update_engagement_context_request.UpdateEngagementContextRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_selling.types.update_engagement_context_response.UpdateEngagementContextResponse"
        ]:
            import capo_partnercentral_selling._operations.aws_partner_central_selling.update_engagement_context

            output, http_response = (
                capo_partnercentral_selling._operations.aws_partner_central_selling.update_engagement_context.update_engagement_context(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_selling.types.update_engagement_context_request.UpdateEngagementContextRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["engagement_identifier"] = engagement_identifier
        input_["context_identifier"] = context_identifier
        input_["engagement_last_modified_at"] = engagement_last_modified_at
        input_["type"] = type
        input_["payload"] = payload

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
