"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#IoTAutobahnControlPlane``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_iotfleetwise._auth._signers
import aws_sdk_iotfleetwise._auth._sigv4
from aws_sdk_iotfleetwise._auth._identity import Credentials
from aws_sdk_iotfleetwise._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_iotfleetwise._auth._zapros_handler import AuthMiddleware
from aws_sdk_iotfleetwise._pagination import resolve_path as _resolve_path
from aws_sdk_iotfleetwise._resources.io_t_autobahn_control_plane.campaign_resource import (
    CampaignResource,
)
from aws_sdk_iotfleetwise._resources.io_t_autobahn_control_plane.decoder_manifest_resource import (
    DecoderManifestResource,
)
from aws_sdk_iotfleetwise._resources.io_t_autobahn_control_plane.fleet_resource import (
    FleetResource,
)
from aws_sdk_iotfleetwise._resources.io_t_autobahn_control_plane.model_manifest_resource import (
    ModelManifestResource,
)
from aws_sdk_iotfleetwise._resources.io_t_autobahn_control_plane.signal_catalog_resource import (
    SignalCatalogResource,
)
from aws_sdk_iotfleetwise._resources.io_t_autobahn_control_plane.state_template_resource import (
    StateTemplateResource,
)
from aws_sdk_iotfleetwise._resources.io_t_autobahn_control_plane.vehicle_resource import (
    VehicleResource,
)
from aws_sdk_iotfleetwise._services._aws_config import aws_config
from aws_sdk_iotfleetwise._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.amazon_resource_name
    import aws_sdk_iotfleetwise.types.batch_create_vehicle_request
    import aws_sdk_iotfleetwise.types.batch_create_vehicle_response
    import aws_sdk_iotfleetwise.types.batch_update_vehicle_request
    import aws_sdk_iotfleetwise.types.batch_update_vehicle_response
    import aws_sdk_iotfleetwise.types.cloud_watch_log_delivery_options
    import aws_sdk_iotfleetwise.types.create_vehicle_request_items
    import aws_sdk_iotfleetwise.types.encryption_type
    import aws_sdk_iotfleetwise.types.get_encryption_configuration_request
    import aws_sdk_iotfleetwise.types.get_encryption_configuration_response
    import aws_sdk_iotfleetwise.types.get_logging_options_request
    import aws_sdk_iotfleetwise.types.get_logging_options_response
    import aws_sdk_iotfleetwise.types.get_register_account_status_request
    import aws_sdk_iotfleetwise.types.get_register_account_status_response
    import aws_sdk_iotfleetwise.types.get_vehicle_status_request
    import aws_sdk_iotfleetwise.types.get_vehicle_status_response
    import aws_sdk_iotfleetwise.types.iam_resources
    import aws_sdk_iotfleetwise.types.list_tags_for_resource_request
    import aws_sdk_iotfleetwise.types.list_tags_for_resource_response
    import aws_sdk_iotfleetwise.types.max_results
    import aws_sdk_iotfleetwise.types.next_token
    import aws_sdk_iotfleetwise.types.put_encryption_configuration_request
    import aws_sdk_iotfleetwise.types.put_encryption_configuration_response
    import aws_sdk_iotfleetwise.types.put_logging_options_request
    import aws_sdk_iotfleetwise.types.put_logging_options_response
    import aws_sdk_iotfleetwise.types.register_account_request
    import aws_sdk_iotfleetwise.types.register_account_response
    import aws_sdk_iotfleetwise.types.tag_key_list
    import aws_sdk_iotfleetwise.types.tag_list
    import aws_sdk_iotfleetwise.types.tag_resource_request
    import aws_sdk_iotfleetwise.types.tag_resource_response
    import aws_sdk_iotfleetwise.types.timestream_resources
    import aws_sdk_iotfleetwise.types.untag_resource_request
    import aws_sdk_iotfleetwise.types.untag_resource_response
    import aws_sdk_iotfleetwise.types.update_vehicle_request_items
    import aws_sdk_iotfleetwise.types.vehicle_name
    import aws_sdk_iotfleetwise.types.vehicle_status


class IoTFleetWiseClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class IoTFleetWiseClient:
    """A client for the ``IoTFleetWise`` service.

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
        self._config = IoTFleetWiseClientConfig(
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
        self.campaign_resource = CampaignResource(self)
        self.decoder_manifest_resource = DecoderManifestResource(self)
        self.fleet_resource = FleetResource(self)
        self.model_manifest_resource = ModelManifestResource(self)
        self.signal_catalog_resource = SignalCatalogResource(self)
        self.state_template_resource = StateTemplateResource(self)
        self.vehicle_resource = VehicleResource(self)

    def operation_options(
        self, config_overrides: Optional[IoTFleetWiseClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: IoTFleetWiseClientConfig = config_overrides or {}
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

    def batch_create_vehicle(
        self,
        vehicles: "aws_sdk_iotfleetwise.types.create_vehicle_request_items.createVehicleRequestItems",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.batch_create_vehicle_response.BatchCreateVehicleResponse":
        r"""<p> Creates a group, or batch, of vehicles. </p> <note> <p> You must specify a decoder manifest and a vehicle model (model manifest) for each vehicle. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-vehicles-cli.html\">Create multiple vehicles (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>. </p>

        Args:
            vehicles: <p> A list of information about each vehicle to create. For more information, see the API data type.</p>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.batch_create_vehicle_request.BatchCreateVehicleRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.batch_create_vehicle_response.BatchCreateVehicleResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.batch_create_vehicle

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.batch_create_vehicle.batch_create_vehicle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.batch_create_vehicle_request.BatchCreateVehicleRequest = {}  # type: ignore[typeddict-item]
        input_["vehicles"] = vehicles

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_vehicle(
        self,
        vehicles: "aws_sdk_iotfleetwise.types.update_vehicle_request_items.updateVehicleRequestItems",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.batch_update_vehicle_response.BatchUpdateVehicleResponse":
        r"""<p> Updates a group, or batch, of vehicles.</p> <note> <p> You must specify a decoder manifest and a vehicle model (model manifest) for each vehicle. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-vehicles-cli.html\">Update multiple vehicles (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>. </p>

        Args:
            vehicles: <p> A list of information about the vehicles to update. For more information, see the API data type.</p>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.batch_update_vehicle_request.BatchUpdateVehicleRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.batch_update_vehicle_response.BatchUpdateVehicleResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.batch_update_vehicle

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.batch_update_vehicle.batch_update_vehicle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.batch_update_vehicle_request.BatchUpdateVehicleRequest = {}  # type: ignore[typeddict-item]
        input_["vehicles"] = vehicles

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_encryption_configuration(
        self, *, config_overrides: Optional[IoTFleetWiseClientConfig] = None
    ) -> "aws_sdk_iotfleetwise.types.get_encryption_configuration_response.GetEncryptionConfigurationResponse":
        """<p>Retrieves the encryption configuration for resources and data in Amazon Web Services IoT FleetWise.</p>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.get_encryption_configuration_request.GetEncryptionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.get_encryption_configuration_response.GetEncryptionConfigurationResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_encryption_configuration

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_encryption_configuration.get_encryption_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.get_encryption_configuration_request.GetEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_logging_options(
        self, *, config_overrides: Optional[IoTFleetWiseClientConfig] = None
    ) -> "aws_sdk_iotfleetwise.types.get_logging_options_response.GetLoggingOptionsResponse":
        """<p>Retrieves the logging options.</p>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.get_logging_options_request.GetLoggingOptionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.get_logging_options_response.GetLoggingOptionsResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_logging_options

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_logging_options.get_logging_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.get_logging_options_request.GetLoggingOptionsRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_register_account_status(
        self, *, config_overrides: Optional[IoTFleetWiseClientConfig] = None
    ) -> "aws_sdk_iotfleetwise.types.get_register_account_status_response.GetRegisterAccountStatusResponse":
        r"""<p> Retrieves information about the status of registering your Amazon Web Services account, IAM, and Amazon Timestream resources so that Amazon Web Services IoT FleetWise can transfer your vehicle data to the Amazon Web Services Cloud. </p> <p>For more information, including step-by-step procedures, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/setting-up.html\">Setting up Amazon Web Services IoT FleetWise</a>. </p> <note> <p>This API operation doesn't require input parameters.</p> </note>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.get_register_account_status_request.GetRegisterAccountStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.get_register_account_status_response.GetRegisterAccountStatusResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_register_account_status

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_register_account_status.get_register_account_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.get_register_account_status_request.GetRegisterAccountStatusRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_vehicle_status(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotfleetwise.types.max_results.maxResults"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.get_vehicle_status_response.GetVehicleStatusResponse":
        """<p> Retrieves information about the status of campaigns, decoder manifests, or state templates associated with a vehicle.</p>

        Args:
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. This parameter is only supported for resources of type <code>CAMPAIGN</code>.</p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive. This parameter is only supported for resources of type <code>CAMPAIGN</code>.</p>
            vehicle_name: <p> The ID of the vehicle to retrieve information about. </p>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.get_vehicle_status_request.GetVehicleStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.get_vehicle_status_response.GetVehicleStatusResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_vehicle_status

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.get_vehicle_status.get_vehicle_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.get_vehicle_status_request.GetVehicleStatusRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["vehicle_name"] = vehicle_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_get_vehicle_status(
        self,
        vehicle_name: "aws_sdk_iotfleetwise.types.vehicle_name.vehicleName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        next_token: Optional["aws_sdk_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional[
            "aws_sdk_iotfleetwise.types.max_results.maxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_iotfleetwise.types.vehicle_status.VehicleStatus]":
        _token = next_token
        while True:
            _response = self.get_vehicle_status(
                vehicle_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("campaigns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_iotfleetwise.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags (metadata) you have assigned to the resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.list_tags_for_resource

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_encryption_configuration(
        self,
        encryption_type: "aws_sdk_iotfleetwise.types.encryption_type.EncryptionType",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        kms_key_id: Optional[str] = None,
    ) -> "aws_sdk_iotfleetwise.types.put_encryption_configuration_response.PutEncryptionConfigurationResponse":
        r"""<p>Creates or updates the encryption configuration. Amazon Web Services IoT FleetWise can encrypt your data and resources using an Amazon Web Services managed key. Or, you can use a KMS key that you own and manage. For more information, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/data-encryption.html\">Data encryption</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            kms_key_id: <p>The ID of the KMS key that is used for encryption.</p>
            encryption_type: <p>The type of encryption. Choose <code>KMS_BASED_ENCRYPTION</code> to use a KMS key or <code>FLEETWISE_DEFAULT_ENCRYPTION</code> to use an Amazon Web Services managed key.</p>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            aws_sdk_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.put_encryption_configuration_request.PutEncryptionConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.put_encryption_configuration_response.PutEncryptionConfigurationResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.put_encryption_configuration

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.put_encryption_configuration.put_encryption_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.put_encryption_configuration_request.PutEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        input_["encryption_type"] = encryption_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_logging_options(
        self,
        cloud_watch_log_delivery: "aws_sdk_iotfleetwise.types.cloud_watch_log_delivery_options.CloudWatchLogDeliveryOptions",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.put_logging_options_response.PutLoggingOptionsResponse":
        """<p>Creates or updates the logging option.</p>

        Args:
            cloud_watch_log_delivery: <p>Creates or updates the log delivery option to Amazon CloudWatch Logs.</p>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            aws_sdk_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.put_logging_options_request.PutLoggingOptionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.put_logging_options_response.PutLoggingOptionsResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.put_logging_options

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.put_logging_options.put_logging_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.put_logging_options_request.PutLoggingOptionsRequest = {}  # type: ignore[typeddict-item]
        input_["cloud_watch_log_delivery"] = cloud_watch_log_delivery

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_account(
        self,
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        timestream_resources: Optional[
            "aws_sdk_iotfleetwise.types.timestream_resources.TimestreamResources"
        ] = None,
        iam_resources: Optional[
            "aws_sdk_iotfleetwise.types.iam_resources.IamResources"
        ] = None,
    ) -> "aws_sdk_iotfleetwise.types.register_account_response.RegisterAccountResponse":
        r"""<important> <p>This API operation contains deprecated parameters. Register your account again without the Timestream resources parameter so that Amazon Web Services IoT FleetWise can remove the Timestream metadata stored. You should then pass the data destination into the <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateCampaign.html\">CreateCampaign</a> API operation.</p> <p>You must delete any existing campaigns that include an empty data destination before you register your account again. For more information, see the <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DeleteCampaign.html\">DeleteCampaign</a> API operation.</p> <p>If you want to delete the Timestream inline policy from the service-linked role, such as to mitigate an overly permissive policy, you must first delete any existing campaigns. Then delete the service-linked role and register your account again to enable CloudWatch metrics. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServiceLinkedRole.html\">DeleteServiceLinkedRole</a> in the <i>Identity and Access Management API Reference</i>.</p> </important> <p>Registers your Amazon Web Services account, IAM, and Amazon Timestream resources so Amazon Web Services IoT FleetWise can transfer your vehicle data to the Amazon Web Services Cloud. For more information, including step-by-step procedures, see <a href=\"https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/setting-up.html\">Setting up Amazon Web Services IoT FleetWise</a>. </p> <note> <p>An Amazon Web Services account is <b>not</b> the same thing as a \"user.\" An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_identity-management.html#intro-identity-users\">Amazon Web Services user</a> is an identity that you create using Identity and Access Management (IAM) and takes the form of either an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html\">IAM user</a> or an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html\">IAM role, both with credentials</a>. A single Amazon Web Services account can, and typically does, contain many users and roles.</p> </note>

        Args:
            iam_resources: <p>The IAM resource that allows Amazon Web Services IoT FleetWise to send data to Amazon Timestream.</p>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            aws_sdk_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.register_account_request.RegisterAccountRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.register_account_response.RegisterAccountResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.register_account

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.register_account.register_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.register_account_request.RegisterAccountRequest = {}  # type: ignore[typeddict-item]
        if timestream_resources is not None:
            input_["timestream_resources"] = timestream_resources
        if iam_resources is not None:
            input_["iam_resources"] = iam_resources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_iotfleetwise.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_iotfleetwise.types.tag_list.TagList",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.tag_resource_response.TagResourceResponse":
        """<p>Adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>The new or modified tags for the resource.</p>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.tag_resource

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_iotfleetwise.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_iotfleetwise.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "aws_sdk_iotfleetwise.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the given tags (metadata) from the resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>A list of the keys of the tags to be removed from the resource.</p>

        Raises:
            aws_sdk_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            aws_sdk_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            aws_sdk_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            aws_sdk_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            aws_sdk_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iotfleetwise.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_iotfleetwise.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.untag_resource

            output, http_response = (
                aws_sdk_iotfleetwise._operations.io_t_autobahn_control_plane.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotfleetwise.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
