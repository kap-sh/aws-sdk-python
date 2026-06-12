"""Generated from Smithy shape ``com.amazonaws.mediastore#MediaStore_20170901``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

from aws_sdk_mediastore._auth._identity import Credentials
from aws_sdk_mediastore._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_mediastore._auth._zapros_handler import AuthMiddleware
from aws_sdk_mediastore._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_arn
    import aws_sdk_mediastore.types.container_list_limit
    import aws_sdk_mediastore.types.container_name
    import aws_sdk_mediastore.types.container_policy
    import aws_sdk_mediastore.types.cors_policy
    import aws_sdk_mediastore.types.create_container_input
    import aws_sdk_mediastore.types.create_container_output
    import aws_sdk_mediastore.types.delete_container_input
    import aws_sdk_mediastore.types.delete_container_output
    import aws_sdk_mediastore.types.delete_container_policy_input
    import aws_sdk_mediastore.types.delete_container_policy_output
    import aws_sdk_mediastore.types.delete_cors_policy_input
    import aws_sdk_mediastore.types.delete_cors_policy_output
    import aws_sdk_mediastore.types.delete_lifecycle_policy_input
    import aws_sdk_mediastore.types.delete_lifecycle_policy_output
    import aws_sdk_mediastore.types.delete_metric_policy_input
    import aws_sdk_mediastore.types.delete_metric_policy_output
    import aws_sdk_mediastore.types.describe_container_input
    import aws_sdk_mediastore.types.describe_container_output
    import aws_sdk_mediastore.types.get_container_policy_input
    import aws_sdk_mediastore.types.get_container_policy_output
    import aws_sdk_mediastore.types.get_cors_policy_input
    import aws_sdk_mediastore.types.get_cors_policy_output
    import aws_sdk_mediastore.types.get_lifecycle_policy_input
    import aws_sdk_mediastore.types.get_lifecycle_policy_output
    import aws_sdk_mediastore.types.get_metric_policy_input
    import aws_sdk_mediastore.types.get_metric_policy_output
    import aws_sdk_mediastore.types.lifecycle_policy
    import aws_sdk_mediastore.types.list_containers_input
    import aws_sdk_mediastore.types.list_containers_output
    import aws_sdk_mediastore.types.list_tags_for_resource_input
    import aws_sdk_mediastore.types.list_tags_for_resource_output
    import aws_sdk_mediastore.types.metric_policy
    import aws_sdk_mediastore.types.pagination_token
    import aws_sdk_mediastore.types.put_container_policy_input
    import aws_sdk_mediastore.types.put_container_policy_output
    import aws_sdk_mediastore.types.put_cors_policy_input
    import aws_sdk_mediastore.types.put_cors_policy_output
    import aws_sdk_mediastore.types.put_lifecycle_policy_input
    import aws_sdk_mediastore.types.put_lifecycle_policy_output
    import aws_sdk_mediastore.types.put_metric_policy_input
    import aws_sdk_mediastore.types.put_metric_policy_output
    import aws_sdk_mediastore.types.start_access_logging_input
    import aws_sdk_mediastore.types.start_access_logging_output
    import aws_sdk_mediastore.types.stop_access_logging_input
    import aws_sdk_mediastore.types.stop_access_logging_output
    import aws_sdk_mediastore.types.tag_key_list
    import aws_sdk_mediastore.types.tag_list
    import aws_sdk_mediastore.types.tag_resource_input
    import aws_sdk_mediastore.types.tag_resource_output
    import aws_sdk_mediastore.types.untag_resource_input
    import aws_sdk_mediastore.types.untag_resource_output


class AsyncMediaStoreClientConfig(TypedDict, total=False):
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


class AsyncMediaStoreClient:
    """A client for the ``MediaStore`` service.

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
        self.config = AsyncMediaStoreClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncMediaStoreClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMediaStoreClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def create_container(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
        tags: Optional["aws_sdk_mediastore.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_mediastore.types.create_container_output.CreateContainerOutput":
        """<p>Creates a storage container to hold objects. A container is similar to a bucket in the Amazon S3 service.</p>

        Args:
            container_name: <p>The name for the container. The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named <code>movies</code> in every region, as long as you don’t have an existing container with that name.</p>
            tags: <p>An array of key:value pairs that you define. These values can be anything that you want. Typically, the tag key represents a category (such as \"environment\") and the tag value represents a specific value within that category (such as \"test,\" \"development,\" or \"production\"). You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see <a href=\"https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html\">Tagging Resources in MediaStore</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.create_container_input.CreateContainerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.create_container_output.CreateContainerOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.create_container

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.create_container.async_create_container(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.create_container_input.CreateContainerInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_container(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.delete_container_output.DeleteContainerOutput":
        """<p>Deletes the specified container. Before you make a <code>DeleteContainer</code> request, delete any objects in the container or in any folders in the container. You can delete only empty containers. </p>

        Args:
            container_name: <p>The name of the container to delete. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.delete_container_input.DeleteContainerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.delete_container_output.DeleteContainerOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.delete_container

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.delete_container.async_delete_container(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.delete_container_input.DeleteContainerInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_container_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.delete_container_policy_output.DeleteContainerPolicyOutput":
        """<p>Deletes the access policy that is associated with the specified container.</p>

        Args:
            container_name: <p>The name of the container that holds the policy.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.delete_container_policy_input.DeleteContainerPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.delete_container_policy_output.DeleteContainerPolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.delete_container_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.delete_container_policy.async_delete_container_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.delete_container_policy_input.DeleteContainerPolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_cors_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.delete_cors_policy_output.DeleteCorsPolicyOutput":
        """<p>Deletes the cross-origin resource sharing (CORS) configuration information that is set for the container.</p> <p>To use this operation, you must have permission to perform the <code>MediaStore:DeleteCorsPolicy</code> action. The container owner has this permission by default and can grant this permission to others.</p>

        Args:
            container_name: <p>The name of the container to remove the policy from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.delete_cors_policy_input.DeleteCorsPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.delete_cors_policy_output.DeleteCorsPolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.delete_cors_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.delete_cors_policy.async_delete_cors_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.delete_cors_policy_input.DeleteCorsPolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_lifecycle_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.delete_lifecycle_policy_output.DeleteLifecyclePolicyOutput":
        """<p>Removes an object lifecycle policy from a container. It takes up to 20 minutes for the change to take effect.</p>

        Args:
            container_name: <p>The name of the container that holds the object lifecycle policy.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.delete_lifecycle_policy_input.DeleteLifecyclePolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.delete_lifecycle_policy_output.DeleteLifecyclePolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.delete_lifecycle_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.delete_lifecycle_policy.async_delete_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.delete_lifecycle_policy_input.DeleteLifecyclePolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_metric_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> (
        "aws_sdk_mediastore.types.delete_metric_policy_output.DeleteMetricPolicyOutput"
    ):
        """<p>Deletes the metric policy that is associated with the specified container. If there is no metric policy associated with the container, MediaStore doesn't send metrics to CloudWatch.</p>

        Args:
            container_name: <p>The name of the container that is associated with the metric policy that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.delete_metric_policy_input.DeleteMetricPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.delete_metric_policy_output.DeleteMetricPolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.delete_metric_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.delete_metric_policy.async_delete_metric_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.delete_metric_policy_input.DeleteMetricPolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_container(
        self,
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
        container_name: Optional[
            "aws_sdk_mediastore.types.container_name.ContainerName"
        ] = None,
    ) -> "aws_sdk_mediastore.types.describe_container_output.DescribeContainerOutput":
        """<p>Retrieves the properties of the requested container. This request is commonly used to retrieve the endpoint of a container. An endpoint is a value assigned by the service when a new container is created. A container's endpoint does not change after it has been assigned. The <code>DescribeContainer</code> request returns a single <code>Container</code> object based on <code>ContainerName</code>. To return all <code>Container</code> objects that are associated with a specified AWS account, use <a>ListContainers</a>.</p>

        Args:
            container_name: <p>The name of the container to query.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.describe_container_input.DescribeContainerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.describe_container_output.DescribeContainerOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.describe_container

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.describe_container.async_describe_container(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.describe_container_input.DescribeContainerInput = {}  # type: ignore[typeddict-item]
        if container_name is not None:
            input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_container_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> (
        "aws_sdk_mediastore.types.get_container_policy_output.GetContainerPolicyOutput"
    ):
        """<p>Retrieves the access policy for the specified container. For information about the data that is included in an access policy, see the <a href=\"https://aws.amazon.com/documentation/iam/\">AWS Identity and Access Management User Guide</a>.</p>

        Args:
            container_name: <p>The name of the container. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.get_container_policy_input.GetContainerPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.get_container_policy_output.GetContainerPolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.get_container_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.get_container_policy.async_get_container_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.get_container_policy_input.GetContainerPolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_cors_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.get_cors_policy_output.GetCorsPolicyOutput":
        """<p>Returns the cross-origin resource sharing (CORS) configuration information that is set for the container.</p> <p>To use this operation, you must have permission to perform the <code>MediaStore:GetCorsPolicy</code> action. By default, the container owner has this permission and can grant it to others.</p>

        Args:
            container_name: <p>The name of the container that the policy is assigned to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.get_cors_policy_input.GetCorsPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.get_cors_policy_output.GetCorsPolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.get_cors_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.get_cors_policy.async_get_cors_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.get_cors_policy_input.GetCorsPolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_lifecycle_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> (
        "aws_sdk_mediastore.types.get_lifecycle_policy_output.GetLifecyclePolicyOutput"
    ):
        """<p>Retrieves the object lifecycle policy that is assigned to a container.</p>

        Args:
            container_name: <p>The name of the container that the object lifecycle policy is assigned to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.get_lifecycle_policy_input.GetLifecyclePolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.get_lifecycle_policy_output.GetLifecyclePolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.get_lifecycle_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.get_lifecycle_policy.async_get_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.get_lifecycle_policy_input.GetLifecyclePolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_metric_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.get_metric_policy_output.GetMetricPolicyOutput":
        """<p>Returns the metric policy for the specified container. </p>

        Args:
            container_name: <p>The name of the container that is associated with the metric policy.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.get_metric_policy_input.GetMetricPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.get_metric_policy_output.GetMetricPolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.get_metric_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.get_metric_policy.async_get_metric_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.get_metric_policy_input.GetMetricPolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_containers(
        self,
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
        next_token: Optional[
            "aws_sdk_mediastore.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_mediastore.types.container_list_limit.ContainerListLimit"
        ] = None,
    ) -> "aws_sdk_mediastore.types.list_containers_output.ListContainersOutput":
        """<p>Lists the properties of all containers in AWS Elemental MediaStore. </p> <p>You can query to receive all the containers in one response. Or you can include the <code>MaxResults</code> parameter to receive a limited number of containers in each response. In this case, the response includes a token. To get the next set of containers, send the command again, this time with the <code>NextToken</code> parameter (with the returned token as its value). The next set of responses appears, with a token if there are still more containers to receive. </p> <p>See also <a>DescribeContainer</a>, which gets the properties of one container. </p>

        Args:
            next_token: <p>Only if you used <code>MaxResults</code> in the first command, enter the token (which was included in the previous response) to obtain the next set of containers. This token is included in a response only if there actually are more containers to list.</p>
            max_results: <p>Enter the maximum number of containers in the response. Use from 1 to 255 characters. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.list_containers_input.ListContainersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.list_containers_output.ListContainersOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.list_containers

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.list_containers.async_list_containers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.list_containers_input.ListContainersInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource: "aws_sdk_mediastore.types.container_arn.ContainerARN",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns a list of the tags assigned to the specified container. </p>

        Args:
            resource: <p>The Amazon Resource Name (ARN) for the container.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input["resource"] = resource

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_container_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        policy: "aws_sdk_mediastore.types.container_policy.ContainerPolicy",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> (
        "aws_sdk_mediastore.types.put_container_policy_output.PutContainerPolicyOutput"
    ):
        """<p>Creates an access policy for the specified container to restrict the users and clients that can access it. For information about the data that is included in an access policy, see the <a href=\"https://aws.amazon.com/documentation/iam/\">AWS Identity and Access Management User Guide</a>.</p> <p>For this release of the REST API, you can create only one policy for a container. If you enter <code>PutContainerPolicy</code> twice, the second command modifies the existing policy. </p>

        Args:
            container_name: <p>The name of the container.</p>
            policy: <p>The contents of the policy, which includes the following: </p> <ul> <li> <p>One <code>Version</code> tag</p> </li> <li> <p>One <code>Statement</code> tag that contains the standard tags for the policy.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.put_container_policy_input.PutContainerPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.put_container_policy_output.PutContainerPolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.put_container_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.put_container_policy.async_put_container_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.put_container_policy_input.PutContainerPolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name
        input["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_cors_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        cors_policy: "aws_sdk_mediastore.types.cors_policy.CorsPolicy",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.put_cors_policy_output.PutCorsPolicyOutput":
        """<p>Sets the cross-origin resource sharing (CORS) configuration on a container so that the container can service cross-origin requests. For example, you might want to enable a request whose origin is http://www.example.com to access your AWS Elemental MediaStore container at my.example.container.com by using the browser's XMLHttpRequest capability.</p> <p>To enable CORS on a container, you attach a CORS policy to the container. In the CORS policy, you configure rules that identify origins and the HTTP methods that can be executed on your container. The policy can contain up to 398,000 characters. You can add up to 100 rules to a CORS policy. If more than one rule applies, the service uses the first applicable rule listed.</p> <p>To learn more about CORS, see <a href=\"https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy.html\">Cross-Origin Resource Sharing (CORS) in AWS Elemental MediaStore</a>.</p>

        Args:
            container_name: <p>The name of the container that you want to assign the CORS policy to.</p>
            cors_policy: <p>The CORS policy to apply to the container. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.put_cors_policy_input.PutCorsPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.put_cors_policy_output.PutCorsPolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.put_cors_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.put_cors_policy.async_put_cors_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.put_cors_policy_input.PutCorsPolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name
        input["cors_policy"] = cors_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_lifecycle_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        lifecycle_policy: "aws_sdk_mediastore.types.lifecycle_policy.LifecyclePolicy",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> (
        "aws_sdk_mediastore.types.put_lifecycle_policy_output.PutLifecyclePolicyOutput"
    ):
        """<p>Writes an object lifecycle policy to a container. If the container already has an object lifecycle policy, the service replaces the existing policy with the new policy. It takes up to 20 minutes for the change to take effect.</p> <p>For information about how to construct an object lifecycle policy, see <a href=\"https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle-components.html\">Components of an Object Lifecycle Policy</a>.</p>

        Args:
            container_name: <p>The name of the container that you want to assign the object lifecycle policy to.</p>
            lifecycle_policy: <p>The object lifecycle policy to apply to the container.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.put_lifecycle_policy_input.PutLifecyclePolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.put_lifecycle_policy_output.PutLifecyclePolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.put_lifecycle_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.put_lifecycle_policy.async_put_lifecycle_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.put_lifecycle_policy_input.PutLifecyclePolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name
        input["lifecycle_policy"] = lifecycle_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_metric_policy(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        metric_policy: "aws_sdk_mediastore.types.metric_policy.MetricPolicy",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.put_metric_policy_output.PutMetricPolicyOutput":
        """<p>The metric policy that you want to add to the container. A metric policy allows AWS Elemental MediaStore to send metrics to Amazon CloudWatch. It takes up to 20 minutes for the new policy to take effect.</p>

        Args:
            container_name: <p>The name of the container that you want to add the metric policy to.</p>
            metric_policy: <p>The metric policy that you want to associate with the container. In the policy, you must indicate whether you want MediaStore to send container-level metrics. You can also include up to five rules to define groups of objects that you want MediaStore to send object-level metrics for. If you include rules in the policy, construct each rule with both of the following:</p> <ul> <li> <p>An object group that defines which objects to include in the group. The definition can be a path or a file name, but it can't have more than 900 characters. Valid characters are: a-z, A-Z, 0-9, _ (underscore), = (equal), : (colon), . (period), - (hyphen), ~ (tilde), / (forward slash), and * (asterisk). Wildcards (*) are acceptable.</p> </li> <li> <p>An object group name that allows you to refer to the object group. The name can't have more than 30 characters. Valid characters are: a-z, A-Z, 0-9, and _ (underscore).</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.put_metric_policy_input.PutMetricPolicyInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.put_metric_policy_output.PutMetricPolicyOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.put_metric_policy

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.put_metric_policy.async_put_metric_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.put_metric_policy_input.PutMetricPolicyInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name
        input["metric_policy"] = metric_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_access_logging(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> (
        "aws_sdk_mediastore.types.start_access_logging_output.StartAccessLoggingOutput"
    ):
        """<p>Starts access logging on the specified container. When you enable access logging on a container, MediaStore delivers access logs for objects stored in that container to Amazon CloudWatch Logs.</p>

        Args:
            container_name: <p>The name of the container that you want to start access logging on.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.start_access_logging_input.StartAccessLoggingInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.start_access_logging_output.StartAccessLoggingOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.start_access_logging

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.start_access_logging.async_start_access_logging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.start_access_logging_input.StartAccessLoggingInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_access_logging(
        self,
        container_name: "aws_sdk_mediastore.types.container_name.ContainerName",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.stop_access_logging_output.StopAccessLoggingOutput":
        """<p>Stops access logging on the specified container. When you stop access logging on a container, MediaStore stops sending access logs to Amazon CloudWatch Logs. These access logs are not saved and are not retrievable.</p>

        Args:
            container_name: <p>The name of the container that you want to stop access logging on.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.stop_access_logging_input.StopAccessLoggingInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.stop_access_logging_output.StopAccessLoggingOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.stop_access_logging

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.stop_access_logging.async_stop_access_logging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.stop_access_logging_input.StopAccessLoggingInput = {}  # type: ignore[typeddict-item]
        input["container_name"] = container_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource: "aws_sdk_mediastore.types.container_arn.ContainerARN",
        tags: "aws_sdk_mediastore.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.tag_resource_output.TagResourceOutput":
        """<p>Adds tags to the specified AWS Elemental MediaStore container. Tags are key:value pairs that you can associate with AWS resources. For example, the tag key might be \"customer\" and the tag value might be \"companyA.\" You can specify one or more tags to add to each container. You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see <a href=\"https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html\">Tagging Resources in MediaStore</a>.</p>

        Args:
            resource: <p>The Amazon Resource Name (ARN) for the container. </p>
            tags: <p>An array of key:value pairs that you want to add to the container. You need to specify only the tags that you want to add or update. For example, suppose a container already has two tags (customer:CompanyA and priority:High). You want to change the priority tag and also add a third tag (type:Contract). For TagResource, you specify the following tags: priority:Medium, type:Contract. The result is that your container has three tags: customer:CompanyA, priority:Medium, and type:Contract.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input["resource"] = resource
        input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource: "aws_sdk_mediastore.types.container_arn.ContainerARN",
        tag_keys: "aws_sdk_mediastore.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncMediaStoreClientConfig] = None,
    ) -> "aws_sdk_mediastore.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from the specified container. You can specify one or more tags to remove. </p>

        Args:
            resource: <p>The Amazon Resource Name (ARN) for the container.</p>
            tag_keys: <p>A comma-separated list of keys for tags that you want to remove from the container. For example, if your container has two tags (customer:CompanyA and priority:High) and you want to remove one of the tags (priority:High), you specify the key for the tag that you want to remove (priority).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediastore.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediastore.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_mediastore._operations.media_store_20170901.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_mediastore._operations.media_store_20170901.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_mediastore.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input["resource"] = resource
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
