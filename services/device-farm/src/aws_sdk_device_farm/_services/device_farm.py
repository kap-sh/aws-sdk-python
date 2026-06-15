"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceFarm_20150623``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_device_farm._auth._signers
import aws_sdk_device_farm._auth._sigv4
from aws_sdk_device_farm._auth._identity import Credentials
from aws_sdk_device_farm._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_device_farm._auth._zapros_handler import AuthMiddleware
from aws_sdk_device_farm._pagination import resolve_path as _resolve_path
from aws_sdk_device_farm._services._aws_config import aws_config
from aws_sdk_device_farm._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.amazon_role_resource_name
    import aws_sdk_device_farm.types.artifact
    import aws_sdk_device_farm.types.artifact_category
    import aws_sdk_device_farm.types.boolean
    import aws_sdk_device_farm.types.content_type
    import aws_sdk_device_farm.types.create_device_pool_request
    import aws_sdk_device_farm.types.create_device_pool_result
    import aws_sdk_device_farm.types.create_instance_profile_request
    import aws_sdk_device_farm.types.create_instance_profile_result
    import aws_sdk_device_farm.types.create_network_profile_request
    import aws_sdk_device_farm.types.create_network_profile_result
    import aws_sdk_device_farm.types.create_project_request
    import aws_sdk_device_farm.types.create_project_result
    import aws_sdk_device_farm.types.create_remote_access_session_configuration
    import aws_sdk_device_farm.types.create_remote_access_session_request
    import aws_sdk_device_farm.types.create_remote_access_session_result
    import aws_sdk_device_farm.types.create_test_grid_project_request
    import aws_sdk_device_farm.types.create_test_grid_project_result
    import aws_sdk_device_farm.types.create_test_grid_url_request
    import aws_sdk_device_farm.types.create_test_grid_url_result
    import aws_sdk_device_farm.types.create_upload_request
    import aws_sdk_device_farm.types.create_upload_result
    import aws_sdk_device_farm.types.create_vpce_configuration_request
    import aws_sdk_device_farm.types.create_vpce_configuration_result
    import aws_sdk_device_farm.types.date_time
    import aws_sdk_device_farm.types.delete_device_pool_request
    import aws_sdk_device_farm.types.delete_device_pool_result
    import aws_sdk_device_farm.types.delete_instance_profile_request
    import aws_sdk_device_farm.types.delete_instance_profile_result
    import aws_sdk_device_farm.types.delete_network_profile_request
    import aws_sdk_device_farm.types.delete_network_profile_result
    import aws_sdk_device_farm.types.delete_project_request
    import aws_sdk_device_farm.types.delete_project_result
    import aws_sdk_device_farm.types.delete_remote_access_session_request
    import aws_sdk_device_farm.types.delete_remote_access_session_result
    import aws_sdk_device_farm.types.delete_run_request
    import aws_sdk_device_farm.types.delete_run_result
    import aws_sdk_device_farm.types.delete_test_grid_project_request
    import aws_sdk_device_farm.types.delete_test_grid_project_result
    import aws_sdk_device_farm.types.delete_upload_request
    import aws_sdk_device_farm.types.delete_upload_result
    import aws_sdk_device_farm.types.delete_vpce_configuration_request
    import aws_sdk_device_farm.types.delete_vpce_configuration_result
    import aws_sdk_device_farm.types.device
    import aws_sdk_device_farm.types.device_farm_arn
    import aws_sdk_device_farm.types.device_filters
    import aws_sdk_device_farm.types.device_pool
    import aws_sdk_device_farm.types.device_pool_type
    import aws_sdk_device_farm.types.device_selection_configuration
    import aws_sdk_device_farm.types.environment_variables
    import aws_sdk_device_farm.types.execution_configuration
    import aws_sdk_device_farm.types.execution_result
    import aws_sdk_device_farm.types.get_account_settings_request
    import aws_sdk_device_farm.types.get_account_settings_result
    import aws_sdk_device_farm.types.get_device_instance_request
    import aws_sdk_device_farm.types.get_device_instance_result
    import aws_sdk_device_farm.types.get_device_pool_compatibility_request
    import aws_sdk_device_farm.types.get_device_pool_compatibility_result
    import aws_sdk_device_farm.types.get_device_pool_request
    import aws_sdk_device_farm.types.get_device_pool_result
    import aws_sdk_device_farm.types.get_device_request
    import aws_sdk_device_farm.types.get_device_result
    import aws_sdk_device_farm.types.get_instance_profile_request
    import aws_sdk_device_farm.types.get_instance_profile_result
    import aws_sdk_device_farm.types.get_job_request
    import aws_sdk_device_farm.types.get_job_result
    import aws_sdk_device_farm.types.get_network_profile_request
    import aws_sdk_device_farm.types.get_network_profile_result
    import aws_sdk_device_farm.types.get_offering_status_request
    import aws_sdk_device_farm.types.get_offering_status_result
    import aws_sdk_device_farm.types.get_project_request
    import aws_sdk_device_farm.types.get_project_result
    import aws_sdk_device_farm.types.get_remote_access_session_request
    import aws_sdk_device_farm.types.get_remote_access_session_result
    import aws_sdk_device_farm.types.get_run_request
    import aws_sdk_device_farm.types.get_run_result
    import aws_sdk_device_farm.types.get_suite_request
    import aws_sdk_device_farm.types.get_suite_result
    import aws_sdk_device_farm.types.get_test_grid_project_request
    import aws_sdk_device_farm.types.get_test_grid_project_result
    import aws_sdk_device_farm.types.get_test_grid_session_request
    import aws_sdk_device_farm.types.get_test_grid_session_result
    import aws_sdk_device_farm.types.get_test_request
    import aws_sdk_device_farm.types.get_test_result
    import aws_sdk_device_farm.types.get_upload_request
    import aws_sdk_device_farm.types.get_upload_result
    import aws_sdk_device_farm.types.get_vpce_configuration_request
    import aws_sdk_device_farm.types.get_vpce_configuration_result
    import aws_sdk_device_farm.types.install_to_remote_access_session_request
    import aws_sdk_device_farm.types.install_to_remote_access_session_result
    import aws_sdk_device_farm.types.instance_labels
    import aws_sdk_device_farm.types.integer
    import aws_sdk_device_farm.types.interaction_mode
    import aws_sdk_device_farm.types.job
    import aws_sdk_device_farm.types.job_timeout_minutes
    import aws_sdk_device_farm.types.list_artifacts_request
    import aws_sdk_device_farm.types.list_artifacts_result
    import aws_sdk_device_farm.types.list_device_instances_request
    import aws_sdk_device_farm.types.list_device_instances_result
    import aws_sdk_device_farm.types.list_device_pools_request
    import aws_sdk_device_farm.types.list_device_pools_result
    import aws_sdk_device_farm.types.list_devices_request
    import aws_sdk_device_farm.types.list_devices_result
    import aws_sdk_device_farm.types.list_instance_profiles_request
    import aws_sdk_device_farm.types.list_instance_profiles_result
    import aws_sdk_device_farm.types.list_jobs_request
    import aws_sdk_device_farm.types.list_jobs_result
    import aws_sdk_device_farm.types.list_network_profiles_request
    import aws_sdk_device_farm.types.list_network_profiles_result
    import aws_sdk_device_farm.types.list_offering_promotions_request
    import aws_sdk_device_farm.types.list_offering_promotions_result
    import aws_sdk_device_farm.types.list_offering_transactions_request
    import aws_sdk_device_farm.types.list_offering_transactions_result
    import aws_sdk_device_farm.types.list_offerings_request
    import aws_sdk_device_farm.types.list_offerings_result
    import aws_sdk_device_farm.types.list_projects_request
    import aws_sdk_device_farm.types.list_projects_result
    import aws_sdk_device_farm.types.list_remote_access_sessions_request
    import aws_sdk_device_farm.types.list_remote_access_sessions_result
    import aws_sdk_device_farm.types.list_runs_request
    import aws_sdk_device_farm.types.list_runs_result
    import aws_sdk_device_farm.types.list_samples_request
    import aws_sdk_device_farm.types.list_samples_result
    import aws_sdk_device_farm.types.list_suites_request
    import aws_sdk_device_farm.types.list_suites_result
    import aws_sdk_device_farm.types.list_tags_for_resource_request
    import aws_sdk_device_farm.types.list_tags_for_resource_response
    import aws_sdk_device_farm.types.list_test_grid_projects_request
    import aws_sdk_device_farm.types.list_test_grid_projects_result
    import aws_sdk_device_farm.types.list_test_grid_session_actions_request
    import aws_sdk_device_farm.types.list_test_grid_session_actions_result
    import aws_sdk_device_farm.types.list_test_grid_session_artifacts_request
    import aws_sdk_device_farm.types.list_test_grid_session_artifacts_result
    import aws_sdk_device_farm.types.list_test_grid_sessions_request
    import aws_sdk_device_farm.types.list_test_grid_sessions_result
    import aws_sdk_device_farm.types.list_tests_request
    import aws_sdk_device_farm.types.list_tests_result
    import aws_sdk_device_farm.types.list_unique_problems_request
    import aws_sdk_device_farm.types.list_unique_problems_result
    import aws_sdk_device_farm.types.list_uploads_request
    import aws_sdk_device_farm.types.list_uploads_result
    import aws_sdk_device_farm.types.list_vpce_configurations_request
    import aws_sdk_device_farm.types.list_vpce_configurations_result
    import aws_sdk_device_farm.types.long
    import aws_sdk_device_farm.types.max_page_size
    import aws_sdk_device_farm.types.message
    import aws_sdk_device_farm.types.name
    import aws_sdk_device_farm.types.network_profile_type
    import aws_sdk_device_farm.types.offering
    import aws_sdk_device_farm.types.offering_identifier
    import aws_sdk_device_farm.types.offering_promotion_identifier
    import aws_sdk_device_farm.types.offering_transaction
    import aws_sdk_device_farm.types.package_ids
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.percent_integer
    import aws_sdk_device_farm.types.project
    import aws_sdk_device_farm.types.purchase_offering_request
    import aws_sdk_device_farm.types.purchase_offering_result
    import aws_sdk_device_farm.types.renew_offering_request
    import aws_sdk_device_farm.types.renew_offering_result
    import aws_sdk_device_farm.types.resource_description
    import aws_sdk_device_farm.types.resource_id
    import aws_sdk_device_farm.types.resource_name
    import aws_sdk_device_farm.types.rules
    import aws_sdk_device_farm.types.run
    import aws_sdk_device_farm.types.sample
    import aws_sdk_device_farm.types.schedule_run_configuration
    import aws_sdk_device_farm.types.schedule_run_request
    import aws_sdk_device_farm.types.schedule_run_result
    import aws_sdk_device_farm.types.schedule_run_test
    import aws_sdk_device_farm.types.service_dns_name
    import aws_sdk_device_farm.types.stop_job_request
    import aws_sdk_device_farm.types.stop_job_result
    import aws_sdk_device_farm.types.stop_remote_access_session_request
    import aws_sdk_device_farm.types.stop_remote_access_session_result
    import aws_sdk_device_farm.types.stop_run_request
    import aws_sdk_device_farm.types.stop_run_result
    import aws_sdk_device_farm.types.suite
    import aws_sdk_device_farm.types.tag_key_list
    import aws_sdk_device_farm.types.tag_list
    import aws_sdk_device_farm.types.tag_resource_request
    import aws_sdk_device_farm.types.tag_resource_response
    import aws_sdk_device_farm.types.test
    import aws_sdk_device_farm.types.test_grid_session_artifact_category
    import aws_sdk_device_farm.types.test_grid_session_status
    import aws_sdk_device_farm.types.test_grid_url_expires_in_seconds_input
    import aws_sdk_device_farm.types.test_grid_vpc_config
    import aws_sdk_device_farm.types.test_type
    import aws_sdk_device_farm.types.unique_problems
    import aws_sdk_device_farm.types.untag_resource_request
    import aws_sdk_device_farm.types.untag_resource_response
    import aws_sdk_device_farm.types.update_device_instance_request
    import aws_sdk_device_farm.types.update_device_instance_result
    import aws_sdk_device_farm.types.update_device_pool_request
    import aws_sdk_device_farm.types.update_device_pool_result
    import aws_sdk_device_farm.types.update_instance_profile_request
    import aws_sdk_device_farm.types.update_instance_profile_result
    import aws_sdk_device_farm.types.update_network_profile_request
    import aws_sdk_device_farm.types.update_network_profile_result
    import aws_sdk_device_farm.types.update_project_request
    import aws_sdk_device_farm.types.update_project_result
    import aws_sdk_device_farm.types.update_test_grid_project_request
    import aws_sdk_device_farm.types.update_test_grid_project_result
    import aws_sdk_device_farm.types.update_upload_request
    import aws_sdk_device_farm.types.update_upload_result
    import aws_sdk_device_farm.types.update_vpce_configuration_request
    import aws_sdk_device_farm.types.update_vpce_configuration_result
    import aws_sdk_device_farm.types.upload
    import aws_sdk_device_farm.types.upload_type
    import aws_sdk_device_farm.types.vpc_config
    import aws_sdk_device_farm.types.vpce_configuration_description
    import aws_sdk_device_farm.types.vpce_configuration_name
    import aws_sdk_device_farm.types.vpce_service_name


class DeviceFarmClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class DeviceFarmClient:
    """A client for the ``DeviceFarm`` service.

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
        self._config = DeviceFarmClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[DeviceFarmClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DeviceFarmClientConfig = config_overrides or {}
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

    def create_device_pool(
        self,
        project_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        name: "aws_sdk_device_farm.types.name.Name",
        rules: "aws_sdk_device_farm.types.rules.Rules",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        description: Optional["aws_sdk_device_farm.types.message.Message"] = None,
        max_devices: Optional["aws_sdk_device_farm.types.integer.Integer"] = None,
    ) -> "aws_sdk_device_farm.types.create_device_pool_result.CreateDevicePoolResult":
        """<p>Creates a device pool.</p>

        Args:
            project_arn: <p>The ARN of the project for the device pool.</p>
            name: <p>The device pool's name.</p>
            description: <p>The device pool's description.</p>
            rules: <p>The device pool's rules.</p>
            max_devices: <p>The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the <code>rules</code> parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.</p> <p>By specifying the maximum number of devices, you can control the costs that you incur by running tests.</p>

        Examples:
            To create a new device pool
            The following example creates a new device pool named MyDevicePool inside an existing project.

            >>> client.create_device_pool(project_arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456', name='MyDevicePool', description='My Android devices', rules=[])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.create_device_pool_request.CreateDevicePoolRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.create_device_pool_result.CreateDevicePoolResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.create_device_pool

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.create_device_pool.create_device_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.create_device_pool_request.CreateDevicePoolRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["rules"] = rules
        if max_devices is not None:
            input_["max_devices"] = max_devices

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_instance_profile(
        self,
        name: "aws_sdk_device_farm.types.name.Name",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        description: Optional["aws_sdk_device_farm.types.message.Message"] = None,
        package_cleanup: Optional["aws_sdk_device_farm.types.boolean.Boolean"] = None,
        exclude_app_packages_from_cleanup: Optional[
            "aws_sdk_device_farm.types.package_ids.PackageIds"
        ] = None,
        reboot_after_use: Optional["aws_sdk_device_farm.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_device_farm.types.create_instance_profile_result.CreateInstanceProfileResult":
        """<p>Creates a profile that can be applied to one or more private fleet device instances.</p>

        Args:
            name: <p>The name of your instance profile.</p>
            description: <p>The description of your instance profile.</p>
            package_cleanup: <p>When set to <code>true</code>, Device Farm removes app packages after a test run. The default value is <code>false</code> for private devices.</p>
            exclude_app_packages_from_cleanup: <p>An array of strings that specifies the list of app packages that should not be cleaned up from the device after a test run.</p> <p>The list of packages is considered only if you set <code>packageCleanup</code> to <code>true</code>.</p>
            reboot_after_use: <p>When set to <code>true</code>, Device Farm reboots the instance after a test run. The default value is <code>true</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.create_instance_profile_request.CreateInstanceProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.create_instance_profile_result.CreateInstanceProfileResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.create_instance_profile

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.create_instance_profile.create_instance_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.create_instance_profile_request.CreateInstanceProfileRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if package_cleanup is not None:
            input_["package_cleanup"] = package_cleanup
        if exclude_app_packages_from_cleanup is not None:
            input_["exclude_app_packages_from_cleanup"] = (
                exclude_app_packages_from_cleanup
            )
        if reboot_after_use is not None:
            input_["reboot_after_use"] = reboot_after_use

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_network_profile(
        self,
        project_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        name: "aws_sdk_device_farm.types.name.Name",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        description: Optional["aws_sdk_device_farm.types.message.Message"] = None,
        type: Optional[
            "aws_sdk_device_farm.types.network_profile_type.NetworkProfileType"
        ] = None,
        uplink_bandwidth_bits: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        downlink_bandwidth_bits: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        uplink_delay_ms: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        downlink_delay_ms: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        uplink_jitter_ms: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        downlink_jitter_ms: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        uplink_loss_percent: Optional[
            "aws_sdk_device_farm.types.percent_integer.PercentInteger"
        ] = None,
        downlink_loss_percent: Optional[
            "aws_sdk_device_farm.types.percent_integer.PercentInteger"
        ] = None,
    ) -> "aws_sdk_device_farm.types.create_network_profile_result.CreateNetworkProfileResult":
        """<p>Creates a network profile.</p>

        Args:
            project_arn: <p>The Amazon Resource Name (ARN) of the project for which you want to create a network profile.</p>
            name: <p>The name for the new network profile.</p>
            description: <p>The description of the network profile.</p>
            type: <p>The type of network profile to create. Valid values are listed here.</p>
            uplink_bandwidth_bits: <p>The data throughput rate in bits per second, as an integer from 0 to 104857600.</p>
            downlink_bandwidth_bits: <p>The data throughput rate in bits per second, as an integer from 0 to 104857600.</p>
            uplink_delay_ms: <p>Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.</p>
            downlink_delay_ms: <p>Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.</p>
            uplink_jitter_ms: <p>Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.</p>
            downlink_jitter_ms: <p>Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.</p>
            uplink_loss_percent: <p>Proportion of transmitted packets that fail to arrive from 0 to 100 percent.</p>
            downlink_loss_percent: <p>Proportion of received packets that fail to arrive from 0 to 100 percent.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.create_network_profile_request.CreateNetworkProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.create_network_profile_result.CreateNetworkProfileResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.create_network_profile

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.create_network_profile.create_network_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.create_network_profile_request.CreateNetworkProfileRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if uplink_bandwidth_bits is not None:
            input_["uplink_bandwidth_bits"] = uplink_bandwidth_bits
        if downlink_bandwidth_bits is not None:
            input_["downlink_bandwidth_bits"] = downlink_bandwidth_bits
        if uplink_delay_ms is not None:
            input_["uplink_delay_ms"] = uplink_delay_ms
        if downlink_delay_ms is not None:
            input_["downlink_delay_ms"] = downlink_delay_ms
        if uplink_jitter_ms is not None:
            input_["uplink_jitter_ms"] = uplink_jitter_ms
        if downlink_jitter_ms is not None:
            input_["downlink_jitter_ms"] = downlink_jitter_ms
        if uplink_loss_percent is not None:
            input_["uplink_loss_percent"] = uplink_loss_percent
        if downlink_loss_percent is not None:
            input_["downlink_loss_percent"] = downlink_loss_percent

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_project(
        self,
        name: "aws_sdk_device_farm.types.name.Name",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        default_job_timeout_minutes: Optional[
            "aws_sdk_device_farm.types.job_timeout_minutes.JobTimeoutMinutes"
        ] = None,
        vpc_config: Optional["aws_sdk_device_farm.types.vpc_config.VpcConfig"] = None,
        environment_variables: Optional[
            "aws_sdk_device_farm.types.environment_variables.EnvironmentVariables"
        ] = None,
        execution_role_arn: Optional[
            "aws_sdk_device_farm.types.amazon_role_resource_name.AmazonRoleResourceName"
        ] = None,
    ) -> "aws_sdk_device_farm.types.create_project_result.CreateProjectResult":
        r"""<p>Creates a project.</p>

        Args:
            name: <p>The project's name.</p>
            default_job_timeout_minutes: <p>Sets the execution timeout value (in minutes) for a project. All test runs in this project use the specified execution timeout value unless overridden when scheduling a run.</p>
            vpc_config: <p>The VPC security groups and subnets that are attached to a project.</p>
            environment_variables: <p> A set of environment variables which are used by default for all runs in the project. These environment variables are applied to the test run during the execution of a test spec file. </p> <p> For more information about using test spec files, please see <a href=\"https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments.html\">Custom test environments </a> in <i>AWS Device Farm.</i> </p>
            execution_role_arn: <p>An IAM role to be assumed by the test host for all runs in the project.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.create_project_request.CreateProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.create_project_result.CreateProjectResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.create_project

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.create_project.create_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.create_project_request.CreateProjectRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if default_job_timeout_minutes is not None:
            input_["default_job_timeout_minutes"] = default_job_timeout_minutes
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_remote_access_session(
        self,
        project_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        device_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        app_arn: Optional[
            "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        instance_arn: Optional[
            "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        name: Optional["aws_sdk_device_farm.types.name.Name"] = None,
        configuration: Optional[
            "aws_sdk_device_farm.types.create_remote_access_session_configuration.CreateRemoteAccessSessionConfiguration"
        ] = None,
        interaction_mode: Optional[
            "aws_sdk_device_farm.types.interaction_mode.InteractionMode"
        ] = None,
        skip_app_resign: Optional["aws_sdk_device_farm.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_device_farm.types.create_remote_access_session_result.CreateRemoteAccessSessionResult":
        r"""<p>Specifies and starts a remote access session.</p>

        Args:
            project_arn: <p>The Amazon Resource Name (ARN) of the project for which you want to create a remote access session.</p>
            device_arn: <p>The ARN of the device for which you want to create a remote access session.</p>
            app_arn: <p>The Amazon Resource Name (ARN) of the app to create the remote access session.</p>
            instance_arn: <p>The Amazon Resource Name (ARN) of the device instance for which you want to create a remote access session.</p>
            name: <p>The name of the remote access session to create.</p>
            configuration: <p>The configuration information for the remote access session request.</p>
            interaction_mode: <p>The interaction mode of the remote access session. Changing the interactive mode of remote access sessions is no longer available.</p>
            skip_app_resign: <p>When set to <code>true</code>, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.</p> <p>For more information on how Device Farm modifies your uploads during tests, see <a href=\"http://aws.amazon.com/device-farm/faqs/\">Do you modify my app?</a> </p>

        Examples:
            To create a remote access session
            The following example creates a remote access session named MySession.

            >>> client.create_remote_access_session(project_arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456', device_arn='arn:aws:devicefarm:us-west-2::device:123EXAMPLE', name='MySession', configuration={'billingMethod': 'METERED'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.create_remote_access_session_request.CreateRemoteAccessSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.create_remote_access_session_result.CreateRemoteAccessSessionResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.create_remote_access_session

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.create_remote_access_session.create_remote_access_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.create_remote_access_session_request.CreateRemoteAccessSessionRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        input_["device_arn"] = device_arn
        if app_arn is not None:
            input_["app_arn"] = app_arn
        if instance_arn is not None:
            input_["instance_arn"] = instance_arn
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration
        if interaction_mode is not None:
            input_["interaction_mode"] = interaction_mode
        if skip_app_resign is not None:
            input_["skip_app_resign"] = skip_app_resign

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_test_grid_project(
        self,
        name: "aws_sdk_device_farm.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        description: Optional[
            "aws_sdk_device_farm.types.resource_description.ResourceDescription"
        ] = None,
        vpc_config: Optional[
            "aws_sdk_device_farm.types.test_grid_vpc_config.TestGridVpcConfig"
        ] = None,
    ) -> "aws_sdk_device_farm.types.create_test_grid_project_result.CreateTestGridProjectResult":
        """<p>Creates a Selenium testing project. Projects are used to track <a>TestGridSession</a> instances.</p>

        Args:
            name: <p>Human-readable name of the Selenium testing project.</p>
            description: <p>Human-readable description of the project.</p>
            vpc_config: <p>The VPC security groups and subnets that are attached to a project.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.create_test_grid_project_request.CreateTestGridProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.create_test_grid_project_result.CreateTestGridProjectResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.create_test_grid_project

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.create_test_grid_project.create_test_grid_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.create_test_grid_project_request.CreateTestGridProjectRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_test_grid_url(
        self,
        project_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn",
        expires_in_seconds: "aws_sdk_device_farm.types.test_grid_url_expires_in_seconds_input.TestGridUrlExpiresInSecondsInput",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> (
        "aws_sdk_device_farm.types.create_test_grid_url_result.CreateTestGridUrlResult"
    ):
        """<p>Creates a signed, short-term URL that can be passed to a Selenium <code>RemoteWebDriver</code> constructor.</p>

        Args:
            project_arn: <p>ARN (from <a>CreateTestGridProject</a> or <a>ListTestGridProjects</a>) to associate with the short-term URL. </p>
            expires_in_seconds: <p>Lifetime, in seconds, of the URL.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.create_test_grid_url_request.CreateTestGridUrlRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.create_test_grid_url_result.CreateTestGridUrlResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.create_test_grid_url

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.create_test_grid_url.create_test_grid_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.create_test_grid_url_request.CreateTestGridUrlRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        input_["expires_in_seconds"] = expires_in_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_upload(
        self,
        project_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        name: "aws_sdk_device_farm.types.name.Name",
        type: "aws_sdk_device_farm.types.upload_type.UploadType",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        content_type: Optional[
            "aws_sdk_device_farm.types.content_type.ContentType"
        ] = None,
    ) -> "aws_sdk_device_farm.types.create_upload_result.CreateUploadResult":
        """<p>Uploads an app or test scripts.</p>

        Args:
            project_arn: <p>The ARN of the project for the upload.</p>
            name: <p>The upload's file name. The name should not contain any forward slashes (<code>/</code>). If you are uploading an iOS app, the file name must end with the <code>.ipa</code> extension. If you are uploading an Android app, the file name must end with the <code>.apk</code> extension. For all others, the file name must end with the <code>.zip</code> file extension.</p>
            type: <p>The upload's upload type.</p> <p>Must be one of the following values:</p> <ul> <li> <p>ANDROID_APP</p> </li> <li> <p>IOS_APP</p> </li> <li> <p>WEB_APP</p> </li> <li> <p>EXTERNAL_DATA</p> </li> <li> <p>APPIUM_JAVA_JUNIT_TEST_PACKAGE</p> </li> <li> <p>APPIUM_JAVA_TESTNG_TEST_PACKAGE</p> </li> <li> <p>APPIUM_PYTHON_TEST_PACKAGE</p> </li> <li> <p>APPIUM_NODE_TEST_PACKAGE</p> </li> <li> <p>APPIUM_RUBY_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_PYTHON_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_NODE_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_RUBY_TEST_PACKAGE</p> </li> <li> <p>INSTRUMENTATION_TEST_PACKAGE</p> </li> <li> <p>XCTEST_TEST_PACKAGE</p> </li> <li> <p>XCTEST_UI_TEST_PACKAGE</p> </li> <li> <p>APPIUM_JAVA_JUNIT_TEST_SPEC</p> </li> <li> <p>APPIUM_JAVA_TESTNG_TEST_SPEC</p> </li> <li> <p>APPIUM_PYTHON_TEST_SPEC</p> </li> <li> <p>APPIUM_NODE_TEST_SPEC</p> </li> <li> <p>APPIUM_RUBY_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_PYTHON_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_NODE_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_RUBY_TEST_SPEC</p> </li> <li> <p>INSTRUMENTATION_TEST_SPEC</p> </li> <li> <p>XCTEST_UI_TEST_SPEC</p> </li> </ul> <p> If you call <code>CreateUpload</code> with <code>WEB_APP</code> specified, AWS Device Farm throws an <code>ArgumentException</code> error.</p>
            content_type: <p>The upload's content type (for example, <code>application/octet-stream</code>).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.create_upload_request.CreateUploadRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.create_upload_result.CreateUploadResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.create_upload

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.create_upload.create_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.create_upload_request.CreateUploadRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        input_["name"] = name
        input_["type"] = type
        if content_type is not None:
            input_["content_type"] = content_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_vpce_configuration(
        self,
        vpce_configuration_name: "aws_sdk_device_farm.types.vpce_configuration_name.VPCEConfigurationName",
        vpce_service_name: "aws_sdk_device_farm.types.vpce_service_name.VPCEServiceName",
        service_dns_name: "aws_sdk_device_farm.types.service_dns_name.ServiceDnsName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        vpce_configuration_description: Optional[
            "aws_sdk_device_farm.types.vpce_configuration_description.VPCEConfigurationDescription"
        ] = None,
    ) -> "aws_sdk_device_farm.types.create_vpce_configuration_result.CreateVPCEConfigurationResult":
        """<p>Creates a configuration record in Device Farm for your Amazon Virtual Private Cloud (VPC) endpoint.</p>

        Args:
            vpce_configuration_name: <p>The friendly name you give to your VPC endpoint configuration, to manage your configurations more easily.</p>
            vpce_service_name: <p>The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.</p>
            service_dns_name: <p>The DNS name of the service running in your VPC that you want Device Farm to test.</p>
            vpce_configuration_description: <p>An optional description that provides details about your VPC endpoint configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.create_vpce_configuration_request.CreateVPCEConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.create_vpce_configuration_result.CreateVPCEConfigurationResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.create_vpce_configuration

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.create_vpce_configuration.create_vpce_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.create_vpce_configuration_request.CreateVPCEConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["vpce_configuration_name"] = vpce_configuration_name
        input_["vpce_service_name"] = vpce_service_name
        input_["service_dns_name"] = service_dns_name
        if vpce_configuration_description is not None:
            input_["vpce_configuration_description"] = vpce_configuration_description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_device_pool(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.delete_device_pool_result.DeleteDevicePoolResult":
        """<p>Deletes a device pool given the pool ARN. Does not allow deletion of curated pools owned by the system.</p>

        Args:
            arn: <p>Represents the Amazon Resource Name (ARN) of the Device Farm device pool to delete.</p>

        Examples:
            To delete a device pool
            The following example deletes a specific device pool.

            >>> client.delete_device_pool(arn='arn:aws:devicefarm:us-west-2::devicepool:123-456-EXAMPLE-GUID')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.delete_device_pool_request.DeleteDevicePoolRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.delete_device_pool_result.DeleteDevicePoolResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.delete_device_pool

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.delete_device_pool.delete_device_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.delete_device_pool_request.DeleteDevicePoolRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_instance_profile(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.delete_instance_profile_result.DeleteInstanceProfileResult":
        """<p>Deletes a profile that can be applied to one or more private device instances.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the instance profile you are requesting to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.delete_instance_profile_request.DeleteInstanceProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.delete_instance_profile_result.DeleteInstanceProfileResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.delete_instance_profile

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.delete_instance_profile.delete_instance_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.delete_instance_profile_request.DeleteInstanceProfileRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_network_profile(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.delete_network_profile_result.DeleteNetworkProfileResult":
        """<p>Deletes a network profile.</p>

        Args:
            arn: <p>The ARN of the network profile to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.delete_network_profile_request.DeleteNetworkProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.delete_network_profile_result.DeleteNetworkProfileResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.delete_network_profile

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.delete_network_profile.delete_network_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.delete_network_profile_request.DeleteNetworkProfileRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_project(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.delete_project_result.DeleteProjectResult":
        """<p>Deletes an AWS Device Farm project, given the project ARN. You cannot delete a project if it has an active run or session.</p> <important> <p>You cannot undo this operation.</p> </important>

        Args:
            arn: <p>Represents the Amazon Resource Name (ARN) of the Device Farm project to delete.</p>

        Examples:
            To delete a project
            The following example deletes a specific project.

            >>> client.delete_project(arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.delete_project_request.DeleteProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.delete_project_result.DeleteProjectResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.delete_project

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.delete_project.delete_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.delete_project_request.DeleteProjectRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_remote_access_session(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.delete_remote_access_session_result.DeleteRemoteAccessSessionResult":
        """<p>Deletes a completed remote access session and its results. You cannot delete a remote access session if it is still active.</p> <important> <p>You cannot undo this operation.</p> </important>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the session for which you want to delete remote access.</p>

        Examples:
            To delete a specific remote access session
            The following example deletes a specific remote access session.

            >>> client.delete_remote_access_session(arn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.delete_remote_access_session_request.DeleteRemoteAccessSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.delete_remote_access_session_result.DeleteRemoteAccessSessionResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.delete_remote_access_session

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.delete_remote_access_session.delete_remote_access_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.delete_remote_access_session_request.DeleteRemoteAccessSessionRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_run(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.delete_run_result.DeleteRunResult":
        """<p>Deletes the run, given the run ARN. You cannot delete a run if it is still active.</p> <important> <p>You cannot undo this operation.</p> </important>

        Args:
            arn: <p>The Amazon Resource Name (ARN) for the run to delete.</p>

        Examples:
            To delete a run
            The following example deletes a specific test run.

            >>> client.delete_run(arn='arn:aws:devicefarm:us-west-2:123456789101:run:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.delete_run_request.DeleteRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.delete_run_result.DeleteRunResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.delete_run

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.delete_run.delete_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.delete_run_request.DeleteRunRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_test_grid_project(
        self,
        project_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.delete_test_grid_project_result.DeleteTestGridProjectResult":
        """<p> Deletes a Selenium testing project and all content generated under it. You cannot delete a project if it has active sessions.</p> <important> <p>You cannot undo this operation.</p> </important>

        Args:
            project_arn: <p>The ARN of the project to delete, from <a>CreateTestGridProject</a> or <a>ListTestGridProjects</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.delete_test_grid_project_request.DeleteTestGridProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.delete_test_grid_project_result.DeleteTestGridProjectResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.delete_test_grid_project

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.delete_test_grid_project.delete_test_grid_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.delete_test_grid_project_request.DeleteTestGridProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_upload(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.delete_upload_result.DeleteUploadResult":
        """<p>Deletes an upload given the upload ARN.</p>

        Args:
            arn: <p>Represents the Amazon Resource Name (ARN) of the Device Farm upload to delete.</p>

        Examples:
            To delete a specific upload
            The following example deletes a specific upload.

            >>> client.delete_upload(arn='arn:aws:devicefarm:us-west-2:123456789101:upload:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.delete_upload_request.DeleteUploadRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.delete_upload_result.DeleteUploadResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.delete_upload

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.delete_upload.delete_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.delete_upload_request.DeleteUploadRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_vpce_configuration(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.delete_vpce_configuration_result.DeleteVPCEConfigurationResult":
        """<p>Deletes a configuration for your Amazon Virtual Private Cloud (VPC) endpoint.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.delete_vpce_configuration_request.DeleteVPCEConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.delete_vpce_configuration_result.DeleteVPCEConfigurationResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.delete_vpce_configuration

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.delete_vpce_configuration.delete_vpce_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.delete_vpce_configuration_request.DeleteVPCEConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_account_settings(
        self, *, config_overrides: Optional[DeviceFarmClientConfig] = None
    ) -> (
        "aws_sdk_device_farm.types.get_account_settings_result.GetAccountSettingsResult"
    ):
        """<p>Returns the number of unmetered iOS or unmetered Android devices that have been purchased by the account.</p>

        Examples:
            To get information about account settings
            The following example returns information about your Device Farm account settings.

            >>> client.get_account_settings()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_account_settings_request.GetAccountSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_account_settings_result.GetAccountSettingsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_account_settings

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_account_settings.get_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_account_settings_request.GetAccountSettingsRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_device(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_device_result.GetDeviceResult":
        """<p>Gets information about a unique device type.</p>

        Args:
            arn: <p>The device type's ARN.</p>

        Examples:
            To get information about a device
            The following example returns information about a specific device.

            >>> client.get_device(arn='arn:aws:devicefarm:us-west-2::device:123EXAMPLE')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_device_request.GetDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_device_result.GetDeviceResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_device

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_device.get_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_device_request.GetDeviceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_device_instance(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_device_instance_result.GetDeviceInstanceResult":
        """<p>Returns information about a device instance that belongs to a private device fleet.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the instance you're requesting information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_device_instance_request.GetDeviceInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_device_instance_result.GetDeviceInstanceResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_device_instance

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_device_instance.get_device_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_device_instance_request.GetDeviceInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_device_pool(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_device_pool_result.GetDevicePoolResult":
        """<p>Gets information about a device pool.</p>

        Args:
            arn: <p>The device pool's ARN.</p>

        Examples:
            To get information about a device pool
            The following example returns information about a specific device pool, given a project ARN.

            >>> client.get_device_pool(arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_device_pool_request.GetDevicePoolRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_device_pool_result.GetDevicePoolResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_device_pool

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_device_pool.get_device_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_device_pool_request.GetDevicePoolRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_device_pool_compatibility(
        self,
        device_pool_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        app_arn: Optional[
            "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        test_type: Optional["aws_sdk_device_farm.types.test_type.TestType"] = None,
        test: Optional[
            "aws_sdk_device_farm.types.schedule_run_test.ScheduleRunTest"
        ] = None,
        configuration: Optional[
            "aws_sdk_device_farm.types.schedule_run_configuration.ScheduleRunConfiguration"
        ] = None,
        project_arn: Optional[
            "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
        ] = None,
    ) -> "aws_sdk_device_farm.types.get_device_pool_compatibility_result.GetDevicePoolCompatibilityResult":
        """<p>Gets information about compatibility with a device pool.</p>

        Args:
            device_pool_arn: <p>The device pool's ARN.</p>
            app_arn: <p>The ARN of the app that is associated with the specified device pool.</p>
            test_type: <p>The test type for the specified device pool.</p> <p>Allowed values include the following:</p> <ul> <li> <p>BUILTIN_FUZZ.</p> </li> <li> <p>APPIUM_JAVA_JUNIT.</p> </li> <li> <p>APPIUM_JAVA_TESTNG.</p> </li> <li> <p>APPIUM_PYTHON.</p> </li> <li> <p>APPIUM_NODE.</p> </li> <li> <p>APPIUM_RUBY.</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT.</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG.</p> </li> <li> <p>APPIUM_WEB_PYTHON.</p> </li> <li> <p>APPIUM_WEB_NODE.</p> </li> <li> <p>APPIUM_WEB_RUBY.</p> </li> <li> <p>INSTRUMENTATION.</p> </li> <li> <p>XCTEST.</p> </li> <li> <p>XCTEST_UI.</p> </li> </ul>
            test: <p>Information about the uploaded test to be run against the device pool.</p>
            configuration: <p>An object that contains information about the settings for a run.</p>
            project_arn: <p>The ARN of the project for which you want to check device pool compatibility.</p>

        Examples:
            To get information about the compatibility of a device pool
            The following example returns information about the compatibility of a specific device pool, given its ARN.

            >>> client.get_device_pool_compatibility(device_pool_arn='arn:aws:devicefarm:us-west-2::devicepool:123-456-EXAMPLE-GUID', app_arn='arn:aws:devicefarm:us-west-2::app:123-456-EXAMPLE-GUID', test_type='APPIUM_PYTHON')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_device_pool_compatibility_request.GetDevicePoolCompatibilityRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_device_pool_compatibility_result.GetDevicePoolCompatibilityResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_device_pool_compatibility

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_device_pool_compatibility.get_device_pool_compatibility(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_device_pool_compatibility_request.GetDevicePoolCompatibilityRequest = {}  # type: ignore[typeddict-item]
        input_["device_pool_arn"] = device_pool_arn
        if app_arn is not None:
            input_["app_arn"] = app_arn
        if test_type is not None:
            input_["test_type"] = test_type
        if test is not None:
            input_["test"] = test
        if configuration is not None:
            input_["configuration"] = configuration
        if project_arn is not None:
            input_["project_arn"] = project_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_instance_profile(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> (
        "aws_sdk_device_farm.types.get_instance_profile_result.GetInstanceProfileResult"
    ):
        """<p>Returns information about the specified instance profile.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of an instance profile.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_instance_profile_request.GetInstanceProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_instance_profile_result.GetInstanceProfileResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_instance_profile

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_instance_profile.get_instance_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_instance_profile_request.GetInstanceProfileRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_job(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_job_result.GetJobResult":
        """<p>Gets information about a job.</p>

        Args:
            arn: <p>The job's ARN.</p>

        Examples:
            To get information about a job
            The following example returns information about a specific job.

            >>> client.get_job(arn='arn:aws:devicefarm:us-west-2::job:123-456-EXAMPLE-GUID')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_job_request.GetJobRequest]",
        ) -> OperationResponse["aws_sdk_device_farm.types.get_job_result.GetJobResult"]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_job

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_job.get_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_job_request.GetJobRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_network_profile(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_network_profile_result.GetNetworkProfileResult":
        """<p>Returns information about a network profile.</p>

        Args:
            arn: <p>The ARN of the network profile to return information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_network_profile_request.GetNetworkProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_network_profile_result.GetNetworkProfileResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_network_profile

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_network_profile.get_network_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_network_profile_request.GetNetworkProfileRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_offering_status(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.get_offering_status_result.GetOfferingStatusResult":
        r"""<p>Gets the current status and future status of all offerings purchased by an AWS account. The response indicates how many offerings are currently available and the offerings that will be available in the next period. The API returns a <code>NotEligible</code> error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact <a href=\"mailto:aws-devicefarm-support@amazon.com\">aws-devicefarm-support@amazon.com</a>.</p>

        Args:
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_offering_status_request.GetOfferingStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_offering_status_result.GetOfferingStatusResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_offering_status

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_offering_status.get_offering_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_offering_status_request.GetOfferingStatusRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_project(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_project_result.GetProjectResult":
        """<p>Gets information about a project.</p>

        Args:
            arn: <p>The project's ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_project_request.GetProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_project_result.GetProjectResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_project

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_project.get_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_project_request.GetProjectRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_remote_access_session(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_remote_access_session_result.GetRemoteAccessSessionResult":
        """<p>Returns a link to a currently running remote access session.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the remote access session about which you want to get session information.</p>

        Examples:
            To get a remote access session
            The following example gets a specific remote access session.

            >>> client.get_remote_access_session(arn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_remote_access_session_request.GetRemoteAccessSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_remote_access_session_result.GetRemoteAccessSessionResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_remote_access_session

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_remote_access_session.get_remote_access_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_remote_access_session_request.GetRemoteAccessSessionRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_run(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_run_result.GetRunResult":
        """<p>Gets information about a run.</p>

        Args:
            arn: <p>The run's ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_run_request.GetRunRequest]",
        ) -> OperationResponse["aws_sdk_device_farm.types.get_run_result.GetRunResult"]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_run

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_run.get_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_run_request.GetRunRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_suite(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_suite_result.GetSuiteResult":
        """<p>Gets information about a suite.</p>

        Args:
            arn: <p>The suite's ARN.</p>

        Examples:
            To get information about a test suite
            The following example gets information about a specific test suite.

            >>> client.get_suite(arn='arn:aws:devicefarm:us-west-2:123456789101:suite:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_suite_request.GetSuiteRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_suite_result.GetSuiteResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_suite

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_suite.get_suite(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_suite_request.GetSuiteRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_test(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_test_result.GetTestResult":
        """<p>Gets information about a test.</p>

        Args:
            arn: <p>The test's ARN.</p>

        Examples:
            To get information about a specific test
            The following example gets information about a specific test.

            >>> client.get_test(arn='arn:aws:devicefarm:us-west-2:123456789101:test:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_test_request.GetTestRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_test_result.GetTestResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_test

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_test.get_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_test_request.GetTestRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_test_grid_project(
        self,
        project_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_test_grid_project_result.GetTestGridProjectResult":
        """<p>Retrieves information about a Selenium testing project.</p>

        Args:
            project_arn: <p>The ARN of the Selenium testing project, from either <a>CreateTestGridProject</a> or <a>ListTestGridProjects</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_test_grid_project_request.GetTestGridProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_test_grid_project_result.GetTestGridProjectResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_test_grid_project

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_test_grid_project.get_test_grid_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_test_grid_project_request.GetTestGridProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_test_grid_session(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        project_arn: Optional[
            "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn"
        ] = None,
        session_id: Optional["aws_sdk_device_farm.types.resource_id.ResourceId"] = None,
        session_arn: Optional[
            "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn"
        ] = None,
    ) -> "aws_sdk_device_farm.types.get_test_grid_session_result.GetTestGridSessionResult":
        """<p>A session is an instance of a browser created through a <code>RemoteWebDriver</code> with the URL from <a>CreateTestGridUrlResult$url</a>. You can use the following to look up sessions:</p> <ul> <li> <p>The session ARN (<a>GetTestGridSessionRequest$sessionArn</a>).</p> </li> <li> <p>The project ARN and a session ID (<a>GetTestGridSessionRequest$projectArn</a> and <a>GetTestGridSessionRequest$sessionId</a>).</p> </li> </ul> <p></p>

        Args:
            project_arn: <p>The ARN for the project that this session belongs to. See <a>CreateTestGridProject</a> and <a>ListTestGridProjects</a>.</p>
            session_id: <p>An ID associated with this session.</p>
            session_arn: <p>An ARN that uniquely identifies a <a>TestGridSession</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_test_grid_session_request.GetTestGridSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_test_grid_session_result.GetTestGridSessionResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_test_grid_session

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_test_grid_session.get_test_grid_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_test_grid_session_request.GetTestGridSessionRequest = {}  # type: ignore[typeddict-item]
        if project_arn is not None:
            input_["project_arn"] = project_arn
        if session_id is not None:
            input_["session_id"] = session_id
        if session_arn is not None:
            input_["session_arn"] = session_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_upload(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_upload_result.GetUploadResult":
        """<p>Gets information about an upload.</p>

        Args:
            arn: <p>The upload's ARN.</p>

        Examples:
            To get information about a specific upload
            The following example gets information about a specific upload.

            >>> client.get_upload(arn='arn:aws:devicefarm:us-west-2:123456789101:upload:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_upload_request.GetUploadRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_upload_result.GetUploadResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_upload

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_upload.get_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_upload_request.GetUploadRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_vpce_configuration(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.get_vpce_configuration_result.GetVPCEConfigurationResult":
        """<p>Returns information about the configuration settings for your Amazon Virtual Private Cloud (VPC) endpoint.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to describe.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.get_vpce_configuration_request.GetVPCEConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.get_vpce_configuration_result.GetVPCEConfigurationResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.get_vpce_configuration

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.get_vpce_configuration.get_vpce_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.get_vpce_configuration_request.GetVPCEConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def install_to_remote_access_session(
        self,
        remote_access_session_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        app_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.install_to_remote_access_session_result.InstallToRemoteAccessSessionResult":
        """<p>Installs an application to the device in a remote access session. For Android applications, the file must be in .apk format. For iOS applications, the file must be in .ipa format.</p>

        Args:
            remote_access_session_arn: <p>The Amazon Resource Name (ARN) of the remote access session about which you are requesting information.</p>
            app_arn: <p>The ARN of the app about which you are requesting information.</p>

        Examples:
            To install to a remote access session
            The following example installs a specific app to a device in a specific remote access session.

            >>> client.install_to_remote_access_session(remote_access_session_arn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456', app_arn='arn:aws:devicefarm:us-west-2:123456789101:app:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.install_to_remote_access_session_request.InstallToRemoteAccessSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.install_to_remote_access_session_result.InstallToRemoteAccessSessionResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.install_to_remote_access_session

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.install_to_remote_access_session.install_to_remote_access_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.install_to_remote_access_session_request.InstallToRemoteAccessSessionRequest = {}  # type: ignore[typeddict-item]
        input_["remote_access_session_arn"] = remote_access_session_arn
        input_["app_arn"] = app_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_artifacts(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        type: "aws_sdk_device_farm.types.artifact_category.ArtifactCategory",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_artifacts_result.ListArtifactsResult":
        """<p>Gets information about artifacts.</p>

        Args:
            arn: <p>The run, job, suite, or test ARN.</p>
            type: <p>The artifacts' type.</p> <p>Allowed values include:</p> <ul> <li> <p>FILE</p> </li> <li> <p>LOG</p> </li> <li> <p>SCREENSHOT</p> </li> </ul>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Examples:
            To list artifacts for a resource
            The following example lists screenshot artifacts for a specific run.

            >>> client.list_artifacts(arn='arn:aws:devicefarm:us-west-2:123456789101:run:EXAMPLE-GUID-123-456', type='SCREENSHOT')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_artifacts_request.ListArtifactsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_artifacts_result.ListArtifactsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_artifacts

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_artifacts.list_artifacts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_artifacts_request.ListArtifactsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_artifacts(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        type: "aws_sdk_device_farm.types.artifact_category.ArtifactCategory",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.artifact.Artifact]":
        _token = next_token
        while True:
            _response = self.list_artifacts(
                arn,
                type,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("artifacts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_device_instances(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        max_results: Optional["aws_sdk_device_farm.types.integer.Integer"] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_device_instances_result.ListDeviceInstancesResult":
        """<p>Returns information about the private device instances associated with one or more AWS accounts.</p>

        Args:
            max_results: <p>An integer that specifies the maximum number of items you want to return in the API response.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_device_instances_request.ListDeviceInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_device_instances_result.ListDeviceInstancesResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_device_instances

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_device_instances.list_device_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_device_instances_request.ListDeviceInstancesRequest = {}  # type: ignore[typeddict-item]
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

    def list_device_pools(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        type: Optional[
            "aws_sdk_device_farm.types.device_pool_type.DevicePoolType"
        ] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_device_pools_result.ListDevicePoolsResult":
        """<p>Gets information about device pools.</p>

        Args:
            arn: <p>The project ARN.</p>
            type: <p>The device pools' type.</p> <p>Allowed values include:</p> <ul> <li> <p>CURATED: A device pool that is created and managed by AWS Device Farm.</p> </li> <li> <p>PRIVATE: A device pool that is created and managed by the device pool developer.</p> </li> </ul>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Examples:
            To get information about device pools
            The following example returns information about the private device pools in a specific project.

            >>> client.list_device_pools(arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456', type='PRIVATE')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_device_pools_request.ListDevicePoolsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_device_pools_result.ListDevicePoolsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_device_pools

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_device_pools.list_device_pools(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_device_pools_request.ListDevicePoolsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_device_pools(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        type: Optional[
            "aws_sdk_device_farm.types.device_pool_type.DevicePoolType"
        ] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.device_pool.DevicePool]":
        _token = next_token
        while True:
            _response = self.list_device_pools(
                arn,
                config_overrides=config_overrides,
                type=type,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("device_pools",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_devices(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        arn: Optional[
            "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
        filters: Optional[
            "aws_sdk_device_farm.types.device_filters.DeviceFilters"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_devices_result.ListDevicesResult":
        r"""<p>Gets information about unique device types.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the project.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>
            filters: <p>Used to select a set of devices. A filter is made up of an attribute, an operator, and one or more values.</p> <ul> <li> <p>Attribute: The aspect of a device such as platform or model used as the selection criteria in a device filter.</p> <p>Allowed values include:</p> <ul> <li> <p>ARN: The Amazon Resource Name (ARN) of the device (for example, <code>arn:aws:devicefarm:us-west-2::device:12345Example</code>).</p> </li> <li> <p>PLATFORM: The device platform. Valid values are ANDROID or IOS.</p> </li> <li> <p>OS_VERSION: The operating system version (for example, 10.3.2).</p> </li> <li> <p>MODEL: The device model (for example, iPad 5th Gen).</p> </li> <li> <p>AVAILABILITY: The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.</p> </li> <li> <p>FORM_FACTOR: The device form factor. Valid values are PHONE or TABLET.</p> </li> <li> <p>MANUFACTURER: The device manufacturer (for example, Apple).</p> </li> <li> <p>REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are TRUE or FALSE.</p> </li> <li> <p>REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE. Because remote debugging is <a href=\"https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html\">no longer supported</a>, this attribute is ignored.</p> </li> <li> <p>INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.</p> </li> <li> <p>INSTANCE_LABELS: The label of the device instance.</p> </li> <li> <p>FLEET_TYPE: The fleet type. Valid values are PUBLIC or PRIVATE.</p> </li> </ul> </li> <li> <p>Operator: The filter operator.</p> <ul> <li> <p>The EQUALS operator is available for every attribute except INSTANCE_LABELS.</p> </li> <li> <p>The CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.</p> </li> <li> <p>The IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.</p> </li> <li> <p>The LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.</p> </li> </ul> </li> <li> <p>Values: An array of one or more filter values.</p> <ul> <li> <p>The IN and NOT_IN operators take a values array that has one or more elements.</p> </li> <li> <p>The other operators require an array with a single element.</p> </li> <li> <p>In a request, the AVAILABILITY attribute takes the following values: AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.</p> </li> </ul> </li> </ul>

        Examples:
            To get information about devices
            The following example returns information about the available devices in a specific project.

            >>> client.list_devices(arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_devices_request.ListDevicesRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_devices_result.ListDevicesResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_devices

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_devices.list_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_devices_request.ListDevicesRequest = {}  # type: ignore[typeddict-item]
        if arn is not None:
            input_["arn"] = arn
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_devices(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        arn: Optional[
            "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
        filters: Optional[
            "aws_sdk_device_farm.types.device_filters.DeviceFilters"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.device.Device]":
        _token = next_token
        while True:
            _response = self.list_devices(
                config_overrides=config_overrides,
                arn=arn,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("devices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_instance_profiles(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        max_results: Optional["aws_sdk_device_farm.types.integer.Integer"] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_instance_profiles_result.ListInstanceProfilesResult":
        """<p>Returns information about all the instance profiles in an AWS account.</p>

        Args:
            max_results: <p>An integer that specifies the maximum number of items you want to return in the API response.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_instance_profiles_request.ListInstanceProfilesRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_instance_profiles_result.ListInstanceProfilesResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_instance_profiles

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_instance_profiles.list_instance_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_instance_profiles_request.ListInstanceProfilesRequest = {}  # type: ignore[typeddict-item]
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

    def list_jobs(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_jobs_result.ListJobsResult":
        """<p>Gets information about jobs for a given test run.</p>

        Args:
            arn: <p>The run's Amazon Resource Name (ARN).</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Examples:
            To get information about jobs
            The following example returns information about jobs in a specific project.

            >>> client.list_jobs(arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_jobs_request.ListJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_jobs_result.ListJobsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_jobs

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_jobs.list_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_jobs_request.ListJobsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_jobs(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.job.Job]":
        _token = next_token
        while True:
            _response = self.list_jobs(
                arn,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_network_profiles(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        type: Optional[
            "aws_sdk_device_farm.types.network_profile_type.NetworkProfileType"
        ] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_network_profiles_result.ListNetworkProfilesResult":
        """<p>Returns the list of available network profiles.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the project for which you want to list network profiles.</p>
            type: <p>The type of network profile to return information about. Valid values are listed here.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_network_profiles_request.ListNetworkProfilesRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_network_profiles_result.ListNetworkProfilesResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_network_profiles

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_network_profiles.list_network_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_network_profiles_request.ListNetworkProfilesRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_offering_promotions(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_offering_promotions_result.ListOfferingPromotionsResult":
        r"""<p>Returns a list of offering promotions. Each offering promotion record contains the ID and description of the promotion. The API returns a <code>NotEligible</code> error if the caller is not permitted to invoke the operation. Contact <a href=\"mailto:aws-devicefarm-support@amazon.com\">aws-devicefarm-support@amazon.com</a> if you must be able to invoke this operation.</p>

        Args:
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_offering_promotions_request.ListOfferingPromotionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_offering_promotions_result.ListOfferingPromotionsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_offering_promotions

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_offering_promotions.list_offering_promotions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_offering_promotions_request.ListOfferingPromotionsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_offerings(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_offerings_result.ListOfferingsResult":
        r"""<p>Returns a list of products or offerings that the user can manage through the API. Each offering record indicates the recurring price per unit and the frequency for that offering. The API returns a <code>NotEligible</code> error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact <a href=\"mailto:aws-devicefarm-support@amazon.com\">aws-devicefarm-support@amazon.com</a>.</p>

        Args:
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Examples:
            To get information about device offerings
            The following example returns information about available device offerings.

            >>> client.list_offerings(next_token='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE=')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_offerings_request.ListOfferingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_offerings_result.ListOfferingsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_offerings

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_offerings.list_offerings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_offerings_request.ListOfferingsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_offerings(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.offering.Offering]":
        _token = next_token
        while True:
            _response = self.list_offerings(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("offerings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_offering_transactions(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_offering_transactions_result.ListOfferingTransactionsResult":
        r"""<p>Returns a list of all historical purchases, renewals, and system renewal transactions for an AWS account. The list is paginated and ordered by a descending timestamp (most recent transactions are first). The API returns a <code>NotEligible</code> error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact <a href=\"mailto:aws-devicefarm-support@amazon.com\">aws-devicefarm-support@amazon.com</a>.</p>

        Args:
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_offering_transactions_request.ListOfferingTransactionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_offering_transactions_result.ListOfferingTransactionsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_offering_transactions

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_offering_transactions.list_offering_transactions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_offering_transactions_request.ListOfferingTransactionsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_offering_transactions(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.offering_transaction.OfferingTransaction]":
        _token = next_token
        while True:
            _response = self.list_offering_transactions(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("offering_transactions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_projects(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        arn: Optional[
            "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_projects_result.ListProjectsResult":
        """<p>Gets information about projects.</p>

        Args:
            arn: <p>Optional. If no Amazon Resource Name (ARN) is specified, then AWS Device Farm returns a list of all projects for the AWS account. You can also specify a project ARN.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_projects_request.ListProjectsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_projects_result.ListProjectsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_projects

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_projects.list_projects(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_projects_request.ListProjectsRequest = {}  # type: ignore[typeddict-item]
        if arn is not None:
            input_["arn"] = arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_projects(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        arn: Optional[
            "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.project.Project]":
        _token = next_token
        while True:
            _response = self.list_projects(
                config_overrides=config_overrides,
                arn=arn,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("projects",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_remote_access_sessions(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_remote_access_sessions_result.ListRemoteAccessSessionsResult":
        """<p>Returns a list of all currently running remote access sessions.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the project about which you are requesting information.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Examples:
            To get information about a remote access session
            The following example returns information about a specific Device Farm remote access session.

            >>> client.list_remote_access_sessions(arn='arn:aws:devicefarm:us-west-2:123456789101:session:EXAMPLE-GUID-123-456', next_token='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE=')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_remote_access_sessions_request.ListRemoteAccessSessionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_remote_access_sessions_result.ListRemoteAccessSessionsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_remote_access_sessions

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_remote_access_sessions.list_remote_access_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_remote_access_sessions_request.ListRemoteAccessSessionsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_runs(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_runs_result.ListRunsResult":
        """<p>Gets information about runs, given an AWS Device Farm project ARN.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the project for which you want to list runs.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_runs_request.ListRunsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_runs_result.ListRunsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_runs

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_runs.list_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_runs_request.ListRunsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_runs(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.run.Run]":
        _token = next_token
        while True:
            _response = self.list_runs(
                arn,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_samples(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_samples_result.ListSamplesResult":
        """<p>Gets information about samples, given an AWS Device Farm job ARN.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the job used to list samples.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Examples:
            To get information about samples
            The following example returns information about samples, given a specific Device Farm project.

            >>> client.list_samples(arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456', next_token='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_samples_request.ListSamplesRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_samples_result.ListSamplesResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_samples

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_samples.list_samples(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_samples_request.ListSamplesRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_samples(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.sample.Sample]":
        _token = next_token
        while True:
            _response = self.list_samples(
                arn,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("samples",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_suites(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_suites_result.ListSuitesResult":
        """<p>Gets information about test suites for a given job.</p>

        Args:
            arn: <p>The job's Amazon Resource Name (ARN).</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Examples:
            To get information about suites
            The following example returns information about suites, given a specific Device Farm job.

            >>> client.list_suites(arn='arn:aws:devicefarm:us-west-2:123456789101:job:EXAMPLE-GUID-123-456', next_token='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_suites_request.ListSuitesRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_suites_result.ListSuitesResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_suites

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_suites.list_suites(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_suites_request.ListSuitesRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_suites(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.suite.Suite]":
        _token = next_token
        while True:
            _response = self.list_suites(
                arn,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("suites",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List the tags for an AWS Device Farm resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource or resources for which to list tags. You can associate tags with the following Device Farm resources: <code>PROJECT</code>, <code>TESTGRID_PROJECT</code>, <code>RUN</code>, <code>NETWORK_PROFILE</code>, <code>INSTANCE_PROFILE</code>, <code>DEVICE_INSTANCE</code>, <code>SESSION</code>, <code>DEVICE_POOL</code>, <code>DEVICE</code>, and <code>VPCE_CONFIGURATION</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_tags_for_resource

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_test_grid_projects(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        max_result: Optional[
            "aws_sdk_device_farm.types.max_page_size.MaxPageSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_test_grid_projects_result.ListTestGridProjectsResult":
        """<p>Gets a list of all Selenium testing projects in your account.</p>

        Args:
            max_result: <p>Return no more than this number of results.</p>
            next_token: <p>From a response, used to continue a paginated listing. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_test_grid_projects_request.ListTestGridProjectsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_test_grid_projects_result.ListTestGridProjectsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_test_grid_projects

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_test_grid_projects.list_test_grid_projects(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_test_grid_projects_request.ListTestGridProjectsRequest = {}  # type: ignore[typeddict-item]
        if max_result is not None:
            input_["max_result"] = max_result
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_test_grid_session_actions(
        self,
        session_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        max_result: Optional[
            "aws_sdk_device_farm.types.max_page_size.MaxPageSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_test_grid_session_actions_result.ListTestGridSessionActionsResult":
        """<p>Returns a list of the actions taken in a <a>TestGridSession</a>.</p>

        Args:
            session_arn: <p>The ARN of the session to retrieve.</p>
            max_result: <p>The maximum number of sessions to return per response.</p>
            next_token: <p>Pagination token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_test_grid_session_actions_request.ListTestGridSessionActionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_test_grid_session_actions_result.ListTestGridSessionActionsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_test_grid_session_actions

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_test_grid_session_actions.list_test_grid_session_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_test_grid_session_actions_request.ListTestGridSessionActionsRequest = {}  # type: ignore[typeddict-item]
        input_["session_arn"] = session_arn
        if max_result is not None:
            input_["max_result"] = max_result
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_test_grid_session_artifacts(
        self,
        session_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        type: Optional[
            "aws_sdk_device_farm.types.test_grid_session_artifact_category.TestGridSessionArtifactCategory"
        ] = None,
        max_result: Optional[
            "aws_sdk_device_farm.types.max_page_size.MaxPageSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_test_grid_session_artifacts_result.ListTestGridSessionArtifactsResult":
        """<p>Retrieves a list of artifacts created during the session.</p>

        Args:
            session_arn: <p>The ARN of a <a>TestGridSession</a>. </p>
            type: <p>Limit results to a specified type of artifact.</p>
            max_result: <p>The maximum number of results to be returned by a request.</p>
            next_token: <p>Pagination token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_test_grid_session_artifacts_request.ListTestGridSessionArtifactsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_test_grid_session_artifacts_result.ListTestGridSessionArtifactsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_test_grid_session_artifacts

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_test_grid_session_artifacts.list_test_grid_session_artifacts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_test_grid_session_artifacts_request.ListTestGridSessionArtifactsRequest = {}  # type: ignore[typeddict-item]
        input_["session_arn"] = session_arn
        if type is not None:
            input_["type"] = type
        if max_result is not None:
            input_["max_result"] = max_result
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_test_grid_sessions(
        self,
        project_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        status: Optional[
            "aws_sdk_device_farm.types.test_grid_session_status.TestGridSessionStatus"
        ] = None,
        creation_time_after: Optional[
            "aws_sdk_device_farm.types.date_time.DateTime"
        ] = None,
        creation_time_before: Optional[
            "aws_sdk_device_farm.types.date_time.DateTime"
        ] = None,
        end_time_after: Optional["aws_sdk_device_farm.types.date_time.DateTime"] = None,
        end_time_before: Optional[
            "aws_sdk_device_farm.types.date_time.DateTime"
        ] = None,
        max_result: Optional[
            "aws_sdk_device_farm.types.max_page_size.MaxPageSize"
        ] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_test_grid_sessions_result.ListTestGridSessionsResult":
        """<p>Retrieves a list of sessions for a <a>TestGridProject</a>.</p>

        Args:
            project_arn: <p>ARN of a <a>TestGridProject</a>.</p>
            status: <p>Return only sessions in this state.</p>
            creation_time_after: <p>Return only sessions created after this time.</p>
            creation_time_before: <p>Return only sessions created before this time.</p>
            end_time_after: <p>Return only sessions that ended after this time.</p>
            end_time_before: <p>Return only sessions that ended before this time.</p>
            max_result: <p>Return only this many results at a time.</p>
            next_token: <p>Pagination token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_test_grid_sessions_request.ListTestGridSessionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_test_grid_sessions_result.ListTestGridSessionsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_test_grid_sessions

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_test_grid_sessions.list_test_grid_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_test_grid_sessions_request.ListTestGridSessionsRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        if status is not None:
            input_["status"] = status
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if end_time_after is not None:
            input_["end_time_after"] = end_time_after
        if end_time_before is not None:
            input_["end_time_before"] = end_time_before
        if max_result is not None:
            input_["max_result"] = max_result
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tests(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_tests_result.ListTestsResult":
        """<p>Gets information about tests in a given test suite.</p>

        Args:
            arn: <p>The test suite's Amazon Resource Name (ARN).</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Examples:
            To get information about tests
            The following example returns information about tests, given a specific Device Farm project.

            >>> client.list_tests(arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456', next_token='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_tests_request.ListTestsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_tests_result.ListTestsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_tests

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_tests.list_tests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_tests_request.ListTestsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_tests(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.test.Test]":
        _token = next_token
        while True:
            _response = self.list_tests(
                arn,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tests",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_unique_problems(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "aws_sdk_device_farm.types.list_unique_problems_result.ListUniqueProblemsResult"
    ):
        """<p>Gets information about unique problems, such as exceptions or crashes.</p> <p>Unique problems are defined as a single instance of an error across a run, job, or suite. For example, if a call in your application consistently raises an exception (<code>OutOfBoundsException in MyActivity.java:386</code>), <code>ListUniqueProblems</code> returns a single entry instead of many individual entries for that exception.</p>

        Args:
            arn: <p>The unique problems' ARNs.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Examples:
            To get information about unique problems
            The following example returns information about unique problems, given a specific Device Farm project.

            >>> client.list_unique_problems(arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456', next_token='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_unique_problems_request.ListUniqueProblemsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_unique_problems_result.ListUniqueProblemsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_unique_problems

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_unique_problems.list_unique_problems(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_unique_problems_request.ListUniqueProblemsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_unique_problems(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[tuple[aws_sdk_device_farm.types.execution_result.ExecutionResult, aws_sdk_device_farm.types.unique_problems.UniqueProblems]]":
        _token = next_token
        while True:
            _response = self.list_unique_problems(
                arn,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("unique_problems",))
            for _k, _v in (_page or {}).items():
                yield (_k, _v)
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_uploads(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        type: Optional["aws_sdk_device_farm.types.upload_type.UploadType"] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_uploads_result.ListUploadsResult":
        """<p>Gets information about uploads, given an AWS Device Farm project ARN.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the project for which you want to list uploads.</p>
            type: <p>The type of upload.</p> <p>Must be one of the following values:</p> <ul> <li> <p>ANDROID_APP</p> </li> <li> <p>IOS_APP</p> </li> <li> <p>WEB_APP</p> </li> <li> <p>EXTERNAL_DATA</p> </li> <li> <p>APPIUM_JAVA_JUNIT_TEST_PACKAGE</p> </li> <li> <p>APPIUM_JAVA_TESTNG_TEST_PACKAGE</p> </li> <li> <p>APPIUM_PYTHON_TEST_PACKAGE</p> </li> <li> <p>APPIUM_NODE_TEST_PACKAGE</p> </li> <li> <p>APPIUM_RUBY_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_PYTHON_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_NODE_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_RUBY_TEST_PACKAGE</p> </li> <li> <p>INSTRUMENTATION_TEST_PACKAGE</p> </li> <li> <p>XCTEST_TEST_PACKAGE</p> </li> <li> <p>XCTEST_UI_TEST_PACKAGE</p> </li> <li> <p>APPIUM_JAVA_JUNIT_TEST_SPEC</p> </li> <li> <p>APPIUM_JAVA_TESTNG_TEST_SPEC</p> </li> <li> <p>APPIUM_PYTHON_TEST_SPEC</p> </li> <li> <p>APPIUM_NODE_TEST_SPEC</p> </li> <li> <p> APPIUM_RUBY_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_PYTHON_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_NODE_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_RUBY_TEST_SPEC</p> </li> <li> <p>INSTRUMENTATION_TEST_SPEC</p> </li> <li> <p>XCTEST_UI_TEST_SPEC</p> </li> </ul>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>

        Examples:
            To get information about uploads
            The following example returns information about uploads, given a specific Device Farm project.

            >>> client.list_uploads(arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456', next_token='RW5DdDJkMWYwZjM2MzM2VHVpOHJIUXlDUXlhc2QzRGViYnc9SEXAMPLE')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_uploads_request.ListUploadsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_uploads_result.ListUploadsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_uploads

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_uploads.list_uploads(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_uploads_request.ListUploadsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_uploads(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        type: Optional["aws_sdk_device_farm.types.upload_type.UploadType"] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_device_farm.types.upload.Upload]":
        _token = next_token
        while True:
            _response = self.list_uploads(
                arn,
                config_overrides=config_overrides,
                type=type,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("uploads",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_vpce_configurations(
        self,
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        max_results: Optional["aws_sdk_device_farm.types.integer.Integer"] = None,
        next_token: Optional[
            "aws_sdk_device_farm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_device_farm.types.list_vpce_configurations_result.ListVPCEConfigurationsResult":
        """<p>Returns information about all Amazon Virtual Private Cloud (VPC) endpoint configurations in the AWS account.</p>

        Args:
            max_results: <p>An integer that specifies the maximum number of items you want to return in the API response.</p>
            next_token: <p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.list_vpce_configurations_request.ListVPCEConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.list_vpce_configurations_result.ListVPCEConfigurationsResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.list_vpce_configurations

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.list_vpce_configurations.list_vpce_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.list_vpce_configurations_request.ListVPCEConfigurationsRequest = {}  # type: ignore[typeddict-item]
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

    def purchase_offering(
        self,
        offering_id: "aws_sdk_device_farm.types.offering_identifier.OfferingIdentifier",
        quantity: "aws_sdk_device_farm.types.integer.Integer",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        offering_promotion_id: Optional[
            "aws_sdk_device_farm.types.offering_promotion_identifier.OfferingPromotionIdentifier"
        ] = None,
    ) -> "aws_sdk_device_farm.types.purchase_offering_result.PurchaseOfferingResult":
        r"""<p>Immediately purchases offerings for an AWS account. Offerings renew with the latest total purchased quantity for an offering, unless the renewal was overridden. The API returns a <code>NotEligible</code> error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact <a href=\"mailto:aws-devicefarm-support@amazon.com\">aws-devicefarm-support@amazon.com</a>.</p>

        Args:
            offering_id: <p>The ID of the offering.</p>
            quantity: <p>The number of device slots to purchase in an offering request.</p>
            offering_promotion_id: <p>The ID of the offering promotion to be applied to the purchase.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.purchase_offering_request.PurchaseOfferingRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.purchase_offering_result.PurchaseOfferingResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.purchase_offering

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.purchase_offering.purchase_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.purchase_offering_request.PurchaseOfferingRequest = {}  # type: ignore[typeddict-item]
        input_["offering_id"] = offering_id
        input_["quantity"] = quantity
        if offering_promotion_id is not None:
            input_["offering_promotion_id"] = offering_promotion_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def renew_offering(
        self,
        offering_id: "aws_sdk_device_farm.types.offering_identifier.OfferingIdentifier",
        quantity: "aws_sdk_device_farm.types.integer.Integer",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.renew_offering_result.RenewOfferingResult":
        r"""<p>Explicitly sets the quantity of devices to renew for an offering, starting from the <code>effectiveDate</code> of the next period. The API returns a <code>NotEligible</code> error if the user is not permitted to invoke the operation. If you must be able to invoke this operation, contact <a href=\"mailto:aws-devicefarm-support@amazon.com\">aws-devicefarm-support@amazon.com</a>.</p>

        Args:
            offering_id: <p>The ID of a request to renew an offering.</p>
            quantity: <p>The quantity requested in an offering renewal.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.renew_offering_request.RenewOfferingRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.renew_offering_result.RenewOfferingResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.renew_offering

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.renew_offering.renew_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.renew_offering_request.RenewOfferingRequest = {}  # type: ignore[typeddict-item]
        input_["offering_id"] = offering_id
        input_["quantity"] = quantity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def schedule_run(
        self,
        project_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        test: "aws_sdk_device_farm.types.schedule_run_test.ScheduleRunTest",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        app_arn: Optional[
            "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        device_pool_arn: Optional[
            "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        device_selection_configuration: Optional[
            "aws_sdk_device_farm.types.device_selection_configuration.DeviceSelectionConfiguration"
        ] = None,
        name: Optional["aws_sdk_device_farm.types.name.Name"] = None,
        configuration: Optional[
            "aws_sdk_device_farm.types.schedule_run_configuration.ScheduleRunConfiguration"
        ] = None,
        execution_configuration: Optional[
            "aws_sdk_device_farm.types.execution_configuration.ExecutionConfiguration"
        ] = None,
    ) -> "aws_sdk_device_farm.types.schedule_run_result.ScheduleRunResult":
        """<p>Schedules a run.</p>

        Args:
            project_arn: <p>The ARN of the project for the run to be scheduled.</p>
            app_arn: <p>The ARN of an application package to run tests against, created with <a>CreateUpload</a>. See <a>ListUploads</a>.</p>
            device_pool_arn: <p>The ARN of the device pool for the run to be scheduled.</p>
            device_selection_configuration: <p>The filter criteria used to dynamically select a set of devices for a test run and the maximum number of devices to be included in the run.</p> <p>Either <b> <code>devicePoolArn</code> </b> or <b> <code>deviceSelectionConfiguration</code> </b> is required in a request.</p>
            name: <p>The name for the run to be scheduled.</p>
            test: <p>Information about the test for the run to be scheduled.</p>
            configuration: <p>Information about the settings for the run to be scheduled.</p>
            execution_configuration: <p>Specifies configuration information about a test run, such as the execution timeout (in minutes).</p>

        Examples:
            To schedule a test run
            The following example schedules a test run named MyRun.

            >>> client.schedule_run(project_arn='arn:aws:devicefarm:us-west-2:123456789101:project:EXAMPLE-GUID-123-456', device_pool_arn='arn:aws:devicefarm:us-west-2:123456789101:pool:EXAMPLE-GUID-123-456', name='MyRun', test={'type': 'APPIUM_JAVA_JUNIT', 'testPackageArn': 'arn:aws:devicefarm:us-west-2:123456789101:test:EXAMPLE-GUID-123-456'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.schedule_run_request.ScheduleRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.schedule_run_result.ScheduleRunResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.schedule_run

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.schedule_run.schedule_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.schedule_run_request.ScheduleRunRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        if app_arn is not None:
            input_["app_arn"] = app_arn
        if device_pool_arn is not None:
            input_["device_pool_arn"] = device_pool_arn
        if device_selection_configuration is not None:
            input_["device_selection_configuration"] = device_selection_configuration
        if name is not None:
            input_["name"] = name
        input_["test"] = test
        if configuration is not None:
            input_["configuration"] = configuration
        if execution_configuration is not None:
            input_["execution_configuration"] = execution_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_job(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.stop_job_result.StopJobResult":
        """<p>Initiates a stop request for the current job. AWS Device Farm immediately stops the job on the device where tests have not started. You are not billed for this device. On the device where tests have started, setup suite and teardown suite tests run to completion on the device. You are billed for setup, teardown, and any tests that were in progress or already completed.</p>

        Args:
            arn: <p>Represents the Amazon Resource Name (ARN) of the Device Farm job to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.stop_job_request.StopJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.stop_job_result.StopJobResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.stop_job

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.stop_job.stop_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.stop_job_request.StopJobRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_remote_access_session(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.stop_remote_access_session_result.StopRemoteAccessSessionResult":
        """<p>Ends a specified remote access session.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the remote access session to stop.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.stop_remote_access_session_request.StopRemoteAccessSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.stop_remote_access_session_result.StopRemoteAccessSessionResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.stop_remote_access_session

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.stop_remote_access_session.stop_remote_access_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.stop_remote_access_session_request.StopRemoteAccessSessionRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_run(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.stop_run_result.StopRunResult":
        """<p>Initiates a stop request for the current test run. AWS Device Farm immediately stops the run on devices where tests have not started. You are not billed for these devices. On devices where tests have started executing, setup suite and teardown suite tests run to completion on those devices. You are billed for setup, teardown, and any tests that were in progress or already completed.</p>

        Args:
            arn: <p>Represents the Amazon Resource Name (ARN) of the Device Farm run to stop.</p>

        Examples:
            To stop a test run
            The following example stops a specific test run.

            >>> client.stop_run(arn='arn:aws:devicefarm:us-west-2:123456789101:run:EXAMPLE-GUID-123-456')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.stop_run_request.StopRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.stop_run_result.StopRunResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.stop_run

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.stop_run.stop_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.stop_run_request.StopRunRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn",
        tags: "aws_sdk_device_farm.types.tag_list.TagList",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.tag_resource_response.TagResourceResponse":
        """<p>Associates the specified tags to a resource with the specified <code>resourceArn</code>. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are also deleted.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource or resources to which to add tags. You can associate tags with the following Device Farm resources: <code>PROJECT</code>, <code>TESTGRID_PROJECT</code>, <code>RUN</code>, <code>NETWORK_PROFILE</code>, <code>INSTANCE_PROFILE</code>, <code>DEVICE_INSTANCE</code>, <code>SESSION</code>, <code>DEVICE_POOL</code>, <code>DEVICE</code>, and <code>VPCE_CONFIGURATION</code>.</p>
            tags: <p>The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters. Tag values can have a maximum length of 256 characters.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.tag_resource

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn",
        tag_keys: "aws_sdk_device_farm.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
    ) -> "aws_sdk_device_farm.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes the specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource or resources from which to delete tags. You can associate tags with the following Device Farm resources: <code>PROJECT</code>, <code>TESTGRID_PROJECT</code>, <code>RUN</code>, <code>NETWORK_PROFILE</code>, <code>INSTANCE_PROFILE</code>, <code>DEVICE_INSTANCE</code>, <code>SESSION</code>, <code>DEVICE_POOL</code>, <code>DEVICE</code>, and <code>VPCE_CONFIGURATION</code>.</p>
            tag_keys: <p>The keys of the tags to be removed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.untag_resource

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_device_instance(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        profile_arn: Optional[
            "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        labels: Optional[
            "aws_sdk_device_farm.types.instance_labels.InstanceLabels"
        ] = None,
    ) -> "aws_sdk_device_farm.types.update_device_instance_result.UpdateDeviceInstanceResult":
        """<p>Updates information about a private device instance.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the device instance.</p>
            profile_arn: <p>The ARN of the profile that you want to associate with the device instance.</p>
            labels: <p>An array of strings that you want to associate with the device instance.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.update_device_instance_request.UpdateDeviceInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.update_device_instance_result.UpdateDeviceInstanceResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.update_device_instance

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.update_device_instance.update_device_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.update_device_instance_request.UpdateDeviceInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if profile_arn is not None:
            input_["profile_arn"] = profile_arn
        if labels is not None:
            input_["labels"] = labels

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_device_pool(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        name: Optional["aws_sdk_device_farm.types.name.Name"] = None,
        description: Optional["aws_sdk_device_farm.types.message.Message"] = None,
        rules: Optional["aws_sdk_device_farm.types.rules.Rules"] = None,
        max_devices: Optional["aws_sdk_device_farm.types.integer.Integer"] = None,
        clear_max_devices: Optional["aws_sdk_device_farm.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_device_farm.types.update_device_pool_result.UpdateDevicePoolResult":
        """<p>Modifies the name, description, and rules in a device pool given the attributes and the pool ARN. Rule updates are all-or-nothing, meaning they can only be updated as a whole (or not at all).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Device Farm device pool to update.</p>
            name: <p>A string that represents the name of the device pool to update.</p>
            description: <p>A description of the device pool to update.</p>
            rules: <p>Represents the rules to modify for the device pool. Updating rules is optional. If you update rules for your request, the update replaces the existing rules.</p>
            max_devices: <p>The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and that meet the criteria that you assign for the <code>rules</code> parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.</p> <p>By specifying the maximum number of devices, you can control the costs that you incur by running tests.</p> <p>If you use this parameter in your request, you cannot use the <code>clearMaxDevices</code> parameter in the same request.</p>
            clear_max_devices: <p>Sets whether the <code>maxDevices</code> parameter applies to your device pool. If you set this parameter to <code>true</code>, the <code>maxDevices</code> parameter does not apply, and Device Farm does not limit the number of devices that it adds to your device pool. In this case, Device Farm adds all available devices that meet the criteria specified in the <code>rules</code> parameter.</p> <p>If you use this parameter in your request, you cannot use the <code>maxDevices</code> parameter in the same request.</p>

        Examples:
            To update a device pool
            The following example updates the specified device pool with a new name and description. It also enables remote access of devices in the device pool.

            >>> client.update_device_pool(arn='arn:aws:devicefarm:us-west-2::devicepool:082d10e5-d7d7-48a5-ba5c-12345EXAMPLE', name='NewName', description='NewDescription', rules=[{'attribute': 'REMOTE_ACCESS_ENABLED', 'operator': 'EQUALS', 'value': 'True'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.update_device_pool_request.UpdateDevicePoolRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.update_device_pool_result.UpdateDevicePoolResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.update_device_pool

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.update_device_pool.update_device_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.update_device_pool_request.UpdateDevicePoolRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if rules is not None:
            input_["rules"] = rules
        if max_devices is not None:
            input_["max_devices"] = max_devices
        if clear_max_devices is not None:
            input_["clear_max_devices"] = clear_max_devices

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_instance_profile(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        name: Optional["aws_sdk_device_farm.types.name.Name"] = None,
        description: Optional["aws_sdk_device_farm.types.message.Message"] = None,
        package_cleanup: Optional["aws_sdk_device_farm.types.boolean.Boolean"] = None,
        exclude_app_packages_from_cleanup: Optional[
            "aws_sdk_device_farm.types.package_ids.PackageIds"
        ] = None,
        reboot_after_use: Optional["aws_sdk_device_farm.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_device_farm.types.update_instance_profile_result.UpdateInstanceProfileResult":
        """<p>Updates information about an existing private device instance profile.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the instance profile.</p>
            name: <p>The updated name for your instance profile.</p>
            description: <p>The updated description for your instance profile.</p>
            package_cleanup: <p>The updated choice for whether you want to specify package cleanup. The default value is <code>false</code> for private devices.</p>
            exclude_app_packages_from_cleanup: <p>An array of strings that specifies the list of app packages that should not be cleaned up from the device after a test run is over.</p> <p>The list of packages is only considered if you set <code>packageCleanup</code> to <code>true</code>.</p>
            reboot_after_use: <p>The updated choice for whether you want to reboot the device after use. The default value is <code>true</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.update_instance_profile_request.UpdateInstanceProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.update_instance_profile_result.UpdateInstanceProfileResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.update_instance_profile

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.update_instance_profile.update_instance_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.update_instance_profile_request.UpdateInstanceProfileRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if package_cleanup is not None:
            input_["package_cleanup"] = package_cleanup
        if exclude_app_packages_from_cleanup is not None:
            input_["exclude_app_packages_from_cleanup"] = (
                exclude_app_packages_from_cleanup
            )
        if reboot_after_use is not None:
            input_["reboot_after_use"] = reboot_after_use

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_network_profile(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        name: Optional["aws_sdk_device_farm.types.name.Name"] = None,
        description: Optional["aws_sdk_device_farm.types.message.Message"] = None,
        type: Optional[
            "aws_sdk_device_farm.types.network_profile_type.NetworkProfileType"
        ] = None,
        uplink_bandwidth_bits: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        downlink_bandwidth_bits: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        uplink_delay_ms: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        downlink_delay_ms: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        uplink_jitter_ms: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        downlink_jitter_ms: Optional["aws_sdk_device_farm.types.long.Long"] = None,
        uplink_loss_percent: Optional[
            "aws_sdk_device_farm.types.percent_integer.PercentInteger"
        ] = None,
        downlink_loss_percent: Optional[
            "aws_sdk_device_farm.types.percent_integer.PercentInteger"
        ] = None,
    ) -> "aws_sdk_device_farm.types.update_network_profile_result.UpdateNetworkProfileResult":
        """<p>Updates the network profile.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the project for which you want to update network profile settings.</p>
            name: <p>The name of the network profile about which you are returning information.</p>
            description: <p>The description of the network profile about which you are returning information.</p>
            type: <p>The type of network profile to return information about. Valid values are listed here.</p>
            uplink_bandwidth_bits: <p>The data throughput rate in bits per second, as an integer from 0 to 104857600.</p>
            downlink_bandwidth_bits: <p>The data throughput rate in bits per second, as an integer from 0 to 104857600.</p>
            uplink_delay_ms: <p>Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.</p>
            downlink_delay_ms: <p>Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.</p>
            uplink_jitter_ms: <p>Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.</p>
            downlink_jitter_ms: <p>Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.</p>
            uplink_loss_percent: <p>Proportion of transmitted packets that fail to arrive from 0 to 100 percent.</p>
            downlink_loss_percent: <p>Proportion of received packets that fail to arrive from 0 to 100 percent.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.update_network_profile_request.UpdateNetworkProfileRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.update_network_profile_result.UpdateNetworkProfileResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.update_network_profile

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.update_network_profile.update_network_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.update_network_profile_request.UpdateNetworkProfileRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if uplink_bandwidth_bits is not None:
            input_["uplink_bandwidth_bits"] = uplink_bandwidth_bits
        if downlink_bandwidth_bits is not None:
            input_["downlink_bandwidth_bits"] = downlink_bandwidth_bits
        if uplink_delay_ms is not None:
            input_["uplink_delay_ms"] = uplink_delay_ms
        if downlink_delay_ms is not None:
            input_["downlink_delay_ms"] = downlink_delay_ms
        if uplink_jitter_ms is not None:
            input_["uplink_jitter_ms"] = uplink_jitter_ms
        if downlink_jitter_ms is not None:
            input_["downlink_jitter_ms"] = downlink_jitter_ms
        if uplink_loss_percent is not None:
            input_["uplink_loss_percent"] = uplink_loss_percent
        if downlink_loss_percent is not None:
            input_["downlink_loss_percent"] = downlink_loss_percent

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_project(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        name: Optional["aws_sdk_device_farm.types.name.Name"] = None,
        default_job_timeout_minutes: Optional[
            "aws_sdk_device_farm.types.job_timeout_minutes.JobTimeoutMinutes"
        ] = None,
        vpc_config: Optional["aws_sdk_device_farm.types.vpc_config.VpcConfig"] = None,
        environment_variables: Optional[
            "aws_sdk_device_farm.types.environment_variables.EnvironmentVariables"
        ] = None,
        execution_role_arn: Optional[
            "aws_sdk_device_farm.types.amazon_role_resource_name.AmazonRoleResourceName"
        ] = None,
    ) -> "aws_sdk_device_farm.types.update_project_result.UpdateProjectResult":
        r"""<p>Modifies the specified project name, given the project ARN and a new name.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the project whose name to update.</p>
            name: <p>A string that represents the new name of the project that you are updating.</p>
            default_job_timeout_minutes: <p>The number of minutes a test run in the project executes before it times out.</p>
            vpc_config: <p>The VPC security groups and subnets that are attached to a project.</p>
            environment_variables: <p> A set of environment variables which are used by default for all runs in the project. These environment variables are applied to the test run during the execution of a test spec file. </p> <p> For more information about using test spec files, please see <a href=\"https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments.html\">Custom test environments </a> in <i>AWS Device Farm.</i> </p>
            execution_role_arn: <p>An IAM role to be assumed by the test host for all runs in the project.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.update_project_request.UpdateProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.update_project_result.UpdateProjectResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.update_project

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.update_project.update_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.update_project_request.UpdateProjectRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if default_job_timeout_minutes is not None:
            input_["default_job_timeout_minutes"] = default_job_timeout_minutes
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_test_grid_project(
        self,
        project_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        name: Optional["aws_sdk_device_farm.types.resource_name.ResourceName"] = None,
        description: Optional[
            "aws_sdk_device_farm.types.resource_description.ResourceDescription"
        ] = None,
        vpc_config: Optional[
            "aws_sdk_device_farm.types.test_grid_vpc_config.TestGridVpcConfig"
        ] = None,
    ) -> "aws_sdk_device_farm.types.update_test_grid_project_result.UpdateTestGridProjectResult":
        """<p>Change details of a project.</p>

        Args:
            project_arn: <p>ARN of the project to update.</p>
            name: <p>Human-readable name for the project.</p>
            description: <p>Human-readable description for the project.</p>
            vpc_config: <p>The VPC security groups and subnets that are attached to a project.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.update_test_grid_project_request.UpdateTestGridProjectRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.update_test_grid_project_result.UpdateTestGridProjectResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.update_test_grid_project

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.update_test_grid_project.update_test_grid_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.update_test_grid_project_request.UpdateTestGridProjectRequest = {}  # type: ignore[typeddict-item]
        input_["project_arn"] = project_arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_upload(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        name: Optional["aws_sdk_device_farm.types.name.Name"] = None,
        content_type: Optional[
            "aws_sdk_device_farm.types.content_type.ContentType"
        ] = None,
        edit_content: Optional["aws_sdk_device_farm.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_device_farm.types.update_upload_result.UpdateUploadResult":
        """<p>Updates an uploaded test spec.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the uploaded test spec.</p>
            name: <p>The upload's test spec file name. The name must not contain any forward slashes (/). The test spec file name must end with the <code>.yaml</code> or <code>.yml</code> file extension.</p>
            content_type: <p>The upload's content type (for example, <code>application/x-yaml</code>).</p>
            edit_content: <p>Set to true if the YAML file has changed and must be updated. Otherwise, set to false.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.update_upload_request.UpdateUploadRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.update_upload_result.UpdateUploadResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.update_upload

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.update_upload.update_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.update_upload_request.UpdateUploadRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if content_type is not None:
            input_["content_type"] = content_type
        if edit_content is not None:
            input_["edit_content"] = edit_content

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_vpce_configuration(
        self,
        arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[DeviceFarmClientConfig] = None,
        vpce_configuration_name: Optional[
            "aws_sdk_device_farm.types.vpce_configuration_name.VPCEConfigurationName"
        ] = None,
        vpce_service_name: Optional[
            "aws_sdk_device_farm.types.vpce_service_name.VPCEServiceName"
        ] = None,
        service_dns_name: Optional[
            "aws_sdk_device_farm.types.service_dns_name.ServiceDnsName"
        ] = None,
        vpce_configuration_description: Optional[
            "aws_sdk_device_farm.types.vpce_configuration_description.VPCEConfigurationDescription"
        ] = None,
    ) -> "aws_sdk_device_farm.types.update_vpce_configuration_result.UpdateVPCEConfigurationResult":
        """<p>Updates information about an Amazon Virtual Private Cloud (VPC) endpoint configuration.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the VPC endpoint configuration you want to update.</p>
            vpce_configuration_name: <p>The friendly name you give to your VPC endpoint configuration to manage your configurations more easily.</p>
            vpce_service_name: <p>The name of the VPC endpoint service running in your AWS account that you want Device Farm to test.</p>
            service_dns_name: <p>The DNS (domain) name used to connect to your private service in your VPC. The DNS name must not already be in use on the internet.</p>
            vpce_configuration_description: <p>An optional description that provides details about your VPC endpoint configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_device_farm.types.update_vpce_configuration_request.UpdateVPCEConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_device_farm.types.update_vpce_configuration_result.UpdateVPCEConfigurationResult"
        ]:
            import aws_sdk_device_farm._operations.device_farm_20150623.update_vpce_configuration

            output, http_response = (
                aws_sdk_device_farm._operations.device_farm_20150623.update_vpce_configuration.update_vpce_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_device_farm.types.update_vpce_configuration_request.UpdateVPCEConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if vpce_configuration_name is not None:
            input_["vpce_configuration_name"] = vpce_configuration_name
        if vpce_service_name is not None:
            input_["vpce_service_name"] = vpce_service_name
        if service_dns_name is not None:
            input_["service_dns_name"] = service_dns_name
        if vpce_configuration_description is not None:
            input_["vpce_configuration_description"] = vpce_configuration_description

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
