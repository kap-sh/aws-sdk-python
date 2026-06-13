from typing import TYPE_CHECKING, Optional

import aws_sdk_mgn._auth._signers
import aws_sdk_mgn._auth._sigv4
from aws_sdk_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.action_category
    import aws_sdk_mgn.types.action_description
    import aws_sdk_mgn.types.action_id
    import aws_sdk_mgn.types.action_name
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.bandwidth_throttling
    import aws_sdk_mgn.types.boot_mode
    import aws_sdk_mgn.types.bounded_string
    import aws_sdk_mgn.types.change_server_life_cycle_state_request
    import aws_sdk_mgn.types.change_server_life_cycle_state_source_server_lifecycle
    import aws_sdk_mgn.types.delete_source_server_request
    import aws_sdk_mgn.types.delete_source_server_response
    import aws_sdk_mgn.types.describe_source_servers_request
    import aws_sdk_mgn.types.describe_source_servers_request_filters
    import aws_sdk_mgn.types.describe_source_servers_response
    import aws_sdk_mgn.types.disconnect_from_service_request
    import aws_sdk_mgn.types.document_version
    import aws_sdk_mgn.types.ec2_instance_type
    import aws_sdk_mgn.types.finalize_cutover_request
    import aws_sdk_mgn.types.get_launch_configuration_request
    import aws_sdk_mgn.types.get_replication_configuration_request
    import aws_sdk_mgn.types.internet_protocol
    import aws_sdk_mgn.types.launch_configuration
    import aws_sdk_mgn.types.launch_disposition
    import aws_sdk_mgn.types.licensing
    import aws_sdk_mgn.types.list_source_server_actions_request
    import aws_sdk_mgn.types.list_source_server_actions_response
    import aws_sdk_mgn.types.mark_as_archived_request
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.order_type
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.pause_replication_request
    import aws_sdk_mgn.types.post_launch_actions
    import aws_sdk_mgn.types.put_source_server_action_request
    import aws_sdk_mgn.types.remove_source_server_action_request
    import aws_sdk_mgn.types.remove_source_server_action_response
    import aws_sdk_mgn.types.replication_configuration
    import aws_sdk_mgn.types.replication_configuration_data_plane_routing
    import aws_sdk_mgn.types.replication_configuration_default_large_staging_disk_type
    import aws_sdk_mgn.types.replication_configuration_ebs_encryption
    import aws_sdk_mgn.types.replication_configuration_replicated_disks
    import aws_sdk_mgn.types.replication_servers_security_groups_i_ds
    import aws_sdk_mgn.types.replication_type
    import aws_sdk_mgn.types.resume_replication_request
    import aws_sdk_mgn.types.retry_data_replication_request
    import aws_sdk_mgn.types.small_bounded_string
    import aws_sdk_mgn.types.source_server
    import aws_sdk_mgn.types.source_server_action_document
    import aws_sdk_mgn.types.source_server_actions_request_filters
    import aws_sdk_mgn.types.source_server_connector_action
    import aws_sdk_mgn.types.source_server_id
    import aws_sdk_mgn.types.ssm_document_external_parameters
    import aws_sdk_mgn.types.ssm_document_parameters
    import aws_sdk_mgn.types.start_cutover_request
    import aws_sdk_mgn.types.start_cutover_request_source_server_i_ds
    import aws_sdk_mgn.types.start_cutover_response
    import aws_sdk_mgn.types.start_replication_request
    import aws_sdk_mgn.types.start_test_request
    import aws_sdk_mgn.types.start_test_request_source_server_i_ds
    import aws_sdk_mgn.types.start_test_response
    import aws_sdk_mgn.types.stop_replication_request
    import aws_sdk_mgn.types.strictly_positive_integer
    import aws_sdk_mgn.types.subnet_id
    import aws_sdk_mgn.types.tag_value
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.target_instance_type_right_sizing_method
    import aws_sdk_mgn.types.terminate_target_instances_request
    import aws_sdk_mgn.types.terminate_target_instances_request_source_server_i_ds
    import aws_sdk_mgn.types.terminate_target_instances_response
    import aws_sdk_mgn.types.update_launch_configuration_request
    import aws_sdk_mgn.types.update_replication_configuration_request
    import aws_sdk_mgn.types.update_source_server_replication_type_request
    import aws_sdk_mgn.types.update_source_server_request
    from aws_sdk_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from aws_sdk_mgn._services.mgn import mgnClient, mgnClientConfig


class SourceServerResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def update(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
        connector_action: Optional[
            "aws_sdk_mgn.types.source_server_connector_action.SourceServerConnectorAction"
        ] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Update Source Server.</p>

        Args:
            account_id: <p>Update Source Server request account ID.</p>
            source_server_id: <p>Update Source Server request source server ID.</p>
            connector_action: <p>Update Source Server request connector action.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.update_source_server_request.UpdateSourceServerRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.update_source_server

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.update_source_server.update_source_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_source_server_request.UpdateSourceServerRequest = {}  # type: ignore[typeddict-item]
        if account_id is not None:
            input["account_id"] = account_id
        input["source_server_id"] = source_server_id
        if connector_action is not None:
            input["connector_action"] = connector_action

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.delete_source_server_response.DeleteSourceServerResponse":
        """<p>Deletes a single source server by ID.</p>

        Args:
            source_server_id: <p>Request to delete Source Server from service by Server ID.</p>
            account_id: <p>Request to delete Source Server from service by Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.delete_source_server_request.DeleteSourceServerRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.delete_source_server_response.DeleteSourceServerResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.delete_source_server

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.delete_source_server.delete_source_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.delete_source_server_request.DeleteSourceServerRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.describe_source_servers_response.DescribeSourceServersResponse":
        """<p>Retrieves all SourceServers or multiple SourceServers by ID.</p>

        Args:
            filters: <p>Request to filter Source Servers list.</p>
            max_results: <p>Request to filter Source Servers list by maximum results.</p>
            next_token: <p>Request to filter Source Servers list by next token.</p>
            account_id: <p>Request to filter Source Servers list by Accoun ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.describe_source_servers_request.DescribeSourceServersRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.describe_source_servers_response.DescribeSourceServersResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.describe_source_servers

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.describe_source_servers.describe_source_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.describe_source_servers_request.DescribeSourceServersRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def change_server_life_cycle_state(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        life_cycle: "aws_sdk_mgn.types.change_server_life_cycle_state_source_server_lifecycle.ChangeServerLifeCycleStateSourceServerLifecycle",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Allows the user to set the SourceServer.LifeCycle.state property for specific Source Server IDs to one of the following: READY_FOR_TEST or READY_FOR_CUTOVER. This command only works if the Source Server is already launchable (dataReplicationInfo.lagDuration is not null.)</p>

        Args:
            source_server_id: <p>The request to change the source server migration lifecycle state by source server ID.</p>
            life_cycle: <p>The request to change the source server migration lifecycle state.</p>
            account_id: <p>The request to change the source server migration account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.change_server_life_cycle_state_request.ChangeServerLifeCycleStateRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.change_server_life_cycle_state

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.change_server_life_cycle_state.change_server_life_cycle_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.change_server_life_cycle_state_request.ChangeServerLifeCycleStateRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        input["life_cycle"] = life_cycle
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disconnect_from_service(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Disconnects specific Source Servers from Application Migration Service. Data replication is stopped immediately. All AWS resources created by Application Migration Service for enabling the replication of these source servers will be terminated / deleted within 90 minutes. Launched Test or Cutover instances will NOT be terminated. If the agent on the source server has not been prevented from communicating with the Application Migration Service service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>Request to disconnect Source Server from service by Server ID.</p>
            account_id: <p>Request to disconnect Source Server from service by Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.disconnect_from_service_request.DisconnectFromServiceRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.disconnect_from_service

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.disconnect_from_service.disconnect_from_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.disconnect_from_service_request.DisconnectFromServiceRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def finalize_cutover(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Finalizes the cutover immediately for specific Source Servers. All AWS resources created by Application Migration Service for enabling the replication of these source servers will be terminated / deleted within 90 minutes. Launched Test or Cutover instances will NOT be terminated. The AWS Replication Agent will receive a command to uninstall itself (within 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be changed to DISCONNECTED; The SourceServer.lifeCycle.state will be changed to CUTOVER; The totalStorageBytes property fo each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>Request to finalize Cutover by Source Server ID.</p>
            account_id: <p>Request to finalize Cutover by Source Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.finalize_cutover_request.FinalizeCutoverRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.finalize_cutover

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.finalize_cutover.finalize_cutover(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.finalize_cutover_request.FinalizeCutoverRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_launch_configuration(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.launch_configuration.LaunchConfiguration":
        """<p>Lists all LaunchConfigurations available, filtered by Source Server IDs.</p>

        Args:
            source_server_id: <p>Request to get Launch Configuration information by Source Server ID.</p>
            account_id: <p>Request to get Launch Configuration information by Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.get_launch_configuration_request.GetLaunchConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.launch_configuration.LaunchConfiguration"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.get_launch_configuration

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.get_launch_configuration.get_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.get_launch_configuration_request.GetLaunchConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_replication_configuration(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.replication_configuration.ReplicationConfiguration":
        """<p>Lists all ReplicationConfigurations, filtered by Source Server ID.</p>

        Args:
            source_server_id: <p>Request to get Replication Configuration by Source Server ID.</p>
            account_id: <p>Request to get Replication Configuration by Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.get_replication_configuration_request.GetReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.replication_configuration.ReplicationConfiguration"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.get_replication_configuration

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.get_replication_configuration.get_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.get_replication_configuration_request.GetReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_source_server_actions(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.source_server_actions_request_filters.SourceServerActionsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.list_source_server_actions_response.ListSourceServerActionsResponse":
        """<p>List source server post migration custom actions.</p>

        Args:
            source_server_id: <p>Source server ID.</p>
            filters: <p>Filters to apply when listing source server post migration custom actions.</p>
            max_results: <p>Maximum amount of items to return when listing source server post migration custom actions.</p>
            next_token: <p>Next token to use when listing source server post migration custom actions.</p>
            account_id: <p>Account ID to return when listing source server post migration custom actions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.list_source_server_actions_request.ListSourceServerActionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.list_source_server_actions_response.ListSourceServerActionsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_source_server_actions

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.list_source_server_actions.list_source_server_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.list_source_server_actions_request.ListSourceServerActionsRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def mark_as_archived(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Archives specific Source Servers by setting the SourceServer.isArchived property to true for specified SourceServers by ID. This command only works for SourceServers with a lifecycle. state which equals DISCONNECTED or CUTOVER.</p>

        Args:
            source_server_id: <p>Mark as archived by Source Server ID.</p>
            account_id: <p>Mark as archived by Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.mark_as_archived_request.MarkAsArchivedRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.mark_as_archived

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.mark_as_archived.mark_as_archived(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.mark_as_archived_request.MarkAsArchivedRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def pause_replication(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Pause Replication.</p>

        Args:
            source_server_id: <p>Pause Replication Request source server ID.</p>
            account_id: <p>Pause Replication Request account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.pause_replication_request.PauseReplicationRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.pause_replication

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.pause_replication.pause_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.pause_replication_request.PauseReplicationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_source_server_action(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        action_name: "aws_sdk_mgn.types.action_name.ActionName",
        document_identifier: "aws_sdk_mgn.types.bounded_string.BoundedString",
        order: "aws_sdk_mgn.types.order_type.OrderType",
        action_id: "aws_sdk_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        document_version: Optional[
            "aws_sdk_mgn.types.document_version.DocumentVersion"
        ] = None,
        active: Optional[bool] = None,
        timeout_seconds: Optional[
            "aws_sdk_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        must_succeed_for_cutover: Optional[bool] = None,
        parameters: Optional[
            "aws_sdk_mgn.types.ssm_document_parameters.SsmDocumentParameters"
        ] = None,
        external_parameters: Optional[
            "aws_sdk_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
        ] = None,
        description: Optional[
            "aws_sdk_mgn.types.action_description.ActionDescription"
        ] = None,
        category: Optional["aws_sdk_mgn.types.action_category.ActionCategory"] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server_action_document.SourceServerActionDocument":
        """<p>Put source server post migration custom action.</p>

        Args:
            source_server_id: <p>Source server ID.</p>
            action_name: <p>Source server post migration custom action name.</p>
            document_identifier: <p>Source server post migration custom action document identifier.</p>
            order: <p>Source server post migration custom action order.</p>
            action_id: <p>Source server post migration custom action ID.</p>
            document_version: <p>Source server post migration custom action document version.</p>
            active: <p>Source server post migration custom action active status.</p>
            timeout_seconds: <p>Source server post migration custom action timeout in seconds.</p>
            must_succeed_for_cutover: <p>Source server post migration custom action must succeed for cutover.</p>
            parameters: <p>Source server post migration custom action parameters.</p>
            external_parameters: <p>Source server post migration custom action external parameters.</p>
            description: <p>Source server post migration custom action description.</p>
            category: <p>Source server post migration custom action category.</p>
            account_id: <p>Source server post migration custom account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.put_source_server_action_request.PutSourceServerActionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.source_server_action_document.SourceServerActionDocument"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.put_source_server_action

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.put_source_server_action.put_source_server_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.put_source_server_action_request.PutSourceServerActionRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        input["action_name"] = action_name
        input["document_identifier"] = document_identifier
        input["order"] = order
        input["action_id"] = action_id
        if document_version is not None:
            input["document_version"] = document_version
        if active is not None:
            input["active"] = active
        if timeout_seconds is not None:
            input["timeout_seconds"] = timeout_seconds
        if must_succeed_for_cutover is not None:
            input["must_succeed_for_cutover"] = must_succeed_for_cutover
        if parameters is not None:
            input["parameters"] = parameters
        if external_parameters is not None:
            input["external_parameters"] = external_parameters
        if description is not None:
            input["description"] = description
        if category is not None:
            input["category"] = category
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_source_server_action(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        action_id: "aws_sdk_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.remove_source_server_action_response.RemoveSourceServerActionResponse":
        """<p>Remove source server post migration custom action.</p>

        Args:
            source_server_id: <p>Source server ID of the post migration custom action to remove.</p>
            action_id: <p>Source server post migration custom action ID to remove.</p>
            account_id: <p>Source server post migration account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.remove_source_server_action_request.RemoveSourceServerActionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.remove_source_server_action_response.RemoveSourceServerActionResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.remove_source_server_action

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.remove_source_server_action.remove_source_server_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.remove_source_server_action_request.RemoveSourceServerActionRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        input["action_id"] = action_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def resume_replication(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Resume Replication.</p>

        Args:
            source_server_id: <p>Resume Replication Request source server ID.</p>
            account_id: <p>Resume Replication Request account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.resume_replication_request.ResumeReplicationRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.resume_replication

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.resume_replication.resume_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.resume_replication_request.ResumeReplicationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def retry_data_replication(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Causes the data replication initiation sequence to begin immediately upon next Handshake for specified SourceServer IDs, regardless of when the previous initiation started. This command will not work if the SourceServer is not stalled or is in a DISCONNECTED or STOPPED state.</p>

        Args:
            source_server_id: <p>Retry data replication for Source Server ID.</p>
            account_id: <p>Retry data replication for Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.retry_data_replication_request.RetryDataReplicationRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.retry_data_replication

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.retry_data_replication.retry_data_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.retry_data_replication_request.RetryDataReplicationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_replication(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Start replication for source server irrespective of its replication type.</p>

        Args:
            source_server_id: <p>ID of source server on which to start replication.</p>
            account_id: <p>Account ID on which to start replication.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.start_replication_request.StartReplicationRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.start_replication

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.start_replication.start_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.start_replication_request.StartReplicationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_replication(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Stop Replication.</p>

        Args:
            source_server_id: <p>Stop Replication Request source server ID.</p>
            account_id: <p>Stop Replication Request account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.stop_replication_request.StopReplicationRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.stop_replication

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.stop_replication.stop_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.stop_replication_request.StopReplicationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_launch_configuration(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional[
            "aws_sdk_mgn.types.small_bounded_string.SmallBoundedString"
        ] = None,
        launch_disposition: Optional[
            "aws_sdk_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "aws_sdk_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["aws_sdk_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["aws_sdk_mgn.types.boot_mode.BootMode"] = None,
        post_launch_actions: Optional[
            "aws_sdk_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional[
            "aws_sdk_mgn.types.tag_value.TagValue"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.launch_configuration.LaunchConfiguration":
        """<p>Updates multiple LaunchConfigurations by Source Server ID.</p> <note> <p>bootMode valid values are <code>LEGACY_BIOS | UEFI</code> </p> </note>

        Args:
            source_server_id: <p>Update Launch configuration by Source Server ID request.</p>
            name: <p>Update Launch configuration name request.</p>
            launch_disposition: <p>Update Launch configuration launch disposition request.</p>
            target_instance_type_right_sizing_method: <p>Update Launch configuration Target instance right sizing request.</p>
            copy_private_ip: <p>Update Launch configuration copy Private IP request.</p>
            copy_tags: <p>Update Launch configuration copy Tags request.</p>
            licensing: <p>Update Launch configuration licensing request.</p>
            boot_mode: <p>Update Launch configuration boot mode request.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration map auto tagging MPE ID.</p>
            account_id: <p>Update Launch configuration Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.launch_configuration.LaunchConfiguration"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.update_launch_configuration

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.update_launch_configuration.update_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if name is not None:
            input["name"] = name
        if launch_disposition is not None:
            input["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input["copy_tags"] = copy_tags
        if licensing is not None:
            input["licensing"] = licensing
        if boot_mode is not None:
            input["boot_mode"] = boot_mode
        if post_launch_actions is not None:
            input["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_replication_configuration(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional[
            "aws_sdk_mgn.types.small_bounded_string.SmallBoundedString"
        ] = None,
        staging_area_subnet_id: Optional["aws_sdk_mgn.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "aws_sdk_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "aws_sdk_mgn.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "aws_sdk_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        replicated_disks: Optional[
            "aws_sdk_mgn.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
        ] = None,
        ebs_encryption: Optional[
            "aws_sdk_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["aws_sdk_mgn.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "aws_sdk_mgn.types.bandwidth_throttling.BandwidthThrottling"
        ] = None,
        data_plane_routing: Optional[
            "aws_sdk_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        use_fips_endpoint: Optional[bool] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
        internet_protocol: Optional[
            "aws_sdk_mgn.types.internet_protocol.InternetProtocol"
        ] = None,
        store_snapshot_on_local_zone: Optional[bool] = None,
    ) -> "aws_sdk_mgn.types.replication_configuration.ReplicationConfiguration":
        """<p>Allows you to update multiple ReplicationConfigurations by Source Server ID.</p>

        Args:
            source_server_id: <p>Update replication configuration Source Server ID request.</p>
            name: <p>Update replication configuration name request.</p>
            staging_area_subnet_id: <p>Update replication configuration Staging Area subnet request.</p>
            associate_default_security_group: <p>Update replication configuration associate default Application Migration Service Security group request.</p>
            replication_servers_security_groups_i_ds: <p>Update replication configuration Replication Server Security Groups IDs request.</p>
            replication_server_instance_type: <p>Update replication configuration Replication Server instance type request.</p>
            use_dedicated_replication_server: <p>Update replication configuration use dedicated Replication Server request.</p>
            default_large_staging_disk_type: <p>Update replication configuration use default large Staging Disk type request.</p>
            replicated_disks: <p>Update replication configuration replicated disks request.</p>
            ebs_encryption: <p>Update replication configuration EBS encryption request.</p>
            ebs_encryption_key_arn: <p>Update replication configuration EBS encryption key ARN request.</p>
            bandwidth_throttling: <p>Update replication configuration bandwidth throttling request.</p>
            data_plane_routing: <p>Update replication configuration data plane routing request.</p>
            create_public_ip: <p>Update replication configuration create Public IP request.</p>
            staging_area_tags: <p>Update replication configuration Staging Area Tags request.</p>
            use_fips_endpoint: <p>Update replication configuration use Fips Endpoint.</p>
            account_id: <p>Update replication configuration Account ID request.</p>
            internet_protocol: <p>Update replication configuration internet protocol.</p>
            store_snapshot_on_local_zone: <p>Update replication configuration store snapshot on local zone.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.replication_configuration.ReplicationConfiguration"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.update_replication_configuration

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.update_replication_configuration.update_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if name is not None:
            input["name"] = name
        if staging_area_subnet_id is not None:
            input["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input["associate_default_security_group"] = associate_default_security_group
        if replication_servers_security_groups_i_ds is not None:
            input["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input["replication_server_instance_type"] = replication_server_instance_type
        if use_dedicated_replication_server is not None:
            input["use_dedicated_replication_server"] = use_dedicated_replication_server
        if default_large_staging_disk_type is not None:
            input["default_large_staging_disk_type"] = default_large_staging_disk_type
        if replicated_disks is not None:
            input["replicated_disks"] = replicated_disks
        if ebs_encryption is not None:
            input["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input["staging_area_tags"] = staging_area_tags
        if use_fips_endpoint is not None:
            input["use_fips_endpoint"] = use_fips_endpoint
        if account_id is not None:
            input["account_id"] = account_id
        if internet_protocol is not None:
            input["internet_protocol"] = internet_protocol
        if store_snapshot_on_local_zone is not None:
            input["store_snapshot_on_local_zone"] = store_snapshot_on_local_zone

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_source_server_replication_type(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        replication_type: "aws_sdk_mgn.types.replication_type.ReplicationType",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Allows you to change between the AGENT_BASED replication type and the SNAPSHOT_SHIPPING replication type. </p> <p>SNAPSHOT_SHIPPING should be used for agentless replication.</p>

        Args:
            source_server_id: <p>ID of source server on which to update replication type.</p>
            replication_type: <p>Replication type to which to update source server.</p>
            account_id: <p>Account ID on which to update replication type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.update_source_server_replication_type_request.UpdateSourceServerReplicationTypeRequest]",
        ) -> OperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.update_source_server_replication_type

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.update_source_server_replication_type.update_source_server_replication_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_source_server_replication_type_request.UpdateSourceServerReplicationTypeRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        input["replication_type"] = replication_type
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_cutover(
        self,
        source_server_i_ds: "aws_sdk_mgn.types.start_cutover_request_source_server_i_ds.StartCutoverRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.start_cutover_response.StartCutoverResponse":
        """<p>Launches a Cutover Instance for specific Source Servers. This command starts a LAUNCH job whose initiatedBy property is StartCutover and changes the SourceServer.lifeCycle.state property to CUTTING_OVER.</p>

        Args:
            source_server_i_ds: <p>Start Cutover by Source Server IDs.</p>
            tags: <p>Start Cutover by Tags.</p>
            account_id: <p>Start Cutover by Account IDs</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.start_cutover_request.StartCutoverRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.start_cutover_response.StartCutoverResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_cutover

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.start_cutover.start_cutover(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.start_cutover_request.StartCutoverRequest = {}  # type: ignore[typeddict-item]
        input["source_server_i_ds"] = source_server_i_ds
        if tags is not None:
            input["tags"] = tags
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_test(
        self,
        source_server_i_ds: "aws_sdk_mgn.types.start_test_request_source_server_i_ds.StartTestRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.start_test_response.StartTestResponse":
        """<p>Launches a Test Instance for specific Source Servers. This command starts a LAUNCH job whose initiatedBy property is StartTest and changes the SourceServer.lifeCycle.state property to TESTING.</p>

        Args:
            source_server_i_ds: <p>Start Test for Source Server IDs.</p>
            tags: <p>Start Test by Tags.</p>
            account_id: <p>Start Test for Account ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.start_test_request.StartTestRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.start_test_response.StartTestResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_test

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.start_test.start_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.start_test_request.StartTestRequest = {}  # type: ignore[typeddict-item]
        input["source_server_i_ds"] = source_server_i_ds
        if tags is not None:
            input["tags"] = tags
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def terminate_target_instances(
        self,
        source_server_i_ds: "aws_sdk_mgn.types.terminate_target_instances_request_source_server_i_ds.TerminateTargetInstancesRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse":
        """<p>Starts a job that terminates specific launched EC2 Test and Cutover instances. This command will not work for any Source Server with a lifecycle.state of TESTING, CUTTING_OVER, or CUTOVER.</p>

        Args:
            source_server_i_ds: <p>Terminate Target instance by Source Server IDs.</p>
            tags: <p>Terminate Target instance by Tags.</p>
            account_id: <p>Terminate Target instance by Account ID</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.terminate_target_instances

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.terminate_target_instances.terminate_target_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest = {}  # type: ignore[typeddict-item]
        input["source_server_i_ds"] = source_server_i_ds
        if tags is not None:
            input["tags"] = tags
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncSourceServerResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def update(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
        connector_action: Optional[
            "aws_sdk_mgn.types.source_server_connector_action.SourceServerConnectorAction"
        ] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Update Source Server.</p>

        Args:
            account_id: <p>Update Source Server request account ID.</p>
            source_server_id: <p>Update Source Server request source server ID.</p>
            connector_action: <p>Update Source Server request connector action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.update_source_server_request.UpdateSourceServerRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.update_source_server

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.update_source_server.async_update_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_source_server_request.UpdateSourceServerRequest = {}  # type: ignore[typeddict-item]
        if account_id is not None:
            input["account_id"] = account_id
        input["source_server_id"] = source_server_id
        if connector_action is not None:
            input["connector_action"] = connector_action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.delete_source_server_response.DeleteSourceServerResponse":
        """<p>Deletes a single source server by ID.</p>

        Args:
            source_server_id: <p>Request to delete Source Server from service by Server ID.</p>
            account_id: <p>Request to delete Source Server from service by Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.delete_source_server_request.DeleteSourceServerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.delete_source_server_response.DeleteSourceServerResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.delete_source_server

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.delete_source_server.async_delete_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.delete_source_server_request.DeleteSourceServerRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.describe_source_servers_response.DescribeSourceServersResponse":
        """<p>Retrieves all SourceServers or multiple SourceServers by ID.</p>

        Args:
            filters: <p>Request to filter Source Servers list.</p>
            max_results: <p>Request to filter Source Servers list by maximum results.</p>
            next_token: <p>Request to filter Source Servers list by next token.</p>
            account_id: <p>Request to filter Source Servers list by Accoun ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.describe_source_servers_request.DescribeSourceServersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.describe_source_servers_response.DescribeSourceServersResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.describe_source_servers

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.describe_source_servers.async_describe_source_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.describe_source_servers_request.DescribeSourceServersRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def change_server_life_cycle_state(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        life_cycle: "aws_sdk_mgn.types.change_server_life_cycle_state_source_server_lifecycle.ChangeServerLifeCycleStateSourceServerLifecycle",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Allows the user to set the SourceServer.LifeCycle.state property for specific Source Server IDs to one of the following: READY_FOR_TEST or READY_FOR_CUTOVER. This command only works if the Source Server is already launchable (dataReplicationInfo.lagDuration is not null.)</p>

        Args:
            source_server_id: <p>The request to change the source server migration lifecycle state by source server ID.</p>
            life_cycle: <p>The request to change the source server migration lifecycle state.</p>
            account_id: <p>The request to change the source server migration account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.change_server_life_cycle_state_request.ChangeServerLifeCycleStateRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.change_server_life_cycle_state

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.change_server_life_cycle_state.async_change_server_life_cycle_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.change_server_life_cycle_state_request.ChangeServerLifeCycleStateRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        input["life_cycle"] = life_cycle
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disconnect_from_service(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Disconnects specific Source Servers from Application Migration Service. Data replication is stopped immediately. All AWS resources created by Application Migration Service for enabling the replication of these source servers will be terminated / deleted within 90 minutes. Launched Test or Cutover instances will NOT be terminated. If the agent on the source server has not been prevented from communicating with the Application Migration Service service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>Request to disconnect Source Server from service by Server ID.</p>
            account_id: <p>Request to disconnect Source Server from service by Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.disconnect_from_service_request.DisconnectFromServiceRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.disconnect_from_service

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.disconnect_from_service.async_disconnect_from_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.disconnect_from_service_request.DisconnectFromServiceRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def finalize_cutover(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Finalizes the cutover immediately for specific Source Servers. All AWS resources created by Application Migration Service for enabling the replication of these source servers will be terminated / deleted within 90 minutes. Launched Test or Cutover instances will NOT be terminated. The AWS Replication Agent will receive a command to uninstall itself (within 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be changed to DISCONNECTED; The SourceServer.lifeCycle.state will be changed to CUTOVER; The totalStorageBytes property fo each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>Request to finalize Cutover by Source Server ID.</p>
            account_id: <p>Request to finalize Cutover by Source Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.finalize_cutover_request.FinalizeCutoverRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.finalize_cutover

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.finalize_cutover.async_finalize_cutover(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.finalize_cutover_request.FinalizeCutoverRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_launch_configuration(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.launch_configuration.LaunchConfiguration":
        """<p>Lists all LaunchConfigurations available, filtered by Source Server IDs.</p>

        Args:
            source_server_id: <p>Request to get Launch Configuration information by Source Server ID.</p>
            account_id: <p>Request to get Launch Configuration information by Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.get_launch_configuration_request.GetLaunchConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.launch_configuration.LaunchConfiguration"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.get_launch_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.get_launch_configuration.async_get_launch_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.get_launch_configuration_request.GetLaunchConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_replication_configuration(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.replication_configuration.ReplicationConfiguration":
        """<p>Lists all ReplicationConfigurations, filtered by Source Server ID.</p>

        Args:
            source_server_id: <p>Request to get Replication Configuration by Source Server ID.</p>
            account_id: <p>Request to get Replication Configuration by Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.get_replication_configuration_request.GetReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.replication_configuration.ReplicationConfiguration"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.get_replication_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.get_replication_configuration.async_get_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.get_replication_configuration_request.GetReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_source_server_actions(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "aws_sdk_mgn.types.source_server_actions_request_filters.SourceServerActionsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.list_source_server_actions_response.ListSourceServerActionsResponse":
        """<p>List source server post migration custom actions.</p>

        Args:
            source_server_id: <p>Source server ID.</p>
            filters: <p>Filters to apply when listing source server post migration custom actions.</p>
            max_results: <p>Maximum amount of items to return when listing source server post migration custom actions.</p>
            next_token: <p>Next token to use when listing source server post migration custom actions.</p>
            account_id: <p>Account ID to return when listing source server post migration custom actions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.list_source_server_actions_request.ListSourceServerActionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.list_source_server_actions_response.ListSourceServerActionsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.list_source_server_actions

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.list_source_server_actions.async_list_source_server_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.list_source_server_actions_request.ListSourceServerActionsRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def mark_as_archived(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Archives specific Source Servers by setting the SourceServer.isArchived property to true for specified SourceServers by ID. This command only works for SourceServers with a lifecycle. state which equals DISCONNECTED or CUTOVER.</p>

        Args:
            source_server_id: <p>Mark as archived by Source Server ID.</p>
            account_id: <p>Mark as archived by Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.mark_as_archived_request.MarkAsArchivedRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.mark_as_archived

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.mark_as_archived.async_mark_as_archived(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.mark_as_archived_request.MarkAsArchivedRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def pause_replication(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Pause Replication.</p>

        Args:
            source_server_id: <p>Pause Replication Request source server ID.</p>
            account_id: <p>Pause Replication Request account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.pause_replication_request.PauseReplicationRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.pause_replication

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.pause_replication.async_pause_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.pause_replication_request.PauseReplicationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_source_server_action(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        action_name: "aws_sdk_mgn.types.action_name.ActionName",
        document_identifier: "aws_sdk_mgn.types.bounded_string.BoundedString",
        order: "aws_sdk_mgn.types.order_type.OrderType",
        action_id: "aws_sdk_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        document_version: Optional[
            "aws_sdk_mgn.types.document_version.DocumentVersion"
        ] = None,
        active: Optional[bool] = None,
        timeout_seconds: Optional[
            "aws_sdk_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        must_succeed_for_cutover: Optional[bool] = None,
        parameters: Optional[
            "aws_sdk_mgn.types.ssm_document_parameters.SsmDocumentParameters"
        ] = None,
        external_parameters: Optional[
            "aws_sdk_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
        ] = None,
        description: Optional[
            "aws_sdk_mgn.types.action_description.ActionDescription"
        ] = None,
        category: Optional["aws_sdk_mgn.types.action_category.ActionCategory"] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server_action_document.SourceServerActionDocument":
        """<p>Put source server post migration custom action.</p>

        Args:
            source_server_id: <p>Source server ID.</p>
            action_name: <p>Source server post migration custom action name.</p>
            document_identifier: <p>Source server post migration custom action document identifier.</p>
            order: <p>Source server post migration custom action order.</p>
            action_id: <p>Source server post migration custom action ID.</p>
            document_version: <p>Source server post migration custom action document version.</p>
            active: <p>Source server post migration custom action active status.</p>
            timeout_seconds: <p>Source server post migration custom action timeout in seconds.</p>
            must_succeed_for_cutover: <p>Source server post migration custom action must succeed for cutover.</p>
            parameters: <p>Source server post migration custom action parameters.</p>
            external_parameters: <p>Source server post migration custom action external parameters.</p>
            description: <p>Source server post migration custom action description.</p>
            category: <p>Source server post migration custom action category.</p>
            account_id: <p>Source server post migration custom account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.put_source_server_action_request.PutSourceServerActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.source_server_action_document.SourceServerActionDocument"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.put_source_server_action

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.put_source_server_action.async_put_source_server_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.put_source_server_action_request.PutSourceServerActionRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        input["action_name"] = action_name
        input["document_identifier"] = document_identifier
        input["order"] = order
        input["action_id"] = action_id
        if document_version is not None:
            input["document_version"] = document_version
        if active is not None:
            input["active"] = active
        if timeout_seconds is not None:
            input["timeout_seconds"] = timeout_seconds
        if must_succeed_for_cutover is not None:
            input["must_succeed_for_cutover"] = must_succeed_for_cutover
        if parameters is not None:
            input["parameters"] = parameters
        if external_parameters is not None:
            input["external_parameters"] = external_parameters
        if description is not None:
            input["description"] = description
        if category is not None:
            input["category"] = category
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_source_server_action(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        action_id: "aws_sdk_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.remove_source_server_action_response.RemoveSourceServerActionResponse":
        """<p>Remove source server post migration custom action.</p>

        Args:
            source_server_id: <p>Source server ID of the post migration custom action to remove.</p>
            action_id: <p>Source server post migration custom action ID to remove.</p>
            account_id: <p>Source server post migration account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.remove_source_server_action_request.RemoveSourceServerActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.remove_source_server_action_response.RemoveSourceServerActionResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.remove_source_server_action

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.remove_source_server_action.async_remove_source_server_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.remove_source_server_action_request.RemoveSourceServerActionRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        input["action_id"] = action_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def resume_replication(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Resume Replication.</p>

        Args:
            source_server_id: <p>Resume Replication Request source server ID.</p>
            account_id: <p>Resume Replication Request account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.resume_replication_request.ResumeReplicationRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.resume_replication

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.resume_replication.async_resume_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.resume_replication_request.ResumeReplicationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def retry_data_replication(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Causes the data replication initiation sequence to begin immediately upon next Handshake for specified SourceServer IDs, regardless of when the previous initiation started. This command will not work if the SourceServer is not stalled or is in a DISCONNECTED or STOPPED state.</p>

        Args:
            source_server_id: <p>Retry data replication for Source Server ID.</p>
            account_id: <p>Retry data replication for Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.retry_data_replication_request.RetryDataReplicationRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.retry_data_replication

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.retry_data_replication.async_retry_data_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.retry_data_replication_request.RetryDataReplicationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_replication(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Start replication for source server irrespective of its replication type.</p>

        Args:
            source_server_id: <p>ID of source server on which to start replication.</p>
            account_id: <p>Account ID on which to start replication.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.start_replication_request.StartReplicationRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.start_replication

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.start_replication.async_start_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.start_replication_request.StartReplicationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_replication(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Stop Replication.</p>

        Args:
            source_server_id: <p>Stop Replication Request source server ID.</p>
            account_id: <p>Stop Replication Request account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.stop_replication_request.StopReplicationRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.stop_replication

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.stop_replication.async_stop_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.stop_replication_request.StopReplicationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_launch_configuration(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        name: Optional[
            "aws_sdk_mgn.types.small_bounded_string.SmallBoundedString"
        ] = None,
        launch_disposition: Optional[
            "aws_sdk_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "aws_sdk_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["aws_sdk_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["aws_sdk_mgn.types.boot_mode.BootMode"] = None,
        post_launch_actions: Optional[
            "aws_sdk_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional[
            "aws_sdk_mgn.types.tag_value.TagValue"
        ] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.launch_configuration.LaunchConfiguration":
        """<p>Updates multiple LaunchConfigurations by Source Server ID.</p> <note> <p>bootMode valid values are <code>LEGACY_BIOS | UEFI</code> </p> </note>

        Args:
            source_server_id: <p>Update Launch configuration by Source Server ID request.</p>
            name: <p>Update Launch configuration name request.</p>
            launch_disposition: <p>Update Launch configuration launch disposition request.</p>
            target_instance_type_right_sizing_method: <p>Update Launch configuration Target instance right sizing request.</p>
            copy_private_ip: <p>Update Launch configuration copy Private IP request.</p>
            copy_tags: <p>Update Launch configuration copy Tags request.</p>
            licensing: <p>Update Launch configuration licensing request.</p>
            boot_mode: <p>Update Launch configuration boot mode request.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration map auto tagging MPE ID.</p>
            account_id: <p>Update Launch configuration Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.launch_configuration.LaunchConfiguration"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.update_launch_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.update_launch_configuration.async_update_launch_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if name is not None:
            input["name"] = name
        if launch_disposition is not None:
            input["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input["copy_tags"] = copy_tags
        if licensing is not None:
            input["licensing"] = licensing
        if boot_mode is not None:
            input["boot_mode"] = boot_mode
        if post_launch_actions is not None:
            input["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_replication_configuration(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        name: Optional[
            "aws_sdk_mgn.types.small_bounded_string.SmallBoundedString"
        ] = None,
        staging_area_subnet_id: Optional["aws_sdk_mgn.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "aws_sdk_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "aws_sdk_mgn.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "aws_sdk_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        replicated_disks: Optional[
            "aws_sdk_mgn.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
        ] = None,
        ebs_encryption: Optional[
            "aws_sdk_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["aws_sdk_mgn.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "aws_sdk_mgn.types.bandwidth_throttling.BandwidthThrottling"
        ] = None,
        data_plane_routing: Optional[
            "aws_sdk_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        use_fips_endpoint: Optional[bool] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
        internet_protocol: Optional[
            "aws_sdk_mgn.types.internet_protocol.InternetProtocol"
        ] = None,
        store_snapshot_on_local_zone: Optional[bool] = None,
    ) -> "aws_sdk_mgn.types.replication_configuration.ReplicationConfiguration":
        """<p>Allows you to update multiple ReplicationConfigurations by Source Server ID.</p>

        Args:
            source_server_id: <p>Update replication configuration Source Server ID request.</p>
            name: <p>Update replication configuration name request.</p>
            staging_area_subnet_id: <p>Update replication configuration Staging Area subnet request.</p>
            associate_default_security_group: <p>Update replication configuration associate default Application Migration Service Security group request.</p>
            replication_servers_security_groups_i_ds: <p>Update replication configuration Replication Server Security Groups IDs request.</p>
            replication_server_instance_type: <p>Update replication configuration Replication Server instance type request.</p>
            use_dedicated_replication_server: <p>Update replication configuration use dedicated Replication Server request.</p>
            default_large_staging_disk_type: <p>Update replication configuration use default large Staging Disk type request.</p>
            replicated_disks: <p>Update replication configuration replicated disks request.</p>
            ebs_encryption: <p>Update replication configuration EBS encryption request.</p>
            ebs_encryption_key_arn: <p>Update replication configuration EBS encryption key ARN request.</p>
            bandwidth_throttling: <p>Update replication configuration bandwidth throttling request.</p>
            data_plane_routing: <p>Update replication configuration data plane routing request.</p>
            create_public_ip: <p>Update replication configuration create Public IP request.</p>
            staging_area_tags: <p>Update replication configuration Staging Area Tags request.</p>
            use_fips_endpoint: <p>Update replication configuration use Fips Endpoint.</p>
            account_id: <p>Update replication configuration Account ID request.</p>
            internet_protocol: <p>Update replication configuration internet protocol.</p>
            store_snapshot_on_local_zone: <p>Update replication configuration store snapshot on local zone.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.replication_configuration.ReplicationConfiguration"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.update_replication_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.update_replication_configuration.async_update_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        if name is not None:
            input["name"] = name
        if staging_area_subnet_id is not None:
            input["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input["associate_default_security_group"] = associate_default_security_group
        if replication_servers_security_groups_i_ds is not None:
            input["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input["replication_server_instance_type"] = replication_server_instance_type
        if use_dedicated_replication_server is not None:
            input["use_dedicated_replication_server"] = use_dedicated_replication_server
        if default_large_staging_disk_type is not None:
            input["default_large_staging_disk_type"] = default_large_staging_disk_type
        if replicated_disks is not None:
            input["replicated_disks"] = replicated_disks
        if ebs_encryption is not None:
            input["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input["staging_area_tags"] = staging_area_tags
        if use_fips_endpoint is not None:
            input["use_fips_endpoint"] = use_fips_endpoint
        if account_id is not None:
            input["account_id"] = account_id
        if internet_protocol is not None:
            input["internet_protocol"] = internet_protocol
        if store_snapshot_on_local_zone is not None:
            input["store_snapshot_on_local_zone"] = store_snapshot_on_local_zone

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_source_server_replication_type(
        self,
        source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID",
        replication_type: "aws_sdk_mgn.types.replication_type.ReplicationType",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.source_server.SourceServer":
        """<p>Allows you to change between the AGENT_BASED replication type and the SNAPSHOT_SHIPPING replication type. </p> <p>SNAPSHOT_SHIPPING should be used for agentless replication.</p>

        Args:
            source_server_id: <p>ID of source server on which to update replication type.</p>
            replication_type: <p>Replication type to which to update source server.</p>
            account_id: <p>Account ID on which to update replication type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.update_source_server_replication_type_request.UpdateSourceServerReplicationTypeRequest]",
        ) -> AsyncOperationResponse["aws_sdk_mgn.types.source_server.SourceServer"]:
            import aws_sdk_mgn._operations.application_migration_service.update_source_server_replication_type

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.update_source_server_replication_type.async_update_source_server_replication_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.update_source_server_replication_type_request.UpdateSourceServerReplicationTypeRequest = {}  # type: ignore[typeddict-item]
        input["source_server_id"] = source_server_id
        input["replication_type"] = replication_type
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_cutover(
        self,
        source_server_i_ds: "aws_sdk_mgn.types.start_cutover_request_source_server_i_ds.StartCutoverRequestSourceServerIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.start_cutover_response.StartCutoverResponse":
        """<p>Launches a Cutover Instance for specific Source Servers. This command starts a LAUNCH job whose initiatedBy property is StartCutover and changes the SourceServer.lifeCycle.state property to CUTTING_OVER.</p>

        Args:
            source_server_i_ds: <p>Start Cutover by Source Server IDs.</p>
            tags: <p>Start Cutover by Tags.</p>
            account_id: <p>Start Cutover by Account IDs</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.start_cutover_request.StartCutoverRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.start_cutover_response.StartCutoverResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_cutover

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.start_cutover.async_start_cutover(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.start_cutover_request.StartCutoverRequest = {}  # type: ignore[typeddict-item]
        input["source_server_i_ds"] = source_server_i_ds
        if tags is not None:
            input["tags"] = tags
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_test(
        self,
        source_server_i_ds: "aws_sdk_mgn.types.start_test_request_source_server_i_ds.StartTestRequestSourceServerIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.start_test_response.StartTestResponse":
        """<p>Launches a Test Instance for specific Source Servers. This command starts a LAUNCH job whose initiatedBy property is StartTest and changes the SourceServer.lifeCycle.state property to TESTING.</p>

        Args:
            source_server_i_ds: <p>Start Test for Source Server IDs.</p>
            tags: <p>Start Test by Tags.</p>
            account_id: <p>Start Test for Account ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.start_test_request.StartTestRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.start_test_response.StartTestResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.start_test

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.start_test.async_start_test(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.start_test_request.StartTestRequest = {}  # type: ignore[typeddict-item]
        input["source_server_i_ds"] = source_server_i_ds
        if tags is not None:
            input["tags"] = tags
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def terminate_target_instances(
        self,
        source_server_i_ds: "aws_sdk_mgn.types.terminate_target_instances_request_source_server_i_ds.TerminateTargetInstancesRequestSourceServerIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        tags: Optional["aws_sdk_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["aws_sdk_mgn.types.account_id.AccountID"] = None,
    ) -> "aws_sdk_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse":
        """<p>Starts a job that terminates specific launched EC2 Test and Cutover instances. This command will not work for any Source Server with a lifecycle.state of TESTING, CUTTING_OVER, or CUTOVER.</p>

        Args:
            source_server_i_ds: <p>Terminate Target instance by Source Server IDs.</p>
            tags: <p>Terminate Target instance by Tags.</p>
            account_id: <p>Terminate Target instance by Account ID</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.terminate_target_instances

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.terminate_target_instances.async_terminate_target_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest = {}  # type: ignore[typeddict-item]
        input["source_server_i_ds"] = source_server_i_ds
        if tags is not None:
            input["tags"] = tags
        if account_id is not None:
            input["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
