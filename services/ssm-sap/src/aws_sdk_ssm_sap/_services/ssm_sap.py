"""Generated from Smithy shape ``com.amazonaws.ssmsap#SsmSap``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_ssm_sap._auth._signers
import aws_sdk_ssm_sap._auth._sigv4
from aws_sdk_ssm_sap._auth._identity import Credentials
from aws_sdk_ssm_sap._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_ssm_sap._auth._zapros_handler import AuthMiddleware
from aws_sdk_ssm_sap._pagination import resolve_path as _resolve_path
from aws_sdk_ssm_sap._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.app_registry_arn
    import aws_sdk_ssm_sap.types.application_credential_list
    import aws_sdk_ssm_sap.types.application_id
    import aws_sdk_ssm_sap.types.application_summary
    import aws_sdk_ssm_sap.types.application_type
    import aws_sdk_ssm_sap.types.arn
    import aws_sdk_ssm_sap.types.backint_config
    import aws_sdk_ssm_sap.types.component_id
    import aws_sdk_ssm_sap.types.component_info_list
    import aws_sdk_ssm_sap.types.component_summary
    import aws_sdk_ssm_sap.types.configuration_check_definition
    import aws_sdk_ssm_sap.types.configuration_check_operation
    import aws_sdk_ssm_sap.types.configuration_check_operation_listing_mode
    import aws_sdk_ssm_sap.types.configuration_check_type_list
    import aws_sdk_ssm_sap.types.connected_entity_type
    import aws_sdk_ssm_sap.types.database_id
    import aws_sdk_ssm_sap.types.database_summary
    import aws_sdk_ssm_sap.types.delete_resource_permission_input
    import aws_sdk_ssm_sap.types.delete_resource_permission_output
    import aws_sdk_ssm_sap.types.deregister_application_input
    import aws_sdk_ssm_sap.types.deregister_application_output
    import aws_sdk_ssm_sap.types.filter_list
    import aws_sdk_ssm_sap.types.get_application_input
    import aws_sdk_ssm_sap.types.get_application_output
    import aws_sdk_ssm_sap.types.get_component_input
    import aws_sdk_ssm_sap.types.get_component_output
    import aws_sdk_ssm_sap.types.get_configuration_check_operation_input
    import aws_sdk_ssm_sap.types.get_configuration_check_operation_output
    import aws_sdk_ssm_sap.types.get_database_input
    import aws_sdk_ssm_sap.types.get_database_output
    import aws_sdk_ssm_sap.types.get_operation_input
    import aws_sdk_ssm_sap.types.get_operation_output
    import aws_sdk_ssm_sap.types.get_resource_permission_input
    import aws_sdk_ssm_sap.types.get_resource_permission_output
    import aws_sdk_ssm_sap.types.instance_list
    import aws_sdk_ssm_sap.types.list_applications_input
    import aws_sdk_ssm_sap.types.list_applications_output
    import aws_sdk_ssm_sap.types.list_components_input
    import aws_sdk_ssm_sap.types.list_components_output
    import aws_sdk_ssm_sap.types.list_configuration_check_definitions_input
    import aws_sdk_ssm_sap.types.list_configuration_check_definitions_output
    import aws_sdk_ssm_sap.types.list_configuration_check_operations_input
    import aws_sdk_ssm_sap.types.list_configuration_check_operations_output
    import aws_sdk_ssm_sap.types.list_databases_input
    import aws_sdk_ssm_sap.types.list_databases_output
    import aws_sdk_ssm_sap.types.list_operation_events_input
    import aws_sdk_ssm_sap.types.list_operation_events_output
    import aws_sdk_ssm_sap.types.list_operations_input
    import aws_sdk_ssm_sap.types.list_operations_output
    import aws_sdk_ssm_sap.types.list_sub_check_results_input
    import aws_sdk_ssm_sap.types.list_sub_check_results_output
    import aws_sdk_ssm_sap.types.list_sub_check_rule_results_input
    import aws_sdk_ssm_sap.types.list_sub_check_rule_results_output
    import aws_sdk_ssm_sap.types.list_tags_for_resource_request
    import aws_sdk_ssm_sap.types.list_tags_for_resource_response
    import aws_sdk_ssm_sap.types.max_results
    import aws_sdk_ssm_sap.types.next_token
    import aws_sdk_ssm_sap.types.operation
    import aws_sdk_ssm_sap.types.operation_event
    import aws_sdk_ssm_sap.types.operation_id
    import aws_sdk_ssm_sap.types.permission_action_type
    import aws_sdk_ssm_sap.types.put_resource_permission_input
    import aws_sdk_ssm_sap.types.put_resource_permission_output
    import aws_sdk_ssm_sap.types.register_application_input
    import aws_sdk_ssm_sap.types.register_application_output
    import aws_sdk_ssm_sap.types.rule_result
    import aws_sdk_ssm_sap.types.sap_instance_number
    import aws_sdk_ssm_sap.types.sid
    import aws_sdk_ssm_sap.types.ssm_sap_arn
    import aws_sdk_ssm_sap.types.start_application_input
    import aws_sdk_ssm_sap.types.start_application_output
    import aws_sdk_ssm_sap.types.start_application_refresh_input
    import aws_sdk_ssm_sap.types.start_application_refresh_output
    import aws_sdk_ssm_sap.types.start_configuration_checks_input
    import aws_sdk_ssm_sap.types.start_configuration_checks_output
    import aws_sdk_ssm_sap.types.stop_application_input
    import aws_sdk_ssm_sap.types.stop_application_output
    import aws_sdk_ssm_sap.types.sub_check_result
    import aws_sdk_ssm_sap.types.sub_check_result_id
    import aws_sdk_ssm_sap.types.tag_key_list
    import aws_sdk_ssm_sap.types.tag_map
    import aws_sdk_ssm_sap.types.tag_resource_request
    import aws_sdk_ssm_sap.types.tag_resource_response
    import aws_sdk_ssm_sap.types.untag_resource_request
    import aws_sdk_ssm_sap.types.untag_resource_response
    import aws_sdk_ssm_sap.types.update_application_settings_input
    import aws_sdk_ssm_sap.types.update_application_settings_output


class SsmSapClientConfig(TypedDict, total=False):
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


class SsmSapClient:
    """A client for the ``SsmSap`` service.

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
        self.config = SsmSapClientConfig(
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
        self, config_overrides: Optional[SsmSapClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SsmSapClientConfig = config_overrides or {}
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

    def delete_resource_permission(
        self,
        resource_arn: "aws_sdk_ssm_sap.types.arn.Arn",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        action_type: Optional[
            "aws_sdk_ssm_sap.types.permission_action_type.PermissionActionType"
        ] = None,
        source_resource_arn: Optional["aws_sdk_ssm_sap.types.arn.Arn"] = None,
    ) -> "aws_sdk_ssm_sap.types.delete_resource_permission_output.DeleteResourcePermissionOutput":
        """<p>Removes permissions associated with the target database.</p>

        Args:
            action_type: <p>Delete or restore the permissions on the target database.</p>
            source_resource_arn: <p>The Amazon Resource Name (ARN) of the source resource.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.delete_resource_permission_input.DeleteResourcePermissionInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.delete_resource_permission_output.DeleteResourcePermissionOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.delete_resource_permission

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.delete_resource_permission.delete_resource_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.delete_resource_permission_input.DeleteResourcePermissionInput = {}  # type: ignore[typeddict-item]
        if action_type is not None:
            input["action_type"] = action_type
        if source_resource_arn is not None:
            input["source_resource_arn"] = source_resource_arn
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deregister_application(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
    ) -> "aws_sdk_ssm_sap.types.deregister_application_output.DeregisterApplicationOutput":
        """<p>Deregister an SAP application with AWS Systems Manager for SAP. This action does not aﬀect the existing setup of your SAP workloads on Amazon EC2.</p>

        Args:
            application_id: <p>The ID of the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.deregister_application_input.DeregisterApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.deregister_application_output.DeregisterApplicationOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.deregister_application

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.deregister_application.deregister_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.deregister_application_input.DeregisterApplicationInput = {}  # type: ignore[typeddict-item]
        input["application_id"] = application_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_application(
        self,
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        application_id: Optional[
            "aws_sdk_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        application_arn: Optional["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"] = None,
        app_registry_arn: Optional[
            "aws_sdk_ssm_sap.types.app_registry_arn.AppRegistryArn"
        ] = None,
    ) -> "aws_sdk_ssm_sap.types.get_application_output.GetApplicationOutput":
        """<p>Gets an application registered with AWS Systems Manager for SAP. It also returns the components of the application.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            application_arn: <p>The Amazon Resource Name (ARN) of the application. </p>
            app_registry_arn: <p>The Amazon Resource Name (ARN) of the application registry.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.get_application_input.GetApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.get_application_output.GetApplicationOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.get_application

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.get_application_input.GetApplicationInput = {}  # type: ignore[typeddict-item]
        if application_id is not None:
            input["application_id"] = application_id
        if application_arn is not None:
            input["application_arn"] = application_arn
        if app_registry_arn is not None:
            input["app_registry_arn"] = app_registry_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_component(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        component_id: "aws_sdk_ssm_sap.types.component_id.ComponentId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
    ) -> "aws_sdk_ssm_sap.types.get_component_output.GetComponentOutput":
        """<p>Gets the component of an application registered with AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            component_id: <p>The ID of the component.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.get_component_input.GetComponentInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.get_component_output.GetComponentOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.get_component

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.get_component.get_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.get_component_input.GetComponentInput = {}  # type: ignore[typeddict-item]
        input["application_id"] = application_id
        input["component_id"] = component_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_configuration_check_operation(
        self,
        operation_id: "aws_sdk_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
    ) -> "aws_sdk_ssm_sap.types.get_configuration_check_operation_output.GetConfigurationCheckOperationOutput":
        """<p>Gets the details of a configuration check operation by specifying the operation ID.</p>

        Args:
            operation_id: <p>The ID of the configuration check operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.get_configuration_check_operation_input.GetConfigurationCheckOperationInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.get_configuration_check_operation_output.GetConfigurationCheckOperationOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.get_configuration_check_operation

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.get_configuration_check_operation.get_configuration_check_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.get_configuration_check_operation_input.GetConfigurationCheckOperationInput = {}  # type: ignore[typeddict-item]
        input["operation_id"] = operation_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_database(
        self,
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        application_id: Optional[
            "aws_sdk_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        component_id: Optional["aws_sdk_ssm_sap.types.component_id.ComponentId"] = None,
        database_id: Optional["aws_sdk_ssm_sap.types.database_id.DatabaseId"] = None,
        database_arn: Optional["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"] = None,
    ) -> "aws_sdk_ssm_sap.types.get_database_output.GetDatabaseOutput":
        """<p>Gets the SAP HANA database of an application registered with AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            component_id: <p>The ID of the component.</p>
            database_id: <p>The ID of the database.</p>
            database_arn: <p>The Amazon Resource Name (ARN) of the database.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.get_database_input.GetDatabaseInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.get_database_output.GetDatabaseOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.get_database

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.get_database.get_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.get_database_input.GetDatabaseInput = {}  # type: ignore[typeddict-item]
        if application_id is not None:
            input["application_id"] = application_id
        if component_id is not None:
            input["component_id"] = component_id
        if database_id is not None:
            input["database_id"] = database_id
        if database_arn is not None:
            input["database_arn"] = database_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_operation(
        self,
        operation_id: "aws_sdk_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
    ) -> "aws_sdk_ssm_sap.types.get_operation_output.GetOperationOutput":
        """<p>Gets the details of an operation by specifying the operation ID.</p>

        Args:
            operation_id: <p>The ID of the operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.get_operation_input.GetOperationInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.get_operation_output.GetOperationOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.get_operation

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.get_operation.get_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.get_operation_input.GetOperationInput = {}  # type: ignore[typeddict-item]
        input["operation_id"] = operation_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_permission(
        self,
        resource_arn: "aws_sdk_ssm_sap.types.arn.Arn",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        action_type: Optional[
            "aws_sdk_ssm_sap.types.permission_action_type.PermissionActionType"
        ] = None,
    ) -> "aws_sdk_ssm_sap.types.get_resource_permission_output.GetResourcePermissionOutput":
        """<p>Gets permissions associated with the target database.</p>

        Args:
            action_type: <p/>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.get_resource_permission_input.GetResourcePermissionInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.get_resource_permission_output.GetResourcePermissionOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.get_resource_permission

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.get_resource_permission.get_resource_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.get_resource_permission_input.GetResourcePermissionInput = {}  # type: ignore[typeddict-item]
        if action_type is not None:
            input["action_type"] = action_type
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_applications(
        self,
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        filters: Optional["aws_sdk_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "aws_sdk_ssm_sap.types.list_applications_output.ListApplicationsOutput":
        """<p>Lists all the applications registered with AWS Systems Manager for SAP.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            filters: <p>The filter of name, value, and operator.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.list_applications_input.ListApplicationsInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.list_applications_output.ListApplicationsOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.list_applications

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.list_applications_input.ListApplicationsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if filters is not None:
            input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_applications(
        self,
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        filters: Optional["aws_sdk_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "Iterator[aws_sdk_ssm_sap.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_components(
        self,
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        application_id: Optional[
            "aws_sdk_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_ssm_sap.types.list_components_output.ListComponentsOutput":
        """<p>Lists all the components registered with AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p> <p>If you do not specify a value for MaxResults, the request returns 50 items per page by default.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.list_components_input.ListComponentsInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.list_components_output.ListComponentsOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.list_components

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.list_components.list_components(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.list_components_input.ListComponentsInput = {}  # type: ignore[typeddict-item]
        if application_id is not None:
            input["application_id"] = application_id
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

    def iter_list_components(
        self,
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        application_id: Optional[
            "aws_sdk_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
    ) -> "Iterator[aws_sdk_ssm_sap.types.component_summary.ComponentSummary]":
        _token = next_token
        while True:
            _response = self.list_components(
                config_overrides=config_overrides,
                application_id=application_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("components",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_configuration_check_definitions(
        self,
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_ssm_sap.types.list_configuration_check_definitions_output.ListConfigurationCheckDefinitionsOutput":
        """<p>Lists all configuration check types supported by AWS Systems Manager for SAP.</p>

        Args:
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            next_token: <p>The token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.list_configuration_check_definitions_input.ListConfigurationCheckDefinitionsInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.list_configuration_check_definitions_output.ListConfigurationCheckDefinitionsOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.list_configuration_check_definitions

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.list_configuration_check_definitions.list_configuration_check_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.list_configuration_check_definitions_input.ListConfigurationCheckDefinitionsInput = {}  # type: ignore[typeddict-item]
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

    def iter_list_configuration_check_definitions(
        self,
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_ssm_sap.types.configuration_check_definition.ConfigurationCheckDefinition]":
        _token = next_token
        while True:
            _response = self.list_configuration_check_definitions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("configuration_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_configuration_check_operations(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        list_mode: Optional[
            "aws_sdk_ssm_sap.types.configuration_check_operation_listing_mode.ConfigurationCheckOperationListingMode"
        ] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["aws_sdk_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "aws_sdk_ssm_sap.types.list_configuration_check_operations_output.ListConfigurationCheckOperationsOutput":
        """<p>Lists the configuration check operations performed by AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            list_mode: <p>The mode for listing configuration check operations. Defaults to \"LATEST_PER_CHECK\".</p> <ul> <li> <p>LATEST_PER_CHECK - Will list the latest configuration check operation per check type.</p> </li> <li> <p>ALL_OPERATIONS - Will list all configuration check operations performed on the application.</p> </li> </ul>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            next_token: <p>The token for the next page of results.</p>
            filters: <p>The filters of an operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.list_configuration_check_operations_input.ListConfigurationCheckOperationsInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.list_configuration_check_operations_output.ListConfigurationCheckOperationsOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.list_configuration_check_operations

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.list_configuration_check_operations.list_configuration_check_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.list_configuration_check_operations_input.ListConfigurationCheckOperationsInput = {}  # type: ignore[typeddict-item]
        input["application_id"] = application_id
        if list_mode is not None:
            input["list_mode"] = list_mode
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_configuration_check_operations(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        list_mode: Optional[
            "aws_sdk_ssm_sap.types.configuration_check_operation_listing_mode.ConfigurationCheckOperationListingMode"
        ] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["aws_sdk_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "Iterator[aws_sdk_ssm_sap.types.configuration_check_operation.ConfigurationCheckOperation]":
        _token = next_token
        while True:
            _response = self.list_configuration_check_operations(
                application_id,
                config_overrides=config_overrides,
                list_mode=list_mode,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("configuration_check_operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_databases(
        self,
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        application_id: Optional[
            "aws_sdk_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        component_id: Optional["aws_sdk_ssm_sap.types.component_id.ComponentId"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_ssm_sap.types.list_databases_output.ListDatabasesOutput":
        """<p>Lists the SAP HANA databases of an application registered with AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            component_id: <p>The ID of the component.</p>
            next_token: <p>The token for the next page of results. </p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value. If you do not specify a value for MaxResults, the request returns 50 items per page by default.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.list_databases_input.ListDatabasesInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.list_databases_output.ListDatabasesOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.list_databases

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.list_databases.list_databases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.list_databases_input.ListDatabasesInput = {}  # type: ignore[typeddict-item]
        if application_id is not None:
            input["application_id"] = application_id
        if component_id is not None:
            input["component_id"] = component_id
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

    def iter_list_databases(
        self,
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        application_id: Optional[
            "aws_sdk_ssm_sap.types.application_id.ApplicationId"
        ] = None,
        component_id: Optional["aws_sdk_ssm_sap.types.component_id.ComponentId"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
    ) -> "Iterator[aws_sdk_ssm_sap.types.database_summary.DatabaseSummary]":
        _token = next_token
        while True:
            _response = self.list_databases(
                config_overrides=config_overrides,
                application_id=application_id,
                component_id=component_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("databases",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_operation_events(
        self,
        operation_id: "aws_sdk_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["aws_sdk_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "aws_sdk_ssm_sap.types.list_operation_events_output.ListOperationEventsOutput":
        """<p>Returns a list of operations events.</p> <p>Available parameters include <code>OperationID</code>, as well as optional parameters <code>MaxResults</code>, <code>NextToken</code>, and <code>Filters</code>.</p>

        Args:
            operation_id: <p>The ID of the operation.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p> <p>If you do not specify a value for <code>MaxResults</code>, the request returns 50 items per page by default.</p>
            next_token: <p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>
            filters: <p>Optionally specify filters to narrow the returned operation event items.</p> <p>Valid filter names include <code>status</code>, <code>resourceID</code>, and <code>resourceType</code>. The valid operator for all three filters is <code>Equals</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.list_operation_events_input.ListOperationEventsInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.list_operation_events_output.ListOperationEventsOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.list_operation_events

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.list_operation_events.list_operation_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.list_operation_events_input.ListOperationEventsInput = {}  # type: ignore[typeddict-item]
        input["operation_id"] = operation_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_operation_events(
        self,
        operation_id: "aws_sdk_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["aws_sdk_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "Iterator[aws_sdk_ssm_sap.types.operation_event.OperationEvent]":
        _token = next_token
        while True:
            _response = self.list_operation_events(
                operation_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("operation_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_operations(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["aws_sdk_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "aws_sdk_ssm_sap.types.list_operations_output.ListOperationsOutput":
        """<p>Lists the operations performed by AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value. If you do not specify a value for MaxResults, the request returns 50 items per page by default.</p>
            next_token: <p>The token for the next page of results. </p>
            filters: <p>The filters of an operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.list_operations_input.ListOperationsInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.list_operations_output.ListOperationsOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.list_operations

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.list_operations.list_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.list_operations_input.ListOperationsInput = {}  # type: ignore[typeddict-item]
        input["application_id"] = application_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_operations(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
        filters: Optional["aws_sdk_ssm_sap.types.filter_list.FilterList"] = None,
    ) -> "Iterator[aws_sdk_ssm_sap.types.operation.Operation]":
        _token = next_token
        while True:
            _response = self.list_operations(
                application_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sub_check_results(
        self,
        operation_id: "aws_sdk_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
    ) -> (
        "aws_sdk_ssm_sap.types.list_sub_check_results_output.ListSubCheckResultsOutput"
    ):
        """<p>Lists the sub-check results of a specified configuration check operation.</p>

        Args:
            operation_id: <p>The ID of the configuration check operation.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            next_token: <p>The token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.list_sub_check_results_input.ListSubCheckResultsInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.list_sub_check_results_output.ListSubCheckResultsOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.list_sub_check_results

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.list_sub_check_results.list_sub_check_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.list_sub_check_results_input.ListSubCheckResultsInput = {}  # type: ignore[typeddict-item]
        input["operation_id"] = operation_id
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

    def iter_list_sub_check_results(
        self,
        operation_id: "aws_sdk_ssm_sap.types.operation_id.OperationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_ssm_sap.types.sub_check_result.SubCheckResult]":
        _token = next_token
        while True:
            _response = self.list_sub_check_results(
                operation_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sub_check_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sub_check_rule_results(
        self,
        sub_check_result_id: "aws_sdk_ssm_sap.types.sub_check_result_id.SubCheckResultId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_ssm_sap.types.list_sub_check_rule_results_output.ListSubCheckRuleResultsOutput":
        """<p>Lists the rules of a specified sub-check belonging to a configuration check operation.</p>

        Args:
            sub_check_result_id: <p>The ID of the sub check result.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            next_token: <p>The token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.list_sub_check_rule_results_input.ListSubCheckRuleResultsInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.list_sub_check_rule_results_output.ListSubCheckRuleResultsOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.list_sub_check_rule_results

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.list_sub_check_rule_results.list_sub_check_rule_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.list_sub_check_rule_results_input.ListSubCheckRuleResultsInput = {}  # type: ignore[typeddict-item]
        input["sub_check_result_id"] = sub_check_result_id
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

    def iter_list_sub_check_rule_results(
        self,
        sub_check_result_id: "aws_sdk_ssm_sap.types.sub_check_result_id.SubCheckResultId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        max_results: Optional["aws_sdk_ssm_sap.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_ssm_sap.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_ssm_sap.types.rule_result.RuleResult]":
        _token = next_token
        while True:
            _response = self.list_sub_check_rule_results(
                sub_check_result_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("rule_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
    ) -> "aws_sdk_ssm_sap.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags on an SAP HANA application and/or database registered with AWS Systems Manager for SAP.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.list_tags_for_resource

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_resource_permission(
        self,
        action_type: "aws_sdk_ssm_sap.types.permission_action_type.PermissionActionType",
        source_resource_arn: "aws_sdk_ssm_sap.types.arn.Arn",
        resource_arn: "aws_sdk_ssm_sap.types.arn.Arn",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
    ) -> "aws_sdk_ssm_sap.types.put_resource_permission_output.PutResourcePermissionOutput":
        """<p>Adds permissions to the target database.</p>

        Args:
            action_type: <p/>
            source_resource_arn: <p/>
            resource_arn: <p/>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.put_resource_permission_input.PutResourcePermissionInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.put_resource_permission_output.PutResourcePermissionOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.put_resource_permission

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.put_resource_permission.put_resource_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.put_resource_permission_input.PutResourcePermissionInput = {}  # type: ignore[typeddict-item]
        input["action_type"] = action_type
        input["source_resource_arn"] = source_resource_arn
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_application(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        application_type: "aws_sdk_ssm_sap.types.application_type.ApplicationType",
        instances: "aws_sdk_ssm_sap.types.instance_list.InstanceList",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        sap_instance_number: Optional[
            "aws_sdk_ssm_sap.types.sap_instance_number.SAPInstanceNumber"
        ] = None,
        sid: Optional["aws_sdk_ssm_sap.types.sid.SID"] = None,
        tags: Optional["aws_sdk_ssm_sap.types.tag_map.TagMap"] = None,
        credentials: Optional[
            "aws_sdk_ssm_sap.types.application_credential_list.ApplicationCredentialList"
        ] = None,
        database_arn: Optional["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"] = None,
        components_info: Optional[
            "aws_sdk_ssm_sap.types.component_info_list.ComponentInfoList"
        ] = None,
    ) -> "aws_sdk_ssm_sap.types.register_application_output.RegisterApplicationOutput":
        """<p>Register an SAP application with AWS Systems Manager for SAP. You must meet the following requirements before registering. </p> <p>The SAP application you want to register with AWS Systems Manager for SAP is running on Amazon EC2.</p> <p>AWS Systems Manager Agent must be setup on an Amazon EC2 instance along with the required IAM permissions.</p> <p>Amazon EC2 instance(s) must have access to the secrets created in AWS Secrets Manager to manage SAP applications and components.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            application_type: <p>The type of the application.</p>
            instances: <p>The Amazon EC2 instances on which your SAP application is running.</p>
            sap_instance_number: <p>The SAP instance number of the application.</p>
            sid: <p>The System ID of the application.</p>
            tags: <p>The tags to be attached to the SAP application.</p>
            credentials: <p>The credentials of the SAP application.</p>
            database_arn: <p>The Amazon Resource Name of the SAP HANA database.</p>
            components_info: <p>This is an optional parameter for component details to which the SAP ABAP application is attached, such as Web Dispatcher.</p> <p>This is an array of ApplicationComponent objects. You may input 0 to 5 items.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.register_application_input.RegisterApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.register_application_output.RegisterApplicationOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.register_application

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.register_application.register_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.register_application_input.RegisterApplicationInput = {}  # type: ignore[typeddict-item]
        input["application_id"] = application_id
        input["application_type"] = application_type
        input["instances"] = instances
        if sap_instance_number is not None:
            input["sap_instance_number"] = sap_instance_number
        if sid is not None:
            input["sid"] = sid
        if tags is not None:
            input["tags"] = tags
        if credentials is not None:
            input["credentials"] = credentials
        if database_arn is not None:
            input["database_arn"] = database_arn
        if components_info is not None:
            input["components_info"] = components_info

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_application(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
    ) -> "aws_sdk_ssm_sap.types.start_application_output.StartApplicationOutput":
        """<p>Request is an operation which starts an application.</p> <p>Parameter <code>ApplicationId</code> is required.</p>

        Args:
            application_id: <p>The ID of the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.start_application_input.StartApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.start_application_output.StartApplicationOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.start_application

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.start_application.start_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.start_application_input.StartApplicationInput = {}  # type: ignore[typeddict-item]
        input["application_id"] = application_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_application_refresh(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
    ) -> "aws_sdk_ssm_sap.types.start_application_refresh_output.StartApplicationRefreshOutput":
        """<p>Refreshes a registered application.</p>

        Args:
            application_id: <p>The ID of the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.start_application_refresh_input.StartApplicationRefreshInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.start_application_refresh_output.StartApplicationRefreshOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.start_application_refresh

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.start_application_refresh.start_application_refresh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.start_application_refresh_input.StartApplicationRefreshInput = {}  # type: ignore[typeddict-item]
        input["application_id"] = application_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_configuration_checks(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        configuration_check_ids: Optional[
            "aws_sdk_ssm_sap.types.configuration_check_type_list.ConfigurationCheckTypeList"
        ] = None,
    ) -> "aws_sdk_ssm_sap.types.start_configuration_checks_output.StartConfigurationChecksOutput":
        """<p>Initiates configuration check operations against a specified application.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            configuration_check_ids: <p>The list of configuration checks to perform.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.start_configuration_checks_input.StartConfigurationChecksInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.start_configuration_checks_output.StartConfigurationChecksOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.start_configuration_checks

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.start_configuration_checks.start_configuration_checks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.start_configuration_checks_input.StartConfigurationChecksInput = {}  # type: ignore[typeddict-item]
        input["application_id"] = application_id
        if configuration_check_ids is not None:
            input["configuration_check_ids"] = configuration_check_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_application(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        stop_connected_entity: Optional[
            "aws_sdk_ssm_sap.types.connected_entity_type.ConnectedEntityType"
        ] = None,
        include_ec2_instance_shutdown: Optional[bool] = None,
    ) -> "aws_sdk_ssm_sap.types.stop_application_output.StopApplicationOutput":
        """<p>Request is an operation to stop an application.</p> <p>Parameter <code>ApplicationId</code> is required. Parameters <code>StopConnectedEntity</code> and <code>IncludeEc2InstanceShutdown</code> are optional.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            stop_connected_entity: <p>Specify the <code>ConnectedEntityType</code>. Accepted type is <code>DBMS</code>.</p> <p>If this parameter is included, the connected DBMS (Database Management System) will be stopped.</p>
            include_ec2_instance_shutdown: <p>Boolean. If included and if set to <code>True</code>, the StopApplication operation will shut down the associated Amazon EC2 instance in addition to the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.stop_application_input.StopApplicationInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.stop_application_output.StopApplicationOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.stop_application

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.stop_application.stop_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.stop_application_input.StopApplicationInput = {}  # type: ignore[typeddict-item]
        input["application_id"] = application_id
        if stop_connected_entity is not None:
            input["stop_connected_entity"] = stop_connected_entity
        if include_ec2_instance_shutdown is not None:
            input["include_ec2_instance_shutdown"] = include_ec2_instance_shutdown

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn",
        tags: "aws_sdk_ssm_sap.types.tag_map.TagMap",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
    ) -> "aws_sdk_ssm_sap.types.tag_resource_response.TagResourceResponse":
        """<p>Creates tag for a resource by specifying the ARN.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags on a resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.tag_resource

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn",
        tag_keys: "aws_sdk_ssm_sap.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
    ) -> "aws_sdk_ssm_sap.types.untag_resource_response.UntagResourceResponse":
        """<p>Delete the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>Adds/updates or removes credentials for applications registered with AWS Systems Manager for SAP.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.untag_resource

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_application_settings(
        self,
        application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SsmSapClientConfig] = None,
        credentials_to_add_or_update: Optional[
            "aws_sdk_ssm_sap.types.application_credential_list.ApplicationCredentialList"
        ] = None,
        credentials_to_remove: Optional[
            "aws_sdk_ssm_sap.types.application_credential_list.ApplicationCredentialList"
        ] = None,
        backint: Optional["aws_sdk_ssm_sap.types.backint_config.BackintConfig"] = None,
        database_arn: Optional["aws_sdk_ssm_sap.types.ssm_sap_arn.SsmSapArn"] = None,
    ) -> "aws_sdk_ssm_sap.types.update_application_settings_output.UpdateApplicationSettingsOutput":
        """<p>Updates the settings of an application registered with AWS Systems Manager for SAP.</p>

        Args:
            application_id: <p>The ID of the application.</p>
            credentials_to_add_or_update: <p>The credentials to be added or updated.</p>
            credentials_to_remove: <p>The credentials to be removed.</p>
            backint: <p>Installation of AWS Backint Agent for SAP HANA.</p>
            database_arn: <p>The Amazon Resource Name of the SAP HANA database that replaces the current SAP HANA connection with the SAP_ABAP application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_sap.types.update_application_settings_input.UpdateApplicationSettingsInput]",
        ) -> OperationResponse[
            "aws_sdk_ssm_sap.types.update_application_settings_output.UpdateApplicationSettingsOutput"
        ]:
            import aws_sdk_ssm_sap._operations.ssm_sap.update_application_settings

            output, http_response = (
                aws_sdk_ssm_sap._operations.ssm_sap.update_application_settings.update_application_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_ssm_sap.types.update_application_settings_input.UpdateApplicationSettingsInput = {}  # type: ignore[typeddict-item]
        input["application_id"] = application_id
        if credentials_to_add_or_update is not None:
            input["credentials_to_add_or_update"] = credentials_to_add_or_update
        if credentials_to_remove is not None:
            input["credentials_to_remove"] = credentials_to_remove
        if backint is not None:
            input["backint"] = backint
        if database_arn is not None:
            input["database_arn"] = database_arn

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
