from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from aws_sdk_odb._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_odb.types.cloud_exadata_infrastructure_summary
    import aws_sdk_odb.types.create_cloud_exadata_infrastructure_input
    import aws_sdk_odb.types.create_cloud_exadata_infrastructure_output
    import aws_sdk_odb.types.customer_contacts
    import aws_sdk_odb.types.db_server_summary
    import aws_sdk_odb.types.delete_cloud_exadata_infrastructure_input
    import aws_sdk_odb.types.delete_cloud_exadata_infrastructure_output
    import aws_sdk_odb.types.general_input_string
    import aws_sdk_odb.types.get_cloud_exadata_infrastructure_input
    import aws_sdk_odb.types.get_cloud_exadata_infrastructure_output
    import aws_sdk_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_input
    import aws_sdk_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_output
    import aws_sdk_odb.types.get_db_server_input
    import aws_sdk_odb.types.get_db_server_output
    import aws_sdk_odb.types.list_cloud_exadata_infrastructures_input
    import aws_sdk_odb.types.list_cloud_exadata_infrastructures_output
    import aws_sdk_odb.types.list_db_servers_input
    import aws_sdk_odb.types.list_db_servers_output
    import aws_sdk_odb.types.maintenance_window
    import aws_sdk_odb.types.request_tag_map
    import aws_sdk_odb.types.resource_display_name
    import aws_sdk_odb.types.resource_id
    import aws_sdk_odb.types.resource_id_or_arn
    import aws_sdk_odb.types.string_list
    import aws_sdk_odb.types.update_cloud_exadata_infrastructure_input
    import aws_sdk_odb.types.update_cloud_exadata_infrastructure_output
    from aws_sdk_odb._services.async_odb import AsyncodbClient, AsyncodbClientConfig
    from aws_sdk_odb._services.odb import odbClient, odbClientConfig


class CloudExadataInfrastructureResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service

    def create(
        self,
        display_name: "aws_sdk_odb.types.resource_display_name.ResourceDisplayName",
        shape: "aws_sdk_odb.types.general_input_string.GeneralInputString",
        compute_count: int,
        storage_count: int,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
        tags: Optional["aws_sdk_odb.types.request_tag_map.RequestTagMap"] = None,
        customer_contacts_to_send_to_oci: Optional[
            "aws_sdk_odb.types.customer_contacts.CustomerContacts"
        ] = None,
        maintenance_window: Optional[
            "aws_sdk_odb.types.maintenance_window.MaintenanceWindow"
        ] = None,
        client_token: Optional[
            "aws_sdk_odb.types.general_input_string.GeneralInputString"
        ] = None,
        database_server_type: Optional[
            "aws_sdk_odb.types.general_input_string.GeneralInputString"
        ] = None,
        storage_server_type: Optional[
            "aws_sdk_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "aws_sdk_odb.types.create_cloud_exadata_infrastructure_output.CreateCloudExadataInfrastructureOutput":
        """<p>Creates an Exadata infrastructure.</p>

        Args:
            display_name: <p>A user-friendly name for the Exadata infrastructure.</p>
            shape: <p>The model name of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>
            availability_zone: <p>The name of the Availability Zone (AZ) where the Exadata infrastructure is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p> <p>Example: <code>us-east-1a</code> </p>
            availability_zone_id: <p>The AZ ID of the AZ where the Exadata infrastructure is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p> <p>Example: <code>use1-az1</code> </p>
            tags: <p>The list of resource tags to apply to the Exadata infrastructure.</p>
            compute_count: <p>The number of database servers for the Exadata infrastructure. Valid values for this parameter depend on the shape. To get information about the minimum and maximum values, use the <code>ListDbSystemShapes</code> operation.</p>
            customer_contacts_to_send_to_oci: <p>The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.</p>
            maintenance_window: <p>The maintenance window configuration for the Exadata Cloud infrastructure.</p> <p>This allows you to define when maintenance operations such as patching and updates can be performed on the infrastructure.</p>
            storage_count: <p>The number of storage servers to activate for this Exadata infrastructure. Valid values for this parameter depend on the shape. To get information about the minimum and maximum values, use the <code>ListDbSystemShapes</code> operation.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>
            database_server_type: <p>The database server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>
            storage_server_type: <p>The storage server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.create_cloud_exadata_infrastructure_input.CreateCloudExadataInfrastructureInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.create_cloud_exadata_infrastructure_output.CreateCloudExadataInfrastructureOutput"
        ]:
            import aws_sdk_odb._operations.odb.create_cloud_exadata_infrastructure

            output, http_response = (
                aws_sdk_odb._operations.odb.create_cloud_exadata_infrastructure.create_cloud_exadata_infrastructure(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.create_cloud_exadata_infrastructure_input.CreateCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
        input_["display_name"] = display_name
        input_["shape"] = shape
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if tags is not None:
            input_["tags"] = tags
        input_["compute_count"] = compute_count
        if customer_contacts_to_send_to_oci is not None:
            input_["customer_contacts_to_send_to_oci"] = (
                customer_contacts_to_send_to_oci
            )
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window
        input_["storage_count"] = storage_count
        if client_token is not None:
            input_["client_token"] = client_token
        if database_server_type is not None:
            input_["database_server_type"] = database_server_type
        if storage_server_type is not None:
            input_["storage_server_type"] = storage_server_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.get_cloud_exadata_infrastructure_output.GetCloudExadataInfrastructureOutput":
        """<p>Returns information about the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.get_cloud_exadata_infrastructure_input.GetCloudExadataInfrastructureInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.get_cloud_exadata_infrastructure_output.GetCloudExadataInfrastructureOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_cloud_exadata_infrastructure

            output, http_response = (
                aws_sdk_odb._operations.odb.get_cloud_exadata_infrastructure.get_cloud_exadata_infrastructure(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.get_cloud_exadata_infrastructure_input.GetCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        maintenance_window: Optional[
            "aws_sdk_odb.types.maintenance_window.MaintenanceWindow"
        ] = None,
    ) -> "aws_sdk_odb.types.update_cloud_exadata_infrastructure_output.UpdateCloudExadataInfrastructureOutput":
        """<p>Updates the properties of an Exadata infrastructure resource.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure to update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.update_cloud_exadata_infrastructure_input.UpdateCloudExadataInfrastructureInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.update_cloud_exadata_infrastructure_output.UpdateCloudExadataInfrastructureOutput"
        ]:
            import aws_sdk_odb._operations.odb.update_cloud_exadata_infrastructure

            output, http_response = (
                aws_sdk_odb._operations.odb.update_cloud_exadata_infrastructure.update_cloud_exadata_infrastructure(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.update_cloud_exadata_infrastructure_input.UpdateCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.delete_cloud_exadata_infrastructure_output.DeleteCloudExadataInfrastructureOutput":
        """<p>Deletes the specified Exadata infrastructure. Before you use this operation, make sure to delete all of the VM clusters that are hosted on this Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.delete_cloud_exadata_infrastructure_input.DeleteCloudExadataInfrastructureInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.delete_cloud_exadata_infrastructure_output.DeleteCloudExadataInfrastructureOutput"
        ]:
            import aws_sdk_odb._operations.odb.delete_cloud_exadata_infrastructure

            output, http_response = (
                aws_sdk_odb._operations.odb.delete_cloud_exadata_infrastructure.delete_cloud_exadata_infrastructure(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.delete_cloud_exadata_infrastructure_input.DeleteCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_odb.types.list_cloud_exadata_infrastructures_output.ListCloudExadataInfrastructuresOutput":
        """<p>Returns information about the Exadata infrastructures owned by your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.list_cloud_exadata_infrastructures_input.ListCloudExadataInfrastructuresInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.list_cloud_exadata_infrastructures_output.ListCloudExadataInfrastructuresOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_cloud_exadata_infrastructures

            output, http_response = (
                aws_sdk_odb._operations.odb.list_cloud_exadata_infrastructures.list_cloud_exadata_infrastructures(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_cloud_exadata_infrastructures_input.ListCloudExadataInfrastructuresInput = {}  # type: ignore[typeddict-item]
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

    def get_cloud_exadata_infrastructure_unallocated_resources(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        db_servers: Optional["aws_sdk_odb.types.string_list.StringList"] = None,
    ) -> "aws_sdk_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_output.GetCloudExadataInfrastructureUnallocatedResourcesOutput":
        """<p>Retrieves information about unallocated resources in a specified Cloud Exadata Infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Cloud Exadata infrastructure for which to retrieve unallocated resources.</p>
            db_servers: <p>The database servers to include in the unallocated resources query.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_input.GetCloudExadataInfrastructureUnallocatedResourcesInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_output.GetCloudExadataInfrastructureUnallocatedResourcesOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_cloud_exadata_infrastructure_unallocated_resources

            output, http_response = (
                aws_sdk_odb._operations.odb.get_cloud_exadata_infrastructure_unallocated_resources.get_cloud_exadata_infrastructure_unallocated_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_input.GetCloudExadataInfrastructureUnallocatedResourcesInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id
        if db_servers is not None:
            input_["db_servers"] = db_servers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_db_server(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        db_server_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.get_db_server_output.GetDbServerOutput":
        """<p>Returns information about the specified database server.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Oracle Exadata infrastructure that contains the database server.</p>
            db_server_id: <p>The unique identifier of the database server to retrieve information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.get_db_server_input.GetDbServerInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.get_db_server_output.GetDbServerOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_db_server

            output, http_response = (
                aws_sdk_odb._operations.odb.get_db_server.get_db_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.get_db_server_input.GetDbServerInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id
        input_["db_server_id"] = db_server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_db_servers(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_odb.types.list_db_servers_output.ListDbServersOutput":
        """<p>Returns information about the database servers that belong to the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Oracle Exadata infrastructure.</p>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.list_db_servers_input.ListDbServersInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.list_db_servers_output.ListDbServersOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_db_servers

            output, http_response = (
                aws_sdk_odb._operations.odb.list_db_servers.list_db_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_db_servers_input.ListDbServersInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id
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


class AsyncCloudExadataInfrastructureResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service

    async def create(
        self,
        display_name: "aws_sdk_odb.types.resource_display_name.ResourceDisplayName",
        shape: "aws_sdk_odb.types.general_input_string.GeneralInputString",
        compute_count: int,
        storage_count: int,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
        tags: Optional["aws_sdk_odb.types.request_tag_map.RequestTagMap"] = None,
        customer_contacts_to_send_to_oci: Optional[
            "aws_sdk_odb.types.customer_contacts.CustomerContacts"
        ] = None,
        maintenance_window: Optional[
            "aws_sdk_odb.types.maintenance_window.MaintenanceWindow"
        ] = None,
        client_token: Optional[
            "aws_sdk_odb.types.general_input_string.GeneralInputString"
        ] = None,
        database_server_type: Optional[
            "aws_sdk_odb.types.general_input_string.GeneralInputString"
        ] = None,
        storage_server_type: Optional[
            "aws_sdk_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "aws_sdk_odb.types.create_cloud_exadata_infrastructure_output.CreateCloudExadataInfrastructureOutput":
        """<p>Creates an Exadata infrastructure.</p>

        Args:
            display_name: <p>A user-friendly name for the Exadata infrastructure.</p>
            shape: <p>The model name of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>
            availability_zone: <p>The name of the Availability Zone (AZ) where the Exadata infrastructure is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p> <p>Example: <code>us-east-1a</code> </p>
            availability_zone_id: <p>The AZ ID of the AZ where the Exadata infrastructure is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p> <p>Example: <code>use1-az1</code> </p>
            tags: <p>The list of resource tags to apply to the Exadata infrastructure.</p>
            compute_count: <p>The number of database servers for the Exadata infrastructure. Valid values for this parameter depend on the shape. To get information about the minimum and maximum values, use the <code>ListDbSystemShapes</code> operation.</p>
            customer_contacts_to_send_to_oci: <p>The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.</p>
            maintenance_window: <p>The maintenance window configuration for the Exadata Cloud infrastructure.</p> <p>This allows you to define when maintenance operations such as patching and updates can be performed on the infrastructure.</p>
            storage_count: <p>The number of storage servers to activate for this Exadata infrastructure. Valid values for this parameter depend on the shape. To get information about the minimum and maximum values, use the <code>ListDbSystemShapes</code> operation.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>
            database_server_type: <p>The database server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>
            storage_server_type: <p>The storage server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.create_cloud_exadata_infrastructure_input.CreateCloudExadataInfrastructureInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.create_cloud_exadata_infrastructure_output.CreateCloudExadataInfrastructureOutput"
        ]:
            import aws_sdk_odb._operations.odb.create_cloud_exadata_infrastructure

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.create_cloud_exadata_infrastructure.async_create_cloud_exadata_infrastructure(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.create_cloud_exadata_infrastructure_input.CreateCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
        input_["display_name"] = display_name
        input_["shape"] = shape
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if tags is not None:
            input_["tags"] = tags
        input_["compute_count"] = compute_count
        if customer_contacts_to_send_to_oci is not None:
            input_["customer_contacts_to_send_to_oci"] = (
                customer_contacts_to_send_to_oci
            )
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window
        input_["storage_count"] = storage_count
        if client_token is not None:
            input_["client_token"] = client_token
        if database_server_type is not None:
            input_["database_server_type"] = database_server_type
        if storage_server_type is not None:
            input_["storage_server_type"] = storage_server_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "aws_sdk_odb.types.get_cloud_exadata_infrastructure_output.GetCloudExadataInfrastructureOutput":
        """<p>Returns information about the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.get_cloud_exadata_infrastructure_input.GetCloudExadataInfrastructureInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.get_cloud_exadata_infrastructure_output.GetCloudExadataInfrastructureOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_cloud_exadata_infrastructure

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.get_cloud_exadata_infrastructure.async_get_cloud_exadata_infrastructure(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.get_cloud_exadata_infrastructure_input.GetCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        maintenance_window: Optional[
            "aws_sdk_odb.types.maintenance_window.MaintenanceWindow"
        ] = None,
    ) -> "aws_sdk_odb.types.update_cloud_exadata_infrastructure_output.UpdateCloudExadataInfrastructureOutput":
        """<p>Updates the properties of an Exadata infrastructure resource.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure to update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.update_cloud_exadata_infrastructure_input.UpdateCloudExadataInfrastructureInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.update_cloud_exadata_infrastructure_output.UpdateCloudExadataInfrastructureOutput"
        ]:
            import aws_sdk_odb._operations.odb.update_cloud_exadata_infrastructure

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.update_cloud_exadata_infrastructure.async_update_cloud_exadata_infrastructure(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.update_cloud_exadata_infrastructure_input.UpdateCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "aws_sdk_odb.types.delete_cloud_exadata_infrastructure_output.DeleteCloudExadataInfrastructureOutput":
        """<p>Deletes the specified Exadata infrastructure. Before you use this operation, make sure to delete all of the VM clusters that are hosted on this Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.delete_cloud_exadata_infrastructure_input.DeleteCloudExadataInfrastructureInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.delete_cloud_exadata_infrastructure_output.DeleteCloudExadataInfrastructureOutput"
        ]:
            import aws_sdk_odb._operations.odb.delete_cloud_exadata_infrastructure

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.delete_cloud_exadata_infrastructure.async_delete_cloud_exadata_infrastructure(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.delete_cloud_exadata_infrastructure_input.DeleteCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_odb.types.list_cloud_exadata_infrastructures_output.ListCloudExadataInfrastructuresOutput":
        """<p>Returns information about the Exadata infrastructures owned by your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.list_cloud_exadata_infrastructures_input.ListCloudExadataInfrastructuresInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.list_cloud_exadata_infrastructures_output.ListCloudExadataInfrastructuresOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_cloud_exadata_infrastructures

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.list_cloud_exadata_infrastructures.async_list_cloud_exadata_infrastructures(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_cloud_exadata_infrastructures_input.ListCloudExadataInfrastructuresInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_cloud_exadata_infrastructure_unallocated_resources(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        db_servers: Optional["aws_sdk_odb.types.string_list.StringList"] = None,
    ) -> "aws_sdk_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_output.GetCloudExadataInfrastructureUnallocatedResourcesOutput":
        """<p>Retrieves information about unallocated resources in a specified Cloud Exadata Infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Cloud Exadata infrastructure for which to retrieve unallocated resources.</p>
            db_servers: <p>The database servers to include in the unallocated resources query.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_input.GetCloudExadataInfrastructureUnallocatedResourcesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_output.GetCloudExadataInfrastructureUnallocatedResourcesOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_cloud_exadata_infrastructure_unallocated_resources

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.get_cloud_exadata_infrastructure_unallocated_resources.async_get_cloud_exadata_infrastructure_unallocated_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_input.GetCloudExadataInfrastructureUnallocatedResourcesInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id
        if db_servers is not None:
            input_["db_servers"] = db_servers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_db_server(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        db_server_id: "aws_sdk_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "aws_sdk_odb.types.get_db_server_output.GetDbServerOutput":
        """<p>Returns information about the specified database server.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Oracle Exadata infrastructure that contains the database server.</p>
            db_server_id: <p>The unique identifier of the database server to retrieve information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.get_db_server_input.GetDbServerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.get_db_server_output.GetDbServerOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_db_server

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.get_db_server.async_get_db_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.get_db_server_input.GetDbServerInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id
        input_["db_server_id"] = db_server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_db_servers(
        self,
        cloud_exadata_infrastructure_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_odb.types.list_db_servers_output.ListDbServersOutput":
        """<p>Returns information about the database servers that belong to the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Oracle Exadata infrastructure.</p>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.list_db_servers_input.ListDbServersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.list_db_servers_output.ListDbServersOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_db_servers

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.list_db_servers.async_list_db_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_db_servers_input.ListDbServersInput = {}  # type: ignore[typeddict-item]
        input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
