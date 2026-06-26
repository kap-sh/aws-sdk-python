from __future__ import annotations

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
    import aws_sdk_mgn.types.delete_vcenter_client_request
    import aws_sdk_mgn.types.describe_vcenter_clients_request
    import aws_sdk_mgn.types.describe_vcenter_clients_response
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token
    import aws_sdk_mgn.types.vcenter_client
    import aws_sdk_mgn.types.vcenter_client_id
    from aws_sdk_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from aws_sdk_mgn._services.mgn import mgnClient, mgnClientConfig


class VcenterClientResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def delete(
        self,
        vcenter_client_id: "aws_sdk_mgn.types.vcenter_client_id.VcenterClientID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> None:
        """<p>Deletes a given vCenter client by ID.</p>

        Args:
            vcenter_client_id: <p>ID of resource to be deleted.</p>

        Raises:
            aws_sdk_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            aws_sdk_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            aws_sdk_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            aws_sdk_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.delete_vcenter_client_request.DeleteVcenterClientRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_mgn._operations.application_migration_service.delete_vcenter_client

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.delete_vcenter_client.delete_vcenter_client(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.delete_vcenter_client_request.DeleteVcenterClientRequest = {}  # type: ignore[typeddict-item]
        input_["vcenter_client_id"] = vcenter_client_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse":
        """<p>Returns a list of the installed vCenter clients.</p>

        Args:
            max_results: <p>Maximum results to be returned in DescribeVcenterClients.</p>
            next_token: <p>Next pagination token to be provided for DescribeVcenterClients.</p>

        Raises:
            aws_sdk_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            aws_sdk_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            aws_sdk_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            aws_sdk_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mgn.types.describe_vcenter_clients_request.DescribeVcenterClientsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.describe_vcenter_clients

            output, http_response = (
                aws_sdk_mgn._operations.application_migration_service.describe_vcenter_clients.describe_vcenter_clients(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.describe_vcenter_clients_request.DescribeVcenterClientsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncVcenterClientResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def delete(
        self,
        vcenter_client_id: "aws_sdk_mgn.types.vcenter_client_id.VcenterClientID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> None:
        """<p>Deletes a given vCenter client by ID.</p>

        Args:
            vcenter_client_id: <p>ID of resource to be deleted.</p>

        Raises:
            aws_sdk_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            aws_sdk_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            aws_sdk_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            aws_sdk_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.delete_vcenter_client_request.DeleteVcenterClientRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_mgn._operations.application_migration_service.delete_vcenter_client

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.delete_vcenter_client.async_delete_vcenter_client(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.delete_vcenter_client_request.DeleteVcenterClientRequest = {}  # type: ignore[typeddict-item]
        input_["vcenter_client_id"] = vcenter_client_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mgn.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_mgn.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse":
        """<p>Returns a list of the installed vCenter clients.</p>

        Args:
            max_results: <p>Maximum results to be returned in DescribeVcenterClients.</p>
            next_token: <p>Next pagination token to be provided for DescribeVcenterClients.</p>

        Raises:
            aws_sdk_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            aws_sdk_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            aws_sdk_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            aws_sdk_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mgn.types.describe_vcenter_clients_request.DescribeVcenterClientsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse"
        ]:
            import aws_sdk_mgn._operations.application_migration_service.describe_vcenter_clients

            (
                output,
                http_response,
            ) = await aws_sdk_mgn._operations.application_migration_service.describe_vcenter_clients.async_describe_vcenter_clients(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mgn.types.describe_vcenter_clients_request.DescribeVcenterClientsRequest = {}  # type: ignore[typeddict-item]
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
