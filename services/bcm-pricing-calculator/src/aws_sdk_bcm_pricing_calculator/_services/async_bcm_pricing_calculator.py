"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#AWSBCMPricingCalculator``."""

from aws_sdk_bcm_pricing_calculator._auth._signers import SigV4Signer
from aws_sdk_bcm_pricing_calculator._auth._sigv4 import presign_sigv4
from collections.abc import AsyncIterator
from typing import Any, Iterable, TypedDict, Unpack, TYPE_CHECKING
from typing_extensions import Self
from typing import Optional
from zapros import URL, AsyncBaseHandler, AsyncClient
from aws_sdk_bcm_pricing_calculator._auth._zapros_handler import AuthMiddleware
from aws_sdk_bcm_pricing_calculator._services._pipeline import AsyncInterceptor, AsyncOperationOptions, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline, aretry
from aws_sdk_bcm_pricing_calculator._async import anysleep
import time
from aws_sdk_bcm_pricing_calculator.errors import ServiceError, WaiterFailedError, WaiterTimeoutError
import warnings
from aws_sdk_bcm_pricing_calculator._auth._identity import Credentials
from aws_sdk_bcm_pricing_calculator._auth._providers import CredentialsProvider, StaticAwsCredentialsProvider
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.arn
    import aws_sdk_bcm_pricing_calculator.types.get_preferences_request
    import aws_sdk_bcm_pricing_calculator.types.get_preferences_response
    import aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_request
    import aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_response
    import aws_sdk_bcm_pricing_calculator.types.rate_types
    import aws_sdk_bcm_pricing_calculator.types.resource_tag_keys
    import aws_sdk_bcm_pricing_calculator.types.tag_resource_request
    import aws_sdk_bcm_pricing_calculator.types.tag_resource_response
    import aws_sdk_bcm_pricing_calculator.types.tags
    import aws_sdk_bcm_pricing_calculator.types.untag_resource_request
    import aws_sdk_bcm_pricing_calculator.types.untag_resource_response
    import aws_sdk_bcm_pricing_calculator.types.update_preferences_request
    import aws_sdk_bcm_pricing_calculator.types.update_preferences_response

class AsyncBCMPricingCalculatorClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None

DEFAULT_RETRY_MAX_ATTEMPTS = 3

async def ensure_async_iterator(it: AsyncIterator[bytes] | bytes) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk

class AsyncBCMPricingCalculatorClient:
    """A client for the ``BCMPricingCalculator`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """
    def __init__(self, http_handler: AsyncBaseHandler | None = None, operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None, retry_max_attempts: int | None = None, use_fips: bool | None = None, endpoint: str | None = None, region: str | None = None, credentials: Credentials | None = None, credentials_provider: CredentialsProvider | None = None):
        self._client = AsyncClient(http_handler).wrap_with_middleware(lambda next: AuthMiddleware(next))
        if credentials is not None and credentials_provider is not None:
            warnings.warn("Both credentials and credentials_provider given; provider takes precedence")
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncBCMPricingCalculatorClientConfig({"operation_interceptors": operation_interceptors or [], "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS if retry_max_attempts is None else retry_max_attempts, "use_fips": use_fips, "endpoint": endpoint, "region": region, "credentials_provider": credentials_provider})
    def operation_options(self, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBCMPricingCalculatorClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [*overrides.get("operation_interceptors", self.config.get("operation_interceptors", [])), aretry()]
        options_: AsyncOperationOptions = AsyncOperationOptions(client=self._client, retry_max_attempts=overrides.get("retry_max_attempts", self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS)), use_fips=overrides.get("use_fips", self.config.get("use_fips")), endpoint=overrides.get("endpoint", self.config.get("endpoint")), region=overrides.get("region", self.config.get("region")), credentials_provider=overrides.get("credentials_provider", self.config.get("credentials_provider")))
        return interceptors_, options_
    async def get_preferences(self, *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.get_preferences_response.GetPreferencesResponse":
        """<p> Retrieves the current preferences for Pricing Calculator. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.get_preferences_request.GetPreferencesRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.get_preferences_response.GetPreferencesResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_preferences
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_preferences.async_get_preferences(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.get_preferences_request.GetPreferencesRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_tags_for_resource(self, arn: "aws_sdk_bcm_pricing_calculator.types.arn.Arn", *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Lists all tags associated with a specified resource. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the resource to list tags for. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_request.ListTagsForResourceRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_response.ListTagsForResourceResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_tags_for_resource
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_tags_for_resource.async_list_tags_for_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def tag_resource(self, arn: "aws_sdk_bcm_pricing_calculator.types.arn.Arn", tags: "aws_sdk_bcm_pricing_calculator.types.tags.Tags", *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.tag_resource_response.TagResourceResponse":
        """<p> Adds one or more tags to a specified resource. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the resource to add tags to. </p>
            tags: <p> The tags to add to the resource. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.tag_resource_request.TagResourceRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.tag_resource_response.TagResourceResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.tag_resource
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.tag_resource.async_tag_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def untag_resource(self, arn: "aws_sdk_bcm_pricing_calculator.types.arn.Arn", tag_keys: "aws_sdk_bcm_pricing_calculator.types.resource_tag_keys.ResourceTagKeys", *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None) -> "aws_sdk_bcm_pricing_calculator.types.untag_resource_response.UntagResourceResponse":
        """<p> Removes one or more tags from a specified resource. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the resource to remove tags from. </p>
            tag_keys: <p> The keys of the tags to remove from the resource. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.untag_resource_request.UntagResourceRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.untag_resource_response.UntagResourceResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.untag_resource
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.untag_resource.async_untag_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def update_preferences(self, *, config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None, management_account_rate_type_selections: Optional["aws_sdk_bcm_pricing_calculator.types.rate_types.RateTypes"] = None, member_account_rate_type_selections: Optional["aws_sdk_bcm_pricing_calculator.types.rate_types.RateTypes"] = None, standalone_account_rate_type_selections: Optional["aws_sdk_bcm_pricing_calculator.types.rate_types.RateTypes"] = None) -> "aws_sdk_bcm_pricing_calculator.types.update_preferences_response.UpdatePreferencesResponse":
        """<p> Updates the preferences for Pricing Calculator. </p>

        Args:
            management_account_rate_type_selections: <p> The updated preferred rate types for the management account. </p>
            member_account_rate_type_selections: <p> The updated preferred rate types for member accounts. </p>
            standalone_account_rate_type_selections: <p> The updated preferred rate types for a standalone account. </p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bcm_pricing_calculator.types.update_preferences_request.UpdatePreferencesRequest]') -> AsyncOperationResponse["aws_sdk_bcm_pricing_calculator.types.update_preferences_response.UpdatePreferencesResponse"]:
            import aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_preferences
            output, http_response = await aws_sdk_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_preferences.async_update_preferences(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bcm_pricing_calculator.types.update_preferences_request.UpdatePreferencesRequest = {}  # type: ignore[typeddict-item]
        if management_account_rate_type_selections is not None:
            input["management_account_rate_type_selections"] = management_account_rate_type_selections
        if member_account_rate_type_selections is not None:
            input["member_account_rate_type_selections"] = member_account_rate_type_selections
        if standalone_account_rate_type_selections is not None:
            input["standalone_account_rate_type_selections"] = standalone_account_rate_type_selections

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def __aenter__(self) -> Self:
        return self
    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()