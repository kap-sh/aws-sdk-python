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
    import aws_sdk_cleanrooms.types.configured_audience_model_arn
    import aws_sdk_cleanrooms.types.configured_audience_model_association_identifier
    import aws_sdk_cleanrooms.types.configured_audience_model_association_name
    import aws_sdk_cleanrooms.types.configured_audience_model_association_summary
    import aws_sdk_cleanrooms.types.create_configured_audience_model_association_input
    import aws_sdk_cleanrooms.types.create_configured_audience_model_association_output
    import aws_sdk_cleanrooms.types.delete_configured_audience_model_association_input
    import aws_sdk_cleanrooms.types.delete_configured_audience_model_association_output
    import aws_sdk_cleanrooms.types.get_configured_audience_model_association_input
    import aws_sdk_cleanrooms.types.get_configured_audience_model_association_output
    import aws_sdk_cleanrooms.types.list_configured_audience_model_associations_input
    import aws_sdk_cleanrooms.types.list_configured_audience_model_associations_output
    import aws_sdk_cleanrooms.types.max_results
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.pagination_token
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.tag_map
    import aws_sdk_cleanrooms.types.update_configured_audience_model_association_input
    import aws_sdk_cleanrooms.types.update_configured_audience_model_association_output
    from aws_sdk_cleanrooms._services.async_clean_rooms import (
        AsyncCleanRoomsClient,
        AsyncCleanRoomsClientConfig,
    )
    from aws_sdk_cleanrooms._services.clean_rooms import (
        CleanRoomsClient,
        CleanRoomsClientConfig,
    )


