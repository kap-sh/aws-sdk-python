from __future__ import annotations

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
    import aws_sdk_redshift_serverless.types.create_usage_limit_request
    import aws_sdk_redshift_serverless.types.create_usage_limit_response
    import aws_sdk_redshift_serverless.types.delete_usage_limit_request
    import aws_sdk_redshift_serverless.types.delete_usage_limit_response
    import aws_sdk_redshift_serverless.types.get_usage_limit_request
    import aws_sdk_redshift_serverless.types.get_usage_limit_response
    import aws_sdk_redshift_serverless.types.list_usage_limits_request
    import aws_sdk_redshift_serverless.types.list_usage_limits_response
    import aws_sdk_redshift_serverless.types.pagination_token
    import aws_sdk_redshift_serverless.types.update_usage_limit_request
    import aws_sdk_redshift_serverless.types.update_usage_limit_response
    import aws_sdk_redshift_serverless.types.usage_limit
    import aws_sdk_redshift_serverless.types.usage_limit_breach_action
    import aws_sdk_redshift_serverless.types.usage_limit_period
    import aws_sdk_redshift_serverless.types.usage_limit_usage_type
    from aws_sdk_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from aws_sdk_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class UsageLimitResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def create_usage_limit(
        self,
        resource_arn: str,
        usage_type: "aws_sdk_redshift_serverless.types.usage_limit_usage_type.UsageLimitUsageType",
        amount: int,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        period: Optional[
            "aws_sdk_redshift_serverless.types.usage_limit_period.UsageLimitPeriod"
        ] = None,
        breach_action: Optional[
            "aws_sdk_redshift_serverless.types.usage_limit_breach_action.UsageLimitBreachAction"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.create_usage_limit_response.CreateUsageLimitResponse":
        """<p>Creates a usage limit for a specified Amazon Redshift Serverless usage type. The usage limit is identified by the returned usage limit identifier. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Redshift Serverless resource to create the usage limit for.</p>
            usage_type: <p>The type of Amazon Redshift Serverless usage to create a usage limit for.</p>
            amount: <p>The limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.</p>
            period: <p>The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly.</p>
            breach_action: <p>The action that Amazon Redshift Serverless takes when the limit is reached. The default is log.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.create_usage_limit_request.CreateUsageLimitRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.create_usage_limit_response.CreateUsageLimitResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.create_usage_limit

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.create_usage_limit.create_usage_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.create_usage_limit_request.CreateUsageLimitRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["usage_type"] = usage_type
        input_["amount"] = amount
        if period is not None:
            input_["period"] = period
        if breach_action is not None:
            input_["breach_action"] = breach_action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_usage_limit(
        self,
        usage_limit_id: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_usage_limit_response.DeleteUsageLimitResponse":
        """<p>Deletes a usage limit from Amazon Redshift Serverless.</p>

        Args:
            usage_limit_id: <p>The unique identifier of the usage limit to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.delete_usage_limit_request.DeleteUsageLimitRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.delete_usage_limit_response.DeleteUsageLimitResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_usage_limit

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.delete_usage_limit.delete_usage_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_usage_limit_request.DeleteUsageLimitRequest = {}  # type: ignore[typeddict-item]
        input_["usage_limit_id"] = usage_limit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_usage_limit(
        self,
        usage_limit_id: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_usage_limit_response.GetUsageLimitResponse":
        """<p>Returns information about a usage limit.</p>

        Args:
            usage_limit_id: <p>The unique identifier of the usage limit to return information for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.get_usage_limit_request.GetUsageLimitRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.get_usage_limit_response.GetUsageLimitResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_usage_limit

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.get_usage_limit.get_usage_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_usage_limit_request.GetUsageLimitRequest = {}  # type: ignore[typeddict-item]
        input_["usage_limit_id"] = usage_limit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_usage_limits(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        resource_arn: Optional[str] = None,
        usage_type: Optional[
            "aws_sdk_redshift_serverless.types.usage_limit_usage_type.UsageLimitUsageType"
        ] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_usage_limits_response.ListUsageLimitsResponse":
        """<p>Lists all usage limits within Amazon Redshift Serverless.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource whose usage limits you want to list.</p>
            usage_type: <p>The Amazon Redshift Serverless feature whose limits you want to see.</p>
            next_token: <p>If your initial <code>ListUsageLimits</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListUsageLimits</code> operations, which returns results in the next page. </p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 100.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.list_usage_limits_request.ListUsageLimitsRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.list_usage_limits_response.ListUsageLimitsResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_usage_limits

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.list_usage_limits.list_usage_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_usage_limits_request.ListUsageLimitsRequest = {}  # type: ignore[typeddict-item]
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if usage_type is not None:
            input_["usage_type"] = usage_type
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

    def update_usage_limit(
        self,
        usage_limit_id: str,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        amount: Optional[int] = None,
        breach_action: Optional[
            "aws_sdk_redshift_serverless.types.usage_limit_breach_action.UsageLimitBreachAction"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_usage_limit_response.UpdateUsageLimitResponse":
        """<p>Update a usage limit in Amazon Redshift Serverless. You can't update the usage type or period of a usage limit.</p>

        Args:
            usage_limit_id: <p>The identifier of the usage limit to update.</p>
            amount: <p>The new limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.</p>
            breach_action: <p>The new action that Amazon Redshift Serverless takes when the limit is reached.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_redshift_serverless.types.update_usage_limit_request.UpdateUsageLimitRequest]",
        ) -> OperationResponse[
            "aws_sdk_redshift_serverless.types.update_usage_limit_response.UpdateUsageLimitResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_usage_limit

            output, http_response = (
                aws_sdk_redshift_serverless._operations.redshift_serverless.update_usage_limit.update_usage_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_usage_limit_request.UpdateUsageLimitRequest = {}  # type: ignore[typeddict-item]
        input_["usage_limit_id"] = usage_limit_id
        if amount is not None:
            input_["amount"] = amount
        if breach_action is not None:
            input_["breach_action"] = breach_action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncUsageLimitResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def create_usage_limit(
        self,
        resource_arn: str,
        usage_type: "aws_sdk_redshift_serverless.types.usage_limit_usage_type.UsageLimitUsageType",
        amount: int,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        period: Optional[
            "aws_sdk_redshift_serverless.types.usage_limit_period.UsageLimitPeriod"
        ] = None,
        breach_action: Optional[
            "aws_sdk_redshift_serverless.types.usage_limit_breach_action.UsageLimitBreachAction"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.create_usage_limit_response.CreateUsageLimitResponse":
        """<p>Creates a usage limit for a specified Amazon Redshift Serverless usage type. The usage limit is identified by the returned usage limit identifier. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Redshift Serverless resource to create the usage limit for.</p>
            usage_type: <p>The type of Amazon Redshift Serverless usage to create a usage limit for.</p>
            amount: <p>The limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.</p>
            period: <p>The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly.</p>
            breach_action: <p>The action that Amazon Redshift Serverless takes when the limit is reached. The default is log.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.create_usage_limit_request.CreateUsageLimitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.create_usage_limit_response.CreateUsageLimitResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.create_usage_limit

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.create_usage_limit.async_create_usage_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.create_usage_limit_request.CreateUsageLimitRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["usage_type"] = usage_type
        input_["amount"] = amount
        if period is not None:
            input_["period"] = period
        if breach_action is not None:
            input_["breach_action"] = breach_action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_usage_limit(
        self,
        usage_limit_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.delete_usage_limit_response.DeleteUsageLimitResponse":
        """<p>Deletes a usage limit from Amazon Redshift Serverless.</p>

        Args:
            usage_limit_id: <p>The unique identifier of the usage limit to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.delete_usage_limit_request.DeleteUsageLimitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.delete_usage_limit_response.DeleteUsageLimitResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.delete_usage_limit

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.delete_usage_limit.async_delete_usage_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.delete_usage_limit_request.DeleteUsageLimitRequest = {}  # type: ignore[typeddict-item]
        input_["usage_limit_id"] = usage_limit_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_usage_limit(
        self,
        usage_limit_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "aws_sdk_redshift_serverless.types.get_usage_limit_response.GetUsageLimitResponse":
        """<p>Returns information about a usage limit.</p>

        Args:
            usage_limit_id: <p>The unique identifier of the usage limit to return information for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.get_usage_limit_request.GetUsageLimitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.get_usage_limit_response.GetUsageLimitResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.get_usage_limit

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.get_usage_limit.async_get_usage_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.get_usage_limit_request.GetUsageLimitRequest = {}  # type: ignore[typeddict-item]
        input_["usage_limit_id"] = usage_limit_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_usage_limits(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        resource_arn: Optional[str] = None,
        usage_type: Optional[
            "aws_sdk_redshift_serverless.types.usage_limit_usage_type.UsageLimitUsageType"
        ] = None,
        next_token: Optional[
            "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_redshift_serverless.types.list_usage_limits_response.ListUsageLimitsResponse":
        """<p>Lists all usage limits within Amazon Redshift Serverless.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource whose usage limits you want to list.</p>
            usage_type: <p>The Amazon Redshift Serverless feature whose limits you want to see.</p>
            next_token: <p>If your initial <code>ListUsageLimits</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListUsageLimits</code> operations, which returns results in the next page. </p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 100.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.list_usage_limits_request.ListUsageLimitsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.list_usage_limits_response.ListUsageLimitsResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.list_usage_limits

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.list_usage_limits.async_list_usage_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.list_usage_limits_request.ListUsageLimitsRequest = {}  # type: ignore[typeddict-item]
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if usage_type is not None:
            input_["usage_type"] = usage_type
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

    async def update_usage_limit(
        self,
        usage_limit_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        amount: Optional[int] = None,
        breach_action: Optional[
            "aws_sdk_redshift_serverless.types.usage_limit_breach_action.UsageLimitBreachAction"
        ] = None,
    ) -> "aws_sdk_redshift_serverless.types.update_usage_limit_response.UpdateUsageLimitResponse":
        """<p>Update a usage limit in Amazon Redshift Serverless. You can't update the usage type or period of a usage limit.</p>

        Args:
            usage_limit_id: <p>The identifier of the usage limit to update.</p>
            amount: <p>The new limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.</p>
            breach_action: <p>The new action that Amazon Redshift Serverless takes when the limit is reached.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_redshift_serverless.types.update_usage_limit_request.UpdateUsageLimitRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_redshift_serverless.types.update_usage_limit_response.UpdateUsageLimitResponse"
        ]:
            import aws_sdk_redshift_serverless._operations.redshift_serverless.update_usage_limit

            (
                output,
                http_response,
            ) = await aws_sdk_redshift_serverless._operations.redshift_serverless.update_usage_limit.async_update_usage_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_redshift_serverless.types.update_usage_limit_request.UpdateUsageLimitRequest = {}  # type: ignore[typeddict-item]
        input_["usage_limit_id"] = usage_limit_id
        if amount is not None:
            input_["amount"] = amount
        if breach_action is not None:
            input_["breach_action"] = breach_action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
