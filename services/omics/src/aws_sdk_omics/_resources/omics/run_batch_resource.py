from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_omics._auth._signers
import aws_sdk_omics._auth._sigv4
from aws_sdk_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_omics.types.batch_id
    import aws_sdk_omics.types.batch_list_item
    import aws_sdk_omics.types.batch_name
    import aws_sdk_omics.types.batch_request_id
    import aws_sdk_omics.types.batch_run_settings
    import aws_sdk_omics.types.batch_status
    import aws_sdk_omics.types.cancel_run_batch_request
    import aws_sdk_omics.types.cancel_run_batch_response
    import aws_sdk_omics.types.default_run_setting
    import aws_sdk_omics.types.delete_batch_request
    import aws_sdk_omics.types.delete_run_batch_request
    import aws_sdk_omics.types.delete_run_batch_response
    import aws_sdk_omics.types.get_batch_request
    import aws_sdk_omics.types.get_batch_response
    import aws_sdk_omics.types.list_batch_request
    import aws_sdk_omics.types.list_batch_response
    import aws_sdk_omics.types.list_runs_in_batch_request
    import aws_sdk_omics.types.list_runs_in_batch_response
    import aws_sdk_omics.types.list_token
    import aws_sdk_omics.types.run_batch_list_item
    import aws_sdk_omics.types.run_group_id
    import aws_sdk_omics.types.start_run_batch_request
    import aws_sdk_omics.types.start_run_batch_response
    import aws_sdk_omics.types.submission_status
    import aws_sdk_omics.types.tag_map
    from aws_sdk_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from aws_sdk_omics._services.omics import OmicsClient, OmicsClientConfig


class RunBatchResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        request_id: "aws_sdk_omics.types.batch_request_id.BatchRequestId",
        default_run_setting: "aws_sdk_omics.types.default_run_setting.DefaultRunSetting",
        batch_run_settings: "aws_sdk_omics.types.batch_run_settings.BatchRunSettings",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        batch_name: Optional["aws_sdk_omics.types.batch_name.BatchName"] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_omics.types.start_run_batch_response.StartRunBatchResponse":
        """<p>Starts a batch of workflow runs. You can group up to 100,000 runs into a single batch that share a common configuration defined in <code>defaultRunSetting</code>. Per-run overrides can be provided either inline via <code>inlineSettings</code> (up to 100 runs) or via a JSON file stored in Amazon S3 via <code>s3UriSettings</code> (up to 100,000 runs).</p> <p> <code>StartRunBatch</code> validates common fields synchronously and returns immediately with a batch ID and status <code>CREATING</code>. The batch transitions to <code>PENDING</code> once initial setup completes. Runs are then submitted gradually and asynchronously at a rate governed by your <code>StartRun</code> throughput quota.</p>

        Args:
            batch_name: <p>An optional user-friendly name for the run batch.</p>
            request_id: <p>A client token used to deduplicate retry requests and prevent duplicate batches from being created.</p>
            tags: <p>AWS tags to associate with the batch resource. These tags are not inherited by individual runs. To tag individual runs, use <code>defaultRunSetting.runTags</code>.</p>
            default_run_setting: <p>Shared configuration applied to all runs in the batch. See <code>DefaultRunSetting</code>.</p>
            batch_run_settings: <p>The individual run configurations. Specify exactly one of <code>inlineSettings</code> or <code>s3UriSettings</code>. See <code>BatchRunSettings</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.start_run_batch_request.StartRunBatchRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.start_run_batch_response.StartRunBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.start_run_batch

            output, http_response = (
                aws_sdk_omics._operations.omics.start_run_batch.start_run_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.start_run_batch_request.StartRunBatchRequest = {}  # type: ignore[typeddict-item]
        if batch_name is not None:
            input_["batch_name"] = batch_name
        input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags
        input_["default_run_setting"] = default_run_setting
        input_["batch_run_settings"] = batch_run_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        batch_id: "aws_sdk_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_batch_response.GetBatchResponse":
        """<p>Retrieves details and current status for a specific run batch, including submission progress and run execution counts.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.get_batch_request.GetBatchRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.get_batch_response.GetBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_batch

            output, http_response = aws_sdk_omics._operations.omics.get_batch.get_batch(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_batch_request.GetBatchRequest = {}  # type: ignore[typeddict-item]
        input_["batch_id"] = batch_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        batch_id: "aws_sdk_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run batch resource and its associated metadata. This operation does not delete the individual workflow runs. To delete the runs, call <code>DeleteRunBatch</code> before calling <code>DeleteBatch</code>.</p> <p> <code>DeleteBatch</code> requires the batch to be in a terminal state: <code>PROCESSED</code>, <code>FAILED</code>, <code>CANCELLED</code>, or <code>RUNS_DELETED</code>. After <code>DeleteBatch</code> completes, the batch metadata is no longer accessible. You cannot call <code>GetBatch</code>, <code>ListRunsInBatch</code>, <code>DeleteRunBatch</code>, or <code>CancelRunBatch</code> on a deleted batch.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.delete_batch_request.DeleteBatchRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_omics._operations.omics.delete_batch

            output, http_response = (
                aws_sdk_omics._operations.omics.delete_batch.delete_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_batch_request.DeleteBatchRequest = {}  # type: ignore[typeddict-item]
        input_["batch_id"] = batch_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_items: Optional[int] = None,
        starting_token: Optional["aws_sdk_omics.types.list_token.ListToken"] = None,
        status: Optional["aws_sdk_omics.types.batch_status.BatchStatus"] = None,
        name: Optional["aws_sdk_omics.types.batch_name.BatchName"] = None,
        run_group_id: Optional["aws_sdk_omics.types.run_group_id.RunGroupId"] = None,
    ) -> "aws_sdk_omics.types.list_batch_response.ListBatchResponse":
        """<p>Returns a list of run batches in your account, with optional filtering by status, name, or run group. Results are paginated. Only one filter per call is supported.</p>

        Args:
            max_items: <p>The maximum number of batches to return. If not specified, defaults to 100.</p>
            starting_token: <p>A pagination token returned from a prior <code>ListBatch</code> call.</p>
            status: <p>Filter batches by status.</p>
            name: <p>Filter batches by name.</p>
            run_group_id: <p>Filter batches by run group ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.list_batch_request.ListBatchRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.list_batch_response.ListBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_batch

            output, http_response = (
                aws_sdk_omics._operations.omics.list_batch.list_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_batch_request.ListBatchRequest = {}  # type: ignore[typeddict-item]
        if max_items is not None:
            input_["max_items"] = max_items
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if status is not None:
            input_["status"] = status
        if name is not None:
            input_["name"] = name
        if run_group_id is not None:
            input_["run_group_id"] = run_group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_run_batch(
        self,
        batch_id: "aws_sdk_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.cancel_run_batch_response.CancelRunBatchResponse":
        """<p>Cancels all runs within a specified batch. This operation prevents not-yet-submitted runs from starting and submits <code>CancelRun</code> requests for runs that have already started.</p> <p>Cancel is only allowed on batches in <code>PENDING</code>, <code>SUBMITTING</code>, or <code>INPROGRESS</code> state. Cancel operations are non-atomic and may be partially successful. Use <code>GetBatch</code> to review <code>successfulCancelSubmissionCount</code> and <code>failedCancelSubmissionCount</code> in the <code>submissionSummary</code>. Only one cancel or delete operation per batch is allowed at a time.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.cancel_run_batch_request.CancelRunBatchRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.cancel_run_batch_response.CancelRunBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.cancel_run_batch

            output, http_response = (
                aws_sdk_omics._operations.omics.cancel_run_batch.cancel_run_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.cancel_run_batch_request.CancelRunBatchRequest = {}  # type: ignore[typeddict-item]
        input_["batch_id"] = batch_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_run_batch(
        self,
        batch_id: "aws_sdk_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.delete_run_batch_response.DeleteRunBatchResponse":
        """<p>Deletes the individual workflow runs within a batch. This operation is separate from <code>DeleteBatch</code>, which removes the batch metadata.</p> <p>Delete is only allowed on batches in <code>PROCESSED</code> or <code>CANCELLED</code> state. Delete operations are non-atomic and may be partially successful. Use <code>GetBatch</code> to review <code>successfulDeleteSubmissionCount</code> and <code>failedDeleteSubmissionCount</code> in the <code>submissionSummary</code>. Only one cancel or delete operation per batch is allowed at a time.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.delete_run_batch_request.DeleteRunBatchRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.delete_run_batch_response.DeleteRunBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_run_batch

            output, http_response = (
                aws_sdk_omics._operations.omics.delete_run_batch.delete_run_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_run_batch_request.DeleteRunBatchRequest = {}  # type: ignore[typeddict-item]
        input_["batch_id"] = batch_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_runs_in_batch(
        self,
        batch_id: "aws_sdk_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_items: Optional[int] = None,
        starting_token: Optional["aws_sdk_omics.types.list_token.ListToken"] = None,
        submission_status: Optional[
            "aws_sdk_omics.types.submission_status.SubmissionStatus"
        ] = None,
        run_setting_id: Optional[str] = None,
        run_id: Optional[str] = None,
    ) -> "aws_sdk_omics.types.list_runs_in_batch_response.ListRunsInBatchResponse":
        """<p>Returns a paginated list of individual workflow runs within a specific batch. Use this operation to map each <code>runSettingId</code> to its HealthOmics-generated <code>runId</code>, and to check the submission status of each run. Only one filter per call is supported.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>
            max_items: <p>The maximum number of runs to return.</p>
            starting_token: <p>A pagination token returned from a prior <code>ListRunsInBatch</code> call.</p>
            submission_status: <p>Filter runs by submission status.</p>
            run_setting_id: <p>Filter runs by the customer-provided run setting ID.</p>
            run_id: <p>Filter runs by the HealthOmics-generated run ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.list_runs_in_batch_request.ListRunsInBatchRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.list_runs_in_batch_response.ListRunsInBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_runs_in_batch

            output, http_response = (
                aws_sdk_omics._operations.omics.list_runs_in_batch.list_runs_in_batch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_runs_in_batch_request.ListRunsInBatchRequest = {}  # type: ignore[typeddict-item]
        input_["batch_id"] = batch_id
        if max_items is not None:
            input_["max_items"] = max_items
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if submission_status is not None:
            input_["submission_status"] = submission_status
        if run_setting_id is not None:
            input_["run_setting_id"] = run_setting_id
        if run_id is not None:
            input_["run_id"] = run_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRunBatchResource:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        request_id: "aws_sdk_omics.types.batch_request_id.BatchRequestId",
        default_run_setting: "aws_sdk_omics.types.default_run_setting.DefaultRunSetting",
        batch_run_settings: "aws_sdk_omics.types.batch_run_settings.BatchRunSettings",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        batch_name: Optional["aws_sdk_omics.types.batch_name.BatchName"] = None,
        tags: Optional["aws_sdk_omics.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_omics.types.start_run_batch_response.StartRunBatchResponse":
        """<p>Starts a batch of workflow runs. You can group up to 100,000 runs into a single batch that share a common configuration defined in <code>defaultRunSetting</code>. Per-run overrides can be provided either inline via <code>inlineSettings</code> (up to 100 runs) or via a JSON file stored in Amazon S3 via <code>s3UriSettings</code> (up to 100,000 runs).</p> <p> <code>StartRunBatch</code> validates common fields synchronously and returns immediately with a batch ID and status <code>CREATING</code>. The batch transitions to <code>PENDING</code> once initial setup completes. Runs are then submitted gradually and asynchronously at a rate governed by your <code>StartRun</code> throughput quota.</p>

        Args:
            batch_name: <p>An optional user-friendly name for the run batch.</p>
            request_id: <p>A client token used to deduplicate retry requests and prevent duplicate batches from being created.</p>
            tags: <p>AWS tags to associate with the batch resource. These tags are not inherited by individual runs. To tag individual runs, use <code>defaultRunSetting.runTags</code>.</p>
            default_run_setting: <p>Shared configuration applied to all runs in the batch. See <code>DefaultRunSetting</code>.</p>
            batch_run_settings: <p>The individual run configurations. Specify exactly one of <code>inlineSettings</code> or <code>s3UriSettings</code>. See <code>BatchRunSettings</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.start_run_batch_request.StartRunBatchRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.start_run_batch_response.StartRunBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.start_run_batch

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.start_run_batch.async_start_run_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.start_run_batch_request.StartRunBatchRequest = {}  # type: ignore[typeddict-item]
        if batch_name is not None:
            input_["batch_name"] = batch_name
        input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags
        input_["default_run_setting"] = default_run_setting
        input_["batch_run_settings"] = batch_run_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        batch_id: "aws_sdk_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_batch_response.GetBatchResponse":
        """<p>Retrieves details and current status for a specific run batch, including submission progress and run execution counts.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.get_batch_request.GetBatchRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.get_batch_response.GetBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_batch

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.get_batch.async_get_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_batch_request.GetBatchRequest = {}  # type: ignore[typeddict-item]
        input_["batch_id"] = batch_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        batch_id: "aws_sdk_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run batch resource and its associated metadata. This operation does not delete the individual workflow runs. To delete the runs, call <code>DeleteRunBatch</code> before calling <code>DeleteBatch</code>.</p> <p> <code>DeleteBatch</code> requires the batch to be in a terminal state: <code>PROCESSED</code>, <code>FAILED</code>, <code>CANCELLED</code>, or <code>RUNS_DELETED</code>. After <code>DeleteBatch</code> completes, the batch metadata is no longer accessible. You cannot call <code>GetBatch</code>, <code>ListRunsInBatch</code>, <code>DeleteRunBatch</code>, or <code>CancelRunBatch</code> on a deleted batch.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.delete_batch_request.DeleteBatchRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_omics._operations.omics.delete_batch

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.delete_batch.async_delete_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_batch_request.DeleteBatchRequest = {}  # type: ignore[typeddict-item]
        input_["batch_id"] = batch_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_items: Optional[int] = None,
        starting_token: Optional["aws_sdk_omics.types.list_token.ListToken"] = None,
        status: Optional["aws_sdk_omics.types.batch_status.BatchStatus"] = None,
        name: Optional["aws_sdk_omics.types.batch_name.BatchName"] = None,
        run_group_id: Optional["aws_sdk_omics.types.run_group_id.RunGroupId"] = None,
    ) -> "aws_sdk_omics.types.list_batch_response.ListBatchResponse":
        """<p>Returns a list of run batches in your account, with optional filtering by status, name, or run group. Results are paginated. Only one filter per call is supported.</p>

        Args:
            max_items: <p>The maximum number of batches to return. If not specified, defaults to 100.</p>
            starting_token: <p>A pagination token returned from a prior <code>ListBatch</code> call.</p>
            status: <p>Filter batches by status.</p>
            name: <p>Filter batches by name.</p>
            run_group_id: <p>Filter batches by run group ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.list_batch_request.ListBatchRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.list_batch_response.ListBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_batch

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.list_batch.async_list_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_batch_request.ListBatchRequest = {}  # type: ignore[typeddict-item]
        if max_items is not None:
            input_["max_items"] = max_items
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if status is not None:
            input_["status"] = status
        if name is not None:
            input_["name"] = name
        if run_group_id is not None:
            input_["run_group_id"] = run_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_run_batch(
        self,
        batch_id: "aws_sdk_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.cancel_run_batch_response.CancelRunBatchResponse":
        """<p>Cancels all runs within a specified batch. This operation prevents not-yet-submitted runs from starting and submits <code>CancelRun</code> requests for runs that have already started.</p> <p>Cancel is only allowed on batches in <code>PENDING</code>, <code>SUBMITTING</code>, or <code>INPROGRESS</code> state. Cancel operations are non-atomic and may be partially successful. Use <code>GetBatch</code> to review <code>successfulCancelSubmissionCount</code> and <code>failedCancelSubmissionCount</code> in the <code>submissionSummary</code>. Only one cancel or delete operation per batch is allowed at a time.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.cancel_run_batch_request.CancelRunBatchRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.cancel_run_batch_response.CancelRunBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.cancel_run_batch

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.cancel_run_batch.async_cancel_run_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.cancel_run_batch_request.CancelRunBatchRequest = {}  # type: ignore[typeddict-item]
        input_["batch_id"] = batch_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_run_batch(
        self,
        batch_id: "aws_sdk_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.delete_run_batch_response.DeleteRunBatchResponse":
        """<p>Deletes the individual workflow runs within a batch. This operation is separate from <code>DeleteBatch</code>, which removes the batch metadata.</p> <p>Delete is only allowed on batches in <code>PROCESSED</code> or <code>CANCELLED</code> state. Delete operations are non-atomic and may be partially successful. Use <code>GetBatch</code> to review <code>successfulDeleteSubmissionCount</code> and <code>failedDeleteSubmissionCount</code> in the <code>submissionSummary</code>. Only one cancel or delete operation per batch is allowed at a time.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.delete_run_batch_request.DeleteRunBatchRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.delete_run_batch_response.DeleteRunBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_run_batch

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.delete_run_batch.async_delete_run_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_run_batch_request.DeleteRunBatchRequest = {}  # type: ignore[typeddict-item]
        input_["batch_id"] = batch_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_runs_in_batch(
        self,
        batch_id: "aws_sdk_omics.types.batch_id.BatchId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_items: Optional[int] = None,
        starting_token: Optional["aws_sdk_omics.types.list_token.ListToken"] = None,
        submission_status: Optional[
            "aws_sdk_omics.types.submission_status.SubmissionStatus"
        ] = None,
        run_setting_id: Optional[str] = None,
        run_id: Optional[str] = None,
    ) -> "aws_sdk_omics.types.list_runs_in_batch_response.ListRunsInBatchResponse":
        """<p>Returns a paginated list of individual workflow runs within a specific batch. Use this operation to map each <code>runSettingId</code> to its HealthOmics-generated <code>runId</code>, and to check the submission status of each run. Only one filter per call is supported.</p>

        Args:
            batch_id: <p>The identifier portion of the run batch ARN.</p>
            max_items: <p>The maximum number of runs to return.</p>
            starting_token: <p>A pagination token returned from a prior <code>ListRunsInBatch</code> call.</p>
            submission_status: <p>Filter runs by submission status.</p>
            run_setting_id: <p>Filter runs by the customer-provided run setting ID.</p>
            run_id: <p>Filter runs by the HealthOmics-generated run ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.list_runs_in_batch_request.ListRunsInBatchRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.list_runs_in_batch_response.ListRunsInBatchResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_runs_in_batch

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.list_runs_in_batch.async_list_runs_in_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_runs_in_batch_request.ListRunsInBatchRequest = {}  # type: ignore[typeddict-item]
        input_["batch_id"] = batch_id
        if max_items is not None:
            input_["max_items"] = max_items
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if submission_status is not None:
            input_["submission_status"] = submission_status
        if run_setting_id is not None:
            input_["run_setting_id"] = run_setting_id
        if run_id is not None:
            input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
