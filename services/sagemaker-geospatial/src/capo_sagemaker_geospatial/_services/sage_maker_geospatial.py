"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#SageMakerGeospatial``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_sagemaker_geospatial._auth._signers
import capo_sagemaker_geospatial._auth._sigv4
from capo_sagemaker_geospatial._auth._identity import Credentials
from capo_sagemaker_geospatial._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sagemaker_geospatial._auth._zapros_handler import AuthMiddleware
from capo_sagemaker_geospatial._resources.sage_maker_geospatial.earth_observation_job import (
    EarthObservationJob,
)
from capo_sagemaker_geospatial._resources.sage_maker_geospatial.raster_data_collection import (
    RasterDataCollection,
)
from capo_sagemaker_geospatial._resources.sage_maker_geospatial.vector_enrichment_job import (
    VectorEnrichmentJob,
)
from capo_sagemaker_geospatial._services._aws_config import aws_config
from capo_sagemaker_geospatial._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.arn
    import capo_sagemaker_geospatial.types.list_tags_for_resource_request
    import capo_sagemaker_geospatial.types.list_tags_for_resource_response
    import capo_sagemaker_geospatial.types.tag_key_list
    import capo_sagemaker_geospatial.types.tag_resource_request
    import capo_sagemaker_geospatial.types.tag_resource_response
    import capo_sagemaker_geospatial.types.tags
    import capo_sagemaker_geospatial.types.untag_resource_request
    import capo_sagemaker_geospatial.types.untag_resource_response


class SageMakerGeospatialClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class SageMakerGeospatialClient:
    """A client for the ``SageMakerGeospatial`` service.

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
        self._config = SageMakerGeospatialClientConfig(
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
        self.earth_observation_job = EarthObservationJob(self)
        self.raster_data_collection = RasterDataCollection(self)
        self.vector_enrichment_job = VectorEnrichmentJob(self)

    def operation_options(
        self, config_overrides: Optional[SageMakerGeospatialClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SageMakerGeospatialClientConfig = config_overrides or {}
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
        resource_arn: "capo_sagemaker_geospatial.types.arn.Arn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags attached to the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource you want to tag.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_tags_for_resource

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_sagemaker_geospatial.types.arn.Arn",
        tags: "capo_sagemaker_geospatial.types.tags.Tags",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.tag_resource_response.TagResourceResponse":
        """<p>The resource you want to tag.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource you want to tag.</p>
            tags: <p>Each tag consists of a key and a value.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.tag_resource

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "capo_sagemaker_geospatial.types.arn.Arn",
        tag_keys: "capo_sagemaker_geospatial.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> (
        "capo_sagemaker_geospatial.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>The resource you want to untag.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource you want to untag.</p>
            tag_keys: <p>Keys of the tags you want to remove.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.untag_resource

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
