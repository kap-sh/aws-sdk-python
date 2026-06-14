from typing import Optional, TYPE_CHECKING
from aws_sdk_appconfigdata._services.async_app_config_data import ensure_async_iterator
from aws_sdk_appconfigdata._services.app_config_data import ensure_sync_iterator
import datetime
from aws_sdk_appconfigdata._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_appconfigdata._auth._signers
import aws_sdk_appconfigdata._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_appconfigdata._services.app_config_data import AppConfigDataClient, AppConfigDataClientConfig
    from aws_sdk_appconfigdata._services.async_app_config_data import AsyncAppConfigDataClient, AsyncAppConfigDataClientConfig
    import aws_sdk_appconfigdata.types.identifier
    import aws_sdk_appconfigdata.types.optional_poll_seconds
    import aws_sdk_appconfigdata.types.start_configuration_session_request
    import aws_sdk_appconfigdata.types.start_configuration_session_response

class ConfigurationSession:
    def __init__(self, service: AppConfigDataClient) -> None:
        self._service = service
    def create(self, application_identifier: "aws_sdk_appconfigdata.types.identifier.Identifier", environment_identifier: "aws_sdk_appconfigdata.types.identifier.Identifier", configuration_profile_identifier: "aws_sdk_appconfigdata.types.identifier.Identifier", *, config_overrides: Optional[AppConfigDataClientConfig] = None, required_minimum_poll_interval_in_seconds: Optional["aws_sdk_appconfigdata.types.optional_poll_seconds.OptionalPollSeconds"] = None) -> "aws_sdk_appconfigdata.types.start_configuration_session_response.StartConfigurationSessionResponse":
        """<p>Starts a configuration session used to retrieve a deployed configuration. For more information about this API action and to view example CLI commands that show how to use it with the <a>GetLatestConfiguration</a> API action, see <a href=\"http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration\">Retrieving the configuration</a> in the <i>AppConfig User Guide</i>. </p>

        Args:
            application_identifier: <p>The application ID or the application name.</p>
            environment_identifier: <p>The environment ID or the environment name.</p>
            configuration_profile_identifier: <p>The configuration profile ID or the configuration profile name.</p>
            required_minimum_poll_interval_in_seconds: <p>Sets a constraint on a session. If you specify a value of, for example, 60 seconds, then the client that established the session can't call <a>GetLatestConfiguration</a> more frequently than every 60 seconds.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_appconfigdata.types.start_configuration_session_request.StartConfigurationSessionRequest]') -> OperationResponse["aws_sdk_appconfigdata.types.start_configuration_session_response.StartConfigurationSessionResponse"]:
            import aws_sdk_appconfigdata._operations.app_config_data.start_configuration_session
            output, http_response = aws_sdk_appconfigdata._operations.app_config_data.start_configuration_session.start_configuration_session(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_appconfigdata.types.start_configuration_session_request.StartConfigurationSessionRequest = {}  # type: ignore[typeddict-item]
        input_["application_identifier"] = application_identifier
        input_["environment_identifier"] = environment_identifier
        input_["configuration_profile_identifier"] = configuration_profile_identifier
        if required_minimum_poll_interval_in_seconds is not None:
            input_["required_minimum_poll_interval_in_seconds"] = required_minimum_poll_interval_in_seconds

        response = execute_pipeline(OperationRequest(input=input_, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncConfigurationSession:
    def __init__(self, service: AsyncAppConfigDataClient) -> None:
        self._service = service
    async def create(self, application_identifier: "aws_sdk_appconfigdata.types.identifier.Identifier", environment_identifier: "aws_sdk_appconfigdata.types.identifier.Identifier", configuration_profile_identifier: "aws_sdk_appconfigdata.types.identifier.Identifier", *, config_overrides: Optional[AsyncAppConfigDataClientConfig] = None, required_minimum_poll_interval_in_seconds: Optional["aws_sdk_appconfigdata.types.optional_poll_seconds.OptionalPollSeconds"] = None) -> "aws_sdk_appconfigdata.types.start_configuration_session_response.StartConfigurationSessionResponse":
        """<p>Starts a configuration session used to retrieve a deployed configuration. For more information about this API action and to view example CLI commands that show how to use it with the <a>GetLatestConfiguration</a> API action, see <a href=\"http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration\">Retrieving the configuration</a> in the <i>AppConfig User Guide</i>. </p>

        Args:
            application_identifier: <p>The application ID or the application name.</p>
            environment_identifier: <p>The environment ID or the environment name.</p>
            configuration_profile_identifier: <p>The configuration profile ID or the configuration profile name.</p>
            required_minimum_poll_interval_in_seconds: <p>Sets a constraint on a session. If you specify a value of, for example, 60 seconds, then the client that established the session can't call <a>GetLatestConfiguration</a> more frequently than every 60 seconds.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_appconfigdata.types.start_configuration_session_request.StartConfigurationSessionRequest]') -> AsyncOperationResponse["aws_sdk_appconfigdata.types.start_configuration_session_response.StartConfigurationSessionResponse"]:
            import aws_sdk_appconfigdata._operations.app_config_data.start_configuration_session
            output, http_response = await aws_sdk_appconfigdata._operations.app_config_data.start_configuration_session.async_start_configuration_session(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_appconfigdata.types.start_configuration_session_request.StartConfigurationSessionRequest = {}  # type: ignore[typeddict-item]
        input_["application_identifier"] = application_identifier
        input_["environment_identifier"] = environment_identifier
        input_["configuration_profile_identifier"] = configuration_profile_identifier
        if required_minimum_poll_interval_in_seconds is not None:
            input_["required_minimum_poll_interval_in_seconds"] = required_minimum_poll_interval_in_seconds

        response = await aexecute_pipeline(AsyncOperationRequest(input=input_, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output