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
    import aws_sdk_opensearchserverless.types.access_policy_type
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.create_access_policy_request
    import aws_sdk_opensearchserverless.types.create_access_policy_response
    import aws_sdk_opensearchserverless.types.delete_access_policy_request
    import aws_sdk_opensearchserverless.types.delete_access_policy_response
    import aws_sdk_opensearchserverless.types.get_access_policy_request
    import aws_sdk_opensearchserverless.types.get_access_policy_response
    import aws_sdk_opensearchserverless.types.list_access_policies_request
    import aws_sdk_opensearchserverless.types.list_access_policies_response
    import aws_sdk_opensearchserverless.types.policy_description
    import aws_sdk_opensearchserverless.types.policy_document
    import aws_sdk_opensearchserverless.types.policy_name
    import aws_sdk_opensearchserverless.types.policy_version
    import aws_sdk_opensearchserverless.types.resource_filter
    import aws_sdk_opensearchserverless.types.update_access_policy_request
    import aws_sdk_opensearchserverless.types.update_access_policy_response
    from aws_sdk_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from aws_sdk_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class AccessPolicy:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def put(
        self,
        type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        policy: "aws_sdk_opensearchserverless.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.create_access_policy_response.CreateAccessPolicyResponse":
        r"""<p>Creates a data access policy for OpenSearch Serverless. Access policies limit access to collections and the resources within them, and allow a user to access that data irrespective of the access mechanism or network source. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            aws_sdk_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            aws_sdk_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            aws_sdk_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            aws_sdk_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            aws_sdk_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.create_access_policy_request.CreateAccessPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.create_access_policy_response.CreateAccessPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_access_policy

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.create_access_policy.create_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.create_access_policy_request.CreateAccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["policy"] = policy
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.get_access_policy_response.GetAccessPolicyResponse":
        r"""<p>Returns an OpenSearch Serverless access policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>Tye type of policy. Currently, the only supported value is <code>data</code>.</p>
            name: <p>The name of the access policy.</p>

        Raises:
            aws_sdk_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            aws_sdk_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            aws_sdk_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            aws_sdk_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.get_access_policy_request.GetAccessPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.get_access_policy_response.GetAccessPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.get_access_policy

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.get_access_policy.get_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.get_access_policy_request.GetAccessPolicyRequest = {}  # type: ignore[typeddict-item]
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
        type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType",
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
    ) -> "aws_sdk_opensearchserverless.types.update_access_policy_response.UpdateAccessPolicyResponse":
        r"""<p>Updates an OpenSearch Serverless access policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy.</p>
            policy_version: <p>The version of the policy being updated.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            aws_sdk_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            aws_sdk_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            aws_sdk_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            aws_sdk_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            aws_sdk_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.update_access_policy_request.UpdateAccessPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.update_access_policy_response.UpdateAccessPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_access_policy

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.update_access_policy.update_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.update_access_policy_request.UpdateAccessPolicyRequest = {}  # type: ignore[typeddict-item]
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
        type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_access_policy_response.DeleteAccessPolicyResponse":
        r"""<p>Deletes an OpenSearch Serverless access policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            aws_sdk_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            aws_sdk_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            aws_sdk_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            aws_sdk_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            aws_sdk_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.delete_access_policy_request.DeleteAccessPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.delete_access_policy_response.DeleteAccessPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_access_policy

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.delete_access_policy.delete_access_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.delete_access_policy_request.DeleteAccessPolicyRequest = {}  # type: ignore[typeddict-item]
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
        type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        resource: Optional[
            "aws_sdk_opensearchserverless.types.resource_filter.ResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_access_policies_response.ListAccessPoliciesResponse":
        """<p>Returns information about a list of OpenSearch Serverless access policies.</p>

        Args:
            type: <p>The type of access policy.</p>
            resource: <p>Resource filters (can be collections or indexes) that policies can apply to.</p>
            next_token: <p>If your initial <code>ListAccessPolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListAccessPolicies</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            aws_sdk_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            aws_sdk_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            aws_sdk_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.list_access_policies_request.ListAccessPoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.list_access_policies_response.ListAccessPoliciesResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_access_policies

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.list_access_policies.list_access_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.list_access_policies_request.ListAccessPoliciesRequest = {}  # type: ignore[typeddict-item]
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


class AsyncAccessPolicy:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def put(
        self,
        type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        policy: "aws_sdk_opensearchserverless.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.create_access_policy_response.CreateAccessPolicyResponse":
        r"""<p>Creates a data access policy for OpenSearch Serverless. Access policies limit access to collections and the resources within them, and allow a user to access that data irrespective of the access mechanism or network source. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            aws_sdk_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            aws_sdk_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            aws_sdk_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            aws_sdk_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            aws_sdk_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.create_access_policy_request.CreateAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.create_access_policy_response.CreateAccessPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_access_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.create_access_policy.async_create_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.create_access_policy_request.CreateAccessPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["type"] = type
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["policy"] = policy
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.get_access_policy_response.GetAccessPolicyResponse":
        r"""<p>Returns an OpenSearch Serverless access policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>Tye type of policy. Currently, the only supported value is <code>data</code>.</p>
            name: <p>The name of the access policy.</p>

        Raises:
            aws_sdk_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            aws_sdk_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            aws_sdk_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            aws_sdk_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.get_access_policy_request.GetAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.get_access_policy_response.GetAccessPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.get_access_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.get_access_policy.async_get_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.get_access_policy_request.GetAccessPolicyRequest = {}  # type: ignore[typeddict-item]
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
        type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType",
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
    ) -> "aws_sdk_opensearchserverless.types.update_access_policy_response.UpdateAccessPolicyResponse":
        r"""<p>Updates an OpenSearch Serverless access policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy.</p>
            policy_version: <p>The version of the policy being updated.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            aws_sdk_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            aws_sdk_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            aws_sdk_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            aws_sdk_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            aws_sdk_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.update_access_policy_request.UpdateAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.update_access_policy_response.UpdateAccessPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_access_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.update_access_policy.async_update_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.update_access_policy_request.UpdateAccessPolicyRequest = {}  # type: ignore[typeddict-item]
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
        type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType",
        name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_access_policy_response.DeleteAccessPolicyResponse":
        r"""<p>Deletes an OpenSearch Serverless access policy. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html\">Data access control for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            aws_sdk_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            aws_sdk_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            aws_sdk_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            aws_sdk_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            aws_sdk_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.delete_access_policy_request.DeleteAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.delete_access_policy_response.DeleteAccessPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_access_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.delete_access_policy.async_delete_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.delete_access_policy_request.DeleteAccessPolicyRequest = {}  # type: ignore[typeddict-item]
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
        type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        resource: Optional[
            "aws_sdk_opensearchserverless.types.resource_filter.ResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_access_policies_response.ListAccessPoliciesResponse":
        """<p>Returns information about a list of OpenSearch Serverless access policies.</p>

        Args:
            type: <p>The type of access policy.</p>
            resource: <p>Resource filters (can be collections or indexes) that policies can apply to.</p>
            next_token: <p>If your initial <code>ListAccessPolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListAccessPolicies</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            aws_sdk_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            aws_sdk_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            aws_sdk_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.list_access_policies_request.ListAccessPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.list_access_policies_response.ListAccessPoliciesResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_access_policies

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.list_access_policies.async_list_access_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.list_access_policies_request.ListAccessPoliciesRequest = {}  # type: ignore[typeddict-item]
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
