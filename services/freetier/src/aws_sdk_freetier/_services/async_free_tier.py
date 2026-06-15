"""Generated from Smithy shape ``com.amazonaws.freetier#AWSFreeTierService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_freetier._auth._signers
import aws_sdk_freetier._auth._sigv4
from aws_sdk_freetier._auth._identity import Credentials
from aws_sdk_freetier._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_freetier._auth._zapros_handler import AuthMiddleware
from aws_sdk_freetier._pagination import resolve_path as _resolve_path
from aws_sdk_freetier._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_freetier.types.account_plan_type
    import aws_sdk_freetier.types.activity_id
    import aws_sdk_freetier.types.activity_summary
    import aws_sdk_freetier.types.expression
    import aws_sdk_freetier.types.filter_activity_statuses
    import aws_sdk_freetier.types.free_tier_usage
    import aws_sdk_freetier.types.get_account_activity_request
    import aws_sdk_freetier.types.get_account_activity_response
    import aws_sdk_freetier.types.get_account_plan_state_request
    import aws_sdk_freetier.types.get_account_plan_state_response
    import aws_sdk_freetier.types.get_free_tier_usage_request
    import aws_sdk_freetier.types.get_free_tier_usage_response
    import aws_sdk_freetier.types.language_code
    import aws_sdk_freetier.types.list_account_activities_request
    import aws_sdk_freetier.types.list_account_activities_response
    import aws_sdk_freetier.types.max_results
    import aws_sdk_freetier.types.next_page_token
    import aws_sdk_freetier.types.upgrade_account_plan_request
    import aws_sdk_freetier.types.upgrade_account_plan_response


class AsyncFreeTierClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncFreeTierClient:
    """A client for the ``FreeTier`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
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
        self._config = AsyncFreeTierClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncFreeTierClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncFreeTierClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def get_account_activity(
        self,
        activity_id: "aws_sdk_freetier.types.activity_id.ActivityId",
        *,
        config_overrides: Optional[AsyncFreeTierClientConfig] = None,
        language_code: Optional[
            "aws_sdk_freetier.types.language_code.LanguageCode"
        ] = None,
    ) -> "aws_sdk_freetier.types.get_account_activity_response.GetAccountActivityResponse":
        """<p> Returns a specific activity record that is available to the customer. </p>

        Args:
            activity_id: <p> A unique identifier that identifies the activity. </p>
            language_code: <p> The language code used to return translated title and description fields. </p>

        Examples:
            Fetching an Account activity by id

            >>> await client.get_account_activity(activity_id='d622f48bf4014286a2686ab10cacfb2e', language_code='en-US')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_freetier.types.get_account_activity_request.GetAccountActivityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_freetier.types.get_account_activity_response.GetAccountActivityResponse"
        ]:
            import aws_sdk_freetier._operations.aws_free_tier_service.get_account_activity

            (
                output,
                http_response,
            ) = await aws_sdk_freetier._operations.aws_free_tier_service.get_account_activity.async_get_account_activity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_freetier.types.get_account_activity_request.GetAccountActivityRequest = {}  # type: ignore[typeddict-item]
        input_["activity_id"] = activity_id
        if language_code is not None:
            input_["language_code"] = language_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_account_plan_state(
        self, *, config_overrides: Optional[AsyncFreeTierClientConfig] = None
    ) -> "aws_sdk_freetier.types.get_account_plan_state_response.GetAccountPlanStateResponse":
        """<p> This returns all of the information related to the state of the account plan related to Free Tier. </p>

        Examples:
            Fetching account plan state by id

            >>> await client.get_account_plan_state()
            Attempt to fetch account plan state by id with insufficient permissions

            >>> await client.get_account_plan_state()
            Internal service error

            >>> await client.get_account_plan_state()
            Attempt to fetch plan state by id for an account without account plan

            >>> await client.get_account_plan_state()
            Request rate exceeds limits

            >>> await client.get_account_plan_state()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_freetier.types.get_account_plan_state_request.GetAccountPlanStateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_freetier.types.get_account_plan_state_response.GetAccountPlanStateResponse"
        ]:
            import aws_sdk_freetier._operations.aws_free_tier_service.get_account_plan_state

            (
                output,
                http_response,
            ) = await aws_sdk_freetier._operations.aws_free_tier_service.get_account_plan_state.async_get_account_plan_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_freetier.types.get_account_plan_state_request.GetAccountPlanStateRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_free_tier_usage(
        self,
        *,
        config_overrides: Optional[AsyncFreeTierClientConfig] = None,
        filter: Optional["aws_sdk_freetier.types.expression.Expression"] = None,
        max_results: Optional["aws_sdk_freetier.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_freetier.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "aws_sdk_freetier.types.get_free_tier_usage_response.GetFreeTierUsageResponse":
        """<p>Returns a list of all Free Tier usage objects that match your filters.</p>

        Args:
            filter: <p>An expression that specifies the conditions that you want each <code>FreeTierUsage</code> object to meet.</p>
            max_results: <p>The maximum number of results to return in the response. <code>MaxResults</code> means that there can be up to the specified number of values, but there might be fewer results based on your filters.</p>
            next_token: <p>The pagination token that indicates the next set of results to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_freetier.types.get_free_tier_usage_request.GetFreeTierUsageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_freetier.types.get_free_tier_usage_response.GetFreeTierUsageResponse"
        ]:
            import aws_sdk_freetier._operations.aws_free_tier_service.get_free_tier_usage

            (
                output,
                http_response,
            ) = await aws_sdk_freetier._operations.aws_free_tier_service.get_free_tier_usage.async_get_free_tier_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_freetier.types.get_free_tier_usage_request.GetFreeTierUsageRequest = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_get_free_tier_usage(
        self,
        *,
        config_overrides: Optional[AsyncFreeTierClientConfig] = None,
        filter: Optional["aws_sdk_freetier.types.expression.Expression"] = None,
        max_results: Optional["aws_sdk_freetier.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_freetier.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_freetier.types.free_tier_usage.FreeTierUsage]":
        _token = next_token
        while True:
            _response = await self.get_free_tier_usage(
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("free_tier_usages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_account_activities(
        self,
        *,
        config_overrides: Optional[AsyncFreeTierClientConfig] = None,
        filter_activity_statuses: Optional[
            "aws_sdk_freetier.types.filter_activity_statuses.FilterActivityStatuses"
        ] = None,
        next_token: Optional[
            "aws_sdk_freetier.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["aws_sdk_freetier.types.max_results.MaxResults"] = None,
        language_code: Optional[
            "aws_sdk_freetier.types.language_code.LanguageCode"
        ] = None,
    ) -> "aws_sdk_freetier.types.list_account_activities_response.ListAccountActivitiesResponse":
        """<p> Returns a list of activities that are available. This operation supports pagination and filtering by status. </p>

        Args:
            filter_activity_statuses: <p> The activity status filter. This field can be used to filter the response by activities status. </p>
            next_token: <p> A token from a previous paginated response. If this is specified, the response includes records beginning from this token (inclusive), up to the number specified by <code>maxResults</code>. </p>
            max_results: <p> The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. </p>
            language_code: <p> The language code used to return translated titles. </p>

        Examples:
            Fetching a page of completed activities

            >>> await client.list_account_activities(filter_activity_statuses=['COMPLETED'], max_results=1, language_code='en-US')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_freetier.types.list_account_activities_request.ListAccountActivitiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_freetier.types.list_account_activities_response.ListAccountActivitiesResponse"
        ]:
            import aws_sdk_freetier._operations.aws_free_tier_service.list_account_activities

            (
                output,
                http_response,
            ) = await aws_sdk_freetier._operations.aws_free_tier_service.list_account_activities.async_list_account_activities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_freetier.types.list_account_activities_request.ListAccountActivitiesRequest = {}  # type: ignore[typeddict-item]
        if filter_activity_statuses is not None:
            input_["filter_activity_statuses"] = filter_activity_statuses
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if language_code is not None:
            input_["language_code"] = language_code

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_account_activities(
        self,
        *,
        config_overrides: Optional[AsyncFreeTierClientConfig] = None,
        filter_activity_statuses: Optional[
            "aws_sdk_freetier.types.filter_activity_statuses.FilterActivityStatuses"
        ] = None,
        next_token: Optional[
            "aws_sdk_freetier.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["aws_sdk_freetier.types.max_results.MaxResults"] = None,
        language_code: Optional[
            "aws_sdk_freetier.types.language_code.LanguageCode"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_freetier.types.activity_summary.ActivitySummary]":
        _token = next_token
        while True:
            _response = await self.list_account_activities(
                config_overrides=config_overrides,
                filter_activity_statuses=filter_activity_statuses,
                next_token=_token,
                max_results=max_results,
                language_code=language_code,
            )
            _page = _resolve_path(_response, ("activities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def upgrade_account_plan(
        self,
        account_plan_type: "aws_sdk_freetier.types.account_plan_type.AccountPlanType",
        *,
        config_overrides: Optional[AsyncFreeTierClientConfig] = None,
    ) -> "aws_sdk_freetier.types.upgrade_account_plan_response.UpgradeAccountPlanResponse":
        """<p> The account plan type for the Amazon Web Services account. </p>

        Args:
            account_plan_type: <p> The target account plan type. This makes it explicit about the change and latest value of the <code>accountPlanType</code>. </p>

        Examples:
            Upgrading an account plan to PAID

            >>> await client.upgrade_account_plan(account_plan_type='PAID')
            Attempt to upgrade an account with insufficient permissions

            >>> await client.upgrade_account_plan(account_plan_type='PAID')
            Attempt to downgrade an account from PAID to FREE

            >>> await client.upgrade_account_plan(account_plan_type='FREE')
            Internal service error

            >>> await client.upgrade_account_plan(account_plan_type='PAID')
            Attempt to upgrade a non-existent account plan

            >>> await client.upgrade_account_plan(account_plan_type='PAID')
            Request rate exceeds limits

            >>> await client.upgrade_account_plan(account_plan_type='PAID')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_freetier.types.upgrade_account_plan_request.UpgradeAccountPlanRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_freetier.types.upgrade_account_plan_response.UpgradeAccountPlanResponse"
        ]:
            import aws_sdk_freetier._operations.aws_free_tier_service.upgrade_account_plan

            (
                output,
                http_response,
            ) = await aws_sdk_freetier._operations.aws_free_tier_service.upgrade_account_plan.async_upgrade_account_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_freetier.types.upgrade_account_plan_request.UpgradeAccountPlanRequest = {}  # type: ignore[typeddict-item]
        input_["account_plan_type"] = account_plan_type

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
