"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AWSStarkControlService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_cleanroomsml._auth._signers
import aws_sdk_cleanroomsml._auth._sigv4
from aws_sdk_cleanroomsml._auth._identity import Credentials
from aws_sdk_cleanroomsml._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_cleanroomsml._auth._zapros_handler import AuthMiddleware
from aws_sdk_cleanroomsml._pagination import resolve_path as _resolve_path
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.audience_export_job import (
    AsyncAudienceExportJob,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.audience_generation_job import (
    AsyncAudienceGenerationJob,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.audience_model import (
    AsyncAudienceModel,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.configured_audience_model import (
    AsyncConfiguredAudienceModel,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.configured_audience_model_policy import (
    AsyncConfiguredAudienceModelPolicy,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.configured_model_algorithm import (
    AsyncConfiguredModelAlgorithm,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.configured_model_algorithm_association import (
    AsyncConfiguredModelAlgorithmAssociation,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.ml_configuration import (
    AsyncMLConfiguration,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.ml_input_channel import (
    AsyncMLInputChannel,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.trained_model import (
    AsyncTrainedModel,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.trained_model_export_job import (
    AsyncTrainedModelExportJob,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.trained_model_inference_job import (
    AsyncTrainedModelInferenceJob,
)
from aws_sdk_cleanroomsml._resources.aws_stark_control_service.training_dataset import (
    AsyncTrainingDataset,
)
from aws_sdk_cleanroomsml._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.collaboration_configured_model_algorithm_association_summary
    import aws_sdk_cleanroomsml.types.collaboration_ml_input_channel_summary
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_summary
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_inference_job_summary
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_summary
    import aws_sdk_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_request
    import aws_sdk_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_response
    import aws_sdk_cleanroomsml.types.list_collaboration_ml_input_channels_request
    import aws_sdk_cleanroomsml.types.list_collaboration_ml_input_channels_response
    import aws_sdk_cleanroomsml.types.list_collaboration_trained_model_export_jobs_request
    import aws_sdk_cleanroomsml.types.list_collaboration_trained_model_export_jobs_response
    import aws_sdk_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_request
    import aws_sdk_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_response
    import aws_sdk_cleanroomsml.types.list_collaboration_trained_models_request
    import aws_sdk_cleanroomsml.types.list_collaboration_trained_models_response
    import aws_sdk_cleanroomsml.types.list_tags_for_resource_request
    import aws_sdk_cleanroomsml.types.list_tags_for_resource_response
    import aws_sdk_cleanroomsml.types.max_results
    import aws_sdk_cleanroomsml.types.next_token
    import aws_sdk_cleanroomsml.types.tag_keys
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.tag_resource_request
    import aws_sdk_cleanroomsml.types.tag_resource_response
    import aws_sdk_cleanroomsml.types.taggable_arn
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.untag_resource_request
    import aws_sdk_cleanroomsml.types.untag_resource_response
    import aws_sdk_cleanroomsml.types.uuid


class AsyncCleanRoomsMLClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
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


class AsyncCleanRoomsMLClient:
    """A client for the ``CleanRoomsML`` service.

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
        self.config = AsyncCleanRoomsMLClientConfig(
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
        self.audience_export_job = AsyncAudienceExportJob(self)
        self.audience_generation_job = AsyncAudienceGenerationJob(self)
        self.audience_model = AsyncAudienceModel(self)
        self.configured_audience_model = AsyncConfiguredAudienceModel(self)
        self.configured_audience_model_policy = AsyncConfiguredAudienceModelPolicy(self)
        self.configured_model_algorithm = AsyncConfiguredModelAlgorithm(self)
        self.configured_model_algorithm_association = (
            AsyncConfiguredModelAlgorithmAssociation(self)
        )
        self.ml_configuration = AsyncMLConfiguration(self)
        self.ml_input_channel = AsyncMLInputChannel(self)
        self.trained_model = AsyncTrainedModel(self)
        self.trained_model_export_job = AsyncTrainedModelExportJob(self)
        self.trained_model_inference_job = AsyncTrainedModelInferenceJob(self)
        self.training_dataset = AsyncTrainingDataset(self)

    def operation_options(
        self, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCleanRoomsMLClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def list_collaboration_configured_model_algorithm_associations(
        self,
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_response.ListCollaborationConfiguredModelAlgorithmAssociationsResponse":
        """<p>Returns a list of the configured model algorithm associations in a collaboration.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the configured model algorithm associations that you are interested in.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_request.ListCollaborationConfiguredModelAlgorithmAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_response.ListCollaborationConfiguredModelAlgorithmAssociationsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_collaboration_configured_model_algorithm_associations

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_collaboration_configured_model_algorithm_associations.async_list_collaboration_configured_model_algorithm_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_request.ListCollaborationConfiguredModelAlgorithmAssociationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["collaboration_identifier"] = collaboration_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_collaboration_configured_model_algorithm_associations(
        self,
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_cleanroomsml.types.collaboration_configured_model_algorithm_association_summary.CollaborationConfiguredModelAlgorithmAssociationSummary]":
        _token = next_token
        while True:
            _response = (
                await self.list_collaboration_configured_model_algorithm_associations(
                    collaboration_identifier,
                    config_overrides=config_overrides,
                    next_token=_token,
                    max_results=max_results,
                )
            )
            _page = _resolve_path(
                _response, ("collaboration_configured_model_algorithm_associations",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_ml_input_channels(
        self,
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_collaboration_ml_input_channels_response.ListCollaborationMLInputChannelsResponse":
        """<p>Returns a list of the ML input channels in a collaboration.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum number of results to return.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the ML input channels that you want to list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_collaboration_ml_input_channels_request.ListCollaborationMLInputChannelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_collaboration_ml_input_channels_response.ListCollaborationMLInputChannelsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_collaboration_ml_input_channels

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_collaboration_ml_input_channels.async_list_collaboration_ml_input_channels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_collaboration_ml_input_channels_request.ListCollaborationMLInputChannelsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["collaboration_identifier"] = collaboration_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_collaboration_ml_input_channels(
        self,
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_cleanroomsml.types.collaboration_ml_input_channel_summary.CollaborationMLInputChannelSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_ml_input_channels(
                collaboration_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("collaboration_ml_input_channels_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_trained_model_export_jobs(
        self,
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
        trained_model_version_identifier: Optional[
            "aws_sdk_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_collaboration_trained_model_export_jobs_response.ListCollaborationTrainedModelExportJobsResponse":
        """<p>Returns a list of the export jobs for a trained model in a collaboration.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the trained model export jobs that you are interested in.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that was used to create the export jobs that you are interested in.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to filter export jobs by. When specified, only export jobs for this specific version of the trained model are returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_collaboration_trained_model_export_jobs_request.ListCollaborationTrainedModelExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_collaboration_trained_model_export_jobs_response.ListCollaborationTrainedModelExportJobsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_model_export_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_model_export_jobs.async_list_collaboration_trained_model_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_collaboration_trained_model_export_jobs_request.ListCollaborationTrainedModelExportJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["collaboration_identifier"] = collaboration_identifier
        input_["trained_model_arn"] = trained_model_arn
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_collaboration_trained_model_export_jobs(
        self,
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
        trained_model_version_identifier: Optional[
            "aws_sdk_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_cleanroomsml.types.collaboration_trained_model_export_job_summary.CollaborationTrainedModelExportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_trained_model_export_jobs(
                collaboration_identifier,
                trained_model_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                trained_model_version_identifier=trained_model_version_identifier,
            )
            _page = _resolve_path(
                _response, ("collaboration_trained_model_export_jobs",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_trained_model_inference_jobs(
        self,
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
        trained_model_arn: Optional[
            "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
        ] = None,
        trained_model_version_identifier: Optional[
            "aws_sdk_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_response.ListCollaborationTrainedModelInferenceJobsResponse":
        """<p>Returns a list of trained model inference jobs in a specified collaboration.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the trained model inference jobs that you are interested in.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that was used to create the trained model inference jobs that you are interested in.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to filter inference jobs by. When specified, only inference jobs that used this specific version of the trained model are returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_request.ListCollaborationTrainedModelInferenceJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_response.ListCollaborationTrainedModelInferenceJobsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_model_inference_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_model_inference_jobs.async_list_collaboration_trained_model_inference_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_request.ListCollaborationTrainedModelInferenceJobsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["collaboration_identifier"] = collaboration_identifier
        if trained_model_arn is not None:
            input_["trained_model_arn"] = trained_model_arn
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_collaboration_trained_model_inference_jobs(
        self,
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
        trained_model_arn: Optional[
            "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
        ] = None,
        trained_model_version_identifier: Optional[
            "aws_sdk_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_cleanroomsml.types.collaboration_trained_model_inference_job_summary.CollaborationTrainedModelInferenceJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_trained_model_inference_jobs(
                collaboration_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                trained_model_arn=trained_model_arn,
                trained_model_version_identifier=trained_model_version_identifier,
            )
            _page = _resolve_path(
                _response, ("collaboration_trained_model_inference_jobs",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_trained_models(
        self,
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_collaboration_trained_models_response.ListCollaborationTrainedModelsResponse":
        """<p>Returns a list of the trained models in a collaboration.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the trained models you are interested in.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_collaboration_trained_models_request.ListCollaborationTrainedModelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_collaboration_trained_models_response.ListCollaborationTrainedModelsResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_models

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_models.async_list_collaboration_trained_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_collaboration_trained_models_request.ListCollaborationTrainedModelsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["collaboration_identifier"] = collaboration_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_collaboration_trained_models(
        self,
        collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["aws_sdk_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_cleanroomsml.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_cleanroomsml.types.collaboration_trained_model_summary.CollaborationTrainedModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_trained_models(
                collaboration_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("collaboration_trained_models",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_cleanroomsml.types.taggable_arn.TaggableArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a provided resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you are interested in.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_cleanroomsml.types.taggable_arn.TaggableArn",
        tags: "aws_sdk_cleanroomsml.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.tag_resource_response.TagResourceResponse":
        """<p>Adds metadata tags to a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to assign tags.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_cleanroomsml.types.taggable_arn.TaggableArn",
        tag_keys: "aws_sdk_cleanroomsml.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "aws_sdk_cleanroomsml.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes metadata tags from a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from.</p>
            tag_keys: <p>The key values of tags that you want to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cleanroomsml.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cleanroomsml.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_cleanroomsml._operations.aws_stark_control_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cleanroomsml._operations.aws_stark_control_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cleanroomsml.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
