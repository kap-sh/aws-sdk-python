from typing import Optional, TYPE_CHECKING
from aws_sdk_braket._services.async_braket import ensure_async_iterator
from aws_sdk_braket._services.braket import ensure_sync_iterator
from aws_sdk_braket._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_braket._auth._signers
import aws_sdk_braket._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_braket._services.braket import BraketClient, BraketClientConfig
    from aws_sdk_braket._services.async_braket import AsyncBraketClient, AsyncBraketClientConfig
    import aws_sdk_braket.types.algorithm_specification
    import aws_sdk_braket.types.associations
    import aws_sdk_braket.types.cancel_job_request
    import aws_sdk_braket.types.cancel_job_response
    import aws_sdk_braket.types.create_job_request
    import aws_sdk_braket.types.create_job_response
    import aws_sdk_braket.types.device_config
    import aws_sdk_braket.types.get_job_request
    import aws_sdk_braket.types.get_job_response
    import aws_sdk_braket.types.hybrid_job_additional_attribute_names_list
    import aws_sdk_braket.types.hyper_parameters
    import aws_sdk_braket.types.input_config_list
    import aws_sdk_braket.types.instance_config
    import aws_sdk_braket.types.job_arn
    import aws_sdk_braket.types.job_checkpoint_config
    import aws_sdk_braket.types.job_output_data_config
    import aws_sdk_braket.types.job_stopping_condition
    import aws_sdk_braket.types.job_summary
    import aws_sdk_braket.types.role_arn
    import aws_sdk_braket.types.search_jobs_filter_list
    import aws_sdk_braket.types.search_jobs_request
    import aws_sdk_braket.types.search_jobs_response
    import aws_sdk_braket.types.string64
    import aws_sdk_braket.types.tags_map

