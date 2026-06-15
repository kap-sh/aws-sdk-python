"""Generated from Smithy shape ``com.amazonaws.connecthealth#ConnectHealth``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_connecthealth._auth._signers
import aws_sdk_connecthealth._auth._sigv4
from aws_sdk_connecthealth._auth._identity import Credentials
from aws_sdk_connecthealth._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_connecthealth._auth._zapros_handler import AuthMiddleware
from aws_sdk_connecthealth._pagination import resolve_path as _resolve_path
from aws_sdk_connecthealth._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.activate_subscription_input
    import aws_sdk_connecthealth.types.activate_subscription_output
    import aws_sdk_connecthealth.types.create_domain_input
    import aws_sdk_connecthealth.types.create_domain_output
    import aws_sdk_connecthealth.types.create_subscription_input
    import aws_sdk_connecthealth.types.create_subscription_output
    import aws_sdk_connecthealth.types.create_web_app_configuration
    import aws_sdk_connecthealth.types.deactivate_subscription_input
    import aws_sdk_connecthealth.types.deactivate_subscription_output
    import aws_sdk_connecthealth.types.delete_domain_input
    import aws_sdk_connecthealth.types.delete_domain_output
    import aws_sdk_connecthealth.types.domain_id
    import aws_sdk_connecthealth.types.domain_name
    import aws_sdk_connecthealth.types.domain_status
    import aws_sdk_connecthealth.types.domain_summary
    import aws_sdk_connecthealth.types.get_domain_input
    import aws_sdk_connecthealth.types.get_domain_output
    import aws_sdk_connecthealth.types.get_medical_scribe_listening_session_input
    import aws_sdk_connecthealth.types.get_medical_scribe_listening_session_output
    import aws_sdk_connecthealth.types.get_patient_insights_job_request
    import aws_sdk_connecthealth.types.get_patient_insights_job_response
    import aws_sdk_connecthealth.types.get_subscription_input
    import aws_sdk_connecthealth.types.get_subscription_output
    import aws_sdk_connecthealth.types.input_data_config
    import aws_sdk_connecthealth.types.insights_context
    import aws_sdk_connecthealth.types.job_id
    import aws_sdk_connecthealth.types.kms_key_arn
    import aws_sdk_connecthealth.types.list_domains_input
    import aws_sdk_connecthealth.types.list_domains_output
    import aws_sdk_connecthealth.types.list_subscriptions_input
    import aws_sdk_connecthealth.types.list_subscriptions_output
    import aws_sdk_connecthealth.types.list_tags_for_resource_input
    import aws_sdk_connecthealth.types.list_tags_for_resource_output
    import aws_sdk_connecthealth.types.medical_scribe_input_stream
    import aws_sdk_connecthealth.types.medical_scribe_language_code
    import aws_sdk_connecthealth.types.medical_scribe_media_encoding
    import aws_sdk_connecthealth.types.medical_scribe_media_sample_rate_hertz
    import aws_sdk_connecthealth.types.non_empty_string
    import aws_sdk_connecthealth.types.output_data_config
    import aws_sdk_connecthealth.types.patient_insights_encounter_context
    import aws_sdk_connecthealth.types.patient_insights_patient_context
    import aws_sdk_connecthealth.types.scribe_session_id
    import aws_sdk_connecthealth.types.start_medical_scribe_listening_session_input
    import aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output
    import aws_sdk_connecthealth.types.start_patient_insights_job_request
    import aws_sdk_connecthealth.types.start_patient_insights_job_response
    import aws_sdk_connecthealth.types.subscription_description
    import aws_sdk_connecthealth.types.subscription_id
    import aws_sdk_connecthealth.types.tag_key_list
    import aws_sdk_connecthealth.types.tag_map
    import aws_sdk_connecthealth.types.tag_resource_input
    import aws_sdk_connecthealth.types.untag_resource_input
    import aws_sdk_connecthealth.types.user_context


class AsyncConnectHealthClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncConnectHealthClient:
    """A client for the ``ConnectHealth`` service.

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
        self._config = AsyncConnectHealthClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncConnectHealthClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncConnectHealthClientConfig = config_overrides or {}
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

    async def activate_subscription(
        self,
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        subscription_id: "aws_sdk_connecthealth.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "aws_sdk_connecthealth.types.activate_subscription_output.ActivateSubscriptionOutput":
        """<p>Activates a Subscription to enable billing for a user.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            subscription_id: <p>The unique identifier of the Subscription.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.activate_subscription_input.ActivateSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.activate_subscription_output.ActivateSubscriptionOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.activate_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.activate_subscription.async_activate_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.activate_subscription_input.ActivateSubscriptionInput = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["subscription_id"] = subscription_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_domain(
        self,
        name: "aws_sdk_connecthealth.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        kms_key_arn: Optional[
            "aws_sdk_connecthealth.types.kms_key_arn.KmsKeyArn"
        ] = None,
        web_app_setup_configuration: Optional[
            "aws_sdk_connecthealth.types.create_web_app_configuration.CreateWebAppConfiguration"
        ] = None,
        tags: Optional["aws_sdk_connecthealth.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_connecthealth.types.create_domain_output.CreateDomainOutput":
        """<p>Creates a new Domain for managing HealthAgent resources.</p>

        Args:
            name: <p>The name for the new Domain.</p>
            kms_key_arn: <p>The ARN of the KMS key to use for encrypting data in this Domain.</p>
            web_app_setup_configuration: <p>Configuration for the Domain web application. Optional, but if provided all fields are required.</p>
            tags: <p>Tags to associate with the Domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.create_domain_input.CreateDomainInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.create_domain_output.CreateDomainOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.create_domain

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.create_domain_input.CreateDomainInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if web_app_setup_configuration is not None:
            input_["web_app_setup_configuration"] = web_app_setup_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_subscription(
        self,
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "aws_sdk_connecthealth.types.create_subscription_output.CreateSubscriptionOutput":
        """<p>Creates a new Subscription within a Domain for billing and user management.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.create_subscription_input.CreateSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.create_subscription_output.CreateSubscriptionOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.create_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.create_subscription.async_create_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.create_subscription_input.CreateSubscriptionInput = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def deactivate_subscription(
        self,
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        subscription_id: "aws_sdk_connecthealth.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "aws_sdk_connecthealth.types.deactivate_subscription_output.DeactivateSubscriptionOutput":
        """<p>Deactivates a Subscription to stop billing for a user.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            subscription_id: <p>The unique identifier of the Subscription.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.deactivate_subscription_input.DeactivateSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.deactivate_subscription_output.DeactivateSubscriptionOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.deactivate_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.deactivate_subscription.async_deactivate_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.deactivate_subscription_input.DeactivateSubscriptionInput = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["subscription_id"] = subscription_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_domain(
        self,
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "aws_sdk_connecthealth.types.delete_domain_output.DeleteDomainOutput":
        """<p>Deletes a Domain and all associated resources.</p>

        Args:
            domain_id: <p>The id of the Domain to delete</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.delete_domain_input.DeleteDomainInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.delete_domain_output.DeleteDomainOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.delete_domain

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.delete_domain_input.DeleteDomainInput = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_domain(
        self,
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "aws_sdk_connecthealth.types.get_domain_output.GetDomainOutput":
        """<p>Retrieves information about a Domain.</p>

        Args:
            domain_id: <p>The id of the Domain to get</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.get_domain_input.GetDomainInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.get_domain_output.GetDomainOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.get_domain

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.get_domain.async_get_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.get_domain_input.GetDomainInput = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_medical_scribe_listening_session(
        self,
        session_id: "aws_sdk_connecthealth.types.scribe_session_id.ScribeSessionId",
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        subscription_id: "aws_sdk_connecthealth.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "aws_sdk_connecthealth.types.get_medical_scribe_listening_session_output.GetMedicalScribeListeningSessionOutput":
        """<p>Retrieves details about an existing Medical Scribe listening session</p>

        Args:
            session_id: <p>The Session identifier</p>
            domain_id: <p>The Domain identifier</p>
            subscription_id: <p>The Subscription identifier</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.get_medical_scribe_listening_session_input.GetMedicalScribeListeningSessionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.get_medical_scribe_listening_session_output.GetMedicalScribeListeningSessionOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.get_medical_scribe_listening_session

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.get_medical_scribe_listening_session.async_get_medical_scribe_listening_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.get_medical_scribe_listening_session_input.GetMedicalScribeListeningSessionInput = {}  # type: ignore[typeddict-item]
        input_["session_id"] = session_id
        input_["domain_id"] = domain_id
        input_["subscription_id"] = subscription_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_patient_insights_job(
        self,
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        job_id: "aws_sdk_connecthealth.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "aws_sdk_connecthealth.types.get_patient_insights_job_response.GetPatientInsightsJobResponse":
        """<p>Get details of a started patient insights job.</p>

        Args:
            domain_id: <p/>
            job_id: <p/>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.get_patient_insights_job_request.GetPatientInsightsJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.get_patient_insights_job_response.GetPatientInsightsJobResponse"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.get_patient_insights_job

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.get_patient_insights_job.async_get_patient_insights_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.get_patient_insights_job_request.GetPatientInsightsJobRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_subscription(
        self,
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        subscription_id: "aws_sdk_connecthealth.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "aws_sdk_connecthealth.types.get_subscription_output.GetSubscriptionOutput":
        """<p>Retrieves information about a Subscription.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            subscription_id: <p>The unique identifier of the Subscription.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.get_subscription_input.GetSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.get_subscription_output.GetSubscriptionOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.get_subscription

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.get_subscription.async_get_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.get_subscription_input.GetSubscriptionInput = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["subscription_id"] = subscription_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_domains(
        self,
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        status: Optional[
            "aws_sdk_connecthealth.types.domain_status.DomainStatus"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_connecthealth.types.list_domains_output.ListDomainsOutput":
        """<p>Lists Domains for a given account.</p>

        Args:
            status: <p>Filter by Domain status.</p>
            max_results: <p>Maximum number of results to return.</p>
            next_token: <p>Token for pagination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.list_domains_input.ListDomainsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.list_domains_output.ListDomainsOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.list_domains

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.list_domains_input.ListDomainsInput = {}  # type: ignore[typeddict-item]
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_domains(
        self,
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        status: Optional[
            "aws_sdk_connecthealth.types.domain_status.DomainStatus"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[aws_sdk_connecthealth.types.domain_summary.DomainSummary]":
        _token = next_token
        while True:
            _response = await self.list_domains(
                config_overrides=config_overrides,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("domains",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscriptions(
        self,
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> (
        "aws_sdk_connecthealth.types.list_subscriptions_output.ListSubscriptionsOutput"
    ):
        """<p>Lists all Subscriptions within a Domain.</p>

        Args:
            domain_id: <p>The unique identifier of the parent Domain.</p>
            max_results: <p>Maximum number of results to return.</p>
            next_token: <p>Token for pagination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.list_subscriptions_input.ListSubscriptionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.list_subscriptions_output.ListSubscriptionsOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.list_subscriptions

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.list_subscriptions.async_list_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.list_subscriptions_input.ListSubscriptionsInput = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_subscriptions(
        self,
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[aws_sdk_connecthealth.types.subscription_description.SubscriptionDescription]":
        _token = next_token
        while True:
            _response = await self.list_subscriptions(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> "aws_sdk_connecthealth.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags associated with the specified resource</p>

        Args:
            resource_arn: <p>The ARN of the resource to list tags for</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_medical_scribe_listening_session(
        self,
        session_id: "aws_sdk_connecthealth.types.scribe_session_id.ScribeSessionId",
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        subscription_id: "aws_sdk_connecthealth.types.subscription_id.SubscriptionId",
        language_code: "aws_sdk_connecthealth.types.medical_scribe_language_code.MedicalScribeLanguageCode",
        media_sample_rate_hertz: "aws_sdk_connecthealth.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz",
        media_encoding: "aws_sdk_connecthealth.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        input_stream: Optional[AsyncIterator[bytes] | bytes] = None,
    ) -> "aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput":
        """<p>Starts a new Medical Scribe listening session for real-time audio transcription</p>

        Args:
            session_id: <p>The Session identifier</p>
            domain_id: <p>The Domain identifier</p>
            subscription_id: <p>The Subscription identifier</p>
            language_code: <p>The Language Code for the audio in the session</p>
            media_sample_rate_hertz: <p>The sample rate of the input audio</p>
            media_encoding: <p>The encoding for the input audio</p>
            input_stream: <p/>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.start_medical_scribe_listening_session_output.StartMedicalScribeListeningSessionOutput"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.start_medical_scribe_listening_session

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.start_medical_scribe_listening_session.async_start_medical_scribe_listening_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.start_medical_scribe_listening_session_input.StartMedicalScribeListeningSessionInput = {}  # type: ignore[typeddict-item]
        input_["session_id"] = session_id
        input_["domain_id"] = domain_id
        input_["subscription_id"] = subscription_id
        input_["language_code"] = language_code
        input_["media_sample_rate_hertz"] = media_sample_rate_hertz
        input_["media_encoding"] = media_encoding
        if input_stream is not None:
            input_["input_stream"] = ensure_async_iterator(input_stream)  # type: ignore

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_patient_insights_job(
        self,
        domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId",
        patient_context: "aws_sdk_connecthealth.types.patient_insights_patient_context.PatientInsightsPatientContext",
        insights_context: "aws_sdk_connecthealth.types.insights_context.InsightsContext",
        encounter_context: "aws_sdk_connecthealth.types.patient_insights_encounter_context.PatientInsightsEncounterContext",
        user_context: "aws_sdk_connecthealth.types.user_context.UserContext",
        input_data_config: "aws_sdk_connecthealth.types.input_data_config.InputDataConfig",
        output_data_config: "aws_sdk_connecthealth.types.output_data_config.OutputDataConfig",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
        client_token: Optional[
            "aws_sdk_connecthealth.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "aws_sdk_connecthealth.types.start_patient_insights_job_response.StartPatientInsightsJobResponse":
        """<p>Starts a new patient insights job.</p>

        Args:
            domain_id: <p/>
            patient_context: <p/>
            insights_context: <p/>
            encounter_context: <p/>
            user_context: <p/>
            input_data_config: <p/>
            output_data_config: <p/>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.start_patient_insights_job_request.StartPatientInsightsJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_connecthealth.types.start_patient_insights_job_response.StartPatientInsightsJobResponse"
        ]:
            import aws_sdk_connecthealth._operations.connect_health.start_patient_insights_job

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.start_patient_insights_job.async_start_patient_insights_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.start_patient_insights_job_request.StartPatientInsightsJobRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["patient_context"] = patient_context
        input_["insights_context"] = insights_context
        input_["encounter_context"] = encounter_context
        input_["user_context"] = user_context
        input_["input_data_config"] = input_data_config
        input_["output_data_config"] = output_data_config
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: str,
        tags: "aws_sdk_connecthealth.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> None:
        """<p>Associates the specified tags with the specified resource</p>

        Args:
            resource_arn: <p>The ARN of the resource to tag</p>
            tags: <p>The tags to add to the resource</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_connecthealth._operations.connect_health.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: str,
        tag_keys: "aws_sdk_connecthealth.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncConnectHealthClientConfig] = None,
    ) -> None:
        """<p>Removes the specified tags from the specified resource</p>

        Args:
            resource_arn: <p>The ARN of the resource to untag</p>
            tag_keys: <p>The tag keys to remove from the resource</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_connecthealth.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_connecthealth._operations.connect_health.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_connecthealth._operations.connect_health.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_connecthealth.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
