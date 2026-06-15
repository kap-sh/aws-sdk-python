from __future__ import annotations

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
    import aws_sdk_drs.types.create_replication_configuration_template_request
    import aws_sdk_drs.types.delete_replication_configuration_template_request
    import aws_sdk_drs.types.delete_replication_configuration_template_response
    import aws_sdk_drs.types.describe_replication_configuration_templates_request
    import aws_sdk_drs.types.describe_replication_configuration_templates_response
    import aws_sdk_drs.types.ec2_instance_type
    import aws_sdk_drs.types.internet_protocol
    import aws_sdk_drs.types.pagination_token
    import aws_sdk_drs.types.pit_policy
    import aws_sdk_drs.types.positive_integer
    import aws_sdk_drs.types.replication_configuration_data_plane_routing
    import aws_sdk_drs.types.replication_configuration_default_large_staging_disk_type
    import aws_sdk_drs.types.replication_configuration_ebs_encryption
    import aws_sdk_drs.types.replication_configuration_template
    import aws_sdk_drs.types.replication_configuration_template_i_ds
    import aws_sdk_drs.types.replication_configuration_template_id
    import aws_sdk_drs.types.replication_servers_security_groups_i_ds
    import aws_sdk_drs.types.strictly_positive_integer
    import aws_sdk_drs.types.subnet_id
    import aws_sdk_drs.types.tags_map
    import aws_sdk_drs.types.update_replication_configuration_template_request
    from aws_sdk_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    from aws_sdk_drs._services.drs import drsClient, drsClientConfig


class ReplicationConfigurationTemplateResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

    def create(
        self,
        staging_area_subnet_id: "aws_sdk_drs.types.subnet_id.SubnetID",
        replication_servers_security_groups_i_ds: "aws_sdk_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs",
        ebs_encryption: "aws_sdk_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption",
        bandwidth_throttling: "aws_sdk_drs.types.positive_integer.PositiveInteger",
        staging_area_tags: "aws_sdk_drs.types.tags_map.TagsMap",
        pit_policy: "aws_sdk_drs.types.pit_policy.PITPolicy",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_server_instance_type: Optional[
            "aws_sdk_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "aws_sdk_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        ebs_encryption_key_arn: Optional["aws_sdk_drs.types.arn.ARN"] = None,
        data_plane_routing: Optional[
            "aws_sdk_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "aws_sdk_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "aws_sdk_drs.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Creates a new ReplicationConfigurationTemplate.</p>

        Args:
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            tags: <p>A set of tags to be associated with the Replication Configuration Template resource.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.create_replication_configuration_template

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.create_replication_configuration_template.create_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
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
        input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        input_["staging_area_tags"] = staging_area_tags
        input_["pit_policy"] = pit_policy
        if tags is not None:
            input_["tags"] = tags
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

    def update(
        self,
        replication_configuration_template_id: "aws_sdk_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        arn: Optional["aws_sdk_drs.types.arn.ARN"] = None,
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
    ) -> "aws_sdk_drs.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Updates a ReplicationConfigurationTemplate by ID.</p>

        Args:
            replication_configuration_template_id: <p>The Replication Configuration Template ID.</p>
            arn: <p>The Replication Configuration Template ARN.</p>
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
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
            req: "OperationRequest[aws_sdk_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.update_replication_configuration_template

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.update_replication_configuration_template.update_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["replication_configuration_template_id"] = (
            replication_configuration_template_id
        )
        if arn is not None:
            input_["arn"] = arn
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

    def delete(
        self,
        replication_configuration_template_id: "aws_sdk_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "aws_sdk_drs.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse":
        """<p>Deletes a single Replication Configuration Template by ID</p>

        Args:
            replication_configuration_template_id: <p>The ID of the Replication Configuration Template to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_replication_configuration_template

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_replication_configuration_template.delete_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["replication_configuration_template_id"] = (
            replication_configuration_template_id
        )

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
        replication_configuration_template_i_ds: Optional[
            "aws_sdk_drs.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse":
        """<p>Lists all ReplicationConfigurationTemplates, filtered by Source Server IDs.</p>

        Args:
            replication_configuration_template_i_ds: <p>The IDs of the Replication Configuration Templates to retrieve. An empty list means all Replication Configuration Templates.</p>
            max_results: <p>Maximum number of Replication Configuration Templates to retrieve.</p>
            next_token: <p>The token of the next Replication Configuration Template to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_drs.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest]",
        ) -> OperationResponse[
            "aws_sdk_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_replication_configuration_templates

            output, http_response = (
                aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_replication_configuration_templates.describe_replication_configuration_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest = {}  # type: ignore[typeddict-item]
        if replication_configuration_template_i_ds is not None:
            input_["replication_configuration_template_i_ds"] = (
                replication_configuration_template_i_ds
            )
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


class AsyncReplicationConfigurationTemplateResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service

    async def create(
        self,
        staging_area_subnet_id: "aws_sdk_drs.types.subnet_id.SubnetID",
        replication_servers_security_groups_i_ds: "aws_sdk_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs",
        ebs_encryption: "aws_sdk_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption",
        bandwidth_throttling: "aws_sdk_drs.types.positive_integer.PositiveInteger",
        staging_area_tags: "aws_sdk_drs.types.tags_map.TagsMap",
        pit_policy: "aws_sdk_drs.types.pit_policy.PITPolicy",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_server_instance_type: Optional[
            "aws_sdk_drs.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "aws_sdk_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        ebs_encryption_key_arn: Optional["aws_sdk_drs.types.arn.ARN"] = None,
        data_plane_routing: Optional[
            "aws_sdk_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None,
        auto_replicate_new_disks: Optional[bool] = None,
        internet_protocol: Optional[
            "aws_sdk_drs.types.internet_protocol.InternetProtocol"
        ] = None,
    ) -> "aws_sdk_drs.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Creates a new ReplicationConfigurationTemplate.</p>

        Args:
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
            ebs_encryption: <p>The type of EBS encryption to be used during replication.</p>
            ebs_encryption_key_arn: <p>The ARN of the EBS encryption key to be used during replication.</p>
            bandwidth_throttling: <p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>
            data_plane_routing: <p>The data plane routing mechanism that will be used for replication.</p>
            create_public_ip: <p>Whether to create a Public IP for the Recovery Instance by default.</p>
            staging_area_tags: <p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>
            pit_policy: <p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>
            tags: <p>A set of tags to be associated with the Replication Configuration Template resource.</p>
            auto_replicate_new_disks: <p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>
            internet_protocol: <p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.create_replication_configuration_template

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.create_replication_configuration_template.async_create_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
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
        input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        input_["staging_area_tags"] = staging_area_tags
        input_["pit_policy"] = pit_policy
        if tags is not None:
            input_["tags"] = tags
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

    async def update(
        self,
        replication_configuration_template_id: "aws_sdk_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        arn: Optional["aws_sdk_drs.types.arn.ARN"] = None,
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
    ) -> "aws_sdk_drs.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Updates a ReplicationConfigurationTemplate by ID.</p>

        Args:
            replication_configuration_template_id: <p>The Replication Configuration Template ID.</p>
            arn: <p>The Replication Configuration Template ARN.</p>
            staging_area_subnet_id: <p>The subnet to be used by the replication staging area.</p>
            associate_default_security_group: <p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.</p>
            replication_servers_security_groups_i_ds: <p>The security group IDs that will be used by the replication server.</p>
            replication_server_instance_type: <p>The instance type to be used for the replication server.</p>
            use_dedicated_replication_server: <p>Whether to use a dedicated Replication Server in the replication staging area.</p>
            default_large_staging_disk_type: <p>The Staging Disk EBS volume type to be used during replication.</p>
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
            req: "AsyncOperationRequest[aws_sdk_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.update_replication_configuration_template

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.update_replication_configuration_template.async_update_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["replication_configuration_template_id"] = (
            replication_configuration_template_id
        )
        if arn is not None:
            input_["arn"] = arn
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

    async def delete(
        self,
        replication_configuration_template_id: "aws_sdk_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse":
        """<p>Deletes a single Replication Configuration Template by ID</p>

        Args:
            replication_configuration_template_id: <p>The ID of the Replication Configuration Template to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_replication_configuration_template

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_replication_configuration_template.async_delete_replication_configuration_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
        input_["replication_configuration_template_id"] = (
            replication_configuration_template_id
        )

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
        replication_configuration_template_i_ds: Optional[
            "aws_sdk_drs.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse":
        """<p>Lists all ReplicationConfigurationTemplates, filtered by Source Server IDs.</p>

        Args:
            replication_configuration_template_i_ds: <p>The IDs of the Replication Configuration Templates to retrieve. An empty list means all Replication Configuration Templates.</p>
            max_results: <p>Maximum number of Replication Configuration Templates to retrieve.</p>
            next_token: <p>The token of the next Replication Configuration Template to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_replication_configuration_templates

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.describe_replication_configuration_templates.async_describe_replication_configuration_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_drs.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest = {}  # type: ignore[typeddict-item]
        if replication_configuration_template_i_ds is not None:
            input_["replication_configuration_template_i_ds"] = (
                replication_configuration_template_i_ds
            )
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
