"""Generated from Smithy shape ``com.amazonaws.groundstation#GroundStation``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_groundstation._auth._signers
import aws_sdk_groundstation._auth._sigv4
from aws_sdk_groundstation._auth._identity import Credentials
from aws_sdk_groundstation._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_groundstation._auth._zapros_handler import AuthMiddleware
from aws_sdk_groundstation._resources.ground_station.agent import Agent
from aws_sdk_groundstation._resources.ground_station.config import Config
from aws_sdk_groundstation._resources.ground_station.contact import Contact
from aws_sdk_groundstation._resources.ground_station.dataflow_endpoint_group import (
    DataflowEndpointGroup,
)
from aws_sdk_groundstation._resources.ground_station.dataflow_endpoint_group_v2 import (
    DataflowEndpointGroupV2,
)
from aws_sdk_groundstation._resources.ground_station.ephemeris import Ephemeris
from aws_sdk_groundstation._resources.ground_station.ground_station_resource import (
    GroundStationResource,
)
from aws_sdk_groundstation._resources.ground_station.mission_profile import (
    MissionProfile,
)
from aws_sdk_groundstation._resources.ground_station.satellite import Satellite
from aws_sdk_groundstation._services._aws_config import aws_config
from aws_sdk_groundstation._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.any_arn
    import aws_sdk_groundstation.types.get_agent_task_response_url_request
    import aws_sdk_groundstation.types.get_agent_task_response_url_response
    import aws_sdk_groundstation.types.get_minute_usage_request
    import aws_sdk_groundstation.types.get_minute_usage_response
    import aws_sdk_groundstation.types.list_tags_for_resource_request
    import aws_sdk_groundstation.types.list_tags_for_resource_response
    import aws_sdk_groundstation.types.month
    import aws_sdk_groundstation.types.tag_keys
    import aws_sdk_groundstation.types.tag_resource_request
    import aws_sdk_groundstation.types.tag_resource_response
    import aws_sdk_groundstation.types.tags_map
    import aws_sdk_groundstation.types.untag_resource_request
    import aws_sdk_groundstation.types.untag_resource_response
    import aws_sdk_groundstation.types.uuid
    import aws_sdk_groundstation.types.year


class GroundStationClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class GroundStationClient:
    """A client for the ``GroundStation`` service.

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
        self._config = GroundStationClientConfig(
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
        self.agent = Agent(self)
        self.config = Config(self)
        self.contact = Contact(self)
        self.dataflow_endpoint_group = DataflowEndpointGroup(self)
        self.dataflow_endpoint_group_v2 = DataflowEndpointGroupV2(self)
        self.ephemeris = Ephemeris(self)
        self.ground_station_resource = GroundStationResource(self)
        self.mission_profile = MissionProfile(self)
        self.satellite = Satellite(self)

    def operation_options(
        self, config_overrides: Optional[GroundStationClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: GroundStationClientConfig = config_overrides or {}
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

    def get_agent_task_response_url(
        self,
        agent_id: "aws_sdk_groundstation.types.uuid.Uuid",
        task_id: "aws_sdk_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.get_agent_task_response_url_response.GetAgentTaskResponseUrlResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Gets a presigned URL for uploading agent task response logs.</p>

        Args:
            agent_id: <p>UUID of agent requesting the response URL.</p>
            task_id: <p>GUID of the agent task for which the response URL is being requested.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.get_agent_task_response_url_request.GetAgentTaskResponseUrlRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.get_agent_task_response_url_response.GetAgentTaskResponseUrlResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.get_agent_task_response_url

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.get_agent_task_response_url.get_agent_task_response_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.get_agent_task_response_url_request.GetAgentTaskResponseUrlRequest = {}  # type: ignore[typeddict-item]
        input_["agent_id"] = agent_id
        input_["task_id"] = task_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_minute_usage(
        self,
        month: "aws_sdk_groundstation.types.month.Month",
        year: "aws_sdk_groundstation.types.year.Year",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.get_minute_usage_response.GetMinuteUsageResponse":
        """<p>Returns the number of reserved minutes used by account.</p>

        Args:
            month: <p>The month being requested, with a value of 1-12.</p>
            year: <p>The year being requested, in the format of YYYY.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.get_minute_usage_request.GetMinuteUsageRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.get_minute_usage_response.GetMinuteUsageResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.get_minute_usage

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.get_minute_usage.get_minute_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.get_minute_usage_request.GetMinuteUsageRequest = {}  # type: ignore[typeddict-item]
        input_["month"] = month
        input_["year"] = year

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_groundstation.types.any_arn.AnyArn",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a specified resource.</p>

        Args:
            resource_arn: <p>ARN of a resource.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.list_tags_for_resource

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_groundstation.types.any_arn.AnyArn",
        tags: "aws_sdk_groundstation.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns a tag to a resource.</p>

        Args:
            resource_arn: <p>ARN of a resource tag.</p>
            tags: <p>Tags assigned to a resource.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.tag_resource

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_groundstation.types.any_arn.AnyArn",
        tag_keys: "aws_sdk_groundstation.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "aws_sdk_groundstation.types.untag_resource_response.UntagResourceResponse":
        """<p>Deassigns a resource tag.</p>

        Args:
            resource_arn: <p>ARN of a resource.</p>
            tag_keys: <p>Keys of a resource tag.</p>

        Raises:
            aws_sdk_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            aws_sdk_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            aws_sdk_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            aws_sdk_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_groundstation.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_groundstation.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_groundstation._operations.ground_station.untag_resource

            output, http_response = (
                aws_sdk_groundstation._operations.ground_station.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_groundstation.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
