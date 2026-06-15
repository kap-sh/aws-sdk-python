"""Generated from Smithy shape ``com.amazonaws.voiceid#VoiceID``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_voice_id._auth._signers
import aws_sdk_voice_id._auth._sigv4
from aws_sdk_voice_id._auth._identity import Credentials
from aws_sdk_voice_id._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_voice_id._auth._zapros_handler import AuthMiddleware
from aws_sdk_voice_id._pagination import resolve_path as _resolve_path
from aws_sdk_voice_id._resources.voice_id.domain_resource import AsyncDomainResource
from aws_sdk_voice_id._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.amazon_resource_name
    import aws_sdk_voice_id.types.associate_fraudster_request
    import aws_sdk_voice_id.types.associate_fraudster_response
    import aws_sdk_voice_id.types.client_token_string
    import aws_sdk_voice_id.types.create_watchlist_request
    import aws_sdk_voice_id.types.create_watchlist_response
    import aws_sdk_voice_id.types.delete_fraudster_request
    import aws_sdk_voice_id.types.delete_speaker_request
    import aws_sdk_voice_id.types.delete_watchlist_request
    import aws_sdk_voice_id.types.describe_fraudster_registration_job_request
    import aws_sdk_voice_id.types.describe_fraudster_registration_job_response
    import aws_sdk_voice_id.types.describe_fraudster_request
    import aws_sdk_voice_id.types.describe_fraudster_response
    import aws_sdk_voice_id.types.describe_speaker_enrollment_job_request
    import aws_sdk_voice_id.types.describe_speaker_enrollment_job_response
    import aws_sdk_voice_id.types.describe_speaker_request
    import aws_sdk_voice_id.types.describe_speaker_response
    import aws_sdk_voice_id.types.describe_watchlist_request
    import aws_sdk_voice_id.types.describe_watchlist_response
    import aws_sdk_voice_id.types.disassociate_fraudster_request
    import aws_sdk_voice_id.types.disassociate_fraudster_response
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.enrollment_config
    import aws_sdk_voice_id.types.evaluate_session_request
    import aws_sdk_voice_id.types.evaluate_session_response
    import aws_sdk_voice_id.types.fraudster_id
    import aws_sdk_voice_id.types.fraudster_registration_job_status
    import aws_sdk_voice_id.types.fraudster_registration_job_summary
    import aws_sdk_voice_id.types.fraudster_summary
    import aws_sdk_voice_id.types.iam_role_arn
    import aws_sdk_voice_id.types.input_data_config
    import aws_sdk_voice_id.types.job_id
    import aws_sdk_voice_id.types.job_name
    import aws_sdk_voice_id.types.list_fraudster_registration_jobs_request
    import aws_sdk_voice_id.types.list_fraudster_registration_jobs_response
    import aws_sdk_voice_id.types.list_fraudsters_request
    import aws_sdk_voice_id.types.list_fraudsters_response
    import aws_sdk_voice_id.types.list_speaker_enrollment_jobs_request
    import aws_sdk_voice_id.types.list_speaker_enrollment_jobs_response
    import aws_sdk_voice_id.types.list_speakers_request
    import aws_sdk_voice_id.types.list_speakers_response
    import aws_sdk_voice_id.types.list_tags_for_resource_request
    import aws_sdk_voice_id.types.list_tags_for_resource_response
    import aws_sdk_voice_id.types.list_watchlists_request
    import aws_sdk_voice_id.types.list_watchlists_response
    import aws_sdk_voice_id.types.max_results_for_list
    import aws_sdk_voice_id.types.next_token
    import aws_sdk_voice_id.types.opt_out_speaker_request
    import aws_sdk_voice_id.types.opt_out_speaker_response
    import aws_sdk_voice_id.types.output_data_config
    import aws_sdk_voice_id.types.registration_config
    import aws_sdk_voice_id.types.session_name_or_id
    import aws_sdk_voice_id.types.speaker_enrollment_job_status
    import aws_sdk_voice_id.types.speaker_enrollment_job_summary
    import aws_sdk_voice_id.types.speaker_id
    import aws_sdk_voice_id.types.speaker_summary
    import aws_sdk_voice_id.types.start_fraudster_registration_job_request
    import aws_sdk_voice_id.types.start_fraudster_registration_job_response
    import aws_sdk_voice_id.types.start_speaker_enrollment_job_request
    import aws_sdk_voice_id.types.start_speaker_enrollment_job_response
    import aws_sdk_voice_id.types.tag_key_list
    import aws_sdk_voice_id.types.tag_list
    import aws_sdk_voice_id.types.tag_resource_request
    import aws_sdk_voice_id.types.tag_resource_response
    import aws_sdk_voice_id.types.untag_resource_request
    import aws_sdk_voice_id.types.untag_resource_response
    import aws_sdk_voice_id.types.update_watchlist_request
    import aws_sdk_voice_id.types.update_watchlist_response
    import aws_sdk_voice_id.types.watchlist_description
    import aws_sdk_voice_id.types.watchlist_id
    import aws_sdk_voice_id.types.watchlist_name
    import aws_sdk_voice_id.types.watchlist_summary


class AsyncVoiceIDClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncVoiceIDClient:
    """A client for the ``VoiceID`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = AsyncVoiceIDClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

        # resources
        self.domain_resource = AsyncDomainResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncVoiceIDClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncVoiceIDClientConfig = config_overrides or {}
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

    async def associate_fraudster(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        watchlist_id: "aws_sdk_voice_id.types.watchlist_id.WatchlistId",
        fraudster_id: "aws_sdk_voice_id.types.fraudster_id.FraudsterId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> (
        "aws_sdk_voice_id.types.associate_fraudster_response.AssociateFraudsterResponse"
    ):
        """<p>Associates the fraudsters with the watchlist specified in the same domain. </p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster.</p>
            watchlist_id: <p>The identifier of the watchlist you want to associate with the fraudster.</p>
            fraudster_id: <p>The identifier of the fraudster to be associated with the watchlist.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.associate_fraudster_request.AssociateFraudsterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.associate_fraudster_response.AssociateFraudsterResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.associate_fraudster

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.associate_fraudster.async_associate_fraudster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.associate_fraudster_request.AssociateFraudsterRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["watchlist_id"] = watchlist_id
        input_["fraudster_id"] = fraudster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_watchlist(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        name: "aws_sdk_voice_id.types.watchlist_name.WatchlistName",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        description: Optional[
            "aws_sdk_voice_id.types.watchlist_description.WatchlistDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_voice_id.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "aws_sdk_voice_id.types.create_watchlist_response.CreateWatchlistResponse":
        r"""<p>Creates a watchlist that fraudsters can be a part of.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the watchlist.</p>
            name: <p>The name of the watchlist.</p>
            description: <p>A brief description of this watchlist.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.create_watchlist_request.CreateWatchlistRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.create_watchlist_response.CreateWatchlistResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.create_watchlist

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.create_watchlist.async_create_watchlist(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.create_watchlist_request.CreateWatchlistRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_fraudster(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        fraudster_id: "aws_sdk_voice_id.types.fraudster_id.FraudsterId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified fraudster from Voice ID. This action disassociates the fraudster from any watchlists it is a part of.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster.</p>
            fraudster_id: <p>The identifier of the fraudster you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.delete_fraudster_request.DeleteFraudsterRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_voice_id._operations.voice_id.delete_fraudster

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.delete_fraudster.async_delete_fraudster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.delete_fraudster_request.DeleteFraudsterRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["fraudster_id"] = fraudster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_speaker(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        speaker_id: "aws_sdk_voice_id.types.speaker_id.SpeakerId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified speaker from Voice ID.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the speaker.</p>
            speaker_id: <p>The identifier of the speaker you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.delete_speaker_request.DeleteSpeakerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_voice_id._operations.voice_id.delete_speaker

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.delete_speaker.async_delete_speaker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.delete_speaker_request.DeleteSpeakerRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["speaker_id"] = speaker_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_watchlist(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        watchlist_id: "aws_sdk_voice_id.types.watchlist_id.WatchlistId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified watchlist from Voice ID. This API throws an exception when there are fraudsters in the watchlist that you are trying to delete. You must delete the fraudsters, and then delete the watchlist. Every domain has a default watchlist which cannot be deleted. </p>

        Args:
            domain_id: <p>The identifier of the domain that contains the watchlist.</p>
            watchlist_id: <p>The identifier of the watchlist to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.delete_watchlist_request.DeleteWatchlistRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_voice_id._operations.voice_id.delete_watchlist

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.delete_watchlist.async_delete_watchlist(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.delete_watchlist_request.DeleteWatchlistRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["watchlist_id"] = watchlist_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_fraudster(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        fraudster_id: "aws_sdk_voice_id.types.fraudster_id.FraudsterId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.describe_fraudster_response.DescribeFraudsterResponse":
        """<p>Describes the specified fraudster.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster.</p>
            fraudster_id: <p>The identifier of the fraudster you are describing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.describe_fraudster_request.DescribeFraudsterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.describe_fraudster_response.DescribeFraudsterResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.describe_fraudster

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.describe_fraudster.async_describe_fraudster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.describe_fraudster_request.DescribeFraudsterRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["fraudster_id"] = fraudster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_fraudster_registration_job(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        job_id: "aws_sdk_voice_id.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.describe_fraudster_registration_job_response.DescribeFraudsterRegistrationJobResponse":
        """<p>Describes the specified fraudster registration job.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster registration job.</p>
            job_id: <p>The identifier of the fraudster registration job you are describing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.describe_fraudster_registration_job_request.DescribeFraudsterRegistrationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.describe_fraudster_registration_job_response.DescribeFraudsterRegistrationJobResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.describe_fraudster_registration_job

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.describe_fraudster_registration_job.async_describe_fraudster_registration_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.describe_fraudster_registration_job_request.DescribeFraudsterRegistrationJobRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_speaker(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        speaker_id: "aws_sdk_voice_id.types.speaker_id.SpeakerId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.describe_speaker_response.DescribeSpeakerResponse":
        """<p>Describes the specified speaker.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the speaker.</p>
            speaker_id: <p>The identifier of the speaker you are describing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.describe_speaker_request.DescribeSpeakerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.describe_speaker_response.DescribeSpeakerResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.describe_speaker

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.describe_speaker.async_describe_speaker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.describe_speaker_request.DescribeSpeakerRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["speaker_id"] = speaker_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_speaker_enrollment_job(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        job_id: "aws_sdk_voice_id.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.describe_speaker_enrollment_job_response.DescribeSpeakerEnrollmentJobResponse":
        """<p>Describes the specified speaker enrollment job.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the speaker enrollment job.</p>
            job_id: <p>The identifier of the speaker enrollment job you are describing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.describe_speaker_enrollment_job_request.DescribeSpeakerEnrollmentJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.describe_speaker_enrollment_job_response.DescribeSpeakerEnrollmentJobResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.describe_speaker_enrollment_job

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.describe_speaker_enrollment_job.async_describe_speaker_enrollment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.describe_speaker_enrollment_job_request.DescribeSpeakerEnrollmentJobRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_watchlist(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        watchlist_id: "aws_sdk_voice_id.types.watchlist_id.WatchlistId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.describe_watchlist_response.DescribeWatchlistResponse":
        """<p>Describes the specified watchlist.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the watchlist.</p>
            watchlist_id: <p>The identifier of the watchlist that you are describing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.describe_watchlist_request.DescribeWatchlistRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.describe_watchlist_response.DescribeWatchlistResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.describe_watchlist

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.describe_watchlist.async_describe_watchlist(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.describe_watchlist_request.DescribeWatchlistRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["watchlist_id"] = watchlist_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_fraudster(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        watchlist_id: "aws_sdk_voice_id.types.watchlist_id.WatchlistId",
        fraudster_id: "aws_sdk_voice_id.types.fraudster_id.FraudsterId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.disassociate_fraudster_response.DisassociateFraudsterResponse":
        """<p>Disassociates the fraudsters from the watchlist specified. Voice ID always expects a fraudster to be a part of at least one watchlist. If you try to disassociate a fraudster from its only watchlist, a <code>ValidationException</code> is thrown. </p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster.</p>
            watchlist_id: <p>The identifier of the watchlist that you want to disassociate from the fraudster.</p>
            fraudster_id: <p>The identifier of the fraudster to be disassociated from the watchlist.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.disassociate_fraudster_request.DisassociateFraudsterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.disassociate_fraudster_response.DisassociateFraudsterResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.disassociate_fraudster

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.disassociate_fraudster.async_disassociate_fraudster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.disassociate_fraudster_request.DisassociateFraudsterRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["watchlist_id"] = watchlist_id
        input_["fraudster_id"] = fraudster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def evaluate_session(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        session_name_or_id: "aws_sdk_voice_id.types.session_name_or_id.SessionNameOrId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.evaluate_session_response.EvaluateSessionResponse":
        """<p>Evaluates a specified session based on audio data accumulated during a streaming Amazon Connect Voice ID call.</p>

        Args:
            domain_id: <p>The identifier of the domain where the session started.</p>
            session_name_or_id: <p>The session identifier, or name of the session, that you want to evaluate. In Voice ID integration, this is the Contact-Id.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.evaluate_session_request.EvaluateSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.evaluate_session_response.EvaluateSessionResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.evaluate_session

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.evaluate_session.async_evaluate_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.evaluate_session_request.EvaluateSessionRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["session_name_or_id"] = session_name_or_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_fraudster_registration_jobs(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        job_status: Optional[
            "aws_sdk_voice_id.types.fraudster_registration_job_status.FraudsterRegistrationJobStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_voice_id.types.list_fraudster_registration_jobs_response.ListFraudsterRegistrationJobsResponse":
        """<p>Lists all the fraudster registration jobs in the domain with the given <code>JobStatus</code>. If <code>JobStatus</code> is not provided, this lists all fraudster registration jobs in the given domain. </p>

        Args:
            domain_id: <p>The identifier of the domain that contains the fraudster registration Jobs.</p>
            job_status: <p>Provides the status of your fraudster registration job.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100. </p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.list_fraudster_registration_jobs_request.ListFraudsterRegistrationJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.list_fraudster_registration_jobs_response.ListFraudsterRegistrationJobsResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.list_fraudster_registration_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.list_fraudster_registration_jobs.async_list_fraudster_registration_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.list_fraudster_registration_jobs_request.ListFraudsterRegistrationJobsRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        if job_status is not None:
            input_["job_status"] = job_status
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

    async def iter_list_fraudster_registration_jobs(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        job_status: Optional[
            "aws_sdk_voice_id.types.fraudster_registration_job_status.FraudsterRegistrationJobStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_voice_id.types.fraudster_registration_job_summary.FraudsterRegistrationJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_fraudster_registration_jobs(
                domain_id,
                config_overrides=config_overrides,
                job_status=job_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_fraudsters(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        watchlist_id: Optional[
            "aws_sdk_voice_id.types.watchlist_id.WatchlistId"
        ] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_voice_id.types.list_fraudsters_response.ListFraudstersResponse":
        """<p>Lists all fraudsters in a specified watchlist or domain.</p>

        Args:
            domain_id: <p>The identifier of the domain. </p>
            watchlist_id: <p>The identifier of the watchlist. If provided, all fraudsters in the watchlist are listed. If not provided, all fraudsters in the domain are listed.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100. </p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.list_fraudsters_request.ListFraudstersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.list_fraudsters_response.ListFraudstersResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.list_fraudsters

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.list_fraudsters.async_list_fraudsters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.list_fraudsters_request.ListFraudstersRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        if watchlist_id is not None:
            input_["watchlist_id"] = watchlist_id
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

    async def iter_list_fraudsters(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        watchlist_id: Optional[
            "aws_sdk_voice_id.types.watchlist_id.WatchlistId"
        ] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_voice_id.types.fraudster_summary.FraudsterSummary]":
        _token = next_token
        while True:
            _response = await self.list_fraudsters(
                domain_id,
                config_overrides=config_overrides,
                watchlist_id=watchlist_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fraudster_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_speaker_enrollment_jobs(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        job_status: Optional[
            "aws_sdk_voice_id.types.speaker_enrollment_job_status.SpeakerEnrollmentJobStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_voice_id.types.list_speaker_enrollment_jobs_response.ListSpeakerEnrollmentJobsResponse":
        """<p>Lists all the speaker enrollment jobs in the domain with the specified <code>JobStatus</code>. If <code>JobStatus</code> is not provided, this lists all jobs with all possible speaker enrollment job statuses.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the speaker enrollment jobs.</p>
            job_status: <p>Provides the status of your speaker enrollment Job.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100.</p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.list_speaker_enrollment_jobs_request.ListSpeakerEnrollmentJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.list_speaker_enrollment_jobs_response.ListSpeakerEnrollmentJobsResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.list_speaker_enrollment_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.list_speaker_enrollment_jobs.async_list_speaker_enrollment_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.list_speaker_enrollment_jobs_request.ListSpeakerEnrollmentJobsRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        if job_status is not None:
            input_["job_status"] = job_status
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

    async def iter_list_speaker_enrollment_jobs(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        job_status: Optional[
            "aws_sdk_voice_id.types.speaker_enrollment_job_status.SpeakerEnrollmentJobStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_voice_id.types.speaker_enrollment_job_summary.SpeakerEnrollmentJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_speaker_enrollment_jobs(
                domain_id,
                config_overrides=config_overrides,
                job_status=job_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_speakers(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_voice_id.types.list_speakers_response.ListSpeakersResponse":
        """<p>Lists all speakers in a specified domain.</p>

        Args:
            domain_id: <p>The identifier of the domain.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100. </p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.list_speakers_request.ListSpeakersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.list_speakers_response.ListSpeakersResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.list_speakers

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.list_speakers.async_list_speakers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.list_speakers_request.ListSpeakersRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_speakers(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_voice_id.types.speaker_summary.SpeakerSummary]":
        _token = next_token
        while True:
            _response = await self.list_speakers(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("speaker_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_voice_id.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with a specified Voice ID resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Voice ID resource for which you want to list the tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_watchlists(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_voice_id.types.list_watchlists_response.ListWatchlistsResponse":
        """<p>Lists all watchlists in a specified domain.</p>

        Args:
            domain_id: <p>The identifier of the domain.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100. </p>
            next_token: <p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.list_watchlists_request.ListWatchlistsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.list_watchlists_response.ListWatchlistsResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.list_watchlists

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.list_watchlists.async_list_watchlists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.list_watchlists_request.ListWatchlistsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_watchlists(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        max_results: Optional[
            "aws_sdk_voice_id.types.max_results_for_list.MaxResultsForList"
        ] = None,
        next_token: Optional["aws_sdk_voice_id.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_voice_id.types.watchlist_summary.WatchlistSummary]":
        _token = next_token
        while True:
            _response = await self.list_watchlists(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("watchlist_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def opt_out_speaker(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        speaker_id: "aws_sdk_voice_id.types.speaker_id.SpeakerId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.opt_out_speaker_response.OptOutSpeakerResponse":
        """<p>Opts out a speaker from Voice ID. A speaker can be opted out regardless of whether or not they already exist in Voice ID. If they don't yet exist, a new speaker is created in an opted out state. If they already exist, their existing status is overridden and they are opted out. Enrollment and evaluation authentication requests are rejected for opted out speakers, and opted out speakers have no voice embeddings stored in Voice ID.</p>

        Args:
            domain_id: <p>The identifier of the domain that contains the speaker.</p>
            speaker_id: <p>The identifier of the speaker you want opted-out.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.opt_out_speaker_request.OptOutSpeakerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.opt_out_speaker_response.OptOutSpeakerResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.opt_out_speaker

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.opt_out_speaker.async_opt_out_speaker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.opt_out_speaker_request.OptOutSpeakerRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["speaker_id"] = speaker_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_fraudster_registration_job(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        data_access_role_arn: "aws_sdk_voice_id.types.iam_role_arn.IamRoleArn",
        input_data_config: "aws_sdk_voice_id.types.input_data_config.InputDataConfig",
        output_data_config: "aws_sdk_voice_id.types.output_data_config.OutputDataConfig",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        client_token: Optional[
            "aws_sdk_voice_id.types.client_token_string.ClientTokenString"
        ] = None,
        job_name: Optional["aws_sdk_voice_id.types.job_name.JobName"] = None,
        registration_config: Optional[
            "aws_sdk_voice_id.types.registration_config.RegistrationConfig"
        ] = None,
    ) -> "aws_sdk_voice_id.types.start_fraudster_registration_job_response.StartFraudsterRegistrationJobResponse":
        r"""<p>Starts a new batch fraudster registration job using provided details.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            job_name: <p>The name of the new fraudster registration job.</p>
            domain_id: <p>The identifier of the domain that contains the fraudster registration job and in which the fraudsters are registered.</p>
            data_access_role_arn: <p>The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the Job output file. Refer to the <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/voiceid-fraudster-watchlist.html\">Create and edit a fraudster watchlist</a> documentation for the permissions needed in this role.</p>
            registration_config: <p>The registration config containing details such as the action to take when a duplicate fraudster is detected, and the similarity threshold to use for detecting a duplicate fraudster. </p>
            input_data_config: <p>The input data config containing an S3 URI for the input manifest file that contains the list of fraudster registration requests.</p>
            output_data_config: <p>The output data config containing the S3 location where Voice ID writes the job output file; you must also include a KMS key ID to encrypt the file.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.start_fraudster_registration_job_request.StartFraudsterRegistrationJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.start_fraudster_registration_job_response.StartFraudsterRegistrationJobResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.start_fraudster_registration_job

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.start_fraudster_registration_job.async_start_fraudster_registration_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.start_fraudster_registration_job_request.StartFraudsterRegistrationJobRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if job_name is not None:
            input_["job_name"] = job_name
        input_["domain_id"] = domain_id
        input_["data_access_role_arn"] = data_access_role_arn
        if registration_config is not None:
            input_["registration_config"] = registration_config
        input_["input_data_config"] = input_data_config
        input_["output_data_config"] = output_data_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_speaker_enrollment_job(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        data_access_role_arn: "aws_sdk_voice_id.types.iam_role_arn.IamRoleArn",
        input_data_config: "aws_sdk_voice_id.types.input_data_config.InputDataConfig",
        output_data_config: "aws_sdk_voice_id.types.output_data_config.OutputDataConfig",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        client_token: Optional[
            "aws_sdk_voice_id.types.client_token_string.ClientTokenString"
        ] = None,
        job_name: Optional["aws_sdk_voice_id.types.job_name.JobName"] = None,
        enrollment_config: Optional[
            "aws_sdk_voice_id.types.enrollment_config.EnrollmentConfig"
        ] = None,
    ) -> "aws_sdk_voice_id.types.start_speaker_enrollment_job_response.StartSpeakerEnrollmentJobResponse":
        r"""<p>Starts a new batch speaker enrollment job using specified details.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            job_name: <p>A name for your speaker enrollment job.</p>
            domain_id: <p>The identifier of the domain that contains the speaker enrollment job and in which the speakers are enrolled. </p>
            data_access_role_arn: <p>The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the job output file. Refer to <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/voiceid-batch-enrollment.html\">Batch enrollment using audio data from prior calls</a> for the permissions needed in this role.</p>
            enrollment_config: <p>The enrollment config that contains details such as the action to take when a speaker is already enrolled in Voice ID or when a speaker is identified as a fraudster.</p>
            input_data_config: <p>The input data config containing the S3 location for the input manifest file that contains the list of speaker enrollment requests.</p>
            output_data_config: <p>The output data config containing the S3 location where Voice ID writes the job output file; you must also include a KMS key ID to encrypt the file.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.start_speaker_enrollment_job_request.StartSpeakerEnrollmentJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.start_speaker_enrollment_job_response.StartSpeakerEnrollmentJobResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.start_speaker_enrollment_job

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.start_speaker_enrollment_job.async_start_speaker_enrollment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.start_speaker_enrollment_job_request.StartSpeakerEnrollmentJobRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if job_name is not None:
            input_["job_name"] = job_name
        input_["domain_id"] = domain_id
        input_["data_access_role_arn"] = data_access_role_arn
        if enrollment_config is not None:
            input_["enrollment_config"] = enrollment_config
        input_["input_data_config"] = input_data_config
        input_["output_data_config"] = output_data_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_voice_id.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_voice_id.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a Voice ID resource with the provided list of tags.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Voice ID resource you want to tag.</p>
            tags: <p>The list of tags to assign to the specified resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_voice_id.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_voice_id.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
    ) -> "aws_sdk_voice_id.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes specified tags from a specified Amazon Connect Voice ID resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Voice ID resource you want to remove tags from.</p>
            tag_keys: <p>The list of tag keys you want to remove from the specified resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_watchlist(
        self,
        domain_id: "aws_sdk_voice_id.types.domain_id.DomainId",
        watchlist_id: "aws_sdk_voice_id.types.watchlist_id.WatchlistId",
        *,
        config_overrides: Optional[AsyncVoiceIDClientConfig] = None,
        name: Optional["aws_sdk_voice_id.types.watchlist_name.WatchlistName"] = None,
        description: Optional[
            "aws_sdk_voice_id.types.watchlist_description.WatchlistDescription"
        ] = None,
    ) -> "aws_sdk_voice_id.types.update_watchlist_response.UpdateWatchlistResponse":
        """<p>Updates the specified watchlist. Every domain has a default watchlist which cannot be updated. </p>

        Args:
            domain_id: <p>The identifier of the domain that contains the watchlist.</p>
            watchlist_id: <p>The identifier of the watchlist to be updated.</p>
            name: <p>The name of the watchlist.</p>
            description: <p>A brief description about this watchlist.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_voice_id.types.update_watchlist_request.UpdateWatchlistRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_voice_id.types.update_watchlist_response.UpdateWatchlistResponse"
        ]:
            import aws_sdk_voice_id._operations.voice_id.update_watchlist

            (
                output,
                http_response,
            ) = await aws_sdk_voice_id._operations.voice_id.update_watchlist.async_update_watchlist(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_voice_id.types.update_watchlist_request.UpdateWatchlistRequest = {}  # type: ignore[typeddict-item]
        input_["domain_id"] = domain_id
        input_["watchlist_id"] = watchlist_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

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
