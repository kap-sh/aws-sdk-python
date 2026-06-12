"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AWSPartnerCentralSelling``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

from aws_sdk_partnercentral_selling._auth._identity import Credentials
from aws_sdk_partnercentral_selling._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_partnercentral_selling._auth._zapros_handler import AuthMiddleware
from aws_sdk_partnercentral_selling._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.client_token
    import aws_sdk_partnercentral_selling.types.create_engagement_context_request
    import aws_sdk_partnercentral_selling.types.create_engagement_context_response
    import aws_sdk_partnercentral_selling.types.date_time
    import aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier
    import aws_sdk_partnercentral_selling.types.engagement_context_identifier
    import aws_sdk_partnercentral_selling.types.engagement_context_payload
    import aws_sdk_partnercentral_selling.types.engagement_context_type
    import aws_sdk_partnercentral_selling.types.get_selling_system_settings_request
    import aws_sdk_partnercentral_selling.types.get_selling_system_settings_response
    import aws_sdk_partnercentral_selling.types.list_tags_for_resource_request
    import aws_sdk_partnercentral_selling.types.list_tags_for_resource_response
    import aws_sdk_partnercentral_selling.types.put_selling_system_settings_request
    import aws_sdk_partnercentral_selling.types.put_selling_system_settings_response
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_role_identifier
    import aws_sdk_partnercentral_selling.types.tag_key_list
    import aws_sdk_partnercentral_selling.types.tag_list
    import aws_sdk_partnercentral_selling.types.tag_resource_request
    import aws_sdk_partnercentral_selling.types.tag_resource_response
    import aws_sdk_partnercentral_selling.types.taggable_resource_arn
    import aws_sdk_partnercentral_selling.types.untag_resource_request
    import aws_sdk_partnercentral_selling.types.untag_resource_response
    import aws_sdk_partnercentral_selling.types.update_engagement_context_payload
    import aws_sdk_partnercentral_selling.types.update_engagement_context_request
    import aws_sdk_partnercentral_selling.types.update_engagement_context_response


class PartnerCentralSellingClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = PartnerCentralSellingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[PartnerCentralSellingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PartnerCentralSellingClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            region=overrides.get("region", self.config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def create_engagement_context(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken",
        type: "aws_sdk_partnercentral_selling.types.engagement_context_type.EngagementContextType",
        payload: "aws_sdk_partnercentral_selling.types.engagement_context_payload.EngagementContextPayload",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "aws_sdk_partnercentral_selling.types.create_engagement_context_response.CreateEngagementContextResponse":
        """<p>Creates a new context within an existing engagement. This action allows you to add contextual information such as customer projects or documents to an engagement, providing additional details that help facilitate collaboration between engagement members.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the engagement context request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the engagement context is created in. Use <code>AWS</code> to create contexts in the production environment, and <code>Sandbox</code> for testing in secure, isolated environments.</p>
            engagement_identifier: <p>The unique identifier of the <code>Engagement</code> for which the context is being created. This parameter ensures the context is associated with the correct engagement and provides the necessary linkage between the engagement and its contextual information.</p>
            client_token: <p>A unique, case-sensitive identifier provided by the client to ensure that the request is handled exactly once. This token helps prevent duplicate context creations and must not exceed sixty-four alphanumeric characters. Use a UUID or other unique string to ensure idempotency.</p>
            type: <p>Specifies the type of context being created for the engagement. This field determines the structure and content of the context payload. Valid values include <code>CustomerProject</code> for customer project-related contexts. The type field ensures that the context is properly categorized and processed according to its intended purpose.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.create_engagement_context_request.CreateEngagementContextRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.create_engagement_context_response.CreateEngagementContextResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_context

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.create_engagement_context.create_engagement_context(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.create_engagement_context_request.CreateEngagementContextRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["engagement_identifier"] = engagement_identifier
        input["client_token"] = client_token
        input["type"] = type
        input["payload"] = payload

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_selling_system_settings(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "aws_sdk_partnercentral_selling.types.get_selling_system_settings_response.GetSellingSystemSettingsResponse":
        """<p>Retrieves the currently set system settings, which include the IAM Role used for resource snapshot jobs.</p>

        Args:
            catalog: <p>Specifies the catalog in which the settings are defined. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.get_selling_system_settings_request.GetSellingSystemSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.get_selling_system_settings_response.GetSellingSystemSettingsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_selling_system_settings

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.get_selling_system_settings.get_selling_system_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.get_selling_system_settings_request.GetSellingSystemSettingsRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_selling.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "aws_sdk_partnercentral_selling.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to retrieve tags.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_tags_for_resource

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_selling_system_settings(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
        resource_snapshot_job_role_identifier: Optional[
            "aws_sdk_partnercentral_selling.types.resource_snapshot_job_role_identifier.ResourceSnapshotJobRoleIdentifier"
        ] = None,
    ) -> "aws_sdk_partnercentral_selling.types.put_selling_system_settings_response.PutSellingSystemSettingsResponse":
        """<p>Updates the currently set system settings, which include the IAM Role used for resource snapshot jobs.</p>

        Args:
            catalog: <p>Specifies the catalog in which the settings will be updated. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>
            resource_snapshot_job_role_identifier: <p>Specifies the ARN of the IAM Role used for resource snapshot job executions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.put_selling_system_settings_request.PutSellingSystemSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.put_selling_system_settings_response.PutSellingSystemSettingsResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.put_selling_system_settings

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.put_selling_system_settings.put_selling_system_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.put_selling_system_settings_request.PutSellingSystemSettingsRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        if resource_snapshot_job_role_identifier is not None:
            input["resource_snapshot_job_role_identifier"] = (
                resource_snapshot_job_role_identifier
            )

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_selling.types.taggable_resource_arn.TaggableResourceArn",
        tags: "aws_sdk_partnercentral_selling.types.tag_list.TagList",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> (
        "aws_sdk_partnercentral_selling.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Assigns one or more tags (key-value pairs) to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.tag_resource

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_partnercentral_selling.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "aws_sdk_partnercentral_selling.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "aws_sdk_partnercentral_selling.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The keys of the key-value pairs for the tag or tags you want to remove from the specified resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.untag_resource

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_engagement_context(
        self,
        catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier",
        engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier",
        context_identifier: "aws_sdk_partnercentral_selling.types.engagement_context_identifier.EngagementContextIdentifier",
        engagement_last_modified_at: "aws_sdk_partnercentral_selling.types.date_time.DateTime",
        type: "aws_sdk_partnercentral_selling.types.engagement_context_type.EngagementContextType",
        payload: "aws_sdk_partnercentral_selling.types.update_engagement_context_payload.UpdateEngagementContextPayload",
        *,
        config_overrides: Optional[PartnerCentralSellingClientConfig] = None,
    ) -> "aws_sdk_partnercentral_selling.types.update_engagement_context_response.UpdateEngagementContextResponse":
        """<p>Updates the context information for an existing engagement with new or modified data.</p>

        Args:
            catalog: <p>Specifies the catalog associated with the engagement context update request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the engagement context is updated in.</p>
            engagement_identifier: <p>The unique identifier of the <code>Engagement</code> containing the context to be updated. This parameter ensures the context update is applied to the correct engagement.</p>
            context_identifier: <p>The unique identifier of the specific engagement context to be updated. This ensures that the correct context within the engagement is modified.</p>
            engagement_last_modified_at: <p>The timestamp when the engagement was last modified, used for optimistic concurrency control. This helps prevent conflicts when multiple users attempt to update the same engagement simultaneously.</p>
            type: <p>Specifies the type of context being updated within the engagement. This field determines the structure and content of the context payload being modified.</p>
            payload: <p>Contains the updated contextual information for the engagement. The structure of this payload varies based on the context type specified in the Type field.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_partnercentral_selling.types.update_engagement_context_request.UpdateEngagementContextRequest]",
        ) -> OperationResponse[
            "aws_sdk_partnercentral_selling.types.update_engagement_context_response.UpdateEngagementContextResponse"
        ]:
            import aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.update_engagement_context

            output, http_response = (
                aws_sdk_partnercentral_selling._operations.aws_partner_central_selling.update_engagement_context.update_engagement_context(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_partnercentral_selling.types.update_engagement_context_request.UpdateEngagementContextRequest = {}  # type: ignore[typeddict-item]
        input["catalog"] = catalog
        input["engagement_identifier"] = engagement_identifier
        input["context_identifier"] = context_identifier
        input["engagement_last_modified_at"] = engagement_last_modified_at
        input["type"] = type
        input["payload"] = payload

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
