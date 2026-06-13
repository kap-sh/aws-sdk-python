from typing import TYPE_CHECKING, Optional

import aws_sdk_braket._auth._signers
import aws_sdk_braket._auth._sigv4
from aws_sdk_braket._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_braket.types.associations
    import aws_sdk_braket.types.cancel_quantum_task_request
    import aws_sdk_braket.types.cancel_quantum_task_response
    import aws_sdk_braket.types.create_quantum_task_request
    import aws_sdk_braket.types.create_quantum_task_response
    import aws_sdk_braket.types.device_arn
    import aws_sdk_braket.types.experimental_capabilities
    import aws_sdk_braket.types.get_quantum_task_request
    import aws_sdk_braket.types.get_quantum_task_response
    import aws_sdk_braket.types.job_token
    import aws_sdk_braket.types.json_value
    import aws_sdk_braket.types.quantum_task_additional_attribute_names_list
    import aws_sdk_braket.types.quantum_task_arn
    import aws_sdk_braket.types.quantum_task_summary
    import aws_sdk_braket.types.search_quantum_tasks_filter_list
    import aws_sdk_braket.types.search_quantum_tasks_request
    import aws_sdk_braket.types.search_quantum_tasks_response
    import aws_sdk_braket.types.string64
    import aws_sdk_braket.types.tags_map
    from aws_sdk_braket._services.async_braket import (
        AsyncBraketClient,
        AsyncBraketClientConfig,
    )
    from aws_sdk_braket._services.braket import BraketClient, BraketClientConfig


