"""Generated from Smithy shape ``com.amazonaws.backupgateway#BackupOnPremises_v20210101``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import aws_sdk_backup_gateway._auth._signers
import aws_sdk_backup_gateway._auth._sigv4
from aws_sdk_backup_gateway._auth._identity import Credentials
from aws_sdk_backup_gateway._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_backup_gateway._auth._zapros_handler import AuthMiddleware
from aws_sdk_backup_gateway._resources.backup_on_premises_v20210101.gateway_resource import (
    GatewayResource,
)
from aws_sdk_backup_gateway._resources.backup_on_premises_v20210101.hypervisor_resource import (
    HypervisorResource,
)
from aws_sdk_backup_gateway._resources.backup_on_premises_v20210101.virtual_machine_resource import (
    VirtualMachineResource,
)
from aws_sdk_backup_gateway._services._aws_config import aws_config
from aws_sdk_backup_gateway._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.list_tags_for_resource_input
    import aws_sdk_backup_gateway.types.list_tags_for_resource_output
    import aws_sdk_backup_gateway.types.resource_arn
    import aws_sdk_backup_gateway.types.tag_keys
    import aws_sdk_backup_gateway.types.tag_resource_input
    import aws_sdk_backup_gateway.types.tag_resource_output
    import aws_sdk_backup_gateway.types.tags
    import aws_sdk_backup_gateway.types.untag_resource_input
    import aws_sdk_backup_gateway.types.untag_resource_output


class BackupGatewayClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class BackupGatewayClient:
    """A client for the ``BackupGateway`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = BackupGatewayClientConfig(
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
        self.gateway_resource = GatewayResource(self)
        self.hypervisor_resource = HypervisorResource(self)
        self.virtual_machine_resource = VirtualMachineResource(self)

    def operation_options(
        self, config_overrides: Optional[BackupGatewayClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BackupGatewayClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_backup_gateway.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags applied to the resource identified by its Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource's tags to list.</p>

        Raises:
            aws_sdk_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            aws_sdk_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            aws_sdk_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            aws_sdk_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            aws_sdk_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_tags_for_resource

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_backup_gateway.types.resource_arn.ResourceArn",
        tags: "aws_sdk_backup_gateway.types.tags.Tags",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.tag_resource_output.TagResourceOutput":
        """<p>Tag the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>A list of tags to assign to the resource.</p>

        Raises:
            aws_sdk_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            aws_sdk_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            aws_sdk_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            aws_sdk_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            aws_sdk_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.tag_resource

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_backup_gateway.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_backup_gateway.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>The list of tag keys specifying which tags to remove.</p>

        Raises:
            aws_sdk_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            aws_sdk_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            aws_sdk_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            aws_sdk_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            aws_sdk_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.untag_resource

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
