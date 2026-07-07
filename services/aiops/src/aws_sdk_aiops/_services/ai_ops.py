"""Generated from Smithy shape ``com.amazonaws.aiops#AIOps``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import aws_sdk_aiops._auth._signers
import aws_sdk_aiops._auth._sigv4
from aws_sdk_aiops._auth._identity import Credentials
from aws_sdk_aiops._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_aiops._auth._zapros_handler import AuthMiddleware
from aws_sdk_aiops._resources.ai_ops.investigation_group import InvestigationGroup
from aws_sdk_aiops._resources.ai_ops.investigation_group_policy import (
    InvestigationGroupPolicy,
)
from aws_sdk_aiops._services._aws_config import aws_config
from aws_sdk_aiops._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_aiops.types.list_tags_for_resource_output
    import aws_sdk_aiops.types.list_tags_for_resource_request
    import aws_sdk_aiops.types.tag_keys
    import aws_sdk_aiops.types.tag_resource_request
    import aws_sdk_aiops.types.tag_resource_response
    import aws_sdk_aiops.types.tags
    import aws_sdk_aiops.types.untag_resource_request
    import aws_sdk_aiops.types.untag_resource_response


class AIOpsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AIOpsClient:
    """A client for the ``AIOps`` service.

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
        self._config = AIOpsClientConfig(
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
        self.investigation_group = InvestigationGroup(self)
        self.investigation_group_policy = InvestigationGroupPolicy(self)

    def operation_options(
        self, config_overrides: Optional[AIOpsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AIOpsClientConfig = config_overrides or {}
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
        self, resource_arn: str, *, config_overrides: Optional[AIOpsClientConfig] = None
    ) -> "aws_sdk_aiops.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Displays the tags associated with a CloudWatch investigations resource. Currently, investigation groups support tagging.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch investigations resource that you want to view tags for. You can use the <code>ListInvestigationGroups</code> operation to find the ARNs of investigation groups.</p> <p>The ARN format for an investigation group is <code>arn:aws:aiops:<i>Region</i>:<i>account-id</i>:investigation-group:<i>investigation-group-id</i> </code>.</p>

        Raises:
            aws_sdk_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            aws_sdk_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            aws_sdk_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            aws_sdk_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            aws_sdk_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            aws_sdk_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            aws_sdk_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            aws_sdk_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_aiops.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_aiops.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_aiops._operations.ai_ops.list_tags_for_resource

            output, http_response = (
                aws_sdk_aiops._operations.ai_ops.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_aiops.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
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
        tags: "aws_sdk_aiops.types.tags.Tags",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "aws_sdk_aiops.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified resource.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can associate as many as 50 tags with a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to apply the tags to. You can use the <code>ListInvestigationGroups</code> operation to find the ARNs of investigation groups.</p>
            tags: <p>The list of key-value pairs to associate with the resource.</p>

        Raises:
            aws_sdk_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            aws_sdk_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            aws_sdk_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            aws_sdk_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            aws_sdk_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            aws_sdk_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            aws_sdk_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            aws_sdk_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_aiops.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_aiops.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_aiops._operations.ai_ops.tag_resource

            output, http_response = (
                aws_sdk_aiops._operations.ai_ops.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_aiops.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        tag_keys: "aws_sdk_aiops.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AIOpsClientConfig] = None,
    ) -> "aws_sdk_aiops.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove the tags from. You can use the<code>ListInvestigationGroups</code> operation to find the ARNs of investigation groups.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            aws_sdk_aiops.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            aws_sdk_aiops.errors.conflict_exception.ConflictException: <p>This operation couldn't be completed because of a conflict in resource states.</p>
            aws_sdk_aiops.errors.forbidden_exception.ForbiddenException: <p>Access id denied for this operation, or this operation is not valid for the specified resource.</p>
            aws_sdk_aiops.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. You can try again later.</p>
            aws_sdk_aiops.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist.</p>
            aws_sdk_aiops.errors.validation_exception.ValidationException: <p>This operation or its parameters aren't formatted correctly.</p>
            aws_sdk_aiops.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits. You can try again later.</p>
            aws_sdk_aiops.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_aiops.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_aiops.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_aiops._operations.ai_ops.untag_resource

            output, http_response = (
                aws_sdk_aiops._operations.ai_ops.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_aiops.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
