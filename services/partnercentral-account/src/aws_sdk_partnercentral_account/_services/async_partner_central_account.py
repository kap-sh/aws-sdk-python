"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PartnerCentralAccount``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_partnercentral_account._auth._signers
import aws_sdk_partnercentral_account._auth._sigv4
from aws_sdk_partnercentral_account._auth._identity import Credentials
from aws_sdk_partnercentral_account._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_partnercentral_account._auth._zapros_handler import AuthMiddleware
from aws_sdk_partnercentral_account._resources.partner_central_account.connection_invitation import (
    AsyncConnectionInvitation,
)
from aws_sdk_partnercentral_account._resources.partner_central_account.connection_preferences import (
    AsyncConnectionPreferences,
)
from aws_sdk_partnercentral_account._resources.partner_central_account.connection_resource import (
    AsyncConnectionResource,
)
from aws_sdk_partnercentral_account._resources.partner_central_account.partner import (
    AsyncPartner,
)
from aws_sdk_partnercentral_account._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.client_token
    import aws_sdk_partnercentral_account.types.email
    import aws_sdk_partnercentral_account.types.get_verification_request
    import aws_sdk_partnercentral_account.types.get_verification_response
    import aws_sdk_partnercentral_account.types.list_tags_for_resource_request
    import aws_sdk_partnercentral_account.types.list_tags_for_resource_response
    import aws_sdk_partnercentral_account.types.send_email_verification_code_request
    import aws_sdk_partnercentral_account.types.send_email_verification_code_response
    import aws_sdk_partnercentral_account.types.start_verification_request
    import aws_sdk_partnercentral_account.types.start_verification_response
    import aws_sdk_partnercentral_account.types.tag_key_list
    import aws_sdk_partnercentral_account.types.tag_list
    import aws_sdk_partnercentral_account.types.tag_resource_request
    import aws_sdk_partnercentral_account.types.tag_resource_response
    import aws_sdk_partnercentral_account.types.taggable_resource_arn
    import aws_sdk_partnercentral_account.types.untag_resource_request
    import aws_sdk_partnercentral_account.types.untag_resource_response
    import aws_sdk_partnercentral_account.types.verification_details
    import aws_sdk_partnercentral_account.types.verification_type


class AsyncPartnerCentralAccountClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncPartnerCentralAccountClient:
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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
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
        self._config = AsyncPartnerCentralAccountClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

        # resources
        self.connection_invitation = AsyncConnectionInvitation(self)
        self.connection_preferences = AsyncConnectionPreferences(self)
        self.connection_resource = AsyncConnectionResource(self)
        self.partner = AsyncPartner(self)

    def operation_options(
        self, config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPartnerCentralAccountClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def get_verification(
        self,
        verification_type: "aws_sdk_partnercentral_account.types.verification_type.VerificationType",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.get_verification_response.GetVerificationResponse":
        """<p>Retrieves the current status and details of a verification process for a partner account. This operation allows partners to check the progress and results of business or registrant verification processes.</p>

        Args:
            verification_type: <p>The type of verification to retrieve information for. Valid values include business verification for company registration details and registrant verification for individual identity confirmation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.get_verification_request.GetVerificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.get_verification_response.GetVerificationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.get_verification

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.get_verification.async_get_verification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.get_verification_request.GetVerificationRequest = {}  # type: ignore[typeddict-item]
        input_["verification_type"] = verification_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_account.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with a specific AWS Partner Central Account resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def send_email_verification_code(
        self,
        catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog",
        email: "aws_sdk_partnercentral_account.types.email.Email",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.send_email_verification_code_response.SendEmailVerificationCodeResponse":
        """<p>Sends an email verification code to the specified email address for account verification purposes.</p>

        Args:
            catalog: <p>The catalog identifier for the partner account.</p>
            email: <p>The email address to send the verification code to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.send_email_verification_code_request.SendEmailVerificationCodeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.send_email_verification_code_response.SendEmailVerificationCodeResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.send_email_verification_code

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.send_email_verification_code.async_send_email_verification_code(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.send_email_verification_code_request.SendEmailVerificationCodeRequest = {}  # type: ignore[typeddict-item]
        input_["catalog"] = catalog
        input_["email"] = email

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_verification(
        self,
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
        client_token: Optional[
            "aws_sdk_partnercentral_account.types.client_token.ClientToken"
        ] = None,
        verification_details: Optional[
            "aws_sdk_partnercentral_account.types.verification_details.VerificationDetails"
        ] = None,
    ) -> "aws_sdk_partnercentral_account.types.start_verification_response.StartVerificationResponse":
        """<p>Initiates a new verification process for a partner account. This operation begins the verification workflow for either business registration or individual registrant identity verification as required by AWS Partner Central.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This prevents duplicate verification processes from being started accidentally.</p>
            verification_details: <p>The specific details required for the verification process, including business information for business verification or personal information for registrant verification.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.start_verification_request.StartVerificationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.start_verification_response.StartVerificationResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.start_verification

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.start_verification.async_start_verification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.start_verification_request.StartVerificationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if verification_details is not None:
            input_["verification_details"] = verification_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_account.types.taggable_resource_arn.TaggableResourceArn",
        tags: "aws_sdk_partnercentral_account.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> (
        "aws_sdk_partnercentral_account.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Adds or updates tags for a specified AWS Partner Central Account resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>A list of tags to add or update for the specified resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_partnercentral_account.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "aws_sdk_partnercentral_account.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncPartnerCentralAccountClientConfig] = None,
    ) -> "aws_sdk_partnercentral_account.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes specified tags from an AWS Partner Central Account resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>A list of tag keys to remove from the specified resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_partnercentral_account.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_partnercentral_account.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_partnercentral_account._operations.partner_central_account.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_partnercentral_account._operations.partner_central_account.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_partnercentral_account.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

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
