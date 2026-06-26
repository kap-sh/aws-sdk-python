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
    import aws_sdk_datazone.types.create_data_product_input
    import aws_sdk_datazone.types.create_data_product_output
    import aws_sdk_datazone.types.create_data_product_revision_input
    import aws_sdk_datazone.types.create_data_product_revision_output
    import aws_sdk_datazone.types.data_product_description
    import aws_sdk_datazone.types.data_product_id
    import aws_sdk_datazone.types.data_product_items
    import aws_sdk_datazone.types.data_product_name
    import aws_sdk_datazone.types.delete_data_product_input
    import aws_sdk_datazone.types.delete_data_product_output
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.form_input_list
    import aws_sdk_datazone.types.get_data_product_input
    import aws_sdk_datazone.types.get_data_product_output
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )


class DataProduct:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.data_product_name.DataProductName",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional[
            "aws_sdk_datazone.types.data_product_description.DataProductDescription"
        ] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        forms_input: Optional[
            "aws_sdk_datazone.types.form_input_list.FormInputList"
        ] = None,
        items: Optional[
            "aws_sdk_datazone.types.data_product_items.DataProductItems"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_data_product_output.CreateDataProductOutput":
        """<p>Creates a data product.</p> <p>A data product is a comprehensive package that combines data assets with their associated metadata, documentation, and access controls. It's designed to serve specific business needs or use cases, making it easier for users to find and consume data appropriately. Data products include important information about data quality, freshness, and usage guidelines, effectively bridging the gap between data producers and consumers while ensuring proper governance.</p> <p>Prerequisites:</p> <ul> <li> <p>The domain must exist and be accessible. </p> </li> <li> <p>The owning project must be valid and active.</p> </li> <li> <p>The name must be unique within the domain (no existing data product with the same name).</p> </li> <li> <p>User must have create permissions for data products in the project.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where the data product is created.</p>
            name: <p>The name of the data product.</p>
            owning_project_identifier: <p>The ID of the owning project of the data product.</p>
            description: <p>The description of the data product.</p>
            glossary_terms: <p>The glossary terms of the data product.</p>
            forms_input: <p>The metadata forms of the data product.</p>
            items: <p>The data assets of the data product.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.create_data_product_input.CreateDataProductInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.create_data_product_output.CreateDataProductOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_data_product

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.create_data_product.create_data_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_data_product_input.CreateDataProductInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["name"] = name
        input_["owning_project_identifier"] = owning_project_identifier
        if description is not None:
            input_["description"] = description
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if forms_input is not None:
            input_["forms_input"] = forms_input
        if items is not None:
            input_["items"] = items
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
        identifier: "aws_sdk_datazone.types.data_product_id.DataProductId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
    ) -> "aws_sdk_datazone.types.get_data_product_output.GetDataProductOutput":
        """<p>Gets the data product.</p> <p>Prerequisites:</p> <ul> <li> <p>The data product ID must exist. </p> </li> <li> <p>The domain must be valid and accessible.</p> </li> <li> <p>User must have read or discovery permissions for the data product.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where the data product lives.</p>
            identifier: <p>The ID of the data product.</p>
            revision: <p>The revision of the data product.</p>

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
            req: "OperationRequest[aws_sdk_datazone.types.get_data_product_input.GetDataProductInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_data_product_output.GetDataProductOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_data_product

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_data_product.get_data_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_data_product_input.GetDataProductInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if revision is not None:
            input_["revision"] = revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.data_product_id.DataProductId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_data_product_output.DeleteDataProductOutput":
        """<p>Deletes a data product in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The data product must exist and not be deleted or archived. </p> </li> <li> <p>The user must have delete permissions for the data product.</p> </li> <li> <p>Domain and project must be active.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the data product is deleted.</p>
            identifier: <p>The identifier of the data product that is deleted.</p>

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
            req: "OperationRequest[aws_sdk_datazone.types.delete_data_product_input.DeleteDataProductInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.delete_data_product_output.DeleteDataProductOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_data_product

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.delete_data_product.delete_data_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_data_product_input.DeleteDataProductInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_data_product_revision(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.data_product_id.DataProductId",
        name: "aws_sdk_datazone.types.data_product_name.DataProductName",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional[
            "aws_sdk_datazone.types.data_product_description.DataProductDescription"
        ] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        items: Optional[
            "aws_sdk_datazone.types.data_product_items.DataProductItems"
        ] = None,
        forms_input: Optional[
            "aws_sdk_datazone.types.form_input_list.FormInputList"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_data_product_revision_output.CreateDataProductRevisionOutput":
        """<p>Creates a data product revision.</p> <p>Prerequisites:</p> <ul> <li> <p>The original data product must exist in the given domain. </p> </li> <li> <p>User must have permissions on the data product.</p> </li> <li> <p>The domain must be valid and accessible.</p> </li> <li> <p>The new revision name must comply with naming constraints (if required).</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where the data product revision is created.</p>
            identifier: <p>The ID of the data product revision.</p>
            name: <p>The name of the data product revision.</p>
            description: <p>The description of the data product revision.</p>
            glossary_terms: <p>The glossary terms of the data product revision.</p>
            items: <p>The data assets of the data product revision.</p>
            forms_input: <p>The metadata forms of the data product revision.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

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
            req: "OperationRequest[aws_sdk_datazone.types.create_data_product_revision_input.CreateDataProductRevisionInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.create_data_product_revision_output.CreateDataProductRevisionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_data_product_revision

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.create_data_product_revision.create_data_product_revision(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_data_product_revision_input.CreateDataProductRevisionInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if items is not None:
            input_["items"] = items
        if forms_input is not None:
            input_["forms_input"] = forms_input
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDataProduct:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.data_product_name.DataProductName",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[
            "aws_sdk_datazone.types.data_product_description.DataProductDescription"
        ] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        forms_input: Optional[
            "aws_sdk_datazone.types.form_input_list.FormInputList"
        ] = None,
        items: Optional[
            "aws_sdk_datazone.types.data_product_items.DataProductItems"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_data_product_output.CreateDataProductOutput":
        """<p>Creates a data product.</p> <p>A data product is a comprehensive package that combines data assets with their associated metadata, documentation, and access controls. It's designed to serve specific business needs or use cases, making it easier for users to find and consume data appropriately. Data products include important information about data quality, freshness, and usage guidelines, effectively bridging the gap between data producers and consumers while ensuring proper governance.</p> <p>Prerequisites:</p> <ul> <li> <p>The domain must exist and be accessible. </p> </li> <li> <p>The owning project must be valid and active.</p> </li> <li> <p>The name must be unique within the domain (no existing data product with the same name).</p> </li> <li> <p>User must have create permissions for data products in the project.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where the data product is created.</p>
            name: <p>The name of the data product.</p>
            owning_project_identifier: <p>The ID of the owning project of the data product.</p>
            description: <p>The description of the data product.</p>
            glossary_terms: <p>The glossary terms of the data product.</p>
            forms_input: <p>The metadata forms of the data product.</p>
            items: <p>The data assets of the data product.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            aws_sdk_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            aws_sdk_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            aws_sdk_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            aws_sdk_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            aws_sdk_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            aws_sdk_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            aws_sdk_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_data_product_input.CreateDataProductInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_data_product_output.CreateDataProductOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_data_product

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_data_product.async_create_data_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_data_product_input.CreateDataProductInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["name"] = name
        input_["owning_project_identifier"] = owning_project_identifier
        if description is not None:
            input_["description"] = description
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if forms_input is not None:
            input_["forms_input"] = forms_input
        if items is not None:
            input_["items"] = items
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
        identifier: "aws_sdk_datazone.types.data_product_id.DataProductId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
    ) -> "aws_sdk_datazone.types.get_data_product_output.GetDataProductOutput":
        """<p>Gets the data product.</p> <p>Prerequisites:</p> <ul> <li> <p>The data product ID must exist. </p> </li> <li> <p>The domain must be valid and accessible.</p> </li> <li> <p>User must have read or discovery permissions for the data product.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where the data product lives.</p>
            identifier: <p>The ID of the data product.</p>
            revision: <p>The revision of the data product.</p>

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
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_data_product_input.GetDataProductInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_data_product_output.GetDataProductOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_data_product

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_data_product.async_get_data_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_data_product_input.GetDataProductInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.data_product_id.DataProductId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_data_product_output.DeleteDataProductOutput":
        """<p>Deletes a data product in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The data product must exist and not be deleted or archived. </p> </li> <li> <p>The user must have delete permissions for the data product.</p> </li> <li> <p>Domain and project must be active.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the data product is deleted.</p>
            identifier: <p>The identifier of the data product that is deleted.</p>

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
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_data_product_input.DeleteDataProductInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_data_product_output.DeleteDataProductOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_data_product

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_data_product.async_delete_data_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_data_product_input.DeleteDataProductInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_data_product_revision(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.data_product_id.DataProductId",
        name: "aws_sdk_datazone.types.data_product_name.DataProductName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[
            "aws_sdk_datazone.types.data_product_description.DataProductDescription"
        ] = None,
        glossary_terms: Optional[
            "aws_sdk_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        items: Optional[
            "aws_sdk_datazone.types.data_product_items.DataProductItems"
        ] = None,
        forms_input: Optional[
            "aws_sdk_datazone.types.form_input_list.FormInputList"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_data_product_revision_output.CreateDataProductRevisionOutput":
        """<p>Creates a data product revision.</p> <p>Prerequisites:</p> <ul> <li> <p>The original data product must exist in the given domain. </p> </li> <li> <p>User must have permissions on the data product.</p> </li> <li> <p>The domain must be valid and accessible.</p> </li> <li> <p>The new revision name must comply with naming constraints (if required).</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where the data product revision is created.</p>
            identifier: <p>The ID of the data product revision.</p>
            name: <p>The name of the data product revision.</p>
            description: <p>The description of the data product revision.</p>
            glossary_terms: <p>The glossary terms of the data product revision.</p>
            items: <p>The data assets of the data product revision.</p>
            forms_input: <p>The metadata forms of the data product revision.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

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
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_data_product_revision_input.CreateDataProductRevisionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_data_product_revision_output.CreateDataProductRevisionOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_data_product_revision

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_data_product_revision.async_create_data_product_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_data_product_revision_input.CreateDataProductRevisionInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if items is not None:
            input_["items"] = items
        if forms_input is not None:
            input_["forms_input"] = forms_input
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
