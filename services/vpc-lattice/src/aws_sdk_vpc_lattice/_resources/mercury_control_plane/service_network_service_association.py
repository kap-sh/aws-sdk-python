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
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.create_service_network_service_association_request
    import aws_sdk_vpc_lattice.types.create_service_network_service_association_response
    import aws_sdk_vpc_lattice.types.delete_service_network_service_association_request
    import aws_sdk_vpc_lattice.types.delete_service_network_service_association_response
    import aws_sdk_vpc_lattice.types.get_service_network_service_association_request
    import aws_sdk_vpc_lattice.types.get_service_network_service_association_response
    import aws_sdk_vpc_lattice.types.list_service_network_service_associations_request
    import aws_sdk_vpc_lattice.types.list_service_network_service_associations_response
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.service_identifier
    import aws_sdk_vpc_lattice.types.service_network_identifier
    import aws_sdk_vpc_lattice.types.service_network_service_association_identifier
    import aws_sdk_vpc_lattice.types.service_network_service_association_summary
    import aws_sdk_vpc_lattice.types.tag_map
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class ServiceNetworkServiceAssociation:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_service_network_service_association_response.CreateServiceNetworkServiceAssociationResponse":
        r"""<p>Associates the specified service with the specified service network. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations\">Manage service associations</a> in the <i>Amazon VPC Lattice User Guide</i>.</p> <p>You can't use this operation if the service and service network are already associated or if there is a disassociation or deletion in progress. If the association fails, you can retry the operation by deleting the association and recreating it.</p> <p>You cannot associate a service and service network that are shared with a caller. The caller must own either the service or the service network.</p> <p>As a result of this operation, the association is created in the service network account and the association owner account.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            service_identifier: <p>The ID or ARN of the service.</p>
            service_network_identifier: <p>The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.</p>
            tags: <p>The tags for the association.</p>

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
            req: "OperationRequest[aws_sdk_vpc_lattice.types.create_service_network_service_association_request.CreateServiceNetworkServiceAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.create_service_network_service_association_response.CreateServiceNetworkServiceAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network_service_association

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network_service_association.create_service_network_service_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_service_network_service_association_request.CreateServiceNetworkServiceAssociationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["service_identifier"] = service_identifier
        input_["service_network_identifier"] = service_network_identifier
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
        service_network_service_association_identifier: "aws_sdk_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_service_network_service_association_response.GetServiceNetworkServiceAssociationResponse":
        """<p>Retrieves information about the specified association between a service network and a service.</p>

        Args:
            service_network_service_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_service_network_service_association_request.GetServiceNetworkServiceAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_service_network_service_association_response.GetServiceNetworkServiceAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network_service_association

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network_service_association.get_service_network_service_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_service_network_service_association_request.GetServiceNetworkServiceAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_service_association_identifier"] = (
            service_network_service_association_identifier
        )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        service_network_service_association_identifier: "aws_sdk_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_service_network_service_association_response.DeleteServiceNetworkServiceAssociationResponse":
        """<p>Deletes the association between a service and a service network. This operation fails if an association is still in progress.</p>

        Args:
            service_network_service_association_identifier: <p>The ID or ARN of the association.</p>

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
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_service_network_service_association_request.DeleteServiceNetworkServiceAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_service_network_service_association_response.DeleteServiceNetworkServiceAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network_service_association

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network_service_association.delete_service_network_service_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_service_network_service_association_request.DeleteServiceNetworkServiceAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_service_association_identifier"] = (
            service_network_service_association_identifier
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
        service_identifier: Optional[
            "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
        ] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_service_network_service_associations_response.ListServiceNetworkServiceAssociationsResponse":
        """<p>Lists the associations between a service network and a service. You can filter the list either by service or service network. You must provide either the service network identifier or the service identifier.</p> <p>Every association in Amazon VPC Lattice has a unique Amazon Resource Name (ARN), such as when a service network is associated with a VPC or when a service is associated with a service network. If the association is for a resource is shared with another account, the association includes the local account ID as the prefix in the ARN.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
            service_identifier: <p>The ID or ARN of the service.</p>
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
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_service_network_service_associations_request.ListServiceNetworkServiceAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_service_network_service_associations_response.ListServiceNetworkServiceAssociationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_service_associations

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_service_associations.list_service_network_service_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_service_network_service_associations_request.ListServiceNetworkServiceAssociationsRequest = {}  # type: ignore[typeddict-item]
        if service_network_identifier is not None:
            input_["service_network_identifier"] = service_network_identifier
        if service_identifier is not None:
            input_["service_identifier"] = service_identifier
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


