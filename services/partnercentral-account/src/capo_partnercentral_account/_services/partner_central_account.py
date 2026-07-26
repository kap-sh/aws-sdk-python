"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PartnerCentralAccount``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_partnercentral_account._auth._signers
import capo_partnercentral_account._auth._sigv4
from capo_partnercentral_account._auth._identity import Credentials
from capo_partnercentral_account._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_partnercentral_account._auth._zapros_handler import AuthMiddleware
from capo_partnercentral_account._resources.partner_central_account.connection_invitation import (
    ConnectionInvitation,
)
from capo_partnercentral_account._resources.partner_central_account.connection_preferences import (
    ConnectionPreferences,
)
from capo_partnercentral_account._resources.partner_central_account.connection_resource import (
    ConnectionResource,
)
from capo_partnercentral_account._resources.partner_central_account.partner import (
    Partner,
)
from capo_partnercentral_account._services._aws_config import aws_config
from capo_partnercentral_account._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.email
    import capo_partnercentral_account.types.get_verification_request
    import capo_partnercentral_account.types.get_verification_response
    import capo_partnercentral_account.types.list_tags_for_resource_request
    import capo_partnercentral_account.types.list_tags_for_resource_response
    import capo_partnercentral_account.types.send_email_verification_code_request
    import capo_partnercentral_account.types.send_email_verification_code_response
    import capo_partnercentral_account.types.start_verification_request
    import capo_partnercentral_account.types.start_verification_response
    import capo_partnercentral_account.types.tag_key_list
    import capo_partnercentral_account.types.tag_list
    import capo_partnercentral_account.types.tag_resource_request
    import capo_partnercentral_account.types.tag_resource_response
    import capo_partnercentral_account.types.taggable_resource_arn
    import capo_partnercentral_account.types.untag_resource_request
    import capo_partnercentral_account.types.untag_resource_response
    import capo_partnercentral_account.types.verification_details
    import capo_partnercentral_account.types.verification_type


class PartnerCentralAccountClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class PartnerCentralAccountClient:
    """A client for the ``PartnerCentralAccount`` service.

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
        self._config = PartnerCentralAccountClientConfig(
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
        self.connection_invitation = ConnectionInvitation(self)
        self.connection_preferences = ConnectionPreferences(self)
        self.connection_resource = ConnectionResource(self)
        self.partner = Partner(self)

    def operation_options(
        self, config_overrides: Optional[PartnerCentralAccountClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PartnerCentralAccountClientConfig = config_overrides or {}
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

    def get_verification(
        self,
        verification_type: "capo_partnercentral_account.types.verification_type.VerificationType",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.get_verification_response.GetVerificationResponse":
        """<p>Retrieves the current status and details of a verification process for a partner account. This operation allows partners to check the progress and results of business or registrant verification processes.</p>

        Args:
            verification_type: <p>The type of verification to retrieve information for. Valid values include business verification for company registration details and registrant verification for individual identity confirmation.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.get_verification_request.GetVerificationRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.get_verification_response.GetVerificationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.get_verification

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.get_verification.get_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.get_verification_request.GetVerificationRequest = {}  # type: ignore[typeddict-item]
        input_["verification_type"] = verification_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_partnercentral_account.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with a specific AWS Partner Central Account resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.list_tags_for_resource

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_email_verification_code(
        self,
        catalog: "capo_partnercentral_account.types.catalog.Catalog",
        email: "capo_partnercentral_account.types.email.Email",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.send_email_verification_code_response.SendEmailVerificationCodeResponse":
        """<p>Sends an email verification code to the specified email address for account verification purposes.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            email: <p>The email address to send the verification code to.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.send_email_verification_code_request.SendEmailVerificationCodeRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.send_email_verification_code_response.SendEmailVerificationCodeResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.send_email_verification_code

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.send_email_verification_code.send_email_verification_code(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.send_email_verification_code_request.SendEmailVerificationCodeRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["email"] = email

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_verification(
        self,
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_account.types.client_token.ClientToken"
        ] = None,
        verification_details: Optional[
            "capo_partnercentral_account.types.verification_details.VerificationDetails"
        ] = None,
    ) -> "capo_partnercentral_account.types.start_verification_response.StartVerificationResponse":
        """<p>Initiates a new verification process for a partner account. This operation begins the verification workflow for either business registration or individual registrant identity verification as required by AWS Partner Central.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This prevents duplicate verification processes from being started accidentally.</p>
            verification_details: <p>The specific details required for the verification process, including business information for business verification or personal information for registrant verification.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.start_verification_request.StartVerificationRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.start_verification_response.StartVerificationResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.start_verification

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.start_verification.start_verification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.start_verification_request.StartVerificationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if verification_details is not None:
            input_["verification_details"] = verification_details

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_partnercentral_account.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_partnercentral_account.types.tag_list.TagList",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for a specified AWS Partner Central Account resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>A list of tags to add or update for the specified resource.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.tag_resource

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "capo_partnercentral_account.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_partnercentral_account.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[PartnerCentralAccountClientConfig] = None,
    ) -> "capo_partnercentral_account.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes specified tags from an AWS Partner Central Account resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>A list of tag keys to remove from the specified resource.</p>

        Raises:
            capo_partnercentral_account.errors.access_denied_exception.AccessDeniedException: <p>The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.</p>
            capo_partnercentral_account.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.</p>
            capo_partnercentral_account.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.</p>
            capo_partnercentral_account.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.</p>
            capo_partnercentral_account.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.</p>
            capo_partnercentral_account.errors.validation_exception.ValidationException: <p>The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.</p>
            capo_partnercentral_account.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_account.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_account.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_partnercentral_account._operations.partner_central_account.untag_resource

            output, http_response = (
                capo_partnercentral_account._operations.partner_central_account.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_partnercentral_account.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
