"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#AmazonBedrockKeystoneRuntimeService``."""

from aws_sdk_bedrock_data_automation_runtime._auth._signers import SigV4Signer
from aws_sdk_bedrock_data_automation_runtime._auth._sigv4 import presign_sigv4
from collections.abc import AsyncIterator
from typing import Any, Iterable, TypedDict, Unpack, TYPE_CHECKING
from typing_extensions import Self
from typing import Optional
from zapros import URL, AsyncBaseHandler, AsyncClient
from aws_sdk_bedrock_data_automation_runtime._auth._zapros_handler import AuthMiddleware
from aws_sdk_bedrock_data_automation_runtime._services._pipeline import AsyncInterceptor, AsyncOperationOptions, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline, aretry
from aws_sdk_bedrock_data_automation_runtime._async import anysleep
import time
from aws_sdk_bedrock_data_automation_runtime.errors import ServiceError, WaiterFailedError, WaiterTimeoutError
import warnings
from aws_sdk_bedrock_data_automation_runtime._auth._identity import Credentials
from aws_sdk_bedrock_data_automation_runtime._auth._providers import CredentialsProvider, StaticAwsCredentialsProvider
if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.blueprint_list
    import aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.data_automation_profile_arn
    import aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_request
    import aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_response
    import aws_sdk_bedrock_data_automation_runtime.types.list_tags_for_resource_request
    import aws_sdk_bedrock_data_automation_runtime.types.list_tags_for_resource_response
    import aws_sdk_bedrock_data_automation_runtime.types.output_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.sync_input_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.tag_key_list
    import aws_sdk_bedrock_data_automation_runtime.types.tag_list
    import aws_sdk_bedrock_data_automation_runtime.types.tag_resource_request
    import aws_sdk_bedrock_data_automation_runtime.types.tag_resource_response
    import aws_sdk_bedrock_data_automation_runtime.types.taggable_resource_arn
    import aws_sdk_bedrock_data_automation_runtime.types.untag_resource_request
    import aws_sdk_bedrock_data_automation_runtime.types.untag_resource_response

class AsyncBedrockDataAutomationRuntimeClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None

DEFAULT_RETRY_MAX_ATTEMPTS = 3

async def ensure_async_iterator(it: AsyncIterator[bytes] | bytes) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk

