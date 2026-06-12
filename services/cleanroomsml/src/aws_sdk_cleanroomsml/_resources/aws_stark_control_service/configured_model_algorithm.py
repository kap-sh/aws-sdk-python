from typing import Optional, TYPE_CHECKING
from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import ensure_async_iterator
from aws_sdk_cleanroomsml._services.clean_rooms_ml import ensure_sync_iterator
from aws_sdk_cleanroomsml._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_cleanroomsml._auth._signers
import aws_sdk_cleanroomsml._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import CleanRoomsMLClient, CleanRoomsMLClientConfig
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import AsyncCleanRoomsMLClient, AsyncCleanRoomsMLClientConfig
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_arn
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_summary
    import aws_sdk_cleanroomsml.types.container_config
    import aws_sdk_cleanroomsml.types.create_configured_model_algorithm_request
    import aws_sdk_cleanroomsml.types.create_configured_model_algorithm_response
    import aws_sdk_cleanroomsml.types.delete_configured_model_algorithm_request
    import aws_sdk_cleanroomsml.types.get_configured_model_algorithm_request
    import aws_sdk_cleanroomsml.types.get_configured_model_algorithm_response
    import aws_sdk_cleanroomsml.types.iam_role_arn
    import aws_sdk_cleanroomsml.types.inference_container_config
    import aws_sdk_cleanroomsml.types.kms_key_arn
    import aws_sdk_cleanroomsml.types.list_configured_model_algorithms_request
    import aws_sdk_cleanroomsml.types.list_configured_model_algorithms_response
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.tag_map