class QuantumTaskResource:
    def __init__(self, service: BraketClient) -> None:
        self._service = service

    def create(
        self,
        client_token: "aws_sdk_braket.types.string64.String64",
        device_arn: "aws_sdk_braket.types.device_arn.DeviceArn",
        shots: int,
        output_s3_bucket: str,
        output_s3_key_prefix: str,
        action: "aws_sdk_braket.types.json_value.JsonValue",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
        device_parameters: Optional["aws_sdk_braket.types.json_value.JsonValue"] = None,
        tags: Optional["aws_sdk_braket.types.tags_map.TagsMap"] = None,
        job_token: Optional["aws_sdk_braket.types.job_token.JobToken"] = None,
        associations: Optional["aws_sdk_braket.types.associations.Associations"] = None,
        experimental_capabilities: Optional[
            "aws_sdk_braket.types.experimental_capabilities.ExperimentalCapabilities"
        ] = None,
    ) -> "aws_sdk_braket.types.create_quantum_task_response.CreateQuantumTaskResponse":
        """<p>Creates a quantum task.</p>

        Args:
            client_token: <p>The client token associated with the request.</p>
            device_arn: <p>The ARN of the device to run the quantum task on.</p>
            device_parameters: <p>The parameters for the device to run the quantum task on.</p>
            shots: <p>The number of shots to use for the quantum task.</p>
            output_s3_bucket: <p>The S3 bucket to store quantum task result files in.</p>
            output_s3_key_prefix: <p>The key prefix for the location in the S3 bucket to store quantum task results in.</p>
            action: <p>The action associated with the quantum task.</p>
            tags: <p>Tags to be added to the quantum task you're creating.</p>
            job_token: <p>The token for an Amazon Braket hybrid job that associates it with the quantum task.</p>
            associations: <p>The list of Amazon Braket resources associated with the quantum task.</p>
            experimental_capabilities: <p>Enable experimental capabilities for the quantum task.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_braket.types.create_quantum_task_request.CreateQuantumTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_braket.types.create_quantum_task_response.CreateQuantumTaskResponse"
        ]:
            import aws_sdk_braket._operations.braket.create_quantum_task

            output, http_response = (
                aws_sdk_braket._operations.braket.create_quantum_task.create_quantum_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.create_quantum_task_request.CreateQuantumTaskRequest = {}  # type: ignore[typeddict-item]
        input["client_token"] = client_token
        input["device_arn"] = device_arn
        if device_parameters is not None:
            input["device_parameters"] = device_parameters
        input["shots"] = shots
        input["output_s3_bucket"] = output_s3_bucket
        input["output_s3_key_prefix"] = output_s3_key_prefix
        input["action"] = action
        if tags is not None:
            input["tags"] = tags
        if job_token is not None:
            input["job_token"] = job_token
        if associations is not None:
            input["associations"] = associations
        if experimental_capabilities is not None:
            input["experimental_capabilities"] = experimental_capabilities

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        quantum_task_arn: "aws_sdk_braket.types.quantum_task_arn.QuantumTaskArn",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
        additional_attribute_names: Optional[
            "aws_sdk_braket.types.quantum_task_additional_attribute_names_list.QuantumTaskAdditionalAttributeNamesList"
        ] = None,
    ) -> "aws_sdk_braket.types.get_quantum_task_response.GetQuantumTaskResponse":
        """<p>Retrieves the specified quantum task.</p>

        Args:
            quantum_task_arn: <p>The ARN of the quantum task to retrieve.</p>
            additional_attribute_names: <p>A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_braket.types.get_quantum_task_request.GetQuantumTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_braket.types.get_quantum_task_response.GetQuantumTaskResponse"
        ]:
            import aws_sdk_braket._operations.braket.get_quantum_task

            output, http_response = (
                aws_sdk_braket._operations.braket.get_quantum_task.get_quantum_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.get_quantum_task_request.GetQuantumTaskRequest = {}  # type: ignore[typeddict-item]
        input["quantum_task_arn"] = quantum_task_arn
        if additional_attribute_names is not None:
            input["additional_attribute_names"] = additional_attribute_names

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        quantum_task_arn: "aws_sdk_braket.types.quantum_task_arn.QuantumTaskArn",
        client_token: "aws_sdk_braket.types.string64.String64",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
    ) -> "aws_sdk_braket.types.cancel_quantum_task_response.CancelQuantumTaskResponse":
        """<p>Cancels the specified task.</p>

        Args:
            quantum_task_arn: <p>The ARN of the quantum task to cancel.</p>
            client_token: <p>The client token associated with the cancellation request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_braket.types.cancel_quantum_task_request.CancelQuantumTaskRequest]",
        ) -> OperationResponse[
            "aws_sdk_braket.types.cancel_quantum_task_response.CancelQuantumTaskResponse"
        ]:
            import aws_sdk_braket._operations.braket.cancel_quantum_task

            output, http_response = (
                aws_sdk_braket._operations.braket.cancel_quantum_task.cancel_quantum_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.cancel_quantum_task_request.CancelQuantumTaskRequest = {}  # type: ignore[typeddict-item]
        input["quantum_task_arn"] = quantum_task_arn
        input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        filters: "aws_sdk_braket.types.search_quantum_tasks_filter_list.SearchQuantumTasksFilterList",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "aws_sdk_braket.types.search_quantum_tasks_response.SearchQuantumTasksResponse"
    ):
        """<p>Searches for tasks that match the specified filter values.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>Maximum number of results to return in the response.</p>
            filters: <p>Array of <code>SearchQuantumTasksFilter</code> objects to use when searching for quantum tasks.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_braket.types.search_quantum_tasks_request.SearchQuantumTasksRequest]",
        ) -> OperationResponse[
            "aws_sdk_braket.types.search_quantum_tasks_response.SearchQuantumTasksResponse"
        ]:
            import aws_sdk_braket._operations.braket.search_quantum_tasks

            output, http_response = (
                aws_sdk_braket._operations.braket.search_quantum_tasks.search_quantum_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.search_quantum_tasks_request.SearchQuantumTasksRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncQuantumTaskResource:
    def __init__(self, service: AsyncBraketClient) -> None:
        self._service = service

    async def create(
        self,
        client_token: "aws_sdk_braket.types.string64.String64",
        device_arn: "aws_sdk_braket.types.device_arn.DeviceArn",
        shots: int,
        output_s3_bucket: str,
        output_s3_key_prefix: str,
        action: "aws_sdk_braket.types.json_value.JsonValue",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        device_parameters: Optional["aws_sdk_braket.types.json_value.JsonValue"] = None,
        tags: Optional["aws_sdk_braket.types.tags_map.TagsMap"] = None,
        job_token: Optional["aws_sdk_braket.types.job_token.JobToken"] = None,
        associations: Optional["aws_sdk_braket.types.associations.Associations"] = None,
        experimental_capabilities: Optional[
            "aws_sdk_braket.types.experimental_capabilities.ExperimentalCapabilities"
        ] = None,
    ) -> "aws_sdk_braket.types.create_quantum_task_response.CreateQuantumTaskResponse":
        """<p>Creates a quantum task.</p>

        Args:
            client_token: <p>The client token associated with the request.</p>
            device_arn: <p>The ARN of the device to run the quantum task on.</p>
            device_parameters: <p>The parameters for the device to run the quantum task on.</p>
            shots: <p>The number of shots to use for the quantum task.</p>
            output_s3_bucket: <p>The S3 bucket to store quantum task result files in.</p>
            output_s3_key_prefix: <p>The key prefix for the location in the S3 bucket to store quantum task results in.</p>
            action: <p>The action associated with the quantum task.</p>
            tags: <p>Tags to be added to the quantum task you're creating.</p>
            job_token: <p>The token for an Amazon Braket hybrid job that associates it with the quantum task.</p>
            associations: <p>The list of Amazon Braket resources associated with the quantum task.</p>
            experimental_capabilities: <p>Enable experimental capabilities for the quantum task.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_braket.types.create_quantum_task_request.CreateQuantumTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_braket.types.create_quantum_task_response.CreateQuantumTaskResponse"
        ]:
            import aws_sdk_braket._operations.braket.create_quantum_task

            (
                output,
                http_response,
            ) = await aws_sdk_braket._operations.braket.create_quantum_task.async_create_quantum_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.create_quantum_task_request.CreateQuantumTaskRequest = {}  # type: ignore[typeddict-item]
        input["client_token"] = client_token
        input["device_arn"] = device_arn
        if device_parameters is not None:
            input["device_parameters"] = device_parameters
        input["shots"] = shots
        input["output_s3_bucket"] = output_s3_bucket
        input["output_s3_key_prefix"] = output_s3_key_prefix
        input["action"] = action
        if tags is not None:
            input["tags"] = tags
        if job_token is not None:
            input["job_token"] = job_token
        if associations is not None:
            input["associations"] = associations
        if experimental_capabilities is not None:
            input["experimental_capabilities"] = experimental_capabilities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        quantum_task_arn: "aws_sdk_braket.types.quantum_task_arn.QuantumTaskArn",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        additional_attribute_names: Optional[
            "aws_sdk_braket.types.quantum_task_additional_attribute_names_list.QuantumTaskAdditionalAttributeNamesList"
        ] = None,
    ) -> "aws_sdk_braket.types.get_quantum_task_response.GetQuantumTaskResponse":
        """<p>Retrieves the specified quantum task.</p>

        Args:
            quantum_task_arn: <p>The ARN of the quantum task to retrieve.</p>
            additional_attribute_names: <p>A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_braket.types.get_quantum_task_request.GetQuantumTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_braket.types.get_quantum_task_response.GetQuantumTaskResponse"
        ]:
            import aws_sdk_braket._operations.braket.get_quantum_task

            (
                output,
                http_response,
            ) = await aws_sdk_braket._operations.braket.get_quantum_task.async_get_quantum_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.get_quantum_task_request.GetQuantumTaskRequest = {}  # type: ignore[typeddict-item]
        input["quantum_task_arn"] = quantum_task_arn
        if additional_attribute_names is not None:
            input["additional_attribute_names"] = additional_attribute_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        quantum_task_arn: "aws_sdk_braket.types.quantum_task_arn.QuantumTaskArn",
        client_token: "aws_sdk_braket.types.string64.String64",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "aws_sdk_braket.types.cancel_quantum_task_response.CancelQuantumTaskResponse":
        """<p>Cancels the specified task.</p>

        Args:
            quantum_task_arn: <p>The ARN of the quantum task to cancel.</p>
            client_token: <p>The client token associated with the cancellation request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_braket.types.cancel_quantum_task_request.CancelQuantumTaskRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_braket.types.cancel_quantum_task_response.CancelQuantumTaskResponse"
        ]:
            import aws_sdk_braket._operations.braket.cancel_quantum_task

            (
                output,
                http_response,
            ) = await aws_sdk_braket._operations.braket.cancel_quantum_task.async_cancel_quantum_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.cancel_quantum_task_request.CancelQuantumTaskRequest = {}  # type: ignore[typeddict-item]
        input["quantum_task_arn"] = quantum_task_arn
        input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        filters: "aws_sdk_braket.types.search_quantum_tasks_filter_list.SearchQuantumTasksFilterList",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "aws_sdk_braket.types.search_quantum_tasks_response.SearchQuantumTasksResponse"
    ):
        """<p>Searches for tasks that match the specified filter values.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>Maximum number of results to return in the response.</p>
            filters: <p>Array of <code>SearchQuantumTasksFilter</code> objects to use when searching for quantum tasks.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_braket.types.search_quantum_tasks_request.SearchQuantumTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_braket.types.search_quantum_tasks_response.SearchQuantumTasksResponse"
        ]:
            import aws_sdk_braket._operations.braket.search_quantum_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_braket._operations.braket.search_quantum_tasks.async_search_quantum_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_braket.types.search_quantum_tasks_request.SearchQuantumTasksRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        input["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
