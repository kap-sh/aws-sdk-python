"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#AmazonBedrockKeystoneRuntimeService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_bedrock_data_automation_runtime._auth._signers
import aws_sdk_bedrock_data_automation_runtime._auth._sigv4
from aws_sdk_bedrock_data_automation_runtime._auth._identity import Credentials
from aws_sdk_bedrock_data_automation_runtime._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_bedrock_data_automation_runtime._auth._zapros_handler import AuthMiddleware
from aws_sdk_bedrock_data_automation_runtime._resources.amazon_bedrock_keystone_runtime_service.automation_job_resource import (
    AutomationJobResource,
)
from aws_sdk_bedrock_data_automation_runtime._services._aws_config import aws_config
from aws_sdk_bedrock_data_automation_runtime._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

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


class BedrockDataAutomationRuntimeClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class BedrockDataAutomationRuntimeClient:
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

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = BedrockDataAutomationRuntimeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

        # resources
        self.automation_job_resource = AutomationJobResource(self)

    def operation_options(
        self,
        config_overrides: Optional[BedrockDataAutomationRuntimeClientConfig] = None,
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BedrockDataAutomationRuntimeClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def invoke_data_automation(
        self,
        input_configuration: "aws_sdk_bedrock_data_automation_runtime.types.sync_input_configuration.SyncInputConfiguration",
        data_automation_profile_arn: "aws_sdk_bedrock_data_automation_runtime.types.data_automation_profile_arn.DataAutomationProfileArn",
        *,
        config_overrides: Optional[BedrockDataAutomationRuntimeClientConfig] = None,
        data_automation_configuration: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration.DataAutomationConfiguration"
        ] = None,
        blueprints: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.blueprint_list.BlueprintList"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        output_configuration: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_response.InvokeDataAutomationResponse":
        """Sync API: Invoke data automation.

        Args:
            input_configuration: Input configuration.
            data_automation_configuration: Data automation configuration.
            blueprints: Blueprint list.
            data_automation_profile_arn: Data automation profile ARN
            encryption_configuration: Encryption configuration.
            output_configuration: Output configuration.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_request.InvokeDataAutomationRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_response.InvokeDataAutomationResponse"
        ]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation

            output, http_response = (
                aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation.invoke_data_automation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_request.InvokeDataAutomationRequest = {}  # type: ignore[typeddict-item]
        input_["input_configuration"] = input_configuration
        if data_automation_configuration is not None:
            input_["data_automation_configuration"] = data_automation_configuration
        if blueprints is not None:
            input_["blueprints"] = blueprints
        input_["data_automation_profile_arn"] = data_automation_profile_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if output_configuration is not None:
            input_["output_configuration"] = output_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[BedrockDataAutomationRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """List tags for an Amazon Bedrock Data Automation resource"""

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn",
        tags: "aws_sdk_bedrock_data_automation_runtime.types.tag_list.TagList",
        *,
        config_overrides: Optional[BedrockDataAutomationRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation_runtime.types.tag_resource_response.TagResourceResponse":
        """Tag an Amazon Bedrock Data Automation resource"""

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation_runtime.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation_runtime.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.tag_resource

            output, http_response = (
                aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation_runtime.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "aws_sdk_bedrock_data_automation_runtime.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[BedrockDataAutomationRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation_runtime.types.untag_resource_response.UntagResourceResponse":
        """Untag an Amazon Bedrock Data Automation resource"""

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation_runtime.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation_runtime.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.untag_resource

            output, http_response = (
                aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation_runtime.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
