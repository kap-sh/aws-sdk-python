"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#AWSMPEntitlementService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_marketplace_entitlement_service._auth._signers
import aws_sdk_marketplace_entitlement_service._auth._sigv4
from aws_sdk_marketplace_entitlement_service._auth._identity import Credentials
from aws_sdk_marketplace_entitlement_service._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_marketplace_entitlement_service._auth._zapros_handler import AuthMiddleware
from aws_sdk_marketplace_entitlement_service._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_marketplace_entitlement_service.types.get_entitlement_filters
    import aws_sdk_marketplace_entitlement_service.types.get_entitlements_request
    import aws_sdk_marketplace_entitlement_service.types.get_entitlements_result
    import aws_sdk_marketplace_entitlement_service.types.non_empty_string
    import aws_sdk_marketplace_entitlement_service.types.page_size_integer
    import aws_sdk_marketplace_entitlement_service.types.product_code


class AsyncMarketplaceEntitlementServiceClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
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


class AsyncMarketplaceEntitlementServiceClient:
    """A client for the ``MarketplaceEntitlementService`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncMarketplaceEntitlementServiceClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[
            AsyncMarketplaceEntitlementServiceClientConfig
        ] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMarketplaceEntitlementServiceClientConfig = (
            config_overrides or {}
        )
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def get_entitlements(
        self,
        product_code: "aws_sdk_marketplace_entitlement_service.types.product_code.ProductCode",
        *,
        config_overrides: Optional[
            AsyncMarketplaceEntitlementServiceClientConfig
        ] = None,
        filter: Optional[
            "aws_sdk_marketplace_entitlement_service.types.get_entitlement_filters.GetEntitlementFilters"
        ] = None,
        next_token: Optional[
            "aws_sdk_marketplace_entitlement_service.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional[
            "aws_sdk_marketplace_entitlement_service.types.page_size_integer.PageSizeInteger"
        ] = None,
    ) -> "aws_sdk_marketplace_entitlement_service.types.get_entitlements_result.GetEntitlementsResult":
        """<p>GetEntitlements retrieves entitlement values for a given product. The results can be filtered based on customer identifier, AWS account ID, license ARN, or product dimensions.</p>

        Args:
            product_code: <p>Product code is used to uniquely identify a product in AWS Marketplace. The product code will be provided by AWS Marketplace when the product listing is created.</p>
            filter: <p>Filter is used to return entitlements for a specific customer or for a specific dimension. Filters are described as keys mapped to a lists of values. Filtered requests are <i>unioned</i> for each value in the value list, and then <i>intersected</i> for each filter key.</p> <p> <code>CustomerIdentifier</code> and <code>CustomerAWSAccountId</code> are mutually exclusive parameters. You must use one or the other, but not both in the same request. </p> <note> <p>If you're migrating an existing integration, use <a href=\"https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-account.html\">Account Feeds</a> to map <code>CustomerIdentifier</code> to <code>CustomerAWSAccountId</code>, and <a href=\"https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-agreements.html\">Agreements Feeds</a> to map <code>CustomerAWSAccountId</code> and <code>LicenseArn</code>.</p> </note>
            next_token: <p>For paginated calls to GetEntitlements, pass the NextToken from the previous GetEntitlementsResult.</p>
            max_results: <p>The maximum number of items to retrieve from the GetEntitlements operation. For pagination, use the NextToken field in subsequent calls to GetEntitlements.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_marketplace_entitlement_service.types.get_entitlements_request.GetEntitlementsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_marketplace_entitlement_service.types.get_entitlements_result.GetEntitlementsResult"
        ]:
            import aws_sdk_marketplace_entitlement_service._operations.awsmp_entitlement_service.get_entitlements

            (
                output,
                http_response,
            ) = await aws_sdk_marketplace_entitlement_service._operations.awsmp_entitlement_service.get_entitlements.async_get_entitlements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_marketplace_entitlement_service.types.get_entitlements_request.GetEntitlementsRequest = {}  # type: ignore[typeddict-item]
        input_["product_code"] = product_code
        if filter is not None:
            input_["filter"] = filter
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
