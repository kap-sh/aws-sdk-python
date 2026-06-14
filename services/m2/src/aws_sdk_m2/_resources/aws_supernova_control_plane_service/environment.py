from typing import TYPE_CHECKING, Optional

import aws_sdk_m2._auth._signers
import aws_sdk_m2._auth._sigv4
from aws_sdk_m2._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_m2.types.boolean
    import aws_sdk_m2.types.capacity_value
    import aws_sdk_m2.types.client_token
    import aws_sdk_m2.types.create_environment_request
    import aws_sdk_m2.types.create_environment_response
    import aws_sdk_m2.types.delete_environment_request
    import aws_sdk_m2.types.delete_environment_response
    import aws_sdk_m2.types.engine_type
    import aws_sdk_m2.types.engine_version
    import aws_sdk_m2.types.entity_description
    import aws_sdk_m2.types.entity_name
    import aws_sdk_m2.types.entity_name_list
    import aws_sdk_m2.types.environment_summary
    import aws_sdk_m2.types.get_environment_request
    import aws_sdk_m2.types.get_environment_response
    import aws_sdk_m2.types.high_availability_config
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.list_environments_request
    import aws_sdk_m2.types.list_environments_response
    import aws_sdk_m2.types.max_results
    import aws_sdk_m2.types.network_type
    import aws_sdk_m2.types.next_token
    import aws_sdk_m2.types.storage_configuration_list
    import aws_sdk_m2.types.string20
    import aws_sdk_m2.types.string50
    import aws_sdk_m2.types.string50_list
    import aws_sdk_m2.types.tag_map
    import aws_sdk_m2.types.update_environment_request
    import aws_sdk_m2.types.update_environment_response
    from aws_sdk_m2._services.async_m2 import Asyncm2Client, Asyncm2ClientConfig
    from aws_sdk_m2._services.m2 import m2Client, m2ClientConfig


