from typing import TYPE_CHECKING, Optional

import aws_sdk_cleanroomsml._auth._signers
import aws_sdk_cleanroomsml._auth._sigv4
from aws_sdk_cleanroomsml._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_arn
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_summary
    import aws_sdk_cleanroomsml.types.create_configured_model_algorithm_association_request
    import aws_sdk_cleanroomsml.types.create_configured_model_algorithm_association_response
    import aws_sdk_cleanroomsml.types.delete_configured_model_algorithm_association_request
    import aws_sdk_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_request
    import aws_sdk_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_response
    import aws_sdk_cleanroomsml.types.get_configured_model_algorithm_association_request
    import aws_sdk_cleanroomsml.types.get_configured_model_algorithm_association_response
    import aws_sdk_cleanroomsml.types.list_configured_model_algorithm_associations_request
    import aws_sdk_cleanroomsml.types.list_configured_model_algorithm_associations_response
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.privacy_configuration
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.uuid
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class ConfiguredModelAlgorithmAssociation:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn",
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        privacy_configuration: Optional[
            "aws_sdk_cleanroomsml.types.privacy_configuration.PrivacyConfiguration"
        ] = None,
        tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_cleanroomsml.types.create_configured_model_algorithm_association_response.CreateConfiguredModelAlgorithmAssociationResponse":
        """<p>Associates a configured model algorithm to a collaboration for use by any member of the collaboration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member who is associating this configured model algorithm.</p>
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to associate.</p>
            name: <p>The name of the configured model algorithm association.</p>
            description: <p>The description of the configured model algorithm association.</p>
            privacy_configuration: <p>Specifies the privacy configuration information for the configured model algorithm association. This information includes the maximum data size that can be exported.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.create_configured_model_algorithm_association_request.CreateConfiguredModelAlgorithmAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.create_configured_model_algorithm_association_response.CreateConfiguredModelAlgorithmAssociationResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm_association

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm_association.create_configured_model_algorithm_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.create_configured_model_algorithm_association_request.CreateConfiguredModelAlgorithmAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["configured_model_algorithm_arn"] = configured_model_algorithm_arn
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if privacy_configuration is not None:
            input_["privacy_configuration"] = privacy_configuration
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
        configured_model_algorithm_association_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn",
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_configured_model_algorithm_association_response.GetConfiguredModelAlgorithmAssociationResponse":
        """<p>Returns information about a configured model algorithm association.</p>

        Args:
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that you want to return information about.</p>
            membership_identifier: <p>The membership ID of the member that created the configured model algorithm association.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.get_configured_model_algorithm_association_request.GetConfiguredModelAlgorithmAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.get_configured_model_algorithm_association_response.GetConfiguredModelAlgorithmAssociationResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm_association

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm_association.get_configured_model_algorithm_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_configured_model_algorithm_association_request.GetConfiguredModelAlgorithmAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["configured_model_algorithm_association_arn"] = (
            configured_model_algorithm_association_arn
        )
        input_["membership_identifier"] = membership_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        configured_model_algorithm_association_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn",
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes a configured model algorithm association.</p>

        Args:
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that you want to delete.</p>
            membership_identifier: <p>The membership ID of the member that is deleting the configured model algorithm association.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.delete_configured_model_algorithm_association_request.DeleteConfiguredModelAlgorithmAssociationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm_association

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm_association.delete_configured_model_algorithm_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.delete_configured_model_algorithm_association_request.DeleteConfiguredModelAlgorithmAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["configured_model_algorithm_association_arn"] = (
            configured_model_algorithm_association_arn
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
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_configured_model_algorithm_associations_response.ListConfiguredModelAlgorithmAssociationsResponse":
        """<p>Returns a list of configured model algorithm associations.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            membership_identifier: <p>The membership ID of the member that created the configured model algorithm associations you are interested in.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.list_configured_model_algorithm_associations_request.ListConfiguredModelAlgorithmAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.list_configured_model_algorithm_associations_response.ListConfiguredModelAlgorithmAssociationsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithm_associations

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithm_associations.list_configured_model_algorithm_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_configured_model_algorithm_associations_request.ListConfiguredModelAlgorithmAssociationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["membership_identifier"] = membership_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_collaboration_configured_model_algorithm_association(
        self,
        configured_model_algorithm_association_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn",
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_response.GetCollaborationConfiguredModelAlgorithmAssociationResponse":
        """<p>Returns information about the configured model algorithm association in a collaboration.</p>

        Args:
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that you want to return information about.</p>
            collaboration_identifier: <p>The collaboration ID for the collaboration that contains the configured model algorithm association that you want to return information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_request.GetCollaborationConfiguredModelAlgorithmAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_response.GetCollaborationConfiguredModelAlgorithmAssociationResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_configured_model_algorithm_association

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_configured_model_algorithm_association.get_collaboration_configured_model_algorithm_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_request.GetCollaborationConfiguredModelAlgorithmAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["configured_model_algorithm_association_arn"] = (
            configured_model_algorithm_association_arn
        )
        input_["collaboration_identifier"] = collaboration_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncConfiguredModelAlgorithmAssociation:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn",
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        privacy_configuration: Optional[
            "aws_sdk_cleanroomsml.types.privacy_configuration.PrivacyConfiguration"
        ] = None,
        tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_cleanroomsml.types.create_configured_model_algorithm_association_response.CreateConfiguredModelAlgorithmAssociationResponse":
        """<p>Associates a configured model algorithm to a collaboration for use by any member of the collaboration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member who is associating this configured model algorithm.</p>
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to associate.</p>
            name: <p>The name of the configured model algorithm association.</p>
            description: <p>The description of the configured model algorithm association.</p>
            privacy_configuration: <p>Specifies the privacy configuration information for the configured model algorithm association. This information includes the maximum data size that can be exported.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.create_configured_model_algorithm_association_request.CreateConfiguredModelAlgorithmAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.create_configured_model_algorithm_association_response.CreateConfiguredModelAlgorithmAssociationResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm_association.async_create_configured_model_algorithm_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.create_configured_model_algorithm_association_request.CreateConfiguredModelAlgorithmAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["configured_model_algorithm_arn"] = configured_model_algorithm_arn
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if privacy_configuration is not None:
            input_["privacy_configuration"] = privacy_configuration
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
        configured_model_algorithm_association_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn",
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_configured_model_algorithm_association_response.GetConfiguredModelAlgorithmAssociationResponse":
        """<p>Returns information about a configured model algorithm association.</p>

        Args:
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that you want to return information about.</p>
            membership_identifier: <p>The membership ID of the member that created the configured model algorithm association.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_configured_model_algorithm_association_request.GetConfiguredModelAlgorithmAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.get_configured_model_algorithm_association_response.GetConfiguredModelAlgorithmAssociationResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm_association.async_get_configured_model_algorithm_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_configured_model_algorithm_association_request.GetConfiguredModelAlgorithmAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["configured_model_algorithm_association_arn"] = (
            configured_model_algorithm_association_arn
        )
        input_["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        configured_model_algorithm_association_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn",
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes a configured model algorithm association.</p>

        Args:
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that you want to delete.</p>
            membership_identifier: <p>The membership ID of the member that is deleting the configured model algorithm association.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.delete_configured_model_algorithm_association_request.DeleteConfiguredModelAlgorithmAssociationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm_association.async_delete_configured_model_algorithm_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.delete_configured_model_algorithm_association_request.DeleteConfiguredModelAlgorithmAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["configured_model_algorithm_association_arn"] = (
            configured_model_algorithm_association_arn
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
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_configured_model_algorithm_associations_response.ListConfiguredModelAlgorithmAssociationsResponse":
        """<p>Returns a list of configured model algorithm associations.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            membership_identifier: <p>The membership ID of the member that created the configured model algorithm associations you are interested in.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_configured_model_algorithm_associations_request.ListConfiguredModelAlgorithmAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_configured_model_algorithm_associations_response.ListConfiguredModelAlgorithmAssociationsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithm_associations

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithm_associations.async_list_configured_model_algorithm_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_configured_model_algorithm_associations_request.ListConfiguredModelAlgorithmAssociationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_collaboration_configured_model_algorithm_association(
        self,
        configured_model_algorithm_association_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn",
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_response.GetCollaborationConfiguredModelAlgorithmAssociationResponse":
        """<p>Returns information about the configured model algorithm association in a collaboration.</p>

        Args:
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that you want to return information about.</p>
            collaboration_identifier: <p>The collaboration ID for the collaboration that contains the configured model algorithm association that you want to return information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_request.GetCollaborationConfiguredModelAlgorithmAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_response.GetCollaborationConfiguredModelAlgorithmAssociationResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_configured_model_algorithm_association

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_configured_model_algorithm_association.async_get_collaboration_configured_model_algorithm_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_request.GetCollaborationConfiguredModelAlgorithmAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["configured_model_algorithm_association_arn"] = (
            configured_model_algorithm_association_arn
        )
        input_["collaboration_identifier"] = collaboration_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
