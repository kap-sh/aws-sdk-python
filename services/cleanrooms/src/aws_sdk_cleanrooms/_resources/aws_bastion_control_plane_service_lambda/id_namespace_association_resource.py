from typing import TYPE_CHECKING, Optional

import aws_sdk_cleanrooms._auth._signers
import aws_sdk_cleanrooms._auth._sigv4
from aws_sdk_cleanrooms._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.create_id_namespace_association_input
    import aws_sdk_cleanrooms.types.create_id_namespace_association_output
    import aws_sdk_cleanrooms.types.delete_id_namespace_association_input
    import aws_sdk_cleanrooms.types.delete_id_namespace_association_output
    import aws_sdk_cleanrooms.types.generic_resource_name
    import aws_sdk_cleanrooms.types.get_id_namespace_association_input
    import aws_sdk_cleanrooms.types.get_id_namespace_association_output
    import aws_sdk_cleanrooms.types.id_mapping_config
    import aws_sdk_cleanrooms.types.id_namespace_association_identifier
    import aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config
    import aws_sdk_cleanrooms.types.id_namespace_association_summary
    import aws_sdk_cleanrooms.types.list_id_namespace_associations_input
    import aws_sdk_cleanrooms.types.list_id_namespace_associations_output
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.tag_map
    import aws_sdk_cleanrooms.types.update_id_namespace_association_input
    import aws_sdk_cleanrooms.types.update_id_namespace_association_output
    from aws_sdk_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from aws_sdk_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class IdNamespaceAssociationResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        input_reference_config: "aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config.IdNamespaceAssociationInputReferenceConfig",
        name: "aws_sdk_cleanrooms.types.generic_resource_name.GenericResourceName",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        id_mapping_config: Optional[
            "aws_sdk_cleanrooms.types.id_mapping_config.IdMappingConfig"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.create_id_namespace_association_output.CreateIdNamespaceAssociationOutput":
        """<p>Creates an ID namespace association.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association.</p>
            input_reference_config: <p>The input reference configuration needed to create the ID namespace association.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            name: <p>The name for the ID namespace association.</p>
            description: <p>The description of the ID namespace association.</p>
            id_mapping_config: <p>The configuration settings for the ID mapping table.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.create_id_namespace_association_input.CreateIdNamespaceAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.create_id_namespace_association_output.CreateIdNamespaceAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_namespace_association

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_namespace_association.create_id_namespace_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.create_id_namespace_association_input.CreateIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["input_reference_config"] = input_reference_config
        if tags is not None:
            input["tags"] = tags
        input["name"] = name
        if description is not None:
            input["description"] = description
        if id_mapping_config is not None:
            input["id_mapping_config"] = id_mapping_config

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        id_namespace_association_identifier: "aws_sdk_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_id_namespace_association_output.GetIdNamespaceAssociationOutput":
        """<p>Retrieves an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_id_namespace_association_input.GetIdNamespaceAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_id_namespace_association_output.GetIdNamespaceAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_namespace_association

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_namespace_association.get_id_namespace_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.get_id_namespace_association_input.GetIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
        input["id_namespace_association_identifier"] = (
            id_namespace_association_identifier
        )
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        id_namespace_association_identifier: "aws_sdk_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        name: Optional[
            "aws_sdk_cleanrooms.types.generic_resource_name.GenericResourceName"
        ] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        id_mapping_config: Optional[
            "aws_sdk_cleanrooms.types.id_mapping_config.IdMappingConfig"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.update_id_namespace_association_output.UpdateIdNamespaceAssociationOutput":
        """<p>Provides the details that are necessary to update an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to update.</p>
            name: <p>A new name for the ID namespace association.</p>
            description: <p>A new description for the ID namespace association.</p>
            id_mapping_config: <p>The configuration settings for the ID mapping table.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.update_id_namespace_association_input.UpdateIdNamespaceAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.update_id_namespace_association_output.UpdateIdNamespaceAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_namespace_association

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_namespace_association.update_id_namespace_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.update_id_namespace_association_input.UpdateIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
        input["id_namespace_association_identifier"] = (
            id_namespace_association_identifier
        )
        input["membership_identifier"] = membership_identifier
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if id_mapping_config is not None:
            input["id_mapping_config"] = id_mapping_config

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        id_namespace_association_identifier: "aws_sdk_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_id_namespace_association_output.DeleteIdNamespaceAssociationOutput":
        """<p>Deletes an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to delete.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.delete_id_namespace_association_input.DeleteIdNamespaceAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.delete_id_namespace_association_output.DeleteIdNamespaceAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_namespace_association

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_namespace_association.delete_id_namespace_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.delete_id_namespace_association_input.DeleteIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
        input["id_namespace_association_identifier"] = (
            id_namespace_association_identifier
        )
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_id_namespace_associations_output.ListIdNamespaceAssociationsOutput":
        """<p>Returns a list of ID namespace associations.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to view.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_id_namespace_associations_input.ListIdNamespaceAssociationsInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_id_namespace_associations_output.ListIdNamespaceAssociationsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_namespace_associations

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_namespace_associations.list_id_namespace_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.list_id_namespace_associations_input.ListIdNamespaceAssociationsInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncIdNamespaceAssociationResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        input_reference_config: "aws_sdk_cleanrooms.types.id_namespace_association_input_reference_config.IdNamespaceAssociationInputReferenceConfig",
        name: "aws_sdk_cleanrooms.types.generic_resource_name.GenericResourceName",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        id_mapping_config: Optional[
            "aws_sdk_cleanrooms.types.id_mapping_config.IdMappingConfig"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.create_id_namespace_association_output.CreateIdNamespaceAssociationOutput":
        """<p>Creates an ID namespace association.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association.</p>
            input_reference_config: <p>The input reference configuration needed to create the ID namespace association.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            name: <p>The name for the ID namespace association.</p>
            description: <p>The description of the ID namespace association.</p>
            id_mapping_config: <p>The configuration settings for the ID mapping table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.create_id_namespace_association_input.CreateIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.create_id_namespace_association_output.CreateIdNamespaceAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_namespace_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_id_namespace_association.async_create_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.create_id_namespace_association_input.CreateIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["input_reference_config"] = input_reference_config
        if tags is not None:
            input["tags"] = tags
        input["name"] = name
        if description is not None:
            input["description"] = description
        if id_mapping_config is not None:
            input["id_mapping_config"] = id_mapping_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        id_namespace_association_identifier: "aws_sdk_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_id_namespace_association_output.GetIdNamespaceAssociationOutput":
        """<p>Retrieves an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to retrieve.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_id_namespace_association_input.GetIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_id_namespace_association_output.GetIdNamespaceAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_namespace_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_id_namespace_association.async_get_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.get_id_namespace_association_input.GetIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
        input["id_namespace_association_identifier"] = (
            id_namespace_association_identifier
        )
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        id_namespace_association_identifier: "aws_sdk_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        name: Optional[
            "aws_sdk_cleanrooms.types.generic_resource_name.GenericResourceName"
        ] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        id_mapping_config: Optional[
            "aws_sdk_cleanrooms.types.id_mapping_config.IdMappingConfig"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.update_id_namespace_association_output.UpdateIdNamespaceAssociationOutput":
        """<p>Provides the details that are necessary to update an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to update.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to update.</p>
            name: <p>A new name for the ID namespace association.</p>
            description: <p>A new description for the ID namespace association.</p>
            id_mapping_config: <p>The configuration settings for the ID mapping table.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.update_id_namespace_association_input.UpdateIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.update_id_namespace_association_output.UpdateIdNamespaceAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_namespace_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_id_namespace_association.async_update_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.update_id_namespace_association_input.UpdateIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
        input["id_namespace_association_identifier"] = (
            id_namespace_association_identifier
        )
        input["membership_identifier"] = membership_identifier
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if id_mapping_config is not None:
            input["id_mapping_config"] = id_mapping_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        id_namespace_association_identifier: "aws_sdk_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_id_namespace_association_output.DeleteIdNamespaceAssociationOutput":
        """<p>Deletes an ID namespace association.</p>

        Args:
            id_namespace_association_identifier: <p>The unique identifier of the ID namespace association that you want to delete.</p>
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.delete_id_namespace_association_input.DeleteIdNamespaceAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.delete_id_namespace_association_output.DeleteIdNamespaceAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_namespace_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_id_namespace_association.async_delete_id_namespace_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.delete_id_namespace_association_input.DeleteIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
        input["id_namespace_association_identifier"] = (
            id_namespace_association_identifier
        )
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cleanrooms.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_cleanrooms.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_cleanrooms.types.list_id_namespace_associations_output.ListIdNamespaceAssociationsOutput":
        """<p>Returns a list of ID namespace associations.</p>

        Args:
            membership_identifier: <p>The unique identifier of the membership that contains the ID namespace association that you want to view.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum size of the results that is returned per call. Service chooses a default if it has not been set. Service may return a nextToken even if the maximum results has not been met.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_id_namespace_associations_input.ListIdNamespaceAssociationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_id_namespace_associations_output.ListIdNamespaceAssociationsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_namespace_associations

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_id_namespace_associations.async_list_id_namespace_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanrooms.types.list_id_namespace_associations_input.ListIdNamespaceAssociationsInput = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
