"""Generated from Smithy shape ``com.amazonaws.launchwizard#LaunchWizard``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_launch_wizard._auth._signers
import capo_launch_wizard._auth._sigv4
from capo_launch_wizard._auth._identity import Credentials
from capo_launch_wizard._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_launch_wizard._auth._zapros_handler import AuthMiddleware
from capo_launch_wizard._resources.launch_wizard.deployment import Deployment
from capo_launch_wizard._resources.launch_wizard.settings_set import SettingsSet
from capo_launch_wizard._resources.launch_wizard.workload import Workload
from capo_launch_wizard._services._aws_config import aws_config
from capo_launch_wizard._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_launch_wizard.types.list_tags_for_resource_input
    import capo_launch_wizard.types.list_tags_for_resource_output
    import capo_launch_wizard.types.tag_key_list
    import capo_launch_wizard.types.tag_resource_input
    import capo_launch_wizard.types.tag_resource_output
    import capo_launch_wizard.types.tags
    import capo_launch_wizard.types.untag_resource_input
    import capo_launch_wizard.types.untag_resource_output


class LaunchWizardClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class LaunchWizardClient:
    """A client for the ``LaunchWizard`` service.

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
        self._config = LaunchWizardClientConfig(
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
        self.deployment = Deployment(self)
        self.settings_set = SettingsSet(self)
        self.workload = Workload(self)

    def operation_options(
        self, config_overrides: Optional[LaunchWizardClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: LaunchWizardClientConfig = config_overrides or {}
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
        resource_arn: str,
        *,
        config_overrides: Optional[LaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags associated with a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href=\"https://repost.aws/\">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Listing tags on a Launch Wizard deployment resource.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:launchwizard:us-east-1:123456789012:deployment/11111111-1111-1111-1111-111111111111')
        """

        def _handler(
            req: "OperationRequest[capo_launch_wizard.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_launch_wizard.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.list_tags_for_resource

            output, http_response = (
                capo_launch_wizard._operations.launch_wizard.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: str,
        tags: "capo_launch_wizard.types.tags.Tags",
        *,
        config_overrides: Optional[LaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.tag_resource_output.TagResourceOutput":
        """<p>Adds the specified tags to the given resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>One or more tags to attach to the resource.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href=\"https://repost.aws/\">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Adding tags to a Launch Wizard deployment resource.

            >>> client.tag_resource(resource_arn='arn:aws:launchwizard:us-east-1:123456789012:deployment/11111111-1111-1111-1111-111111111111', tags={'key1': 'value1', 'key2': 'value2'})
        """

        def _handler(
            req: "OperationRequest[capo_launch_wizard.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_launch_wizard.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.tag_resource

            output, http_response = (
                capo_launch_wizard._operations.launch_wizard.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: str,
        tag_keys: "capo_launch_wizard.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[LaunchWizardClientConfig] = None,
    ) -> "capo_launch_wizard.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes the specified tags from the given resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>Keys identifying the tags to remove.</p>

        Raises:
            capo_launch_wizard.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on <a href=\"https://repost.aws/\">re:Post</a>.</p>
            capo_launch_wizard.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified workload or deployment resource can't be found.</p>
            capo_launch_wizard.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_launch_wizard.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Removing tags on a Launch Wizard deployment resource.

            >>> client.untag_resource(resource_arn='arn:aws:launchwizard:us-east-1:123456789012:deployment/11111111-1111-1111-1111-111111111111', tag_keys=['key1', 'key2'])
        """

        def _handler(
            req: "OperationRequest[capo_launch_wizard.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_launch_wizard.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_launch_wizard._operations.launch_wizard.untag_resource

            output, http_response = (
                capo_launch_wizard._operations.launch_wizard.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_launch_wizard.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