class AsyncServiceNetworkServiceAssociation:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier",
        service_network_identifier: "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_service_network_service_association_response.CreateServiceNetworkServiceAssociationResponse":
        r"""<p>Associates the specified service with the specified service network. For more information, see <a href=\"https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations\">Manage service associations</a> in the <i>Amazon VPC Lattice User Guide</i>.</p> <p>You can't use this operation if the service and service network are already associated or if there is a disassociation or deletion in progress. If the association fails, you can retry the operation by deleting the association and recreating it.</p> <p>You cannot associate a service and service network that are shared with a caller. The caller must own either the service or the service network.</p> <p>As a result of this operation, the association is created in the service network account and the association owner account.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            service_identifier: <p>The ID or ARN of the service.</p>
            service_network_identifier: <p>The ID or ARN of the service network. You must use an ARN if the resources are in different accounts.</p>
            tags: <p>The tags for the association.</p>

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
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.create_service_network_service_association_request.CreateServiceNetworkServiceAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.create_service_network_service_association_response.CreateServiceNetworkServiceAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network_service_association

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.create_service_network_service_association.async_create_service_network_service_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_service_network_service_association_request.CreateServiceNetworkServiceAssociationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["service_identifier"] = service_identifier
        input_["service_network_identifier"] = service_network_identifier
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
        service_network_service_association_identifier: "aws_sdk_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_service_network_service_association_response.GetServiceNetworkServiceAssociationResponse":
        """<p>Retrieves information about the specified association between a service network and a service.</p>

        Args:
            service_network_service_association_identifier: <p>The ID or ARN of the association.</p>

        Raises:
            aws_sdk_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            aws_sdk_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            aws_sdk_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            aws_sdk_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            aws_sdk_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_service_network_service_association_request.GetServiceNetworkServiceAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_service_network_service_association_response.GetServiceNetworkServiceAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network_service_association

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_service_network_service_association.async_get_service_network_service_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_service_network_service_association_request.GetServiceNetworkServiceAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_service_association_identifier"] = (
            service_network_service_association_identifier
        )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        service_network_service_association_identifier: "aws_sdk_vpc_lattice.types.service_network_service_association_identifier.ServiceNetworkServiceAssociationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_service_network_service_association_response.DeleteServiceNetworkServiceAssociationResponse":
        """<p>Deletes the association between a service and a service network. This operation fails if an association is still in progress.</p>

        Args:
            service_network_service_association_identifier: <p>The ID or ARN of the association.</p>

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
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_service_network_service_association_request.DeleteServiceNetworkServiceAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_service_network_service_association_response.DeleteServiceNetworkServiceAssociationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network_service_association

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_service_network_service_association.async_delete_service_network_service_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_service_network_service_association_request.DeleteServiceNetworkServiceAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["service_network_service_association_identifier"] = (
            service_network_service_association_identifier
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
        service_identifier: Optional[
            "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
        ] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_service_network_service_associations_response.ListServiceNetworkServiceAssociationsResponse":
        """<p>Lists the associations between a service network and a service. You can filter the list either by service or service network. You must provide either the service network identifier or the service identifier.</p> <p>Every association in Amazon VPC Lattice has a unique Amazon Resource Name (ARN), such as when a service network is associated with a VPC or when a service is associated with a service network. If the association is for a resource is shared with another account, the association includes the local account ID as the prefix in the ARN.</p>

        Args:
            service_network_identifier: <p>The ID or ARN of the service network.</p>
            service_identifier: <p>The ID or ARN of the service.</p>
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
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_service_network_service_associations_request.ListServiceNetworkServiceAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_service_network_service_associations_response.ListServiceNetworkServiceAssociationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_service_associations

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_service_network_service_associations.async_list_service_network_service_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_service_network_service_associations_request.ListServiceNetworkServiceAssociationsRequest = {}  # type: ignore[typeddict-item]
        if service_network_identifier is not None:
            input_["service_network_identifier"] = service_network_identifier
        if service_identifier is not None:
            input_["service_identifier"] = service_identifier
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
