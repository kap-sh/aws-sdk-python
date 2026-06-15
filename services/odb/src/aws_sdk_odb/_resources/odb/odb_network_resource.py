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
    import aws_sdk_odb.types.access
    import aws_sdk_odb.types.create_odb_network_input
    import aws_sdk_odb.types.create_odb_network_output
    import aws_sdk_odb.types.delete_odb_network_input
    import aws_sdk_odb.types.delete_odb_network_output
    import aws_sdk_odb.types.general_input_string
    import aws_sdk_odb.types.get_odb_network_input
    import aws_sdk_odb.types.get_odb_network_output
    import aws_sdk_odb.types.list_odb_networks_input
    import aws_sdk_odb.types.list_odb_networks_output
    import aws_sdk_odb.types.odb_network_summary
    import aws_sdk_odb.types.policy_document
    import aws_sdk_odb.types.request_tag_map
    import aws_sdk_odb.types.resource_display_name
    import aws_sdk_odb.types.resource_id_or_arn
    import aws_sdk_odb.types.string_list
    import aws_sdk_odb.types.update_odb_network_input
    import aws_sdk_odb.types.update_odb_network_output
    from aws_sdk_odb._services.async_odb import AsyncodbClient, AsyncodbClientConfig
    from aws_sdk_odb._services.odb import odbClient, odbClientConfig


class OdbNetworkResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service

    def create(
        self,
        display_name: "aws_sdk_odb.types.resource_display_name.ResourceDisplayName",
        client_subnet_cidr: str,
        *,
        config_overrides: Optional[odbClientConfig] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
        backup_subnet_cidr: Optional[str] = None,
        custom_domain_name: Optional[str] = None,
        default_dns_prefix: Optional[str] = None,
        client_token: Optional[
            "aws_sdk_odb.types.general_input_string.GeneralInputString"
        ] = None,
        s3_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        zero_etl_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        sts_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        kms_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        s3_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        sts_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        kms_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        cross_region_s3_restore_sources_to_enable: Optional[
            "aws_sdk_odb.types.string_list.StringList"
        ] = None,
        tags: Optional["aws_sdk_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "aws_sdk_odb.types.create_odb_network_output.CreateOdbNetworkOutput":
        """<p>Creates an ODB network.</p>

        Args:
            display_name: <p>A user-friendly name for the ODB network.</p>
            availability_zone: <p>The Amazon Web Services Availability Zone (AZ) where the ODB network is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p>
            availability_zone_id: <p>The AZ ID of the AZ where the ODB network is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p>
            client_subnet_cidr: <p>The CIDR range of the client subnet for the ODB network.</p> <p>Constraints:</p> <ul> <li> <p>Must not overlap with the CIDR range of the backup subnet.</p> </li> <li> <p>Must not overlap with the CIDR ranges of the VPCs that are connected to the ODB network.</p> </li> <li> <p>Must not use the following CIDR ranges that are reserved by OCI:</p> <ul> <li> <p> <code>100.106.0.0/16</code> and <code>100.107.0.0/16</code> </p> </li> <li> <p> <code>169.254.0.0/16</code> </p> </li> <li> <p> <code>224.0.0.0 - 239.255.255.255</code> </p> </li> <li> <p> <code>240.0.0.0 - 255.255.255.255</code> </p> </li> </ul> </li> </ul>
            backup_subnet_cidr: <p>The CIDR range of the backup subnet for the ODB network.</p> <p>Constraints:</p> <ul> <li> <p>Must not overlap with the CIDR range of the client subnet.</p> </li> <li> <p>Must not overlap with the CIDR ranges of the VPCs that are connected to the ODB network.</p> </li> <li> <p>Must not use the following CIDR ranges that are reserved by OCI:</p> <ul> <li> <p> <code>100.106.0.0/16</code> and <code>100.107.0.0/16</code> </p> </li> <li> <p> <code>169.254.0.0/16</code> </p> </li> <li> <p> <code>224.0.0.0 - 239.255.255.255</code> </p> </li> <li> <p> <code>240.0.0.0 - 255.255.255.255</code> </p> </li> </ul> </li> </ul>
            custom_domain_name: <p>The domain name to use for the resources in the ODB network.</p>
            default_dns_prefix: <p>The DNS prefix to the default DNS domain name. The default DNS domain name is oraclevcn.com.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>
            s3_access: <p>Specifies the configuration for Amazon S3 access from the ODB network.</p>
            zero_etl_access: <p>Specifies the configuration for Zero-ETL access from the ODB network.</p>
            sts_access: <p>The Amazon Web Services Security Token Service (STS) access configuration for the ODB network.</p>
            kms_access: <p>The Amazon Web Services Key Management Service (KMS) access configuration for the ODB network.</p>
            s3_policy_document: <p>Specifies the endpoint policy for Amazon S3 access from the ODB network.</p>
            sts_policy_document: <p>The Amazon Web Services Security Token Service (STS) policy document that defines permissions for token service usage within the ODB network.</p>
            kms_policy_document: <p>The Amazon Web Services Key Management Service (KMS) policy document that defines permissions for key usage within the ODB network.</p>
            cross_region_s3_restore_sources_to_enable: <p>The cross-Region Amazon S3 restore sources to enable for the ODB network.</p>
            tags: <p>The list of resource tags to apply to the ODB network.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.create_odb_network_input.CreateOdbNetworkInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.create_odb_network_output.CreateOdbNetworkOutput"
        ]:
            import aws_sdk_odb._operations.odb.create_odb_network

            output, http_response = (
                aws_sdk_odb._operations.odb.create_odb_network.create_odb_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.create_odb_network_input.CreateOdbNetworkInput = {}  # type: ignore[typeddict-item]
        input_["display_name"] = display_name
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        input_["client_subnet_cidr"] = client_subnet_cidr
        if backup_subnet_cidr is not None:
            input_["backup_subnet_cidr"] = backup_subnet_cidr
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if default_dns_prefix is not None:
            input_["default_dns_prefix"] = default_dns_prefix
        if client_token is not None:
            input_["client_token"] = client_token
        if s3_access is not None:
            input_["s3_access"] = s3_access
        if zero_etl_access is not None:
            input_["zero_etl_access"] = zero_etl_access
        if sts_access is not None:
            input_["sts_access"] = sts_access
        if kms_access is not None:
            input_["kms_access"] = kms_access
        if s3_policy_document is not None:
            input_["s3_policy_document"] = s3_policy_document
        if sts_policy_document is not None:
            input_["sts_policy_document"] = sts_policy_document
        if kms_policy_document is not None:
            input_["kms_policy_document"] = kms_policy_document
        if cross_region_s3_restore_sources_to_enable is not None:
            input_["cross_region_s3_restore_sources_to_enable"] = (
                cross_region_s3_restore_sources_to_enable
            )
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        odb_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.get_odb_network_output.GetOdbNetworkOutput":
        """<p>Returns information about the specified ODB network.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.get_odb_network_input.GetOdbNetworkInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.get_odb_network_output.GetOdbNetworkOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_odb_network

            output, http_response = (
                aws_sdk_odb._operations.odb.get_odb_network.get_odb_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.get_odb_network_input.GetOdbNetworkInput = {}  # type: ignore[typeddict-item]
        input_["odb_network_id"] = odb_network_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        odb_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        display_name: Optional[
            "aws_sdk_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        peered_cidrs_to_be_added: Optional[
            "aws_sdk_odb.types.string_list.StringList"
        ] = None,
        peered_cidrs_to_be_removed: Optional[
            "aws_sdk_odb.types.string_list.StringList"
        ] = None,
        s3_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        zero_etl_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        sts_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        kms_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        s3_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        sts_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        kms_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        cross_region_s3_restore_sources_to_enable: Optional[
            "aws_sdk_odb.types.string_list.StringList"
        ] = None,
        cross_region_s3_restore_sources_to_disable: Optional[
            "aws_sdk_odb.types.string_list.StringList"
        ] = None,
    ) -> "aws_sdk_odb.types.update_odb_network_output.UpdateOdbNetworkOutput":
        """<p>Updates properties of a specified ODB network.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network to update.</p>
            display_name: <p>The new user-friendly name of the ODB network.</p>
            peered_cidrs_to_be_added: <p>The list of CIDR ranges from the peered VPC that allow access to the ODB network.</p>
            peered_cidrs_to_be_removed: <p>The list of CIDR ranges from the peered VPC to remove from the ODB network.</p>
            s3_access: <p>Specifies the updated configuration for Amazon S3 access from the ODB network.</p>
            zero_etl_access: <p>Specifies the updated configuration for Zero-ETL access from the ODB network.</p>
            sts_access: <p>The Amazon Web Services Security Token Service (STS) access configuration for the ODB network.</p>
            kms_access: <p>The Amazon Web Services Key Management Service (KMS) access configuration for the ODB network.</p>
            s3_policy_document: <p>Specifies the updated endpoint policy for Amazon S3 access from the ODB network.</p>
            sts_policy_document: <p>The Amazon Web Services Security Token Service (STS) policy document that defines permissions for token service usage within the ODB network.</p>
            kms_policy_document: <p>The Amazon Web Services Key Management Service (KMS) policy document that defines permissions for key usage within the ODB network.</p>
            cross_region_s3_restore_sources_to_enable: <p>The cross-Region Amazon S3 restore sources to enable for the ODB network.</p>
            cross_region_s3_restore_sources_to_disable: <p>The cross-Region Amazon S3 restore sources to disable for the ODB network.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.update_odb_network_input.UpdateOdbNetworkInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.update_odb_network_output.UpdateOdbNetworkOutput"
        ]:
            import aws_sdk_odb._operations.odb.update_odb_network

            output, http_response = (
                aws_sdk_odb._operations.odb.update_odb_network.update_odb_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.update_odb_network_input.UpdateOdbNetworkInput = {}  # type: ignore[typeddict-item]
        input_["odb_network_id"] = odb_network_id
        if display_name is not None:
            input_["display_name"] = display_name
        if peered_cidrs_to_be_added is not None:
            input_["peered_cidrs_to_be_added"] = peered_cidrs_to_be_added
        if peered_cidrs_to_be_removed is not None:
            input_["peered_cidrs_to_be_removed"] = peered_cidrs_to_be_removed
        if s3_access is not None:
            input_["s3_access"] = s3_access
        if zero_etl_access is not None:
            input_["zero_etl_access"] = zero_etl_access
        if sts_access is not None:
            input_["sts_access"] = sts_access
        if kms_access is not None:
            input_["kms_access"] = kms_access
        if s3_policy_document is not None:
            input_["s3_policy_document"] = s3_policy_document
        if sts_policy_document is not None:
            input_["sts_policy_document"] = sts_policy_document
        if kms_policy_document is not None:
            input_["kms_policy_document"] = kms_policy_document
        if cross_region_s3_restore_sources_to_enable is not None:
            input_["cross_region_s3_restore_sources_to_enable"] = (
                cross_region_s3_restore_sources_to_enable
            )
        if cross_region_s3_restore_sources_to_disable is not None:
            input_["cross_region_s3_restore_sources_to_disable"] = (
                cross_region_s3_restore_sources_to_disable
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        odb_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        delete_associated_resources: bool,
        *,
        config_overrides: Optional[odbClientConfig] = None,
    ) -> "aws_sdk_odb.types.delete_odb_network_output.DeleteOdbNetworkOutput":
        """<p>Deletes the specified ODB network.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network to delete.</p>
            delete_associated_resources: <p>Specifies whether to delete associated OCI networking resources along with the ODB network.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.delete_odb_network_input.DeleteOdbNetworkInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.delete_odb_network_output.DeleteOdbNetworkOutput"
        ]:
            import aws_sdk_odb._operations.odb.delete_odb_network

            output, http_response = (
                aws_sdk_odb._operations.odb.delete_odb_network.delete_odb_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.delete_odb_network_input.DeleteOdbNetworkInput = {}  # type: ignore[typeddict-item]
        input_["odb_network_id"] = odb_network_id
        input_["delete_associated_resources"] = delete_associated_resources

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
    ) -> "aws_sdk_odb.types.list_odb_networks_output.ListOdbNetworksOutput":
        """<p>Returns information about the ODB networks owned by your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_odb.types.list_odb_networks_input.ListOdbNetworksInput]",
        ) -> OperationResponse[
            "aws_sdk_odb.types.list_odb_networks_output.ListOdbNetworksOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_odb_networks

            output, http_response = (
                aws_sdk_odb._operations.odb.list_odb_networks.list_odb_networks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_odb_networks_input.ListOdbNetworksInput = {}  # type: ignore[typeddict-item]
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


class AsyncOdbNetworkResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service

    async def create(
        self,
        display_name: "aws_sdk_odb.types.resource_display_name.ResourceDisplayName",
        client_subnet_cidr: str,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
        backup_subnet_cidr: Optional[str] = None,
        custom_domain_name: Optional[str] = None,
        default_dns_prefix: Optional[str] = None,
        client_token: Optional[
            "aws_sdk_odb.types.general_input_string.GeneralInputString"
        ] = None,
        s3_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        zero_etl_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        sts_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        kms_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        s3_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        sts_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        kms_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        cross_region_s3_restore_sources_to_enable: Optional[
            "aws_sdk_odb.types.string_list.StringList"
        ] = None,
        tags: Optional["aws_sdk_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "aws_sdk_odb.types.create_odb_network_output.CreateOdbNetworkOutput":
        """<p>Creates an ODB network.</p>

        Args:
            display_name: <p>A user-friendly name for the ODB network.</p>
            availability_zone: <p>The Amazon Web Services Availability Zone (AZ) where the ODB network is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p>
            availability_zone_id: <p>The AZ ID of the AZ where the ODB network is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p>
            client_subnet_cidr: <p>The CIDR range of the client subnet for the ODB network.</p> <p>Constraints:</p> <ul> <li> <p>Must not overlap with the CIDR range of the backup subnet.</p> </li> <li> <p>Must not overlap with the CIDR ranges of the VPCs that are connected to the ODB network.</p> </li> <li> <p>Must not use the following CIDR ranges that are reserved by OCI:</p> <ul> <li> <p> <code>100.106.0.0/16</code> and <code>100.107.0.0/16</code> </p> </li> <li> <p> <code>169.254.0.0/16</code> </p> </li> <li> <p> <code>224.0.0.0 - 239.255.255.255</code> </p> </li> <li> <p> <code>240.0.0.0 - 255.255.255.255</code> </p> </li> </ul> </li> </ul>
            backup_subnet_cidr: <p>The CIDR range of the backup subnet for the ODB network.</p> <p>Constraints:</p> <ul> <li> <p>Must not overlap with the CIDR range of the client subnet.</p> </li> <li> <p>Must not overlap with the CIDR ranges of the VPCs that are connected to the ODB network.</p> </li> <li> <p>Must not use the following CIDR ranges that are reserved by OCI:</p> <ul> <li> <p> <code>100.106.0.0/16</code> and <code>100.107.0.0/16</code> </p> </li> <li> <p> <code>169.254.0.0/16</code> </p> </li> <li> <p> <code>224.0.0.0 - 239.255.255.255</code> </p> </li> <li> <p> <code>240.0.0.0 - 255.255.255.255</code> </p> </li> </ul> </li> </ul>
            custom_domain_name: <p>The domain name to use for the resources in the ODB network.</p>
            default_dns_prefix: <p>The DNS prefix to the default DNS domain name. The default DNS domain name is oraclevcn.com.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>
            s3_access: <p>Specifies the configuration for Amazon S3 access from the ODB network.</p>
            zero_etl_access: <p>Specifies the configuration for Zero-ETL access from the ODB network.</p>
            sts_access: <p>The Amazon Web Services Security Token Service (STS) access configuration for the ODB network.</p>
            kms_access: <p>The Amazon Web Services Key Management Service (KMS) access configuration for the ODB network.</p>
            s3_policy_document: <p>Specifies the endpoint policy for Amazon S3 access from the ODB network.</p>
            sts_policy_document: <p>The Amazon Web Services Security Token Service (STS) policy document that defines permissions for token service usage within the ODB network.</p>
            kms_policy_document: <p>The Amazon Web Services Key Management Service (KMS) policy document that defines permissions for key usage within the ODB network.</p>
            cross_region_s3_restore_sources_to_enable: <p>The cross-Region Amazon S3 restore sources to enable for the ODB network.</p>
            tags: <p>The list of resource tags to apply to the ODB network.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.create_odb_network_input.CreateOdbNetworkInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.create_odb_network_output.CreateOdbNetworkOutput"
        ]:
            import aws_sdk_odb._operations.odb.create_odb_network

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.create_odb_network.async_create_odb_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.create_odb_network_input.CreateOdbNetworkInput = {}  # type: ignore[typeddict-item]
        input_["display_name"] = display_name
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        input_["client_subnet_cidr"] = client_subnet_cidr
        if backup_subnet_cidr is not None:
            input_["backup_subnet_cidr"] = backup_subnet_cidr
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if default_dns_prefix is not None:
            input_["default_dns_prefix"] = default_dns_prefix
        if client_token is not None:
            input_["client_token"] = client_token
        if s3_access is not None:
            input_["s3_access"] = s3_access
        if zero_etl_access is not None:
            input_["zero_etl_access"] = zero_etl_access
        if sts_access is not None:
            input_["sts_access"] = sts_access
        if kms_access is not None:
            input_["kms_access"] = kms_access
        if s3_policy_document is not None:
            input_["s3_policy_document"] = s3_policy_document
        if sts_policy_document is not None:
            input_["sts_policy_document"] = sts_policy_document
        if kms_policy_document is not None:
            input_["kms_policy_document"] = kms_policy_document
        if cross_region_s3_restore_sources_to_enable is not None:
            input_["cross_region_s3_restore_sources_to_enable"] = (
                cross_region_s3_restore_sources_to_enable
            )
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        odb_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "aws_sdk_odb.types.get_odb_network_output.GetOdbNetworkOutput":
        """<p>Returns information about the specified ODB network.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.get_odb_network_input.GetOdbNetworkInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.get_odb_network_output.GetOdbNetworkOutput"
        ]:
            import aws_sdk_odb._operations.odb.get_odb_network

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.get_odb_network.async_get_odb_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.get_odb_network_input.GetOdbNetworkInput = {}  # type: ignore[typeddict-item]
        input_["odb_network_id"] = odb_network_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        odb_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        display_name: Optional[
            "aws_sdk_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        peered_cidrs_to_be_added: Optional[
            "aws_sdk_odb.types.string_list.StringList"
        ] = None,
        peered_cidrs_to_be_removed: Optional[
            "aws_sdk_odb.types.string_list.StringList"
        ] = None,
        s3_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        zero_etl_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        sts_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        kms_access: Optional["aws_sdk_odb.types.access.Access"] = None,
        s3_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        sts_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        kms_policy_document: Optional[
            "aws_sdk_odb.types.policy_document.PolicyDocument"
        ] = None,
        cross_region_s3_restore_sources_to_enable: Optional[
            "aws_sdk_odb.types.string_list.StringList"
        ] = None,
        cross_region_s3_restore_sources_to_disable: Optional[
            "aws_sdk_odb.types.string_list.StringList"
        ] = None,
    ) -> "aws_sdk_odb.types.update_odb_network_output.UpdateOdbNetworkOutput":
        """<p>Updates properties of a specified ODB network.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network to update.</p>
            display_name: <p>The new user-friendly name of the ODB network.</p>
            peered_cidrs_to_be_added: <p>The list of CIDR ranges from the peered VPC that allow access to the ODB network.</p>
            peered_cidrs_to_be_removed: <p>The list of CIDR ranges from the peered VPC to remove from the ODB network.</p>
            s3_access: <p>Specifies the updated configuration for Amazon S3 access from the ODB network.</p>
            zero_etl_access: <p>Specifies the updated configuration for Zero-ETL access from the ODB network.</p>
            sts_access: <p>The Amazon Web Services Security Token Service (STS) access configuration for the ODB network.</p>
            kms_access: <p>The Amazon Web Services Key Management Service (KMS) access configuration for the ODB network.</p>
            s3_policy_document: <p>Specifies the updated endpoint policy for Amazon S3 access from the ODB network.</p>
            sts_policy_document: <p>The Amazon Web Services Security Token Service (STS) policy document that defines permissions for token service usage within the ODB network.</p>
            kms_policy_document: <p>The Amazon Web Services Key Management Service (KMS) policy document that defines permissions for key usage within the ODB network.</p>
            cross_region_s3_restore_sources_to_enable: <p>The cross-Region Amazon S3 restore sources to enable for the ODB network.</p>
            cross_region_s3_restore_sources_to_disable: <p>The cross-Region Amazon S3 restore sources to disable for the ODB network.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.update_odb_network_input.UpdateOdbNetworkInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.update_odb_network_output.UpdateOdbNetworkOutput"
        ]:
            import aws_sdk_odb._operations.odb.update_odb_network

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.update_odb_network.async_update_odb_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.update_odb_network_input.UpdateOdbNetworkInput = {}  # type: ignore[typeddict-item]
        input_["odb_network_id"] = odb_network_id
        if display_name is not None:
            input_["display_name"] = display_name
        if peered_cidrs_to_be_added is not None:
            input_["peered_cidrs_to_be_added"] = peered_cidrs_to_be_added
        if peered_cidrs_to_be_removed is not None:
            input_["peered_cidrs_to_be_removed"] = peered_cidrs_to_be_removed
        if s3_access is not None:
            input_["s3_access"] = s3_access
        if zero_etl_access is not None:
            input_["zero_etl_access"] = zero_etl_access
        if sts_access is not None:
            input_["sts_access"] = sts_access
        if kms_access is not None:
            input_["kms_access"] = kms_access
        if s3_policy_document is not None:
            input_["s3_policy_document"] = s3_policy_document
        if sts_policy_document is not None:
            input_["sts_policy_document"] = sts_policy_document
        if kms_policy_document is not None:
            input_["kms_policy_document"] = kms_policy_document
        if cross_region_s3_restore_sources_to_enable is not None:
            input_["cross_region_s3_restore_sources_to_enable"] = (
                cross_region_s3_restore_sources_to_enable
            )
        if cross_region_s3_restore_sources_to_disable is not None:
            input_["cross_region_s3_restore_sources_to_disable"] = (
                cross_region_s3_restore_sources_to_disable
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        odb_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn",
        delete_associated_resources: bool,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "aws_sdk_odb.types.delete_odb_network_output.DeleteOdbNetworkOutput":
        """<p>Deletes the specified ODB network.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network to delete.</p>
            delete_associated_resources: <p>Specifies whether to delete associated OCI networking resources along with the ODB network.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.delete_odb_network_input.DeleteOdbNetworkInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.delete_odb_network_output.DeleteOdbNetworkOutput"
        ]:
            import aws_sdk_odb._operations.odb.delete_odb_network

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.delete_odb_network.async_delete_odb_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.delete_odb_network_input.DeleteOdbNetworkInput = {}  # type: ignore[typeddict-item]
        input_["odb_network_id"] = odb_network_id
        input_["delete_associated_resources"] = delete_associated_resources

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
    ) -> "aws_sdk_odb.types.list_odb_networks_output.ListOdbNetworksOutput":
        """<p>Returns information about the ODB networks owned by your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_odb.types.list_odb_networks_input.ListOdbNetworksInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_odb.types.list_odb_networks_output.ListOdbNetworksOutput"
        ]:
            import aws_sdk_odb._operations.odb.list_odb_networks

            (
                output,
                http_response,
            ) = await aws_sdk_odb._operations.odb.list_odb_networks.async_list_odb_networks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_odb.types.list_odb_networks_input.ListOdbNetworksInput = {}  # type: ignore[typeddict-item]
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
