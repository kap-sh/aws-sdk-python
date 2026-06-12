from typing import Optional, TYPE_CHECKING
from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import ensure_async_iterator
from aws_sdk_cleanroomsml._services.clean_rooms_ml import ensure_sync_iterator
from aws_sdk_cleanroomsml._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_cleanroomsml._auth._signers
import aws_sdk_cleanroomsml._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import CleanRoomsMLClient, CleanRoomsMLClientConfig
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import AsyncCleanRoomsMLClient, AsyncCleanRoomsMLClientConfig
    import aws_sdk_cleanroomsml.types.account_id
    import aws_sdk_cleanroomsml.types.cancel_trained_model_request
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn
    import aws_sdk_cleanroomsml.types.create_trained_model_request
    import aws_sdk_cleanroomsml.types.create_trained_model_response
    import aws_sdk_cleanroomsml.types.delete_trained_model_output_request
    import aws_sdk_cleanroomsml.types.environment
    import aws_sdk_cleanroomsml.types.get_collaboration_trained_model_request
    import aws_sdk_cleanroomsml.types.get_collaboration_trained_model_response
    import aws_sdk_cleanroomsml.types.get_trained_model_request
    import aws_sdk_cleanroomsml.types.get_trained_model_response
    import aws_sdk_cleanroomsml.types.hyper_parameters
    import aws_sdk_cleanroomsml.types.incremental_training_data_channels
    import aws_sdk_cleanroomsml.types.kms_key_arn
    import aws_sdk_cleanroomsml.types.list_trained_model_versions_request
    import aws_sdk_cleanroomsml.types.list_trained_model_versions_response
    import aws_sdk_cleanroomsml.types.list_trained_models_request
    import aws_sdk_cleanroomsml.types.list_trained_models_response
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.model_training_data_channels
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.resource_config
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.stopping_condition
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.trained_model_status
    import aws_sdk_cleanroomsml.types.trained_model_summary
    import aws_sdk_cleanroomsml.types.training_input_mode
    import aws_sdk_cleanroomsml.types.uuid

