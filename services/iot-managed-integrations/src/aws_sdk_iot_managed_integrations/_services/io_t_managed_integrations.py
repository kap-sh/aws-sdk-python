"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#IotManagedIntegrations``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_iot_managed_integrations._auth._signers
import aws_sdk_iot_managed_integrations._auth._sigv4
from aws_sdk_iot_managed_integrations._auth._identity import Credentials
from aws_sdk_iot_managed_integrations._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_iot_managed_integrations._auth._zapros_handler import AuthMiddleware
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.account_association_resource import (
    AccountAssociationResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.cloud_connector_resource import (
    CloudConnectorResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.connector_destination_resource import (
    ConnectorDestinationResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.credential_locker_resource import (
    CredentialLockerResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.destination_resource import (
    DestinationResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.device_discovery_resource import (
    DeviceDiscoveryResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.event_log_configuration_resource import (
    EventLogConfigurationResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.hub_configuration_resource import (
    HubConfigurationResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.kms_key_association_resource import (
    KmsKeyAssociationResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.managed_thing_association_resource import (
    ManagedThingAssociationResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.managed_thing_command_resource import (
    ManagedThingCommandResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.managed_thing_resource import (
    ManagedThingResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.managed_thing_state_resource import (
    ManagedThingStateResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.notification_configuration_resource import (
    NotificationConfigurationResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.ota_task_configuration_resource import (
    OtaTaskConfigurationResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.ota_task_resource import (
    OtaTaskResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.provisioning_profile_resource import (
    ProvisioningProfileResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.runtime_log_configuration_resource import (
    RuntimeLogConfigurationResource,
)
from aws_sdk_iot_managed_integrations._resources.iot_managed_integrations.schema_version_resource import (
    SchemaVersionResource,
)
from aws_sdk_iot_managed_integrations._services._aws_config import aws_config
from aws_sdk_iot_managed_integrations._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.connector_device_id
    import aws_sdk_iot_managed_integrations.types.connector_event_message
    import aws_sdk_iot_managed_integrations.types.connector_event_operation
    import aws_sdk_iot_managed_integrations.types.connector_event_operation_version
    import aws_sdk_iot_managed_integrations.types.connector_event_status_code
    import aws_sdk_iot_managed_integrations.types.connector_id
    import aws_sdk_iot_managed_integrations.types.device_discovery_id
    import aws_sdk_iot_managed_integrations.types.devices
    import aws_sdk_iot_managed_integrations.types.get_custom_endpoint_request
    import aws_sdk_iot_managed_integrations.types.get_custom_endpoint_response
    import aws_sdk_iot_managed_integrations.types.io_t_managed_integrations_resource_arn
    import aws_sdk_iot_managed_integrations.types.list_tags_for_resource_request
    import aws_sdk_iot_managed_integrations.types.list_tags_for_resource_response
    import aws_sdk_iot_managed_integrations.types.matter_endpoint
    import aws_sdk_iot_managed_integrations.types.register_custom_endpoint_request
    import aws_sdk_iot_managed_integrations.types.register_custom_endpoint_response
    import aws_sdk_iot_managed_integrations.types.send_connector_event_request
    import aws_sdk_iot_managed_integrations.types.send_connector_event_response
    import aws_sdk_iot_managed_integrations.types.tag_key_list
    import aws_sdk_iot_managed_integrations.types.tag_resource_request
    import aws_sdk_iot_managed_integrations.types.tag_resource_response
    import aws_sdk_iot_managed_integrations.types.tags_map
    import aws_sdk_iot_managed_integrations.types.third_party_user_id
    import aws_sdk_iot_managed_integrations.types.trace_id
    import aws_sdk_iot_managed_integrations.types.untag_resource_request
    import aws_sdk_iot_managed_integrations.types.untag_resource_response


class IoTManagedIntegrationsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class IoTManagedIntegrationsClient:
    """A client for the ``IoTManagedIntegrations`` service.

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
        self._config = IoTManagedIntegrationsClientConfig(
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
        self.account_association_resource = AccountAssociationResource(self)
        self.cloud_connector_resource = CloudConnectorResource(self)
        self.connector_destination_resource = ConnectorDestinationResource(self)
        self.credential_locker_resource = CredentialLockerResource(self)
        self.destination_resource = DestinationResource(self)
        self.device_discovery_resource = DeviceDiscoveryResource(self)
        self.event_log_configuration_resource = EventLogConfigurationResource(self)
        self.hub_configuration_resource = HubConfigurationResource(self)
        self.kms_key_association_resource = KmsKeyAssociationResource(self)
        self.managed_thing_association_resource = ManagedThingAssociationResource(self)
        self.managed_thing_command_resource = ManagedThingCommandResource(self)
        self.managed_thing_resource = ManagedThingResource(self)
        self.managed_thing_state_resource = ManagedThingStateResource(self)
        self.notification_configuration_resource = NotificationConfigurationResource(
            self
        )
        self.ota_task_configuration_resource = OtaTaskConfigurationResource(self)
        self.ota_task_resource = OtaTaskResource(self)
        self.provisioning_profile_resource = ProvisioningProfileResource(self)
        self.runtime_log_configuration_resource = RuntimeLogConfigurationResource(self)
        self.schema_version_resource = SchemaVersionResource(self)

    def operation_options(
        self, config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: IoTManagedIntegrationsClientConfig = config_overrides or {}
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

    def get_custom_endpoint(
        self, *, config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None
    ) -> "aws_sdk_iot_managed_integrations.types.get_custom_endpoint_response.GetCustomEndpointResponse":
        """<p>Returns the IoT managed integrations custom endpoint.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_custom_endpoint_request.GetCustomEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_custom_endpoint_response.GetCustomEndpointResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_custom_endpoint

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_custom_endpoint.get_custom_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_custom_endpoint_request.GetCustomEndpointRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_iot_managed_integrations.types.io_t_managed_integrations_resource_arn.IoTManagedIntegrationsResourceARN",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_tags_for_resource

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_custom_endpoint(
        self, *, config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None
    ) -> "aws_sdk_iot_managed_integrations.types.register_custom_endpoint_response.RegisterCustomEndpointResponse":
        """<p>Customers can request IoT managed integrations to manage the server trust for them or bring their own external server trusts for the custom domain. Returns an IoT managed integrations endpoint.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.register_custom_endpoint_request.RegisterCustomEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.register_custom_endpoint_response.RegisterCustomEndpointResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.register_custom_endpoint

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.register_custom_endpoint.register_custom_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.register_custom_endpoint_request.RegisterCustomEndpointRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_connector_event(
        self,
        connector_id: "aws_sdk_iot_managed_integrations.types.connector_id.ConnectorId",
        operation: "aws_sdk_iot_managed_integrations.types.connector_event_operation.ConnectorEventOperation",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        user_id: Optional[
            "aws_sdk_iot_managed_integrations.types.third_party_user_id.ThirdPartyUserId"
        ] = None,
        operation_version: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_event_operation_version.ConnectorEventOperationVersion"
        ] = None,
        status_code: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_event_status_code.ConnectorEventStatusCode"
        ] = None,
        message: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_event_message.ConnectorEventMessage"
        ] = None,
        device_discovery_id: Optional[
            "aws_sdk_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId"
        ] = None,
        connector_device_id: Optional[
            "aws_sdk_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
        ] = None,
        trace_id: Optional[
            "aws_sdk_iot_managed_integrations.types.trace_id.TraceId"
        ] = None,
        devices: Optional[
            "aws_sdk_iot_managed_integrations.types.devices.Devices"
        ] = None,
        matter_endpoint: Optional[
            "aws_sdk_iot_managed_integrations.types.matter_endpoint.MatterEndpoint"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.send_connector_event_response.SendConnectorEventResponse":
        r"""<p>Relays third-party device events for a connector such as a new device or a device state change event.</p>

        Args:
            connector_id: <p>The id of the connector between the third-party cloud provider and IoT managed integrations.</p>
            user_id: <p>The id of the third-party cloud provider.</p>
            operation: <p>The Open Connectivity Foundation (OCF) operation requested to be performed on the managed thing.</p> <note> <p>The field op can have a value of \"I\" or \"U\". The field \"cn\" will contain the capability types.</p> </note>
            operation_version: <p>The Open Connectivity Foundation (OCF) security specification version for the operation being requested on the managed thing. For more information, see <a href=\"https://openconnectivity.org/specs/OCF_Security_Specification_v1.0.0.pdf\">OCF Security Specification</a>.</p>
            status_code: <p>The status code of the Open Connectivity Foundation (OCF) operation being performed on the managed thing.</p>
            message: <p>The device state change event payload.</p> <p>This parameter will include the following three fields:</p> <ul> <li> <p> <code>uri</code>: <code>schema auc://&lt;PARTNER-DEVICE-ID&gt;/ResourcePath</code> (The <code>Resourcepath</code> corresponds to an OCF resource.)</p> </li> <li> <p> <code>op</code>: For device state changes, this field must populate as <code>n+d</code>.</p> </li> <li> <p> <code>cn</code>: The content depends on the OCF resource referenced in <code>ResourcePath</code>.</p> </li> </ul>
            device_discovery_id: <p>The id for the device discovery job.</p>
            connector_device_id: <p>The third-party device id as defined by the connector. This device id must not contain personal identifiable information (PII).</p> <note> <p>This parameter is used for cloud-to-cloud devices only.</p> </note>
            trace_id: <p>The trace request identifier. This is generated by IoT managed integrations and can be used to trace this command and its related operations in CloudWatch.</p>
            devices: <p>The list of devices.</p>
            matter_endpoint: <p>The device endpoint.</p>

        Examples:
            SendConnectorEvent happy path for device discovery

            >>> client.send_connector_event(connector_id='MockConnectorId', user_id='MockThirdPartyUserId', operation='DEVICE_DISCOVERY', operation_version='1.0', status_code=200, message='Sample ConnectorEventMessage', device_discovery_id='358275hbk3qr', devices=[{'ConnectorDeviceId': 'Mock-Connector-DeviceId-1', 'ConnectorDeviceName': 'Sample-User-device-1', 'CapabilityReport': {'version': '1.0.0', 'nodeId': '1', 'endpoints': [{'id': 'EP1', 'deviceTypes': ['Refrigerator'], 'clusters': [{'id': '0x0201', 'revision': 1, 'attributes': [{'id': '0x0000', 'value': 'exampleString'}, {'id': '0x0001'}, {'id': '0x0002'}], 'commands': ['0x00', '0x01'], 'events': []}]}]}}])
            SendConnectorEvent happy path for device command response

            >>> client.send_connector_event(connector_id='MockConnectorId', user_id='MockThirdPartyUserId', operation='DEVICE_COMMAND_RESPONSE', operation_version='1.0', status_code=200, message='Sample ConnectorEventMessage', trace_id='9b75f3839b6140f=_1', matter_endpoint={'id': '1', 'clusters': [{'id': '0x1003', 'attributes': {'0x0000': [73], '0x15570003': 'exampleString'}, 'commands': {'0x03': {}}}]})
            SendConnectorEvent happy path for device event

            >>> client.send_connector_event(connector_id='MockConnectorId', user_id='MockThirdPartyUserId', operation='DEVICE_EVENT', operation_version='1.0', status_code=200, message='Sample ConnectorEventMessage', trace_id='TraceId-Sample', matter_endpoint={'id': '1', 'clusters': [{'id': '0x1003', 'attributes': {'0x0000': 73}}]})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.send_connector_event_request.SendConnectorEventRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.send_connector_event_response.SendConnectorEventResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.send_connector_event

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.send_connector_event.send_connector_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.send_connector_event_request.SendConnectorEventRequest = {}  # type: ignore[typeddict-item]
        input_["connector_id"] = connector_id
        if user_id is not None:
            input_["user_id"] = user_id
        input_["operation"] = operation
        if operation_version is not None:
            input_["operation_version"] = operation_version
        if status_code is not None:
            input_["status_code"] = status_code
        if message is not None:
            input_["message"] = message
        if device_discovery_id is not None:
            input_["device_discovery_id"] = device_discovery_id
        if connector_device_id is not None:
            input_["connector_device_id"] = connector_device_id
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if devices is not None:
            input_["devices"] = devices
        if matter_endpoint is not None:
            input_["matter_endpoint"] = matter_endpoint

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_iot_managed_integrations.types.io_t_managed_integrations_resource_arn.IoTManagedIntegrationsResourceARN",
        tags: "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which to add tags.</p>
            tags: <p>A set of key/value pairs that are used to manage the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.tag_resource

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_iot_managed_integrations.types.io_t_managed_integrations_resource_arn.IoTManagedIntegrationsResourceARN",
        tag_keys: "aws_sdk_iot_managed_integrations.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>A list of tag keys to remove from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.untag_resource

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
