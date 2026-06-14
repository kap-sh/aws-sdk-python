from __future__ import annotations

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
    import aws_sdk_opensearchserverless.types.delete_security_policy_request
    import aws_sdk_opensearchserverless.types.delete_security_policy_response
    import aws_sdk_opensearchserverless.types.get_security_policy_request
    import aws_sdk_opensearchserverless.types.get_security_policy_response
    import aws_sdk_opensearchserverless.types.list_security_policies_request
    import aws_sdk_opensearchserverless.types.list_security_policies_response
    import aws_sdk_opensearchserverless.types.policy_description
    import aws_sdk_opensearchserverless.types.policy_document
    import aws_sdk_opensearchserverless.types.policy_name
    import aws_sdk_opensearchserverless.types.policy_version
    import aws_sdk_opensearchserverless.types.resource_filter
    import aws_sdk_opensearchserverless.types.security_policy_type
    import aws_sdk_opensearchserverless.types.update_security_policy_request
    import aws_sdk_opensearchserverless.types.update_security_policy_response
    from aws_sdk_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from aws_sdk_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class SecurityPolicy:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def read(
        self,
        type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.get_security_policy_response.GetSecurityPolicyResponse":
        r"""<p>Returns information about a configured OpenSearch Serverless security policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html\">Network access for Amazon OpenSearch Serverless</a> and <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html\">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security policy.</p>
            name: <p>The name of the security policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.get_security_policy_request.GetSecurityPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.get_security_policy_response.GetSecurityPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.get_security_policy

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.get_security_policy.get_security_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.get_security_policy_request.GetSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType",
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
    ) -> "aws_sdk_opensearchserverless.types.update_security_policy_response.UpdateSecurityPolicyResponse":
        r"""<p>Updates an OpenSearch Serverless security policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html\">Network access for Amazon OpenSearch Serverless</a> and <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html\">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of access policy.</p>
            name: <p>The name of the policy.</p>
            policy_version: <p>The version of the policy being updated.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the new policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.update_security_policy_request.UpdateSecurityPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.update_security_policy_response.UpdateSecurityPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_security_policy

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.update_security_policy.update_security_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.update_security_policy_request.UpdateSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
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
        type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_security_policy_response.DeleteSecurityPolicyResponse":
        """<p>Deletes an OpenSearch Serverless security policy.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.delete_security_policy_request.DeleteSecurityPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.delete_security_policy_response.DeleteSecurityPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_security_policy

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.delete_security_policy.delete_security_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.delete_security_policy_request.DeleteSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
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
        type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        resource: Optional[
            "aws_sdk_opensearchserverless.types.resource_filter.ResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_security_policies_response.ListSecurityPoliciesResponse":
        """<p>Returns information about configured OpenSearch Serverless security policies.</p>

        Args:
            type: <p>The type of policy.</p>
            resource: <p>Resource filters (can be collection or indexes) that policies can apply to. </p>
            next_token: <p>If your initial <code>ListSecurityPolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListSecurityPolicies</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.list_security_policies_request.ListSecurityPoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.list_security_policies_response.ListSecurityPoliciesResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_security_policies

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.list_security_policies.list_security_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.list_security_policies_request.ListSecurityPoliciesRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        if resource is not None:
            input_["resource"] = resource
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


class AsyncSecurityPolicy:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def read(
        self,
        type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.get_security_policy_response.GetSecurityPolicyResponse":
        r"""<p>Returns information about a configured OpenSearch Serverless security policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html\">Network access for Amazon OpenSearch Serverless</a> and <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html\">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security policy.</p>
            name: <p>The name of the security policy.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.get_security_policy_request.GetSecurityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.get_security_policy_response.GetSecurityPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.get_security_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.get_security_policy.async_get_security_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.get_security_policy_request.GetSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType",
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
    ) -> "aws_sdk_opensearchserverless.types.update_security_policy_response.UpdateSecurityPolicyResponse":
        r"""<p>Updates an OpenSearch Serverless security policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html\">Network access for Amazon OpenSearch Serverless</a> and <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html\">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of access policy.</p>
            name: <p>The name of the policy.</p>
            policy_version: <p>The version of the policy being updated.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the new policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.update_security_policy_request.UpdateSecurityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.update_security_policy_response.UpdateSecurityPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_security_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.update_security_policy.async_update_security_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.update_security_policy_request.UpdateSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
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
        type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_security_policy_response.DeleteSecurityPolicyResponse":
        """<p>Deletes an OpenSearch Serverless security policy.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.delete_security_policy_request.DeleteSecurityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.delete_security_policy_response.DeleteSecurityPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_security_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.delete_security_policy.async_delete_security_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.delete_security_policy_request.DeleteSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
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
        type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        resource: Optional[
            "aws_sdk_opensearchserverless.types.resource_filter.ResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_security_policies_response.ListSecurityPoliciesResponse":
        """<p>Returns information about configured OpenSearch Serverless security policies.</p>

        Args:
            type: <p>The type of policy.</p>
            resource: <p>Resource filters (can be collection or indexes) that policies can apply to. </p>
            next_token: <p>If your initial <code>ListSecurityPolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListSecurityPolicies</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.list_security_policies_request.ListSecurityPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.list_security_policies_response.ListSecurityPoliciesResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_security_policies

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.list_security_policies.async_list_security_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.list_security_policies_request.ListSecurityPoliciesRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        if resource is not None:
            input_["resource"] = resource
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
