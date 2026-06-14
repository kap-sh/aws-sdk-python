from typing import TYPE_CHECKING, Optional

import aws_sdk_drs._auth._signers
import aws_sdk_drs._auth._sigv4
from aws_sdk_drs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_drs.types.arn
    import aws_sdk_drs.types.delete_source_server_request
    import aws_sdk_drs.types.delete_source_server_response
    import aws_sdk_drs.types.describe_recovery_snapshots_request
    import aws_sdk_drs.types.describe_recovery_snapshots_request_filters
    import aws_sdk_drs.types.describe_recovery_snapshots_response
    import aws_sdk_drs.types.describe_source_servers_request
    import aws_sdk_drs.types.describe_source_servers_request_filters
    import aws_sdk_drs.types.describe_source_servers_response
    import aws_sdk_drs.types.disconnect_source_server_request
    import aws_sdk_drs.types.ec2_instance_type
    import aws_sdk_drs.types.get_launch_configuration_request
    import aws_sdk_drs.types.get_replication_configuration_request
    import aws_sdk_drs.types.internet_protocol
    import aws_sdk_drs.types.launch_configuration
    import aws_sdk_drs.types.launch_disposition
    import aws_sdk_drs.types.launch_into_instance_properties
    import aws_sdk_drs.types.licensing
    import aws_sdk_drs.types.pagination_token
    import aws_sdk_drs.types.pit_policy
    import aws_sdk_drs.types.positive_integer
    import aws_sdk_drs.types.recovery_snapshot
    import aws_sdk_drs.types.recovery_snapshots_order
    import aws_sdk_drs.types.replication_configuration
    import aws_sdk_drs.types.replication_configuration_data_plane_routing
    import aws_sdk_drs.types.replication_configuration_default_large_staging_disk_type
    import aws_sdk_drs.types.replication_configuration_ebs_encryption
    import aws_sdk_drs.types.replication_configuration_replicated_disks
    import aws_sdk_drs.types.replication_servers_security_groups_i_ds
    import aws_sdk_drs.types.retry_data_replication_request
    import aws_sdk_drs.types.small_bounded_string
    import aws_sdk_drs.types.source_server
    import aws_sdk_drs.types.source_server_id
    import aws_sdk_drs.types.start_recovery_request
    import aws_sdk_drs.types.start_recovery_request_source_servers
    import aws_sdk_drs.types.start_recovery_response
    import aws_sdk_drs.types.start_replication_request
    import aws_sdk_drs.types.start_replication_response
    import aws_sdk_drs.types.stop_replication_request
    import aws_sdk_drs.types.stop_replication_response
    import aws_sdk_drs.types.strictly_positive_integer
    import aws_sdk_drs.types.subnet_id
    import aws_sdk_drs.types.tags_map
    import aws_sdk_drs.types.target_instance_type_right_sizing_method
    import aws_sdk_drs.types.update_launch_configuration_request
    import aws_sdk_drs.types.update_replication_configuration_request
    from aws_sdk_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    from aws_sdk_drs._services.drs import drsClient, drsClientConfig


class SourceServerResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

    def delete(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.delete_source_server_response.DeleteSourceServerResponse":
        """<p>Deletes a single Source Server by ID. The Source Server must be disconnected first.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.delete_source_server_request.DeleteSourceServerRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.delete_source_server_response.DeleteSourceServerResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_source_server

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_source_server.delete_source_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.delete_source_server_request.DeleteSourceServerRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[drsClientConfig] = None,
        filters: Optional[
            "aws_sdk_drs.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.describe_source_servers_response.DescribeSourceServersResponse":
        """<p>Lists all Source Servers or multiple Source Servers filtered by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Source Servers.</p>
            max_results: <p>Maximum number of Source Servers to retrieve.</p>
            next_token: <p>The token of the next Source Server to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.describe_source_servers_request.DescribeSourceServersRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.describe_source_servers_response.DescribeSourceServersResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_source_servers

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_source_servers.describe_source_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_source_servers_request.DescribeSourceServersRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    def describe_recovery_snapshots(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        filters: Optional[
            "aws_sdk_drs.types.describe_recovery_snapshots_request_filters.DescribeRecoverySnapshotsRequestFilters"
        ] = None,
        order: Optional[
            "aws_sdk_drs.types.recovery_snapshots_order.RecoverySnapshotsOrder"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.describe_recovery_snapshots_response.DescribeRecoverySnapshotsResponse":
        """<p>Lists all Recovery Snapshots for a single Source Server.</p>

        Args:
            source_server_id: <p>Filter Recovery Snapshots by Source Server ID.</p>
            filters: <p>A set of filters by which to return Recovery Snapshots.</p>
            order: <p>The sorted ordering by which to return Recovery Snapshots.</p>
            max_results: <p>Maximum number of Recovery Snapshots to retrieve.</p>
            next_token: <p>The token of the next Recovery Snapshot to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.describe_recovery_snapshots_request.DescribeRecoverySnapshotsRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.describe_recovery_snapshots_response.DescribeRecoverySnapshotsResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_recovery_snapshots

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_recovery_snapshots.describe_recovery_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_recovery_snapshots_request.DescribeRecoverySnapshotsRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id
        if filters is not None:
            input_["filters"] = filters
        if order is not None:
            input_["order"] = order
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

    def disconnect_source_server(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.source_server.SourceServer":
        """<p>Disconnects a specific Source Server from Elastic Disaster Recovery. Data replication is stopped immediately. All AWS resources created by Elastic Disaster Recovery for enabling the replication of the Source Server will be terminated / deleted within 90 minutes. You cannot disconnect a Source Server if it has a Recovery Instance. If the agent on the Source Server has not been prevented from communicating with the Elastic Disaster Recovery service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to disconnect.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.disconnect_source_server_request.DisconnectSourceServerRequest]",
        ) -> OperationResponse["aws_sdk_drs.types.source_server.SourceServer"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.disconnect_source_server

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.disconnect_source_server.disconnect_source_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.disconnect_source_server_request.DisconnectSourceServerRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_launch_configuration(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.launch_configuration.LaunchConfiguration":
        """<p>Gets a LaunchConfiguration, filtered by Source Server IDs.</p>

        Args:
            source_server_id: <p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.get_launch_configuration_request.GetLaunchConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.launch_configuration.LaunchConfiguration"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.get_launch_configuration

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.get_launch_configuration.get_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.get_launch_configuration_request.GetLaunchConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_replication_configuration(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.replication_configuration.ReplicationConfiguration":
        """<p>Gets a ReplicationConfiguration, filtered by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Serve for this Replication Configuration.r</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.get_replication_configuration_request.GetReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.replication_configuration.ReplicationConfiguration"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.get_replication_configuration

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.get_replication_configuration.get_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.get_replication_configuration_request.GetReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def retry_data_replication(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.source_server.SourceServer":
        """<p>WARNING: RetryDataReplication is deprecated. Causes the data replication initiation sequence to begin immediately upon next Handshake for the specified Source Server ID, regardless of when the previous initiation started. This command will work only if the Source Server is stalled or is in a DISCONNECTED or STOPPED state. </p>

        Args:
            source_server_id: <p>The ID of the Source Server whose data replication should be retried.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.retry_data_replication_request.RetryDataReplicationRequest]",
        ) -> OperationResponse["aws_sdk_drs.types.source_server.SourceServer"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.retry_data_replication

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.retry_data_replication.retry_data_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.retry_data_replication_request.RetryDataReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_replication(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.start_replication_response.StartReplicationResponse":
        """<p>Starts replication for a stopped Source Server. This action would make the Source Server protected again and restart billing for it.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to start replication for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.start_replication_request.StartReplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.start_replication_response.StartReplicationResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.start_replication

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.start_replication.start_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.start_replication_request.StartReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_replication(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.stop_replication_response.StopReplicationResponse":
        """<p>Stops replication for a Source Server. This action would make the Source Server unprotected, delete its existing snapshots and stop billing for it.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to stop replication for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.stop_replication_request.StopReplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.stop_replication_response.StopReplicationResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.stop_replication

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.stop_replication.stop_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.stop_replication_request.StopReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_launch_configuration(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        name: Optional[
            "aws_sdk_drs.types.small_bounded_string.SmallBoundedString"
        ] = None,
        launch_disposition: Optional[
            "aws_sdk_drs.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "aws_sdk_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["aws_sdk_drs.types.licensing.Licensing"] = None,
        post_launch_enabled: Optional[bool] = None,
        launch_into_instance_properties: Optional[
            "aws_sdk_drs.types.launch_into_instance_properties.LaunchIntoInstanceProperties"
        ] = None,
    ) -> "aws_sdk_drs.types.launch_configuration.LaunchConfiguration":
        """<p>Updates a LaunchConfiguration by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>
            name: <p>The name of the launch configuration.</p>
            launch_disposition: <p>The state of the Recovery Instance in EC2 after the recovery operation.</p>
            target_instance_type_right_sizing_method: <p>Whether Elastic Disaster Recovery should try to automatically choose the instance type that best matches the OS, CPU, and RAM of your Source Server.</p>
            copy_private_ip: <p>Whether we should copy the Private IP of the Source Server to the Recovery Instance.</p>
            copy_tags: <p>Whether we want to copy the tags of the Source Server to the EC2 machine of the Recovery Instance.</p>
            licensing: <p>The licensing configuration to be used for this launch configuration.</p>
            post_launch_enabled: <p>Whether we want to enable post-launch actions for the Source Server.</p>
            launch_into_instance_properties: <p>Launch into existing instance properties.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.launch_configuration.LaunchConfiguration"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.update_launch_configuration

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.update_launch_configuration.update_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id
        if name is not None:
            input_["name"] = name
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if post_launch_enabled is not None:
            input_["post_launch_enabled"] = post_launch_enabled
        if launch_into_instance_properties is not None:
            input_["launch_into_instance_properties"] = launch_into_instance_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_replication_configuration(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        name: Optional[
            "aws_sdk_drs.types.small_bounded_string.SmallBoundedString"
        ] = None,
        staging_area_subnet_id: Optional["aws_sdk_drs.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "aws_sdk_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "aws_sdk_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "aws_sdk_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        replicated_disks: Optional[
            "aws_sdk_drs.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
        ] = None,
        ebs_encryption: Optional[
            "aws_sdk_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["aws_sdk_drs.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "aws_sdk_drs.types.positive_integer.PositiveInteger"
        ] = None,
        data_plane_routing: Optional[
            "aws_sdk_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None,
        pit_policy: Optional["aws_sdk_drs.types.pit_policy.PITPolicy"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "aws_sdk_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "aws_sdk_drs.types.replication_configuration.ReplicationConfiguration":
        """<p>Allows you to update a ReplicationConfiguration by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Server for this Replication Configuration.</p>
            name: <p>The name of the Replication Configuration.</p>
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            replicated_disks: <p>The configuration of the disks of the Source Server to be replicated.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.replication_configuration.ReplicationConfiguration"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.update_replication_configuration

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.update_replication_configuration.update_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id
        if name is not None:
            input_["name"] = name
        if staging_area_subnet_id is not None:
            input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
        if replication_servers_security_groups_i_ds is not None:
            input_["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input_["replication_server_instance_type"] = (
                replication_server_instance_type
            )
        if use_dedicated_replication_server is not None:
            input_["use_dedicated_replication_server"] = (
                use_dedicated_replication_server
            )
        if default_large_staging_disk_type is not None:
            input_["default_large_staging_disk_type"] = default_large_staging_disk_type
        if replicated_disks is not None:
            input_["replicated_disks"] = replicated_disks
        if ebs_encryption is not None:
            input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input_["staging_area_tags"] = staging_area_tags
        if pit_policy is not None:
            input_["pit_policy"] = pit_policy
        if auto_replicate_new_disks is not None:
            input_["auto_replicate_new_disks"] = auto_replicate_new_disks
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_recovery(
        self,
        source_servers: "aws_sdk_drs.types.start_recovery_request_source_servers.StartRecoveryRequestSourceServers",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        is_drill: Optional[bool] = None,
        tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_drs.types.start_recovery_response.StartRecoveryResponse":
        """<p>Launches Recovery Instances for the specified Source Servers. For each Source Server you may choose a point in time snapshot to launch from, or use an on demand snapshot.</p>

        Args:
            source_servers: <p>The Source Servers that we want to start a Recovery Job for.</p>
            is_drill: <p>Whether this Source Server Recovery operation is a drill or not.</p>
            tags: <p>The tags to be associated with the Recovery Job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.start_recovery_request.StartRecoveryRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.start_recovery_response.StartRecoveryResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.start_recovery

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.start_recovery.start_recovery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.start_recovery_request.StartRecoveryRequest = {}  # type: ignore[typeddict-item]
        input_["source_servers"] = source_servers
        if is_drill is not None:
            input_["is_drill"] = is_drill
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncSourceServerResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service

    async def delete(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.delete_source_server_response.DeleteSourceServerResponse":
        """<p>Deletes a single Source Server by ID. The Source Server must be disconnected first.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.delete_source_server_request.DeleteSourceServerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.delete_source_server_response.DeleteSourceServerResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_source_server

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_source_server.async_delete_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.delete_source_server_request.DeleteSourceServerRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "aws_sdk_drs.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.describe_source_servers_response.DescribeSourceServersResponse":
        """<p>Lists all Source Servers or multiple Source Servers filtered by ID.</p>

        Args:
            filters: <p>A set of filters by which to return Source Servers.</p>
            max_results: <p>Maximum number of Source Servers to retrieve.</p>
            next_token: <p>The token of the next Source Server to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.describe_source_servers_request.DescribeSourceServersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.describe_source_servers_response.DescribeSourceServersResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_source_servers

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_source_servers.async_describe_source_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_source_servers_request.DescribeSourceServersRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_recovery_snapshots(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "aws_sdk_drs.types.describe_recovery_snapshots_request_filters.DescribeRecoverySnapshotsRequestFilters"
        ] = None,
        order: Optional[
            "aws_sdk_drs.types.recovery_snapshots_order.RecoverySnapshotsOrder"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.describe_recovery_snapshots_response.DescribeRecoverySnapshotsResponse":
        """<p>Lists all Recovery Snapshots for a single Source Server.</p>

        Args:
            source_server_id: <p>Filter Recovery Snapshots by Source Server ID.</p>
            filters: <p>A set of filters by which to return Recovery Snapshots.</p>
            order: <p>The sorted ordering by which to return Recovery Snapshots.</p>
            max_results: <p>Maximum number of Recovery Snapshots to retrieve.</p>
            next_token: <p>The token of the next Recovery Snapshot to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.describe_recovery_snapshots_request.DescribeRecoverySnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.describe_recovery_snapshots_response.DescribeRecoverySnapshotsResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_recovery_snapshots

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_recovery_snapshots.async_describe_recovery_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_recovery_snapshots_request.DescribeRecoverySnapshotsRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id
        if filters is not None:
            input_["filters"] = filters
        if order is not None:
            input_["order"] = order
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

    async def disconnect_source_server(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.source_server.SourceServer":
        """<p>Disconnects a specific Source Server from Elastic Disaster Recovery. Data replication is stopped immediately. All AWS resources created by Elastic Disaster Recovery for enabling the replication of the Source Server will be terminated / deleted within 90 minutes. You cannot disconnect a Source Server if it has a Recovery Instance. If the agent on the Source Server has not been prevented from communicating with the Elastic Disaster Recovery service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to disconnect.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.disconnect_source_server_request.DisconnectSourceServerRequest]",
        ) -> AsyncOperationResponse["aws_sdk_drs.types.source_server.SourceServer"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.disconnect_source_server

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.disconnect_source_server.async_disconnect_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.disconnect_source_server_request.DisconnectSourceServerRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_launch_configuration(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.launch_configuration.LaunchConfiguration":
        """<p>Gets a LaunchConfiguration, filtered by Source Server IDs.</p>

        Args:
            source_server_id: <p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.get_launch_configuration_request.GetLaunchConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.launch_configuration.LaunchConfiguration"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.get_launch_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.get_launch_configuration.async_get_launch_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.get_launch_configuration_request.GetLaunchConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_replication_configuration(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.replication_configuration.ReplicationConfiguration":
        """<p>Gets a ReplicationConfiguration, filtered by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Serve for this Replication Configuration.r</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.get_replication_configuration_request.GetReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.replication_configuration.ReplicationConfiguration"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.get_replication_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.get_replication_configuration.async_get_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.get_replication_configuration_request.GetReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def retry_data_replication(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.source_server.SourceServer":
        """<p>WARNING: RetryDataReplication is deprecated. Causes the data replication initiation sequence to begin immediately upon next Handshake for the specified Source Server ID, regardless of when the previous initiation started. This command will work only if the Source Server is stalled or is in a DISCONNECTED or STOPPED state. </p>

        Args:
            source_server_id: <p>The ID of the Source Server whose data replication should be retried.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.retry_data_replication_request.RetryDataReplicationRequest]",
        ) -> AsyncOperationResponse["aws_sdk_drs.types.source_server.SourceServer"]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.retry_data_replication

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.retry_data_replication.async_retry_data_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.retry_data_replication_request.RetryDataReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_replication(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.start_replication_response.StartReplicationResponse":
        """<p>Starts replication for a stopped Source Server. This action would make the Source Server protected again and restart billing for it.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to start replication for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.start_replication_request.StartReplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.start_replication_response.StartReplicationResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.start_replication

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.start_replication.async_start_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.start_replication_request.StartReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_replication(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.stop_replication_response.StopReplicationResponse":
        """<p>Stops replication for a Source Server. This action would make the Source Server unprotected, delete its existing snapshots and stop billing for it.</p>

        Args:
            source_server_id: <p>The ID of the Source Server to stop replication for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.stop_replication_request.StopReplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.stop_replication_response.StopReplicationResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.stop_replication

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.stop_replication.async_stop_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.stop_replication_request.StopReplicationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_launch_configuration(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        name: Optional[
            "aws_sdk_drs.types.small_bounded_string.SmallBoundedString"
        ] = None,
        launch_disposition: Optional[
            "aws_sdk_drs.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "aws_sdk_drs.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["aws_sdk_drs.types.licensing.Licensing"] = None,
        post_launch_enabled: Optional[bool] = None,
        launch_into_instance_properties: Optional[
            "aws_sdk_drs.types.launch_into_instance_properties.LaunchIntoInstanceProperties"
        ] = None,
    ) -> "aws_sdk_drs.types.launch_configuration.LaunchConfiguration":
        """<p>Updates a LaunchConfiguration by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Server that we want to retrieve a Launch Configuration for.</p>
            name: <p>The name of the launch configuration.</p>
            launch_disposition: <p>The state of the Recovery Instance in EC2 after the recovery operation.</p>
            target_instance_type_right_sizing_method: <p>Whether Elastic Disaster Recovery should try to automatically choose the instance type that best matches the OS, CPU, and RAM of your Source Server.</p>
            copy_private_ip: <p>Whether we should copy the Private IP of the Source Server to the Recovery Instance.</p>
            copy_tags: <p>Whether we want to copy the tags of the Source Server to the EC2 machine of the Recovery Instance.</p>
            licensing: <p>The licensing configuration to be used for this launch configuration.</p>
            post_launch_enabled: <p>Whether we want to enable post-launch actions for the Source Server.</p>
            launch_into_instance_properties: <p>Launch into existing instance properties.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.launch_configuration.LaunchConfiguration"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.update_launch_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.update_launch_configuration.async_update_launch_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id
        if name is not None:
            input_["name"] = name
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if post_launch_enabled is not None:
            input_["post_launch_enabled"] = post_launch_enabled
        if launch_into_instance_properties is not None:
            input_["launch_into_instance_properties"] = launch_into_instance_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_replication_configuration(
        self,
        source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        name: Optional[
            "aws_sdk_drs.types.small_bounded_string.SmallBoundedString"
        ] = None,
        staging_area_subnet_id: Optional["aws_sdk_drs.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "aws_sdk_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "aws_sdk_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "aws_sdk_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        replicated_disks: Optional[
            "aws_sdk_drs.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
        ] = None,
        ebs_encryption: Optional[
            "aws_sdk_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["aws_sdk_drs.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "aws_sdk_drs.types.positive_integer.PositiveInteger"
        ] = None,
        data_plane_routing: Optional[
            "aws_sdk_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None,
        pit_policy: Optional["aws_sdk_drs.types.pit_policy.PITPolicy"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "aws_sdk_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "aws_sdk_drs.types.replication_configuration.ReplicationConfiguration":
        """<p>Allows you to update a ReplicationConfiguration by Source Server ID.</p>

        Args:
            source_server_id: <p>The ID of the Source Server for this Replication Configuration.</p>
            name: <p>The name of the Replication Configuration.</p>
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            replicated_disks: <p>The configuration of the disks of the Source Server to be replicated.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.replication_configuration.ReplicationConfiguration"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.update_replication_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.update_replication_configuration.async_update_replication_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_id"] = source_server_id
        if name is not None:
            input_["name"] = name
        if staging_area_subnet_id is not None:
            input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
        if replication_servers_security_groups_i_ds is not None:
            input_["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input_["replication_server_instance_type"] = (
                replication_server_instance_type
            )
        if use_dedicated_replication_server is not None:
            input_["use_dedicated_replication_server"] = (
                use_dedicated_replication_server
            )
        if default_large_staging_disk_type is not None:
            input_["default_large_staging_disk_type"] = default_large_staging_disk_type
        if replicated_disks is not None:
            input_["replicated_disks"] = replicated_disks
        if ebs_encryption is not None:
            input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input_["staging_area_tags"] = staging_area_tags
        if pit_policy is not None:
            input_["pit_policy"] = pit_policy
        if auto_replicate_new_disks is not None:
            input_["auto_replicate_new_disks"] = auto_replicate_new_disks
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_recovery(
        self,
        source_servers: "aws_sdk_drs.types.start_recovery_request_source_servers.StartRecoveryRequestSourceServers",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        is_drill: Optional[bool] = None,
        tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_drs.types.start_recovery_response.StartRecoveryResponse":
        """<p>Launches Recovery Instances for the specified Source Servers. For each Source Server you may choose a point in time snapshot to launch from, or use an on demand snapshot.</p>

        Args:
            source_servers: <p>The Source Servers that we want to start a Recovery Job for.</p>
            is_drill: <p>Whether this Source Server Recovery operation is a drill or not.</p>
            tags: <p>The tags to be associated with the Recovery Job.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.start_recovery_request.StartRecoveryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.start_recovery_response.StartRecoveryResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.start_recovery

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.start_recovery.async_start_recovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.start_recovery_request.StartRecoveryRequest = {}  # type: ignore[typeddict-item]
        input_["source_servers"] = source_servers
        if is_drill is not None:
            input_["is_drill"] = is_drill
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
