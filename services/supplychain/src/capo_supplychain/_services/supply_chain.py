"""Generated from Smithy shape ``com.amazonaws.supplychain#GalaxyPublicAPIGateway``."""

import datetime
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_supplychain._auth._signers
import capo_supplychain._auth._sigv4
from capo_supplychain._auth._identity import Credentials
from capo_supplychain._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_supplychain._auth._zapros_handler import AuthMiddleware
from capo_supplychain._pagination import resolve_path as _resolve_path
from capo_supplychain._resources.galaxy_public_api_gateway.bill_of_materials_import_job_resource import (
    BillOfMaterialsImportJobResource,
)
from capo_supplychain._resources.galaxy_public_api_gateway.data_integration_flow_resource import (
    DataIntegrationFlowResource,
)
from capo_supplychain._resources.galaxy_public_api_gateway.data_lake_dataset_resource import (
    DataLakeDatasetResource,
)
from capo_supplychain._resources.galaxy_public_api_gateway.data_lake_namespace_resource import (
    DataLakeNamespaceResource,
)
from capo_supplychain._resources.galaxy_public_api_gateway.instance_resource import (
    InstanceResource,
)
from capo_supplychain._services._aws_config import aws_config
from capo_supplychain._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_supplychain.types.asc_resource_arn
    import capo_supplychain.types.client_token
    import capo_supplychain.types.data_integration_event
    import capo_supplychain.types.data_integration_event_data
    import capo_supplychain.types.data_integration_event_dataset_target_configuration
    import capo_supplychain.types.data_integration_event_group_id
    import capo_supplychain.types.data_integration_event_max_results
    import capo_supplychain.types.data_integration_event_next_token
    import capo_supplychain.types.data_integration_event_type
    import capo_supplychain.types.data_integration_flow_execution
    import capo_supplychain.types.data_integration_flow_execution_max_results
    import capo_supplychain.types.data_integration_flow_execution_next_token
    import capo_supplychain.types.data_integration_flow_name
    import capo_supplychain.types.get_data_integration_event_request
    import capo_supplychain.types.get_data_integration_event_response
    import capo_supplychain.types.get_data_integration_flow_execution_request
    import capo_supplychain.types.get_data_integration_flow_execution_response
    import capo_supplychain.types.list_data_integration_events_request
    import capo_supplychain.types.list_data_integration_events_response
    import capo_supplychain.types.list_data_integration_flow_executions_request
    import capo_supplychain.types.list_data_integration_flow_executions_response
    import capo_supplychain.types.list_tags_for_resource_request
    import capo_supplychain.types.list_tags_for_resource_response
    import capo_supplychain.types.send_data_integration_event_request
    import capo_supplychain.types.send_data_integration_event_response
    import capo_supplychain.types.tag_key_list
    import capo_supplychain.types.tag_map
    import capo_supplychain.types.tag_resource_request
    import capo_supplychain.types.tag_resource_response
    import capo_supplychain.types.untag_resource_request
    import capo_supplychain.types.untag_resource_response
    import capo_supplychain.types.uuid


class SupplyChainClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SupplyChainClient:
    """A client for the ``SupplyChain`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = SupplyChainClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.bill_of_materials_import_job_resource = BillOfMaterialsImportJobResource(
            self
        )
        self.data_integration_flow_resource = DataIntegrationFlowResource(self)
        self.data_lake_dataset_resource = DataLakeDatasetResource(self)
        self.data_lake_namespace_resource = DataLakeNamespaceResource(self)
        self.instance_resource = InstanceResource(self)

    def operation_options(
        self, config_overrides: Optional[SupplyChainClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SupplyChainClientConfig = config_overrides or {}
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

    def get_data_integration_event(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        event_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_data_integration_event_response.GetDataIntegrationEventResponse":
        """<p>Enables you to programmatically view an Amazon Web Services Supply Chain Data Integration Event. Developers can view the eventType, eventGroupId, eventTimestamp, datasetTarget, datasetLoadExecution.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            event_id: <p>The unique event identifier.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful GetDataIntegrationEvent

            >>> client.get_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_id='19739c8e-cd2e-4cbc-a2f7-0dc43239f042')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.get_data_integration_event_request.GetDataIntegrationEventRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.get_data_integration_event_response.GetDataIntegrationEventResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_event

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_event.get_data_integration_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.get_data_integration_event_request.GetDataIntegrationEventRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["event_id"] = event_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_data_integration_flow_execution(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        flow_name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        execution_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.get_data_integration_flow_execution_response.GetDataIntegrationFlowExecutionResponse":
        """<p>Get the flow execution.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            flow_name: <p>The flow name.</p>
            execution_id: <p>The flow execution identifier.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful GetDataIntegrationFlowExecution for S3 source

            >>> client.get_data_integration_flow_execution(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', flow_name='source-product', execution_id='edbbdd3f-c0f9-49d9-ab01-f64542f803b7')
            Successful GetDataIntegrationFlowExecution for DATASET source

            >>> client.get_data_integration_flow_execution(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', flow_name='target-product', execution_id='9daf6071-d12c-4eef-864c-73cea2557825')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.get_data_integration_flow_execution_request.GetDataIntegrationFlowExecutionRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.get_data_integration_flow_execution_response.GetDataIntegrationFlowExecutionResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow_execution

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.get_data_integration_flow_execution.get_data_integration_flow_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.get_data_integration_flow_execution_request.GetDataIntegrationFlowExecutionRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["flow_name"] = flow_name
        input_["execution_id"] = execution_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_data_integration_events(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        event_type: Optional[
            "capo_supplychain.types.data_integration_event_type.DataIntegrationEventType"
        ] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_event_next_token.DataIntegrationEventNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_event_max_results.DataIntegrationEventMaxResults"
        ] = None,
    ) -> "capo_supplychain.types.list_data_integration_events_response.ListDataIntegrationEventsResponse":
        """<p>Enables you to programmatically list all data integration events for the provided Amazon Web Services Supply Chain instance.</p>

        Args:
            instance_id: <p>The Amazon Web Services Supply Chain instance identifier.</p>
            event_type: <p>List data integration events for the specified eventType.</p>
            next_token: <p>The pagination token to fetch the next page of the data integration events.</p>
            max_results: <p>Specify the maximum number of data integration events to fetch in one paginated request.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful ListDataIntegrationEvents

            >>> client.list_data_integration_events(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.list_data_integration_events_request.ListDataIntegrationEventsRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.list_data_integration_events_response.ListDataIntegrationEventsResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_events

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_events.list_data_integration_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.list_data_integration_events_request.ListDataIntegrationEventsRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        if event_type is not None:
            input_["event_type"] = event_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_data_integration_events(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        event_type: Optional[
            "capo_supplychain.types.data_integration_event_type.DataIntegrationEventType"
        ] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_event_next_token.DataIntegrationEventNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_event_max_results.DataIntegrationEventMaxResults"
        ] = None,
    ) -> "Iterator[capo_supplychain.types.data_integration_event.DataIntegrationEvent]":
        _token = next_token
        while True:
            _response = self.list_data_integration_events(
                instance_id,
                config_overrides=config_overrides,
                event_type=event_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_integration_flow_executions(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        flow_name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_flow_execution_next_token.DataIntegrationFlowExecutionNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_flow_execution_max_results.DataIntegrationFlowExecutionMaxResults"
        ] = None,
    ) -> "capo_supplychain.types.list_data_integration_flow_executions_response.ListDataIntegrationFlowExecutionsResponse":
        """<p>List flow executions.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            flow_name: <p>The flow name.</p>
            next_token: <p>The pagination token to fetch next page of flow executions.</p>
            max_results: <p>The number to specify the max number of flow executions to fetch in this paginated request.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful ListDataIntegrationFlowExecutions

            >>> client.list_data_integration_flow_executions(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', flow_name='source-product')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.list_data_integration_flow_executions_request.ListDataIntegrationFlowExecutionsRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.list_data_integration_flow_executions_response.ListDataIntegrationFlowExecutionsResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flow_executions

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.list_data_integration_flow_executions.list_data_integration_flow_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.list_data_integration_flow_executions_request.ListDataIntegrationFlowExecutionsRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["flow_name"] = flow_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_data_integration_flow_executions(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        flow_name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        next_token: Optional[
            "capo_supplychain.types.data_integration_flow_execution_next_token.DataIntegrationFlowExecutionNextToken"
        ] = None,
        max_results: Optional[
            "capo_supplychain.types.data_integration_flow_execution_max_results.DataIntegrationFlowExecutionMaxResults"
        ] = None,
    ) -> "Iterator[capo_supplychain.types.data_integration_flow_execution.DataIntegrationFlowExecution]":
        _token = next_token
        while True:
            _response = self.list_data_integration_flow_executions(
                instance_id,
                flow_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("flow_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_supplychain.types.asc_resource_arn.AscResourceArn",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all the tags for an Amazon Web ServicesSupply Chain resource. You can list all the tags added to a resource. By listing the tags, developers can view the tag level information on a resource and perform actions such as, deleting a resource associated with a particular tag.</p>

        Args:
            resource_arn: <p>The Amazon Web Services Supply chain resource ARN that needs tags to be listed.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful ListTagsForResource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/data-integration-flows/my_flow1')
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.list_tags_for_resource

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_data_integration_event(
        self,
        instance_id: "capo_supplychain.types.uuid.UUID",
        event_type: "capo_supplychain.types.data_integration_event_type.DataIntegrationEventType",
        data: "capo_supplychain.types.data_integration_event_data.DataIntegrationEventData",
        event_group_id: "capo_supplychain.types.data_integration_event_group_id.DataIntegrationEventGroupId",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
        event_timestamp: Optional[datetime.datetime] = None,
        client_token: Optional[
            "capo_supplychain.types.client_token.ClientToken"
        ] = None,
        dataset_target: Optional[
            "capo_supplychain.types.data_integration_event_dataset_target_configuration.DataIntegrationEventDatasetTargetConfiguration"
        ] = None,
    ) -> "capo_supplychain.types.send_data_integration_event_response.SendDataIntegrationEventResponse":
        r"""<p>Send the data payload for the event with real-time data for analysis or monitoring. The real-time data events are stored in an Amazon Web Services service before being processed and stored in data lake.</p>

        Args:
            instance_id: <p>The AWS Supply Chain instance identifier.</p>
            event_type: <p>The data event type.</p> <ul> <li> <p> <b>scn.data.dataset</b> - Send data directly to any specified dataset.</p> </li> <li> <p> <b>scn.data.supplyplan</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/supply-plan-entity.html\">supply_plan</a> dataset.</p> </li> <li> <p> <b>scn.data.shipmentstoporder</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-order-entity.html\">shipment_stop_order</a> dataset.</p> </li> <li> <p> <b>scn.data.shipmentstop</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-stop-entity.html\">shipment_stop</a> dataset.</p> </li> <li> <p> <b>scn.data.shipment</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-shipment-entity.html\">shipment</a> dataset.</p> </li> <li> <p> <b>scn.data.reservation</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/planning-reservation-entity.html\">reservation</a> dataset.</p> </li> <li> <p> <b>scn.data.processproduct</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-product-entity.html\">process_product</a> dataset.</p> </li> <li> <p> <b>scn.data.processoperation</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-operation-entity.html\">process_operation</a> dataset.</p> </li> <li> <p> <b>scn.data.processheader</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/operation-process-header-entity.html\">process_header</a> dataset.</p> </li> <li> <p> <b>scn.data.forecast</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/forecast-forecast-entity.html\">forecast</a> dataset.</p> </li> <li> <p> <b>scn.data.inventorylevel</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/inventory_mgmnt-inv-level-entity.html\">inv_level</a> dataset.</p> </li> <li> <p> <b>scn.data.inboundorder</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-entity.html\">inbound_order</a> dataset.</p> </li> <li> <p> <b>scn.data.inboundorderline</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-entity.html\">inbound_order_line</a> dataset.</p> </li> <li> <p> <b>scn.data.inboundorderlineschedule</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/replenishment-inbound-order-line-schedule-entity.html\">inbound_order_line_schedule</a> dataset.</p> </li> <li> <p> <b>scn.data.outboundorderline</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-order-line-entity.html\">outbound_order_line</a> dataset.</p> </li> <li> <p> <b>scn.data.outboundshipment</b> - Send data to <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/outbound-fulfillment-shipment-entity.html\">outbound_shipment</a> dataset.</p> </li> </ul>
            data: <p>The data payload of the event, should follow the data schema of the target dataset, or see <a href=\"https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html\">Data entities supported in AWS Supply Chain</a>. To send single data record, use JsonObject format; to send multiple data records, use JsonArray format.</p> <p>Note that for AWS Supply Chain dataset under <b>asc</b> namespace, it has a connection_id internal field that is not allowed to be provided by client directly, they will be auto populated.</p>
            event_group_id: <p>Event identifier (for example, orderId for InboundOrder) used for data sharding or partitioning. Noted under one eventGroupId of same eventType and instanceId, events are processed sequentially in the order they are received by the server.</p>
            event_timestamp: <p>The timestamp (in epoch seconds) associated with the event. If not provided, it will be assigned with current timestamp.</p>
            client_token: <p>The idempotent client token. The token is active for 8 hours, and within its lifetime, it ensures the request completes only once upon retry with same client token. If omitted, the AWS SDK generates a unique value so that AWS SDK can safely retry the request upon network errors.</p>
            dataset_target: <p>The target dataset configuration for <b>scn.data.dataset</b> event type.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful SendDataIntegrationEvent for inboundorder event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.inboundorder', data='{"id": "inbound-order-id-test-123", "tpartner_id": "partner-id-test-123" }', event_group_id='inboundOrderId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for inboundorderline event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.inboundorderline', data='{"id": "inbound-order-line-id-test-123", "order_id": "order-id-test-123", "tpartner_id": "partner-id-test-123", "product_id": "product-id-test-123", "quantity_submitted": "100.0" }', event_group_id='inboundOrderLineId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for inboundorderlineschedule event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.inboundorderlineschedule', data='{"id": "inbound-order-line-schedule-id-test-123", "order_id": "order-id-test-123", "order_line_id": "order-line-id-test-123", "product_id": "product-id-test-123"}', event_group_id='inboundOrderLineScheduleId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for forecast event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.forecast', data='{"snapshot_date": "1672470400000", "product_id": "product-id-test-123", "site_id": "site-id-test-123", "region_id": "region-id-test-123", "product_group_id": "product-group-id-test-123", "forecast_start_dttm": "1672470400000", "forecast_end_dttm": "1672470400000" }', event_group_id='forecastId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for inventorylevel event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.inventorylevel', data='{"snapshot_date": "1672470400000", "site_id": "site-id-test-123", "product_id": "product-id-test-123", "on_hand_inventory": "100.0", "inv_condition": "good", "lot_number": "lot-number-test-123"}', event_group_id='inventoryLevelId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for outboundorderline event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.outboundorderline', data='{"id": "outbound-orderline-id-test-123", "cust_order_id": "cust-order-id-test-123", "product_id": "product-id-test-123" }', event_group_id='outboundOrderLineId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for outboundshipment event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.outboundshipment', data='{"id": "outbound-shipment-id-test-123", "cust_order_id": "cust-order-id-test-123", "cust_order_line_id": "cust-order-line-id-test-123", "product_id": "product-id-test-123" }', event_group_id='outboundShipmentId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for processheader event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.processheader', data='{"process_id": "process-id-test-123" }', event_group_id='processHeaderId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for processoperation event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.processoperation', data='{"process_operation_id": "process-operation-id-test-123", "process_id": "process-id-test-123" }', event_group_id='processOperationId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for processproduct event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.processproduct', data='{"process_product_id": "process-product-id-test-123", "process_id": "process-id-test-123" }', event_group_id='processProductId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for reservation event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.reservation', data='{"reservation_id": "reservation-id-test-123", "reservation_detail_id": "reservation-detail-id-test-123" }', event_group_id='reservationId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for shipment event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.shipment', data='{"id": "shipment-id-test-123", "supplier_tpartner_id": "supplier-tpartner-id-test-123", "product_id": "product-id-test-123", "order_id": "order-id-test-123", "order_line_id": "order-line-id-test-123", "package_id": "package-id-test-123" }', event_group_id='shipmentId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for shipmentstop event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.shipmentstop', data='{"shipment_stop_id": "shipment-stop-id-test-123", "shipment_id": "shipment-id-test-123" }', event_group_id='shipmentStopId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for shipmentstoporder event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.shipmentstoporder', data='{"shipment_stop_order_id": "shipment-stop-order-id-test-123", "shipment_stop_id": "shipment-stop-id-test-123", "shipment_id": "shipment-id-test-123" }', event_group_id='shipmentStopOrderId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for supplyplan event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.supplyplan', data='{"supply_plan_id": "supply-plan-id-test-123" }', event_group_id='supplyPlanId', event_timestamp=1515531081.123)
            Successful SendDataIntegrationEvent for dataset event type

            >>> client.send_data_integration_event(instance_id='8928ae12-15e5-4441-825d-ec2184f0a43a', event_type='scn.data.dataset', data='{"dataset_id": "datset-id-test-123" }', event_group_id='datasetId', event_timestamp=1515531081.123, dataset_target={'datasetIdentifier': 'arn:aws:scn:us-west-2:135808960812:instance/8928ae12-15e5-4441-825d-ec2184f0a43a/namespaces/asc/datasets/product', 'operationType': 'APPEND'})
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.send_data_integration_event_request.SendDataIntegrationEventRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.send_data_integration_event_response.SendDataIntegrationEventResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.send_data_integration_event

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.send_data_integration_event.send_data_integration_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.send_data_integration_event_request.SendDataIntegrationEventRequest = {}  # type: ignore[typeddict-item]
        input_["instance_id"] = instance_id
        input_["event_type"] = event_type
        input_["data"] = data
        input_["event_group_id"] = event_group_id
        if event_timestamp is not None:
            input_["event_timestamp"] = event_timestamp
        if client_token is not None:
            input_["client_token"] = client_token
        if dataset_target is not None:
            input_["dataset_target"] = dataset_target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_supplychain.types.asc_resource_arn.AscResourceArn",
        tags: "capo_supplychain.types.tag_map.TagMap",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.tag_resource_response.TagResourceResponse":
        """<p>You can create tags during or after creating a resource such as instance, data flow, or dataset in AWS Supply chain. During the data ingestion process, you can add tags such as dev, test, or prod to data flows created during the data ingestion process in the AWS Supply Chain datasets. You can use these tags to identify a group of resources or a single resource used by the developer.</p>

        Args:
            resource_arn: <p>The Amazon Web Services Supply chain resource ARN that needs to be tagged.</p>
            tags: <p>The tags of the Amazon Web Services Supply chain resource to be created.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful TagResource

            >>> client.tag_resource(resource_arn='arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/data-integration-flows/my_flow1', tags={'tagKey1': 'tagValue1'})
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.tag_resource

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "capo_supplychain.types.asc_resource_arn.AscResourceArn",
        tag_keys: "capo_supplychain.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[SupplyChainClientConfig] = None,
    ) -> "capo_supplychain.types.untag_resource_response.UntagResourceResponse":
        """<p>You can delete tags for an Amazon Web Services Supply chain resource such as instance, data flow, or dataset in AWS Supply Chain. During the data ingestion process, you can delete tags such as dev, test, or prod to data flows created during the data ingestion process in the AWS Supply Chain datasets. </p>

        Args:
            resource_arn: <p>The Amazon Web Services Supply chain resource ARN that needs to be untagged.</p>
            tag_keys: <p>The list of tag keys to be deleted for an Amazon Web Services Supply Chain resource.</p>

        Raises:
            capo_supplychain.errors.access_denied_exception.AccessDeniedException: <p>You do not have the required privileges to perform this action.</p>
            capo_supplychain.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_supplychain.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_supplychain.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_supplychain.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_supplychain.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_supplychain.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an AWS service.</p>
            capo_supplychain.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful UntagResource

            >>> client.untag_resource(resource_arn='arn:aws:scn:us-east-1:123456789012:instance/8850c54e-e187-4fa7-89d4-6370f165174d/data-integration-flows/my_flow1', tag_keys=['tagKey1'])
        """

        def _handler(
            req: "OperationRequest[capo_supplychain.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_supplychain.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_supplychain._operations.galaxy_public_api_gateway.untag_resource

            output, http_response = (
                capo_supplychain._operations.galaxy_public_api_gateway.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_supplychain.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

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
