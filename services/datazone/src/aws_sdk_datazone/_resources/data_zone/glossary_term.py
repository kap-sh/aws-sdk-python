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
    import aws_sdk_datazone.types.create_glossary_term_input
    import aws_sdk_datazone.types.create_glossary_term_output
    import aws_sdk_datazone.types.delete_glossary_term_input
    import aws_sdk_datazone.types.delete_glossary_term_output
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.get_glossary_term_input
    import aws_sdk_datazone.types.get_glossary_term_output
    import aws_sdk_datazone.types.glossary_term_id
    import aws_sdk_datazone.types.glossary_term_name
    import aws_sdk_datazone.types.glossary_term_status
    import aws_sdk_datazone.types.long_description
    import aws_sdk_datazone.types.short_description
    import aws_sdk_datazone.types.term_relations
    import aws_sdk_datazone.types.update_glossary_term_input
    import aws_sdk_datazone.types.update_glossary_term_output
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )


class GlossaryTerm:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        glossary_identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId",
        name: "aws_sdk_datazone.types.glossary_term_name.GlossaryTermName",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        status: Optional[
            "aws_sdk_datazone.types.glossary_term_status.GlossaryTermStatus"
        ] = None,
        short_description: Optional[
            "aws_sdk_datazone.types.short_description.ShortDescription"
        ] = None,
        long_description: Optional[
            "aws_sdk_datazone.types.long_description.LongDescription"
        ] = None,
        term_relations: Optional[
            "aws_sdk_datazone.types.term_relations.TermRelations"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_glossary_term_output.CreateGlossaryTermOutput":
        """<p>Creates a business glossary term.</p> <p>A glossary term represents an individual entry within the Amazon DataZone glossary, serving as a standardized definition for a specific business concept or data element. Each term can include rich metadata such as detailed definitions, synonyms, related terms, and usage examples. Glossary terms can be linked directly to data assets, providing business context to technical data elements. This linking capability helps users understand the business meaning of data fields and ensures consistent interpretation across different systems and teams. Terms can also have relationships with other terms, creating a semantic network that reflects the complexity of business concepts.</p> <p>Prerequisites:</p> <ul> <li> <p>Domain must exist. </p> </li> <li> <p>Glossary must exist.</p> </li> <li> <p>The term name must be unique within the glossary.</p> </li> <li> <p>Ensure term does not conflict with existing terms in hierarchy.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary term is created.</p>
            glossary_identifier: <p>The ID of the business glossary in which this term is created.</p>
            name: <p>The name of this business glossary term.</p>
            status: <p>The status of this business glossary term.</p>
            short_description: <p>The short description of this business glossary term.</p>
            long_description: <p>The long description of this business glossary term.</p>
            term_relations: <p>The term relations of this business glossary term.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.create_glossary_term_input.CreateGlossaryTermInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.create_glossary_term_output.CreateGlossaryTermOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_glossary_term

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.create_glossary_term.create_glossary_term(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_glossary_term_input.CreateGlossaryTermInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["glossary_identifier"] = glossary_identifier
        input_["name"] = name
        if status is not None:
            input_["status"] = status
        if short_description is not None:
            input_["short_description"] = short_description
        if long_description is not None:
            input_["long_description"] = long_description
        if term_relations is not None:
            input_["term_relations"] = term_relations
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
        identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_glossary_term_output.GetGlossaryTermOutput":
        """<p>Gets a business glossary term in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Glossary term with identifier must exist in the domain. </p> </li> <li> <p>User must have permission on the glossary term.</p> </li> <li> <p>Domain must be accessible and active.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary term exists.</p>
            identifier: <p>The ID of the business glossary term.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.get_glossary_term_input.GetGlossaryTermInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_glossary_term_output.GetGlossaryTermOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_glossary_term

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_glossary_term.get_glossary_term(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_glossary_term_input.GetGlossaryTermInput = {}  # type: ignore[typeddict-item]
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
        identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        glossary_identifier: Optional[
            "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId"
        ] = None,
        name: Optional[
            "aws_sdk_datazone.types.glossary_term_name.GlossaryTermName"
        ] = None,
        short_description: Optional[
            "aws_sdk_datazone.types.short_description.ShortDescription"
        ] = None,
        long_description: Optional[
            "aws_sdk_datazone.types.long_description.LongDescription"
        ] = None,
        term_relations: Optional[
            "aws_sdk_datazone.types.term_relations.TermRelations"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.glossary_term_status.GlossaryTermStatus"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_glossary_term_output.UpdateGlossaryTermOutput":
        """<p>Updates a business glossary term in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Glossary term must exist in the specified domain. </p> </li> <li> <p>New name must not conflict with existing terms in the same glossary.</p> </li> <li> <p>User must have permissions on the term.</p> </li> <li> <p>The term must not be in DELETED status.</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a business glossary term is to be updated.</p>
            glossary_identifier: <p>The identifier of the business glossary in which a term is to be updated.</p>
            identifier: <p>The identifier of the business glossary term that is to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            short_description: <p>The short description to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            long_description: <p>The long description to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            term_relations: <p>The term relations to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            status: <p>The status to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.update_glossary_term_input.UpdateGlossaryTermInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.update_glossary_term_output.UpdateGlossaryTermOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_glossary_term

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.update_glossary_term.update_glossary_term(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_glossary_term_input.UpdateGlossaryTermInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if glossary_identifier is not None:
            input_["glossary_identifier"] = glossary_identifier
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name
        if short_description is not None:
            input_["short_description"] = short_description
        if long_description is not None:
            input_["long_description"] = long_description
        if term_relations is not None:
            input_["term_relations"] = term_relations
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_glossary_term_output.DeleteGlossaryTermOutput":
        """<p>Deletes a business glossary term in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Glossary term must exist and be active. </p> </li> <li> <p>The term must not be linked to other assets or child terms.</p> </li> <li> <p>Caller must have delete permissions in the domain/glossary.</p> </li> <li> <p>Ensure all associations (such as to assets or parent terms) are removed before deletion.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the business glossary term is deleted.</p>
            identifier: <p>The ID of the business glossary term that is deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.delete_glossary_term_input.DeleteGlossaryTermInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.delete_glossary_term_output.DeleteGlossaryTermOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_glossary_term

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.delete_glossary_term.delete_glossary_term(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_glossary_term_input.DeleteGlossaryTermInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncGlossaryTerm:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        glossary_identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId",
        name: "aws_sdk_datazone.types.glossary_term_name.GlossaryTermName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "aws_sdk_datazone.types.glossary_term_status.GlossaryTermStatus"
        ] = None,
        short_description: Optional[
            "aws_sdk_datazone.types.short_description.ShortDescription"
        ] = None,
        long_description: Optional[
            "aws_sdk_datazone.types.long_description.LongDescription"
        ] = None,
        term_relations: Optional[
            "aws_sdk_datazone.types.term_relations.TermRelations"
        ] = None,
        client_token: Optional[
            "aws_sdk_datazone.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_datazone.types.create_glossary_term_output.CreateGlossaryTermOutput":
        """<p>Creates a business glossary term.</p> <p>A glossary term represents an individual entry within the Amazon DataZone glossary, serving as a standardized definition for a specific business concept or data element. Each term can include rich metadata such as detailed definitions, synonyms, related terms, and usage examples. Glossary terms can be linked directly to data assets, providing business context to technical data elements. This linking capability helps users understand the business meaning of data fields and ensures consistent interpretation across different systems and teams. Terms can also have relationships with other terms, creating a semantic network that reflects the complexity of business concepts.</p> <p>Prerequisites:</p> <ul> <li> <p>Domain must exist. </p> </li> <li> <p>Glossary must exist.</p> </li> <li> <p>The term name must be unique within the glossary.</p> </li> <li> <p>Ensure term does not conflict with existing terms in hierarchy.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary term is created.</p>
            glossary_identifier: <p>The ID of the business glossary in which this term is created.</p>
            name: <p>The name of this business glossary term.</p>
            status: <p>The status of this business glossary term.</p>
            short_description: <p>The short description of this business glossary term.</p>
            long_description: <p>The long description of this business glossary term.</p>
            term_relations: <p>The term relations of this business glossary term.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.create_glossary_term_input.CreateGlossaryTermInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.create_glossary_term_output.CreateGlossaryTermOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.create_glossary_term

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.create_glossary_term.async_create_glossary_term(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.create_glossary_term_input.CreateGlossaryTermInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["glossary_identifier"] = glossary_identifier
        input_["name"] = name
        if status is not None:
            input_["status"] = status
        if short_description is not None:
            input_["short_description"] = short_description
        if long_description is not None:
            input_["long_description"] = long_description
        if term_relations is not None:
            input_["term_relations"] = term_relations
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
        identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.get_glossary_term_output.GetGlossaryTermOutput":
        """<p>Gets a business glossary term in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Glossary term with identifier must exist in the domain. </p> </li> <li> <p>User must have permission on the glossary term.</p> </li> <li> <p>Domain must be accessible and active.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary term exists.</p>
            identifier: <p>The ID of the business glossary term.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_glossary_term_input.GetGlossaryTermInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_glossary_term_output.GetGlossaryTermOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_glossary_term

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_glossary_term.async_get_glossary_term(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_glossary_term_input.GetGlossaryTermInput = {}  # type: ignore[typeddict-item]
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
        identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        glossary_identifier: Optional[
            "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId"
        ] = None,
        name: Optional[
            "aws_sdk_datazone.types.glossary_term_name.GlossaryTermName"
        ] = None,
        short_description: Optional[
            "aws_sdk_datazone.types.short_description.ShortDescription"
        ] = None,
        long_description: Optional[
            "aws_sdk_datazone.types.long_description.LongDescription"
        ] = None,
        term_relations: Optional[
            "aws_sdk_datazone.types.term_relations.TermRelations"
        ] = None,
        status: Optional[
            "aws_sdk_datazone.types.glossary_term_status.GlossaryTermStatus"
        ] = None,
    ) -> "aws_sdk_datazone.types.update_glossary_term_output.UpdateGlossaryTermOutput":
        """<p>Updates a business glossary term in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Glossary term must exist in the specified domain. </p> </li> <li> <p>New name must not conflict with existing terms in the same glossary.</p> </li> <li> <p>User must have permissions on the term.</p> </li> <li> <p>The term must not be in DELETED status.</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a business glossary term is to be updated.</p>
            glossary_identifier: <p>The identifier of the business glossary in which a term is to be updated.</p>
            identifier: <p>The identifier of the business glossary term that is to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            short_description: <p>The short description to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            long_description: <p>The long description to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            term_relations: <p>The term relations to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            status: <p>The status to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.update_glossary_term_input.UpdateGlossaryTermInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.update_glossary_term_output.UpdateGlossaryTermOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.update_glossary_term

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.update_glossary_term.async_update_glossary_term(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.update_glossary_term_input.UpdateGlossaryTermInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        if glossary_identifier is not None:
            input_["glossary_identifier"] = glossary_identifier
        input_["identifier"] = identifier
        if name is not None:
            input_["name"] = name
        if short_description is not None:
            input_["short_description"] = short_description
        if long_description is not None:
            input_["long_description"] = long_description
        if term_relations is not None:
            input_["term_relations"] = term_relations
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.glossary_term_id.GlossaryTermId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_glossary_term_output.DeleteGlossaryTermOutput":
        """<p>Deletes a business glossary term in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Glossary term must exist and be active. </p> </li> <li> <p>The term must not be linked to other assets or child terms.</p> </li> <li> <p>Caller must have delete permissions in the domain/glossary.</p> </li> <li> <p>Ensure all associations (such as to assets or parent terms) are removed before deletion.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the business glossary term is deleted.</p>
            identifier: <p>The ID of the business glossary term that is deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_glossary_term_input.DeleteGlossaryTermInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_glossary_term_output.DeleteGlossaryTermOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_glossary_term

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_glossary_term.async_delete_glossary_term(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_glossary_term_input.DeleteGlossaryTermInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
