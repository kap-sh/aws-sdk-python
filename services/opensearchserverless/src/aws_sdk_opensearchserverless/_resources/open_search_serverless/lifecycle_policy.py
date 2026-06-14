from typing import TYPE_CHECKING, Optional

from aws_sdk_opensearchserverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.delete_lifecycle_policy_request
    import aws_sdk_opensearchserverless.types.delete_lifecycle_policy_response
    import aws_sdk_opensearchserverless.types.lifecycle_policy_type
    import aws_sdk_opensearchserverless.types.lifecycle_resource_filter
    import aws_sdk_opensearchserverless.types.list_lifecycle_policies_request
    import aws_sdk_opensearchserverless.types.list_lifecycle_policies_response
    import aws_sdk_opensearchserverless.types.policy_description
    import aws_sdk_opensearchserverless.types.policy_document
    import aws_sdk_opensearchserverless.types.policy_name
    import aws_sdk_opensearchserverless.types.policy_version
    import aws_sdk_opensearchserverless.types.update_lifecycle_policy_request
    import aws_sdk_opensearchserverless.types.update_lifecycle_policy_response
    from aws_sdk_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from aws_sdk_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class LifecyclePolicy:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def update(
        self,
        type: "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        policy_version: "aws_sdk_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        policy: Optional[
            "aws_sdk_opensearchserverless.types.policy_document.PolicyDocument"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse":
        """<p>Updates an OpenSearch Serverless access policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-update\">Updating data lifecycle policies</a>.</p>

        Args:
            type: <p> The type of lifecycle policy.</p>
            name: <p>The name of the policy.</p>
            policy_version: <p>The version of the policy being updated.</p>
            description: <p>A description of the lifecycle policy.</p>
            policy: <p>The JSON policy document to use as the content for the lifecycle policy.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_lifecycle_policy

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.update_lifecycle_policy.update_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["name"] = name
        input_["policy_version"] = policy_version
        if description is not None:
            input_["description"] = description
        if policy is not None:
            input_["policy"] = policy
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        type: "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse":
        """<p>Deletes an OpenSearch Serverless lifecycle policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-delete\">Deleting data lifecycle policies</a>.</p>

        Args:
            type: <p>The type of lifecycle policy.</p>
            name: <p>The name of the policy to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_lifecycle_policy

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.delete_lifecycle_policy.delete_lifecycle_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        type: "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        resources: Optional[
            "aws_sdk_opensearchserverless.types.lifecycle_resource_filter.LifecycleResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_lifecycle_policies_response.ListLifecyclePoliciesResponse":
        """<p>Returns a list of OpenSearch Serverless lifecycle policies. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list\">Viewing data lifecycle policies</a>.</p>

        Args:
            type: <p>The type of lifecycle policy.</p>
            resources: <p>Resource filters that policies can apply to. Currently, the only supported resource type is <code>index</code>.</p>
            next_token: <p>If your initial <code>ListLifecyclePolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListLifecyclePolicies</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use use <code>nextToken</code> to get the next page of results. The default is 10.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.list_lifecycle_policies_request.ListLifecyclePoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.list_lifecycle_policies_response.ListLifecyclePoliciesResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_lifecycle_policies

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.list_lifecycle_policies.list_lifecycle_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.list_lifecycle_policies_request.ListLifecyclePoliciesRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        if resources is not None:
            input_["resources"] = resources
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


class AsyncLifecyclePolicy:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def update(
        self,
        type: "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        policy_version: "aws_sdk_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        policy: Optional[
            "aws_sdk_opensearchserverless.types.policy_document.PolicyDocument"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse":
        """<p>Updates an OpenSearch Serverless access policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-update\">Updating data lifecycle policies</a>.</p>

        Args:
            type: <p> The type of lifecycle policy.</p>
            name: <p>The name of the policy.</p>
            policy_version: <p>The version of the policy being updated.</p>
            description: <p>A description of the lifecycle policy.</p>
            policy: <p>The JSON policy document to use as the content for the lifecycle policy.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.update_lifecycle_policy_response.UpdateLifecyclePolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_lifecycle_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.update_lifecycle_policy.async_update_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.update_lifecycle_policy_request.UpdateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["name"] = name
        input_["policy_version"] = policy_version
        if description is not None:
            input_["description"] = description
        if policy is not None:
            input_["policy"] = policy
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        type: "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse":
        """<p>Deletes an OpenSearch Serverless lifecycle policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-delete\">Deleting data lifecycle policies</a>.</p>

        Args:
            type: <p>The type of lifecycle policy.</p>
            name: <p>The name of the policy to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.delete_lifecycle_policy_response.DeleteLifecyclePolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_lifecycle_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.delete_lifecycle_policy.async_delete_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.delete_lifecycle_policy_request.DeleteLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        type: "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        resources: Optional[
            "aws_sdk_opensearchserverless.types.lifecycle_resource_filter.LifecycleResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_lifecycle_policies_response.ListLifecyclePoliciesResponse":
        """<p>Returns a list of OpenSearch Serverless lifecycle policies. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list\">Viewing data lifecycle policies</a>.</p>

        Args:
            type: <p>The type of lifecycle policy.</p>
            resources: <p>Resource filters that policies can apply to. Currently, the only supported resource type is <code>index</code>.</p>
            next_token: <p>If your initial <code>ListLifecyclePolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListLifecyclePolicies</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use use <code>nextToken</code> to get the next page of results. The default is 10.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.list_lifecycle_policies_request.ListLifecyclePoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.list_lifecycle_policies_response.ListLifecyclePoliciesResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_lifecycle_policies

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.list_lifecycle_policies.async_list_lifecycle_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.list_lifecycle_policies_request.ListLifecyclePoliciesRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        if resources is not None:
            input_["resources"] = resources
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
