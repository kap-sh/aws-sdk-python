"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ObservabilityAdmin``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_observabilityadmin._auth._signers
import aws_sdk_observabilityadmin._auth._sigv4
from aws_sdk_observabilityadmin._auth._identity import Credentials
from aws_sdk_observabilityadmin._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_observabilityadmin._auth._zapros_handler import AuthMiddleware
from aws_sdk_observabilityadmin._pagination import resolve_path as _resolve_path
from aws_sdk_observabilityadmin._resources.observability_admin.telemetry_pipeline_resource import (
    TelemetryPipelineResource,
)
from aws_sdk_observabilityadmin._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.account_identifiers
    import aws_sdk_observabilityadmin.types.all_regions
    import aws_sdk_observabilityadmin.types.centralization_rule
    import aws_sdk_observabilityadmin.types.centralization_rule_summary
    import aws_sdk_observabilityadmin.types.create_centralization_rule_for_organization_input
    import aws_sdk_observabilityadmin.types.create_centralization_rule_for_organization_output
    import aws_sdk_observabilityadmin.types.create_s3_table_integration_input
    import aws_sdk_observabilityadmin.types.create_s3_table_integration_output
    import aws_sdk_observabilityadmin.types.create_telemetry_rule_for_organization_input
    import aws_sdk_observabilityadmin.types.create_telemetry_rule_for_organization_output
    import aws_sdk_observabilityadmin.types.create_telemetry_rule_input
    import aws_sdk_observabilityadmin.types.create_telemetry_rule_output
    import aws_sdk_observabilityadmin.types.delete_centralization_rule_for_organization_input
    import aws_sdk_observabilityadmin.types.delete_s3_table_integration_input
    import aws_sdk_observabilityadmin.types.delete_telemetry_rule_for_organization_input
    import aws_sdk_observabilityadmin.types.delete_telemetry_rule_input
    import aws_sdk_observabilityadmin.types.encryption
    import aws_sdk_observabilityadmin.types.get_centralization_rule_for_organization_input
    import aws_sdk_observabilityadmin.types.get_centralization_rule_for_organization_output
    import aws_sdk_observabilityadmin.types.get_s3_table_integration_input
    import aws_sdk_observabilityadmin.types.get_s3_table_integration_output
    import aws_sdk_observabilityadmin.types.get_telemetry_enrichment_status_output
    import aws_sdk_observabilityadmin.types.get_telemetry_evaluation_status_for_organization_output
    import aws_sdk_observabilityadmin.types.get_telemetry_evaluation_status_output
    import aws_sdk_observabilityadmin.types.get_telemetry_rule_for_organization_input
    import aws_sdk_observabilityadmin.types.get_telemetry_rule_for_organization_output
    import aws_sdk_observabilityadmin.types.get_telemetry_rule_input
    import aws_sdk_observabilityadmin.types.get_telemetry_rule_output
    import aws_sdk_observabilityadmin.types.integration_summary
    import aws_sdk_observabilityadmin.types.list_centralization_rules_for_organization_input
    import aws_sdk_observabilityadmin.types.list_centralization_rules_for_organization_max_results
    import aws_sdk_observabilityadmin.types.list_centralization_rules_for_organization_output
    import aws_sdk_observabilityadmin.types.list_resource_telemetry_for_organization_input
    import aws_sdk_observabilityadmin.types.list_resource_telemetry_for_organization_max_results
    import aws_sdk_observabilityadmin.types.list_resource_telemetry_for_organization_output
    import aws_sdk_observabilityadmin.types.list_resource_telemetry_input
    import aws_sdk_observabilityadmin.types.list_resource_telemetry_max_results
    import aws_sdk_observabilityadmin.types.list_resource_telemetry_output
    import aws_sdk_observabilityadmin.types.list_s3_table_integrations_input
    import aws_sdk_observabilityadmin.types.list_s3_table_integrations_max_results
    import aws_sdk_observabilityadmin.types.list_s3_table_integrations_output
    import aws_sdk_observabilityadmin.types.list_tags_for_resource_input
    import aws_sdk_observabilityadmin.types.list_tags_for_resource_output
    import aws_sdk_observabilityadmin.types.list_telemetry_rules_for_organization_input
    import aws_sdk_observabilityadmin.types.list_telemetry_rules_for_organization_max_results
    import aws_sdk_observabilityadmin.types.list_telemetry_rules_for_organization_output
    import aws_sdk_observabilityadmin.types.list_telemetry_rules_input
    import aws_sdk_observabilityadmin.types.list_telemetry_rules_max_results
    import aws_sdk_observabilityadmin.types.list_telemetry_rules_output
    import aws_sdk_observabilityadmin.types.next_token
    import aws_sdk_observabilityadmin.types.organization_unit_identifiers
    import aws_sdk_observabilityadmin.types.records
    import aws_sdk_observabilityadmin.types.regions
    import aws_sdk_observabilityadmin.types.resource_arn
    import aws_sdk_observabilityadmin.types.resource_identifier_prefix
    import aws_sdk_observabilityadmin.types.resource_types
    import aws_sdk_observabilityadmin.types.rule_identifier
    import aws_sdk_observabilityadmin.types.rule_name
    import aws_sdk_observabilityadmin.types.start_telemetry_enrichment_output
    import aws_sdk_observabilityadmin.types.start_telemetry_evaluation_for_organization_input
    import aws_sdk_observabilityadmin.types.start_telemetry_evaluation_input
    import aws_sdk_observabilityadmin.types.stop_telemetry_enrichment_output
    import aws_sdk_observabilityadmin.types.tag_key_list
    import aws_sdk_observabilityadmin.types.tag_map_input
    import aws_sdk_observabilityadmin.types.tag_resource_input
    import aws_sdk_observabilityadmin.types.telemetry_configuration
    import aws_sdk_observabilityadmin.types.telemetry_configuration_state
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration
    import aws_sdk_observabilityadmin.types.telemetry_rule
    import aws_sdk_observabilityadmin.types.telemetry_rule_summary
    import aws_sdk_observabilityadmin.types.test_telemetry_pipeline_input
    import aws_sdk_observabilityadmin.types.test_telemetry_pipeline_output
    import aws_sdk_observabilityadmin.types.untag_resource_input
    import aws_sdk_observabilityadmin.types.update_centralization_rule_for_organization_input
    import aws_sdk_observabilityadmin.types.update_centralization_rule_for_organization_output
    import aws_sdk_observabilityadmin.types.update_telemetry_rule_for_organization_input
    import aws_sdk_observabilityadmin.types.update_telemetry_rule_for_organization_output
    import aws_sdk_observabilityadmin.types.update_telemetry_rule_input
    import aws_sdk_observabilityadmin.types.update_telemetry_rule_output
    import aws_sdk_observabilityadmin.types.validate_telemetry_pipeline_configuration_input
    import aws_sdk_observabilityadmin.types.validate_telemetry_pipeline_configuration_output


class ObservabilityAdminClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class ObservabilityAdminClient:
    """A client for the ``ObservabilityAdmin`` service.

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
        self._config = ObservabilityAdminClientConfig(
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

        # resources
        self.telemetry_pipeline_resource = TelemetryPipelineResource(self)

    def operation_options(
        self, config_overrides: Optional[ObservabilityAdminClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ObservabilityAdminClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def create_centralization_rule_for_organization(
        self,
        rule_name: "aws_sdk_observabilityadmin.types.rule_name.RuleName",
        rule: "aws_sdk_observabilityadmin.types.centralization_rule.CentralizationRule",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        tags: Optional[
            "aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "aws_sdk_observabilityadmin.types.create_centralization_rule_for_organization_output.CreateCentralizationRuleForOrganizationOutput":
        """<p>Creates a centralization rule that applies across an Amazon Web Services Organization. This operation can only be called by the organization's management account or a delegated administrator account.</p>

        Args:
            rule_name: <p>A unique name for the organization-wide centralization rule being created.</p>
            rule: <p>The configuration details for the organization-wide centralization rule, including the source configuration and the destination configuration to centralize telemetry data across the organization.</p>
            tags: <p>The key-value pairs to associate with the organization telemetry rule resource for categorization and management purposes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.create_centralization_rule_for_organization_input.CreateCentralizationRuleForOrganizationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.create_centralization_rule_for_organization_output.CreateCentralizationRuleForOrganizationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.create_centralization_rule_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.create_centralization_rule_for_organization.create_centralization_rule_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.create_centralization_rule_for_organization_input.CreateCentralizationRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
        input_["rule_name"] = rule_name
        input_["rule"] = rule
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_s3_table_integration(
        self,
        encryption: "aws_sdk_observabilityadmin.types.encryption.Encryption",
        role_arn: "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        tags: Optional[
            "aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "aws_sdk_observabilityadmin.types.create_s3_table_integration_output.CreateS3TableIntegrationOutput":
        """<p>Creates an integration between CloudWatch and S3 Tables for analytics. This integration enables querying CloudWatch telemetry data using analytics engines like Amazon Athena, Amazon Redshift, and Apache Spark.</p>

        Args:
            encryption: <p>The encryption configuration for the S3 Table integration, including the encryption algorithm and KMS key settings.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants permissions for the S3 Table integration to access necessary resources.</p>
            tags: <p>The key-value pairs to associate with the S3 Table integration resource for categorization and management purposes.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.create_s3_table_integration_input.CreateS3TableIntegrationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.create_s3_table_integration_output.CreateS3TableIntegrationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.create_s3_table_integration

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.create_s3_table_integration.create_s3_table_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.create_s3_table_integration_input.CreateS3TableIntegrationInput = {}  # type: ignore[typeddict-item]
        input_["encryption"] = encryption
        input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_telemetry_rule(
        self,
        rule_name: "aws_sdk_observabilityadmin.types.rule_name.RuleName",
        rule: "aws_sdk_observabilityadmin.types.telemetry_rule.TelemetryRule",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        tags: Optional[
            "aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "aws_sdk_observabilityadmin.types.create_telemetry_rule_output.CreateTelemetryRuleOutput":
        """<p> Creates a telemetry rule that defines how telemetry should be configured for Amazon Web Services resources in your account. The rule specifies which resources should have telemetry enabled and how that telemetry data should be collected based on resource type, telemetry type, and selection criteria. </p>

        Args:
            rule_name: <p> A unique name for the telemetry rule being created. </p>
            rule: <p> The configuration details for the telemetry rule, including the resource type, telemetry type, destination configuration, and selection criteria for which resources the rule applies to. </p>
            tags: <p> The key-value pairs to associate with the telemetry rule resource for categorization and management purposes. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.create_telemetry_rule_input.CreateTelemetryRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.create_telemetry_rule_output.CreateTelemetryRuleOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.create_telemetry_rule

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.create_telemetry_rule.create_telemetry_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.create_telemetry_rule_input.CreateTelemetryRuleInput = {}  # type: ignore[typeddict-item]
        input_["rule_name"] = rule_name
        input_["rule"] = rule
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_telemetry_rule_for_organization(
        self,
        rule_name: "aws_sdk_observabilityadmin.types.rule_name.RuleName",
        rule: "aws_sdk_observabilityadmin.types.telemetry_rule.TelemetryRule",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        tags: Optional[
            "aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
    ) -> "aws_sdk_observabilityadmin.types.create_telemetry_rule_for_organization_output.CreateTelemetryRuleForOrganizationOutput":
        """<p> Creates a telemetry rule that applies across an Amazon Web Services Organization. This operation can only be called by the organization's management account or a delegated administrator account. </p>

        Args:
            rule_name: <p> A unique name for the organization-wide telemetry rule being created. </p>
            rule: <p> The configuration details for the organization-wide telemetry rule, including the resource type, telemetry type, destination configuration, and selection criteria for which resources the rule applies to across the organization. </p>
            tags: <p> The key-value pairs to associate with the organization telemetry rule resource for categorization and management purposes. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.create_telemetry_rule_for_organization_input.CreateTelemetryRuleForOrganizationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.create_telemetry_rule_for_organization_output.CreateTelemetryRuleForOrganizationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.create_telemetry_rule_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.create_telemetry_rule_for_organization.create_telemetry_rule_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.create_telemetry_rule_for_organization_input.CreateTelemetryRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
        input_["rule_name"] = rule_name
        input_["rule"] = rule
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_centralization_rule_for_organization(
        self,
        rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes an organization-wide centralization rule. This operation can only be called by the organization's management account or a delegated administrator account.</p>

        Args:
            rule_identifier: <p>The identifier (name or ARN) of the organization centralization rule to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.delete_centralization_rule_for_organization_input.DeleteCentralizationRuleForOrganizationInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_observabilityadmin._operations.observability_admin.delete_centralization_rule_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.delete_centralization_rule_for_organization.delete_centralization_rule_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.delete_centralization_rule_for_organization_input.DeleteCentralizationRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
        input_["rule_identifier"] = rule_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_s3_table_integration(
        self,
        arn: "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes an S3 Table integration and its associated data. This operation removes the connection between CloudWatch Observability Admin and S3 Tables.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the S3 Table integration to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.delete_s3_table_integration_input.DeleteS3TableIntegrationInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_observabilityadmin._operations.observability_admin.delete_s3_table_integration

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.delete_s3_table_integration.delete_s3_table_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.delete_s3_table_integration_input.DeleteS3TableIntegrationInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_telemetry_rule(
        self,
        rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p> Deletes a telemetry rule from your account. Any telemetry configurations previously created by the rule will remain but no new resources will be configured by this rule. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the telemetry rule to delete. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.delete_telemetry_rule_input.DeleteTelemetryRuleInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_observabilityadmin._operations.observability_admin.delete_telemetry_rule

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.delete_telemetry_rule.delete_telemetry_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.delete_telemetry_rule_input.DeleteTelemetryRuleInput = {}  # type: ignore[typeddict-item]
        input_["rule_identifier"] = rule_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_telemetry_rule_for_organization(
        self,
        rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p> Deletes an organization-wide telemetry rule. This operation can only be called by the organization's management account or a delegated administrator account. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the organization telemetry rule to delete. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.delete_telemetry_rule_for_organization_input.DeleteTelemetryRuleForOrganizationInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_observabilityadmin._operations.observability_admin.delete_telemetry_rule_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.delete_telemetry_rule_for_organization.delete_telemetry_rule_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.delete_telemetry_rule_for_organization_input.DeleteTelemetryRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
        input_["rule_identifier"] = rule_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_centralization_rule_for_organization(
        self,
        rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "aws_sdk_observabilityadmin.types.get_centralization_rule_for_organization_output.GetCentralizationRuleForOrganizationOutput":
        """<p>Retrieves the details of a specific organization centralization rule. This operation can only be called by the organization's management account or a delegated administrator account.</p>

        Args:
            rule_identifier: <p>The identifier (name or ARN) of the organization centralization rule to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.get_centralization_rule_for_organization_input.GetCentralizationRuleForOrganizationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.get_centralization_rule_for_organization_output.GetCentralizationRuleForOrganizationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.get_centralization_rule_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.get_centralization_rule_for_organization.get_centralization_rule_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.get_centralization_rule_for_organization_input.GetCentralizationRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
        input_["rule_identifier"] = rule_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_s3_table_integration(
        self,
        arn: "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "aws_sdk_observabilityadmin.types.get_s3_table_integration_output.GetS3TableIntegrationOutput":
        """<p>Retrieves information about a specific S3 Table integration, including its configuration, status, and metadata.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the S3 Table integration to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.get_s3_table_integration_input.GetS3TableIntegrationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.get_s3_table_integration_output.GetS3TableIntegrationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.get_s3_table_integration

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.get_s3_table_integration.get_s3_table_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.get_s3_table_integration_input.GetS3TableIntegrationInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_telemetry_enrichment_status(
        self, *, config_overrides: Optional[ObservabilityAdminClientConfig] = None
    ) -> "aws_sdk_observabilityadmin.types.get_telemetry_enrichment_status_output.GetTelemetryEnrichmentStatusOutput":
        """<p> Returns the current status of the resource tags for telemetry feature, which enhances telemetry data with additional resource metadata from Resource Explorer. </p>"""

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.get_telemetry_enrichment_status_output.GetTelemetryEnrichmentStatusOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.get_telemetry_enrichment_status

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.get_telemetry_enrichment_status.get_telemetry_enrichment_status(
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

    def get_telemetry_evaluation_status(
        self, *, config_overrides: Optional[ObservabilityAdminClientConfig] = None
    ) -> "aws_sdk_observabilityadmin.types.get_telemetry_evaluation_status_output.GetTelemetryEvaluationStatusOutput":
        """<p> Returns the current onboarding status of the telemetry config feature, including the status of the feature and reason the feature failed to start or stop. </p>"""

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.get_telemetry_evaluation_status_output.GetTelemetryEvaluationStatusOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.get_telemetry_evaluation_status

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.get_telemetry_evaluation_status.get_telemetry_evaluation_status(
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

    def get_telemetry_evaluation_status_for_organization(
        self, *, config_overrides: Optional[ObservabilityAdminClientConfig] = None
    ) -> "aws_sdk_observabilityadmin.types.get_telemetry_evaluation_status_for_organization_output.GetTelemetryEvaluationStatusForOrganizationOutput":
        """<p> This returns the onboarding status of the telemetry configuration feature for the organization. It can only be called by a Management Account of an Amazon Web Services Organization or an assigned Delegated Admin Account of Amazon CloudWatch telemetry config. </p>"""

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.get_telemetry_evaluation_status_for_organization_output.GetTelemetryEvaluationStatusForOrganizationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.get_telemetry_evaluation_status_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.get_telemetry_evaluation_status_for_organization.get_telemetry_evaluation_status_for_organization(
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

    def get_telemetry_rule(
        self,
        rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "aws_sdk_observabilityadmin.types.get_telemetry_rule_output.GetTelemetryRuleOutput":
        """<p> Retrieves the details of a specific telemetry rule in your account. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the telemetry rule to retrieve. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.get_telemetry_rule_input.GetTelemetryRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.get_telemetry_rule_output.GetTelemetryRuleOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.get_telemetry_rule

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.get_telemetry_rule.get_telemetry_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.get_telemetry_rule_input.GetTelemetryRuleInput = {}  # type: ignore[typeddict-item]
        input_["rule_identifier"] = rule_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_telemetry_rule_for_organization(
        self,
        rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "aws_sdk_observabilityadmin.types.get_telemetry_rule_for_organization_output.GetTelemetryRuleForOrganizationOutput":
        """<p> Retrieves the details of a specific organization telemetry rule. This operation can only be called by the organization's management account or a delegated administrator account. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the organization telemetry rule to retrieve. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.get_telemetry_rule_for_organization_input.GetTelemetryRuleForOrganizationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.get_telemetry_rule_for_organization_output.GetTelemetryRuleForOrganizationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.get_telemetry_rule_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.get_telemetry_rule_for_organization.get_telemetry_rule_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.get_telemetry_rule_for_organization_input.GetTelemetryRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
        input_["rule_identifier"] = rule_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_centralization_rules_for_organization(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        all_regions: Optional[bool] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_centralization_rules_for_organization_max_results.ListCentralizationRulesForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_observabilityadmin.types.list_centralization_rules_for_organization_output.ListCentralizationRulesForOrganizationOutput":
        """<p>Lists all centralization rules in your organization. This operation can only be called by the organization's management account or a delegated administrator account.</p>

        Args:
            rule_name_prefix: <p>A string to filter organization centralization rules whose names begin with the specified prefix.</p>
            all_regions: <p>A flag determining whether to return organization centralization rules from all regions or only the current region.</p>
            max_results: <p>The maximum number of organization centralization rules to return in a single call.</p>
            next_token: <p>The token for the next set of results. A previous call generates this token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.list_centralization_rules_for_organization_input.ListCentralizationRulesForOrganizationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.list_centralization_rules_for_organization_output.ListCentralizationRulesForOrganizationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.list_centralization_rules_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.list_centralization_rules_for_organization.list_centralization_rules_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.list_centralization_rules_for_organization_input.ListCentralizationRulesForOrganizationInput = {}  # type: ignore[typeddict-item]
        if rule_name_prefix is not None:
            input_["rule_name_prefix"] = rule_name_prefix
        if all_regions is not None:
            input_["all_regions"] = all_regions
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_centralization_rules_for_organization(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        all_regions: Optional[bool] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_centralization_rules_for_organization_max_results.ListCentralizationRulesForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_observabilityadmin.types.centralization_rule_summary.CentralizationRuleSummary]":
        _token = next_token
        while True:
            _response = self.list_centralization_rules_for_organization(
                config_overrides=config_overrides,
                rule_name_prefix=rule_name_prefix,
                all_regions=all_regions,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("centralization_rule_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_telemetry(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        resource_identifier_prefix: Optional[
            "aws_sdk_observabilityadmin.types.resource_identifier_prefix.ResourceIdentifierPrefix"
        ] = None,
        resource_types: Optional[
            "aws_sdk_observabilityadmin.types.resource_types.ResourceTypes"
        ] = None,
        telemetry_configuration_state: Optional[
            "aws_sdk_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
        ] = None,
        resource_tags: Optional[
            "aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_resource_telemetry_max_results.ListResourceTelemetryMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_observabilityadmin.types.list_resource_telemetry_output.ListResourceTelemetryOutput":
        r"""<p> Returns a list of telemetry configurations for Amazon Web Services resources supported by telemetry config. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-cloudwatch.html\">Auditing CloudWatch telemetry configurations</a>. </p>

        Args:
            resource_identifier_prefix: <p> A string used to filter resources which have a <code>ResourceIdentifier</code> starting with the <code>ResourceIdentifierPrefix</code>. </p>
            resource_types: <p> A list of resource types used to filter resources supported by telemetry config. If this parameter is provided, the resources will be returned in the same order used in the request. </p>
            telemetry_configuration_state: <p> A key-value pair to filter resources based on the telemetry type and the state of the telemetry configuration. The key is the telemetry type and the value is the state. </p>
            resource_tags: <p> A key-value pair to filter resources based on tags associated with the resource. For more information about tags, see <a href=\"https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html\">What are tags?</a> </p>
            max_results: <p> A number field used to limit the number of results within the returned list. </p>
            next_token: <p> The token for the next set of items to return. A previous call generates this token. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.list_resource_telemetry_input.ListResourceTelemetryInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.list_resource_telemetry_output.ListResourceTelemetryOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.list_resource_telemetry

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.list_resource_telemetry.list_resource_telemetry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.list_resource_telemetry_input.ListResourceTelemetryInput = {}  # type: ignore[typeddict-item]
        if resource_identifier_prefix is not None:
            input_["resource_identifier_prefix"] = resource_identifier_prefix
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if telemetry_configuration_state is not None:
            input_["telemetry_configuration_state"] = telemetry_configuration_state
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_resource_telemetry(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        resource_identifier_prefix: Optional[
            "aws_sdk_observabilityadmin.types.resource_identifier_prefix.ResourceIdentifierPrefix"
        ] = None,
        resource_types: Optional[
            "aws_sdk_observabilityadmin.types.resource_types.ResourceTypes"
        ] = None,
        telemetry_configuration_state: Optional[
            "aws_sdk_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
        ] = None,
        resource_tags: Optional[
            "aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_resource_telemetry_max_results.ListResourceTelemetryMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_observabilityadmin.types.telemetry_configuration.TelemetryConfiguration]":
        _token = next_token
        while True:
            _response = self.list_resource_telemetry(
                config_overrides=config_overrides,
                resource_identifier_prefix=resource_identifier_prefix,
                resource_types=resource_types,
                telemetry_configuration_state=telemetry_configuration_state,
                resource_tags=resource_tags,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("telemetry_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_telemetry_for_organization(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        account_identifiers: Optional[
            "aws_sdk_observabilityadmin.types.account_identifiers.AccountIdentifiers"
        ] = None,
        resource_identifier_prefix: Optional[
            "aws_sdk_observabilityadmin.types.resource_identifier_prefix.ResourceIdentifierPrefix"
        ] = None,
        resource_types: Optional[
            "aws_sdk_observabilityadmin.types.resource_types.ResourceTypes"
        ] = None,
        telemetry_configuration_state: Optional[
            "aws_sdk_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
        ] = None,
        resource_tags: Optional[
            "aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_resource_telemetry_for_organization_max_results.ListResourceTelemetryForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_observabilityadmin.types.list_resource_telemetry_for_organization_output.ListResourceTelemetryForOrganizationOutput":
        r"""<p> Returns a list of telemetry configurations for Amazon Web Services resources supported by telemetry config in the organization. </p>

        Args:
            account_identifiers: <p> A list of Amazon Web Services accounts used to filter the resources to those associated with the specified accounts. </p>
            resource_identifier_prefix: <p> A string used to filter resources in the organization which have a <code>ResourceIdentifier</code> starting with the <code>ResourceIdentifierPrefix</code>. </p>
            resource_types: <p> A list of resource types used to filter resources in the organization. If this parameter is provided, the resources will be returned in the same order used in the request. </p>
            telemetry_configuration_state: <p> A key-value pair to filter resources in the organization based on the telemetry type and the state of the telemetry configuration. The key is the telemetry type and the value is the state. </p>
            resource_tags: <p> A key-value pair to filter resources in the organization based on tags associated with the resource. Fore more information about tags, see <a href=\"https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html\">What are tags?</a> </p>
            max_results: <p> A number field used to limit the number of results within the returned list. </p>
            next_token: <p> The token for the next set of items to return. A previous call provides this token. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.list_resource_telemetry_for_organization_input.ListResourceTelemetryForOrganizationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.list_resource_telemetry_for_organization_output.ListResourceTelemetryForOrganizationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.list_resource_telemetry_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.list_resource_telemetry_for_organization.list_resource_telemetry_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.list_resource_telemetry_for_organization_input.ListResourceTelemetryForOrganizationInput = {}  # type: ignore[typeddict-item]
        if account_identifiers is not None:
            input_["account_identifiers"] = account_identifiers
        if resource_identifier_prefix is not None:
            input_["resource_identifier_prefix"] = resource_identifier_prefix
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if telemetry_configuration_state is not None:
            input_["telemetry_configuration_state"] = telemetry_configuration_state
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_resource_telemetry_for_organization(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        account_identifiers: Optional[
            "aws_sdk_observabilityadmin.types.account_identifiers.AccountIdentifiers"
        ] = None,
        resource_identifier_prefix: Optional[
            "aws_sdk_observabilityadmin.types.resource_identifier_prefix.ResourceIdentifierPrefix"
        ] = None,
        resource_types: Optional[
            "aws_sdk_observabilityadmin.types.resource_types.ResourceTypes"
        ] = None,
        telemetry_configuration_state: Optional[
            "aws_sdk_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
        ] = None,
        resource_tags: Optional[
            "aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"
        ] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_resource_telemetry_for_organization_max_results.ListResourceTelemetryForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_observabilityadmin.types.telemetry_configuration.TelemetryConfiguration]":
        _token = next_token
        while True:
            _response = self.list_resource_telemetry_for_organization(
                config_overrides=config_overrides,
                account_identifiers=account_identifiers,
                resource_identifier_prefix=resource_identifier_prefix,
                resource_types=resource_types,
                telemetry_configuration_state=telemetry_configuration_state,
                resource_tags=resource_tags,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("telemetry_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_s3_table_integrations(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_s3_table_integrations_max_results.ListS3TableIntegrationsMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_observabilityadmin.types.list_s3_table_integrations_output.ListS3TableIntegrationsOutput":
        """<p>Lists all S3 Table integrations in your account. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            max_results: <p>The maximum number of S3 Table integrations to return in a single call.</p>
            next_token: <p>The token for the next set of results. A previous call generates this token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.list_s3_table_integrations_input.ListS3TableIntegrationsInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.list_s3_table_integrations_output.ListS3TableIntegrationsOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.list_s3_table_integrations

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.list_s3_table_integrations.list_s3_table_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.list_s3_table_integrations_input.ListS3TableIntegrationsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_s3_table_integrations(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_s3_table_integrations_max_results.ListS3TableIntegrationsMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_observabilityadmin.types.integration_summary.IntegrationSummary]":
        _token = next_token
        while True:
            _response = self.list_s3_table_integrations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("integration_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "aws_sdk_observabilityadmin.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p> Lists all tags attached to the specified resource. Supports telemetry rule resources and telemetry pipeline resources. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the telemetry rule resource whose tags you want to list. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.list_tags_for_resource

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_telemetry_rules(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_telemetry_rules_max_results.ListTelemetryRulesMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_observabilityadmin.types.list_telemetry_rules_output.ListTelemetryRulesOutput":
        """<p> Lists all telemetry rules in your account. You can filter the results by specifying a rule name prefix. </p>

        Args:
            rule_name_prefix: <p> A string to filter telemetry rules whose names begin with the specified prefix. </p>
            max_results: <p> The maximum number of telemetry rules to return in a single call. </p>
            next_token: <p> The token for the next set of results. A previous call generates this token. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.list_telemetry_rules_input.ListTelemetryRulesInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.list_telemetry_rules_output.ListTelemetryRulesOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.list_telemetry_rules

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.list_telemetry_rules.list_telemetry_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.list_telemetry_rules_input.ListTelemetryRulesInput = {}  # type: ignore[typeddict-item]
        if rule_name_prefix is not None:
            input_["rule_name_prefix"] = rule_name_prefix
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_telemetry_rules(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_telemetry_rules_max_results.ListTelemetryRulesMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_observabilityadmin.types.telemetry_rule_summary.TelemetryRuleSummary]":
        _token = next_token
        while True:
            _response = self.list_telemetry_rules(
                config_overrides=config_overrides,
                rule_name_prefix=rule_name_prefix,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("telemetry_rule_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_telemetry_rules_for_organization(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        source_account_ids: Optional[
            "aws_sdk_observabilityadmin.types.account_identifiers.AccountIdentifiers"
        ] = None,
        source_organization_unit_ids: Optional[
            "aws_sdk_observabilityadmin.types.organization_unit_identifiers.OrganizationUnitIdentifiers"
        ] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_telemetry_rules_for_organization_max_results.ListTelemetryRulesForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_observabilityadmin.types.list_telemetry_rules_for_organization_output.ListTelemetryRulesForOrganizationOutput":
        """<p> Lists all telemetry rules in your organization. This operation can only be called by the organization's management account or a delegated administrator account. </p>

        Args:
            rule_name_prefix: <p> A string to filter organization telemetry rules whose names begin with the specified prefix. </p>
            source_account_ids: <p> The list of account IDs to filter organization telemetry rules by their source accounts. </p>
            source_organization_unit_ids: <p> The list of organizational unit IDs to filter organization telemetry rules by their source organizational units. </p>
            max_results: <p> The maximum number of organization telemetry rules to return in a single call. </p>
            next_token: <p> The token for the next set of results. A previous call generates this token. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.list_telemetry_rules_for_organization_input.ListTelemetryRulesForOrganizationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.list_telemetry_rules_for_organization_output.ListTelemetryRulesForOrganizationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.list_telemetry_rules_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.list_telemetry_rules_for_organization.list_telemetry_rules_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.list_telemetry_rules_for_organization_input.ListTelemetryRulesForOrganizationInput = {}  # type: ignore[typeddict-item]
        if rule_name_prefix is not None:
            input_["rule_name_prefix"] = rule_name_prefix
        if source_account_ids is not None:
            input_["source_account_ids"] = source_account_ids
        if source_organization_unit_ids is not None:
            input_["source_organization_unit_ids"] = source_organization_unit_ids
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_telemetry_rules_for_organization(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        rule_name_prefix: Optional[str] = None,
        source_account_ids: Optional[
            "aws_sdk_observabilityadmin.types.account_identifiers.AccountIdentifiers"
        ] = None,
        source_organization_unit_ids: Optional[
            "aws_sdk_observabilityadmin.types.organization_unit_identifiers.OrganizationUnitIdentifiers"
        ] = None,
        max_results: Optional[
            "aws_sdk_observabilityadmin.types.list_telemetry_rules_for_organization_max_results.ListTelemetryRulesForOrganizationMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_observabilityadmin.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_observabilityadmin.types.telemetry_rule_summary.TelemetryRuleSummary]":
        _token = next_token
        while True:
            _response = self.list_telemetry_rules_for_organization(
                config_overrides=config_overrides,
                rule_name_prefix=rule_name_prefix,
                source_account_ids=source_account_ids,
                source_organization_unit_ids=source_organization_unit_ids,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("telemetry_rule_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_telemetry_enrichment(
        self, *, config_overrides: Optional[ObservabilityAdminClientConfig] = None
    ) -> "aws_sdk_observabilityadmin.types.start_telemetry_enrichment_output.StartTelemetryEnrichmentOutput":
        """<p> Enables the resource tags for telemetry feature for your account, which enhances telemetry data with additional resource metadata from Resource Explorer to provide richer context for monitoring and observability. </p>"""

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.start_telemetry_enrichment_output.StartTelemetryEnrichmentOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.start_telemetry_enrichment

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.start_telemetry_enrichment.start_telemetry_enrichment(
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

    def start_telemetry_evaluation(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        regions: Optional["aws_sdk_observabilityadmin.types.regions.Regions"] = None,
        all_regions: Optional[
            "aws_sdk_observabilityadmin.types.all_regions.AllRegions"
        ] = None,
    ) -> None:
        """<p> This action begins onboarding the caller Amazon Web Services account to the telemetry config feature. </p>

        Args:
            regions: <p> An optional list of Amazon Web Services Regions to include in multi-region telemetry evaluation. The current region is always implicitly included and must not be specified in this list. When provided, telemetry evaluation starts in the current region and propagates to all specified regions. Mutually exclusive with <code>AllRegions</code>. If neither <code>Regions</code> nor <code>AllRegions</code> is provided, the operation applies only to the current region. </p>
            all_regions: <p> If set to <code>true</code>, telemetry evaluation starts in all Amazon Web Services Regions where Amazon CloudWatch Observability Admin is available in the current partition. The current region becomes the home region for managing multi-region evaluation. When new regions become available, evaluation automatically expands to include them. Mutually exclusive with <code>Regions</code>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.start_telemetry_evaluation_input.StartTelemetryEvaluationInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_observabilityadmin._operations.observability_admin.start_telemetry_evaluation

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.start_telemetry_evaluation.start_telemetry_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.start_telemetry_evaluation_input.StartTelemetryEvaluationInput = {}  # type: ignore[typeddict-item]
        if regions is not None:
            input_["regions"] = regions
        if all_regions is not None:
            input_["all_regions"] = all_regions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_telemetry_evaluation_for_organization(
        self,
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
        regions: Optional["aws_sdk_observabilityadmin.types.regions.Regions"] = None,
        all_regions: Optional[
            "aws_sdk_observabilityadmin.types.all_regions.AllRegions"
        ] = None,
    ) -> None:
        """<p> This actions begins onboarding the organization and all member accounts to the telemetry config feature. </p>

        Args:
            regions: <p> An optional list of Amazon Web Services Regions to include in multi-region telemetry evaluation for the organization. The current region is always implicitly included and must not be specified in this list. When provided, telemetry evaluation starts in the current region and propagates to all specified regions for the organization. Mutually exclusive with <code>AllRegions</code>. If neither <code>Regions</code> nor <code>AllRegions</code> is provided, the operation applies only to the current region. </p>
            all_regions: <p> If set to <code>true</code>, telemetry evaluation for the organization starts in all Amazon Web Services Regions where Amazon CloudWatch Observability Admin is available in the current partition. The current region becomes the home region for managing multi-region evaluation for the organization. When new regions become available, evaluation automatically expands to include them. Mutually exclusive with <code>Regions</code>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.start_telemetry_evaluation_for_organization_input.StartTelemetryEvaluationForOrganizationInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_observabilityadmin._operations.observability_admin.start_telemetry_evaluation_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.start_telemetry_evaluation_for_organization.start_telemetry_evaluation_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.start_telemetry_evaluation_for_organization_input.StartTelemetryEvaluationForOrganizationInput = {}  # type: ignore[typeddict-item]
        if regions is not None:
            input_["regions"] = regions
        if all_regions is not None:
            input_["all_regions"] = all_regions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_telemetry_enrichment(
        self, *, config_overrides: Optional[ObservabilityAdminClientConfig] = None
    ) -> "aws_sdk_observabilityadmin.types.stop_telemetry_enrichment_output.StopTelemetryEnrichmentOutput":
        """<p> Disables the resource tags for telemetry feature for your account, stopping the enhancement of telemetry data with additional resource metadata. </p>"""

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.stop_telemetry_enrichment_output.StopTelemetryEnrichmentOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.stop_telemetry_enrichment

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.stop_telemetry_enrichment.stop_telemetry_enrichment(
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

    def stop_telemetry_evaluation(
        self, *, config_overrides: Optional[ObservabilityAdminClientConfig] = None
    ) -> None:
        """<p> This action begins offboarding the caller Amazon Web Services account from the telemetry config feature. </p>"""

        def _handler(req: "OperationRequest[None]") -> OperationResponse[None]:
            import aws_sdk_observabilityadmin._operations.observability_admin.stop_telemetry_evaluation

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.stop_telemetry_evaluation.stop_telemetry_evaluation(
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

    def stop_telemetry_evaluation_for_organization(
        self, *, config_overrides: Optional[ObservabilityAdminClientConfig] = None
    ) -> None:
        """<p> This action offboards the Organization of the caller Amazon Web Services account from the telemetry config feature. </p>"""

        def _handler(req: "OperationRequest[None]") -> OperationResponse[None]:
            import aws_sdk_observabilityadmin._operations.observability_admin.stop_telemetry_evaluation_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.stop_telemetry_evaluation_for_organization.stop_telemetry_evaluation_for_organization(
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

    def tag_resource(
        self,
        resource_arn: "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn",
        tags: "aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p> Adds or updates tags for a resource. Supports telemetry rule resources and telemetry pipeline resources. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the telemetry rule resource to tag. </p>
            tags: <p> The key-value pairs to add or update for the telemetry rule resource. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_observabilityadmin._operations.observability_admin.tag_resource

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def test_telemetry_pipeline(
        self,
        records: "aws_sdk_observabilityadmin.types.records.Records",
        configuration: "aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "aws_sdk_observabilityadmin.types.test_telemetry_pipeline_output.TestTelemetryPipelineOutput":
        """<p>Tests a pipeline configuration with sample records to validate data processing before deployment. This operation helps ensure your pipeline configuration works as expected. </p>

        Args:
            records: <p>The sample records to process through the pipeline configuration for testing purposes.</p>
            configuration: <p>The pipeline configuration to test with the provided sample records.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.test_telemetry_pipeline_input.TestTelemetryPipelineInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.test_telemetry_pipeline_output.TestTelemetryPipelineOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.test_telemetry_pipeline

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.test_telemetry_pipeline.test_telemetry_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.test_telemetry_pipeline_input.TestTelemetryPipelineInput = {}  # type: ignore[typeddict-item]
        input_["records"] = records
        input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_observabilityadmin.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> None:
        """<p> Removes tags from a resource. Supports telemetry rule resources and telemetry pipeline resources. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the telemetry rule resource to remove tags from. </p>
            tag_keys: <p> The list of tag keys to remove from the telemetry rule resource. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[None]:
            import aws_sdk_observabilityadmin._operations.observability_admin.untag_resource

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_centralization_rule_for_organization(
        self,
        rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier",
        rule: "aws_sdk_observabilityadmin.types.centralization_rule.CentralizationRule",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "aws_sdk_observabilityadmin.types.update_centralization_rule_for_organization_output.UpdateCentralizationRuleForOrganizationOutput":
        """<p>Updates an existing centralization rule that applies across an Amazon Web Services Organization. This operation can only be called by the organization's management account or a delegated administrator account.</p>

        Args:
            rule_identifier: <p>The identifier (name or ARN) of the organization centralization rule to update.</p>
            rule: <p>The configuration details for the organization-wide centralization rule, including the source configuration and the destination configuration to centralize telemetry data across the organization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.update_centralization_rule_for_organization_input.UpdateCentralizationRuleForOrganizationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.update_centralization_rule_for_organization_output.UpdateCentralizationRuleForOrganizationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.update_centralization_rule_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.update_centralization_rule_for_organization.update_centralization_rule_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.update_centralization_rule_for_organization_input.UpdateCentralizationRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
        input_["rule_identifier"] = rule_identifier
        input_["rule"] = rule

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_telemetry_rule(
        self,
        rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier",
        rule: "aws_sdk_observabilityadmin.types.telemetry_rule.TelemetryRule",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "aws_sdk_observabilityadmin.types.update_telemetry_rule_output.UpdateTelemetryRuleOutput":
        """<p> Updates an existing telemetry rule in your account. If multiple users attempt to modify the same telemetry rule simultaneously, a ConflictException is returned to provide specific error information for concurrent modification scenarios. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the telemetry rule to update. </p>
            rule: <p> The new configuration details for the telemetry rule. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.update_telemetry_rule_input.UpdateTelemetryRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.update_telemetry_rule_output.UpdateTelemetryRuleOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.update_telemetry_rule

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.update_telemetry_rule.update_telemetry_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.update_telemetry_rule_input.UpdateTelemetryRuleInput = {}  # type: ignore[typeddict-item]
        input_["rule_identifier"] = rule_identifier
        input_["rule"] = rule

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_telemetry_rule_for_organization(
        self,
        rule_identifier: "aws_sdk_observabilityadmin.types.rule_identifier.RuleIdentifier",
        rule: "aws_sdk_observabilityadmin.types.telemetry_rule.TelemetryRule",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "aws_sdk_observabilityadmin.types.update_telemetry_rule_for_organization_output.UpdateTelemetryRuleForOrganizationOutput":
        """<p> Updates an existing telemetry rule that applies across an Amazon Web Services Organization. This operation can only be called by the organization's management account or a delegated administrator account. </p>

        Args:
            rule_identifier: <p> The identifier (name or ARN) of the organization telemetry rule to update. </p>
            rule: <p> The new configuration details for the organization telemetry rule, including resource type, telemetry type, and destination configuration. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.update_telemetry_rule_for_organization_input.UpdateTelemetryRuleForOrganizationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.update_telemetry_rule_for_organization_output.UpdateTelemetryRuleForOrganizationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.update_telemetry_rule_for_organization

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.update_telemetry_rule_for_organization.update_telemetry_rule_for_organization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.update_telemetry_rule_for_organization_input.UpdateTelemetryRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
        input_["rule_identifier"] = rule_identifier
        input_["rule"] = rule

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def validate_telemetry_pipeline_configuration(
        self,
        configuration: "aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration",
        *,
        config_overrides: Optional[ObservabilityAdminClientConfig] = None,
    ) -> "aws_sdk_observabilityadmin.types.validate_telemetry_pipeline_configuration_output.ValidateTelemetryPipelineConfigurationOutput":
        """<p>Validates a pipeline configuration without creating the pipeline. This operation checks the configuration for syntax errors and compatibility issues.</p>

        Args:
            configuration: <p>The pipeline configuration to validate for syntax and compatibility.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_observabilityadmin.types.validate_telemetry_pipeline_configuration_input.ValidateTelemetryPipelineConfigurationInput]",
        ) -> OperationResponse[
            "aws_sdk_observabilityadmin.types.validate_telemetry_pipeline_configuration_output.ValidateTelemetryPipelineConfigurationOutput"
        ]:
            import aws_sdk_observabilityadmin._operations.observability_admin.validate_telemetry_pipeline_configuration

            output, http_response = (
                aws_sdk_observabilityadmin._operations.observability_admin.validate_telemetry_pipeline_configuration.validate_telemetry_pipeline_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_observabilityadmin.types.validate_telemetry_pipeline_configuration_input.ValidateTelemetryPipelineConfigurationInput = {}  # type: ignore[typeddict-item]
        input_["configuration"] = configuration

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
