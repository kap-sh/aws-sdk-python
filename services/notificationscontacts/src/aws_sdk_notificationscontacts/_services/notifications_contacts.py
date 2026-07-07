"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#NotificationsContacts``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import aws_sdk_notificationscontacts._auth._signers
import aws_sdk_notificationscontacts._auth._sigv4
from aws_sdk_notificationscontacts._auth._identity import Credentials
from aws_sdk_notificationscontacts._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_notificationscontacts._auth._zapros_handler import AuthMiddleware
from aws_sdk_notificationscontacts._resources.notifications_contacts.email_contact_resource import (
    EmailContactResource,
)
from aws_sdk_notificationscontacts._services._aws_config import aws_config
from aws_sdk_notificationscontacts._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_notificationscontacts.types.email_contact_arn
    import aws_sdk_notificationscontacts.types.list_tags_for_resource_request
    import aws_sdk_notificationscontacts.types.list_tags_for_resource_response
    import aws_sdk_notificationscontacts.types.tag_keys
    import aws_sdk_notificationscontacts.types.tag_map
    import aws_sdk_notificationscontacts.types.tag_resource_request
    import aws_sdk_notificationscontacts.types.tag_resource_response
    import aws_sdk_notificationscontacts.types.untag_resource_request
    import aws_sdk_notificationscontacts.types.untag_resource_response


class NotificationsContactsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class NotificationsContactsClient:
    """A client for the ``NotificationsContacts`` service.

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

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = NotificationsContactsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.email_contact_resource = EmailContactResource(self)

    def operation_options(
        self, config_overrides: Optional[NotificationsContactsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: NotificationsContactsClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
    ) -> "aws_sdk_notificationscontacts.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify. The resource can be a user, server, or role.</p>

        Args:
            arn: <p>The ARN you specified to list the tags of.</p>

        Raises:
            aws_sdk_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notificationscontacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Your request references a resource which does not exist. </p>
            aws_sdk_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notificationscontacts.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_notificationscontacts.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.list_tags_for_resource

            output, http_response = (
                aws_sdk_notificationscontacts._operations.notifications_contacts.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn",
        tags: "aws_sdk_notificationscontacts.types.tag_map.TagMap",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
    ) -> (
        "aws_sdk_notificationscontacts.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN). Taggable resources in AWS User Notifications Contacts include email contacts.</p>

        Args:
            arn: <p>The ARN of the configuration.</p>
            tags: <p>A list of tags to apply to the configuration.</p>

        Raises:
            aws_sdk_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notificationscontacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Your request references a resource which does not exist. </p>
            aws_sdk_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notificationscontacts.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_notificationscontacts.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.tag_resource

            output, http_response = (
                aws_sdk_notificationscontacts._operations.notifications_contacts.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn",
        tag_keys: "aws_sdk_notificationscontacts.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[NotificationsContactsClientConfig] = None,
    ) -> "aws_sdk_notificationscontacts.types.untag_resource_response.UntagResourceResponse":
        """<p>Detaches a key-value pair from a resource, as identified by its Amazon Resource Name (ARN). Taggable resources in AWS User Notifications Contacts include email contacts..</p>

        Args:
            arn: <p>The value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific AWS resource, such as a server, user, or role.</p>
            tag_keys: <p>Specifies a list of tag keys that you want to remove from the specified resources.</p>

        Raises:
            aws_sdk_notificationscontacts.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_notificationscontacts.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notificationscontacts.errors.resource_not_found_exception.ResourceNotFoundException: <p>Your request references a resource which does not exist. </p>
            aws_sdk_notificationscontacts.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_notificationscontacts.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_notificationscontacts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_notificationscontacts.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_notificationscontacts.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_notificationscontacts._operations.notifications_contacts.untag_resource

            output, http_response = (
                aws_sdk_notificationscontacts._operations.notifications_contacts.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_notificationscontacts.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
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
