from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_vpc_lattice._auth._signers
import aws_sdk_vpc_lattice._auth._sigv4
from aws_sdk_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.create_service_network_vpc_association_request
    import aws_sdk_vpc_lattice.types.create_service_network_vpc_association_response
    import aws_sdk_vpc_lattice.types.delete_service_network_vpc_association_request
    import aws_sdk_vpc_lattice.types.delete_service_network_vpc_association_response
    import aws_sdk_vpc_lattice.types.dns_options
    import aws_sdk_vpc_lattice.types.get_service_network_vpc_association_request
    import aws_sdk_vpc_lattice.types.get_service_network_vpc_association_response
    import aws_sdk_vpc_lattice.types.list_service_network_vpc_associations_request
    import aws_sdk_vpc_lattice.types.list_service_network_vpc_associations_response
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.security_group_list
    import aws_sdk_vpc_lattice.types.service_network_identifier
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_identifier
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_summary
    import aws_sdk_vpc_lattice.types.tag_map
    import aws_sdk_vpc_lattice.types.update_service_network_vpc_association_request
    import aws_sdk_vpc_lattice.types.update_service_network_vpc_association_response
    import aws_sdk_vpc_lattice.types.vpc_id
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class ServiceNetworkVpcAssociation:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        vpc_identifier: "aws_sdk_vpc_lattice.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        private_dns_enabled: Optional[
            "aws_sdk_vpc_lattice.types.boolean.Boolean"
        ] = None,
        security_group_ids: Optional[
            "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
        dns_options: Optional[
            "aws_sdk_vpc_lattice.types.dns_options.DnsOptions"
        ] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_service_network_vpc_association_response.CreateServiceNetworkVpcAssociationResponse":
        r"""<p>Associates a VPC with a service network. When you associate a VPC with the service network, it enables all the resources within that VPC to be clients and communicate with other services in the service network. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations\">Manage VPC associations</a> in the <i>Amazon VPC Lattice User Guide</i>.</p> <p>You can't use this operation if there is a disassociation in progress. If the association fails, retry by deleting the association and recreating it.</p> <p>As a result of this operation, the association gets created in the service network account and the VPC owner account.</p> <p>If you add a security group to the service network and VPC association, the association must continue to always have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and recreate it without security groups.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            service_network_identifier: <p>The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.</p>
            vpc_identifier: <p>The ID of the VPC.</p>
            private_dns_enabled: <p> Indicates if private DNS is enabled for the VPC association. </p>
            security_group_ids: <p>The IDs of the security groups. Security groups aren't added by default. You can add a security group to apply network level controls to control which resources in a VPC are allowed to access the service network and its services. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html\">Control traffic to resources using security groups</a> in the <i>Amazon VPC User Guide</i>.</p>
            tags: <p>The tags for the association.</p>
            dns_options: <p> DNS options for the service network VPC association. </p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.create_service_network_vpc_association_request.CreateServiceNetworkVpcAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.create_service_network_vpc_association_response.CreateServiceNetworkVpcAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network_vpc_association

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network_vpc_association.create_service_network_vpc_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_service_network_vpc_association_request.CreateServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["service_network_identifier"] = service_network_identifier
        input_["vpc_identifier"] = vpc_identifier
        if private_dns_enabled is not None:
            input_["private_dns_enabled"] = private_dns_enabled
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if dns_options is not None:
            input_["dns_options"] = dns_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        service_network_vpc_association_identifier: "aws_sdk_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_service_network_vpc_association_response.GetServiceNetworkVpcAssociationResponse":
        """<p>Retrieves information about the specified association between a service network and a VPC.</p>

        Args:
            service_network_vpc_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_service_network_vpc_association_request.GetServiceNetworkVpcAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_service_network_vpc_association_response.GetServiceNetworkVpcAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network_vpc_association

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network_vpc_association.get_service_network_vpc_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_service_network_vpc_association_request.GetServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_vpc_association_identifier"] = (
            service_network_vpc_association_identifier
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        service_network_vpc_association_identifier: "aws_sdk_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier",
        security_group_ids: "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_service_network_vpc_association_response.UpdateServiceNetworkVpcAssociationResponse":
        """<p>Updates the service network and VPC association. If you add a security group to the service network and VPC association, the association must continue to have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and then recreate it without security groups.</p>

        Args:
            service_network_vpc_association_identifier: <p>The ID or ARN of the association.</p>
            security_group_ids: <p>The IDs of the security groups.</p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.update_service_network_vpc_association_request.UpdateServiceNetworkVpcAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.update_service_network_vpc_association_response.UpdateServiceNetworkVpcAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service_network_vpc_association

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service_network_vpc_association.update_service_network_vpc_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_service_network_vpc_association_request.UpdateServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_vpc_association_identifier"] = (
            service_network_vpc_association_identifier
        )
        input_["security_group_ids"] = security_group_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        service_network_vpc_association_identifier: "aws_sdk_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_service_network_vpc_association_response.DeleteServiceNetworkVpcAssociationResponse":
        """<p>Disassociates the VPC from the service network. You can't disassociate the VPC if there is a create or update association in progress.</p>

        Args:
            service_network_vpc_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_service_network_vpc_association_request.DeleteServiceNetworkVpcAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_service_network_vpc_association_response.DeleteServiceNetworkVpcAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network_vpc_association

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network_vpc_association.delete_service_network_vpc_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_service_network_vpc_association_request.DeleteServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_vpc_association_identifier"] = (
            service_network_vpc_association_identifier
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
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        service_network_identifier: Optional[
            "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
        ] = None,
        vpc_identifier: Optional["aws_sdk_vpc_lattice.types.vpc_id.VpcId"] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_service_network_vpc_associations_response.ListServiceNetworkVpcAssociationsResponse":
        """<p>Lists the associations between a service network and a VPC. You can filter the list either by VPC or service network. You must provide either the ID of the service network identifier or the ID of the VPC.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
            vpc_identifier: <p>The ID or ARN of the VPC.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_service_network_vpc_associations_request.ListServiceNetworkVpcAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_service_network_vpc_associations_response.ListServiceNetworkVpcAssociationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_associations

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_associations.list_service_network_vpc_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_service_network_vpc_associations_request.ListServiceNetworkVpcAssociationsRequest = {}  # type: ignore[typeddict-item]
        if service_network_identifier is not None:
            input_["service_network_identifier"] = service_network_identifier
        if vpc_identifier is not None:
            input_["vpc_identifier"] = vpc_identifier
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


class AsyncServiceNetworkVpcAssociation:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        vpc_identifier: "aws_sdk_vpc_lattice.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        private_dns_enabled: Optional[
            "aws_sdk_vpc_lattice.types.boolean.Boolean"
        ] = None,
        security_group_ids: Optional[
            "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
        dns_options: Optional[
            "aws_sdk_vpc_lattice.types.dns_options.DnsOptions"
        ] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_service_network_vpc_association_response.CreateServiceNetworkVpcAssociationResponse":
        r"""<p>Associates a VPC with a service network. When you associate a VPC with the service network, it enables all the resources within that VPC to be clients and communicate with other services in the service network. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations\">Manage VPC associations</a> in the <i>Amazon VPC Lattice User Guide</i>.</p> <p>You can't use this operation if there is a disassociation in progress. If the association fails, retry by deleting the association and recreating it.</p> <p>As a result of this operation, the association gets created in the service network account and the VPC owner account.</p> <p>If you add a security group to the service network and VPC association, the association must continue to always have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and recreate it without security groups.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            service_network_identifier: <p>The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.</p>
            vpc_identifier: <p>The ID of the VPC.</p>
            private_dns_enabled: <p> Indicates if private DNS is enabled for the VPC association. </p>
            security_group_ids: <p>The IDs of the security groups. Security groups aren't added by default. You can add a security group to apply network level controls to control which resources in a VPC are allowed to access the service network and its services. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html\">Control traffic to resources using security groups</a> in the <i>Amazon VPC User Guide</i>.</p>
            tags: <p>The tags for the association.</p>
            dns_options: <p> DNS options for the service network VPC association. </p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.create_service_network_vpc_association_request.CreateServiceNetworkVpcAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.create_service_network_vpc_association_response.CreateServiceNetworkVpcAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network_vpc_association

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network_vpc_association.async_create_service_network_vpc_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_service_network_vpc_association_request.CreateServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["service_network_identifier"] = service_network_identifier
        input_["vpc_identifier"] = vpc_identifier
        if private_dns_enabled is not None:
            input_["private_dns_enabled"] = private_dns_enabled
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if tags is not None:
            input_["tags"] = tags
        if dns_options is not None:
            input_["dns_options"] = dns_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        service_network_vpc_association_identifier: "aws_sdk_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_service_network_vpc_association_response.GetServiceNetworkVpcAssociationResponse":
        """<p>Retrieves information about the specified association between a service network and a VPC.</p>

        Args:
            service_network_vpc_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_service_network_vpc_association_request.GetServiceNetworkVpcAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_service_network_vpc_association_response.GetServiceNetworkVpcAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network_vpc_association

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network_vpc_association.async_get_service_network_vpc_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_service_network_vpc_association_request.GetServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_vpc_association_identifier"] = (
            service_network_vpc_association_identifier
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        service_network_vpc_association_identifier: "aws_sdk_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier",
        security_group_ids: "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_service_network_vpc_association_response.UpdateServiceNetworkVpcAssociationResponse":
        """<p>Updates the service network and VPC association. If you add a security group to the service network and VPC association, the association must continue to have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and then recreate it without security groups.</p>

        Args:
            service_network_vpc_association_identifier: <p>The ID or ARN of the association.</p>
            security_group_ids: <p>The IDs of the security groups.</p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.update_service_network_vpc_association_request.UpdateServiceNetworkVpcAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.update_service_network_vpc_association_response.UpdateServiceNetworkVpcAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service_network_vpc_association

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.update_service_network_vpc_association.async_update_service_network_vpc_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_service_network_vpc_association_request.UpdateServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_vpc_association_identifier"] = (
            service_network_vpc_association_identifier
        )
        input_["security_group_ids"] = security_group_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        service_network_vpc_association_identifier: "aws_sdk_vpc_lattice.types.service_network_vpc_association_identifier.ServiceNetworkVpcAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_service_network_vpc_association_response.DeleteServiceNetworkVpcAssociationResponse":
        """<p>Disassociates the VPC from the service network. You can't disassociate the VPC if there is a create or update association in progress.</p>

        Args:
            service_network_vpc_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_service_network_vpc_association_request.DeleteServiceNetworkVpcAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_service_network_vpc_association_response.DeleteServiceNetworkVpcAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network_vpc_association

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network_vpc_association.async_delete_service_network_vpc_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_service_network_vpc_association_request.DeleteServiceNetworkVpcAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_vpc_association_identifier"] = (
            service_network_vpc_association_identifier
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
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        service_network_identifier: Optional[
            "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
        ] = None,
        vpc_identifier: Optional["aws_sdk_vpc_lattice.types.vpc_id.VpcId"] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_service_network_vpc_associations_response.ListServiceNetworkVpcAssociationsResponse":
        """<p>Lists the associations between a service network and a VPC. You can filter the list either by VPC or service network. You must provide either the ID of the service network identifier or the ID of the VPC.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
            vpc_identifier: <p>The ID or ARN of the VPC.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_service_network_vpc_associations_request.ListServiceNetworkVpcAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_service_network_vpc_associations_response.ListServiceNetworkVpcAssociationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_associations

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_vpc_associations.async_list_service_network_vpc_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_service_network_vpc_associations_request.ListServiceNetworkVpcAssociationsRequest = {}  # type: ignore[typeddict-item]
        if service_network_identifier is not None:
            input_["service_network_identifier"] = service_network_identifier
        if vpc_identifier is not None:
            input_["vpc_identifier"] = vpc_identifier
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
