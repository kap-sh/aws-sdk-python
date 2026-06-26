from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_launch_wizard._auth._signers
import aws_sdk_launch_wizard._auth._sigv4
from aws_sdk_launch_wizard._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.get_workload_input
    import aws_sdk_launch_wizard.types.get_workload_output
    import aws_sdk_launch_wizard.types.list_workloads_input
    import aws_sdk_launch_wizard.types.list_workloads_output
    import aws_sdk_launch_wizard.types.max_workload_results
    import aws_sdk_launch_wizard.types.next_token
    import aws_sdk_launch_wizard.types.workload_data_summary
    import aws_sdk_launch_wizard.types.workload_name
    from aws_sdk_launch_wizard._services.async_launch_wizard import (
        AsyncLaunchWizardClient,
        AsyncLaunchWizardClientConfig,
    )
    from aws_sdk_launch_wizard._services.launch_wizard import (
        LaunchWizardClient,
        LaunchWizardClientConfig,
    )


class Workload:
    def __init__(self, service: LaunchWizardClient) -> None:
        self._service = service

    def read(
        self,
        workload_name: "aws_sdk_launch_wizard.types.workload_name.WorkloadName",
        *,
        config_overrides: Optional[LaunchWizardClientConfig] = None,
    ) -> "aws_sdk_launch_wizard.types.get_workload_output.GetWorkloadOutput":
        """<p>Returns information about a workload.</p>

        Args:
            workload_name: <p>The name of the workload.</p>

        Raises:
            aws_sdk_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href=\"https://repost.aws/\">re:Post</a>.</p>
            aws_sdk_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            aws_sdk_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get details about a specific workload.

            >>> client.read(workload_name='SAP')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_launch_wizard.types.get_workload_input.GetWorkloadInput]",
        ) -> OperationResponse[
            "aws_sdk_launch_wizard.types.get_workload_output.GetWorkloadOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.get_workload

            output, http_response = (
                aws_sdk_launch_wizard._operations.launch_wizard.get_workload.get_workload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.get_workload_input.GetWorkloadInput = {}  # type: ignore[typeddict-item]
        input_["workload_name"] = workload_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[LaunchWizardClientConfig] = None,
        max_results: Optional[
            "aws_sdk_launch_wizard.types.max_workload_results.MaxWorkloadResults"
        ] = None,
        next_token: Optional["aws_sdk_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_launch_wizard.types.list_workloads_output.ListWorkloadsOutput":
        r"""<p>Lists the available workload names. You can use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html\">ListWorkloadDeploymentPatterns</a> operation to discover the available deployment patterns for a given workload.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            aws_sdk_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href=\"https://repost.aws/\">re:Post</a>.</p>
            aws_sdk_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all available workloads supported by AWS Launch Wizard.

            >>> client.list()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_launch_wizard.types.list_workloads_input.ListWorkloadsInput]",
        ) -> OperationResponse[
            "aws_sdk_launch_wizard.types.list_workloads_output.ListWorkloadsOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.list_workloads

            output, http_response = (
                aws_sdk_launch_wizard._operations.launch_wizard.list_workloads.list_workloads(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.list_workloads_input.ListWorkloadsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncWorkload:
    def __init__(self, service: AsyncLaunchWizardClient) -> None:
        self._service = service

    async def read(
        self,
        workload_name: "aws_sdk_launch_wizard.types.workload_name.WorkloadName",
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
    ) -> "aws_sdk_launch_wizard.types.get_workload_output.GetWorkloadOutput":
        """<p>Returns information about a workload.</p>

        Args:
            workload_name: <p>The name of the workload.</p>

        Raises:
            aws_sdk_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href=\"https://repost.aws/\">re:Post</a>.</p>
            aws_sdk_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            aws_sdk_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get details about a specific workload.

            >>> await client.read(workload_name='SAP')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_launch_wizard.types.get_workload_input.GetWorkloadInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_launch_wizard.types.get_workload_output.GetWorkloadOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.get_workload

            (
                output,
                http_response,
            ) = await aws_sdk_launch_wizard._operations.launch_wizard.get_workload.async_get_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.get_workload_input.GetWorkloadInput = {}  # type: ignore[typeddict-item]
        input_["workload_name"] = workload_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncLaunchWizardClientConfig] = None,
        max_results: Optional[
            "aws_sdk_launch_wizard.types.max_workload_results.MaxWorkloadResults"
        ] = None,
        next_token: Optional["aws_sdk_launch_wizard.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_launch_wizard.types.list_workloads_output.ListWorkloadsOutput":
        r"""<p>Lists the available workload names. You can use the <a href=\"https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html\">ListWorkloadDeploymentPatterns</a> operation to discover the available deployment patterns for a given workload.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            aws_sdk_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href=\"https://repost.aws/\">re:Post</a>.</p>
            aws_sdk_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List all available workloads supported by AWS Launch Wizard.

            >>> await client.list()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_launch_wizard.types.list_workloads_input.ListWorkloadsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_launch_wizard.types.list_workloads_output.ListWorkloadsOutput"
        ]:
            import aws_sdk_launch_wizard._operations.launch_wizard.list_workloads

            (
                output,
                http_response,
            ) = await aws_sdk_launch_wizard._operations.launch_wizard.list_workloads.async_list_workloads(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_launch_wizard.types.list_workloads_input.ListWorkloadsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
