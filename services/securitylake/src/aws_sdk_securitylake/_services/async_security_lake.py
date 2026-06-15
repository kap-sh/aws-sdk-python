"""Generated from Smithy shape ``com.amazonaws.securitylake#SecurityLake``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_securitylake._auth._signers
import aws_sdk_securitylake._auth._sigv4
from aws_sdk_securitylake._auth._identity import Credentials
from aws_sdk_securitylake._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_securitylake._auth._zapros_handler import AuthMiddleware
from aws_sdk_securitylake._pagination import resolve_path as _resolve_path
from aws_sdk_securitylake._resources.security_lake.data_lake import AsyncDataLake
from aws_sdk_securitylake._resources.security_lake.subscriber import AsyncSubscriber
from aws_sdk_securitylake._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.amazon_resource_name
    import aws_sdk_securitylake.types.create_data_lake_exception_subscription_request
    import aws_sdk_securitylake.types.create_data_lake_exception_subscription_response
    import aws_sdk_securitylake.types.data_lake_exception
    import aws_sdk_securitylake.types.delete_data_lake_exception_subscription_request
    import aws_sdk_securitylake.types.delete_data_lake_exception_subscription_response
    import aws_sdk_securitylake.types.deregister_data_lake_delegated_administrator_request
    import aws_sdk_securitylake.types.deregister_data_lake_delegated_administrator_response
    import aws_sdk_securitylake.types.get_data_lake_exception_subscription_request
    import aws_sdk_securitylake.types.get_data_lake_exception_subscription_response
    import aws_sdk_securitylake.types.list_data_lake_exceptions_request
    import aws_sdk_securitylake.types.list_data_lake_exceptions_response
    import aws_sdk_securitylake.types.list_tags_for_resource_request
    import aws_sdk_securitylake.types.list_tags_for_resource_response
    import aws_sdk_securitylake.types.max_results
    import aws_sdk_securitylake.types.next_token
    import aws_sdk_securitylake.types.region_list
    import aws_sdk_securitylake.types.register_data_lake_delegated_administrator_request
    import aws_sdk_securitylake.types.register_data_lake_delegated_administrator_response
    import aws_sdk_securitylake.types.safe_string
    import aws_sdk_securitylake.types.subscription_protocol
    import aws_sdk_securitylake.types.tag_key_list
    import aws_sdk_securitylake.types.tag_list
    import aws_sdk_securitylake.types.tag_resource_request
    import aws_sdk_securitylake.types.tag_resource_response
    import aws_sdk_securitylake.types.untag_resource_request
    import aws_sdk_securitylake.types.untag_resource_response
    import aws_sdk_securitylake.types.update_data_lake_exception_subscription_request
    import aws_sdk_securitylake.types.update_data_lake_exception_subscription_response


class AsyncSecurityLakeClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncSecurityLakeClient:
    """A client for the ``SecurityLake`` service.

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
        self._config = AsyncSecurityLakeClientConfig(
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
        self.data_lake = AsyncDataLake(self)
        self.subscriber = AsyncSubscriber(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSecurityLakeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSecurityLakeClientConfig = config_overrides or {}
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

    async def create_data_lake_exception_subscription(
        self,
        subscription_protocol: "aws_sdk_securitylake.types.subscription_protocol.SubscriptionProtocol",
        notification_endpoint: "aws_sdk_securitylake.types.safe_string.SafeString",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        exception_time_to_live: Optional[int] = None,
    ) -> "aws_sdk_securitylake.types.create_data_lake_exception_subscription_response.CreateDataLakeExceptionSubscriptionResponse":
        """<p>Creates the specified notification subscription in Amazon Security Lake for the organization you specify. The notification subscription is created for exceptions that cannot be resolved by Security Lake automatically.</p>

        Args:
            subscription_protocol: <p>The subscription protocol to which exception notifications are posted.</p>
            notification_endpoint: <p>The Amazon Web Services account where you want to receive exception notifications.</p>
            exception_time_to_live: <p>The expiration period and time-to-live (TTL). It is the duration of time until which the exception message remains.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.create_data_lake_exception_subscription_request.CreateDataLakeExceptionSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.create_data_lake_exception_subscription_response.CreateDataLakeExceptionSubscriptionResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.create_data_lake_exception_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.create_data_lake_exception_subscription.async_create_data_lake_exception_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.create_data_lake_exception_subscription_request.CreateDataLakeExceptionSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["subscription_protocol"] = subscription_protocol
        input_["notification_endpoint"] = notification_endpoint
        if exception_time_to_live is not None:
            input_["exception_time_to_live"] = exception_time_to_live

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_data_lake_exception_subscription(
        self, *, config_overrides: Optional[AsyncSecurityLakeClientConfig] = None
    ) -> "aws_sdk_securitylake.types.delete_data_lake_exception_subscription_response.DeleteDataLakeExceptionSubscriptionResponse":
        """<p>Deletes the specified notification subscription in Amazon Security Lake for the organization you specify.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.delete_data_lake_exception_subscription_request.DeleteDataLakeExceptionSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.delete_data_lake_exception_subscription_response.DeleteDataLakeExceptionSubscriptionResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.delete_data_lake_exception_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.delete_data_lake_exception_subscription.async_delete_data_lake_exception_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.delete_data_lake_exception_subscription_request.DeleteDataLakeExceptionSubscriptionRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def deregister_data_lake_delegated_administrator(
        self, *, config_overrides: Optional[AsyncSecurityLakeClientConfig] = None
    ) -> "aws_sdk_securitylake.types.deregister_data_lake_delegated_administrator_response.DeregisterDataLakeDelegatedAdministratorResponse":
        """<p>Deletes the Amazon Security Lake delegated administrator account for the organization. This API can only be called by the organization management account. The organization management account cannot be the delegated administrator account.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.deregister_data_lake_delegated_administrator_request.DeregisterDataLakeDelegatedAdministratorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.deregister_data_lake_delegated_administrator_response.DeregisterDataLakeDelegatedAdministratorResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.deregister_data_lake_delegated_administrator

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.deregister_data_lake_delegated_administrator.async_deregister_data_lake_delegated_administrator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.deregister_data_lake_delegated_administrator_request.DeregisterDataLakeDelegatedAdministratorRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_lake_exception_subscription(
        self, *, config_overrides: Optional[AsyncSecurityLakeClientConfig] = None
    ) -> "aws_sdk_securitylake.types.get_data_lake_exception_subscription_response.GetDataLakeExceptionSubscriptionResponse":
        """<p>Retrieves the protocol and endpoint that were provided when subscribing to Amazon SNS topics for exception notifications.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.get_data_lake_exception_subscription_request.GetDataLakeExceptionSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.get_data_lake_exception_subscription_response.GetDataLakeExceptionSubscriptionResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.get_data_lake_exception_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.get_data_lake_exception_subscription.async_get_data_lake_exception_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.get_data_lake_exception_subscription_request.GetDataLakeExceptionSubscriptionRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_data_lake_exceptions(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        regions: Optional["aws_sdk_securitylake.types.region_list.RegionList"] = None,
        max_results: Optional[
            "aws_sdk_securitylake.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securitylake.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_securitylake.types.list_data_lake_exceptions_response.ListDataLakeExceptionsResponse":
        """<p>Lists the Amazon Security Lake exceptions that you can use to find the source of problems and fix them.</p>

        Args:
            regions: <p>The Amazon Web Services Regions from which exceptions are retrieved.</p>
            max_results: <p>Lists the maximum number of failures in Security Lake.</p>
            next_token: <p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.list_data_lake_exceptions_request.ListDataLakeExceptionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.list_data_lake_exceptions_response.ListDataLakeExceptionsResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.list_data_lake_exceptions

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.list_data_lake_exceptions.async_list_data_lake_exceptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.list_data_lake_exceptions_request.ListDataLakeExceptionsRequest = {}  # type: ignore[typeddict-item]
        if regions is not None:
            input_["regions"] = regions
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_data_lake_exceptions(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        regions: Optional["aws_sdk_securitylake.types.region_list.RegionList"] = None,
        max_results: Optional[
            "aws_sdk_securitylake.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_securitylake.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_securitylake.types.data_lake_exception.DataLakeException]":
        _token = next_token
        while True:
            _response = await self.list_data_lake_exceptions(
                config_overrides=config_overrides,
                regions=regions,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("exceptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_securitylake.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the tags (keys and values) that are associated with an Amazon Security Lake resource: a subscriber, or the data lake configuration for your Amazon Web Services account in a particular Amazon Web Services Region.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Security Lake resource for which you want to retrieve the tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def register_data_lake_delegated_administrator(
        self,
        account_id: "aws_sdk_securitylake.types.safe_string.SafeString",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.register_data_lake_delegated_administrator_response.RegisterDataLakeDelegatedAdministratorResponse":
        """<p>Designates the Amazon Security Lake delegated administrator account for the organization. This API can only be called by the organization management account. The organization management account cannot be the delegated administrator account.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Security Lake delegated administrator.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.register_data_lake_delegated_administrator_request.RegisterDataLakeDelegatedAdministratorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.register_data_lake_delegated_administrator_response.RegisterDataLakeDelegatedAdministratorResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.register_data_lake_delegated_administrator

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.register_data_lake_delegated_administrator.async_register_data_lake_delegated_administrator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.register_data_lake_delegated_administrator_request.RegisterDataLakeDelegatedAdministratorRequest = {}  # type: ignore[typeddict-item]
        input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_securitylake.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_securitylake.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.tag_resource_response.TagResourceResponse":
        r"""<p>Adds or updates one or more tags that are associated with an Amazon Security Lake resource: a subscriber, or the data lake configuration for your Amazon Web Services account in a particular Amazon Web Services Region. A <i>tag</i> is a label that you can define and associate with Amazon Web Services resources. Each tag consists of a required <i>tag key</i> and an associated <i>tag value</i>. A <i>tag key</i> is a general label that acts as a category for a more specific tag value. A <i>tag value</i> acts as a descriptor for a tag key. Tags can help you identify, categorize, and manage resources in different ways, such as by owner, environment, or other criteria. For more information, see <a href=\"https://docs.aws.amazon.com/security-lake/latest/userguide/tagging-resources.html\">Tagging Amazon Security Lake resources</a> in the <i>Amazon Security Lake User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Security Lake resource to add or update the tags for.</p>
            tags: <p>An array of objects, one for each tag (key and value) to associate with the Amazon Security Lake resource. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_securitylake.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_securitylake.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "aws_sdk_securitylake.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags (keys and values) from an Amazon Security Lake resource: a subscriber, or the data lake configuration for your Amazon Web Services account in a particular Amazon Web Services Region.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Security Lake resource to remove one or more tags from.</p>
            tag_keys: <p>A list of one or more tag keys. For each value in the list, specify the tag key for a tag to remove from the Amazon Security Lake resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_data_lake_exception_subscription(
        self,
        subscription_protocol: "aws_sdk_securitylake.types.subscription_protocol.SubscriptionProtocol",
        notification_endpoint: "aws_sdk_securitylake.types.safe_string.SafeString",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        exception_time_to_live: Optional[int] = None,
    ) -> "aws_sdk_securitylake.types.update_data_lake_exception_subscription_response.UpdateDataLakeExceptionSubscriptionResponse":
        """<p>Updates the specified notification subscription in Amazon Security Lake for the organization you specify.</p>

        Args:
            subscription_protocol: <p>The subscription protocol to which exception messages are posted.</p>
            notification_endpoint: <p>The account that is subscribed to receive exception notifications.</p>
            exception_time_to_live: <p>The time-to-live (TTL) for the exception message to remain. It is the duration of time until which the exception message remains. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securitylake.types.update_data_lake_exception_subscription_request.UpdateDataLakeExceptionSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securitylake.types.update_data_lake_exception_subscription_response.UpdateDataLakeExceptionSubscriptionResponse"
        ]:
            import aws_sdk_securitylake._operations.security_lake.update_data_lake_exception_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_securitylake._operations.security_lake.update_data_lake_exception_subscription.async_update_data_lake_exception_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_securitylake.types.update_data_lake_exception_subscription_request.UpdateDataLakeExceptionSubscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["subscription_protocol"] = subscription_protocol
        input_["notification_endpoint"] = notification_endpoint
        if exception_time_to_live is not None:
            input_["exception_time_to_live"] = exception_time_to_live

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
