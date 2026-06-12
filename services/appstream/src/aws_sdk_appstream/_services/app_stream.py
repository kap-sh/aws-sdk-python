"""Generated from Smithy shape ``com.amazonaws.appstream#PhotonAdminProxyService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

from aws_sdk_appstream._auth._identity import Credentials
from aws_sdk_appstream._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_appstream._auth._zapros_handler import AuthMiddleware
from aws_sdk_appstream._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_appstream.types.access_endpoint_list
    import aws_sdk_appstream.types.agent_access_config
    import aws_sdk_appstream.types.agent_access_config_for_update
    import aws_sdk_appstream.types.agent_software_version
    import aws_sdk_appstream.types.ami_name
    import aws_sdk_appstream.types.app_block_builder_attributes
    import aws_sdk_appstream.types.app_block_builder_platform_type
    import aws_sdk_appstream.types.app_catalog_config
    import aws_sdk_appstream.types.app_visibility
    import aws_sdk_appstream.types.application_attributes
    import aws_sdk_appstream.types.application_settings
    import aws_sdk_appstream.types.appstream_agent_version
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.arn_list
    import aws_sdk_appstream.types.associate_app_block_builder_app_block_request
    import aws_sdk_appstream.types.associate_app_block_builder_app_block_result
    import aws_sdk_appstream.types.associate_application_fleet_request
    import aws_sdk_appstream.types.associate_application_fleet_result
    import aws_sdk_appstream.types.associate_application_to_entitlement_request
    import aws_sdk_appstream.types.associate_application_to_entitlement_result
    import aws_sdk_appstream.types.associate_fleet_request
    import aws_sdk_appstream.types.associate_fleet_result
    import aws_sdk_appstream.types.associate_software_to_image_builder_request
    import aws_sdk_appstream.types.associate_software_to_image_builder_result
    import aws_sdk_appstream.types.authentication_type
    import aws_sdk_appstream.types.aws_account_id
    import aws_sdk_appstream.types.aws_account_id_list
    import aws_sdk_appstream.types.batch_associate_user_stack_request
    import aws_sdk_appstream.types.batch_associate_user_stack_result
    import aws_sdk_appstream.types.batch_disassociate_user_stack_request
    import aws_sdk_appstream.types.batch_disassociate_user_stack_result
    import aws_sdk_appstream.types.boolean
    import aws_sdk_appstream.types.boolean_object
    import aws_sdk_appstream.types.certificate_based_auth_properties
    import aws_sdk_appstream.types.compute_capacity
    import aws_sdk_appstream.types.content_redirection
    import aws_sdk_appstream.types.copy_image_request
    import aws_sdk_appstream.types.copy_image_response
    import aws_sdk_appstream.types.create_app_block_builder_request
    import aws_sdk_appstream.types.create_app_block_builder_result
    import aws_sdk_appstream.types.create_app_block_builder_streaming_url_request
    import aws_sdk_appstream.types.create_app_block_builder_streaming_url_result
    import aws_sdk_appstream.types.create_app_block_request
    import aws_sdk_appstream.types.create_app_block_result
    import aws_sdk_appstream.types.create_application_request
    import aws_sdk_appstream.types.create_application_result
    import aws_sdk_appstream.types.create_directory_config_request
    import aws_sdk_appstream.types.create_directory_config_result
    import aws_sdk_appstream.types.create_entitlement_request
    import aws_sdk_appstream.types.create_entitlement_result
    import aws_sdk_appstream.types.create_export_image_task_request
    import aws_sdk_appstream.types.create_export_image_task_result
    import aws_sdk_appstream.types.create_fleet_request
    import aws_sdk_appstream.types.create_fleet_result
    import aws_sdk_appstream.types.create_image_builder_request
    import aws_sdk_appstream.types.create_image_builder_result
    import aws_sdk_appstream.types.create_image_builder_streaming_url_request
    import aws_sdk_appstream.types.create_image_builder_streaming_url_result
    import aws_sdk_appstream.types.create_imported_image_request
    import aws_sdk_appstream.types.create_imported_image_result
    import aws_sdk_appstream.types.create_stack_request
    import aws_sdk_appstream.types.create_stack_result
    import aws_sdk_appstream.types.create_streaming_url_request
    import aws_sdk_appstream.types.create_streaming_url_result
    import aws_sdk_appstream.types.create_theme_for_stack_request
    import aws_sdk_appstream.types.create_theme_for_stack_result
    import aws_sdk_appstream.types.create_updated_image_request
    import aws_sdk_appstream.types.create_updated_image_result
    import aws_sdk_appstream.types.create_usage_report_subscription_request
    import aws_sdk_appstream.types.create_usage_report_subscription_result
    import aws_sdk_appstream.types.create_user_request
    import aws_sdk_appstream.types.create_user_result
    import aws_sdk_appstream.types.delete_app_block_builder_request
    import aws_sdk_appstream.types.delete_app_block_builder_result
    import aws_sdk_appstream.types.delete_app_block_request
    import aws_sdk_appstream.types.delete_app_block_result
    import aws_sdk_appstream.types.delete_application_request
    import aws_sdk_appstream.types.delete_application_result
    import aws_sdk_appstream.types.delete_directory_config_request
    import aws_sdk_appstream.types.delete_directory_config_result
    import aws_sdk_appstream.types.delete_entitlement_request
    import aws_sdk_appstream.types.delete_entitlement_result
    import aws_sdk_appstream.types.delete_fleet_request
    import aws_sdk_appstream.types.delete_fleet_result
    import aws_sdk_appstream.types.delete_image_builder_request
    import aws_sdk_appstream.types.delete_image_builder_result
    import aws_sdk_appstream.types.delete_image_permissions_request
    import aws_sdk_appstream.types.delete_image_permissions_result
    import aws_sdk_appstream.types.delete_image_request
    import aws_sdk_appstream.types.delete_image_result
    import aws_sdk_appstream.types.delete_stack_request
    import aws_sdk_appstream.types.delete_stack_result
    import aws_sdk_appstream.types.delete_theme_for_stack_request
    import aws_sdk_appstream.types.delete_theme_for_stack_result
    import aws_sdk_appstream.types.delete_usage_report_subscription_request
    import aws_sdk_appstream.types.delete_usage_report_subscription_result
    import aws_sdk_appstream.types.delete_user_request
    import aws_sdk_appstream.types.delete_user_result
    import aws_sdk_appstream.types.describe_app_block_builder_app_block_associations_request
    import aws_sdk_appstream.types.describe_app_block_builder_app_block_associations_result
    import aws_sdk_appstream.types.describe_app_block_builders_request
    import aws_sdk_appstream.types.describe_app_block_builders_result
    import aws_sdk_appstream.types.describe_app_blocks_request
    import aws_sdk_appstream.types.describe_app_blocks_result
    import aws_sdk_appstream.types.describe_app_license_usage_request
    import aws_sdk_appstream.types.describe_app_license_usage_result
    import aws_sdk_appstream.types.describe_application_fleet_associations_request
    import aws_sdk_appstream.types.describe_application_fleet_associations_result
    import aws_sdk_appstream.types.describe_applications_request
    import aws_sdk_appstream.types.describe_applications_result
    import aws_sdk_appstream.types.describe_directory_configs_request
    import aws_sdk_appstream.types.describe_directory_configs_result
    import aws_sdk_appstream.types.describe_entitlements_request
    import aws_sdk_appstream.types.describe_entitlements_result
    import aws_sdk_appstream.types.describe_fleets_request
    import aws_sdk_appstream.types.describe_fleets_result
    import aws_sdk_appstream.types.describe_image_builders_request
    import aws_sdk_appstream.types.describe_image_builders_result
    import aws_sdk_appstream.types.describe_image_permissions_request
    import aws_sdk_appstream.types.describe_image_permissions_result
    import aws_sdk_appstream.types.describe_images_max_results
    import aws_sdk_appstream.types.describe_images_request
    import aws_sdk_appstream.types.describe_images_result
    import aws_sdk_appstream.types.describe_sessions_request
    import aws_sdk_appstream.types.describe_sessions_result
    import aws_sdk_appstream.types.describe_software_associations_request
    import aws_sdk_appstream.types.describe_software_associations_result
    import aws_sdk_appstream.types.describe_stacks_request
    import aws_sdk_appstream.types.describe_stacks_result
    import aws_sdk_appstream.types.describe_theme_for_stack_request
    import aws_sdk_appstream.types.describe_theme_for_stack_result
    import aws_sdk_appstream.types.describe_usage_report_subscriptions_request
    import aws_sdk_appstream.types.describe_usage_report_subscriptions_result
    import aws_sdk_appstream.types.describe_user_stack_associations_request
    import aws_sdk_appstream.types.describe_user_stack_associations_result
    import aws_sdk_appstream.types.describe_users_request
    import aws_sdk_appstream.types.describe_users_result
    import aws_sdk_appstream.types.description
    import aws_sdk_appstream.types.directory_name
    import aws_sdk_appstream.types.directory_name_list
    import aws_sdk_appstream.types.disable_user_request
    import aws_sdk_appstream.types.disable_user_result
    import aws_sdk_appstream.types.disassociate_app_block_builder_app_block_request
    import aws_sdk_appstream.types.disassociate_app_block_builder_app_block_result
    import aws_sdk_appstream.types.disassociate_application_fleet_request
    import aws_sdk_appstream.types.disassociate_application_fleet_result
    import aws_sdk_appstream.types.disassociate_application_from_entitlement_request
    import aws_sdk_appstream.types.disassociate_application_from_entitlement_result
    import aws_sdk_appstream.types.disassociate_fleet_request
    import aws_sdk_appstream.types.disassociate_fleet_result
    import aws_sdk_appstream.types.disassociate_software_from_image_builder_request
    import aws_sdk_appstream.types.disassociate_software_from_image_builder_result
    import aws_sdk_appstream.types.display_name
    import aws_sdk_appstream.types.domain_join_info
    import aws_sdk_appstream.types.drain_session_instance_request
    import aws_sdk_appstream.types.drain_session_instance_result
    import aws_sdk_appstream.types.embed_host_domains
    import aws_sdk_appstream.types.enable_user_request
    import aws_sdk_appstream.types.enable_user_result
    import aws_sdk_appstream.types.entitlement_attribute_list
    import aws_sdk_appstream.types.expire_session_request
    import aws_sdk_appstream.types.expire_session_result
    import aws_sdk_appstream.types.feedback_url
    import aws_sdk_appstream.types.filters
    import aws_sdk_appstream.types.fleet_attributes
    import aws_sdk_appstream.types.fleet_type
    import aws_sdk_appstream.types.get_export_image_task_request
    import aws_sdk_appstream.types.get_export_image_task_result
    import aws_sdk_appstream.types.image_import_description
    import aws_sdk_appstream.types.image_import_display_name
    import aws_sdk_appstream.types.image_permissions
    import aws_sdk_appstream.types.integer
    import aws_sdk_appstream.types.list_associated_fleets_request
    import aws_sdk_appstream.types.list_associated_fleets_result
    import aws_sdk_appstream.types.list_associated_stacks_request
    import aws_sdk_appstream.types.list_associated_stacks_result
    import aws_sdk_appstream.types.list_entitled_applications_request
    import aws_sdk_appstream.types.list_entitled_applications_result
    import aws_sdk_appstream.types.list_export_image_tasks_request
    import aws_sdk_appstream.types.list_export_image_tasks_result
    import aws_sdk_appstream.types.list_tags_for_resource_request
    import aws_sdk_appstream.types.list_tags_for_resource_response
    import aws_sdk_appstream.types.long
    import aws_sdk_appstream.types.max_results
    import aws_sdk_appstream.types.message_action
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.organizational_unit_distinguished_names_list
    import aws_sdk_appstream.types.packaging_type
    import aws_sdk_appstream.types.photon_ami_id
    import aws_sdk_appstream.types.platform_type
    import aws_sdk_appstream.types.platforms
    import aws_sdk_appstream.types.redirect_url
    import aws_sdk_appstream.types.region_name
    import aws_sdk_appstream.types.runtime_validation_config
    import aws_sdk_appstream.types.s3_location
    import aws_sdk_appstream.types.script_details
    import aws_sdk_appstream.types.service_account_credentials
    import aws_sdk_appstream.types.stack_attributes
    import aws_sdk_appstream.types.start_app_block_builder_request
    import aws_sdk_appstream.types.start_app_block_builder_result
    import aws_sdk_appstream.types.start_fleet_request
    import aws_sdk_appstream.types.start_fleet_result
    import aws_sdk_appstream.types.start_image_builder_request
    import aws_sdk_appstream.types.start_image_builder_result
    import aws_sdk_appstream.types.start_software_deployment_to_image_builder_request
    import aws_sdk_appstream.types.start_software_deployment_to_image_builder_result
    import aws_sdk_appstream.types.stop_app_block_builder_request
    import aws_sdk_appstream.types.stop_app_block_builder_result
    import aws_sdk_appstream.types.stop_fleet_request
    import aws_sdk_appstream.types.stop_fleet_result
    import aws_sdk_appstream.types.stop_image_builder_request
    import aws_sdk_appstream.types.stop_image_builder_result
    import aws_sdk_appstream.types.storage_connector_list
    import aws_sdk_appstream.types.stream_view
    import aws_sdk_appstream.types.streaming_experience_settings
    import aws_sdk_appstream.types.streaming_url_user_id
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.string_list
    import aws_sdk_appstream.types.tag_key_list
    import aws_sdk_appstream.types.tag_resource_request
    import aws_sdk_appstream.types.tag_resource_response
    import aws_sdk_appstream.types.tags
    import aws_sdk_appstream.types.theme_attributes
    import aws_sdk_appstream.types.theme_footer_links
    import aws_sdk_appstream.types.theme_state
    import aws_sdk_appstream.types.theme_styling
    import aws_sdk_appstream.types.theme_title_text
    import aws_sdk_appstream.types.untag_resource_request
    import aws_sdk_appstream.types.untag_resource_response
    import aws_sdk_appstream.types.update_app_block_builder_request
    import aws_sdk_appstream.types.update_app_block_builder_result
    import aws_sdk_appstream.types.update_application_request
    import aws_sdk_appstream.types.update_application_result
    import aws_sdk_appstream.types.update_directory_config_request
    import aws_sdk_appstream.types.update_directory_config_result
    import aws_sdk_appstream.types.update_entitlement_request
    import aws_sdk_appstream.types.update_entitlement_result
    import aws_sdk_appstream.types.update_fleet_request
    import aws_sdk_appstream.types.update_fleet_result
    import aws_sdk_appstream.types.update_image_permissions_request
    import aws_sdk_appstream.types.update_image_permissions_result
    import aws_sdk_appstream.types.update_stack_request
    import aws_sdk_appstream.types.update_stack_result
    import aws_sdk_appstream.types.update_theme_for_stack_request
    import aws_sdk_appstream.types.update_theme_for_stack_result
    import aws_sdk_appstream.types.usb_device_filter_strings
    import aws_sdk_appstream.types.user_attribute_value
    import aws_sdk_appstream.types.user_id
    import aws_sdk_appstream.types.user_setting_list
    import aws_sdk_appstream.types.user_stack_association_list
    import aws_sdk_appstream.types.username
    import aws_sdk_appstream.types.uuid
    import aws_sdk_appstream.types.visibility_type
    import aws_sdk_appstream.types.volume_config
    import aws_sdk_appstream.types.vpc_config
    import aws_sdk_appstream.types.workspace_image_id


class AppStreamClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class AppStreamClient:
    """A client for the ``AppStream`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self.config = AppStreamClientConfig(
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
        self, config_overrides: Optional[AppStreamClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AppStreamClientConfig = config_overrides or {}
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

    def associate_app_block_builder_app_block(
        self,
        app_block_arn: "aws_sdk_appstream.types.arn.Arn",
        app_block_builder_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.associate_app_block_builder_app_block_result.AssociateAppBlockBuilderAppBlockResult":
        """<p>Associates the specified app block builder with the specified app block.</p>

        Args:
            app_block_arn: <p>The ARN of the app block.</p>
            app_block_builder_name: <p>The name of the app block builder.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.associate_app_block_builder_app_block_request.AssociateAppBlockBuilderAppBlockRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.associate_app_block_builder_app_block_result.AssociateAppBlockBuilderAppBlockResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.associate_app_block_builder_app_block

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.associate_app_block_builder_app_block.associate_app_block_builder_app_block(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.associate_app_block_builder_app_block_request.AssociateAppBlockBuilderAppBlockRequest = {}  # type: ignore[typeddict-item]
        input["app_block_arn"] = app_block_arn
        input["app_block_builder_name"] = app_block_builder_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_application_fleet(
        self,
        fleet_name: "aws_sdk_appstream.types.name.Name",
        application_arn: "aws_sdk_appstream.types.arn.Arn",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.associate_application_fleet_result.AssociateApplicationFleetResult":
        """<p>Associates the specified application with the specified fleet. This is only supported for Elastic fleets.</p>

        Args:
            fleet_name: <p>The name of the fleet.</p>
            application_arn: <p>The ARN of the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.associate_application_fleet_request.AssociateApplicationFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.associate_application_fleet_result.AssociateApplicationFleetResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.associate_application_fleet

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.associate_application_fleet.associate_application_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.associate_application_fleet_request.AssociateApplicationFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_name"] = fleet_name
        input["application_arn"] = application_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_application_to_entitlement(
        self,
        stack_name: "aws_sdk_appstream.types.name.Name",
        entitlement_name: "aws_sdk_appstream.types.name.Name",
        application_identifier: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.associate_application_to_entitlement_result.AssociateApplicationToEntitlementResult":
        """<p>Associates an application to entitle.</p>

        Args:
            stack_name: <p>The name of the stack.</p>
            entitlement_name: <p>The name of the entitlement.</p>
            application_identifier: <p>The identifier of the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.associate_application_to_entitlement_request.AssociateApplicationToEntitlementRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.associate_application_to_entitlement_result.AssociateApplicationToEntitlementResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.associate_application_to_entitlement

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.associate_application_to_entitlement.associate_application_to_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.associate_application_to_entitlement_request.AssociateApplicationToEntitlementRequest = {}  # type: ignore[typeddict-item]
        input["stack_name"] = stack_name
        input["entitlement_name"] = entitlement_name
        input["application_identifier"] = application_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_fleet(
        self,
        fleet_name: "aws_sdk_appstream.types.string.String",
        stack_name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.associate_fleet_result.AssociateFleetResult":
        """<p>Associates the specified fleet with the specified stack.</p>

        Args:
            fleet_name: <p>The name of the fleet. </p>
            stack_name: <p>The name of the stack.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.associate_fleet_request.AssociateFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.associate_fleet_result.AssociateFleetResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.associate_fleet

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.associate_fleet.associate_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.associate_fleet_request.AssociateFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_name"] = fleet_name
        input["stack_name"] = stack_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_software_to_image_builder(
        self,
        image_builder_name: "aws_sdk_appstream.types.name.Name",
        software_names: "aws_sdk_appstream.types.string_list.StringList",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.associate_software_to_image_builder_result.AssociateSoftwareToImageBuilderResult":
        """<p>Associates license included application(s) with an existing image builder instance.</p>

        Args:
            image_builder_name: <p>The name of the target image builder instance.</p>
            software_names: <p>The list of license included applications to associate with the image builder.</p> <p>Possible values include the following:</p> <ul> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_64Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_64Bit</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.associate_software_to_image_builder_request.AssociateSoftwareToImageBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.associate_software_to_image_builder_result.AssociateSoftwareToImageBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.associate_software_to_image_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.associate_software_to_image_builder.associate_software_to_image_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.associate_software_to_image_builder_request.AssociateSoftwareToImageBuilderRequest = {}  # type: ignore[typeddict-item]
        input["image_builder_name"] = image_builder_name
        input["software_names"] = software_names

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_associate_user_stack(
        self,
        user_stack_associations: "aws_sdk_appstream.types.user_stack_association_list.UserStackAssociationList",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.batch_associate_user_stack_result.BatchAssociateUserStackResult":
        """<p>Associates the specified users with the specified stacks. Users in a user pool cannot be assigned to stacks with fleets that are joined to an Active Directory domain.</p>

        Args:
            user_stack_associations: <p>The list of UserStackAssociation objects.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.batch_associate_user_stack_request.BatchAssociateUserStackRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.batch_associate_user_stack_result.BatchAssociateUserStackResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.batch_associate_user_stack

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.batch_associate_user_stack.batch_associate_user_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.batch_associate_user_stack_request.BatchAssociateUserStackRequest = {}  # type: ignore[typeddict-item]
        input["user_stack_associations"] = user_stack_associations

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_disassociate_user_stack(
        self,
        user_stack_associations: "aws_sdk_appstream.types.user_stack_association_list.UserStackAssociationList",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.batch_disassociate_user_stack_result.BatchDisassociateUserStackResult":
        """<p>Disassociates the specified users from the specified stacks.</p>

        Args:
            user_stack_associations: <p>The list of UserStackAssociation objects.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.batch_disassociate_user_stack_request.BatchDisassociateUserStackRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.batch_disassociate_user_stack_result.BatchDisassociateUserStackResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.batch_disassociate_user_stack

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.batch_disassociate_user_stack.batch_disassociate_user_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.batch_disassociate_user_stack_request.BatchDisassociateUserStackRequest = {}  # type: ignore[typeddict-item]
        input["user_stack_associations"] = user_stack_associations

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def copy_image(
        self,
        source_image_name: "aws_sdk_appstream.types.name.Name",
        destination_image_name: "aws_sdk_appstream.types.name.Name",
        destination_region: "aws_sdk_appstream.types.region_name.RegionName",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        destination_image_description: Optional[
            "aws_sdk_appstream.types.description.Description"
        ] = None,
    ) -> "aws_sdk_appstream.types.copy_image_response.CopyImageResponse":
        """<p>Copies the image within the same region or to a new region within the same AWS account. Note that any tags you added to the image will not be copied.</p>

        Args:
            source_image_name: <p>The name of the image to copy.</p>
            destination_image_name: <p>The name that the image will have when it is copied to the destination.</p>
            destination_region: <p>The destination region to which the image will be copied. This parameter is required, even if you are copying an image within the same region.</p>
            destination_image_description: <p>The description that the image will have when it is copied to the destination.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.copy_image_request.CopyImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.copy_image_response.CopyImageResponse"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.copy_image

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.copy_image.copy_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.copy_image_request.CopyImageRequest = {}  # type: ignore[typeddict-item]
        input["source_image_name"] = source_image_name
        input["destination_image_name"] = destination_image_name
        input["destination_region"] = destination_region
        if destination_image_description is not None:
            input["destination_image_description"] = destination_image_description

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_app_block(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        source_s3_location: "aws_sdk_appstream.types.s3_location.S3Location",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
        display_name: Optional[
            "aws_sdk_appstream.types.display_name.DisplayName"
        ] = None,
        setup_script_details: Optional[
            "aws_sdk_appstream.types.script_details.ScriptDetails"
        ] = None,
        tags: Optional["aws_sdk_appstream.types.tags.Tags"] = None,
        post_setup_script_details: Optional[
            "aws_sdk_appstream.types.script_details.ScriptDetails"
        ] = None,
        packaging_type: Optional[
            "aws_sdk_appstream.types.packaging_type.PackagingType"
        ] = None,
    ) -> "aws_sdk_appstream.types.create_app_block_result.CreateAppBlockResult":
        """<p>Creates an app block.</p> <p>App blocks are a WorkSpaces Applications resource that stores the details about the virtual hard disk in an S3 bucket. It also stores the setup script with details about how to mount the virtual hard disk. The virtual hard disk includes the application binaries and other files necessary to launch your applications. Multiple applications can be assigned to a single app block.</p> <p>This is only supported for Elastic fleets.</p>

        Args:
            name: <p>The name of the app block.</p>
            description: <p>The description of the app block.</p>
            display_name: <p>The display name of the app block. This is not displayed to the user.</p>
            source_s3_location: <p>The source S3 location of the app block.</p>
            setup_script_details: <p>The setup script details of the app block. This must be provided for the <code>CUSTOM</code> PackagingType.</p>
            tags: <p>The tags assigned to the app block.</p>
            post_setup_script_details: <p>The post setup script details of the app block. This can only be provided for the <code>APPSTREAM2</code> PackagingType.</p>
            packaging_type: <p>The packaging type of the app block.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_app_block_request.CreateAppBlockRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_app_block_result.CreateAppBlockResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_app_block

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_app_block.create_app_block(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_app_block_request.CreateAppBlockRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if display_name is not None:
            input["display_name"] = display_name
        input["source_s3_location"] = source_s3_location
        if setup_script_details is not None:
            input["setup_script_details"] = setup_script_details
        if tags is not None:
            input["tags"] = tags
        if post_setup_script_details is not None:
            input["post_setup_script_details"] = post_setup_script_details
        if packaging_type is not None:
            input["packaging_type"] = packaging_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_app_block_builder(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        platform: "aws_sdk_appstream.types.app_block_builder_platform_type.AppBlockBuilderPlatformType",
        instance_type: "aws_sdk_appstream.types.string.String",
        vpc_config: "aws_sdk_appstream.types.vpc_config.VpcConfig",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
        display_name: Optional[
            "aws_sdk_appstream.types.display_name.DisplayName"
        ] = None,
        tags: Optional["aws_sdk_appstream.types.tags.Tags"] = None,
        enable_default_internet_access: Optional[
            "aws_sdk_appstream.types.boolean_object.BooleanObject"
        ] = None,
        iam_role_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        access_endpoints: Optional[
            "aws_sdk_appstream.types.access_endpoint_list.AccessEndpointList"
        ] = None,
        disable_imdsv1: Optional[
            "aws_sdk_appstream.types.boolean_object.BooleanObject"
        ] = None,
    ) -> "aws_sdk_appstream.types.create_app_block_builder_result.CreateAppBlockBuilderResult":
        """<p>Creates an app block builder.</p>

        Args:
            name: <p>The unique name for the app block builder.</p>
            description: <p>The description of the app block builder.</p>
            display_name: <p>The display name of the app block builder.</p>
            tags: <p>The tags to associate with the app block builder. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=. </p> <p>If you do not specify a value, the value is set to an empty string.</p> <p>Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters: </p> <p>_ . : / = + \ - @</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html\">Tagging Your Resources</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>
            platform: <p>The platform of the app block builder.</p> <p> <code>WINDOWS_SERVER_2019</code> is the only valid value.</p>
            instance_type: <p>The instance type to use when launching the app block builder. The following instance types are available:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.standard.xlarge</p> </li> <li> <p>stream.standard.2xlarge</p> </li> </ul>
            vpc_config: <p>The VPC configuration for the app block builder.</p> <p>App block builders require that you specify at least two subnets in different availability zones.</p>
            enable_default_internet_access: <p>Enables or disables default internet access for the app block builder.</p>
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to apply to the app block builder. To assume a role, the app block builder calls the AWS Security Token Service (STS) <code>AssumeRole</code> API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the <b>appstream_machine_role</b> credential profile on the instance.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html\">Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>
            access_endpoints: <p>The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the app block builder only through the specified endpoints.</p>
            disable_imdsv1: <p>Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_app_block_builder_request.CreateAppBlockBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_app_block_builder_result.CreateAppBlockBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_app_block_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_app_block_builder.create_app_block_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_app_block_builder_request.CreateAppBlockBuilderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if display_name is not None:
            input["display_name"] = display_name
        if tags is not None:
            input["tags"] = tags
        input["platform"] = platform
        input["instance_type"] = instance_type
        input["vpc_config"] = vpc_config
        if enable_default_internet_access is not None:
            input["enable_default_internet_access"] = enable_default_internet_access
        if iam_role_arn is not None:
            input["iam_role_arn"] = iam_role_arn
        if access_endpoints is not None:
            input["access_endpoints"] = access_endpoints
        if disable_imdsv1 is not None:
            input["disable_imdsv1"] = disable_imdsv1

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_app_block_builder_streaming_url(
        self,
        app_block_builder_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        validity: Optional["aws_sdk_appstream.types.long.Long"] = None,
    ) -> "aws_sdk_appstream.types.create_app_block_builder_streaming_url_result.CreateAppBlockBuilderStreamingURLResult":
        """<p>Creates a URL to start a create app block builder streaming session.</p>

        Args:
            app_block_builder_name: <p>The name of the app block builder.</p>
            validity: <p>The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 3600 seconds.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_app_block_builder_streaming_url_request.CreateAppBlockBuilderStreamingURLRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_app_block_builder_streaming_url_result.CreateAppBlockBuilderStreamingURLResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_app_block_builder_streaming_url

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_app_block_builder_streaming_url.create_app_block_builder_streaming_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_app_block_builder_streaming_url_request.CreateAppBlockBuilderStreamingURLRequest = {}  # type: ignore[typeddict-item]
        input["app_block_builder_name"] = app_block_builder_name
        if validity is not None:
            input["validity"] = validity

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_application(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        icon_s3_location: "aws_sdk_appstream.types.s3_location.S3Location",
        launch_path: "aws_sdk_appstream.types.string.String",
        platforms: "aws_sdk_appstream.types.platforms.Platforms",
        instance_families: "aws_sdk_appstream.types.string_list.StringList",
        app_block_arn: "aws_sdk_appstream.types.arn.Arn",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        display_name: Optional[
            "aws_sdk_appstream.types.display_name.DisplayName"
        ] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
        working_directory: Optional["aws_sdk_appstream.types.string.String"] = None,
        launch_parameters: Optional["aws_sdk_appstream.types.string.String"] = None,
        tags: Optional["aws_sdk_appstream.types.tags.Tags"] = None,
    ) -> "aws_sdk_appstream.types.create_application_result.CreateApplicationResult":
        """<p>Creates an application.</p> <p>Applications are a WorkSpaces Applications resource that stores the details about how to launch applications on Elastic fleet streaming instances. An application consists of the launch details, icon, and display name. Applications are associated with an app block that contains the application binaries and other files. The applications assigned to an Elastic fleet are the applications users can launch. </p> <p>This is only supported for Elastic fleets.</p>

        Args:
            name: <p>The name of the application. This name is visible to users when display name is not specified.</p>
            display_name: <p>The display name of the application. This name is visible to users in the application catalog.</p>
            description: <p>The description of the application.</p>
            icon_s3_location: <p>The location in S3 of the application icon.</p>
            launch_path: <p>The launch path of the application.</p>
            working_directory: <p>The working directory of the application.</p>
            launch_parameters: <p>The launch parameters of the application.</p>
            platforms: <p>The platforms the application supports. WINDOWS_SERVER_2019, AMAZON_LINUX2 and UBUNTU_PRO_2404 are supported for Elastic fleets.</p>
            instance_families: <p>The instance families the application supports. Valid values are GENERAL_PURPOSE and GRAPHICS_G4.</p>
            app_block_arn: <p>The app block ARN to which the application should be associated</p>
            tags: <p>The tags assigned to the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_application_result.CreateApplicationResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_application

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_application_request.CreateApplicationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if display_name is not None:
            input["display_name"] = display_name
        if description is not None:
            input["description"] = description
        input["icon_s3_location"] = icon_s3_location
        input["launch_path"] = launch_path
        if working_directory is not None:
            input["working_directory"] = working_directory
        if launch_parameters is not None:
            input["launch_parameters"] = launch_parameters
        input["platforms"] = platforms
        input["instance_families"] = instance_families
        input["app_block_arn"] = app_block_arn
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_directory_config(
        self,
        directory_name: "aws_sdk_appstream.types.directory_name.DirectoryName",
        organizational_unit_distinguished_names: "aws_sdk_appstream.types.organizational_unit_distinguished_names_list.OrganizationalUnitDistinguishedNamesList",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        service_account_credentials: Optional[
            "aws_sdk_appstream.types.service_account_credentials.ServiceAccountCredentials"
        ] = None,
        certificate_based_auth_properties: Optional[
            "aws_sdk_appstream.types.certificate_based_auth_properties.CertificateBasedAuthProperties"
        ] = None,
    ) -> "aws_sdk_appstream.types.create_directory_config_result.CreateDirectoryConfigResult":
        """<p>Creates a Directory Config object in WorkSpaces Applications. This object includes the configuration information required to join fleets and image builders to Microsoft Active Directory domains.</p>

        Args:
            directory_name: <p>The fully qualified name of the directory (for example, corp.example.com).</p>
            organizational_unit_distinguished_names: <p>The distinguished names of the organizational units for computer accounts.</p>
            service_account_credentials: <p>The credentials for the service account used by the fleet or image builder to connect to the directory.</p>
            certificate_based_auth_properties: <p>The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory domain-joined streaming instances. Fallback is turned on by default when certificate-based authentication is <b>Enabled</b> . Fallback allows users to log in using their AD domain password if certificate-based authentication is unsuccessful, or to unlock a desktop lock screen. <b>Enabled_no_directory_login_fallback</b> enables certificate-based authentication, but does not allow users to log in using their AD domain password. Users will be disconnected to re-authenticate using certificates.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_directory_config_request.CreateDirectoryConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_directory_config_result.CreateDirectoryConfigResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_directory_config

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_directory_config.create_directory_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_directory_config_request.CreateDirectoryConfigRequest = {}  # type: ignore[typeddict-item]
        input["directory_name"] = directory_name
        input["organizational_unit_distinguished_names"] = (
            organizational_unit_distinguished_names
        )
        if service_account_credentials is not None:
            input["service_account_credentials"] = service_account_credentials
        if certificate_based_auth_properties is not None:
            input["certificate_based_auth_properties"] = (
                certificate_based_auth_properties
            )

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_entitlement(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        stack_name: "aws_sdk_appstream.types.name.Name",
        app_visibility: "aws_sdk_appstream.types.app_visibility.AppVisibility",
        attributes: "aws_sdk_appstream.types.entitlement_attribute_list.EntitlementAttributeList",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
    ) -> "aws_sdk_appstream.types.create_entitlement_result.CreateEntitlementResult":
        """<p>Creates a new entitlement. Entitlements control access to specific applications within a stack, based on user attributes. Entitlements apply to SAML 2.0 federated user identities. WorkSpaces Applications user pool and streaming URL users are entitled to all applications in a stack. Entitlements don't apply to the desktop stream view application, or to applications managed by a dynamic app provider using the Dynamic Application Framework.</p>

        Args:
            name: <p>The name of the entitlement.</p>
            stack_name: <p>The name of the stack with which the entitlement is associated.</p>
            description: <p>The description of the entitlement.</p>
            app_visibility: <p>Specifies whether all or selected apps are entitled.</p>
            attributes: <p>The attributes of the entitlement.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_entitlement_request.CreateEntitlementRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_entitlement_result.CreateEntitlementResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_entitlement

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_entitlement.create_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_entitlement_request.CreateEntitlementRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["stack_name"] = stack_name
        if description is not None:
            input["description"] = description
        input["app_visibility"] = app_visibility
        input["attributes"] = attributes

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_export_image_task(
        self,
        image_name: "aws_sdk_appstream.types.name.Name",
        ami_name: "aws_sdk_appstream.types.ami_name.AmiName",
        iam_role_arn: "aws_sdk_appstream.types.arn.Arn",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        tag_specifications: Optional["aws_sdk_appstream.types.tags.Tags"] = None,
        ami_description: Optional[
            "aws_sdk_appstream.types.description.Description"
        ] = None,
    ) -> "aws_sdk_appstream.types.create_export_image_task_result.CreateExportImageTaskResult":
        """<p>Creates a task to export a WorkSpaces Applications image to an EC2 AMI. This allows you to use your customized WorkSpaces Applications images with other AWS services or for backup purposes.</p>

        Args:
            image_name: <p>The name of the WorkSpaces Applications image to export. The image must be in an available state and owned by your account.</p>
            ami_name: <p>The name for the exported EC2 AMI. This is a required field that must be unique within your account and region.</p>
            iam_role_arn: <p>The ARN of the IAM role that allows WorkSpaces Applications to create the AMI. The role must have permissions to copy images, describe images, and create tags, with a trust relationship allowing appstream.amazonaws.com to assume the role.</p>
            tag_specifications: <p>The tags to apply to the exported AMI. These tags help you organize and manage your EC2 AMIs.</p>
            ami_description: <p>An optional description for the exported AMI. This description will be applied to the resulting EC2 AMI.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_export_image_task_request.CreateExportImageTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_export_image_task_result.CreateExportImageTaskResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_export_image_task

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_export_image_task.create_export_image_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_export_image_task_request.CreateExportImageTaskRequest = {}  # type: ignore[typeddict-item]
        input["image_name"] = image_name
        input["ami_name"] = ami_name
        input["iam_role_arn"] = iam_role_arn
        if tag_specifications is not None:
            input["tag_specifications"] = tag_specifications
        if ami_description is not None:
            input["ami_description"] = ami_description

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_fleet(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        instance_type: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        image_name: Optional["aws_sdk_appstream.types.name.Name"] = None,
        image_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        fleet_type: Optional["aws_sdk_appstream.types.fleet_type.FleetType"] = None,
        compute_capacity: Optional[
            "aws_sdk_appstream.types.compute_capacity.ComputeCapacity"
        ] = None,
        vpc_config: Optional["aws_sdk_appstream.types.vpc_config.VpcConfig"] = None,
        max_user_duration_in_seconds: Optional[
            "aws_sdk_appstream.types.integer.Integer"
        ] = None,
        disconnect_timeout_in_seconds: Optional[
            "aws_sdk_appstream.types.integer.Integer"
        ] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
        display_name: Optional[
            "aws_sdk_appstream.types.display_name.DisplayName"
        ] = None,
        enable_default_internet_access: Optional[
            "aws_sdk_appstream.types.boolean_object.BooleanObject"
        ] = None,
        domain_join_info: Optional[
            "aws_sdk_appstream.types.domain_join_info.DomainJoinInfo"
        ] = None,
        tags: Optional["aws_sdk_appstream.types.tags.Tags"] = None,
        idle_disconnect_timeout_in_seconds: Optional[
            "aws_sdk_appstream.types.integer.Integer"
        ] = None,
        iam_role_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        stream_view: Optional["aws_sdk_appstream.types.stream_view.StreamView"] = None,
        platform: Optional["aws_sdk_appstream.types.platform_type.PlatformType"] = None,
        max_concurrent_sessions: Optional[
            "aws_sdk_appstream.types.integer.Integer"
        ] = None,
        usb_device_filter_strings: Optional[
            "aws_sdk_appstream.types.usb_device_filter_strings.UsbDeviceFilterStrings"
        ] = None,
        session_script_s3_location: Optional[
            "aws_sdk_appstream.types.s3_location.S3Location"
        ] = None,
        max_sessions_per_instance: Optional[
            "aws_sdk_appstream.types.integer.Integer"
        ] = None,
        root_volume_config: Optional[
            "aws_sdk_appstream.types.volume_config.VolumeConfig"
        ] = None,
        disable_imdsv1: Optional[
            "aws_sdk_appstream.types.boolean_object.BooleanObject"
        ] = None,
    ) -> "aws_sdk_appstream.types.create_fleet_result.CreateFleetResult":
        """<p>Creates a fleet. A fleet consists of streaming instances that your users access for their applications and desktops.</p>

        Args:
            name: <p>A unique name for the fleet.</p>
            image_name: <p>The name of the image used to create the fleet.</p>
            image_arn: <p>The ARN of the public, private, or shared image to use.</p>
            instance_type: <p>The instance type to use when launching fleet instances. The following instance types are available:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.standard.xlarge</p> </li> <li> <p>stream.standard.2xlarge</p> </li> <li> <p>stream.compute.large</p> </li> <li> <p>stream.compute.xlarge</p> </li> <li> <p>stream.compute.2xlarge</p> </li> <li> <p>stream.compute.4xlarge</p> </li> <li> <p>stream.compute.8xlarge</p> </li> <li> <p>stream.memory.large</p> </li> <li> <p>stream.memory.xlarge</p> </li> <li> <p>stream.memory.2xlarge</p> </li> <li> <p>stream.memory.4xlarge</p> </li> <li> <p>stream.memory.8xlarge</p> </li> <li> <p>stream.memory.z1d.large</p> </li> <li> <p>stream.memory.z1d.xlarge</p> </li> <li> <p>stream.memory.z1d.2xlarge</p> </li> <li> <p>stream.memory.z1d.3xlarge</p> </li> <li> <p>stream.memory.z1d.6xlarge</p> </li> <li> <p>stream.memory.z1d.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.xlarge</p> </li> <li> <p>stream.graphics.g4dn.2xlarge</p> </li> <li> <p>stream.graphics.g4dn.4xlarge</p> </li> <li> <p>stream.graphics.g4dn.8xlarge</p> </li> <li> <p>stream.graphics.g4dn.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.16xlarge</p> </li> <li> <p>stream.graphics.g5.xlarge</p> </li> <li> <p>stream.graphics.g5.2xlarge</p> </li> <li> <p>stream.graphics.g5.4xlarge</p> </li> <li> <p>stream.graphics.g5.8xlarge</p> </li> <li> <p>stream.graphics.g5.12xlarge</p> </li> <li> <p>stream.graphics.g5.16xlarge</p> </li> <li> <p>stream.graphics.g5.24xlarge</p> </li> <li> <p>stream.graphics.g6.xlarge</p> </li> <li> <p>stream.graphics.g6.2xlarge</p> </li> <li> <p>stream.graphics.g6.4xlarge</p> </li> <li> <p>stream.graphics.g6.8xlarge</p> </li> <li> <p>stream.graphics.g6.16xlarge</p> </li> <li> <p>stream.graphics.g6.12xlarge</p> </li> <li> <p>stream.graphics.g6.24xlarge</p> </li> <li> <p>stream.graphics.gr6.4xlarge</p> </li> <li> <p>stream.graphics.gr6.8xlarge</p> </li> <li> <p>stream.graphics.g6f.large</p> </li> <li> <p>stream.graphics.g6f.xlarge</p> </li> <li> <p>stream.graphics.g6f.2xlarge</p> </li> <li> <p>stream.graphics.g6f.4xlarge</p> </li> <li> <p>stream.graphics.gr6f.4xlarge</p> </li> </ul> <p>The following instance types are available for Elastic fleets:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.standard.xlarge</p> </li> <li> <p>stream.standard.2xlarge</p> </li> </ul>
            fleet_type: <p>The fleet type.</p> <dl> <dt>ALWAYS_ON</dt> <dd> <p>Provides users with instant-on access to their apps. You are charged for all running instances in your fleet, even if no users are streaming apps.</p> </dd> <dt>ON_DEMAND</dt> <dd> <p>Provide users with access to applications after they connect, which takes one to two minutes. You are charged for instance streaming when users are connected and a small hourly fee for instances that are not streaming apps.</p> </dd> </dl>
            compute_capacity: <p>The desired capacity for the fleet. This is not allowed for Elastic fleets. For Elastic fleets, specify MaxConcurrentSessions instead.</p>
            vpc_config: <p>The VPC configuration for the fleet. This is required for Elastic fleets, but not required for other fleet types. Elastic fleets require that you specify at least two subnets in different availability zones.</p>
            max_user_duration_in_seconds: <p>The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.</p> <p>Specify a value between 600 and 432000.</p>
            disconnect_timeout_in_seconds: <p>The amount of time that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance. </p> <p>Specify a value between 60 and 36000.</p>
            description: <p>The description to display.</p>
            display_name: <p>The fleet name to display.</p>
            enable_default_internet_access: <p>Enables or disables default internet access for the fleet.</p>
            domain_join_info: <p>The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain. This is not allowed for Elastic fleets. </p>
            tags: <p>The tags to associate with the fleet. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=. </p> <p>If you do not specify a value, the value is set to an empty string.</p> <p>Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters: </p> <p>_ . : / = + \ - @</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html\">Tagging Your Resources</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>
            idle_disconnect_timeout_in_seconds: <p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the <code>DisconnectTimeoutInSeconds</code> time interval begins. Users are notified before they are disconnected due to inactivity. If they try to reconnect to the streaming session before the time interval specified in <code>DisconnectTimeoutInSeconds</code> elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in <code>IdleDisconnectTimeoutInSeconds</code> elapses, they are disconnected.</p> <p>To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 36000. The default value is 0.</p> <note> <p>If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity. </p> </note>
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to apply to the fleet. To assume a role, a fleet instance calls the AWS Security Token Service (STS) <code>AssumeRole</code> API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the <b>appstream_machine_role</b> credential profile on the instance.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html\">Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>
            stream_view: <p>The WorkSpaces Applications view that is displayed to your users when they stream from the fleet. When <code>APP</code> is specified, only the windows of applications opened by users display. When <code>DESKTOP</code> is specified, the standard desktop that is provided by the operating system displays.</p> <p>The default value is <code>APP</code>.</p>
            platform: <p>The fleet platform. WINDOWS_SERVER_2019, AMAZON_LINUX2 and UBUNTU_PRO_2404 are supported for Elastic fleets. </p>
            max_concurrent_sessions: <p>The maximum concurrent sessions of the Elastic fleet. This is required for Elastic fleets, and not allowed for other fleet types.</p>
            usb_device_filter_strings: <p>The USB device filter strings that specify which USB devices a user can redirect to the fleet streaming session, when using the Windows native client. This is allowed but not required for Elastic fleets.</p>
            session_script_s3_location: <p>The S3 location of the session scripts configuration zip file. This only applies to Elastic fleets.</p>
            max_sessions_per_instance: <p>The maximum number of user sessions on an instance. This only applies to multi-session fleets.</p>
            root_volume_config: <p>The configuration for the root volume of fleet instances. Use this to customize storage capacity from 200 GB up to 500 GB based on your application requirements.</p>
            disable_imdsv1: <p>Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.</p> <note> <p>Before disabling IMDSv1, ensure your WorkSpaces Applications images are running the agent version or managed image update released on or after January 16, 2024 to support IMDSv2 enforcement.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_fleet_request.CreateFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_fleet_result.CreateFleetResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_fleet

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_fleet.create_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_fleet_request.CreateFleetRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if image_name is not None:
            input["image_name"] = image_name
        if image_arn is not None:
            input["image_arn"] = image_arn
        input["instance_type"] = instance_type
        if fleet_type is not None:
            input["fleet_type"] = fleet_type
        if compute_capacity is not None:
            input["compute_capacity"] = compute_capacity
        if vpc_config is not None:
            input["vpc_config"] = vpc_config
        if max_user_duration_in_seconds is not None:
            input["max_user_duration_in_seconds"] = max_user_duration_in_seconds
        if disconnect_timeout_in_seconds is not None:
            input["disconnect_timeout_in_seconds"] = disconnect_timeout_in_seconds
        if description is not None:
            input["description"] = description
        if display_name is not None:
            input["display_name"] = display_name
        if enable_default_internet_access is not None:
            input["enable_default_internet_access"] = enable_default_internet_access
        if domain_join_info is not None:
            input["domain_join_info"] = domain_join_info
        if tags is not None:
            input["tags"] = tags
        if idle_disconnect_timeout_in_seconds is not None:
            input["idle_disconnect_timeout_in_seconds"] = (
                idle_disconnect_timeout_in_seconds
            )
        if iam_role_arn is not None:
            input["iam_role_arn"] = iam_role_arn
        if stream_view is not None:
            input["stream_view"] = stream_view
        if platform is not None:
            input["platform"] = platform
        if max_concurrent_sessions is not None:
            input["max_concurrent_sessions"] = max_concurrent_sessions
        if usb_device_filter_strings is not None:
            input["usb_device_filter_strings"] = usb_device_filter_strings
        if session_script_s3_location is not None:
            input["session_script_s3_location"] = session_script_s3_location
        if max_sessions_per_instance is not None:
            input["max_sessions_per_instance"] = max_sessions_per_instance
        if root_volume_config is not None:
            input["root_volume_config"] = root_volume_config
        if disable_imdsv1 is not None:
            input["disable_imdsv1"] = disable_imdsv1

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_image_builder(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        instance_type: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        image_name: Optional["aws_sdk_appstream.types.string.String"] = None,
        image_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
        display_name: Optional[
            "aws_sdk_appstream.types.display_name.DisplayName"
        ] = None,
        vpc_config: Optional["aws_sdk_appstream.types.vpc_config.VpcConfig"] = None,
        iam_role_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        enable_default_internet_access: Optional[
            "aws_sdk_appstream.types.boolean_object.BooleanObject"
        ] = None,
        domain_join_info: Optional[
            "aws_sdk_appstream.types.domain_join_info.DomainJoinInfo"
        ] = None,
        appstream_agent_version: Optional[
            "aws_sdk_appstream.types.appstream_agent_version.AppstreamAgentVersion"
        ] = None,
        tags: Optional["aws_sdk_appstream.types.tags.Tags"] = None,
        access_endpoints: Optional[
            "aws_sdk_appstream.types.access_endpoint_list.AccessEndpointList"
        ] = None,
        root_volume_config: Optional[
            "aws_sdk_appstream.types.volume_config.VolumeConfig"
        ] = None,
        softwares_to_install: Optional[
            "aws_sdk_appstream.types.string_list.StringList"
        ] = None,
        softwares_to_uninstall: Optional[
            "aws_sdk_appstream.types.string_list.StringList"
        ] = None,
        disable_imdsv1: Optional[
            "aws_sdk_appstream.types.boolean_object.BooleanObject"
        ] = None,
    ) -> "aws_sdk_appstream.types.create_image_builder_result.CreateImageBuilderResult":
        """<p>Creates an image builder. An image builder is a virtual machine that is used to create an image.</p> <p>The initial state of the builder is <code>PENDING</code>. When it is ready, the state is <code>RUNNING</code>.</p>

        Args:
            name: <p>A unique name for the image builder.</p>
            image_name: <p>The name of the image used to create the image builder.</p>
            image_arn: <p>The ARN of the public, private, or shared image to use.</p>
            instance_type: <p>The instance type to use when launching the image builder. The following instance types are available:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.compute.large</p> </li> <li> <p>stream.compute.xlarge</p> </li> <li> <p>stream.compute.2xlarge</p> </li> <li> <p>stream.compute.4xlarge</p> </li> <li> <p>stream.compute.8xlarge</p> </li> <li> <p>stream.memory.large</p> </li> <li> <p>stream.memory.xlarge</p> </li> <li> <p>stream.memory.2xlarge</p> </li> <li> <p>stream.memory.4xlarge</p> </li> <li> <p>stream.memory.8xlarge</p> </li> <li> <p>stream.memory.z1d.large</p> </li> <li> <p>stream.memory.z1d.xlarge</p> </li> <li> <p>stream.memory.z1d.2xlarge</p> </li> <li> <p>stream.memory.z1d.3xlarge</p> </li> <li> <p>stream.memory.z1d.6xlarge</p> </li> <li> <p>stream.memory.z1d.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.xlarge</p> </li> <li> <p>stream.graphics.g4dn.2xlarge</p> </li> <li> <p>stream.graphics.g4dn.4xlarge</p> </li> <li> <p>stream.graphics.g4dn.8xlarge</p> </li> <li> <p>stream.graphics.g4dn.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.16xlarge</p> </li> <li> <p>stream.graphics.g5.xlarge</p> </li> <li> <p>stream.graphics.g5.2xlarge</p> </li> <li> <p>stream.graphics.g5.4xlarge</p> </li> <li> <p>stream.graphics.g5.8xlarge</p> </li> <li> <p>stream.graphics.g5.16xlarge</p> </li> <li> <p>stream.graphics.g5.12xlarge</p> </li> <li> <p>stream.graphics.g5.24xlarge</p> </li> <li> <p>stream.graphics.g6.xlarge</p> </li> <li> <p>stream.graphics.g6.2xlarge</p> </li> <li> <p>stream.graphics.g6.4xlarge</p> </li> <li> <p>stream.graphics.g6.8xlarge</p> </li> <li> <p>stream.graphics.g6.16xlarge</p> </li> <li> <p>stream.graphics.g6.12xlarge</p> </li> <li> <p>stream.graphics.g6.24xlarge</p> </li> <li> <p>stream.graphics.gr6.4xlarge</p> </li> <li> <p>stream.graphics.gr6.8xlarge</p> </li> <li> <p>stream.graphics.g6f.large</p> </li> <li> <p>stream.graphics.g6f.xlarge</p> </li> <li> <p>stream.graphics.g6f.2xlarge</p> </li> <li> <p>stream.graphics.g6f.4xlarge</p> </li> <li> <p>stream.graphics.gr6f.4xlarge</p> </li> </ul>
            description: <p>The description to display.</p>
            display_name: <p>The image builder name to display.</p>
            vpc_config: <p>The VPC configuration for the image builder. You can specify only one subnet.</p>
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to apply to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) <code>AssumeRole</code> API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the <b>appstream_machine_role</b> credential profile on the instance.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html\">Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>
            enable_default_internet_access: <p>Enables or disables default internet access for the image builder.</p>
            domain_join_info: <p>The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain. </p>
            appstream_agent_version: <p>The version of the WorkSpaces Applications agent to use for this image builder. To use the latest version of the WorkSpaces Applications agent, specify [LATEST]. </p>
            tags: <p>The tags to associate with the image builder. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=. </p> <p>Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters: </p> <p>_ . : / = + \ - @</p> <p>If you do not specify a value, the value is set to an empty string.</p> <p>For more information about tags, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html\">Tagging Your Resources</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>
            access_endpoints: <p>The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the image builder only through the specified endpoints.</p>
            root_volume_config: <p>The configuration for the root volume of the image builder. Use this to customize storage capacity from 200 GB up to 500 GB based on your application installation requirements.</p>
            softwares_to_install: <p>The list of license included applications to install on the image builder during creation.</p> <p>Possible values include the following:</p> <ul> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_64Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_64Bit</p> </li> </ul>
            softwares_to_uninstall: <p>The list of license included applications to uninstall from the image builder during creation.</p> <p>Possible values include the following:</p> <ul> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_64Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_64Bit</p> </li> </ul>
            disable_imdsv1: <p>Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.</p> <note> <p>Before disabling IMDSv1, ensure your WorkSpaces Applications images are running the agent version or managed image update released on or after January 16, 2024 to support IMDSv2 enforcement.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_image_builder_request.CreateImageBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_image_builder_result.CreateImageBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_image_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_image_builder.create_image_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_image_builder_request.CreateImageBuilderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if image_name is not None:
            input["image_name"] = image_name
        if image_arn is not None:
            input["image_arn"] = image_arn
        input["instance_type"] = instance_type
        if description is not None:
            input["description"] = description
        if display_name is not None:
            input["display_name"] = display_name
        if vpc_config is not None:
            input["vpc_config"] = vpc_config
        if iam_role_arn is not None:
            input["iam_role_arn"] = iam_role_arn
        if enable_default_internet_access is not None:
            input["enable_default_internet_access"] = enable_default_internet_access
        if domain_join_info is not None:
            input["domain_join_info"] = domain_join_info
        if appstream_agent_version is not None:
            input["appstream_agent_version"] = appstream_agent_version
        if tags is not None:
            input["tags"] = tags
        if access_endpoints is not None:
            input["access_endpoints"] = access_endpoints
        if root_volume_config is not None:
            input["root_volume_config"] = root_volume_config
        if softwares_to_install is not None:
            input["softwares_to_install"] = softwares_to_install
        if softwares_to_uninstall is not None:
            input["softwares_to_uninstall"] = softwares_to_uninstall
        if disable_imdsv1 is not None:
            input["disable_imdsv1"] = disable_imdsv1

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_image_builder_streaming_url(
        self,
        name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        validity: Optional["aws_sdk_appstream.types.long.Long"] = None,
    ) -> "aws_sdk_appstream.types.create_image_builder_streaming_url_result.CreateImageBuilderStreamingURLResult":
        """<p>Creates a URL to start an image builder streaming session.</p>

        Args:
            name: <p>The name of the image builder.</p>
            validity: <p>The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 3600 seconds.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_image_builder_streaming_url_request.CreateImageBuilderStreamingURLRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_image_builder_streaming_url_result.CreateImageBuilderStreamingURLResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_image_builder_streaming_url

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_image_builder_streaming_url.create_image_builder_streaming_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_image_builder_streaming_url_request.CreateImageBuilderStreamingURLRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if validity is not None:
            input["validity"] = validity

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_imported_image(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        source_ami_id: Optional[
            "aws_sdk_appstream.types.photon_ami_id.PhotonAmiId"
        ] = None,
        workspace_image_id: Optional[
            "aws_sdk_appstream.types.workspace_image_id.WorkspaceImageId"
        ] = None,
        iam_role_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        description: Optional[
            "aws_sdk_appstream.types.image_import_description.ImageImportDescription"
        ] = None,
        display_name: Optional[
            "aws_sdk_appstream.types.image_import_display_name.ImageImportDisplayName"
        ] = None,
        tags: Optional["aws_sdk_appstream.types.tags.Tags"] = None,
        runtime_validation_config: Optional[
            "aws_sdk_appstream.types.runtime_validation_config.RuntimeValidationConfig"
        ] = None,
        agent_software_version: Optional[
            "aws_sdk_appstream.types.agent_software_version.AgentSoftwareVersion"
        ] = None,
        app_catalog_config: Optional[
            "aws_sdk_appstream.types.app_catalog_config.AppCatalogConfig"
        ] = None,
        dry_run: Optional["aws_sdk_appstream.types.boolean.Boolean"] = None,
    ) -> (
        "aws_sdk_appstream.types.create_imported_image_result.CreateImportedImageResult"
    ):
        """<p>Creates a custom WorkSpaces Applications image by importing an EC2 AMI. This allows you to use your own customized AMI to create WorkSpaces Applications images that support additional instance types beyond the standard stream.* instances.</p>

        Args:
            name: <p>A unique name for the imported image. The name must be between 1 and 100 characters and can contain letters, numbers, underscores, periods, and hyphens.</p>
            source_ami_id: <p>The ID of the EC2 AMI to import.</p>
            workspace_image_id: <p>The ID of the Workspaces Image to import.</p>
            iam_role_arn: <p>The ARN of the IAM role that allows WorkSpaces Applications to access your AMI. The role must have permissions to modify image attributes and describe images, with a trust relationship allowing appstream.amazonaws.com to assume the role.</p>
            description: <p>An optional description for the imported image. The description must match approved regex patterns and can be up to 256 characters.</p>
            display_name: <p>An optional display name for the imported image. The display name must match approved regex patterns and can be up to 100 characters.</p>
            tags: <p>The tags to apply to the imported image. Tags help you organize and manage your WorkSpaces Applications resources.</p>
            runtime_validation_config: <p>Configuration for runtime validation of the imported image. When specified, WorkSpaces Applications provisions an instance to test streaming functionality, which helps ensure the image is suitable for use.</p>
            agent_software_version: <p>The version of the WorkSpaces Applications agent to use for the imported image. Choose CURRENT_LATEST to use the agent version available at the time of import, or ALWAYS_LATEST to automatically update to the latest agent version when new versions are released.</p>
            app_catalog_config: <p>Configuration for the application catalog of the imported image. This allows you to specify applications available for streaming, including their paths, icons, and launch parameters. This field contains sensitive data.</p>
            dry_run: <p>When set to true, performs validation checks without actually creating the imported image. Use this to verify your configuration before executing the actual import operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_imported_image_request.CreateImportedImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_imported_image_result.CreateImportedImageResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_imported_image

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_imported_image.create_imported_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_imported_image_request.CreateImportedImageRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if source_ami_id is not None:
            input["source_ami_id"] = source_ami_id
        if workspace_image_id is not None:
            input["workspace_image_id"] = workspace_image_id
        if iam_role_arn is not None:
            input["iam_role_arn"] = iam_role_arn
        if description is not None:
            input["description"] = description
        if display_name is not None:
            input["display_name"] = display_name
        if tags is not None:
            input["tags"] = tags
        if runtime_validation_config is not None:
            input["runtime_validation_config"] = runtime_validation_config
        if agent_software_version is not None:
            input["agent_software_version"] = agent_software_version
        if app_catalog_config is not None:
            input["app_catalog_config"] = app_catalog_config
        if dry_run is not None:
            input["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_stack(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
        display_name: Optional[
            "aws_sdk_appstream.types.display_name.DisplayName"
        ] = None,
        storage_connectors: Optional[
            "aws_sdk_appstream.types.storage_connector_list.StorageConnectorList"
        ] = None,
        redirect_url: Optional[
            "aws_sdk_appstream.types.redirect_url.RedirectURL"
        ] = None,
        feedback_url: Optional[
            "aws_sdk_appstream.types.feedback_url.FeedbackURL"
        ] = None,
        user_settings: Optional[
            "aws_sdk_appstream.types.user_setting_list.UserSettingList"
        ] = None,
        application_settings: Optional[
            "aws_sdk_appstream.types.application_settings.ApplicationSettings"
        ] = None,
        tags: Optional["aws_sdk_appstream.types.tags.Tags"] = None,
        access_endpoints: Optional[
            "aws_sdk_appstream.types.access_endpoint_list.AccessEndpointList"
        ] = None,
        embed_host_domains: Optional[
            "aws_sdk_appstream.types.embed_host_domains.EmbedHostDomains"
        ] = None,
        streaming_experience_settings: Optional[
            "aws_sdk_appstream.types.streaming_experience_settings.StreamingExperienceSettings"
        ] = None,
        content_redirection: Optional[
            "aws_sdk_appstream.types.content_redirection.ContentRedirection"
        ] = None,
        agent_access_config: Optional[
            "aws_sdk_appstream.types.agent_access_config.AgentAccessConfig"
        ] = None,
    ) -> "aws_sdk_appstream.types.create_stack_result.CreateStackResult":
        """<p>Creates a stack to start streaming applications to users. A stack consists of an associated fleet, user access policies, and storage configurations. </p>

        Args:
            name: <p>The name of the stack.</p>
            description: <p>The description to display.</p>
            display_name: <p>The stack name to display.</p>
            storage_connectors: <p>The storage connectors to enable.</p>
            redirect_url: <p>The URL that users are redirected to after their streaming session ends.</p>
            feedback_url: <p>The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.</p>
            user_settings: <p>The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled. </p>
            application_settings: <p>The persistent application settings for users of a stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.</p>
            tags: <p>The tags to associate with the stack. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=. </p> <p>If you do not specify a value, the value is set to an empty string.</p> <p>Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters: </p> <p>_ . : / = + \ - @</p> <p>For more information about tags, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html\">Tagging Your Resources</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>
            access_endpoints: <p>The list of interface VPC endpoint (interface endpoint) objects. Users of the stack can connect to WorkSpaces Applications only through the specified endpoints.</p>
            embed_host_domains: <p>The domains where WorkSpaces Applications streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded WorkSpaces Applications streaming sessions. </p>
            streaming_experience_settings: <p>The streaming protocol you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.</p>
            agent_access_config: <p>The configuration for agent access on the stack. If specified, agent access is enabled for the stack.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_stack_request.CreateStackRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_stack_result.CreateStackResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_stack

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_stack.create_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_stack_request.CreateStackRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if display_name is not None:
            input["display_name"] = display_name
        if storage_connectors is not None:
            input["storage_connectors"] = storage_connectors
        if redirect_url is not None:
            input["redirect_url"] = redirect_url
        if feedback_url is not None:
            input["feedback_url"] = feedback_url
        if user_settings is not None:
            input["user_settings"] = user_settings
        if application_settings is not None:
            input["application_settings"] = application_settings
        if tags is not None:
            input["tags"] = tags
        if access_endpoints is not None:
            input["access_endpoints"] = access_endpoints
        if embed_host_domains is not None:
            input["embed_host_domains"] = embed_host_domains
        if streaming_experience_settings is not None:
            input["streaming_experience_settings"] = streaming_experience_settings
        if content_redirection is not None:
            input["content_redirection"] = content_redirection
        if agent_access_config is not None:
            input["agent_access_config"] = agent_access_config

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_streaming_url(
        self,
        stack_name: "aws_sdk_appstream.types.string.String",
        fleet_name: "aws_sdk_appstream.types.string.String",
        user_id: "aws_sdk_appstream.types.streaming_url_user_id.StreamingUrlUserId",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        application_id: Optional["aws_sdk_appstream.types.string.String"] = None,
        validity: Optional["aws_sdk_appstream.types.long.Long"] = None,
        session_context: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.create_streaming_url_result.CreateStreamingURLResult":
        """<p>Creates a temporary URL to start an WorkSpaces Applications streaming session for the specified user. A streaming URL enables application streaming to be tested without user setup. </p>

        Args:
            stack_name: <p>The name of the stack.</p>
            fleet_name: <p>The name of the fleet.</p>
            user_id: <p>The identifier of the user.</p>
            application_id: <p>The name of the application to launch after the session starts. This is the name that you specified as <b>Name</b> in the Image Assistant. If your fleet is enabled for the <b>Desktop</b> stream view, you can also choose to launch directly to the operating system desktop. To do so, specify <b>Desktop</b>.</p>
            validity: <p>The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 60 seconds.</p>
            session_context: <p>The session context. For more information, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-stacks-fleets.html#managing-stacks-fleets-parameters\">Session Context</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_streaming_url_request.CreateStreamingURLRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_streaming_url_result.CreateStreamingURLResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_streaming_url

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_streaming_url.create_streaming_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_streaming_url_request.CreateStreamingURLRequest = {}  # type: ignore[typeddict-item]
        input["stack_name"] = stack_name
        input["fleet_name"] = fleet_name
        input["user_id"] = user_id
        if application_id is not None:
            input["application_id"] = application_id
        if validity is not None:
            input["validity"] = validity
        if session_context is not None:
            input["session_context"] = session_context

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_theme_for_stack(
        self,
        stack_name: "aws_sdk_appstream.types.name.Name",
        title_text: "aws_sdk_appstream.types.theme_title_text.ThemeTitleText",
        theme_styling: "aws_sdk_appstream.types.theme_styling.ThemeStyling",
        organization_logo_s3_location: "aws_sdk_appstream.types.s3_location.S3Location",
        favicon_s3_location: "aws_sdk_appstream.types.s3_location.S3Location",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        footer_links: Optional[
            "aws_sdk_appstream.types.theme_footer_links.ThemeFooterLinks"
        ] = None,
    ) -> "aws_sdk_appstream.types.create_theme_for_stack_result.CreateThemeForStackResult":
        """<p>Creates custom branding that customizes the appearance of the streaming application catalog page.</p>

        Args:
            stack_name: <p>The name of the stack for the theme.</p>
            footer_links: <p>The links that are displayed in the footer of the streaming application catalog page. These links are helpful resources for users, such as the organization's IT support and product marketing sites.</p>
            title_text: <p>The title that is displayed at the top of the browser tab during users' application streaming sessions.</p>
            theme_styling: <p>The color theme that is applied to website links, text, and buttons. These colors are also applied as accents in the background for the streaming application catalog page.</p>
            organization_logo_s3_location: <p>The organization logo that appears on the streaming application catalog page.</p>
            favicon_s3_location: <p>The S3 location of the favicon. The favicon enables users to recognize their application streaming site in a browser full of tabs or bookmarks. It is displayed at the top of the browser tab for the application streaming site during users' streaming sessions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_theme_for_stack_request.CreateThemeForStackRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_theme_for_stack_result.CreateThemeForStackResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_theme_for_stack

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_theme_for_stack.create_theme_for_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_theme_for_stack_request.CreateThemeForStackRequest = {}  # type: ignore[typeddict-item]
        input["stack_name"] = stack_name
        if footer_links is not None:
            input["footer_links"] = footer_links
        input["title_text"] = title_text
        input["theme_styling"] = theme_styling
        input["organization_logo_s3_location"] = organization_logo_s3_location
        input["favicon_s3_location"] = favicon_s3_location

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_updated_image(
        self,
        existing_image_name: "aws_sdk_appstream.types.name.Name",
        new_image_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        new_image_description: Optional[
            "aws_sdk_appstream.types.description.Description"
        ] = None,
        new_image_display_name: Optional[
            "aws_sdk_appstream.types.display_name.DisplayName"
        ] = None,
        new_image_tags: Optional["aws_sdk_appstream.types.tags.Tags"] = None,
        dry_run: Optional["aws_sdk_appstream.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_appstream.types.create_updated_image_result.CreateUpdatedImageResult":
        """<p>Creates a new image with the latest Windows operating system updates, driver updates, and WorkSpaces Applications agent software.</p> <p>For more information, see the \"Update an Image by Using Managed WorkSpaces Applications Image Updates\" section in <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-images.html\">Administer Your WorkSpaces Applications Images</a>, in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>

        Args:
            existing_image_name: <p>The name of the image to update.</p>
            new_image_name: <p>The name of the new image. The name must be unique within the AWS account and Region.</p>
            new_image_description: <p>The description to display for the new image.</p>
            new_image_display_name: <p>The name to display for the new image.</p>
            new_image_tags: <p>The tags to associate with the new image. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=. </p> <p>Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters: </p> <p>_ . : / = + \ - @</p> <p>If you do not specify a value, the value is set to an empty string.</p> <p>For more information about tags, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html\">Tagging Your Resources</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>
            dry_run: <p>Indicates whether to display the status of image update availability before WorkSpaces Applications initiates the process of creating a new updated image. If this value is set to <code>true</code>, WorkSpaces Applications displays whether image updates are available. If this value is set to <code>false</code>, WorkSpaces Applications initiates the process of creating a new updated image without displaying whether image updates are available.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_updated_image_request.CreateUpdatedImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_updated_image_result.CreateUpdatedImageResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_updated_image

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_updated_image.create_updated_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_updated_image_request.CreateUpdatedImageRequest = {}  # type: ignore[typeddict-item]
        input["existing_image_name"] = existing_image_name
        input["new_image_name"] = new_image_name
        if new_image_description is not None:
            input["new_image_description"] = new_image_description
        if new_image_display_name is not None:
            input["new_image_display_name"] = new_image_display_name
        if new_image_tags is not None:
            input["new_image_tags"] = new_image_tags
        if dry_run is not None:
            input["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_usage_report_subscription(
        self, *, config_overrides: Optional[AppStreamClientConfig] = None
    ) -> "aws_sdk_appstream.types.create_usage_report_subscription_result.CreateUsageReportSubscriptionResult":
        """<p>Creates a usage report subscription. Usage reports are generated daily.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_usage_report_subscription_request.CreateUsageReportSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_usage_report_subscription_result.CreateUsageReportSubscriptionResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_usage_report_subscription

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_usage_report_subscription.create_usage_report_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_usage_report_subscription_request.CreateUsageReportSubscriptionRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_user(
        self,
        user_name: "aws_sdk_appstream.types.username.Username",
        authentication_type: "aws_sdk_appstream.types.authentication_type.AuthenticationType",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        message_action: Optional[
            "aws_sdk_appstream.types.message_action.MessageAction"
        ] = None,
        first_name: Optional[
            "aws_sdk_appstream.types.user_attribute_value.UserAttributeValue"
        ] = None,
        last_name: Optional[
            "aws_sdk_appstream.types.user_attribute_value.UserAttributeValue"
        ] = None,
    ) -> "aws_sdk_appstream.types.create_user_result.CreateUserResult":
        """<p>Creates a new user in the user pool.</p>

        Args:
            user_name: <p>The email address of the user.</p> <note> <p>Users' email addresses are case-sensitive. During login, if they specify an email address that doesn't use the same capitalization as the email address specified when their user pool account was created, a \"user does not exist\" error message displays.</p> </note>
            message_action: <p>The action to take for the welcome email that is sent to a user after the user is created in the user pool. If you specify SUPPRESS, no email is sent. If you specify RESEND, do not specify the first name or last name of the user. If the value is null, the email is sent. </p> <note> <p>The temporary password in the welcome email is valid for only 7 days. If users don’t set their passwords within 7 days, you must send them a new welcome email.</p> </note>
            first_name: <p>The first name, or given name, of the user.</p>
            last_name: <p>The last name, or surname, of the user.</p>
            authentication_type: <p>The authentication type for the user. You must specify USERPOOL. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.create_user_result.CreateUserResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.create_user

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.create_user_request.CreateUserRequest = {}  # type: ignore[typeddict-item]
        input["user_name"] = user_name
        if message_action is not None:
            input["message_action"] = message_action
        if first_name is not None:
            input["first_name"] = first_name
        if last_name is not None:
            input["last_name"] = last_name
        input["authentication_type"] = authentication_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_app_block(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_app_block_result.DeleteAppBlockResult":
        """<p>Deletes an app block.</p>

        Args:
            name: <p>The name of the app block.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_app_block_request.DeleteAppBlockRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_app_block_result.DeleteAppBlockResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_app_block

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_app_block.delete_app_block(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_app_block_request.DeleteAppBlockRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_app_block_builder(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_app_block_builder_result.DeleteAppBlockBuilderResult":
        """<p>Deletes an app block builder.</p> <p>An app block builder can only be deleted when it has no association with an app block.</p>

        Args:
            name: <p>The name of the app block builder.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_app_block_builder_request.DeleteAppBlockBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_app_block_builder_result.DeleteAppBlockBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_app_block_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_app_block_builder.delete_app_block_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_app_block_builder_request.DeleteAppBlockBuilderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_application(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_application_result.DeleteApplicationResult":
        """<p>Deletes an application.</p>

        Args:
            name: <p>The name of the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_application_result.DeleteApplicationResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_application

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_application_request.DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_directory_config(
        self,
        directory_name: "aws_sdk_appstream.types.directory_name.DirectoryName",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_directory_config_result.DeleteDirectoryConfigResult":
        """<p>Deletes the specified Directory Config object from WorkSpaces Applications. This object includes the information required to join streaming instances to an Active Directory domain.</p>

        Args:
            directory_name: <p>The name of the directory configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_directory_config_request.DeleteDirectoryConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_directory_config_result.DeleteDirectoryConfigResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_directory_config

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_directory_config.delete_directory_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_directory_config_request.DeleteDirectoryConfigRequest = {}  # type: ignore[typeddict-item]
        input["directory_name"] = directory_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_entitlement(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        stack_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_entitlement_result.DeleteEntitlementResult":
        """<p>Deletes the specified entitlement.</p>

        Args:
            name: <p>The name of the entitlement.</p>
            stack_name: <p>The name of the stack with which the entitlement is associated.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_entitlement_request.DeleteEntitlementRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_entitlement_result.DeleteEntitlementResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_entitlement

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_entitlement.delete_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_entitlement_request.DeleteEntitlementRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["stack_name"] = stack_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_fleet(
        self,
        name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_fleet_result.DeleteFleetResult":
        """<p>Deletes the specified fleet.</p>

        Args:
            name: <p>The name of the fleet.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_fleet_request.DeleteFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_fleet_result.DeleteFleetResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_fleet

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_fleet.delete_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_fleet_request.DeleteFleetRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_image(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_image_result.DeleteImageResult":
        """<p>Deletes the specified image. You cannot delete an image when it is in use. After you delete an image, you cannot provision new capacity using the image.</p>

        Args:
            name: <p>The name of the image.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_image_request.DeleteImageRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_image_result.DeleteImageResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_image

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_image.delete_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_image_request.DeleteImageRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_image_builder(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_image_builder_result.DeleteImageBuilderResult":
        """<p>Deletes the specified image builder and releases the capacity.</p>

        Args:
            name: <p>The name of the image builder.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_image_builder_request.DeleteImageBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_image_builder_result.DeleteImageBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_image_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_image_builder.delete_image_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_image_builder_request.DeleteImageBuilderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_image_permissions(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        shared_account_id: "aws_sdk_appstream.types.aws_account_id.AwsAccountId",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_image_permissions_result.DeleteImagePermissionsResult":
        """<p>Deletes permissions for the specified private image. After you delete permissions for an image, AWS accounts to which you previously granted these permissions can no longer use the image.</p>

        Args:
            name: <p>The name of the private image.</p>
            shared_account_id: <p>The 12-digit identifier of the AWS account for which to delete image permissions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_image_permissions_request.DeleteImagePermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_image_permissions_result.DeleteImagePermissionsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_image_permissions

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_image_permissions.delete_image_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_image_permissions_request.DeleteImagePermissionsRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["shared_account_id"] = shared_account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_stack(
        self,
        name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_stack_result.DeleteStackResult":
        """<p>Deletes the specified stack. After the stack is deleted, the application streaming environment provided by the stack is no longer available to users. Also, any reservations made for application streaming sessions for the stack are released.</p>

        Args:
            name: <p>The name of the stack.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_stack_request.DeleteStackRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_stack_result.DeleteStackResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_stack

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_stack.delete_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_stack_request.DeleteStackRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_theme_for_stack(
        self,
        stack_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_theme_for_stack_result.DeleteThemeForStackResult":
        """<p>Deletes custom branding that customizes the appearance of the streaming application catalog page.</p>

        Args:
            stack_name: <p>The name of the stack for the theme.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_theme_for_stack_request.DeleteThemeForStackRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_theme_for_stack_result.DeleteThemeForStackResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_theme_for_stack

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_theme_for_stack.delete_theme_for_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_theme_for_stack_request.DeleteThemeForStackRequest = {}  # type: ignore[typeddict-item]
        input["stack_name"] = stack_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_usage_report_subscription(
        self, *, config_overrides: Optional[AppStreamClientConfig] = None
    ) -> "aws_sdk_appstream.types.delete_usage_report_subscription_result.DeleteUsageReportSubscriptionResult":
        """<p>Disables usage report generation.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_usage_report_subscription_request.DeleteUsageReportSubscriptionRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_usage_report_subscription_result.DeleteUsageReportSubscriptionResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_usage_report_subscription

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_usage_report_subscription.delete_usage_report_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_usage_report_subscription_request.DeleteUsageReportSubscriptionRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_user(
        self,
        user_name: "aws_sdk_appstream.types.username.Username",
        authentication_type: "aws_sdk_appstream.types.authentication_type.AuthenticationType",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.delete_user_result.DeleteUserResult":
        """<p>Deletes a user from the user pool.</p>

        Args:
            user_name: <p>The email address of the user.</p> <note> <p>Users' email addresses are case-sensitive.</p> </note>
            authentication_type: <p>The authentication type for the user. You must specify USERPOOL.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.delete_user_request.DeleteUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.delete_user_result.DeleteUserResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.delete_user

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.delete_user.delete_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.delete_user_request.DeleteUserRequest = {}  # type: ignore[typeddict-item]
        input["user_name"] = user_name
        input["authentication_type"] = authentication_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_app_block_builder_app_block_associations(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        app_block_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        app_block_builder_name: Optional["aws_sdk_appstream.types.name.Name"] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_app_block_builder_app_block_associations_result.DescribeAppBlockBuilderAppBlockAssociationsResult":
        """<p>Retrieves a list that describes one or more app block builder associations.</p>

        Args:
            app_block_arn: <p>The ARN of the app block.</p>
            app_block_builder_name: <p>The name of the app block builder.</p>
            max_results: <p>The maximum size of each page of results.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_app_block_builder_app_block_associations_request.DescribeAppBlockBuilderAppBlockAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_app_block_builder_app_block_associations_result.DescribeAppBlockBuilderAppBlockAssociationsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_app_block_builder_app_block_associations

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_app_block_builder_app_block_associations.describe_app_block_builder_app_block_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_app_block_builder_app_block_associations_request.DescribeAppBlockBuilderAppBlockAssociationsRequest = {}  # type: ignore[typeddict-item]
        if app_block_arn is not None:
            input["app_block_arn"] = app_block_arn
        if app_block_builder_name is not None:
            input["app_block_builder_name"] = app_block_builder_name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_app_block_builders(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        names: Optional["aws_sdk_appstream.types.string_list.StringList"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
    ) -> "aws_sdk_appstream.types.describe_app_block_builders_result.DescribeAppBlockBuildersResult":
        """<p>Retrieves a list that describes one or more app block builders.</p>

        Args:
            names: <p>The names of the app block builders.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum size of each page of results. The maximum value is 25.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_app_block_builders_request.DescribeAppBlockBuildersRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_app_block_builders_result.DescribeAppBlockBuildersResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_app_block_builders

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_app_block_builders.describe_app_block_builders(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_app_block_builders_request.DescribeAppBlockBuildersRequest = {}  # type: ignore[typeddict-item]
        if names is not None:
            input["names"] = names
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

    def describe_app_blocks(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        arns: Optional["aws_sdk_appstream.types.arn_list.ArnList"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
    ) -> "aws_sdk_appstream.types.describe_app_blocks_result.DescribeAppBlocksResult":
        """<p>Retrieves a list that describes one or more app blocks.</p>

        Args:
            arns: <p>The ARNs of the app blocks.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum size of each page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_app_blocks_request.DescribeAppBlocksRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_app_blocks_result.DescribeAppBlocksResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_app_blocks

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_app_blocks.describe_app_blocks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_app_blocks_request.DescribeAppBlocksRequest = {}  # type: ignore[typeddict-item]
        if arns is not None:
            input["arns"] = arns
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

    def describe_application_fleet_associations(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        fleet_name: Optional["aws_sdk_appstream.types.name.Name"] = None,
        application_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_application_fleet_associations_result.DescribeApplicationFleetAssociationsResult":
        """<p>Retrieves a list that describes one or more application fleet associations. Either ApplicationArn or FleetName must be specified.</p>

        Args:
            fleet_name: <p>The name of the fleet.</p>
            application_arn: <p>The ARN of the application.</p>
            max_results: <p>The maximum size of each page of results.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_application_fleet_associations_request.DescribeApplicationFleetAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_application_fleet_associations_result.DescribeApplicationFleetAssociationsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_application_fleet_associations

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_application_fleet_associations.describe_application_fleet_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_application_fleet_associations_request.DescribeApplicationFleetAssociationsRequest = {}  # type: ignore[typeddict-item]
        if fleet_name is not None:
            input["fleet_name"] = fleet_name
        if application_arn is not None:
            input["application_arn"] = application_arn
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_applications(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        arns: Optional["aws_sdk_appstream.types.arn_list.ArnList"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
    ) -> "aws_sdk_appstream.types.describe_applications_result.DescribeApplicationsResult":
        """<p>Retrieves a list that describes one or more applications.</p>

        Args:
            arns: <p>The ARNs for the applications.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum size of each page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_applications_request.DescribeApplicationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_applications_result.DescribeApplicationsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_applications

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_applications.describe_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_applications_request.DescribeApplicationsRequest = {}  # type: ignore[typeddict-item]
        if arns is not None:
            input["arns"] = arns
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

    def describe_app_license_usage(
        self,
        billing_period: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_app_license_usage_result.DescribeAppLicenseUsageResult":
        """<p>Retrieves license included application usage information.</p>

        Args:
            billing_period: <p>Billing period for the usage record.</p> <p>Specify the value in <i>yyyy-mm</i> format. For example, for August 2025, use <i>2025-08</i>.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>Token for pagination of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_app_license_usage_request.DescribeAppLicenseUsageRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_app_license_usage_result.DescribeAppLicenseUsageResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_app_license_usage

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_app_license_usage.describe_app_license_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_app_license_usage_request.DescribeAppLicenseUsageRequest = {}  # type: ignore[typeddict-item]
        input["billing_period"] = billing_period
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_directory_configs(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        directory_names: Optional[
            "aws_sdk_appstream.types.directory_name_list.DirectoryNameList"
        ] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_directory_configs_result.DescribeDirectoryConfigsResult":
        """<p>Retrieves a list that describes one or more specified Directory Config objects for WorkSpaces Applications, if the names for these objects are provided. Otherwise, all Directory Config objects in the account are described. These objects include the configuration information required to join fleets and image builders to Microsoft Active Directory domains. </p> <p>Although the response syntax in this topic includes the account password, this password is not returned in the actual response.</p>

        Args:
            directory_names: <p>The directory names.</p>
            max_results: <p>The maximum size of each page of results.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_directory_configs_request.DescribeDirectoryConfigsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_directory_configs_result.DescribeDirectoryConfigsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_directory_configs

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_directory_configs.describe_directory_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_directory_configs_request.DescribeDirectoryConfigsRequest = {}  # type: ignore[typeddict-item]
        if directory_names is not None:
            input["directory_names"] = directory_names
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_entitlements(
        self,
        stack_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        name: Optional["aws_sdk_appstream.types.name.Name"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
    ) -> "aws_sdk_appstream.types.describe_entitlements_result.DescribeEntitlementsResult":
        """<p>Retrieves a list that describes one of more entitlements.</p>

        Args:
            name: <p>The name of the entitlement.</p>
            stack_name: <p>The name of the stack with which the entitlement is associated.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum size of each page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_entitlements_request.DescribeEntitlementsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_entitlements_result.DescribeEntitlementsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_entitlements

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_entitlements.describe_entitlements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_entitlements_request.DescribeEntitlementsRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input["name"] = name
        input["stack_name"] = stack_name
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

    def describe_fleets(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        names: Optional["aws_sdk_appstream.types.string_list.StringList"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_fleets_result.DescribeFleetsResult":
        """<p>Retrieves a list that describes one or more specified fleets, if the fleet names are provided. Otherwise, all fleets in the account are described.</p>

        Args:
            names: <p>The names of the fleets to describe.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_fleets_request.DescribeFleetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_fleets_result.DescribeFleetsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_fleets

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_fleets.describe_fleets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_fleets_request.DescribeFleetsRequest = {}  # type: ignore[typeddict-item]
        if names is not None:
            input["names"] = names
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_image_builders(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        names: Optional["aws_sdk_appstream.types.string_list.StringList"] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_image_builders_result.DescribeImageBuildersResult":
        """<p>Retrieves a list that describes one or more specified image builders, if the image builder names are provided. Otherwise, all image builders in the account are described.</p>

        Args:
            names: <p>The names of the image builders to describe.</p>
            max_results: <p>The maximum size of each page of results.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_image_builders_request.DescribeImageBuildersRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_image_builders_result.DescribeImageBuildersResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_image_builders

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_image_builders.describe_image_builders(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_image_builders_request.DescribeImageBuildersRequest = {}  # type: ignore[typeddict-item]
        if names is not None:
            input["names"] = names
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_image_permissions(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        max_results: Optional["aws_sdk_appstream.types.max_results.MaxResults"] = None,
        shared_aws_account_ids: Optional[
            "aws_sdk_appstream.types.aws_account_id_list.AwsAccountIdList"
        ] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_image_permissions_result.DescribeImagePermissionsResult":
        """<p>Retrieves a list that describes the permissions for shared AWS account IDs on a private image that you own. </p>

        Args:
            name: <p>The name of the private image for which to describe permissions. The image must be one that you own. </p>
            max_results: <p>The maximum size of each page of results.</p>
            shared_aws_account_ids: <p>The 12-digit identifier of one or more AWS accounts with which the image is shared.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_image_permissions_request.DescribeImagePermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_image_permissions_result.DescribeImagePermissionsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_image_permissions

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_image_permissions.describe_image_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_image_permissions_request.DescribeImagePermissionsRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if max_results is not None:
            input["max_results"] = max_results
        if shared_aws_account_ids is not None:
            input["shared_aws_account_ids"] = shared_aws_account_ids
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_images(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        names: Optional["aws_sdk_appstream.types.string_list.StringList"] = None,
        arns: Optional["aws_sdk_appstream.types.arn_list.ArnList"] = None,
        type: Optional["aws_sdk_appstream.types.visibility_type.VisibilityType"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_appstream.types.describe_images_max_results.DescribeImagesMaxResults"
        ] = None,
    ) -> "aws_sdk_appstream.types.describe_images_result.DescribeImagesResult":
        """<p>Retrieves a list that describes one or more specified images, if the image names or image ARNs are provided. Otherwise, all images in the account are described.</p>

        Args:
            names: <p>The names of the public or private images to describe.</p>
            arns: <p>The ARNs of the public, private, and shared images to describe.</p>
            type: <p>The type of image (public, private, or shared) to describe. </p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
            max_results: <p>The maximum size of each page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_images_request.DescribeImagesRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_images_result.DescribeImagesResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_images

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_images.describe_images(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_images_request.DescribeImagesRequest = {}  # type: ignore[typeddict-item]
        if names is not None:
            input["names"] = names
        if arns is not None:
            input["arns"] = arns
        if type is not None:
            input["type"] = type
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

    def describe_sessions(
        self,
        stack_name: "aws_sdk_appstream.types.name.Name",
        fleet_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        user_id: Optional["aws_sdk_appstream.types.user_id.UserId"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
        limit: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
        authentication_type: Optional[
            "aws_sdk_appstream.types.authentication_type.AuthenticationType"
        ] = None,
        instance_id: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_sessions_result.DescribeSessionsResult":
        """<p>Retrieves a list that describes the streaming sessions for a specified stack and fleet. If a UserId is provided for the stack and fleet, only streaming sessions for that user are described. If an authentication type is not provided, the default is to authenticate users using a streaming URL.</p>

        Args:
            stack_name: <p>The name of the stack. This value is case-sensitive.</p>
            fleet_name: <p>The name of the fleet. This value is case-sensitive.</p>
            user_id: <p>The user identifier (ID). If you specify a user ID, you must also specify the authentication type.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
            limit: <p>The size of each page of results. The default value is 20 and the maximum value is 50.</p>
            authentication_type: <p>The authentication method. Specify <code>API</code> for a user authenticated using a streaming URL or <code>SAML</code> for a SAML federated user. The default is to authenticate users using a streaming URL.</p>
            instance_id: <p>The identifier for the instance hosting the session.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_sessions_request.DescribeSessionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_sessions_result.DescribeSessionsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_sessions

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_sessions.describe_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_sessions_request.DescribeSessionsRequest = {}  # type: ignore[typeddict-item]
        input["stack_name"] = stack_name
        input["fleet_name"] = fleet_name
        if user_id is not None:
            input["user_id"] = user_id
        if next_token is not None:
            input["next_token"] = next_token
        if limit is not None:
            input["limit"] = limit
        if authentication_type is not None:
            input["authentication_type"] = authentication_type
        if instance_id is not None:
            input["instance_id"] = instance_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_software_associations(
        self,
        associated_resource: "aws_sdk_appstream.types.arn.Arn",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_software_associations_result.DescribeSoftwareAssociationsResult":
        """<p>Retrieves license included application associations for a specified resource.</p>

        Args:
            associated_resource: <p>The ARN of the resource to describe software associations. Possible resources are Image and ImageBuilder.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_software_associations_request.DescribeSoftwareAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_software_associations_result.DescribeSoftwareAssociationsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_software_associations

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_software_associations.describe_software_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_software_associations_request.DescribeSoftwareAssociationsRequest = {}  # type: ignore[typeddict-item]
        input["associated_resource"] = associated_resource
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_stacks(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        names: Optional["aws_sdk_appstream.types.string_list.StringList"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_stacks_result.DescribeStacksResult":
        """<p>Retrieves a list that describes one or more specified stacks, if the stack names are provided. Otherwise, all stacks in the account are described.</p>

        Args:
            names: <p>The names of the stacks to describe.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_stacks_request.DescribeStacksRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_stacks_result.DescribeStacksResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_stacks

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_stacks.describe_stacks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_stacks_request.DescribeStacksRequest = {}  # type: ignore[typeddict-item]
        if names is not None:
            input["names"] = names
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_theme_for_stack(
        self,
        stack_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.describe_theme_for_stack_result.DescribeThemeForStackResult":
        """<p>Retrieves a list that describes the theme for a specified stack. A theme is custom branding that customizes the appearance of the streaming application catalog page.</p>

        Args:
            stack_name: <p>The name of the stack for the theme.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_theme_for_stack_request.DescribeThemeForStackRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_theme_for_stack_result.DescribeThemeForStackResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_theme_for_stack

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_theme_for_stack.describe_theme_for_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_theme_for_stack_request.DescribeThemeForStackRequest = {}  # type: ignore[typeddict-item]
        input["stack_name"] = stack_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_usage_report_subscriptions(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_usage_report_subscriptions_result.DescribeUsageReportSubscriptionsResult":
        """<p>Retrieves a list that describes one or more usage report subscriptions.</p>

        Args:
            max_results: <p>The maximum size of each page of results.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_usage_report_subscriptions_request.DescribeUsageReportSubscriptionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_usage_report_subscriptions_result.DescribeUsageReportSubscriptionsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_usage_report_subscriptions

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_usage_report_subscriptions.describe_usage_report_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_usage_report_subscriptions_request.DescribeUsageReportSubscriptionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_users(
        self,
        authentication_type: "aws_sdk_appstream.types.authentication_type.AuthenticationType",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_users_result.DescribeUsersResult":
        """<p>Retrieves a list that describes one or more specified users in the user pool.</p>

        Args:
            authentication_type: <p>The authentication type for the users in the user pool to describe. You must specify USERPOOL.</p>
            max_results: <p>The maximum size of each page of results.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_users_request.DescribeUsersRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_users_result.DescribeUsersResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_users

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_users.describe_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_users_request.DescribeUsersRequest = {}  # type: ignore[typeddict-item]
        input["authentication_type"] = authentication_type
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_user_stack_associations(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        stack_name: Optional["aws_sdk_appstream.types.string.String"] = None,
        user_name: Optional["aws_sdk_appstream.types.username.Username"] = None,
        authentication_type: Optional[
            "aws_sdk_appstream.types.authentication_type.AuthenticationType"
        ] = None,
        max_results: Optional["aws_sdk_appstream.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.describe_user_stack_associations_result.DescribeUserStackAssociationsResult":
        """<p>Retrieves a list that describes the UserStackAssociation objects. You must specify either or both of the following:</p> <ul> <li> <p>The stack name</p> </li> <li> <p>The user name (email address of the user associated with the stack) and the authentication type for the user</p> </li> </ul>

        Args:
            stack_name: <p>The name of the stack that is associated with the user.</p>
            user_name: <p>The email address of the user who is associated with the stack.</p> <note> <p>Users' email addresses are case-sensitive.</p> </note>
            authentication_type: <p>The authentication type for the user who is associated with the stack. You must specify USERPOOL.</p>
            max_results: <p>The maximum size of each page of results.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.describe_user_stack_associations_request.DescribeUserStackAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.describe_user_stack_associations_result.DescribeUserStackAssociationsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.describe_user_stack_associations

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.describe_user_stack_associations.describe_user_stack_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.describe_user_stack_associations_request.DescribeUserStackAssociationsRequest = {}  # type: ignore[typeddict-item]
        if stack_name is not None:
            input["stack_name"] = stack_name
        if user_name is not None:
            input["user_name"] = user_name
        if authentication_type is not None:
            input["authentication_type"] = authentication_type
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable_user(
        self,
        user_name: "aws_sdk_appstream.types.username.Username",
        authentication_type: "aws_sdk_appstream.types.authentication_type.AuthenticationType",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.disable_user_result.DisableUserResult":
        """<p>Disables the specified user in the user pool. Users can't sign in to WorkSpaces Applications until they are re-enabled. This action does not delete the user. </p>

        Args:
            user_name: <p>The email address of the user.</p> <note> <p>Users' email addresses are case-sensitive.</p> </note>
            authentication_type: <p>The authentication type for the user. You must specify USERPOOL.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.disable_user_request.DisableUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.disable_user_result.DisableUserResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.disable_user

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.disable_user.disable_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.disable_user_request.DisableUserRequest = {}  # type: ignore[typeddict-item]
        input["user_name"] = user_name
        input["authentication_type"] = authentication_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_app_block_builder_app_block(
        self,
        app_block_arn: "aws_sdk_appstream.types.arn.Arn",
        app_block_builder_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.disassociate_app_block_builder_app_block_result.DisassociateAppBlockBuilderAppBlockResult":
        """<p>Disassociates a specified app block builder from a specified app block.</p>

        Args:
            app_block_arn: <p>The ARN of the app block.</p>
            app_block_builder_name: <p>The name of the app block builder.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.disassociate_app_block_builder_app_block_request.DisassociateAppBlockBuilderAppBlockRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.disassociate_app_block_builder_app_block_result.DisassociateAppBlockBuilderAppBlockResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.disassociate_app_block_builder_app_block

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.disassociate_app_block_builder_app_block.disassociate_app_block_builder_app_block(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.disassociate_app_block_builder_app_block_request.DisassociateAppBlockBuilderAppBlockRequest = {}  # type: ignore[typeddict-item]
        input["app_block_arn"] = app_block_arn
        input["app_block_builder_name"] = app_block_builder_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_application_fleet(
        self,
        fleet_name: "aws_sdk_appstream.types.name.Name",
        application_arn: "aws_sdk_appstream.types.arn.Arn",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.disassociate_application_fleet_result.DisassociateApplicationFleetResult":
        """<p>Disassociates the specified application from the fleet.</p>

        Args:
            fleet_name: <p>The name of the fleet.</p>
            application_arn: <p>The ARN of the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.disassociate_application_fleet_request.DisassociateApplicationFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.disassociate_application_fleet_result.DisassociateApplicationFleetResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.disassociate_application_fleet

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.disassociate_application_fleet.disassociate_application_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.disassociate_application_fleet_request.DisassociateApplicationFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_name"] = fleet_name
        input["application_arn"] = application_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_application_from_entitlement(
        self,
        stack_name: "aws_sdk_appstream.types.name.Name",
        entitlement_name: "aws_sdk_appstream.types.name.Name",
        application_identifier: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.disassociate_application_from_entitlement_result.DisassociateApplicationFromEntitlementResult":
        """<p>Deletes the specified application from the specified entitlement.</p>

        Args:
            stack_name: <p>The name of the stack with which the entitlement is associated.</p>
            entitlement_name: <p>The name of the entitlement.</p>
            application_identifier: <p>The identifier of the application to remove from the entitlement.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.disassociate_application_from_entitlement_request.DisassociateApplicationFromEntitlementRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.disassociate_application_from_entitlement_result.DisassociateApplicationFromEntitlementResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.disassociate_application_from_entitlement

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.disassociate_application_from_entitlement.disassociate_application_from_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.disassociate_application_from_entitlement_request.DisassociateApplicationFromEntitlementRequest = {}  # type: ignore[typeddict-item]
        input["stack_name"] = stack_name
        input["entitlement_name"] = entitlement_name
        input["application_identifier"] = application_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_fleet(
        self,
        fleet_name: "aws_sdk_appstream.types.string.String",
        stack_name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.disassociate_fleet_result.DisassociateFleetResult":
        """<p>Disassociates the specified fleet from the specified stack.</p>

        Args:
            fleet_name: <p>The name of the fleet.</p>
            stack_name: <p>The name of the stack.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.disassociate_fleet_request.DisassociateFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.disassociate_fleet_result.DisassociateFleetResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.disassociate_fleet

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.disassociate_fleet.disassociate_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.disassociate_fleet_request.DisassociateFleetRequest = {}  # type: ignore[typeddict-item]
        input["fleet_name"] = fleet_name
        input["stack_name"] = stack_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_software_from_image_builder(
        self,
        image_builder_name: "aws_sdk_appstream.types.name.Name",
        software_names: "aws_sdk_appstream.types.string_list.StringList",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.disassociate_software_from_image_builder_result.DisassociateSoftwareFromImageBuilderResult":
        """<p>Removes license included application(s) association(s) from an image builder instance.</p>

        Args:
            image_builder_name: <p>The name of the target image builder instance.</p>
            software_names: <p>The list of license included applications to disassociate from the image builder.</p> <p>Possible values include the following:</p> <ul> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_64Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_64Bit</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.disassociate_software_from_image_builder_request.DisassociateSoftwareFromImageBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.disassociate_software_from_image_builder_result.DisassociateSoftwareFromImageBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.disassociate_software_from_image_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.disassociate_software_from_image_builder.disassociate_software_from_image_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.disassociate_software_from_image_builder_request.DisassociateSoftwareFromImageBuilderRequest = {}  # type: ignore[typeddict-item]
        input["image_builder_name"] = image_builder_name
        input["software_names"] = software_names

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def drain_session_instance(
        self,
        session_id: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.drain_session_instance_result.DrainSessionInstanceResult":
        """<p>Drains the instance hosting the specified streaming session. The instance stops accepting new sessions while existing sessions continue uninterrupted. Once all sessions end, the instance is reclaimed and replaced. This only applies to multi-session fleets.</p>

        Args:
            session_id: <p>The identifier of the streaming session.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.drain_session_instance_request.DrainSessionInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.drain_session_instance_result.DrainSessionInstanceResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.drain_session_instance

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.drain_session_instance.drain_session_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.drain_session_instance_request.DrainSessionInstanceRequest = {}  # type: ignore[typeddict-item]
        input["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_user(
        self,
        user_name: "aws_sdk_appstream.types.username.Username",
        authentication_type: "aws_sdk_appstream.types.authentication_type.AuthenticationType",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.enable_user_result.EnableUserResult":
        """<p>Enables a user in the user pool. After being enabled, users can sign in to WorkSpaces Applications and open applications from the stacks to which they are assigned.</p>

        Args:
            user_name: <p>The email address of the user.</p> <note> <p>Users' email addresses are case-sensitive. During login, if they specify an email address that doesn't use the same capitalization as the email address specified when their user pool account was created, a \"user does not exist\" error message displays. </p> </note>
            authentication_type: <p>The authentication type for the user. You must specify USERPOOL.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.enable_user_request.EnableUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.enable_user_result.EnableUserResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.enable_user

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.enable_user.enable_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.enable_user_request.EnableUserRequest = {}  # type: ignore[typeddict-item]
        input["user_name"] = user_name
        input["authentication_type"] = authentication_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def expire_session(
        self,
        session_id: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.expire_session_result.ExpireSessionResult":
        """<p>Immediately stops the specified streaming session.</p>

        Args:
            session_id: <p>The identifier of the streaming session.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.expire_session_request.ExpireSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.expire_session_result.ExpireSessionResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.expire_session

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.expire_session.expire_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.expire_session_request.ExpireSessionRequest = {}  # type: ignore[typeddict-item]
        input["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_export_image_task(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        task_id: Optional["aws_sdk_appstream.types.uuid.UUID"] = None,
    ) -> (
        "aws_sdk_appstream.types.get_export_image_task_result.GetExportImageTaskResult"
    ):
        """<p>Retrieves information about an export image task, including its current state, progress, and any error details.</p>

        Args:
            task_id: <p>The unique identifier of the export image task to retrieve information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.get_export_image_task_request.GetExportImageTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.get_export_image_task_result.GetExportImageTaskResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.get_export_image_task

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.get_export_image_task.get_export_image_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.get_export_image_task_request.GetExportImageTaskRequest = {}  # type: ignore[typeddict-item]
        if task_id is not None:
            input["task_id"] = task_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_associated_fleets(
        self,
        stack_name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.list_associated_fleets_result.ListAssociatedFleetsResult":
        """<p>Retrieves the name of the fleet that is associated with the specified stack.</p>

        Args:
            stack_name: <p>The name of the stack.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.list_associated_fleets_request.ListAssociatedFleetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.list_associated_fleets_result.ListAssociatedFleetsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.list_associated_fleets

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.list_associated_fleets.list_associated_fleets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.list_associated_fleets_request.ListAssociatedFleetsRequest = {}  # type: ignore[typeddict-item]
        input["stack_name"] = stack_name
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_associated_stacks(
        self,
        fleet_name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.list_associated_stacks_result.ListAssociatedStacksResult":
        """<p>Retrieves the name of the stack with which the specified fleet is associated.</p>

        Args:
            fleet_name: <p>The name of the fleet.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.list_associated_stacks_request.ListAssociatedStacksRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.list_associated_stacks_result.ListAssociatedStacksResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.list_associated_stacks

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.list_associated_stacks.list_associated_stacks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.list_associated_stacks_request.ListAssociatedStacksRequest = {}  # type: ignore[typeddict-item]
        input["fleet_name"] = fleet_name
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_entitled_applications(
        self,
        stack_name: "aws_sdk_appstream.types.name.Name",
        entitlement_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
        max_results: Optional["aws_sdk_appstream.types.integer.Integer"] = None,
    ) -> "aws_sdk_appstream.types.list_entitled_applications_result.ListEntitledApplicationsResult":
        """<p>Retrieves a list of entitled applications.</p>

        Args:
            stack_name: <p>The name of the stack with which the entitlement is associated.</p>
            entitlement_name: <p>The name of the entitlement.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum size of each page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.list_entitled_applications_request.ListEntitledApplicationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.list_entitled_applications_result.ListEntitledApplicationsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.list_entitled_applications

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.list_entitled_applications.list_entitled_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.list_entitled_applications_request.ListEntitledApplicationsRequest = {}  # type: ignore[typeddict-item]
        input["stack_name"] = stack_name
        input["entitlement_name"] = entitlement_name
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

    def list_export_image_tasks(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        filters: Optional["aws_sdk_appstream.types.filters.Filters"] = None,
        max_results: Optional["aws_sdk_appstream.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_appstream.types.string.String"] = None,
    ) -> "aws_sdk_appstream.types.list_export_image_tasks_result.ListExportImageTasksResult":
        """<p>Lists export image tasks, with optional filtering and pagination. Use this operation to monitor the status of multiple export operations.</p>

        Args:
            filters: <p>Optional filters to apply when listing export image tasks. Filters help you narrow down the results based on specific criteria.</p>
            max_results: <p>The maximum number of export image tasks to return in a single request. The valid range is 1-500, with a default of 50.</p>
            next_token: <p>The pagination token from a previous request. Use this to retrieve the next page of results when there are more tasks than the MaxResults limit.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.list_export_image_tasks_request.ListExportImageTasksRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.list_export_image_tasks_result.ListExportImageTasksResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.list_export_image_tasks

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.list_export_image_tasks.list_export_image_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.list_export_image_tasks_request.ListExportImageTasksRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_appstream.types.arn.Arn",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves a list of all tags for the specified WorkSpaces Applications resource. You can tag WorkSpaces Applications image builders, images, fleets, and stacks.</p> <p>For more information about tags, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html\">Tagging Your Resources</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_app_block_builder(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.start_app_block_builder_result.StartAppBlockBuilderResult":
        """<p>Starts an app block builder.</p> <p>An app block builder can only be started when it's associated with an app block.</p> <p>Starting an app block builder starts a new instance, which is equivalent to an elastic fleet instance with application builder assistance functionality.</p>

        Args:
            name: <p>The name of the app block builder.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.start_app_block_builder_request.StartAppBlockBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.start_app_block_builder_result.StartAppBlockBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.start_app_block_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.start_app_block_builder.start_app_block_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.start_app_block_builder_request.StartAppBlockBuilderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_fleet(
        self,
        name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.start_fleet_result.StartFleetResult":
        """<p>Starts the specified fleet.</p>

        Args:
            name: <p>The name of the fleet.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.start_fleet_request.StartFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.start_fleet_result.StartFleetResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.start_fleet

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.start_fleet.start_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.start_fleet_request.StartFleetRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_image_builder(
        self,
        name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        appstream_agent_version: Optional[
            "aws_sdk_appstream.types.appstream_agent_version.AppstreamAgentVersion"
        ] = None,
    ) -> "aws_sdk_appstream.types.start_image_builder_result.StartImageBuilderResult":
        """<p>Starts the specified image builder.</p>

        Args:
            name: <p>The name of the image builder.</p>
            appstream_agent_version: <p>The version of the WorkSpaces Applications agent to use for this image builder. To use the latest version of the WorkSpaces Applications agent, specify [LATEST]. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.start_image_builder_request.StartImageBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.start_image_builder_result.StartImageBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.start_image_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.start_image_builder.start_image_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.start_image_builder_request.StartImageBuilderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if appstream_agent_version is not None:
            input["appstream_agent_version"] = appstream_agent_version

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_software_deployment_to_image_builder(
        self,
        image_builder_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        retry_failed_deployments: Optional[
            "aws_sdk_appstream.types.boolean.Boolean"
        ] = None,
    ) -> "aws_sdk_appstream.types.start_software_deployment_to_image_builder_result.StartSoftwareDeploymentToImageBuilderResult":
        """<p>Initiates license included applications deployment to an image builder instance.</p>

        Args:
            image_builder_name: <p>The name of the target image builder instance.</p>
            retry_failed_deployments: <p>Whether to retry previously failed license included application deployments.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.start_software_deployment_to_image_builder_request.StartSoftwareDeploymentToImageBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.start_software_deployment_to_image_builder_result.StartSoftwareDeploymentToImageBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.start_software_deployment_to_image_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.start_software_deployment_to_image_builder.start_software_deployment_to_image_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.start_software_deployment_to_image_builder_request.StartSoftwareDeploymentToImageBuilderRequest = {}  # type: ignore[typeddict-item]
        input["image_builder_name"] = image_builder_name
        if retry_failed_deployments is not None:
            input["retry_failed_deployments"] = retry_failed_deployments

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_app_block_builder(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.stop_app_block_builder_result.StopAppBlockBuilderResult":
        """<p>Stops an app block builder.</p> <p>Stopping an app block builder terminates the instance, and the instance state is not persisted.</p>

        Args:
            name: <p>The name of the app block builder.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.stop_app_block_builder_request.StopAppBlockBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.stop_app_block_builder_result.StopAppBlockBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.stop_app_block_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.stop_app_block_builder.stop_app_block_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.stop_app_block_builder_request.StopAppBlockBuilderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_fleet(
        self,
        name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.stop_fleet_result.StopFleetResult":
        """<p>Stops the specified fleet.</p>

        Args:
            name: <p>The name of the fleet.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.stop_fleet_request.StopFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.stop_fleet_result.StopFleetResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.stop_fleet

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.stop_fleet.stop_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.stop_fleet_request.StopFleetRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_image_builder(
        self,
        name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.stop_image_builder_result.StopImageBuilderResult":
        """<p>Stops the specified image builder.</p>

        Args:
            name: <p>The name of the image builder.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.stop_image_builder_request.StopImageBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.stop_image_builder_result.StopImageBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.stop_image_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.stop_image_builder.stop_image_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.stop_image_builder_request.StopImageBuilderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_appstream.types.arn.Arn",
        tags: "aws_sdk_appstream.types.tags.Tags",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or overwrites one or more tags for the specified WorkSpaces Applications resource. You can tag WorkSpaces Applications image builders, images, fleets, and stacks.</p> <p>Each tag consists of a key and an optional value. If a resource already has a tag with the same key, this operation updates its value.</p> <p>To list the current tags for your resources, use <a>ListTagsForResource</a>. To disassociate tags from your resources, use <a>UntagResource</a>.</p> <p>For more information about tags, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html\">Tagging Your Resources</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags to associate. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=. </p> <p>If you do not specify a value, the value is set to an empty string.</p> <p>Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters: </p> <p>_ . : / = + \ - @</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.tag_resource

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_appstream.types.arn.Arn",
        tag_keys: "aws_sdk_appstream.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.untag_resource_response.UntagResourceResponse":
        """<p>Disassociates one or more specified tags from the specified WorkSpaces Applications resource.</p> <p>To list the current tags for your resources, use <a>ListTagsForResource</a>.</p> <p>For more information about tags, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html\">Tagging Your Resources</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys for the tags to disassociate.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.untag_resource

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_app_block_builder(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
        display_name: Optional[
            "aws_sdk_appstream.types.display_name.DisplayName"
        ] = None,
        platform: Optional["aws_sdk_appstream.types.platform_type.PlatformType"] = None,
        instance_type: Optional["aws_sdk_appstream.types.string.String"] = None,
        vpc_config: Optional["aws_sdk_appstream.types.vpc_config.VpcConfig"] = None,
        enable_default_internet_access: Optional[
            "aws_sdk_appstream.types.boolean_object.BooleanObject"
        ] = None,
        iam_role_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        access_endpoints: Optional[
            "aws_sdk_appstream.types.access_endpoint_list.AccessEndpointList"
        ] = None,
        attributes_to_delete: Optional[
            "aws_sdk_appstream.types.app_block_builder_attributes.AppBlockBuilderAttributes"
        ] = None,
        disable_imdsv1: Optional[
            "aws_sdk_appstream.types.boolean_object.BooleanObject"
        ] = None,
    ) -> "aws_sdk_appstream.types.update_app_block_builder_result.UpdateAppBlockBuilderResult":
        """<p>Updates an app block builder.</p> <p>If the app block builder is in the <code>STARTING</code> or <code>STOPPING</code> state, you can't update it. If the app block builder is in the <code>RUNNING</code> state, you can only update the DisplayName and Description. If the app block builder is in the <code>STOPPED</code> state, you can update any attribute except the Name.</p>

        Args:
            name: <p>The unique name for the app block builder.</p>
            description: <p>The description of the app block builder.</p>
            display_name: <p>The display name of the app block builder.</p>
            platform: <p>The platform of the app block builder.</p> <p> <code>WINDOWS_SERVER_2019</code> is the only valid value.</p>
            instance_type: <p>The instance type to use when launching the app block builder. The following instance types are available:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.standard.xlarge</p> </li> <li> <p>stream.standard.2xlarge</p> </li> </ul>
            vpc_config: <p>The VPC configuration for the app block builder.</p> <p>App block builders require that you specify at least two subnets in different availability zones.</p>
            enable_default_internet_access: <p>Enables or disables default internet access for the app block builder.</p>
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to apply to the app block builder. To assume a role, the app block builder calls the AWS Security Token Service (STS) <code>AssumeRole</code> API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the <b>appstream_machine_role</b> credential profile on the instance.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html\">Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>
            access_endpoints: <p>The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the app block builder only through the specified endpoints.</p>
            attributes_to_delete: <p>The attributes to delete from the app block builder.</p>
            disable_imdsv1: <p>Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.update_app_block_builder_request.UpdateAppBlockBuilderRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.update_app_block_builder_result.UpdateAppBlockBuilderResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.update_app_block_builder

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.update_app_block_builder.update_app_block_builder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.update_app_block_builder_request.UpdateAppBlockBuilderRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if display_name is not None:
            input["display_name"] = display_name
        if platform is not None:
            input["platform"] = platform
        if instance_type is not None:
            input["instance_type"] = instance_type
        if vpc_config is not None:
            input["vpc_config"] = vpc_config
        if enable_default_internet_access is not None:
            input["enable_default_internet_access"] = enable_default_internet_access
        if iam_role_arn is not None:
            input["iam_role_arn"] = iam_role_arn
        if access_endpoints is not None:
            input["access_endpoints"] = access_endpoints
        if attributes_to_delete is not None:
            input["attributes_to_delete"] = attributes_to_delete
        if disable_imdsv1 is not None:
            input["disable_imdsv1"] = disable_imdsv1

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_application(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        display_name: Optional[
            "aws_sdk_appstream.types.display_name.DisplayName"
        ] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
        icon_s3_location: Optional[
            "aws_sdk_appstream.types.s3_location.S3Location"
        ] = None,
        launch_path: Optional["aws_sdk_appstream.types.string.String"] = None,
        working_directory: Optional["aws_sdk_appstream.types.string.String"] = None,
        launch_parameters: Optional["aws_sdk_appstream.types.string.String"] = None,
        app_block_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        attributes_to_delete: Optional[
            "aws_sdk_appstream.types.application_attributes.ApplicationAttributes"
        ] = None,
    ) -> "aws_sdk_appstream.types.update_application_result.UpdateApplicationResult":
        """<p>Updates the specified application.</p>

        Args:
            name: <p>The name of the application. This name is visible to users when display name is not specified.</p>
            display_name: <p>The display name of the application. This name is visible to users in the application catalog.</p>
            description: <p>The description of the application.</p>
            icon_s3_location: <p>The icon S3 location of the application.</p>
            launch_path: <p>The launch path of the application.</p>
            working_directory: <p>The working directory of the application.</p>
            launch_parameters: <p>The launch parameters of the application.</p>
            app_block_arn: <p>The ARN of the app block.</p>
            attributes_to_delete: <p>The attributes to delete for an application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.update_application_result.UpdateApplicationResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.update_application

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.update_application_request.UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if display_name is not None:
            input["display_name"] = display_name
        if description is not None:
            input["description"] = description
        if icon_s3_location is not None:
            input["icon_s3_location"] = icon_s3_location
        if launch_path is not None:
            input["launch_path"] = launch_path
        if working_directory is not None:
            input["working_directory"] = working_directory
        if launch_parameters is not None:
            input["launch_parameters"] = launch_parameters
        if app_block_arn is not None:
            input["app_block_arn"] = app_block_arn
        if attributes_to_delete is not None:
            input["attributes_to_delete"] = attributes_to_delete

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_directory_config(
        self,
        directory_name: "aws_sdk_appstream.types.directory_name.DirectoryName",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        organizational_unit_distinguished_names: Optional[
            "aws_sdk_appstream.types.organizational_unit_distinguished_names_list.OrganizationalUnitDistinguishedNamesList"
        ] = None,
        service_account_credentials: Optional[
            "aws_sdk_appstream.types.service_account_credentials.ServiceAccountCredentials"
        ] = None,
        certificate_based_auth_properties: Optional[
            "aws_sdk_appstream.types.certificate_based_auth_properties.CertificateBasedAuthProperties"
        ] = None,
    ) -> "aws_sdk_appstream.types.update_directory_config_result.UpdateDirectoryConfigResult":
        """<p>Updates the specified Directory Config object in WorkSpaces Applications. This object includes the configuration information required to join fleets and image builders to Microsoft Active Directory domains.</p>

        Args:
            directory_name: <p>The name of the Directory Config object.</p>
            organizational_unit_distinguished_names: <p>The distinguished names of the organizational units for computer accounts.</p>
            service_account_credentials: <p>The credentials for the service account used by the fleet or image builder to connect to the directory.</p>
            certificate_based_auth_properties: <p>The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory domain-joined streaming instances. Fallback is turned on by default when certificate-based authentication is <b>Enabled</b> . Fallback allows users to log in using their AD domain password if certificate-based authentication is unsuccessful, or to unlock a desktop lock screen. <b>Enabled_no_directory_login_fallback</b> enables certificate-based authentication, but does not allow users to log in using their AD domain password. Users will be disconnected to re-authenticate using certificates.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.update_directory_config_request.UpdateDirectoryConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.update_directory_config_result.UpdateDirectoryConfigResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.update_directory_config

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.update_directory_config.update_directory_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.update_directory_config_request.UpdateDirectoryConfigRequest = {}  # type: ignore[typeddict-item]
        input["directory_name"] = directory_name
        if organizational_unit_distinguished_names is not None:
            input["organizational_unit_distinguished_names"] = (
                organizational_unit_distinguished_names
            )
        if service_account_credentials is not None:
            input["service_account_credentials"] = service_account_credentials
        if certificate_based_auth_properties is not None:
            input["certificate_based_auth_properties"] = (
                certificate_based_auth_properties
            )

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_entitlement(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        stack_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
        app_visibility: Optional[
            "aws_sdk_appstream.types.app_visibility.AppVisibility"
        ] = None,
        attributes: Optional[
            "aws_sdk_appstream.types.entitlement_attribute_list.EntitlementAttributeList"
        ] = None,
    ) -> "aws_sdk_appstream.types.update_entitlement_result.UpdateEntitlementResult":
        """<p>Updates the specified entitlement.</p>

        Args:
            name: <p>The name of the entitlement.</p>
            stack_name: <p>The name of the stack with which the entitlement is associated.</p>
            description: <p>The description of the entitlement.</p>
            app_visibility: <p>Specifies whether all or only selected apps are entitled.</p>
            attributes: <p>The attributes of the entitlement.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.update_entitlement_request.UpdateEntitlementRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.update_entitlement_result.UpdateEntitlementResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.update_entitlement

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.update_entitlement.update_entitlement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.update_entitlement_request.UpdateEntitlementRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["stack_name"] = stack_name
        if description is not None:
            input["description"] = description
        if app_visibility is not None:
            input["app_visibility"] = app_visibility
        if attributes is not None:
            input["attributes"] = attributes

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_fleet(
        self,
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        image_name: Optional["aws_sdk_appstream.types.string.String"] = None,
        image_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        name: Optional["aws_sdk_appstream.types.name.Name"] = None,
        instance_type: Optional["aws_sdk_appstream.types.string.String"] = None,
        compute_capacity: Optional[
            "aws_sdk_appstream.types.compute_capacity.ComputeCapacity"
        ] = None,
        vpc_config: Optional["aws_sdk_appstream.types.vpc_config.VpcConfig"] = None,
        max_user_duration_in_seconds: Optional[
            "aws_sdk_appstream.types.integer.Integer"
        ] = None,
        disconnect_timeout_in_seconds: Optional[
            "aws_sdk_appstream.types.integer.Integer"
        ] = None,
        delete_vpc_config: Optional["aws_sdk_appstream.types.boolean.Boolean"] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
        display_name: Optional[
            "aws_sdk_appstream.types.display_name.DisplayName"
        ] = None,
        enable_default_internet_access: Optional[
            "aws_sdk_appstream.types.boolean_object.BooleanObject"
        ] = None,
        domain_join_info: Optional[
            "aws_sdk_appstream.types.domain_join_info.DomainJoinInfo"
        ] = None,
        idle_disconnect_timeout_in_seconds: Optional[
            "aws_sdk_appstream.types.integer.Integer"
        ] = None,
        attributes_to_delete: Optional[
            "aws_sdk_appstream.types.fleet_attributes.FleetAttributes"
        ] = None,
        iam_role_arn: Optional["aws_sdk_appstream.types.arn.Arn"] = None,
        stream_view: Optional["aws_sdk_appstream.types.stream_view.StreamView"] = None,
        platform: Optional["aws_sdk_appstream.types.platform_type.PlatformType"] = None,
        max_concurrent_sessions: Optional[
            "aws_sdk_appstream.types.integer.Integer"
        ] = None,
        usb_device_filter_strings: Optional[
            "aws_sdk_appstream.types.usb_device_filter_strings.UsbDeviceFilterStrings"
        ] = None,
        session_script_s3_location: Optional[
            "aws_sdk_appstream.types.s3_location.S3Location"
        ] = None,
        max_sessions_per_instance: Optional[
            "aws_sdk_appstream.types.integer.Integer"
        ] = None,
        root_volume_config: Optional[
            "aws_sdk_appstream.types.volume_config.VolumeConfig"
        ] = None,
        disable_imdsv1: Optional[
            "aws_sdk_appstream.types.boolean_object.BooleanObject"
        ] = None,
    ) -> "aws_sdk_appstream.types.update_fleet_result.UpdateFleetResult":
        """<p>Updates the specified fleet.</p> <p>If the fleet is in the <code>STOPPED</code> state, you can update any attribute except the fleet name.</p> <p>If the fleet is in the <code>RUNNING</code> state, you can update the following based on the fleet type:</p> <ul> <li> <p>Always-On and On-Demand fleet types</p> <p>You can update the <code>DisplayName</code>, <code>ComputeCapacity</code>, <code>ImageARN</code>, <code>ImageName</code>, <code>IdleDisconnectTimeoutInSeconds</code>, and <code>DisconnectTimeoutInSeconds</code> attributes.</p> </li> <li> <p>Elastic fleet type</p> <p>You can update the <code>DisplayName</code>, <code>IdleDisconnectTimeoutInSeconds</code>, <code>DisconnectTimeoutInSeconds</code>, <code>MaxConcurrentSessions</code>, <code>SessionScriptS3Location</code> and <code>UsbDeviceFilterStrings</code> attributes.</p> </li> </ul> <p>If the fleet is in the <code>STARTING</code> or <code>STOPPED</code> state, you can't update it.</p>

        Args:
            image_name: <p>The name of the image used to create the fleet.</p>
            image_arn: <p>The ARN of the public, private, or shared image to use.</p>
            name: <p>A unique name for the fleet.</p>
            instance_type: <p>The instance type to use when launching fleet instances. The following instance types are available:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.standard.xlarge</p> </li> <li> <p>stream.standard.2xlarge</p> </li> <li> <p>stream.compute.large</p> </li> <li> <p>stream.compute.xlarge</p> </li> <li> <p>stream.compute.2xlarge</p> </li> <li> <p>stream.compute.4xlarge</p> </li> <li> <p>stream.compute.8xlarge</p> </li> <li> <p>stream.memory.large</p> </li> <li> <p>stream.memory.xlarge</p> </li> <li> <p>stream.memory.2xlarge</p> </li> <li> <p>stream.memory.4xlarge</p> </li> <li> <p>stream.memory.8xlarge</p> </li> <li> <p>stream.memory.z1d.large</p> </li> <li> <p>stream.memory.z1d.xlarge</p> </li> <li> <p>stream.memory.z1d.2xlarge</p> </li> <li> <p>stream.memory.z1d.3xlarge</p> </li> <li> <p>stream.memory.z1d.6xlarge</p> </li> <li> <p>stream.memory.z1d.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.xlarge</p> </li> <li> <p>stream.graphics.g4dn.2xlarge</p> </li> <li> <p>stream.graphics.g4dn.4xlarge</p> </li> <li> <p>stream.graphics.g4dn.8xlarge</p> </li> <li> <p>stream.graphics.g4dn.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.16xlarge</p> </li> <li> <p>stream.graphics.g5.xlarge</p> </li> <li> <p>stream.graphics.g5.2xlarge</p> </li> <li> <p>stream.graphics.g5.4xlarge</p> </li> <li> <p>stream.graphics.g5.8xlarge</p> </li> <li> <p>stream.graphics.g5.16xlarge</p> </li> <li> <p>stream.graphics.g5.12xlarge</p> </li> <li> <p>stream.graphics.g5.24xlarge</p> </li> <li> <p>stream.graphics.g6.xlarge</p> </li> <li> <p>stream.graphics.g6.2xlarge</p> </li> <li> <p>stream.graphics.g6.4xlarge</p> </li> <li> <p>stream.graphics.g6.8xlarge</p> </li> <li> <p>stream.graphics.g6.16xlarge</p> </li> <li> <p>stream.graphics.g6.12xlarge</p> </li> <li> <p>stream.graphics.g6.24xlarge</p> </li> <li> <p>stream.graphics.gr6.4xlarge</p> </li> <li> <p>stream.graphics.gr6.8xlarge</p> </li> <li> <p>stream.graphics.g6f.large</p> </li> <li> <p>stream.graphics.g6f.xlarge</p> </li> <li> <p>stream.graphics.g6f.2xlarge</p> </li> <li> <p>stream.graphics.g6f.4xlarge</p> </li> <li> <p>stream.graphics.gr6f.4xlarge</p> </li> </ul> <p>The following instance types are available for Elastic fleets:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.standard.xlarge</p> </li> <li> <p>stream.standard.2xlarge</p> </li> </ul>
            compute_capacity: <p>The desired capacity for the fleet. This is not allowed for Elastic fleets.</p>
            vpc_config: <p>The VPC configuration for the fleet. This is required for Elastic fleets, but not required for other fleet types. Elastic fleets require that you specify at least two subnets in different availability zones. </p>
            max_user_duration_in_seconds: <p>The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.</p> <p>Specify a value between 600 and 432000.</p>
            disconnect_timeout_in_seconds: <p>The amount of time that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance. </p> <p>Specify a value between 60 and 36000.</p>
            delete_vpc_config: <p>Deletes the VPC association for the specified fleet.</p>
            description: <p>The description to display.</p>
            display_name: <p>The fleet name to display.</p>
            enable_default_internet_access: <p>Enables or disables default internet access for the fleet.</p>
            domain_join_info: <p>The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain. </p>
            idle_disconnect_timeout_in_seconds: <p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the <code>DisconnectTimeoutInSeconds</code> time interval begins. Users are notified before they are disconnected due to inactivity. If users try to reconnect to the streaming session before the time interval specified in <code>DisconnectTimeoutInSeconds</code> elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in <code>IdleDisconnectTimeoutInSeconds</code> elapses, they are disconnected. </p> <p>To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 36000. The default value is 0.</p> <note> <p>If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity. </p> </note>
            attributes_to_delete: <p>The fleet attributes to delete.</p>
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to apply to the fleet. To assume a role, a fleet instance calls the AWS Security Token Service (STS) <code>AssumeRole</code> API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the <b>appstream_machine_role</b> credential profile on the instance.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html\">Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>
            stream_view: <p>The WorkSpaces Applications view that is displayed to your users when they stream from the fleet. When <code>APP</code> is specified, only the windows of applications opened by users display. When <code>DESKTOP</code> is specified, the standard desktop that is provided by the operating system displays.</p> <p>The default value is <code>APP</code>.</p>
            platform: <p>The platform of the fleet. WINDOWS_SERVER_2019, AMAZON_LINUX2 and UBUNTU_PRO_2404 are supported for Elastic fleets. </p>
            max_concurrent_sessions: <p>The maximum number of concurrent sessions for a fleet.</p>
            usb_device_filter_strings: <p>The USB device filter strings that specify which USB devices a user can redirect to the fleet streaming session, when using the Windows native client. This is allowed but not required for Elastic fleets.</p>
            session_script_s3_location: <p>The S3 location of the session scripts configuration zip file. This only applies to Elastic fleets. </p>
            max_sessions_per_instance: <p>The maximum number of user sessions on an instance. This only applies to multi-session fleets.</p>
            root_volume_config: <p>The updated configuration for the root volume of fleet instances. Note that volume size cannot be decreased below the image volume size.</p>
            disable_imdsv1: <p>Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.</p> <note> <p>Before disabling IMDSv1, ensure your WorkSpaces Applications images are running the agent version or managed image update released on or after January 16, 2024 to support IMDSv2 enforcement.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.update_fleet_request.UpdateFleetRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.update_fleet_result.UpdateFleetResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.update_fleet

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.update_fleet.update_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.update_fleet_request.UpdateFleetRequest = {}  # type: ignore[typeddict-item]
        if image_name is not None:
            input["image_name"] = image_name
        if image_arn is not None:
            input["image_arn"] = image_arn
        if name is not None:
            input["name"] = name
        if instance_type is not None:
            input["instance_type"] = instance_type
        if compute_capacity is not None:
            input["compute_capacity"] = compute_capacity
        if vpc_config is not None:
            input["vpc_config"] = vpc_config
        if max_user_duration_in_seconds is not None:
            input["max_user_duration_in_seconds"] = max_user_duration_in_seconds
        if disconnect_timeout_in_seconds is not None:
            input["disconnect_timeout_in_seconds"] = disconnect_timeout_in_seconds
        if delete_vpc_config is not None:
            input["delete_vpc_config"] = delete_vpc_config
        if description is not None:
            input["description"] = description
        if display_name is not None:
            input["display_name"] = display_name
        if enable_default_internet_access is not None:
            input["enable_default_internet_access"] = enable_default_internet_access
        if domain_join_info is not None:
            input["domain_join_info"] = domain_join_info
        if idle_disconnect_timeout_in_seconds is not None:
            input["idle_disconnect_timeout_in_seconds"] = (
                idle_disconnect_timeout_in_seconds
            )
        if attributes_to_delete is not None:
            input["attributes_to_delete"] = attributes_to_delete
        if iam_role_arn is not None:
            input["iam_role_arn"] = iam_role_arn
        if stream_view is not None:
            input["stream_view"] = stream_view
        if platform is not None:
            input["platform"] = platform
        if max_concurrent_sessions is not None:
            input["max_concurrent_sessions"] = max_concurrent_sessions
        if usb_device_filter_strings is not None:
            input["usb_device_filter_strings"] = usb_device_filter_strings
        if session_script_s3_location is not None:
            input["session_script_s3_location"] = session_script_s3_location
        if max_sessions_per_instance is not None:
            input["max_sessions_per_instance"] = max_sessions_per_instance
        if root_volume_config is not None:
            input["root_volume_config"] = root_volume_config
        if disable_imdsv1 is not None:
            input["disable_imdsv1"] = disable_imdsv1

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_image_permissions(
        self,
        name: "aws_sdk_appstream.types.name.Name",
        shared_account_id: "aws_sdk_appstream.types.aws_account_id.AwsAccountId",
        image_permissions: "aws_sdk_appstream.types.image_permissions.ImagePermissions",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
    ) -> "aws_sdk_appstream.types.update_image_permissions_result.UpdateImagePermissionsResult":
        """<p>Adds or updates permissions for the specified private image. </p>

        Args:
            name: <p>The name of the private image.</p>
            shared_account_id: <p>The 12-digit identifier of the AWS account for which you want add or update image permissions.</p>
            image_permissions: <p>The permissions for the image.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.update_image_permissions_request.UpdateImagePermissionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.update_image_permissions_result.UpdateImagePermissionsResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.update_image_permissions

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.update_image_permissions.update_image_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.update_image_permissions_request.UpdateImagePermissionsRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["shared_account_id"] = shared_account_id
        input["image_permissions"] = image_permissions

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_stack(
        self,
        name: "aws_sdk_appstream.types.string.String",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        display_name: Optional[
            "aws_sdk_appstream.types.display_name.DisplayName"
        ] = None,
        description: Optional["aws_sdk_appstream.types.description.Description"] = None,
        storage_connectors: Optional[
            "aws_sdk_appstream.types.storage_connector_list.StorageConnectorList"
        ] = None,
        delete_storage_connectors: Optional[
            "aws_sdk_appstream.types.boolean.Boolean"
        ] = None,
        redirect_url: Optional[
            "aws_sdk_appstream.types.redirect_url.RedirectURL"
        ] = None,
        feedback_url: Optional[
            "aws_sdk_appstream.types.feedback_url.FeedbackURL"
        ] = None,
        attributes_to_delete: Optional[
            "aws_sdk_appstream.types.stack_attributes.StackAttributes"
        ] = None,
        user_settings: Optional[
            "aws_sdk_appstream.types.user_setting_list.UserSettingList"
        ] = None,
        application_settings: Optional[
            "aws_sdk_appstream.types.application_settings.ApplicationSettings"
        ] = None,
        access_endpoints: Optional[
            "aws_sdk_appstream.types.access_endpoint_list.AccessEndpointList"
        ] = None,
        embed_host_domains: Optional[
            "aws_sdk_appstream.types.embed_host_domains.EmbedHostDomains"
        ] = None,
        streaming_experience_settings: Optional[
            "aws_sdk_appstream.types.streaming_experience_settings.StreamingExperienceSettings"
        ] = None,
        content_redirection: Optional[
            "aws_sdk_appstream.types.content_redirection.ContentRedirection"
        ] = None,
        agent_access_config: Optional[
            "aws_sdk_appstream.types.agent_access_config_for_update.AgentAccessConfigForUpdate"
        ] = None,
    ) -> "aws_sdk_appstream.types.update_stack_result.UpdateStackResult":
        """<p>Updates the specified fields for the specified stack.</p>

        Args:
            display_name: <p>The stack name to display.</p>
            description: <p>The description to display.</p>
            name: <p>The name of the stack.</p>
            storage_connectors: <p>The storage connectors to enable.</p>
            delete_storage_connectors: <p>Deletes the storage connectors currently enabled for the stack.</p>
            redirect_url: <p>The URL that users are redirected to after their streaming session ends.</p>
            feedback_url: <p>The URL that users are redirected to after they choose the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.</p>
            attributes_to_delete: <p>The stack attributes to delete.</p>
            user_settings: <p>The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.</p>
            application_settings: <p>The persistent application settings for users of a stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.</p>
            access_endpoints: <p>The list of interface VPC endpoint (interface endpoint) objects. Users of the stack can connect to WorkSpaces Applications only through the specified endpoints.</p>
            embed_host_domains: <p>The domains where WorkSpaces Applications streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded WorkSpaces Applications streaming sessions. </p>
            streaming_experience_settings: <p>The streaming protocol you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.</p>
            agent_access_config: <p>The configuration for agent access on the stack. Specify this to update agent access settings. To remove agent access, use AttributesToDelete with the AGENT_ACCESS_CONFIG value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.update_stack_request.UpdateStackRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.update_stack_result.UpdateStackResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.update_stack

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.update_stack.update_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.update_stack_request.UpdateStackRequest = {}  # type: ignore[typeddict-item]
        if display_name is not None:
            input["display_name"] = display_name
        if description is not None:
            input["description"] = description
        input["name"] = name
        if storage_connectors is not None:
            input["storage_connectors"] = storage_connectors
        if delete_storage_connectors is not None:
            input["delete_storage_connectors"] = delete_storage_connectors
        if redirect_url is not None:
            input["redirect_url"] = redirect_url
        if feedback_url is not None:
            input["feedback_url"] = feedback_url
        if attributes_to_delete is not None:
            input["attributes_to_delete"] = attributes_to_delete
        if user_settings is not None:
            input["user_settings"] = user_settings
        if application_settings is not None:
            input["application_settings"] = application_settings
        if access_endpoints is not None:
            input["access_endpoints"] = access_endpoints
        if embed_host_domains is not None:
            input["embed_host_domains"] = embed_host_domains
        if streaming_experience_settings is not None:
            input["streaming_experience_settings"] = streaming_experience_settings
        if content_redirection is not None:
            input["content_redirection"] = content_redirection
        if agent_access_config is not None:
            input["agent_access_config"] = agent_access_config

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_theme_for_stack(
        self,
        stack_name: "aws_sdk_appstream.types.name.Name",
        *,
        config_overrides: Optional[AppStreamClientConfig] = None,
        footer_links: Optional[
            "aws_sdk_appstream.types.theme_footer_links.ThemeFooterLinks"
        ] = None,
        title_text: Optional[
            "aws_sdk_appstream.types.theme_title_text.ThemeTitleText"
        ] = None,
        theme_styling: Optional[
            "aws_sdk_appstream.types.theme_styling.ThemeStyling"
        ] = None,
        organization_logo_s3_location: Optional[
            "aws_sdk_appstream.types.s3_location.S3Location"
        ] = None,
        favicon_s3_location: Optional[
            "aws_sdk_appstream.types.s3_location.S3Location"
        ] = None,
        state: Optional["aws_sdk_appstream.types.theme_state.ThemeState"] = None,
        attributes_to_delete: Optional[
            "aws_sdk_appstream.types.theme_attributes.ThemeAttributes"
        ] = None,
    ) -> "aws_sdk_appstream.types.update_theme_for_stack_result.UpdateThemeForStackResult":
        """<p>Updates custom branding that customizes the appearance of the streaming application catalog page.</p>

        Args:
            stack_name: <p>The name of the stack for the theme.</p>
            footer_links: <p>The links that are displayed in the footer of the streaming application catalog page. These links are helpful resources for users, such as the organization's IT support and product marketing sites.</p>
            title_text: <p>The title that is displayed at the top of the browser tab during users' application streaming sessions.</p>
            theme_styling: <p>The color theme that is applied to website links, text, and buttons. These colors are also applied as accents in the background for the streaming application catalog page.</p>
            organization_logo_s3_location: <p>The organization logo that appears on the streaming application catalog page.</p>
            favicon_s3_location: <p>The S3 location of the favicon. The favicon enables users to recognize their application streaming site in a browser full of tabs or bookmarks. It is displayed at the top of the browser tab for the application streaming site during users' streaming sessions.</p>
            state: <p>Specifies whether custom branding should be applied to catalog page or not.</p>
            attributes_to_delete: <p>The attributes to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_appstream.types.update_theme_for_stack_request.UpdateThemeForStackRequest]",
        ) -> OperationResponse[
            "aws_sdk_appstream.types.update_theme_for_stack_result.UpdateThemeForStackResult"
        ]:
            import aws_sdk_appstream._operations.photon_admin_proxy_service.update_theme_for_stack

            output, http_response = (
                aws_sdk_appstream._operations.photon_admin_proxy_service.update_theme_for_stack.update_theme_for_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appstream.types.update_theme_for_stack_request.UpdateThemeForStackRequest = {}  # type: ignore[typeddict-item]
        input["stack_name"] = stack_name
        if footer_links is not None:
            input["footer_links"] = footer_links
        if title_text is not None:
            input["title_text"] = title_text
        if theme_styling is not None:
            input["theme_styling"] = theme_styling
        if organization_logo_s3_location is not None:
            input["organization_logo_s3_location"] = organization_logo_s3_location
        if favicon_s3_location is not None:
            input["favicon_s3_location"] = favicon_s3_location
        if state is not None:
            input["state"] = state
        if attributes_to_delete is not None:
            input["attributes_to_delete"] = attributes_to_delete

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
