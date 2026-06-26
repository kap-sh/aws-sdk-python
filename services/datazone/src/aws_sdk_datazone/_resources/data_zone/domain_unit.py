from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4
from aws_sdk_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.create_domain_unit_input
    import aws_sdk_datazone.types.create_domain_unit_output
    import aws_sdk_datazone.types.delete_domain_unit_input
    import aws_sdk_datazone.types.delete_domain_unit_output
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_description
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.domain_unit_name
    import aws_sdk_datazone.types.domain_unit_summary
    import aws_sdk_datazone.types.get_domain_unit_input
    import aws_sdk_datazone.types.get_domain_unit_output
    import aws_sdk_datazone.types.list_domain_units_for_parent_input
    import aws_sdk_datazone.types.list_domain_units_for_parent_output
    import aws_sdk_datazone.types.max_results_for_list_domains
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.update_domain_unit_input
    import aws_sdk_datazone.types.update_domain_unit_output
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )


class DomainUnit:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.domain_unit_name.DomainUnitName",
        parent_domain_unit_identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional[
            "aws_sdk_datazone.types.domain_unit_description.DomainUnitDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_domain_unit_output.CreateDomainUnitOutput":
        """<p>Creates a domain unit in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to crate a domain unit.</p>
            name: <p>The name of the domain unit.</p>
            parent_domain_unit_identifier: <p>The ID of the parent domain unit.</p>
            description: <p>The description of the domain unit.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.create_domain_unit_input.CreateDomainUnitInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.create_domain_unit_output.CreateDomainUnitOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_domain_unit

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.create_domain_unit.create_domain_unit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_domain_unit_input.CreateDomainUnitInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["name"] = name
        input_["parent_domain_unit_identifier"] = parent_domain_unit_identifier
        if description is not None:
            input_["description"] = description
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_domain_unit_output.GetDomainUnitOutput":
        """<p>Gets the details of the specified domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to get a domain unit.</p>
            identifier: <p>The identifier of the domain unit that you want to get.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.get_domain_unit_input.GetDomainUnitInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_domain_unit_output.GetDomainUnitOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_domain_unit

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_domain_unit.get_domain_unit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_domain_unit_input.GetDomainUnitInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional[
            "aws_sdk_datazone.types.domain_unit_description.DomainUnitDescription"
        ] = None,
        name: Optional["aws_sdk_datazone.types.domain_unit_name.DomainUnitName"] = None,
    ) -> "aws_sdk_datazone.types.update_domain_unit_output.UpdateDomainUnitOutput":
        """<p>Updates the domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to update a domain unit.</p>
            identifier: <p>The ID of the domain unit that you want to update.</p>
            description: <p>The description of the domain unit that you want to update.</p>
            name: <p>The name of the domain unit that you want to update.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.update_domain_unit_input.UpdateDomainUnitInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.update_domain_unit_output.UpdateDomainUnitOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_domain_unit

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.update_domain_unit.update_domain_unit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_domain_unit_input.UpdateDomainUnitInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_domain_unit_output.DeleteDomainUnitOutput":
        """<p>Deletes a domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to delete a domain unit.</p>
            identifier: <p>The ID of the domain unit that you want to delete.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.delete_domain_unit_input.DeleteDomainUnitInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.delete_domain_unit_output.DeleteDomainUnitOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_domain_unit

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.delete_domain_unit.delete_domain_unit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_domain_unit_input.DeleteDomainUnitInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        parent_domain_unit_identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        max_results: Optional[
            "aws_sdk_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_domain_units_for_parent_output.ListDomainUnitsForParentOutput":
        """<p>Lists child domain units for the specified parent domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which you want to list domain units for a parent domain unit.</p>
            parent_domain_unit_identifier: <p>The ID of the parent domain unit.</p>
            max_results: <p>The maximum number of domain units to return in a single call to ListDomainUnitsForParent. When the number of domain units to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.</p>
            next_token: <p>When the number of domain units is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of domain units, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.list_domain_units_for_parent_input.ListDomainUnitsForParentInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.list_domain_units_for_parent_output.ListDomainUnitsForParentOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_domain_units_for_parent

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.list_domain_units_for_parent.list_domain_units_for_parent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_domain_units_for_parent_input.ListDomainUnitsForParentInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["parent_domain_unit_identifier"] = parent_domain_unit_identifier
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


class AsyncDomainUnit:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.domain_unit_name.DomainUnitName",
        parent_domain_unit_identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[
            "aws_sdk_datazone.types.domain_unit_description.DomainUnitDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_domain_unit_output.CreateDomainUnitOutput":
        """<p>Creates a domain unit in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to crate a domain unit.</p>
            name: <p>The name of the domain unit.</p>
            parent_domain_unit_identifier: <p>The ID of the parent domain unit.</p>
            description: <p>The description of the domain unit.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_domain_unit_input.CreateDomainUnitInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_domain_unit_output.CreateDomainUnitOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_domain_unit

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_domain_unit.async_create_domain_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_domain_unit_input.CreateDomainUnitInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["name"] = name
        input_["parent_domain_unit_identifier"] = parent_domain_unit_identifier
        if description is not None:
            input_["description"] = description
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_domain_unit_output.GetDomainUnitOutput":
        """<p>Gets the details of the specified domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to get a domain unit.</p>
            identifier: <p>The identifier of the domain unit that you want to get.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_domain_unit_input.GetDomainUnitInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_domain_unit_output.GetDomainUnitOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_domain_unit

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_domain_unit.async_get_domain_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_domain_unit_input.GetDomainUnitInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[
            "aws_sdk_datazone.types.domain_unit_description.DomainUnitDescription"
        ] = None,
        name: Optional["aws_sdk_datazone.types.domain_unit_name.DomainUnitName"] = None,
    ) -> "aws_sdk_datazone.types.update_domain_unit_output.UpdateDomainUnitOutput":
        """<p>Updates the domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to update a domain unit.</p>
            identifier: <p>The ID of the domain unit that you want to update.</p>
            description: <p>The description of the domain unit that you want to update.</p>
            name: <p>The name of the domain unit that you want to update.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_domain_unit_input.UpdateDomainUnitInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_domain_unit_output.UpdateDomainUnitOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_domain_unit

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_domain_unit.async_update_domain_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_domain_unit_input.UpdateDomainUnitInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_domain_unit_output.DeleteDomainUnitOutput":
        """<p>Deletes a domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to delete a domain unit.</p>
            identifier: <p>The ID of the domain unit that you want to delete.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_domain_unit_input.DeleteDomainUnitInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_domain_unit_output.DeleteDomainUnitOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_domain_unit

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_domain_unit.async_delete_domain_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_domain_unit_input.DeleteDomainUnitInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        parent_domain_unit_identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional[
            "aws_sdk_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "aws_sdk_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.list_domain_units_for_parent_output.ListDomainUnitsForParentOutput":
        """<p>Lists child domain units for the specified parent domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which you want to list domain units for a parent domain unit.</p>
            parent_domain_unit_identifier: <p>The ID of the parent domain unit.</p>
            max_results: <p>The maximum number of domain units to return in a single call to ListDomainUnitsForParent. When the number of domain units to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.</p>
            next_token: <p>When the number of domain units is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of domain units, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.list_domain_units_for_parent_input.ListDomainUnitsForParentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.list_domain_units_for_parent_output.ListDomainUnitsForParentOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.list_domain_units_for_parent

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.list_domain_units_for_parent.async_list_domain_units_for_parent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.list_domain_units_for_parent_input.ListDomainUnitsForParentInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["parent_domain_unit_identifier"] = parent_domain_unit_identifier
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
