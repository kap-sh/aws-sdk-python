from typing import Optional, TYPE_CHECKING
from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import ensure_async_iterator
from aws_sdk_cleanroomsml._services.clean_rooms_ml import ensure_sync_iterator
from aws_sdk_cleanroomsml._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_cleanroomsml._auth._signers
import aws_sdk_cleanroomsml._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import CleanRoomsMLClient, CleanRoomsMLClientConfig
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import AsyncCleanRoomsMLClient, AsyncCleanRoomsMLClientConfig
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list
    import aws_sdk_cleanroomsml.types.create_ml_input_channel_request
    import aws_sdk_cleanroomsml.types.create_ml_input_channel_response
    import aws_sdk_cleanroomsml.types.delete_ml_input_channel_data_request
    import aws_sdk_cleanroomsml.types.get_collaboration_ml_input_channel_request
    import aws_sdk_cleanroomsml.types.get_collaboration_ml_input_channel_response
    import aws_sdk_cleanroomsml.types.get_ml_input_channel_request
    import aws_sdk_cleanroomsml.types.get_ml_input_channel_response
    import aws_sdk_cleanroomsml.types.input_channel
    import aws_sdk_cleanroomsml.types.kms_key_arn
    import aws_sdk_cleanroomsml.types.list_ml_input_channels_request
    import aws_sdk_cleanroomsml.types.list_ml_input_channels_response
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.ml_input_channel_arn
    import aws_sdk_cleanroomsml.types.ml_input_channel_summary
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.payer_configuration
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.uuid