class ConfiguredAudienceModelAssociationResource:
    def __init__(self, service: CleanRoomsClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_audience_model_arn: "aws_sdk_cleanrooms.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        configured_audience_model_association_name: "aws_sdk_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName",
        manage_resource_policies: bool,
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.create_configured_audience_model_association_output.CreateConfiguredAudienceModelAssociationOutput":
        """<p>Provides the details necessary to create a configured audience model association.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The configured audience model is associated to the collaboration that this membership belongs to. Accepts a membership ID.</p>
            configured_audience_model_arn: <p>A unique identifier for the configured audience model that you want to associate.</p>
            configured_audience_model_association_name: <p>The name of the configured audience model association.</p>
            manage_resource_policies: <p>When <code>TRUE</code>, indicates that the resource policy for the configured audience model resource being associated is configured for Clean Rooms to manage permissions related to the given collaboration. When <code>FALSE</code>, indicates that the configured audience model resource owner will manage permissions related to the given collaboration.</p> <p>Setting this to <code>TRUE</code> requires you to have permissions to create, update, and delete the resource policy for the <code>cleanrooms-ml</code> resource when you call the <a>DeleteConfiguredAudienceModelAssociation</a> resource. In addition, if you are the collaboration creator and specify <code>TRUE</code>, you must have the same permissions when you call the <a>DeleteMember</a> and <a>DeleteCollaboration</a> APIs.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            description: <p>A description of the configured audience model association.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.create_configured_audience_model_association_input.CreateConfiguredAudienceModelAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.create_configured_audience_model_association_output.CreateConfiguredAudienceModelAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_audience_model_association

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_audience_model_association.create_configured_audience_model_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_configured_audience_model_association_input.CreateConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["configured_audience_model_arn"] = configured_audience_model_arn
        input_["configured_audience_model_association_name"] = (
            configured_audience_model_association_name
        )
        input_["manage_resource_policies"] = manage_resource_policies
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        configured_audience_model_association_identifier: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_configured_audience_model_association_output.GetConfiguredAudienceModelAssociationOutput":
        """<p>Returns information about a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to retrieve.</p>
            membership_identifier: <p>A unique identifier for the membership that contains the configured audience model association that you want to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.get_configured_audience_model_association_input.GetConfiguredAudienceModelAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.get_configured_audience_model_association_output.GetConfiguredAudienceModelAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_audience_model_association

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_audience_model_association.get_configured_audience_model_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_configured_audience_model_association_input.GetConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
        input_["configured_audience_model_association_identifier"] = (
            configured_audience_model_association_identifier
        )
        input_["membership_identifier"] = membership_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        configured_audience_model_association_identifier: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        name: Optional[
            "aws_sdk_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.update_configured_audience_model_association_output.UpdateConfiguredAudienceModelAssociationOutput":
        """<p>Provides the details necessary to update a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to update.</p>
            membership_identifier: <p>A unique identifier of the membership that contains the configured audience model association that you want to update.</p>
            description: <p>A new description for the configured audience model association.</p>
            name: <p>A new name for the configured audience model association.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.update_configured_audience_model_association_input.UpdateConfiguredAudienceModelAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.update_configured_audience_model_association_output.UpdateConfiguredAudienceModelAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_audience_model_association

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_audience_model_association.update_configured_audience_model_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_configured_audience_model_association_input.UpdateConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
        input_["configured_audience_model_association_identifier"] = (
            configured_audience_model_association_identifier
        )
        input_["membership_identifier"] = membership_identifier
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
        configured_audience_model_association_identifier: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_configured_audience_model_association_output.DeleteConfiguredAudienceModelAssociationOutput":
        """<p>Provides the information necessary to delete a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier of the configured audience model association that you want to delete.</p>
            membership_identifier: <p>A unique identifier of the membership that contains the audience model association that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.delete_configured_audience_model_association_input.DeleteConfiguredAudienceModelAssociationInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.delete_configured_audience_model_association_output.DeleteConfiguredAudienceModelAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_audience_model_association

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_audience_model_association.delete_configured_audience_model_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_configured_audience_model_association_input.DeleteConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
        input_["configured_audience_model_association_identifier"] = (
            configured_audience_model_association_identifier
        )
        input_["membership_identifier"] = membership_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
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
    ) -> "aws_sdk_cleanrooms.types.list_configured_audience_model_associations_output.ListConfiguredAudienceModelAssociationsOutput":
        """<p>Lists information about requested configured audience model associations.</p>

        Args:
            membership_identifier: <p>A unique identifier for a membership that contains the configured audience model associations that you want to retrieve.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_configured_audience_model_associations_input.ListConfiguredAudienceModelAssociationsInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_configured_audience_model_associations_output.ListConfiguredAudienceModelAssociationsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_audience_model_associations

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_audience_model_associations.list_configured_audience_model_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_configured_audience_model_associations_input.ListConfiguredAudienceModelAssociationsInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncConfiguredAudienceModelAssociationResource:
    def __init__(self, service: AsyncCleanRoomsClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        configured_audience_model_arn: "aws_sdk_cleanrooms.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        configured_audience_model_association_name: "aws_sdk_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName",
        manage_resource_policies: bool,
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        tags: Optional["aws_sdk_cleanrooms.types.tag_map.TagMap"] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.create_configured_audience_model_association_output.CreateConfiguredAudienceModelAssociationOutput":
        """<p>Provides the details necessary to create a configured audience model association.</p>

        Args:
            membership_identifier: <p>A unique identifier for one of your memberships for a collaboration. The configured audience model is associated to the collaboration that this membership belongs to. Accepts a membership ID.</p>
            configured_audience_model_arn: <p>A unique identifier for the configured audience model that you want to associate.</p>
            configured_audience_model_association_name: <p>The name of the configured audience model association.</p>
            manage_resource_policies: <p>When <code>TRUE</code>, indicates that the resource policy for the configured audience model resource being associated is configured for Clean Rooms to manage permissions related to the given collaboration. When <code>FALSE</code>, indicates that the configured audience model resource owner will manage permissions related to the given collaboration.</p> <p>Setting this to <code>TRUE</code> requires you to have permissions to create, update, and delete the resource policy for the <code>cleanrooms-ml</code> resource when you call the <a>DeleteConfiguredAudienceModelAssociation</a> resource. In addition, if you are the collaboration creator and specify <code>TRUE</code>, you must have the same permissions when you call the <a>DeleteMember</a> and <a>DeleteCollaboration</a> APIs.</p>
            tags: <p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>
            description: <p>A description of the configured audience model association.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.create_configured_audience_model_association_input.CreateConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.create_configured_audience_model_association_output.CreateConfiguredAudienceModelAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_audience_model_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.create_configured_audience_model_association.async_create_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.create_configured_audience_model_association_input.CreateConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["configured_audience_model_arn"] = configured_audience_model_arn
        input_["configured_audience_model_association_name"] = (
            configured_audience_model_association_name
        )
        input_["manage_resource_policies"] = manage_resource_policies
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        configured_audience_model_association_identifier: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.get_configured_audience_model_association_output.GetConfiguredAudienceModelAssociationOutput":
        """<p>Returns information about a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to retrieve.</p>
            membership_identifier: <p>A unique identifier for the membership that contains the configured audience model association that you want to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.get_configured_audience_model_association_input.GetConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.get_configured_audience_model_association_output.GetConfiguredAudienceModelAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_audience_model_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.get_configured_audience_model_association.async_get_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.get_configured_audience_model_association_input.GetConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
        input_["configured_audience_model_association_identifier"] = (
            configured_audience_model_association_identifier
        )
        input_["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        configured_audience_model_association_identifier: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
        ] = None,
        name: Optional[
            "aws_sdk_cleanrooms.types.configured_audience_model_association_name.ConfiguredAudienceModelAssociationName"
        ] = None,
    ) -> "aws_sdk_cleanrooms.types.update_configured_audience_model_association_output.UpdateConfiguredAudienceModelAssociationOutput":
        """<p>Provides the details necessary to update a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier for the configured audience model association that you want to update.</p>
            membership_identifier: <p>A unique identifier of the membership that contains the configured audience model association that you want to update.</p>
            description: <p>A new description for the configured audience model association.</p>
            name: <p>A new name for the configured audience model association.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.update_configured_audience_model_association_input.UpdateConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.update_configured_audience_model_association_output.UpdateConfiguredAudienceModelAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_audience_model_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.update_configured_audience_model_association.async_update_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.update_configured_audience_model_association_input.UpdateConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
        input_["configured_audience_model_association_identifier"] = (
            configured_audience_model_association_identifier
        )
        input_["membership_identifier"] = membership_identifier
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
        configured_audience_model_association_identifier: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier",
        membership_identifier: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier",
        *,
        config_overrides: Optional[AsyncCleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.delete_configured_audience_model_association_output.DeleteConfiguredAudienceModelAssociationOutput":
        """<p>Provides the information necessary to delete a configured audience model association.</p>

        Args:
            configured_audience_model_association_identifier: <p>A unique identifier of the configured audience model association that you want to delete.</p>
            membership_identifier: <p>A unique identifier of the membership that contains the audience model association that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.delete_configured_audience_model_association_input.DeleteConfiguredAudienceModelAssociationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.delete_configured_audience_model_association_output.DeleteConfiguredAudienceModelAssociationOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_audience_model_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.delete_configured_audience_model_association.async_delete_configured_audience_model_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.delete_configured_audience_model_association_input.DeleteConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
        input_["configured_audience_model_association_identifier"] = (
            configured_audience_model_association_identifier
        )
        input_["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
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
    ) -> "aws_sdk_cleanrooms.types.list_configured_audience_model_associations_output.ListConfiguredAudienceModelAssociationsOutput":
        """<p>Lists information about requested configured audience model associations.</p>

        Args:
            membership_identifier: <p>A unique identifier for a membership that contains the configured audience model associations that you want to retrieve.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanrooms.types.list_configured_audience_model_associations_input.ListConfiguredAudienceModelAssociationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanrooms.types.list_configured_audience_model_associations_output.ListConfiguredAudienceModelAssociationsOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_audience_model_associations

            (
                output,
                http_response,
            ) = await aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_configured_audience_model_associations.async_list_configured_audience_model_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_configured_audience_model_associations_input.ListConfiguredAudienceModelAssociationsInput = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
