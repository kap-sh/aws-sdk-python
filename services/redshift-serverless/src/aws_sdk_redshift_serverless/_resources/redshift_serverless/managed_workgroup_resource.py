from typing import TYPE_CHECKING, Optional

from aws_sdk_redshift_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.list_managed_workgroups_request
    import aws_sdk_redshift_serverless.types.list_managed_workgroups_response
    import aws_sdk_redshift_serverless.types.managed_workgroup_list_item
    import aws_sdk_redshift_serverless.types.pagination_token
    import aws_sdk_redshift_serverless.types.source_arn
    from aws_sdk_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from aws_sdk_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class ManagedWorkgroupResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def list_managed_workgroups(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        source_arn: Optional[
            "aws_sdk_redshift_serverless.types.source_arn.SourceArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_managed_workgroups_response.ListManagedWorkgroupsResponse":
        """<p>Returns information about a list of specified managed workgroups in your account.</p>

        Args:
            source_arn: <p>The Amazon Resource Name (ARN) for the managed workgroup in the Glue Data Catalog.</p>
            next_token: <p>If your initial ListManagedWorkgroups operation returns a nextToken, you can include the returned nextToken in following ListManagedWorkgroups operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.list_managed_workgroups_request.ListManagedWorkgroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.list_managed_workgroups_response.ListManagedWorkgroupsResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_managed_workgroups

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.list_managed_workgroups.list_managed_workgroups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_managed_workgroups_request.ListManagedWorkgroupsRequest = {}  # type: ignore[typeddict-item]
        if source_arn is not None:
            input_["source_arn"] = source_arn
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


class AsyncManagedWorkgroupResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def list_managed_workgroups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        source_arn: Optional[
            "aws_sdk_redshift_serverless.types.source_arn.SourceArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_managed_workgroups_response.ListManagedWorkgroupsResponse":
        """<p>Returns information about a list of specified managed workgroups in your account.</p>

        Args:
            source_arn: <p>The Amazon Resource Name (ARN) for the managed workgroup in the Glue Data Catalog.</p>
            next_token: <p>If your initial ListManagedWorkgroups operation returns a nextToken, you can include the returned nextToken in following ListManagedWorkgroups operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.list_managed_workgroups_request.ListManagedWorkgroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.list_managed_workgroups_response.ListManagedWorkgroupsResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_managed_workgroups

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.list_managed_workgroups.async_list_managed_workgroups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_managed_workgroups_request.ListManagedWorkgroupsRequest = {}  # type: ignore[typeddict-item]
        if source_arn is not None:
            input_["source_arn"] = source_arn
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
