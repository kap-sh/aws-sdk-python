"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#OpenSearchServerless``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_opensearchserverless._auth._signers
import capo_opensearchserverless._auth._sigv4
from capo_opensearchserverless._auth._identity import Credentials
from capo_opensearchserverless._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_opensearchserverless._auth._zapros_handler import AuthMiddleware
from capo_opensearchserverless._resources.open_search_serverless.access_policy import (
    AsyncAccessPolicy,
)
from capo_opensearchserverless._resources.open_search_serverless.collection import (
    AsyncCollection,
)
from capo_opensearchserverless._resources.open_search_serverless.collection_group import (
    AsyncCollectionGroup,
)
from capo_opensearchserverless._resources.open_search_serverless.index import AsyncIndex
from capo_opensearchserverless._resources.open_search_serverless.lifecycle_policy import (
    AsyncLifecyclePolicy,
)
from capo_opensearchserverless._resources.open_search_serverless.security_config import (
    AsyncSecurityConfig,
)
from capo_opensearchserverless._resources.open_search_serverless.security_policy import (
    AsyncSecurityPolicy,
)
from capo_opensearchserverless._resources.open_search_serverless.vpc_endpoint import (
    AsyncVpcEndpoint,
)
from capo_opensearchserverless._services._aws_config import aaws_config
from capo_opensearchserverless._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_opensearchserverless.types.arn
    import capo_opensearchserverless.types.batch_get_collection_group_request
    import capo_opensearchserverless.types.batch_get_collection_group_response
    import capo_opensearchserverless.types.batch_get_collection_request
    import capo_opensearchserverless.types.batch_get_collection_response
    import capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_request
    import capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_response
    import capo_opensearchserverless.types.batch_get_lifecycle_policy_request
    import capo_opensearchserverless.types.batch_get_lifecycle_policy_response
    import capo_opensearchserverless.types.batch_get_vpc_endpoint_request
    import capo_opensearchserverless.types.batch_get_vpc_endpoint_response
    import capo_opensearchserverless.types.capacity_limits
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_group_ids
    import capo_opensearchserverless.types.collection_group_names
    import capo_opensearchserverless.types.collection_ids
    import capo_opensearchserverless.types.collection_names
    import capo_opensearchserverless.types.create_lifecycle_policy_request
    import capo_opensearchserverless.types.create_lifecycle_policy_response
    import capo_opensearchserverless.types.create_security_policy_request
    import capo_opensearchserverless.types.create_security_policy_response
    import capo_opensearchserverless.types.get_account_settings_request
    import capo_opensearchserverless.types.get_account_settings_response
    import capo_opensearchserverless.types.get_policies_stats_request
    import capo_opensearchserverless.types.get_policies_stats_response
    import capo_opensearchserverless.types.lifecycle_policy_identifiers
    import capo_opensearchserverless.types.lifecycle_policy_resource_identifiers
    import capo_opensearchserverless.types.lifecycle_policy_type
    import capo_opensearchserverless.types.list_tags_for_resource_request
    import capo_opensearchserverless.types.list_tags_for_resource_response
    import capo_opensearchserverless.types.policy_description
    import capo_opensearchserverless.types.policy_document
    import capo_opensearchserverless.types.policy_name
    import capo_opensearchserverless.types.security_group_ids
    import capo_opensearchserverless.types.security_policy_type
    import capo_opensearchserverless.types.subnet_ids
    import capo_opensearchserverless.types.tag_keys
    import capo_opensearchserverless.types.tag_resource_request
    import capo_opensearchserverless.types.tag_resource_response
    import capo_opensearchserverless.types.tags
    import capo_opensearchserverless.types.untag_resource_request
    import capo_opensearchserverless.types.untag_resource_response
    import capo_opensearchserverless.types.update_account_settings_request
    import capo_opensearchserverless.types.update_account_settings_response
    import capo_opensearchserverless.types.update_vpc_endpoint_request
    import capo_opensearchserverless.types.update_vpc_endpoint_response
    import capo_opensearchserverless.types.vpc_endpoint_id
    import capo_opensearchserverless.types.vpc_endpoint_ids


class AsyncOpenSearchServerlessClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncOpenSearchServerlessClient:
    """A client for the ``OpenSearchServerless`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncOpenSearchServerlessClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.access_policy = AsyncAccessPolicy(self)
        self.collection = AsyncCollection(self)
        self.collection_group = AsyncCollectionGroup(self)
        self.index = AsyncIndex(self)
        self.lifecycle_policy = AsyncLifecyclePolicy(self)
        self.security_config = AsyncSecurityConfig(self)
        self.security_policy = AsyncSecurityPolicy(self)
        self.vpc_endpoint = AsyncVpcEndpoint(self)

    def operation_options(
        self, config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncOpenSearchServerlessClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def batch_get_collection(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        ids: Optional[
            "capo_opensearchserverless.types.collection_ids.CollectionIds"
        ] = None,
        names: Optional[
            "capo_opensearchserverless.types.collection_names.CollectionNames"
        ] = None,
    ) -> "capo_opensearchserverless.types.batch_get_collection_response.BatchGetCollectionResponse":
        r"""<p>Returns attributes for one or more collections, including the collection endpoint, the OpenSearch Dashboards endpoint, and FIPS-compliant endpoints. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            ids: <p>A list of collection IDs. You can't provide names and IDs in the same request. The ID is part of the collection endpoint. You can also retrieve it using the <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html\">ListCollections</a> API.</p>
            names: <p>A list of collection names. You can't provide names and IDs in the same request.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.batch_get_collection_request.BatchGetCollectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.batch_get_collection_response.BatchGetCollectionResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.batch_get_collection

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.batch_get_collection.async_batch_get_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.batch_get_collection_request.BatchGetCollectionRequest = {}  # type: ignore[typeddict-item]
        if ids is not None:
            input_["ids"] = ids
        if names is not None:
            input_["names"] = names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_collection_group(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        ids: Optional[
            "capo_opensearchserverless.types.collection_group_ids.CollectionGroupIds"
        ] = None,
        names: Optional[
            "capo_opensearchserverless.types.collection_group_names.CollectionGroupNames"
        ] = None,
    ) -> "capo_opensearchserverless.types.batch_get_collection_group_response.BatchGetCollectionGroupResponse":
        r"""<p>Returns attributes for one or more collection groups, including capacity limits and the number of collections in each group. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            ids: <p>A list of collection group IDs. You can't provide names and IDs in the same request.</p>
            names: <p>A list of collection group names. You can't provide names and IDs in the same request.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.batch_get_collection_group_request.BatchGetCollectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.batch_get_collection_group_response.BatchGetCollectionGroupResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.batch_get_collection_group

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.batch_get_collection_group.async_batch_get_collection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.batch_get_collection_group_request.BatchGetCollectionGroupRequest = {}  # type: ignore[typeddict-item]
        if ids is not None:
            input_["ids"] = ids
        if names is not None:
            input_["names"] = names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_effective_lifecycle_policy(
        self,
        resource_identifiers: "capo_opensearchserverless.types.lifecycle_policy_resource_identifiers.LifecyclePolicyResourceIdentifiers",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_response.BatchGetEffectiveLifecyclePolicyResponse":
        r"""<p>Returns a list of successful and failed retrievals for the OpenSearch Serverless indexes. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list\">Viewing data lifecycle policies</a>.</p>

        Args:
            resource_identifiers: <p>The unique identifiers of policy types and resource names.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_request.BatchGetEffectiveLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_response.BatchGetEffectiveLifecyclePolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.batch_get_effective_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.batch_get_effective_lifecycle_policy.async_batch_get_effective_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.batch_get_effective_lifecycle_policy_request.BatchGetEffectiveLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_identifiers"] = resource_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_lifecycle_policy(
        self,
        identifiers: "capo_opensearchserverless.types.lifecycle_policy_identifiers.LifecyclePolicyIdentifiers",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.batch_get_lifecycle_policy_response.BatchGetLifecyclePolicyResponse":
        r"""<p>Returns one or more configured OpenSearch Serverless lifecycle policies. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list\">Viewing data lifecycle policies</a>.</p>

        Args:
            identifiers: <p>The unique identifiers of policy types and policy names.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.batch_get_lifecycle_policy_request.BatchGetLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.batch_get_lifecycle_policy_response.BatchGetLifecyclePolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.batch_get_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.batch_get_lifecycle_policy.async_batch_get_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.batch_get_lifecycle_policy_request.BatchGetLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["identifiers"] = identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_vpc_endpoint(
        self,
        ids: "capo_opensearchserverless.types.vpc_endpoint_ids.VpcEndpointIds",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.batch_get_vpc_endpoint_response.BatchGetVpcEndpointResponse":
        r"""<p>Returns attributes for one or more VPC endpoints associated with the current account. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            ids: <p>A list of VPC endpoint identifiers.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.batch_get_vpc_endpoint_request.BatchGetVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.batch_get_vpc_endpoint_response.BatchGetVpcEndpointResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.batch_get_vpc_endpoint

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.batch_get_vpc_endpoint.async_batch_get_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.batch_get_vpc_endpoint_request.BatchGetVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["ids"] = ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_lifecycle_policy(
        self,
        type: "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        policy: "capo_opensearchserverless.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse":
        r"""<p>Creates a lifecyle policy to be applied to OpenSearch Serverless indexes. Lifecycle policies define the number of days or hours to retain the data on an OpenSearch Serverless index. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-create\">Creating data lifecycle policies</a>.</p>

        Args:
            type: <p>The type of lifecycle policy.</p>
            name: <p>The name of the lifecycle policy.</p>
            description: <p>A description of the lifecycle policy.</p>
            policy: <p>The JSON policy document to use as the content for the lifecycle policy.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_lifecycle_policy

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.create_lifecycle_policy.async_create_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
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

    async def create_security_policy(
        self,
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        policy: "capo_opensearchserverless.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_security_policy_response.CreateSecurityPolicyResponse":
        r"""<p>Creates a security policy to be used by one or more OpenSearch Serverless collections. Security policies provide access to a collection and its OpenSearch Dashboards endpoint from public networks or specific VPC endpoints. They also allow you to secure a collection with a KMS encryption key. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html\">Network access for Amazon OpenSearch Serverless</a> and <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html\">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security policy.</p>
            name: <p>The name of the policy.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the new policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.create_security_policy_request.CreateSecurityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.create_security_policy_response.CreateSecurityPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_security_policy

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.create_security_policy.async_create_security_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_security_policy_request.CreateSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
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

    async def get_account_settings(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_account_settings_response.GetAccountSettingsResponse":
        """<p>Returns account-level settings related to OpenSearch Serverless.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.get_account_settings_request.GetAccountSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.get_account_settings_response.GetAccountSettingsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_account_settings

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.get_account_settings.async_get_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_account_settings_request.GetAccountSettingsRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_policies_stats(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_policies_stats_response.GetPoliciesStatsResponse":
        """<p>Returns statistical information about your OpenSearch Serverless access policies, security configurations, and security policies.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.get_policies_stats_request.GetPoliciesStatsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.get_policies_stats_response.GetPoliciesStatsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_policies_stats

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.get_policies_stats.async_get_policies_stats(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_policies_stats_request.GetPoliciesStatsRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_opensearchserverless.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        r"""<p>Returns the tags for an OpenSearch Serverless resource. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html\">Tagging Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_opensearchserverless.types.arn.Arn",
        tags: "capo_opensearchserverless.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.tag_resource_response.TagResourceResponse":
        r"""<p>Associates tags with an OpenSearch Serverless resource. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html\">Tagging Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>
            tags: <p>A list of tags (key-value pairs) to add to the resource. All tag keys in the request must be unique.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.tag_resource

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_opensearchserverless.types.arn.Arn",
        tag_keys: "capo_opensearchserverless.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> (
        "capo_opensearchserverless.types.untag_resource_response.UntagResourceResponse"
    ):
        r"""<p>Removes a tag or set of tags from an OpenSearch Serverless resource. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html\">Tagging Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>
            tag_keys: <p>The tag or set of tags to remove from the resource. All tag keys in the request must be unique.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.untag_resource

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_account_settings(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        capacity_limits: Optional[
            "capo_opensearchserverless.types.capacity_limits.CapacityLimits"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_account_settings_response.UpdateAccountSettingsResponse":
        r"""<p>Update the OpenSearch Serverless settings for the current Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-scaling.html\">Managing capacity limits for Amazon OpenSearch Serverless</a>.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.update_account_settings_request.UpdateAccountSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.update_account_settings_response.UpdateAccountSettingsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_account_settings

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.update_account_settings.async_update_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_account_settings_request.UpdateAccountSettingsRequest = {}  # type: ignore[typeddict-item]
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_vpc_endpoint(
        self,
        id: "capo_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        add_subnet_ids: Optional[
            "capo_opensearchserverless.types.subnet_ids.SubnetIds"
        ] = None,
        remove_subnet_ids: Optional[
            "capo_opensearchserverless.types.subnet_ids.SubnetIds"
        ] = None,
        add_security_group_ids: Optional[
            "capo_opensearchserverless.types.security_group_ids.SecurityGroupIds"
        ] = None,
        remove_security_group_ids: Optional[
            "capo_opensearchserverless.types.security_group_ids.SecurityGroupIds"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse":
        r"""<p>Updates an OpenSearch Serverless-managed interface endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            id: <p>The unique identifier of the interface endpoint to update.</p>
            add_subnet_ids: <p>The ID of one or more subnets to add to the endpoint.</p>
            remove_subnet_ids: <p>The unique identifiers of the subnets to remove from the endpoint.</p>
            add_security_group_ids: <p>The unique identifiers of the security groups to add to the endpoint. Security groups define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            remove_security_group_ids: <p>The unique identifiers of the security groups to remove from the endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_vpc_endpoint

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.update_vpc_endpoint.async_update_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if add_subnet_ids is not None:
            input_["add_subnet_ids"] = add_subnet_ids
        if remove_subnet_ids is not None:
            input_["remove_subnet_ids"] = remove_subnet_ids
        if add_security_group_ids is not None:
            input_["add_security_group_ids"] = add_security_group_ids
        if remove_security_group_ids is not None:
            input_["remove_security_group_ids"] = remove_security_group_ids
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
