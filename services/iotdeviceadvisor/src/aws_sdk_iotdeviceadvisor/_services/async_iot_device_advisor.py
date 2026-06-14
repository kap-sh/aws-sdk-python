"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#IotSenateService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_iotdeviceadvisor._auth._signers
import aws_sdk_iotdeviceadvisor._auth._sigv4
from aws_sdk_iotdeviceadvisor._auth._identity import Credentials
from aws_sdk_iotdeviceadvisor._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_iotdeviceadvisor._auth._zapros_handler import AuthMiddleware
from aws_sdk_iotdeviceadvisor._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.amazon_resource_name
    import aws_sdk_iotdeviceadvisor.types.authentication_method
    import aws_sdk_iotdeviceadvisor.types.client_token
    import aws_sdk_iotdeviceadvisor.types.create_suite_definition_request
    import aws_sdk_iotdeviceadvisor.types.create_suite_definition_response
    import aws_sdk_iotdeviceadvisor.types.delete_suite_definition_request
    import aws_sdk_iotdeviceadvisor.types.delete_suite_definition_response
    import aws_sdk_iotdeviceadvisor.types.get_endpoint_request
    import aws_sdk_iotdeviceadvisor.types.get_endpoint_response
    import aws_sdk_iotdeviceadvisor.types.get_suite_definition_request
    import aws_sdk_iotdeviceadvisor.types.get_suite_definition_response
    import aws_sdk_iotdeviceadvisor.types.get_suite_run_report_request
    import aws_sdk_iotdeviceadvisor.types.get_suite_run_report_response
    import aws_sdk_iotdeviceadvisor.types.get_suite_run_request
    import aws_sdk_iotdeviceadvisor.types.get_suite_run_response
    import aws_sdk_iotdeviceadvisor.types.list_suite_definitions_request
    import aws_sdk_iotdeviceadvisor.types.list_suite_definitions_response
    import aws_sdk_iotdeviceadvisor.types.list_suite_runs_request
    import aws_sdk_iotdeviceadvisor.types.list_suite_runs_response
    import aws_sdk_iotdeviceadvisor.types.list_tags_for_resource_request
    import aws_sdk_iotdeviceadvisor.types.list_tags_for_resource_response
    import aws_sdk_iotdeviceadvisor.types.max_results
    import aws_sdk_iotdeviceadvisor.types.start_suite_run_request
    import aws_sdk_iotdeviceadvisor.types.start_suite_run_response
    import aws_sdk_iotdeviceadvisor.types.stop_suite_run_request
    import aws_sdk_iotdeviceadvisor.types.stop_suite_run_response
    import aws_sdk_iotdeviceadvisor.types.suite_definition_configuration
    import aws_sdk_iotdeviceadvisor.types.suite_definition_version
    import aws_sdk_iotdeviceadvisor.types.suite_run_configuration
    import aws_sdk_iotdeviceadvisor.types.tag_key_list
    import aws_sdk_iotdeviceadvisor.types.tag_map
    import aws_sdk_iotdeviceadvisor.types.tag_resource_request
    import aws_sdk_iotdeviceadvisor.types.tag_resource_response
    import aws_sdk_iotdeviceadvisor.types.token
    import aws_sdk_iotdeviceadvisor.types.untag_resource_request
    import aws_sdk_iotdeviceadvisor.types.untag_resource_response
    import aws_sdk_iotdeviceadvisor.types.update_suite_definition_request
    import aws_sdk_iotdeviceadvisor.types.update_suite_definition_response
    import aws_sdk_iotdeviceadvisor.types.uuid


class AsyncIotDeviceAdvisorClientConfig(TypedDict, total=False):
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