class MLInputChannel:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service
    def create(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", configured_model_algorithm_associations: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList", input_channel: "aws_sdk_cleanroomsml.types.input_channel.InputChannel", name: "aws_sdk_cleanroomsml.types.name_string.NameString", retention_in_days: int, *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, description: Optional["aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"] = None, kms_key_arn: Optional["aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None, tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None, payer_configuration: Optional["aws_sdk_cleanroomsml.types.payer_configuration.PayerConfiguration"] = None) -> "aws_sdk_cleanroomsml.types.create_ml_input_channel_response.CreateMLInputChannelResponse":
        """<p>Provides the information to create an ML input channel. An ML input channel is the result of a query that can be used for ML modeling.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is creating the ML input channel.</p>
            configured_model_algorithm_associations: <p>The associated configured model algorithms that are necessary to create this ML input channel.</p>
            input_channel: <p>The input data that is used to create this ML input channel.</p>
            name: <p>The name of the ML input channel.</p>
            retention_in_days: <p>The number of days that the data in the ML input channel is retained.</p>
            description: <p>The description of the ML input channel.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key that is used to access the input channel.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            payer_configuration: <p>The payer configuration for the ML input channel. Determines which member account pays for compute and synthetic data costs.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.create_ml_input_channel_response.CreateMLInputChannelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_ml_input_channel
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_ml_input_channel.create_ml_input_channel(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["configured_model_algorithm_associations"] = configured_model_algorithm_associations
        input["input_channel"] = input_channel
        input["name"] = name
        input["retention_in_days"] = retention_in_days
        if description is not None:
            input["description"] = description
        if kms_key_arn is not None:
            input["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input["tags"] = tags
        if payer_configuration is not None:
            input["payer_configuration"] = payer_configuration

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, ml_input_channel_arn: "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn", membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None) -> "aws_sdk_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse":
        """<p>Returns information about an ML input channel.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channel that you want to get.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.get_ml_input_channel_request.GetMLInputChannelRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_ml_input_channel
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_ml_input_channel.get_ml_input_channel(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_ml_input_channel_request.GetMLInputChannelRequest = {}  # type: ignore[typeddict-item]
        input["ml_input_channel_arn"] = ml_input_channel_arn
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, ml_input_channel_arn: "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn", membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None) -> None:
        """<p>Provides the information necessary to delete an ML input channel.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to delete.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channel you want to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.delete_ml_input_channel_data_request.DeleteMLInputChannelDataRequest]') -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_ml_input_channel_data
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_ml_input_channel_data.delete_ml_input_channel_data(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.delete_ml_input_channel_data_request.DeleteMLInputChannelDataRequest = {}  # type: ignore[typeddict-item]
        input["ml_input_channel_arn"] = ml_input_channel_arn
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_cleanroomsml.types.max_results.MaxResults"] = None) -> "aws_sdk_cleanroomsml.types.list_ml_input_channels_response.ListMLInputChannelsResponse":
        """<p>Returns a list of ML input channels.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum number of ML input channels to return.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channels that you want to list.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.list_ml_input_channels_request.ListMLInputChannelsRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.list_ml_input_channels_response.ListMLInputChannelsResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_ml_input_channels
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_ml_input_channels.list_ml_input_channels(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.list_ml_input_channels_request.ListMLInputChannelsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_collaboration_ml_input_channel(self, ml_input_channel_arn: "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn", collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None) -> "aws_sdk_cleanroomsml.types.get_collaboration_ml_input_channel_response.GetCollaborationMLInputChannelResponse":
        """<p>Returns information about a specific ML input channel in a collaboration.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the ML input channel that you want to get.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.get_collaboration_ml_input_channel_request.GetCollaborationMLInputChannelRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.get_collaboration_ml_input_channel_response.GetCollaborationMLInputChannelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_ml_input_channel
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_ml_input_channel.get_collaboration_ml_input_channel(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_collaboration_ml_input_channel_request.GetCollaborationMLInputChannelRequest = {}  # type: ignore[typeddict-item]
        input["ml_input_channel_arn"] = ml_input_channel_arn
        input["collaboration_identifier"] = collaboration_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncMLInputChannel:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service
    async def create(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", configured_model_algorithm_associations: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList", input_channel: "aws_sdk_cleanroomsml.types.input_channel.InputChannel", name: "aws_sdk_cleanroomsml.types.name_string.NameString", retention_in_days: int, *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, description: Optional["aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"] = None, kms_key_arn: Optional["aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None, tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None, payer_configuration: Optional["aws_sdk_cleanroomsml.types.payer_configuration.PayerConfiguration"] = None) -> "aws_sdk_cleanroomsml.types.create_ml_input_channel_response.CreateMLInputChannelResponse":
        """<p>Provides the information to create an ML input channel. An ML input channel is the result of a query that can be used for ML modeling.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is creating the ML input channel.</p>
            configured_model_algorithm_associations: <p>The associated configured model algorithms that are necessary to create this ML input channel.</p>
            input_channel: <p>The input data that is used to create this ML input channel.</p>
            name: <p>The name of the ML input channel.</p>
            retention_in_days: <p>The number of days that the data in the ML input channel is retained.</p>
            description: <p>The description of the ML input channel.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key that is used to access the input channel.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            payer_configuration: <p>The payer configuration for the ML input channel. Determines which member account pays for compute and synthetic data costs.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.create_ml_input_channel_response.CreateMLInputChannelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_ml_input_channel
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_ml_input_channel.async_create_ml_input_channel(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["configured_model_algorithm_associations"] = configured_model_algorithm_associations
        input["input_channel"] = input_channel
        input["name"] = name
        input["retention_in_days"] = retention_in_days
        if description is not None:
            input["description"] = description
        if kms_key_arn is not None:
            input["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input["tags"] = tags
        if payer_configuration is not None:
            input["payer_configuration"] = payer_configuration

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, ml_input_channel_arn: "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn", membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None) -> "aws_sdk_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse":
        """<p>Returns information about an ML input channel.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channel that you want to get.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_ml_input_channel_request.GetMLInputChannelRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_ml_input_channel
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_ml_input_channel.async_get_ml_input_channel(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_ml_input_channel_request.GetMLInputChannelRequest = {}  # type: ignore[typeddict-item]
        input["ml_input_channel_arn"] = ml_input_channel_arn
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, ml_input_channel_arn: "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn", membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None) -> None:
        """<p>Provides the information necessary to delete an ML input channel.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to delete.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channel you want to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.delete_ml_input_channel_data_request.DeleteMLInputChannelDataRequest]') -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_ml_input_channel_data
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_ml_input_channel_data.async_delete_ml_input_channel_data(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.delete_ml_input_channel_data_request.DeleteMLInputChannelDataRequest = {}  # type: ignore[typeddict-item]
        input["ml_input_channel_arn"] = ml_input_channel_arn
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_cleanroomsml.types.max_results.MaxResults"] = None) -> "aws_sdk_cleanroomsml.types.list_ml_input_channels_response.ListMLInputChannelsResponse":
        """<p>Returns a list of ML input channels.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum number of ML input channels to return.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channels that you want to list.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_ml_input_channels_request.ListMLInputChannelsRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.list_ml_input_channels_response.ListMLInputChannelsResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_ml_input_channels
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_ml_input_channels.async_list_ml_input_channels(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.list_ml_input_channels_request.ListMLInputChannelsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_collaboration_ml_input_channel(self, ml_input_channel_arn: "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn", collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None) -> "aws_sdk_cleanroomsml.types.get_collaboration_ml_input_channel_response.GetCollaborationMLInputChannelResponse":
        """<p>Returns information about a specific ML input channel in a collaboration.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the ML input channel that you want to get.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_collaboration_ml_input_channel_request.GetCollaborationMLInputChannelRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.get_collaboration_ml_input_channel_response.GetCollaborationMLInputChannelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_ml_input_channel
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_ml_input_channel.async_get_collaboration_ml_input_channel(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_collaboration_ml_input_channel_request.GetCollaborationMLInputChannelRequest = {}  # type: ignore[typeddict-item]
        input["ml_input_channel_arn"] = ml_input_channel_arn
        input["collaboration_identifier"] = collaboration_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output