class JobResource:
    def __init__(self, service: BraketClient) -> None:
        self._service = service
    def create(self, client_token: "aws_sdk_braket.types.string64.String64", algorithm_specification: "aws_sdk_braket.types.algorithm_specification.AlgorithmSpecification", output_data_config: "aws_sdk_braket.types.job_output_data_config.JobOutputDataConfig", job_name: str, role_arn: "aws_sdk_braket.types.role_arn.RoleArn", instance_config: "aws_sdk_braket.types.instance_config.InstanceConfig", device_config: "aws_sdk_braket.types.device_config.DeviceConfig", *, config_overrides: Optional[BraketClientConfig] = None, input_data_config: Optional["aws_sdk_braket.types.input_config_list.InputConfigList"] = None, checkpoint_config: Optional["aws_sdk_braket.types.job_checkpoint_config.JobCheckpointConfig"] = None, stopping_condition: Optional["aws_sdk_braket.types.job_stopping_condition.JobStoppingCondition"] = None, hyper_parameters: Optional["aws_sdk_braket.types.hyper_parameters.HyperParameters"] = None, tags: Optional["aws_sdk_braket.types.tags_map.TagsMap"] = None, associations: Optional["aws_sdk_braket.types.associations.Associations"] = None) -> "aws_sdk_braket.types.create_job_response.CreateJobResponse":
        """<p>Creates an Amazon Braket hybrid job.</p>

        Args:
            client_token: <p>The client token associated with this request that guarantees that the request is idempotent.</p>
            algorithm_specification: <p>Definition of the Amazon Braket job to be created. Specifies the container image the job uses and information about the Python scripts used for entry and training.</p>
            input_data_config: <p>A list of parameters that specify the name and type of input data and where it is located.</p>
            output_data_config: <p>The path to the S3 location where you want to store hybrid job artifacts and the encryption key used to store them.</p>
            checkpoint_config: <p>Information about the output locations for hybrid job checkpoint data.</p>
            job_name: <p>The name of the Amazon Braket hybrid job.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that Amazon Braket can assume to perform tasks on behalf of a user. It can access user resources, run an Amazon Braket job container on behalf of user, and output results and hybrid job details to the users' s3 buckets.</p>
            stopping_condition: <p> The user-defined criteria that specifies when a hybrid job stops running.</p>
            instance_config: <p>Configuration of the resource instances to use while running the hybrid job on Amazon Braket.</p>
            hyper_parameters: <p>Algorithm-specific parameters used by an Amazon Braket hybrid job that influence the quality of the training job. The values are set with a map of JSON key:value pairs, where the key is the name of the hyperparameter and the value is the value of the hyperparameter.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request hyperparameter variable or plain text fields.</p> </important>
            device_config: <p>The quantum processing unit (QPU) or simulator used to create an Amazon Braket hybrid job.</p>
            tags: <p>Tags to be added to the hybrid job you're creating.</p>
            associations: <p>The list of Amazon Braket resources associated with the hybrid job.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_braket.types.create_job_request.CreateJobRequest]') -> OperationResponse["aws_sdk_braket.types.create_job_response.CreateJobResponse"]:
            import aws_sdk_braket._operations.braket.create_job
            output, http_response = aws_sdk_braket._operations.braket.create_job.create_job(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.create_job_request.CreateJobRequest = {}  # type: ignore[typeddict-item]
        input["client_token"] = client_token
        input["algorithm_specification"] = algorithm_specification
        if input_data_config is not None:
            input["input_data_config"] = input_data_config
        input["output_data_config"] = output_data_config
        if checkpoint_config is not None:
            input["checkpoint_config"] = checkpoint_config
        input["job_name"] = job_name
        input["role_arn"] = role_arn
        if stopping_condition is not None:
            input["stopping_condition"] = stopping_condition
        input["instance_config"] = instance_config
        if hyper_parameters is not None:
            input["hyper_parameters"] = hyper_parameters
        input["device_config"] = device_config
        if tags is not None:
            input["tags"] = tags
        if associations is not None:
            input["associations"] = associations

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def read(self, job_arn: "aws_sdk_braket.types.job_arn.JobArn", *, config_overrides: Optional[BraketClientConfig] = None, additional_attribute_names: Optional["aws_sdk_braket.types.hybrid_job_additional_attribute_names_list.HybridJobAdditionalAttributeNamesList"] = None) -> "aws_sdk_braket.types.get_job_response.GetJobResponse":
        """<p>Retrieves the specified Amazon Braket hybrid job.</p>

        Args:
            job_arn: <p>The ARN of the hybrid job to retrieve.</p>
            additional_attribute_names: <p>A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported. </p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_braket.types.get_job_request.GetJobRequest]') -> OperationResponse["aws_sdk_braket.types.get_job_response.GetJobResponse"]:
            import aws_sdk_braket._operations.braket.get_job
            output, http_response = aws_sdk_braket._operations.braket.get_job.get_job(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.get_job_request.GetJobRequest = {}  # type: ignore[typeddict-item]
        input["job_arn"] = job_arn
        if additional_attribute_names is not None:
            input["additional_attribute_names"] = additional_attribute_names

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def update(self, job_arn: "aws_sdk_braket.types.job_arn.JobArn", *, config_overrides: Optional[BraketClientConfig] = None) -> "aws_sdk_braket.types.cancel_job_response.CancelJobResponse":
        """<p>Cancels an Amazon Braket hybrid job.</p>

        Args:
            job_arn: <p>The ARN of the Amazon Braket hybrid job to cancel.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_braket.types.cancel_job_request.CancelJobRequest]') -> OperationResponse["aws_sdk_braket.types.cancel_job_response.CancelJobResponse"]:
            import aws_sdk_braket._operations.braket.cancel_job
            output, http_response = aws_sdk_braket._operations.braket.cancel_job.cancel_job(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.cancel_job_request.CancelJobRequest = {}  # type: ignore[typeddict-item]
        input["job_arn"] = job_arn

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    def search_jobs(self, filters: "aws_sdk_braket.types.search_jobs_filter_list.SearchJobsFilterList", *, config_overrides: Optional[BraketClientConfig] = None, next_token: Optional[str] = None, max_results: Optional[int] = None) -> "aws_sdk_braket.types.search_jobs_response.SearchJobsResponse":
        """<p>Searches for Amazon Braket hybrid jobs that match the specified filter values.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            filters: <p>Array of SearchJobsFilter objects to use when searching for hybrid jobs.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_braket.types.search_jobs_request.SearchJobsRequest]') -> OperationResponse["aws_sdk_braket.types.search_jobs_response.SearchJobsResponse"]:
            import aws_sdk_braket._operations.braket.search_jobs
            output, http_response = aws_sdk_braket._operations.braket.search_jobs.search_jobs(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.search_jobs_request.SearchJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["filters"] = filters

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncJobResource:
    def __init__(self, service: AsyncBraketClient) -> None:
        self._service = service
    async def create(self, client_token: "aws_sdk_braket.types.string64.String64", algorithm_specification: "aws_sdk_braket.types.algorithm_specification.AlgorithmSpecification", output_data_config: "aws_sdk_braket.types.job_output_data_config.JobOutputDataConfig", job_name: str, role_arn: "aws_sdk_braket.types.role_arn.RoleArn", instance_config: "aws_sdk_braket.types.instance_config.InstanceConfig", device_config: "aws_sdk_braket.types.device_config.DeviceConfig", *, config_overrides: Optional[AsyncBraketClientConfig] = None, input_data_config: Optional["aws_sdk_braket.types.input_config_list.InputConfigList"] = None, checkpoint_config: Optional["aws_sdk_braket.types.job_checkpoint_config.JobCheckpointConfig"] = None, stopping_condition: Optional["aws_sdk_braket.types.job_stopping_condition.JobStoppingCondition"] = None, hyper_parameters: Optional["aws_sdk_braket.types.hyper_parameters.HyperParameters"] = None, tags: Optional["aws_sdk_braket.types.tags_map.TagsMap"] = None, associations: Optional["aws_sdk_braket.types.associations.Associations"] = None) -> "aws_sdk_braket.types.create_job_response.CreateJobResponse":
        """<p>Creates an Amazon Braket hybrid job.</p>

        Args:
            client_token: <p>The client token associated with this request that guarantees that the request is idempotent.</p>
            algorithm_specification: <p>Definition of the Amazon Braket job to be created. Specifies the container image the job uses and information about the Python scripts used for entry and training.</p>
            input_data_config: <p>A list of parameters that specify the name and type of input data and where it is located.</p>
            output_data_config: <p>The path to the S3 location where you want to store hybrid job artifacts and the encryption key used to store them.</p>
            checkpoint_config: <p>Information about the output locations for hybrid job checkpoint data.</p>
            job_name: <p>The name of the Amazon Braket hybrid job.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that Amazon Braket can assume to perform tasks on behalf of a user. It can access user resources, run an Amazon Braket job container on behalf of user, and output results and hybrid job details to the users' s3 buckets.</p>
            stopping_condition: <p> The user-defined criteria that specifies when a hybrid job stops running.</p>
            instance_config: <p>Configuration of the resource instances to use while running the hybrid job on Amazon Braket.</p>
            hyper_parameters: <p>Algorithm-specific parameters used by an Amazon Braket hybrid job that influence the quality of the training job. The values are set with a map of JSON key:value pairs, where the key is the name of the hyperparameter and the value is the value of the hyperparameter.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request hyperparameter variable or plain text fields.</p> </important>
            device_config: <p>The quantum processing unit (QPU) or simulator used to create an Amazon Braket hybrid job.</p>
            tags: <p>Tags to be added to the hybrid job you're creating.</p>
            associations: <p>The list of Amazon Braket resources associated with the hybrid job.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_braket.types.create_job_request.CreateJobRequest]') -> AsyncOperationResponse["aws_sdk_braket.types.create_job_response.CreateJobResponse"]:
            import aws_sdk_braket._operations.braket.create_job
            output, http_response = await aws_sdk_braket._operations.braket.create_job.async_create_job(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.create_job_request.CreateJobRequest = {}  # type: ignore[typeddict-item]
        input["client_token"] = client_token
        input["algorithm_specification"] = algorithm_specification
        if input_data_config is not None:
            input["input_data_config"] = input_data_config
        input["output_data_config"] = output_data_config
        if checkpoint_config is not None:
            input["checkpoint_config"] = checkpoint_config
        input["job_name"] = job_name
        input["role_arn"] = role_arn
        if stopping_condition is not None:
            input["stopping_condition"] = stopping_condition
        input["instance_config"] = instance_config
        if hyper_parameters is not None:
            input["hyper_parameters"] = hyper_parameters
        input["device_config"] = device_config
        if tags is not None:
            input["tags"] = tags
        if associations is not None:
            input["associations"] = associations

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def read(self, job_arn: "aws_sdk_braket.types.job_arn.JobArn", *, config_overrides: Optional[AsyncBraketClientConfig] = None, additional_attribute_names: Optional["aws_sdk_braket.types.hybrid_job_additional_attribute_names_list.HybridJobAdditionalAttributeNamesList"] = None) -> "aws_sdk_braket.types.get_job_response.GetJobResponse":
        """<p>Retrieves the specified Amazon Braket hybrid job.</p>

        Args:
            job_arn: <p>The ARN of the hybrid job to retrieve.</p>
            additional_attribute_names: <p>A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_braket.types.get_job_request.GetJobRequest]') -> AsyncOperationResponse["aws_sdk_braket.types.get_job_response.GetJobResponse"]:
            import aws_sdk_braket._operations.braket.get_job
            output, http_response = await aws_sdk_braket._operations.braket.get_job.async_get_job(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.get_job_request.GetJobRequest = {}  # type: ignore[typeddict-item]
        input["job_arn"] = job_arn
        if additional_attribute_names is not None:
            input["additional_attribute_names"] = additional_attribute_names

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update(self, job_arn: "aws_sdk_braket.types.job_arn.JobArn", *, config_overrides: Optional[AsyncBraketClientConfig] = None) -> "aws_sdk_braket.types.cancel_job_response.CancelJobResponse":
        """<p>Cancels an Amazon Braket hybrid job.</p>

        Args:
            job_arn: <p>The ARN of the Amazon Braket hybrid job to cancel.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_braket.types.cancel_job_request.CancelJobRequest]') -> AsyncOperationResponse["aws_sdk_braket.types.cancel_job_response.CancelJobResponse"]:
            import aws_sdk_braket._operations.braket.cancel_job
            output, http_response = await aws_sdk_braket._operations.braket.cancel_job.async_cancel_job(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.cancel_job_request.CancelJobRequest = {}  # type: ignore[typeddict-item]
        input["job_arn"] = job_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def search_jobs(self, filters: "aws_sdk_braket.types.search_jobs_filter_list.SearchJobsFilterList", *, config_overrides: Optional[AsyncBraketClientConfig] = None, next_token: Optional[str] = None, max_results: Optional[int] = None) -> "aws_sdk_braket.types.search_jobs_response.SearchJobsResponse":
        """<p>Searches for Amazon Braket hybrid jobs that match the specified filter values.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            filters: <p>Array of SearchJobsFilter objects to use when searching for hybrid jobs.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_braket.types.search_jobs_request.SearchJobsRequest]') -> AsyncOperationResponse["aws_sdk_braket.types.search_jobs_response.SearchJobsResponse"]:
            import aws_sdk_braket._operations.braket.search_jobs
            output, http_response = await aws_sdk_braket._operations.braket.search_jobs.async_search_jobs(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.search_jobs_request.SearchJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["filters"] = filters

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output