class AsyncIotDeviceAdvisorClient:
    """A client for the ``IotDeviceAdvisor`` service.

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
        self._config = AsyncIotDeviceAdvisorClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIotDeviceAdvisorClientConfig = config_overrides or {}
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

    async def create_suite_definition(
        self,
        suite_definition_configuration: "aws_sdk_iotdeviceadvisor.types.suite_definition_configuration.SuiteDefinitionConfiguration",
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
        tags: Optional["aws_sdk_iotdeviceadvisor.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_iotdeviceadvisor.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.create_suite_definition_response.CreateSuiteDefinitionResponse":
        """<p>Creates a Device Advisor test suite.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">CreateSuiteDefinition</a> action.</p>

        Args:
            suite_definition_configuration: <p>Creates a Device Advisor test suite with suite definition configuration.</p>
            tags: <p>The tags to be attached to the suite definition.</p>
            client_token: <p>The client token for the test suite definition creation. This token is used for tracking test suite definition creation using retries and obtaining its status. This parameter is optional.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.create_suite_definition_request.CreateSuiteDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.create_suite_definition_response.CreateSuiteDefinitionResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.create_suite_definition

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.create_suite_definition.async_create_suite_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.create_suite_definition_request.CreateSuiteDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["suite_definition_configuration"] = suite_definition_configuration
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_suite_definition(
        self,
        suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.delete_suite_definition_response.DeleteSuiteDefinitionResponse":
        """<p>Deletes a Device Advisor test suite.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">DeleteSuiteDefinition</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.delete_suite_definition_request.DeleteSuiteDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.delete_suite_definition_response.DeleteSuiteDefinitionResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.delete_suite_definition

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.delete_suite_definition.async_delete_suite_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.delete_suite_definition_request.DeleteSuiteDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["suite_definition_id"] = suite_definition_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_endpoint(
        self,
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
        thing_arn: Optional[
            "aws_sdk_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        certificate_arn: Optional[
            "aws_sdk_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        device_role_arn: Optional[
            "aws_sdk_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        authentication_method: Optional[
            "aws_sdk_iotdeviceadvisor.types.authentication_method.AuthenticationMethod"
        ] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.get_endpoint_response.GetEndpointResponse":
        """<p>Gets information about an Device Advisor endpoint.</p>

        Args:
            thing_arn: <p>The thing ARN of the device. This is an optional parameter.</p>
            certificate_arn: <p>The certificate ARN of the device. This is an optional parameter.</p>
            device_role_arn: <p>The device role ARN of the device. This is an optional parameter.</p>
            authentication_method: <p>The authentication method used during the device connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.get_endpoint_request.GetEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.get_endpoint_response.GetEndpointResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.get_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.get_endpoint.async_get_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.get_endpoint_request.GetEndpointRequest = {}  # type: ignore[typeddict-item]
        if thing_arn is not None:
            input_["thing_arn"] = thing_arn
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if device_role_arn is not None:
            input_["device_role_arn"] = device_role_arn
        if authentication_method is not None:
            input_["authentication_method"] = authentication_method

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_suite_definition(
        self,
        suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
        suite_definition_version: Optional[
            "aws_sdk_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
        ] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.get_suite_definition_response.GetSuiteDefinitionResponse":
        """<p>Gets information about a Device Advisor test suite.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">GetSuiteDefinition</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite to get.</p>
            suite_definition_version: <p>Suite definition version of the test suite to get.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.get_suite_definition_request.GetSuiteDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.get_suite_definition_response.GetSuiteDefinitionResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.get_suite_definition

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.get_suite_definition.async_get_suite_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.get_suite_definition_request.GetSuiteDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["suite_definition_id"] = suite_definition_id
        if suite_definition_version is not None:
            input_["suite_definition_version"] = suite_definition_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_suite_run(
        self,
        suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID",
        suite_run_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.get_suite_run_response.GetSuiteRunResponse":
        """<p>Gets information about a Device Advisor test suite run.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">GetSuiteRun</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID for the test suite run.</p>
            suite_run_id: <p>Suite run ID for the test suite run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.get_suite_run_request.GetSuiteRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.get_suite_run_response.GetSuiteRunResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.get_suite_run

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.get_suite_run.async_get_suite_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.get_suite_run_request.GetSuiteRunRequest = {}  # type: ignore[typeddict-item]
        input_["suite_definition_id"] = suite_definition_id
        input_["suite_run_id"] = suite_run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_suite_run_report(
        self,
        suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID",
        suite_run_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.get_suite_run_report_response.GetSuiteRunReportResponse":
        """<p>Gets a report download link for a successful Device Advisor qualifying test suite run.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">GetSuiteRunReport</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite.</p>
            suite_run_id: <p>Suite run ID of the test suite run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.get_suite_run_report_request.GetSuiteRunReportRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.get_suite_run_report_response.GetSuiteRunReportResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.get_suite_run_report

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.get_suite_run_report.async_get_suite_run_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.get_suite_run_report_request.GetSuiteRunReportRequest = {}  # type: ignore[typeddict-item]
        input_["suite_definition_id"] = suite_definition_id
        input_["suite_run_id"] = suite_run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_suite_definitions(
        self,
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_iotdeviceadvisor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iotdeviceadvisor.types.token.Token"] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.list_suite_definitions_response.ListSuiteDefinitionsResponse":
        """<p>Lists the Device Advisor test suites you have created.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">ListSuiteDefinitions</a> action.</p>

        Args:
            max_results: <p>The maximum number of results to return at once.</p>
            next_token: <p>A token used to get the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.list_suite_definitions_request.ListSuiteDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.list_suite_definitions_response.ListSuiteDefinitionsResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.list_suite_definitions

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.list_suite_definitions.async_list_suite_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.list_suite_definitions_request.ListSuiteDefinitionsRequest = {}  # type: ignore[typeddict-item]
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

    async def list_suite_runs(
        self,
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
        suite_definition_id: Optional[
            "aws_sdk_iotdeviceadvisor.types.uuid.UUID"
        ] = None,
        suite_definition_version: Optional[
            "aws_sdk_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
        ] = None,
        max_results: Optional[
            "aws_sdk_iotdeviceadvisor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_iotdeviceadvisor.types.token.Token"] = None,
    ) -> (
        "aws_sdk_iotdeviceadvisor.types.list_suite_runs_response.ListSuiteRunsResponse"
    ):
        """<p>Lists runs of the specified Device Advisor test suite. You can list all runs of the test suite, or the runs of a specific version of the test suite.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">ListSuiteRuns</a> action.</p>

        Args:
            suite_definition_id: <p>Lists the test suite runs of the specified test suite based on suite definition ID.</p>
            suite_definition_version: <p>Must be passed along with <code>suiteDefinitionId</code>. Lists the test suite runs of the specified test suite based on suite definition version.</p>
            max_results: <p>The maximum number of results to return at once.</p>
            next_token: <p>A token to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.list_suite_runs_request.ListSuiteRunsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.list_suite_runs_response.ListSuiteRunsResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.list_suite_runs

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.list_suite_runs.async_list_suite_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.list_suite_runs_request.ListSuiteRunsRequest = {}  # type: ignore[typeddict-item]
        if suite_definition_id is not None:
            input_["suite_definition_id"] = suite_definition_id
        if suite_definition_version is not None:
            input_["suite_definition_version"] = suite_definition_version
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags attached to an IoT Device Advisor resource.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">ListTagsForResource</a> action.</p>

        Args:
            resource_arn: <p>The resource ARN of the IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_suite_run(
        self,
        suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID",
        suite_run_configuration: "aws_sdk_iotdeviceadvisor.types.suite_run_configuration.SuiteRunConfiguration",
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
        suite_definition_version: Optional[
            "aws_sdk_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
        ] = None,
        tags: Optional["aws_sdk_iotdeviceadvisor.types.tag_map.TagMap"] = None,
    ) -> (
        "aws_sdk_iotdeviceadvisor.types.start_suite_run_response.StartSuiteRunResponse"
    ):
        """<p>Starts a Device Advisor test suite run.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">StartSuiteRun</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite.</p>
            suite_definition_version: <p>Suite definition version of the test suite.</p>
            suite_run_configuration: <p>Suite run configuration.</p>
            tags: <p>The tags to be attached to the suite run.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.start_suite_run_request.StartSuiteRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.start_suite_run_response.StartSuiteRunResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.start_suite_run

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.start_suite_run.async_start_suite_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.start_suite_run_request.StartSuiteRunRequest = {}  # type: ignore[typeddict-item]
        input_["suite_definition_id"] = suite_definition_id
        if suite_definition_version is not None:
            input_["suite_definition_version"] = suite_definition_version
        input_["suite_run_configuration"] = suite_run_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_suite_run(
        self,
        suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID",
        suite_run_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.stop_suite_run_response.StopSuiteRunResponse":
        """<p>Stops a Device Advisor test suite run that is currently running.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">StopSuiteRun</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite run to be stopped.</p>
            suite_run_id: <p>Suite run ID of the test suite run to be stopped.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.stop_suite_run_request.StopSuiteRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.stop_suite_run_response.StopSuiteRunResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.stop_suite_run

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.stop_suite_run.async_stop_suite_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.stop_suite_run_request.StopSuiteRunRequest = {}  # type: ignore[typeddict-item]
        input_["suite_definition_id"] = suite_definition_id
        input_["suite_run_id"] = suite_run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_iotdeviceadvisor.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.tag_resource_response.TagResourceResponse":
        """<p>Adds to and modifies existing tags of an IoT Device Advisor resource.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">TagResource</a> action.</p>

        Args:
            resource_arn: <p>The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.</p>
            tags: <p>The tags to be attached to the IoT Device Advisor resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_iotdeviceadvisor.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from an IoT Device Advisor resource.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">UntagResource</a> action.</p>

        Args:
            resource_arn: <p>The resource ARN of an IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.</p>
            tag_keys: <p>List of tag keys to remove from the IoT Device Advisor resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_suite_definition(
        self,
        suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID",
        suite_definition_configuration: "aws_sdk_iotdeviceadvisor.types.suite_definition_configuration.SuiteDefinitionConfiguration",
        *,
        config_overrides: Optional[AsyncIotDeviceAdvisorClientConfig] = None,
    ) -> "aws_sdk_iotdeviceadvisor.types.update_suite_definition_response.UpdateSuiteDefinitionResponse":
        """<p>Updates a Device Advisor test suite.</p> <p>Requires permission to access the <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\">UpdateSuiteDefinition</a> action.</p>

        Args:
            suite_definition_id: <p>Suite definition ID of the test suite to be updated.</p>
            suite_definition_configuration: <p>Updates a Device Advisor test suite with suite definition configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iotdeviceadvisor.types.update_suite_definition_request.UpdateSuiteDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iotdeviceadvisor.types.update_suite_definition_response.UpdateSuiteDefinitionResponse"
        ]:
            import aws_sdk_iotdeviceadvisor._operations.iot_senate_service.update_suite_definition

            (
                output,
                http_response,
            ) = await aws_sdk_iotdeviceadvisor._operations.iot_senate_service.update_suite_definition.async_update_suite_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_iotdeviceadvisor.types.update_suite_definition_request.UpdateSuiteDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["suite_definition_id"] = suite_definition_id
        input_["suite_definition_configuration"] = suite_definition_configuration

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
