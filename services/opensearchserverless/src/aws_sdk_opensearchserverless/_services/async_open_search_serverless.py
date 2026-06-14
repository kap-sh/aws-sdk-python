"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#OpenSearchServerless``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_opensearchserverless._auth._signers
import aws_sdk_opensearchserverless._auth._sigv4
from aws_sdk_opensearchserverless._auth._identity import Credentials
from aws_sdk_opensearchserverless._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_opensearchserverless._auth._zapros_handler import AuthMiddleware
from aws_sdk_opensearchserverless._resources.open_search_serverless.access_policy import (
    AsyncAccessPolicy,
)
from aws_sdk_opensearchserverless._resources.open_search_serverless.collection import (
    AsyncCollection,
)
from aws_sdk_opensearchserverless._resources.open_search_serverless.collection_group import (
    AsyncCollectionGroup,
)
from aws_sdk_opensearchserverless._resources.open_search_serverless.index import (
    AsyncIndex,
)
from aws_sdk_opensearchserverless._resources.open_search_serverless.lifecycle_policy import (
    AsyncLifecyclePolicy,
)
from aws_sdk_opensearchserverless._resources.open_search_serverless.security_config import (
    AsyncSecurityConfig,
)
from aws_sdk_opensearchserverless._resources.open_search_serverless.security_policy import (
    AsyncSecurityPolicy,
)
from aws_sdk_opensearchserverless._resources.open_search_serverless.vpc_endpoint import (
    AsyncVpcEndpoint,
)
from aws_sdk_opensearchserverless._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.arn
    import aws_sdk_opensearchserverless.types.batch_get_collection_group_request
    import aws_sdk_opensearchserverless.types.batch_get_collection_group_response
    import aws_sdk_opensearchserverless.types.batch_get_collection_request
    import aws_sdk_opensearchserverless.types.batch_get_collection_response
    import aws_sdk_opensearchserverless.types.batch_get_effective_lifecycle_policy_request
    import aws_sdk_opensearchserverless.types.batch_get_effective_lifecycle_policy_response
    import aws_sdk_opensearchserverless.types.batch_get_lifecycle_policy_request
    import aws_sdk_opensearchserverless.types.batch_get_lifecycle_policy_response
    import aws_sdk_opensearchserverless.types.batch_get_vpc_endpoint_request
    import aws_sdk_opensearchserverless.types.batch_get_vpc_endpoint_response
    import aws_sdk_opensearchserverless.types.capacity_limits
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.collection_group_ids
    import aws_sdk_opensearchserverless.types.collection_group_names
    import aws_sdk_opensearchserverless.types.collection_ids
    import aws_sdk_opensearchserverless.types.collection_names
    import aws_sdk_opensearchserverless.types.create_lifecycle_policy_request
    import aws_sdk_opensearchserverless.types.create_lifecycle_policy_response
    import aws_sdk_opensearchserverless.types.create_security_policy_request
    import aws_sdk_opensearchserverless.types.create_security_policy_response
    import aws_sdk_opensearchserverless.types.get_account_settings_request
    import aws_sdk_opensearchserverless.types.get_account_settings_response
    import aws_sdk_opensearchserverless.types.get_policies_stats_request
    import aws_sdk_opensearchserverless.types.get_policies_stats_response
    import aws_sdk_opensearchserverless.types.lifecycle_policy_identifiers
    import aws_sdk_opensearchserverless.types.lifecycle_policy_resource_identifiers
    import aws_sdk_opensearchserverless.types.lifecycle_policy_type
    import aws_sdk_opensearchserverless.types.list_tags_for_resource_request
    import aws_sdk_opensearchserverless.types.list_tags_for_resource_response
    import aws_sdk_opensearchserverless.types.policy_description
    import aws_sdk_opensearchserverless.types.policy_document
    import aws_sdk_opensearchserverless.types.policy_name
    import aws_sdk_opensearchserverless.types.security_group_ids
    import aws_sdk_opensearchserverless.types.security_policy_type
    import aws_sdk_opensearchserverless.types.subnet_ids
    import aws_sdk_opensearchserverless.types.tag_keys
    import aws_sdk_opensearchserverless.types.tag_resource_request
    import aws_sdk_opensearchserverless.types.tag_resource_response
    import aws_sdk_opensearchserverless.types.tags
    import aws_sdk_opensearchserverless.types.untag_resource_request
    import aws_sdk_opensearchserverless.types.untag_resource_response
    import aws_sdk_opensearchserverless.types.update_account_settings_request
    import aws_sdk_opensearchserverless.types.update_account_settings_response
    import aws_sdk_opensearchserverless.types.update_vpc_endpoint_request
    import aws_sdk_opensearchserverless.types.update_vpc_endpoint_response
    import aws_sdk_opensearchserverless.types.vpc_endpoint_id
    import aws_sdk_opensearchserverless.types.vpc_endpoint_ids


class AsyncOpenSearchServerlessClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncOpenSearchServerlessClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
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
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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
            "aws_sdk_opensearchserverless.types.collection_ids.CollectionIds"
        ] = None,
        names: Optional[
            "aws_sdk_opensearchserverless.types.collection_names.CollectionNames"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.batch_get_collection_response.BatchGetCollectionResponse":
        """<p>Returns attributes for one or more collections, including the collection endpoint, the OpenSearch Dashboards endpoint, and FIPS-compliant endpoints. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            ids: <p>A list of collection IDs. You can't provide names and IDs in the same request. The ID is part of the collection endpoint. You can also retrieve it using the <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html\">ListCollections</a> API.</p>
            names: <p>A list of collection names. You can't provide names and IDs in the same request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.batch_get_collection_request.BatchGetCollectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.batch_get_collection_response.BatchGetCollectionResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.batch_get_collection

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.batch_get_collection.async_batch_get_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.batch_get_collection_request.BatchGetCollectionRequest = {}  # type: ignore[typeddict-item]
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
            "aws_sdk_opensearchserverless.types.collection_group_ids.CollectionGroupIds"
        ] = None,
        names: Optional[
            "aws_sdk_opensearchserverless.types.collection_group_names.CollectionGroupNames"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.batch_get_collection_group_response.BatchGetCollectionGroupResponse":
        """<p>Returns attributes for one or more collection groups, including capacity limits and the number of collections in each group. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            ids: <p>A list of collection group IDs. You can't provide names and IDs in the same request.</p>
            names: <p>A list of collection group names. You can't provide names and IDs in the same request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.batch_get_collection_group_request.BatchGetCollectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.batch_get_collection_group_response.BatchGetCollectionGroupResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.batch_get_collection_group

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.batch_get_collection_group.async_batch_get_collection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.batch_get_collection_group_request.BatchGetCollectionGroupRequest = {}  # type: ignore[typeddict-item]
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
        resource_identifiers: "aws_sdk_opensearchserverless.types.lifecycle_policy_resource_identifiers.LifecyclePolicyResourceIdentifiers",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.batch_get_effective_lifecycle_policy_response.BatchGetEffectiveLifecyclePolicyResponse":
        """<p>Returns a list of successful and failed retrievals for the OpenSearch Serverless indexes. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list\">Viewing data lifecycle policies</a>.</p>

        Args:
            resource_identifiers: <p>The unique identifiers of policy types and resource names.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.batch_get_effective_lifecycle_policy_request.BatchGetEffectiveLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.batch_get_effective_lifecycle_policy_response.BatchGetEffectiveLifecyclePolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.batch_get_effective_lifecycle_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.batch_get_effective_lifecycle_policy.async_batch_get_effective_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.batch_get_effective_lifecycle_policy_request.BatchGetEffectiveLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_identifiers"] = resource_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_lifecycle_policy(
        self,
        identifiers: "aws_sdk_opensearchserverless.types.lifecycle_policy_identifiers.LifecyclePolicyIdentifiers",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.batch_get_lifecycle_policy_response.BatchGetLifecyclePolicyResponse":
        """<p>Returns one or more configured OpenSearch Serverless lifecycle policies. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list\">Viewing data lifecycle policies</a>.</p>

        Args:
            identifiers: <p>The unique identifiers of policy types and policy names.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.batch_get_lifecycle_policy_request.BatchGetLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.batch_get_lifecycle_policy_response.BatchGetLifecyclePolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.batch_get_lifecycle_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.batch_get_lifecycle_policy.async_batch_get_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.batch_get_lifecycle_policy_request.BatchGetLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["identifiers"] = identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_get_vpc_endpoint(
        self,
        ids: "aws_sdk_opensearchserverless.types.vpc_endpoint_ids.VpcEndpointIds",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.batch_get_vpc_endpoint_response.BatchGetVpcEndpointResponse":
        """<p>Returns attributes for one or more VPC endpoints associated with the current account. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            ids: <p>A list of VPC endpoint identifiers.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.batch_get_vpc_endpoint_request.BatchGetVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.batch_get_vpc_endpoint_response.BatchGetVpcEndpointResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.batch_get_vpc_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.batch_get_vpc_endpoint.async_batch_get_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.batch_get_vpc_endpoint_request.BatchGetVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["ids"] = ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_lifecycle_policy(
        self,
        type: "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType",
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
    ) -> "aws_sdk_opensearchserverless.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse":
        """<p>Creates a lifecyle policy to be applied to OpenSearch Serverless indexes. Lifecycle policies define the number of days or hours to retain the data on an OpenSearch Serverless index. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-create\">Creating data lifecycle policies</a>.</p>

        Args:
            type: <p>The type of lifecycle policy.</p>
            name: <p>The name of the lifecycle policy.</p>
            description: <p>A description of the lifecycle policy.</p>
            policy: <p>The JSON policy document to use as the content for the lifecycle policy.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.create_lifecycle_policy_response.CreateLifecyclePolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_lifecycle_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.create_lifecycle_policy.async_create_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.create_lifecycle_policy_request.CreateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
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
        type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType",
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
    ) -> "aws_sdk_opensearchserverless.types.create_security_policy_response.CreateSecurityPolicyResponse":
        """<p>Creates a security policy to be used by one or more OpenSearch Serverless collections. Security policies provide access to a collection and its OpenSearch Dashboards endpoint from public networks or specific VPC endpoints. They also allow you to secure a collection with a KMS encryption key. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html\">Network access for Amazon OpenSearch Serverless</a> and <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html\">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security policy.</p>
            name: <p>The name of the policy.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the new policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.create_security_policy_request.CreateSecurityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.create_security_policy_response.CreateSecurityPolicyResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_security_policy

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.create_security_policy.async_create_security_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.create_security_policy_request.CreateSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
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
    ) -> "aws_sdk_opensearchserverless.types.get_account_settings_response.GetAccountSettingsResponse":
        """<p>Returns account-level settings related to OpenSearch Serverless.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.get_account_settings_request.GetAccountSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.get_account_settings_response.GetAccountSettingsResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.get_account_settings

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.get_account_settings.async_get_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.get_account_settings_request.GetAccountSettingsRequest = {}  # type: ignore[typeddict-item]

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
    ) -> "aws_sdk_opensearchserverless.types.get_policies_stats_response.GetPoliciesStatsResponse":
        """<p>Returns statistical information about your OpenSearch Serverless access policies, security configurations, and security policies.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.get_policies_stats_request.GetPoliciesStatsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.get_policies_stats_response.GetPoliciesStatsResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.get_policies_stats

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.get_policies_stats.async_get_policies_stats(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.get_policies_stats_request.GetPoliciesStatsRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_opensearchserverless.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns the tags for an OpenSearch Serverless resource. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html\">Tagging Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_opensearchserverless.types.arn.Arn",
        tags: "aws_sdk_opensearchserverless.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.tag_resource_response.TagResourceResponse":
        """<p>Associates tags with an OpenSearch Serverless resource. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html\">Tagging Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>
            tags: <p>A list of tags (key-value pairs) to add to the resource. All tag keys in the request must be unique.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_opensearchserverless.types.arn.Arn",
        tag_keys: "aws_sdk_opensearchserverless.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "aws_sdk_opensearchserverless.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or set of tags from an OpenSearch Serverless resource. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection.html\">Tagging Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>
            tag_keys: <p>The tag or set of tags to remove from the resource. All tag keys in the request must be unique.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
            "aws_sdk_opensearchserverless.types.capacity_limits.CapacityLimits"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.update_account_settings_response.UpdateAccountSettingsResponse":
        """<p>Update the OpenSearch Serverless settings for the current Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-scaling.html\">Managing capacity limits for Amazon OpenSearch Serverless</a>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.update_account_settings_request.UpdateAccountSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.update_account_settings_response.UpdateAccountSettingsResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_account_settings

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.update_account_settings.async_update_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.update_account_settings_request.UpdateAccountSettingsRequest = {}  # type: ignore[typeddict-item]
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
        id: "aws_sdk_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        add_subnet_ids: Optional[
            "aws_sdk_opensearchserverless.types.subnet_ids.SubnetIds"
        ] = None,
        remove_subnet_ids: Optional[
            "aws_sdk_opensearchserverless.types.subnet_ids.SubnetIds"
        ] = None,
        add_security_group_ids: Optional[
            "aws_sdk_opensearchserverless.types.security_group_ids.SecurityGroupIds"
        ] = None,
        remove_security_group_ids: Optional[
            "aws_sdk_opensearchserverless.types.security_group_ids.SecurityGroupIds"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse":
        """<p>Updates an OpenSearch Serverless-managed interface endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            id: <p>The unique identifier of the interface endpoint to update.</p>
            add_subnet_ids: <p>The ID of one or more subnets to add to the endpoint.</p>
            remove_subnet_ids: <p>The unique identifiers of the subnets to remove from the endpoint.</p>
            add_security_group_ids: <p>The unique identifiers of the security groups to add to the endpoint. Security groups define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            remove_security_group_ids: <p>The unique identifiers of the security groups to remove from the endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_vpc_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.update_vpc_endpoint.async_update_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
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
