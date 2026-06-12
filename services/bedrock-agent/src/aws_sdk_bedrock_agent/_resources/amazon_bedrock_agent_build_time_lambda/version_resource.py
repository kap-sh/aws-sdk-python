from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agent._auth._signers
import aws_sdk_bedrock_agent._auth._sigv4
from aws_sdk_bedrock_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_version_summary
    import aws_sdk_bedrock_agent.types.delete_agent_version_request
    import aws_sdk_bedrock_agent.types.delete_agent_version_response
    import aws_sdk_bedrock_agent.types.get_agent_version_request
    import aws_sdk_bedrock_agent.types.get_agent_version_response
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.list_agent_versions_request
    import aws_sdk_bedrock_agent.types.list_agent_versions_response
    import aws_sdk_bedrock_agent.types.max_results
    import aws_sdk_bedrock_agent.types.next_token
    import aws_sdk_bedrock_agent.types.numerical_version
    from aws_sdk_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from aws_sdk_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class VersionResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def delete_agent_version(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "aws_sdk_bedrock_agent.types.delete_agent_version_response.DeleteAgentVersionResponse":
        """<p>Deletes a version of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the version belongs to.</p>
            agent_version: <p>The version of the agent to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.delete_agent_version_request.DeleteAgentVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.delete_agent_version_response.DeleteAgentVersionResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_version

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_version.delete_agent_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.delete_agent_version_request.DeleteAgentVersionRequest = {}  # type: ignore[typeddict-item]
        input["agent_id"] = agent_id
        input["agent_version"] = agent_version
        if skip_resource_in_use_check is not None:
            input["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_agent_version(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse"
    ):
        """<p>Gets details about a version of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_version: <p>The version of the agent.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.get_agent_version_request.GetAgentVersionRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_version

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_version.get_agent_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.get_agent_version_request.GetAgentVersionRequest = {}  # type: ignore[typeddict-item]
        input["agent_id"] = agent_id
        input["agent_version"] = agent_version

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_agent_versions(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_agent_versions_response.ListAgentVersionsResponse":
        """<p>Lists the versions of an agent and information about each version.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.list_agent_versions_request.ListAgentVersionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.list_agent_versions_response.ListAgentVersionsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_versions

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_versions.list_agent_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.list_agent_versions_request.ListAgentVersionsRequest = {}  # type: ignore[typeddict-item]
        input["agent_id"] = agent_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncVersionResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def delete_agent_version(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "aws_sdk_bedrock_agent.types.delete_agent_version_response.DeleteAgentVersionResponse":
        """<p>Deletes a version of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the version belongs to.</p>
            agent_version: <p>The version of the agent to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.delete_agent_version_request.DeleteAgentVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.delete_agent_version_response.DeleteAgentVersionResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_version

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_version.async_delete_agent_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.delete_agent_version_request.DeleteAgentVersionRequest = {}  # type: ignore[typeddict-item]
        input["agent_id"] = agent_id
        input["agent_version"] = agent_version
        if skip_resource_in_use_check is not None:
            input["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_agent_version(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        agent_version: "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse"
    ):
        """<p>Gets details about a version of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_version: <p>The version of the agent.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.get_agent_version_request.GetAgentVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_version

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_version.async_get_agent_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.get_agent_version_request.GetAgentVersionRequest = {}  # type: ignore[typeddict-item]
        input["agent_id"] = agent_id
        input["agent_version"] = agent_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_agent_versions(
        self,
        agent_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_agent_versions_response.ListAgentVersionsResponse":
        """<p>Lists the versions of an agent and information about each version.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.list_agent_versions_request.ListAgentVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.list_agent_versions_response.ListAgentVersionsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_versions

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_versions.async_list_agent_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent.types.list_agent_versions_request.ListAgentVersionsRequest = {}  # type: ignore[typeddict-item]
        input["agent_id"] = agent_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