class TrainedModel:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service
    def create(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", name: "aws_sdk_cleanroomsml.types.name_string.NameString", configured_model_algorithm_association_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn", resource_config: "aws_sdk_cleanroomsml.types.resource_config.ResourceConfig", data_channels: "aws_sdk_cleanroomsml.types.model_training_data_channels.ModelTrainingDataChannels", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, hyperparameters: Optional["aws_sdk_cleanroomsml.types.hyper_parameters.HyperParameters"] = None, environment: Optional["aws_sdk_cleanroomsml.types.environment.Environment"] = None, stopping_condition: Optional["aws_sdk_cleanroomsml.types.stopping_condition.StoppingCondition"] = None, incremental_training_data_channels: Optional["aws_sdk_cleanroomsml.types.incremental_training_data_channels.IncrementalTrainingDataChannels"] = None, training_input_mode: Optional["aws_sdk_cleanroomsml.types.training_input_mode.TrainingInputMode"] = None, description: Optional["aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"] = None, kms_key_arn: Optional["aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None, tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None, ml_model_training_payer_account_id: Optional["aws_sdk_cleanroomsml.types.account_id.AccountId"] = None) -> "aws_sdk_cleanroomsml.types.create_trained_model_response.CreateTrainedModelResponse":
        """<p>Creates a trained model from an associated configured model algorithm using data from any member of the collaboration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is creating the trained model.</p>
            name: <p>The name of the trained model.</p>
            configured_model_algorithm_association_arn: <p>The associated configured model algorithm used to train this model.</p>
            hyperparameters: <p>Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process.</p>
            environment: <p>The environment variables to set in the Docker container.</p>
            resource_config: <p>Information about the EC2 resources that are used to train this model.</p>
            stopping_condition: <p>The criteria that is used to stop model training.</p>
            incremental_training_data_channels: <p>Specifies the incremental training data channels for the trained model. </p> <p>Incremental training allows you to create a new trained model with updates without retraining from scratch. You can specify up to one incremental training data channel that references a previously trained model and its version.</p> <p>Limit: Maximum of 20 channels total (including both <code>incrementalTrainingDataChannels</code> and <code>dataChannels</code>).</p>
            data_channels: <p>Defines the data channels that are used as input for the trained model request.</p> <p>Limit: Maximum of 20 channels total (including both <code>dataChannels</code> and <code>incrementalTrainingDataChannels</code>).</p>
            training_input_mode: <p>The input mode for accessing the training data. This parameter determines how the training data is made available to the training algorithm. Valid values are:</p> <ul> <li> <p> <code>File</code> - The training data is downloaded to the training instance and made available as files.</p> </li> <li> <p> <code>FastFile</code> - The training data is streamed directly from Amazon S3 to the training algorithm, providing faster access for large datasets.</p> </li> <li> <p> <code>Pipe</code> - The training data is streamed to the training algorithm using named pipes, which can improve performance for certain algorithms.</p> </li> </ul>
            description: <p>The description of the trained model.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and the associated data.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            ml_model_training_payer_account_id: <p>The account ID of the member that is responsible for paying for model training costs.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.create_trained_model_request.CreateTrainedModelRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.create_trained_model_response.CreateTrainedModelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_trained_model
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_trained_model.create_trained_model(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.create_trained_model_request.CreateTrainedModelRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["name"] = name
        input["configured_model_algorithm_association_arn"] = configured_model_algorithm_association_arn
        if hyperparameters is not None:
            input["hyperparameters"] = hyperparameters
        if environment is not None:
            input["environment"] = environment
        input["resource_config"] = resource_config
        if stopping_condition is not None:
            input["stopping_condition"] = stopping_condition
        if incremental_training_data_channels is not None:
            input["incremental_training_data_channels"] = incremental_training_data_channels
        input["data_channels"] = data_channels
        if training_input_mode is not None:
            input["training_input_mode"] = training_input_mode
        if description is not None:
            input["description"] = description
        if kms_key_arn is not None:
            input["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input["tags"] = tags
        if ml_model_training_payer_account_id is not None:
            input["ml_model_training_payer_account_id"] = ml_model_training_payer_account_id

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn", membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, version_identifier: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None) -> "aws_sdk_cleanroomsml.types.get_trained_model_response.GetTrainedModelResponse":
        """<p>Returns information about a trained model.</p>

        Args:
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that you are interested in.</p>
            membership_identifier: <p>The membership ID of the member that created the trained model that you are interested in.</p>
            version_identifier: <p>The version identifier of the trained model to retrieve. If not specified, the operation returns information about the latest version of the trained model.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.get_trained_model_request.GetTrainedModelRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.get_trained_model_response.GetTrainedModelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_trained_model
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_trained_model.get_trained_model(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_trained_model_request.GetTrainedModelRequest = {}  # type: ignore[typeddict-item]
        input["trained_model_arn"] = trained_model_arn
        input["membership_identifier"] = membership_identifier
        if version_identifier is not None:
            input["version_identifier"] = version_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def delete(self, trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn", membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, version_identifier: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None) -> None:
        """<p>Deletes the model artifacts stored by the service.</p>

        Args:
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model whose output you want to delete.</p>
            membership_identifier: <p>The membership ID of the member that is deleting the trained model output.</p>
            version_identifier: <p>The version identifier of the trained model to delete. If not specified, the operation will delete the base version of the trained model. When specified, only the particular version will be deleted.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.delete_trained_model_output_request.DeleteTrainedModelOutputRequest]') -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_trained_model_output
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_trained_model_output.delete_trained_model_output(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.delete_trained_model_output_request.DeleteTrainedModelOutputRequest = {}  # type: ignore[typeddict-item]
        input["trained_model_arn"] = trained_model_arn
        input["membership_identifier"] = membership_identifier
        if version_identifier is not None:
            input["version_identifier"] = version_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_cleanroomsml.types.max_results.MaxResults"] = None) -> "aws_sdk_cleanroomsml.types.list_trained_models_response.ListTrainedModelsResponse":
        """<p>Returns a list of trained models.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            membership_identifier: <p>The membership ID of the member that created the trained models you are interested in.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.list_trained_models_request.ListTrainedModelsRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.list_trained_models_response.ListTrainedModelsResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_models
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_models.list_trained_models(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.list_trained_models_request.ListTrainedModelsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["membership_identifier"] = membership_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def cancel_trained_model(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, version_identifier: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None) -> None:
        """<p>Submits a request to cancel the trained model job.</p>

        Args:
            membership_identifier: <p>The membership ID of the trained model job that you want to cancel.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model job that you want to cancel.</p>
            version_identifier: <p>The version identifier of the trained model to cancel. This parameter allows you to specify which version of the trained model you want to cancel when multiple versions exist.</p> <p>If <code>versionIdentifier</code> is not specified, the base model will be cancelled.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.cancel_trained_model_request.CancelTrainedModelRequest]') -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model.cancel_trained_model(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.cancel_trained_model_request.CancelTrainedModelRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["trained_model_arn"] = trained_model_arn
        if version_identifier is not None:
            input["version_identifier"] = version_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def get_collaboration_trained_model(self, trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn", collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, version_identifier: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None) -> "aws_sdk_cleanroomsml.types.get_collaboration_trained_model_response.GetCollaborationTrainedModelResponse":
        """<p>Returns information about a trained model in a collaboration.</p>

        Args:
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that you want to return information about.</p>
            collaboration_identifier: <p>The collaboration ID that contains the trained model that you want to return information about.</p>
            version_identifier: <p>The version identifier of the trained model to retrieve. If not specified, the operation returns information about the latest version of the trained model.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.get_collaboration_trained_model_request.GetCollaborationTrainedModelRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.get_collaboration_trained_model_response.GetCollaborationTrainedModelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_trained_model
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_trained_model.get_collaboration_trained_model(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_collaboration_trained_model_request.GetCollaborationTrainedModelRequest = {}  # type: ignore[typeddict-item]
        input["trained_model_arn"] = trained_model_arn
        input["collaboration_identifier"] = collaboration_identifier
        if version_identifier is not None:
            input["version_identifier"] = version_identifier

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def list_trained_model_versions(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn", *, config_overrides: Optional[CleanRoomsMLClientConfig] = None, next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_cleanroomsml.types.max_results.MaxResults"] = None, status: Optional["aws_sdk_cleanroomsml.types.trained_model_status.TrainedModelStatus"] = None) -> "aws_sdk_cleanroomsml.types.list_trained_model_versions_response.ListTrainedModelVersionsResponse":
        """<p>Returns a list of trained model versions for a specified trained model. This operation allows you to view all versions of a trained model, including information about their status and creation details. You can use this to track the evolution of your trained models and select specific versions for inference or further training.</p>

        Args:
            next_token: <p>The pagination token from a previous <code>ListTrainedModelVersions</code> request. Use this token to retrieve the next page of results.</p>
            max_results: <p>The maximum number of trained model versions to return in a single page. The default value is 10, and the maximum value is 100.</p>
            membership_identifier: <p>The membership identifier for the collaboration that contains the trained model.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model for which to list versions.</p>
            status: <p>Filter the results to only include trained model versions with the specified status. Valid values include <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>ACTIVE</code>, <code>CREATE_FAILED</code>, and others.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_cleanroomsml.types.list_trained_model_versions_request.ListTrainedModelVersionsRequest]') -> OperationResponse["aws_sdk_cleanroomsml.types.list_trained_model_versions_response.ListTrainedModelVersionsResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_model_versions
            output, http_response = aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_model_versions.list_trained_model_versions(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.list_trained_model_versions_request.ListTrainedModelVersionsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["membership_identifier"] = membership_identifier
        input["trained_model_arn"] = trained_model_arn
        if status is not None:
            input["status"] = status

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncTrainedModel:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service
    async def create(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", name: "aws_sdk_cleanroomsml.types.name_string.NameString", configured_model_algorithm_association_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn", resource_config: "aws_sdk_cleanroomsml.types.resource_config.ResourceConfig", data_channels: "aws_sdk_cleanroomsml.types.model_training_data_channels.ModelTrainingDataChannels", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, hyperparameters: Optional["aws_sdk_cleanroomsml.types.hyper_parameters.HyperParameters"] = None, environment: Optional["aws_sdk_cleanroomsml.types.environment.Environment"] = None, stopping_condition: Optional["aws_sdk_cleanroomsml.types.stopping_condition.StoppingCondition"] = None, incremental_training_data_channels: Optional["aws_sdk_cleanroomsml.types.incremental_training_data_channels.IncrementalTrainingDataChannels"] = None, training_input_mode: Optional["aws_sdk_cleanroomsml.types.training_input_mode.TrainingInputMode"] = None, description: Optional["aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"] = None, kms_key_arn: Optional["aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None, tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None, ml_model_training_payer_account_id: Optional["aws_sdk_cleanroomsml.types.account_id.AccountId"] = None) -> "aws_sdk_cleanroomsml.types.create_trained_model_response.CreateTrainedModelResponse":
        """<p>Creates a trained model from an associated configured model algorithm using data from any member of the collaboration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is creating the trained model.</p>
            name: <p>The name of the trained model.</p>
            configured_model_algorithm_association_arn: <p>The associated configured model algorithm used to train this model.</p>
            hyperparameters: <p>Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process.</p>
            environment: <p>The environment variables to set in the Docker container.</p>
            resource_config: <p>Information about the EC2 resources that are used to train this model.</p>
            stopping_condition: <p>The criteria that is used to stop model training.</p>
            incremental_training_data_channels: <p>Specifies the incremental training data channels for the trained model. </p> <p>Incremental training allows you to create a new trained model with updates without retraining from scratch. You can specify up to one incremental training data channel that references a previously trained model and its version.</p> <p>Limit: Maximum of 20 channels total (including both <code>incrementalTrainingDataChannels</code> and <code>dataChannels</code>).</p>
            data_channels: <p>Defines the data channels that are used as input for the trained model request.</p> <p>Limit: Maximum of 20 channels total (including both <code>dataChannels</code> and <code>incrementalTrainingDataChannels</code>).</p>
            training_input_mode: <p>The input mode for accessing the training data. This parameter determines how the training data is made available to the training algorithm. Valid values are:</p> <ul> <li> <p> <code>File</code> - The training data is downloaded to the training instance and made available as files.</p> </li> <li> <p> <code>FastFile</code> - The training data is streamed directly from Amazon S3 to the training algorithm, providing faster access for large datasets.</p> </li> <li> <p> <code>Pipe</code> - The training data is streamed to the training algorithm using named pipes, which can improve performance for certain algorithms.</p> </li> </ul>
            description: <p>The description of the trained model.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and the associated data.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            ml_model_training_payer_account_id: <p>The account ID of the member that is responsible for paying for model training costs.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.create_trained_model_request.CreateTrainedModelRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.create_trained_model_response.CreateTrainedModelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_trained_model
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.create_trained_model.async_create_trained_model(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.create_trained_model_request.CreateTrainedModelRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["name"] = name
        input["configured_model_algorithm_association_arn"] = configured_model_algorithm_association_arn
        if hyperparameters is not None:
            input["hyperparameters"] = hyperparameters
        if environment is not None:
            input["environment"] = environment
        input["resource_config"] = resource_config
        if stopping_condition is not None:
            input["stopping_condition"] = stopping_condition
        if incremental_training_data_channels is not None:
            input["incremental_training_data_channels"] = incremental_training_data_channels
        input["data_channels"] = data_channels
        if training_input_mode is not None:
            input["training_input_mode"] = training_input_mode
        if description is not None:
            input["description"] = description
        if kms_key_arn is not None:
            input["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input["tags"] = tags
        if ml_model_training_payer_account_id is not None:
            input["ml_model_training_payer_account_id"] = ml_model_training_payer_account_id

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn", membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, version_identifier: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None) -> "aws_sdk_cleanroomsml.types.get_trained_model_response.GetTrainedModelResponse":
        """<p>Returns information about a trained model.</p>

        Args:
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that you are interested in.</p>
            membership_identifier: <p>The membership ID of the member that created the trained model that you are interested in.</p>
            version_identifier: <p>The version identifier of the trained model to retrieve. If not specified, the operation returns information about the latest version of the trained model.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_trained_model_request.GetTrainedModelRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.get_trained_model_response.GetTrainedModelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_trained_model
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_trained_model.async_get_trained_model(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_trained_model_request.GetTrainedModelRequest = {}  # type: ignore[typeddict-item]
        input["trained_model_arn"] = trained_model_arn
        input["membership_identifier"] = membership_identifier
        if version_identifier is not None:
            input["version_identifier"] = version_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def delete(self, trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn", membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, version_identifier: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None) -> None:
        """<p>Deletes the model artifacts stored by the service.</p>

        Args:
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model whose output you want to delete.</p>
            membership_identifier: <p>The membership ID of the member that is deleting the trained model output.</p>
            version_identifier: <p>The version identifier of the trained model to delete. If not specified, the operation will delete the base version of the trained model. When specified, only the particular version will be deleted.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.delete_trained_model_output_request.DeleteTrainedModelOutputRequest]') -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_trained_model_output
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.delete_trained_model_output.async_delete_trained_model_output(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.delete_trained_model_output_request.DeleteTrainedModelOutputRequest = {}  # type: ignore[typeddict-item]
        input["trained_model_arn"] = trained_model_arn
        input["membership_identifier"] = membership_identifier
        if version_identifier is not None:
            input["version_identifier"] = version_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_cleanroomsml.types.max_results.MaxResults"] = None) -> "aws_sdk_cleanroomsml.types.list_trained_models_response.ListTrainedModelsResponse":
        """<p>Returns a list of trained models.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            membership_identifier: <p>The membership ID of the member that created the trained models you are interested in.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_trained_models_request.ListTrainedModelsRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.list_trained_models_response.ListTrainedModelsResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_models
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_models.async_list_trained_models(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.list_trained_models_request.ListTrainedModelsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["membership_identifier"] = membership_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def cancel_trained_model(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, version_identifier: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None) -> None:
        """<p>Submits a request to cancel the trained model job.</p>

        Args:
            membership_identifier: <p>The membership ID of the trained model job that you want to cancel.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model job that you want to cancel.</p>
            version_identifier: <p>The version identifier of the trained model to cancel. This parameter allows you to specify which version of the trained model you want to cancel when multiple versions exist.</p> <p>If <code>versionIdentifier</code> is not specified, the base model will be cancelled.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.cancel_trained_model_request.CancelTrainedModelRequest]') -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model.async_cancel_trained_model(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.cancel_trained_model_request.CancelTrainedModelRequest = {}  # type: ignore[typeddict-item]
        input["membership_identifier"] = membership_identifier
        input["trained_model_arn"] = trained_model_arn
        if version_identifier is not None:
            input["version_identifier"] = version_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def get_collaboration_trained_model(self, trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn", collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, version_identifier: Optional["aws_sdk_cleanroomsml.types.uuid.UUID"] = None) -> "aws_sdk_cleanroomsml.types.get_collaboration_trained_model_response.GetCollaborationTrainedModelResponse":
        """<p>Returns information about a trained model in a collaboration.</p>

        Args:
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that you want to return information about.</p>
            collaboration_identifier: <p>The collaboration ID that contains the trained model that you want to return information about.</p>
            version_identifier: <p>The version identifier of the trained model to retrieve. If not specified, the operation returns information about the latest version of the trained model.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_collaboration_trained_model_request.GetCollaborationTrainedModelRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.get_collaboration_trained_model_response.GetCollaborationTrainedModelResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_trained_model
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_collaboration_trained_model.async_get_collaboration_trained_model(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.get_collaboration_trained_model_request.GetCollaborationTrainedModelRequest = {}  # type: ignore[typeddict-item]
        input["trained_model_arn"] = trained_model_arn
        input["collaboration_identifier"] = collaboration_identifier
        if version_identifier is not None:
            input["version_identifier"] = version_identifier

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_trained_model_versions(self, membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID", trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn", *, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None, next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None, max_results: Optional["aws_sdk_cleanroomsml.types.max_results.MaxResults"] = None, status: Optional["aws_sdk_cleanroomsml.types.trained_model_status.TrainedModelStatus"] = None) -> "aws_sdk_cleanroomsml.types.list_trained_model_versions_response.ListTrainedModelVersionsResponse":
        """<p>Returns a list of trained model versions for a specified trained model. This operation allows you to view all versions of a trained model, including information about their status and creation details. You can use this to track the evolution of your trained models and select specific versions for inference or further training.</p>

        Args:
            next_token: <p>The pagination token from a previous <code>ListTrainedModelVersions</code> request. Use this token to retrieve the next page of results.</p>
            max_results: <p>The maximum number of trained model versions to return in a single page. The default value is 10, and the maximum value is 100.</p>
            membership_identifier: <p>The membership identifier for the collaboration that contains the trained model.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model for which to list versions.</p>
            status: <p>Filter the results to only include trained model versions with the specified status. Valid values include <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>ACTIVE</code>, <code>CREATE_FAILED</code>, and others.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_trained_model_versions_request.ListTrainedModelVersionsRequest]') -> AsyncOperationResponse["aws_sdk_cleanroomsml.types.list_trained_model_versions_response.ListTrainedModelVersionsResponse"]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_model_versions
            output, http_response = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_model_versions.async_list_trained_model_versions(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_cleanroomsml.types.list_trained_model_versions_request.ListTrainedModelVersionsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["membership_identifier"] = membership_identifier
        input["trained_model_arn"] = trained_model_arn
        if status is not None:
            input["status"] = status

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output