class ConfiguredModelAlgorithm:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service
    def create(self, name: "aws_sdk_cleanroomsml.types.name_string.NameString", role_arn: "aws_sdk_cleanroomsml.types.iam_role_arn.IamRoleArn", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, description: Optional["aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"] = None, training_container_config: Optional["aws_sdk_cleanroomsml.types.container_config.ContainerConfig"] = None, inference_container_config: Optional["aws_sdk_cleanroomsml.types.inference_container_config.InferenceContainerConfig"] = None, tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None, kms_key_arn: Optional["aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None) -> "aws_sdk_cleanroomsml.types.create_configured_model_algorithm_response.CreateConfiguredModelAlgorithmResponse":
        """<p>Creates a configured model algorithm using a container image stored in an ECR repository.</p>

        Args:
            name: <p>The name of the configured model algorithm.</p>
            description: <p>The description of the configured model algorithm.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the role that is used to access the repository.</p>
            training_container_config: <p>Configuration information for the training container, including entrypoints and arguments.</p>
            inference_container_config: <p>Configuration information for the inference container that is used when you run an inference job on a configured model algorithm.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the configured ML model algorithm and associated data.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.create_configured_model_algorithm_request.CreateConfiguredModelAlgorithmRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.create_configured_model_algorithm_response.CreateConfiguredModelAlgorithmResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm.create_configured_model_algorithm(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.create_configured_model_algorithm_request.CreateConfiguredModelAlgorithmRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["role_arn"] = role_arn
        if training_container_config is not None:
            input["training_container_config"] = training_container_config
        if inference_container_config is not None:
            input["inference_container_config"] = inference_container_config
        if tags is not None:
            input["tags"] = tags
        if kms_key_arn is not None:
            input["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None) -> "aws_sdk_cleanroomsml.types.get_configured_model_algorithm_response.GetConfiguredModelAlgorithmResponse":
        """<p>Returns information about a configured model algorithm.</p>

        Args:
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to return information about.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.get_configured_model_algorithm_request.GetConfiguredModelAlgorithmRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.get_configured_model_algorithm_response.GetConfiguredModelAlgorithmResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm.get_configured_model_algorithm(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_configured_model_algorithm_request.GetConfiguredModelAlgorithmRequest = {}  # type: ignore[typeddict-item]
        input["configured_model_algorithm_arn"] = configured_model_algorithm_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None) -> None:
        """<p>Deletes a configured model algorithm.</p>

        Args:
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to delete.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.delete_configured_model_algorithm_request.DeleteConfiguredModelAlgorithmRequest]') -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm.delete_configured_model_algorithm(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.delete_configured_model_algorithm_request.DeleteConfiguredModelAlgorithmRequest = {}  # type: ignore[typeddict-item]
        input["configured_model_algorithm_arn"] = configured_model_algorithm_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_cleanroomsml.types.max_results.MaxResults"] = None) -> "aws_sdk_cleanroomsml.types.list_configured_model_algorithms_response.ListConfiguredModelAlgorithmsResponse":
        """<p>Returns a list of configured model algorithms.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.list_configured_model_algorithms_request.ListConfiguredModelAlgorithmsRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.list_configured_model_algorithms_response.ListConfiguredModelAlgorithmsResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithms
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithms.list_configured_model_algorithms(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.list_configured_model_algorithms_request.ListConfiguredModelAlgorithmsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncConfiguredModelAlgorithm:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service
    async def create(self, name: "aws_sdk_cleanroomsml.types.name_string.NameString", role_arn: "aws_sdk_cleanroomsml.types.iam_role_arn.IamRoleArn", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, description: Optional["aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"] = None, training_container_config: Optional["aws_sdk_cleanroomsml.types.container_config.ContainerConfig"] = None, inference_container_config: Optional["aws_sdk_cleanroomsml.types.inference_container_config.InferenceContainerConfig"] = None, tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None, kms_key_arn: Optional["aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None) -> "aws_sdk_cleanroomsml.types.create_configured_model_algorithm_response.CreateConfiguredModelAlgorithmResponse":
        """<p>Creates a configured model algorithm using a container image stored in an ECR repository.</p>

        Args:
            name: <p>The name of the configured model algorithm.</p>
            description: <p>The description of the configured model algorithm.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the role that is used to access the repository.</p>
            training_container_config: <p>Configuration information for the training container, including entrypoints and arguments.</p>
            inference_container_config: <p>Configuration information for the inference container that is used when you run an inference job on a configured model algorithm.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the configured ML model algorithm and associated data.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.create_configured_model_algorithm_request.CreateConfiguredModelAlgorithmRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.create_configured_model_algorithm_response.CreateConfiguredModelAlgorithmResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm.async_create_configured_model_algorithm(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.create_configured_model_algorithm_request.CreateConfiguredModelAlgorithmRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["role_arn"] = role_arn
        if training_container_config is not None:
            input["training_container_config"] = training_container_config
        if inference_container_config is not None:
            input["inference_container_config"] = inference_container_config
        if tags is not None:
            input["tags"] = tags
        if kms_key_arn is not None:
            input["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None) -> "aws_sdk_cleanroomsml.types.get_configured_model_algorithm_response.GetConfiguredModelAlgorithmResponse":
        """<p>Returns information about a configured model algorithm.</p>

        Args:
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to return information about.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_configured_model_algorithm_request.GetConfiguredModelAlgorithmRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.get_configured_model_algorithm_response.GetConfiguredModelAlgorithmResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm.async_get_configured_model_algorithm(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_configured_model_algorithm_request.GetConfiguredModelAlgorithmRequest = {}  # type: ignore[typeddict-item]
        input["configured_model_algorithm_arn"] = configured_model_algorithm_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None) -> None:
        """<p>Deletes a configured model algorithm.</p>

        Args:
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to delete.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.delete_configured_model_algorithm_request.DeleteConfiguredModelAlgorithmRequest]') -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm.async_delete_configured_model_algorithm(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.delete_configured_model_algorithm_request.DeleteConfiguredModelAlgorithmRequest = {}  # type: ignore[typeddict-item]
        input["configured_model_algorithm_arn"] = configured_model_algorithm_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_cleanroomsml.types.max_results.MaxResults"] = None) -> "aws_sdk_cleanroomsml.types.list_configured_model_algorithms_response.ListConfiguredModelAlgorithmsResponse":
        """<p>Returns a list of configured model algorithms.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_configured_model_algorithms_request.ListConfiguredModelAlgorithmsRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.list_configured_model_algorithms_response.ListConfiguredModelAlgorithmsResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithms
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithms.async_list_configured_model_algorithms(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.list_configured_model_algorithms_request.ListConfiguredModelAlgorithmsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output