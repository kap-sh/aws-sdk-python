from typing import Optional, TYPE_CHECKING
from aws_sdk_datazone._services.async_data_zone import ensure_async_iterator
from aws_sdk_datazone._services.data_zone import ensure_sync_iterator
from aws_sdk_datazone._services._pipeline import (
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
)
import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4

if TYPE_CHECKING:
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.create_glossary_input
    import aws_sdk_datazone.types.create_glossary_output
    import aws_sdk_datazone.types.delete_glossary_input
    import aws_sdk_datazone.types.delete_glossary_output
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.get_glossary_input
    import aws_sdk_datazone.types.get_glossary_output
    import aws_sdk_datazone.types.glossary_description
    import aws_sdk_datazone.types.glossary_id
    import aws_sdk_datazone.types.glossary_name
    import aws_sdk_datazone.types.glossary_status
    import aws_sdk_datazone.types.glossary_usage_restrictions
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.update_glossary_input
    import aws_sdk_datazone.types.update_glossary_output


class Glossary:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.glossary_name.GlossaryName",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional[
            "aws_sdk_datazone.types.glossary_description.GlossaryDescription"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.glossary_status.GlossaryStatus"
        ] = None,
        usage_restrictions: Optional[
            "aws_sdk_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_glossary_output.CreateGlossaryOutput":
        """<p>Creates an Amazon DataZone business glossary.</p> <p>Specifies that this is a create glossary policy.</p> <p>A glossary serves as the central repository for business terminology and definitions within an organization. It helps establish and maintain a common language across different departments and teams, reducing miscommunication and ensuring consistent interpretation of business concepts. Glossaries can include hierarchical relationships between terms, cross-references, and links to actual data assets, making them invaluable for both business users and technical teams trying to understand and use data correctly.</p> <p>Prerequisites:</p> <ul> <li> <p>Domain must exist and be in an active state. </p> </li> <li> <p>Owning project must exist and be accessible by the caller.</p> </li> <li> <p>The glossary name must be unique within the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary is created.</p>
            name: <p>The name of this business glossary.</p>
            owning_project_identifier: <p>The ID of the project that currently owns business glossary.</p>
            description: <p>The description of this business glossary.</p>
            status: <p>The status of this business glossary.</p>
            usage_restrictions: <p>The usage restriction of the restricted glossary.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.create_glossary_input.CreateGlossaryInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.create_glossary_output.CreateGlossaryOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_glossary

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.create_glossary.create_glossary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.create_glossary_input.CreateGlossaryInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["name"] = name
        input["owning_project_identifier"] = owning_project_identifier
        if description is not None:
            input["description"] = description
        if status is not None:
            input["status"] = status
        if usage_restrictions is not None:
            input["usage_restrictions"] = usage_restrictions
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_glossary_output.GetGlossaryOutput":
        """<p>Gets a business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The specified glossary ID must exist and be associated with the given domain. </p> </li> <li> <p>The caller must have the <code>datazone:GetGlossary</code> permission on the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary exists.</p>
            identifier: <p>The ID of the business glossary.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.get_glossary_input.GetGlossaryInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_glossary_output.GetGlossaryOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_glossary

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_glossary.get_glossary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.get_glossary_input.GetGlossaryInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        name: Optional["aws_sdk_datazone.types.glossary_name.GlossaryName"] = None,
        description: Optional[
            "aws_sdk_datazone.types.glossary_description.GlossaryDescription"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.glossary_status.GlossaryStatus"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_glossary_output.UpdateGlossaryOutput":
        """<p>Updates the business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The glossary must exist in the given domain. </p> </li> <li> <p>The caller must have the <code>datazone:UpdateGlossary</code> permission to update it.</p> </li> <li> <p>When updating the name, the new name must be unique within the domain.</p> </li> <li> <p>The glossary must not be deleted or in a terminal state.</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a business glossary is to be updated.</p>
            identifier: <p>The identifier of the business glossary to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateGlossary</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateGlossary</code> action.</p>
            status: <p>The status to be updated as part of the <code>UpdateGlossary</code> action.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.update_glossary_input.UpdateGlossaryInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.update_glossary_output.UpdateGlossaryOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_glossary

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.update_glossary.update_glossary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.update_glossary_input.UpdateGlossaryInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if status is not None:
            input["status"] = status
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_glossary_output.DeleteGlossaryOutput":
        """<p>Deletes a business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The glossary must be in DISABLED state. </p> </li> <li> <p>The glossary must not have any glossary terms associated with it.</p> </li> <li> <p>The glossary must exist in the specified domain.</p> </li> <li> <p>The caller must have the <code>datazone:DeleteGlossary</code> permission in the domain and glossary.</p> </li> <li> <p>Glossary should not be linked to any active metadata forms.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the business glossary is deleted.</p>
            identifier: <p>The ID of the business glossary that is deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.delete_glossary_input.DeleteGlossaryInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.delete_glossary_output.DeleteGlossaryOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_glossary

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.delete_glossary.delete_glossary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.delete_glossary_input.DeleteGlossaryInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncGlossary:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        name: "aws_sdk_datazone.types.glossary_name.GlossaryName",
        owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[
            "aws_sdk_datazone.types.glossary_description.GlossaryDescription"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.glossary_status.GlossaryStatus"
        ] = None,
        usage_restrictions: Optional[
            "aws_sdk_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_glossary_output.CreateGlossaryOutput":
        """<p>Creates an Amazon DataZone business glossary.</p> <p>Specifies that this is a create glossary policy.</p> <p>A glossary serves as the central repository for business terminology and definitions within an organization. It helps establish and maintain a common language across different departments and teams, reducing miscommunication and ensuring consistent interpretation of business concepts. Glossaries can include hierarchical relationships between terms, cross-references, and links to actual data assets, making them invaluable for both business users and technical teams trying to understand and use data correctly.</p> <p>Prerequisites:</p> <ul> <li> <p>Domain must exist and be in an active state. </p> </li> <li> <p>Owning project must exist and be accessible by the caller.</p> </li> <li> <p>The glossary name must be unique within the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary is created.</p>
            name: <p>The name of this business glossary.</p>
            owning_project_identifier: <p>The ID of the project that currently owns business glossary.</p>
            description: <p>The description of this business glossary.</p>
            status: <p>The status of this business glossary.</p>
            usage_restrictions: <p>The usage restriction of the restricted glossary.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_glossary_input.CreateGlossaryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_glossary_output.CreateGlossaryOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_glossary

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_glossary.async_create_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.create_glossary_input.CreateGlossaryInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["name"] = name
        input["owning_project_identifier"] = owning_project_identifier
        if description is not None:
            input["description"] = description
        if status is not None:
            input["status"] = status
        if usage_restrictions is not None:
            input["usage_restrictions"] = usage_restrictions
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_glossary_output.GetGlossaryOutput":
        """<p>Gets a business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The specified glossary ID must exist and be associated with the given domain. </p> </li> <li> <p>The caller must have the <code>datazone:GetGlossary</code> permission on the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary exists.</p>
            identifier: <p>The ID of the business glossary.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_glossary_input.GetGlossaryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_glossary_output.GetGlossaryOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_glossary

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_glossary.async_get_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.get_glossary_input.GetGlossaryInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["aws_sdk_datazone.types.glossary_name.GlossaryName"] = None,
        description: Optional[
            "aws_sdk_datazone.types.glossary_description.GlossaryDescription"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.glossary_status.GlossaryStatus"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_glossary_output.UpdateGlossaryOutput":
        """<p>Updates the business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The glossary must exist in the given domain. </p> </li> <li> <p>The caller must have the <code>datazone:UpdateGlossary</code> permission to update it.</p> </li> <li> <p>When updating the name, the new name must be unique within the domain.</p> </li> <li> <p>The glossary must not be deleted or in a terminal state.</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a business glossary is to be updated.</p>
            identifier: <p>The identifier of the business glossary to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateGlossary</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateGlossary</code> action.</p>
            status: <p>The status to be updated as part of the <code>UpdateGlossary</code> action.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_glossary_input.UpdateGlossaryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_glossary_output.UpdateGlossaryOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_glossary

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_glossary.async_update_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.update_glossary_input.UpdateGlossaryInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if status is not None:
            input["status"] = status
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_glossary_output.DeleteGlossaryOutput":
        """<p>Deletes a business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The glossary must be in DISABLED state. </p> </li> <li> <p>The glossary must not have any glossary terms associated with it.</p> </li> <li> <p>The glossary must exist in the specified domain.</p> </li> <li> <p>The caller must have the <code>datazone:DeleteGlossary</code> permission in the domain and glossary.</p> </li> <li> <p>Glossary should not be linked to any active metadata forms.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the business glossary is deleted.</p>
            identifier: <p>The ID of the business glossary that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_glossary_input.DeleteGlossaryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_glossary_output.DeleteGlossaryOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_glossary

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_glossary.async_delete_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_datazone.types.delete_glossary_input.DeleteGlossaryInput = {}  # type: ignore[typeddict-item]
        input["domain_identifier"] = domain_identifier
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