class Environment:
    def __init__(self, service: m2Client) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_m2.types.entity_name.EntityName",
        instance_type: "aws_sdk_m2.types.string20.String20",
        engine_type: "aws_sdk_m2.types.engine_type.EngineType",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        description: Optional[
            "aws_sdk_m2.types.entity_description.EntityDescription"
        ] = None,
        engine_version: Optional[
            "aws_sdk_m2.types.engine_version.EngineVersion"
        ] = None,
        subnet_ids: Optional["aws_sdk_m2.types.string50_list.String50List"] = None,
        security_group_ids: Optional[
            "aws_sdk_m2.types.string50_list.String50List"
        ] = None,
        storage_configurations: Optional[
            "aws_sdk_m2.types.storage_configuration_list.StorageConfigurationList"
        ] = None,
        publicly_accessible: Optional["aws_sdk_m2.types.boolean.Boolean"] = None,
        high_availability_config: Optional[
            "aws_sdk_m2.types.high_availability_config.HighAvailabilityConfig"
        ] = None,
        tags: Optional["aws_sdk_m2.types.tag_map.TagMap"] = None,
        preferred_maintenance_window: Optional[
            "aws_sdk_m2.types.string50.String50"
        ] = None,
        network_type: Optional["aws_sdk_m2.types.network_type.NetworkType"] = None,
        client_token: Optional["aws_sdk_m2.types.client_token.ClientToken"] = None,
        kms_key_id: Optional[str] = None,
    ) -> "aws_sdk_m2.types.create_environment_response.CreateEnvironmentResponse":
        """<p>Creates a runtime environment for a given runtime engine.</p>

        Args:
            name: <p>The name of the runtime environment. Must be unique within the account.</p>
            instance_type: <p>The type of instance for the runtime environment.</p>
            description: <p>The description of the runtime environment.</p>
            engine_type: <p>The engine type for the runtime environment.</p>
            engine_version: <p>The version of the engine type for the runtime environment.</p>
            subnet_ids: <p>The list of subnets associated with the VPC for this runtime environment.</p>
            security_group_ids: <p>The list of security groups for the VPC associated with this runtime environment.</p>
            storage_configurations: <p>Optional. The storage configurations for this runtime environment.</p>
            publicly_accessible: <p>Specifies whether the runtime environment is publicly accessible.</p>
            high_availability_config: <p>The details of a high availability configuration for this runtime environment.</p>
            tags: <p>The tags for the runtime environment.</p>
            preferred_maintenance_window: <p>Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format <code>ddd:hh24:mi-ddd:hh24:mi</code> and must be less than 24 hours. The following two examples are valid maintenance windows: <code>sun:23:45-mon:00:15</code> or <code>sat:01:00-sat:03:00</code>. </p> <p>If you do not provide a value, a random system-generated value will be assigned.</p>
            network_type: <p>The network type required for the runtime environment.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create an environment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>
            kms_key_id: <p>The identifier of a customer managed key.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_m2.types.create_environment_request.CreateEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_m2.types.create_environment_response.CreateEnvironmentResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.create_environment

            output, http_response = (
                aws_sdk_m2._operations.aws_supernova_control_plane_service.create_environment.create_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_m2.types.create_environment_request.CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["instance_type"] = instance_type
        if description is not None:
            input_["description"] = description
        input_["engine_type"] = engine_type
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if storage_configurations is not None:
            input_["storage_configurations"] = storage_configurations
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if high_availability_config is not None:
            input_["high_availability_config"] = high_availability_config
        if tags is not None:
            input_["tags"] = tags
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if network_type is not None:
            input_["network_type"] = network_type
        if client_token is not None:
            input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        environment_id: "aws_sdk_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "aws_sdk_m2.types.get_environment_response.GetEnvironmentResponse":
        """<p>Describes a specific runtime environment.</p>

        Args:
            environment_id: <p>The unique identifier of the runtime environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_m2.types.get_environment_request.GetEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_m2.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.get_environment

            output, http_response = (
                aws_sdk_m2._operations.aws_supernova_control_plane_service.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_m2.types.get_environment_request.GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        environment_id: "aws_sdk_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        desired_capacity: Optional[
            "aws_sdk_m2.types.capacity_value.CapacityValue"
        ] = None,
        instance_type: Optional["aws_sdk_m2.types.string20.String20"] = None,
        engine_version: Optional[
            "aws_sdk_m2.types.engine_version.EngineVersion"
        ] = None,
        preferred_maintenance_window: Optional[str] = None,
        apply_during_maintenance_window: Optional[
            "aws_sdk_m2.types.boolean.Boolean"
        ] = None,
        force_update: Optional["aws_sdk_m2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_m2.types.update_environment_response.UpdateEnvironmentResponse":
        """<p>Updates the configuration details for a specific runtime environment.</p>

        Args:
            environment_id: <p>The unique identifier of the runtime environment that you want to update.</p>
            desired_capacity: <p>The desired capacity for the runtime environment to update. The minimum possible value is 0 and the maximum is 100.</p>
            instance_type: <p>The instance type for the runtime environment to update.</p>
            engine_version: <p>The version of the runtime engine for the runtime environment.</p>
            preferred_maintenance_window: <p>Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format <code>ddd:hh24:mi-ddd:hh24:mi</code> and must be less than 24 hours. The following two examples are valid maintenance windows: <code>sun:23:45-mon:00:15</code> or <code>sat:01:00-sat:03:00</code>. </p> <p>If you do not provide a value, a random system-generated value will be assigned.</p>
            apply_during_maintenance_window: <p>Indicates whether to update the runtime environment during the maintenance window. The default is false. Currently, Amazon Web Services Mainframe Modernization accepts the <code>engineVersion</code> parameter only if <code>applyDuringMaintenanceWindow</code> is true. If any parameter other than <code>engineVersion</code> is provided in <code>UpdateEnvironmentRequest</code>, it will fail if <code>applyDuringMaintenanceWindow</code> is set to true.</p>
            force_update: <p>Forces the updates on the environment. This option is needed if the applications in the environment are not stopped or if there are ongoing application-related activities in the environment.</p> <p>If you use this option, be aware that it could lead to data corruption in the applications, and that you might need to perform repair and recovery procedures for the applications.</p> <p>This option is not needed if the attribute being updated is <code>preferredMaintenanceWindow</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_m2.types.update_environment_request.UpdateEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_m2.types.update_environment_response.UpdateEnvironmentResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.update_environment

            output, http_response = (
                aws_sdk_m2._operations.aws_supernova_control_plane_service.update_environment.update_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_m2.types.update_environment_request.UpdateEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["environment_id"] = environment_id
        if desired_capacity is not None:
            input_["desired_capacity"] = desired_capacity
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if apply_during_maintenance_window is not None:
            input_["apply_during_maintenance_window"] = apply_during_maintenance_window
        if force_update is not None:
            input_["force_update"] = force_update

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        environment_id: "aws_sdk_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[m2ClientConfig] = None,
    ) -> "aws_sdk_m2.types.delete_environment_response.DeleteEnvironmentResponse":
        """<p>Deletes a specific runtime environment. The environment cannot contain deployed applications. If it does, you must delete those applications before you delete the environment.</p>

        Args:
            environment_id: <p>The unique identifier of the runtime environment you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_m2.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_m2.types.delete_environment_response.DeleteEnvironmentResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.delete_environment

            output, http_response = (
                aws_sdk_m2._operations.aws_supernova_control_plane_service.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_m2.types.delete_environment_request.DeleteEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["environment_id"] = environment_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[m2ClientConfig] = None,
        next_token: Optional["aws_sdk_m2.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_m2.types.max_results.MaxResults"] = None,
        names: Optional["aws_sdk_m2.types.entity_name_list.EntityNameList"] = None,
        engine_type: Optional["aws_sdk_m2.types.engine_type.EngineType"] = None,
    ) -> "aws_sdk_m2.types.list_environments_response.ListEnvironmentsResponse":
        """<p>Lists the runtime environments.</p>

        Args:
            next_token: <p>A pagination token to control the number of runtime environments displayed in the list.</p>
            max_results: <p>The maximum number of runtime environments to return.</p>
            names: <p>The names of the runtime environments. Must be unique within the account.</p>
            engine_type: <p>The engine type for the runtime environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_m2.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_m2.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.list_environments

            output, http_response = (
                aws_sdk_m2._operations.aws_supernova_control_plane_service.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_m2.types.list_environments_request.ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if names is not None:
            input_["names"] = names
        if engine_type is not None:
            input_["engine_type"] = engine_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEnvironment:
    def __init__(self, service: Asyncm2Client) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_m2.types.entity_name.EntityName",
        instance_type: "aws_sdk_m2.types.string20.String20",
        engine_type: "aws_sdk_m2.types.engine_type.EngineType",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        description: Optional[
            "aws_sdk_m2.types.entity_description.EntityDescription"
        ] = None,
        engine_version: Optional[
            "aws_sdk_m2.types.engine_version.EngineVersion"
        ] = None,
        subnet_ids: Optional["aws_sdk_m2.types.string50_list.String50List"] = None,
        security_group_ids: Optional[
            "aws_sdk_m2.types.string50_list.String50List"
        ] = None,
        storage_configurations: Optional[
            "aws_sdk_m2.types.storage_configuration_list.StorageConfigurationList"
        ] = None,
        publicly_accessible: Optional["aws_sdk_m2.types.boolean.Boolean"] = None,
        high_availability_config: Optional[
            "aws_sdk_m2.types.high_availability_config.HighAvailabilityConfig"
        ] = None,
        tags: Optional["aws_sdk_m2.types.tag_map.TagMap"] = None,
        preferred_maintenance_window: Optional[
            "aws_sdk_m2.types.string50.String50"
        ] = None,
        network_type: Optional["aws_sdk_m2.types.network_type.NetworkType"] = None,
        client_token: Optional["aws_sdk_m2.types.client_token.ClientToken"] = None,
        kms_key_id: Optional[str] = None,
    ) -> "aws_sdk_m2.types.create_environment_response.CreateEnvironmentResponse":
        """<p>Creates a runtime environment for a given runtime engine.</p>

        Args:
            name: <p>The name of the runtime environment. Must be unique within the account.</p>
            instance_type: <p>The type of instance for the runtime environment.</p>
            description: <p>The description of the runtime environment.</p>
            engine_type: <p>The engine type for the runtime environment.</p>
            engine_version: <p>The version of the engine type for the runtime environment.</p>
            subnet_ids: <p>The list of subnets associated with the VPC for this runtime environment.</p>
            security_group_ids: <p>The list of security groups for the VPC associated with this runtime environment.</p>
            storage_configurations: <p>Optional. The storage configurations for this runtime environment.</p>
            publicly_accessible: <p>Specifies whether the runtime environment is publicly accessible.</p>
            high_availability_config: <p>The details of a high availability configuration for this runtime environment.</p>
            tags: <p>The tags for the runtime environment.</p>
            preferred_maintenance_window: <p>Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format <code>ddd:hh24:mi-ddd:hh24:mi</code> and must be less than 24 hours. The following two examples are valid maintenance windows: <code>sun:23:45-mon:00:15</code> or <code>sat:01:00-sat:03:00</code>. </p> <p>If you do not provide a value, a random system-generated value will be assigned.</p>
            network_type: <p>The network type required for the runtime environment.</p>
            client_token: <p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create an environment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires. </p>
            kms_key_id: <p>The identifier of a customer managed key.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_m2.types.create_environment_request.CreateEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_m2.types.create_environment_response.CreateEnvironmentResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.create_environment

            (
                output,
                http_response,
            ) = await aws_sdk_m2._operations.aws_supernova_control_plane_service.create_environment.async_create_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_m2.types.create_environment_request.CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["instance_type"] = instance_type
        if description is not None:
            input_["description"] = description
        input_["engine_type"] = engine_type
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if storage_configurations is not None:
            input_["storage_configurations"] = storage_configurations
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if high_availability_config is not None:
            input_["high_availability_config"] = high_availability_config
        if tags is not None:
            input_["tags"] = tags
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if network_type is not None:
            input_["network_type"] = network_type
        if client_token is not None:
            input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        environment_id: "aws_sdk_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "aws_sdk_m2.types.get_environment_response.GetEnvironmentResponse":
        """<p>Describes a specific runtime environment.</p>

        Args:
            environment_id: <p>The unique identifier of the runtime environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_m2.types.get_environment_request.GetEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_m2.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.get_environment

            (
                output,
                http_response,
            ) = await aws_sdk_m2._operations.aws_supernova_control_plane_service.get_environment.async_get_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_m2.types.get_environment_request.GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["environment_id"] = environment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        environment_id: "aws_sdk_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        desired_capacity: Optional[
            "aws_sdk_m2.types.capacity_value.CapacityValue"
        ] = None,
        instance_type: Optional["aws_sdk_m2.types.string20.String20"] = None,
        engine_version: Optional[
            "aws_sdk_m2.types.engine_version.EngineVersion"
        ] = None,
        preferred_maintenance_window: Optional[str] = None,
        apply_during_maintenance_window: Optional[
            "aws_sdk_m2.types.boolean.Boolean"
        ] = None,
        force_update: Optional["aws_sdk_m2.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_m2.types.update_environment_response.UpdateEnvironmentResponse":
        """<p>Updates the configuration details for a specific runtime environment.</p>

        Args:
            environment_id: <p>The unique identifier of the runtime environment that you want to update.</p>
            desired_capacity: <p>The desired capacity for the runtime environment to update. The minimum possible value is 0 and the maximum is 100.</p>
            instance_type: <p>The instance type for the runtime environment to update.</p>
            engine_version: <p>The version of the runtime engine for the runtime environment.</p>
            preferred_maintenance_window: <p>Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format <code>ddd:hh24:mi-ddd:hh24:mi</code> and must be less than 24 hours. The following two examples are valid maintenance windows: <code>sun:23:45-mon:00:15</code> or <code>sat:01:00-sat:03:00</code>. </p> <p>If you do not provide a value, a random system-generated value will be assigned.</p>
            apply_during_maintenance_window: <p>Indicates whether to update the runtime environment during the maintenance window. The default is false. Currently, Amazon Web Services Mainframe Modernization accepts the <code>engineVersion</code> parameter only if <code>applyDuringMaintenanceWindow</code> is true. If any parameter other than <code>engineVersion</code> is provided in <code>UpdateEnvironmentRequest</code>, it will fail if <code>applyDuringMaintenanceWindow</code> is set to true.</p>
            force_update: <p>Forces the updates on the environment. This option is needed if the applications in the environment are not stopped or if there are ongoing application-related activities in the environment.</p> <p>If you use this option, be aware that it could lead to data corruption in the applications, and that you might need to perform repair and recovery procedures for the applications.</p> <p>This option is not needed if the attribute being updated is <code>preferredMaintenanceWindow</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_m2.types.update_environment_request.UpdateEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_m2.types.update_environment_response.UpdateEnvironmentResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.update_environment

            (
                output,
                http_response,
            ) = await aws_sdk_m2._operations.aws_supernova_control_plane_service.update_environment.async_update_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_m2.types.update_environment_request.UpdateEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["environment_id"] = environment_id
        if desired_capacity is not None:
            input_["desired_capacity"] = desired_capacity
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if apply_during_maintenance_window is not None:
            input_["apply_during_maintenance_window"] = apply_during_maintenance_window
        if force_update is not None:
            input_["force_update"] = force_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        environment_id: "aws_sdk_m2.types.identifier.Identifier",
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
    ) -> "aws_sdk_m2.types.delete_environment_response.DeleteEnvironmentResponse":
        """<p>Deletes a specific runtime environment. The environment cannot contain deployed applications. If it does, you must delete those applications before you delete the environment.</p>

        Args:
            environment_id: <p>The unique identifier of the runtime environment you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_m2.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_m2.types.delete_environment_response.DeleteEnvironmentResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.delete_environment

            (
                output,
                http_response,
            ) = await aws_sdk_m2._operations.aws_supernova_control_plane_service.delete_environment.async_delete_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_m2.types.delete_environment_request.DeleteEnvironmentRequest = {}  # type: ignore[typeddict-item]
        input_["environment_id"] = environment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[Asyncm2ClientConfig] = None,
        next_token: Optional["aws_sdk_m2.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_m2.types.max_results.MaxResults"] = None,
        names: Optional["aws_sdk_m2.types.entity_name_list.EntityNameList"] = None,
        engine_type: Optional["aws_sdk_m2.types.engine_type.EngineType"] = None,
    ) -> "aws_sdk_m2.types.list_environments_response.ListEnvironmentsResponse":
        """<p>Lists the runtime environments.</p>

        Args:
            next_token: <p>A pagination token to control the number of runtime environments displayed in the list.</p>
            max_results: <p>The maximum number of runtime environments to return.</p>
            names: <p>The names of the runtime environments. Must be unique within the account.</p>
            engine_type: <p>The engine type for the runtime environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_m2.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_m2.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import aws_sdk_m2._operations.aws_supernova_control_plane_service.list_environments

            (
                output,
                http_response,
            ) = await aws_sdk_m2._operations.aws_supernova_control_plane_service.list_environments.async_list_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_m2.types.list_environments_request.ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if names is not None:
            input_["names"] = names
        if engine_type is not None:
            input_["engine_type"] = engine_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
