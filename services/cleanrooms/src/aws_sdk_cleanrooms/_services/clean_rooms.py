"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AWSBastionControlPlaneServiceLambda``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_cleanrooms._auth._signers
import aws_sdk_cleanrooms._auth._sigv4
from aws_sdk_cleanrooms._auth._identity import Credentials
from aws_sdk_cleanrooms._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_cleanrooms._auth._zapros_handler import AuthMiddleware
from aws_sdk_cleanrooms._resources.aws_bastion_control_plane_service_lambda.analysis_template_resource import (
    AnalysisTemplateResource,
)
from aws_sdk_cleanrooms._resources.aws_bastion_control_plane_service_lambda.collaboration_resource import (
    CollaborationResource,
)
from aws_sdk_cleanrooms._resources.aws_bastion_control_plane_service_lambda.configured_audience_model_association_resource import (
    ConfiguredAudienceModelAssociationResource,
)
from aws_sdk_cleanrooms._resources.aws_bastion_control_plane_service_lambda.configured_table_association_resource import (
    ConfiguredTableAssociationResource,
)
from aws_sdk_cleanrooms._resources.aws_bastion_control_plane_service_lambda.configured_table_resource import (
    ConfiguredTableResource,
)
from aws_sdk_cleanrooms._resources.aws_bastion_control_plane_service_lambda.id_mapping_table_resource import (
    IdMappingTableResource,
)
from aws_sdk_cleanrooms._resources.aws_bastion_control_plane_service_lambda.id_namespace_association_resource import (
    IdNamespaceAssociationResource,
)
from aws_sdk_cleanrooms._resources.aws_bastion_control_plane_service_lambda.membership_resource import (
    MembershipResource,
)
from aws_sdk_cleanrooms._resources.aws_bastion_control_plane_service_lambda.privacy_budget_template_resource import (
    PrivacyBudgetTemplateResource,
)
from aws_sdk_cleanrooms._services._aws_config import aws_config
from aws_sdk_cleanrooms._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.cleanrooms_arn
    import aws_sdk_cleanrooms.types.list_tags_for_resource_input
    import aws_sdk_cleanrooms.types.list_tags_for_resource_output
    import aws_sdk_cleanrooms.types.tag_keys
    import aws_sdk_cleanrooms.types.tag_map
    import aws_sdk_cleanrooms.types.tag_resource_input
    import aws_sdk_cleanrooms.types.tag_resource_output
    import aws_sdk_cleanrooms.types.untag_resource_input
    import aws_sdk_cleanrooms.types.untag_resource_output


class CleanRoomsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class CleanRoomsClient:
    """A client for the ``CleanRooms`` service.

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
        self._config = CleanRoomsClientConfig(
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
        self.analysis_template_resource = AnalysisTemplateResource(self)
        self.collaboration_resource = CollaborationResource(self)
        self.configured_audience_model_association_resource = (
            ConfiguredAudienceModelAssociationResource(self)
        )
        self.configured_table_association_resource = ConfiguredTableAssociationResource(
            self
        )
        self.configured_table_resource = ConfiguredTableResource(self)
        self.id_mapping_table_resource = IdMappingTableResource(self)
        self.id_namespace_association_resource = IdNamespaceAssociationResource(self)
        self.membership_resource = MembershipResource(self)
        self.privacy_budget_template_resource = PrivacyBudgetTemplateResource(self)

    def operation_options(
        self, config_overrides: Optional[CleanRoomsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CleanRoomsClientConfig = config_overrides or {}
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
        resource_arn: "aws_sdk_cleanrooms.types.cleanrooms_arn.CleanroomsArn",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists all of the tags that have been added to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource you want to list tags on.</p>

        Raises:
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_tags_for_resource

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_cleanrooms.types.cleanrooms_arn.CleanroomsArn",
        tags: "aws_sdk_cleanrooms.types.tag_map.TagMap",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.tag_resource_output.TagResourceOutput":
        """<p>Tags a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource you want to tag.</p>
            tags: <p>A map of objects specifying each key name and value.</p>

        Raises:
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.tag_resource

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_cleanrooms.types.cleanrooms_arn.CleanroomsArn",
        tag_keys: "aws_sdk_cleanrooms.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[CleanRoomsClientConfig] = None,
    ) -> "aws_sdk_cleanrooms.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a tag or list of tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource you want to remove the tag from.</p>
            tag_keys: <p>A list of key names of tags to be removed.</p>

        Raises:
            aws_sdk_cleanrooms.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            aws_sdk_cleanrooms.errors.validation_exception.ValidationException: <p>The input fails to satisfy the specified constraints.</p>
            aws_sdk_cleanrooms.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cleanrooms.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_cleanrooms.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.untag_resource

            output, http_response = (
                aws_sdk_cleanrooms._operations.aws_bastion_control_plane_service_lambda.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cleanrooms.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