class AsyncBedrockDataAutomationRuntimeClient:
    """A client for the ``BedrockDataAutomationRuntime`` service.

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
    def __init__(self, http_handler: AsyncBaseHandler | None = None, operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None, retry_max_attempts: int | None = None, region: str | None = None, use_dual_stack: bool | None = None, use_fips: bool | None = None, endpoint: str | None = None, credentials: Credentials | None = None, credentials_provider: CredentialsProvider | None = None):
        self._client = AsyncClient(http_handler).wrap_with_middleware(lambda next: AuthMiddleware(next))
        if credentials is not None and credentials_provider is not None:
            warnings.warn("Both credentials and credentials_provider given; provider takes precedence")
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncBedrockDataAutomationRuntimeClientConfig({"operation_interceptors": operation_interceptors or [], "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS if retry_max_attempts is None else retry_max_attempts, "region": region, "use_dual_stack": use_dual_stack, "use_fips": use_fips, "endpoint": endpoint, "credentials_provider": credentials_provider})
    def operation_options(self, config_overrides: Optional[AsyncBedrockDataAutomationRuntimeClientConfig] = None) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBedrockDataAutomationRuntimeClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [*overrides.get("operation_interceptors", self.config.get("operation_interceptors", [])), aretry()]
        options_: AsyncOperationOptions = AsyncOperationOptions(client=self._client, retry_max_attempts=overrides.get("retry_max_attempts", self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS)), region=overrides.get("region", self.config.get("region")), use_dual_stack=overrides.get("use_dual_stack", self.config.get("use_dual_stack")), use_fips=overrides.get("use_fips", self.config.get("use_fips")), endpoint=overrides.get("endpoint", self.config.get("endpoint")), credentials_provider=overrides.get("credentials_provider", self.config.get("credentials_provider")))
        return interceptors_, options_
    async def invoke_data_automation(self, input_configuration: "aws_sdk_bedrock_data_automation_runtime.types.sync_input_configuration.SyncInputConfiguration", data_automation_profile_arn: "aws_sdk_bedrock_data_automation_runtime.types.data_automation_profile_arn.DataAutomationProfileArn", *, config_overrides: Optional[AsyncBedrockDataAutomationRuntimeClientConfig] = None, data_automation_configuration: Optional["aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration.DataAutomationConfiguration"] = None, blueprints: Optional["aws_sdk_bedrock_data_automation_runtime.types.blueprint_list.BlueprintList"] = None, encryption_configuration: Optional["aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration.EncryptionConfiguration"] = None, output_configuration: Optional["aws_sdk_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration"] = None) -> "aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_response.InvokeDataAutomationResponse":
        """Sync API: Invoke data automation.

        Args:
            input_configuration: Input configuration.
            data_automation_configuration: Data automation configuration.
            blueprints: Blueprint list.
            data_automation_profile_arn: Data automation profile ARN
            encryption_configuration: Encryption configuration.
            output_configuration: Output configuration.
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_request.InvokeDataAutomationRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_response.InvokeDataAutomationResponse"]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation
            output, http_response = await aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation.async_invoke_data_automation(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_request.InvokeDataAutomationRequest = {}  # type: ignore[typeddict-item]
        input["input_configuration"] = input_configuration
        if data_automation_configuration is not None:
            input["data_automation_configuration"] = data_automation_configuration
        if blueprints is not None:
            input["blueprints"] = blueprints
        input["data_automation_profile_arn"] = data_automation_profile_arn
        if encryption_configuration is not None:
            input["encryption_configuration"] = encryption_configuration
        if output_configuration is not None:
            input["output_configuration"] = output_configuration

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def list_tags_for_resource(self, resource_arn: "aws_sdk_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn", *, config_overrides: Optional[AsyncBedrockDataAutomationRuntimeClientConfig] = None) -> "aws_sdk_bedrock_data_automation_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """List tags for an Amazon Bedrock Data Automation resource
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_data_automation_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_data_automation_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse"]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.list_tags_for_resource
            output, http_response = await aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.list_tags_for_resource.async_list_tags_for_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bedrock_data_automation_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def tag_resource(self, resource_arn: "aws_sdk_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn", tags: "aws_sdk_bedrock_data_automation_runtime.types.tag_list.TagList", *, config_overrides: Optional[AsyncBedrockDataAutomationRuntimeClientConfig] = None) -> "aws_sdk_bedrock_data_automation_runtime.types.tag_resource_response.TagResourceResponse":
        """Tag an Amazon Bedrock Data Automation resource
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_data_automation_runtime.types.tag_resource_request.TagResourceRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_data_automation_runtime.types.tag_resource_response.TagResourceResponse"]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.tag_resource
            output, http_response = await aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.tag_resource.async_tag_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bedrock_data_automation_runtime.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def untag_resource(self, resource_arn: "aws_sdk_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn", tag_keys: "aws_sdk_bedrock_data_automation_runtime.types.tag_key_list.TagKeyList", *, config_overrides: Optional[AsyncBedrockDataAutomationRuntimeClientConfig] = None) -> "aws_sdk_bedrock_data_automation_runtime.types.untag_resource_response.UntagResourceResponse":
        """Untag an Amazon Bedrock Data Automation resource
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_data_automation_runtime.types.untag_resource_request.UntagResourceRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_data_automation_runtime.types.untag_resource_response.UntagResourceResponse"]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.untag_resource
            output, http_response = await aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.untag_resource.async_untag_resource(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_bedrock_data_automation_runtime.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output
    async def __aenter__(self) -> Self:
        return self
    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()