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
    import aws_sdk_cleanroomsml.types.account_id
    import aws_sdk_cleanroomsml.types.cancel_trained_model_inference_job_request
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn
    import aws_sdk_cleanroomsml.types.get_trained_model_inference_job_request
    import aws_sdk_cleanroomsml.types.get_trained_model_inference_job_response
    import aws_sdk_cleanroomsml.types.inference_container_execution_parameters
    import aws_sdk_cleanroomsml.types.inference_environment_map
    import aws_sdk_cleanroomsml.types.inference_output_configuration
    import aws_sdk_cleanroomsml.types.inference_resource_config
    import aws_sdk_cleanroomsml.types.kms_key_arn
    import aws_sdk_cleanroomsml.types.list_trained_model_inference_jobs_request
    import aws_sdk_cleanroomsml.types.list_trained_model_inference_jobs_response
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.model_inference_data_source
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.start_trained_model_inference_job_request
    import aws_sdk_cleanroomsml.types.start_trained_model_inference_job_response
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.trained_model_inference_job_arn
    import aws_sdk_cleanroomsml.types.trained_model_inference_job_summary
    import aws_sdk_cleanroomsml.types.uuid
    from aws_sdk_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from aws_sdk_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class TrainedModelInferenceJob:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        resource_config: "aws_sdk_cleanroomsml.types.inference_resource_config.InferenceResourceConfig",
        output_configuration: "aws_sdk_cleanroomsml.types.inference_output_configuration.InferenceOutputConfiguration",
        data_source: "aws_sdk_cleanroomsml.types.model_inference_data_source.ModelInferenceDataSource",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        trained_model_version_identifier: Optional[
            "aws_sdk_cleanroomsml.types.uuid.UUID"
        ] = None,
        configured_model_algorithm_association_arn: Optional[
            "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
        ] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        container_execution_parameters: Optional[
            "aws_sdk_cleanroomsml.types.inference_container_execution_parameters.InferenceContainerExecutionParameters"
        ] = None,
        environment: Optional[
            "aws_sdk_cleanroomsml.types.inference_environment_map.InferenceEnvironmentMap"
        ] = None,
        kms_key_arn: Optional[
            "aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None,
        ml_model_inference_payer_account_id: Optional[
            "aws_sdk_cleanroomsml.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.start_trained_model_inference_job_response.StartTrainedModelInferenceJobResponse":
        """<p>Defines the information necessary to begin a trained model inference job.</p>

        Args:
            membership_identifier: <p>The membership ID of the membership that contains the trained model inference job.</p>
            name: <p>The name of the trained model inference job.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that is used for this trained model inference job.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to use for inference. This specifies which version of the trained model should be used to generate predictions on the input data.</p>
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that is used for this trained model inference job.</p>
            resource_config: <p>Defines the resource configuration for the trained model inference job.</p>
            output_configuration: <p>Defines the output configuration information for the trained model inference job.</p>
            data_source: <p>Defines the data source that is used for the trained model inference job.</p>
            description: <p>The description of the trained model inference job.</p>
            container_execution_parameters: <p>The execution parameters for the container.</p>
            environment: <p>The environment variables to set in the Docker container.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the ML inference job and associated data.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            ml_model_inference_payer_account_id: <p>The account ID of the member that is responsible for paying for model inference costs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.start_trained_model_inference_job_request.StartTrainedModelInferenceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.start_trained_model_inference_job_response.StartTrainedModelInferenceJobResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_trained_model_inference_job

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_trained_model_inference_job.start_trained_model_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.start_trained_model_inference_job_request.StartTrainedModelInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["name"] = name
        input_["trained_model_arn"] = trained_model_arn
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )
        if configured_model_algorithm_association_arn is not None:
            input_["configured_model_algorithm_association_arn"] = (
                configured_model_algorithm_association_arn
            )
        input_["resource_config"] = resource_config
        input_["output_configuration"] = output_configuration
        input_["data_source"] = data_source
        if description is not None:
            input_["description"] = description
        if container_execution_parameters is not None:
            input_["container_execution_parameters"] = container_execution_parameters
        if environment is not None:
            input_["environment"] = environment
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if ml_model_inference_payer_account_id is not None:
            input_["ml_model_inference_payer_account_id"] = (
                ml_model_inference_payer_account_id
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        trained_model_inference_job_arn: "aws_sdk_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_trained_model_inference_job_response.GetTrainedModelInferenceJobResponse":
        """<p>Returns information about a trained model inference job.</p>

        Args:
            membership_identifier: <p>Provides the membership ID of the membership that contains the trained model inference job that you are interested in.</p>
            trained_model_inference_job_arn: <p>Provides the Amazon Resource Name (ARN) of the trained model inference job that you are interested in.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.get_trained_model_inference_job_request.GetTrainedModelInferenceJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.get_trained_model_inference_job_response.GetTrainedModelInferenceJobResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_trained_model_inference_job

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_trained_model_inference_job.get_trained_model_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_trained_model_inference_job_request.GetTrainedModelInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["trained_model_inference_job_arn"] = trained_model_inference_job_arn

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
        trained_model_arn: Optional[
            "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
        ] = None,
        trained_model_version_identifier: Optional[
            "aws_sdk_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_trained_model_inference_jobs_response.ListTrainedModelInferenceJobsResponse":
        """<p>Returns a list of trained model inference jobs that match the request parameters.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            membership_identifier: <p>The membership </p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of a trained model that was used to create the trained model inference jobs that you are interested in.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to filter inference jobs by. When specified, only inference jobs that used this specific version of the trained model are returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.list_trained_model_inference_jobs_request.ListTrainedModelInferenceJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cleanroomsml.types.list_trained_model_inference_jobs_response.ListTrainedModelInferenceJobsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_model_inference_jobs

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_model_inference_jobs.list_trained_model_inference_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_trained_model_inference_jobs_request.ListTrainedModelInferenceJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["membership_identifier"] = membership_identifier
        if trained_model_arn is not None:
            input_["trained_model_arn"] = trained_model_arn
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_trained_model_inference_job(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        trained_model_inference_job_arn: "aws_sdk_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Submits a request to cancel a trained model inference job.</p>

        Args:
            membership_identifier: <p>The membership ID of the trained model inference job that you want to cancel.</p>
            trained_model_inference_job_arn: <p>The Amazon Resource Name (ARN) of the trained model inference job that you want to cancel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanroomsml.types.cancel_trained_model_inference_job_request.CancelTrainedModelInferenceJobRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model_inference_job

            output, http_response = (
                aws_sdk_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model_inference_job.cancel_trained_model_inference_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.cancel_trained_model_inference_job_request.CancelTrainedModelInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["trained_model_inference_job_arn"] = trained_model_inference_job_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTrainedModelInferenceJob:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        name: "aws_sdk_cleanroomsml.types.name_string.NameString",
        trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        resource_config: "aws_sdk_cleanroomsml.types.inference_resource_config.InferenceResourceConfig",
        output_configuration: "aws_sdk_cleanroomsml.types.inference_output_configuration.InferenceOutputConfiguration",
        data_source: "aws_sdk_cleanroomsml.types.model_inference_data_source.ModelInferenceDataSource",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        trained_model_version_identifier: Optional[
            "aws_sdk_cleanroomsml.types.uuid.UUID"
        ] = None,
        configured_model_algorithm_association_arn: Optional[
            "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
        ] = None,
        description: Optional[
            "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        container_execution_parameters: Optional[
            "aws_sdk_cleanroomsml.types.inference_container_execution_parameters.InferenceContainerExecutionParameters"
        ] = None,
        environment: Optional[
            "aws_sdk_cleanroomsml.types.inference_environment_map.InferenceEnvironmentMap"
        ] = None,
        kms_key_arn: Optional[
            "aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_cleanroomsml.types.tag_map.TagMap"] = None,
        ml_model_inference_payer_account_id: Optional[
            "aws_sdk_cleanroomsml.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.start_trained_model_inference_job_response.StartTrainedModelInferenceJobResponse":
        """<p>Defines the information necessary to begin a trained model inference job.</p>

        Args:
            membership_identifier: <p>The membership ID of the membership that contains the trained model inference job.</p>
            name: <p>The name of the trained model inference job.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that is used for this trained model inference job.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to use for inference. This specifies which version of the trained model should be used to generate predictions on the input data.</p>
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that is used for this trained model inference job.</p>
            resource_config: <p>Defines the resource configuration for the trained model inference job.</p>
            output_configuration: <p>Defines the output configuration information for the trained model inference job.</p>
            data_source: <p>Defines the data source that is used for the trained model inference job.</p>
            description: <p>The description of the trained model inference job.</p>
            container_execution_parameters: <p>The execution parameters for the container.</p>
            environment: <p>The environment variables to set in the Docker container.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the ML inference job and associated data.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            ml_model_inference_payer_account_id: <p>The account ID of the member that is responsible for paying for model inference costs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.start_trained_model_inference_job_request.StartTrainedModelInferenceJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.start_trained_model_inference_job_response.StartTrainedModelInferenceJobResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_trained_model_inference_job

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.start_trained_model_inference_job.async_start_trained_model_inference_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.start_trained_model_inference_job_request.StartTrainedModelInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["name"] = name
        input_["trained_model_arn"] = trained_model_arn
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )
        if configured_model_algorithm_association_arn is not None:
            input_["configured_model_algorithm_association_arn"] = (
                configured_model_algorithm_association_arn
            )
        input_["resource_config"] = resource_config
        input_["output_configuration"] = output_configuration
        input_["data_source"] = data_source
        if description is not None:
            input_["description"] = description
        if container_execution_parameters is not None:
            input_["container_execution_parameters"] = container_execution_parameters
        if environment is not None:
            input_["environment"] = environment
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if ml_model_inference_payer_account_id is not None:
            input_["ml_model_inference_payer_account_id"] = (
                ml_model_inference_payer_account_id
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        trained_model_inference_job_arn: "aws_sdk_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.get_trained_model_inference_job_response.GetTrainedModelInferenceJobResponse":
        """<p>Returns information about a trained model inference job.</p>

        Args:
            membership_identifier: <p>Provides the membership ID of the membership that contains the trained model inference job that you are interested in.</p>
            trained_model_inference_job_arn: <p>Provides the Amazon Resource Name (ARN) of the trained model inference job that you are interested in.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.get_trained_model_inference_job_request.GetTrainedModelInferenceJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.get_trained_model_inference_job_response.GetTrainedModelInferenceJobResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_trained_model_inference_job

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.get_trained_model_inference_job.async_get_trained_model_inference_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.get_trained_model_inference_job_request.GetTrainedModelInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["trained_model_inference_job_arn"] = trained_model_inference_job_arn

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
        trained_model_arn: Optional[
            "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
        ] = None,
        trained_model_version_identifier: Optional[
            "aws_sdk_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_trained_model_inference_jobs_response.ListTrainedModelInferenceJobsResponse":
        """<p>Returns a list of trained model inference jobs that match the request parameters.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            membership_identifier: <p>The membership </p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of a trained model that was used to create the trained model inference jobs that you are interested in.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to filter inference jobs by. When specified, only inference jobs that used this specific version of the trained model are returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_trained_model_inference_jobs_request.ListTrainedModelInferenceJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_trained_model_inference_jobs_response.ListTrainedModelInferenceJobsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_model_inference_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_trained_model_inference_jobs.async_list_trained_model_inference_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_trained_model_inference_jobs_request.ListTrainedModelInferenceJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["membership_identifier"] = membership_identifier
        if trained_model_arn is not None:
            input_["trained_model_arn"] = trained_model_arn
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_trained_model_inference_job(
        self,
        membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        trained_model_inference_job_arn: "aws_sdk_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Submits a request to cancel a trained model inference job.</p>

        Args:
            membership_identifier: <p>The membership ID of the trained model inference job that you want to cancel.</p>
            trained_model_inference_job_arn: <p>The Amazon Resource Name (ARN) of the trained model inference job that you want to cancel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.cancel_trained_model_inference_job_request.CancelTrainedModelInferenceJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model_inference_job

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model_inference_job.async_cancel_trained_model_inference_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.cancel_trained_model_inference_job_request.CancelTrainedModelInferenceJobRequest = {}  # type: ignore[typeddict-item]
        input_["membership_identifier"] = membership_identifier
        input_["trained_model_inference_job_arn"] = trained_model_inference_job_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
