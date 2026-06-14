from typing import TYPE_CHECKING, Optional

import aws_sdk_ssm_guiconnect._auth._signers
import aws_sdk_ssm_guiconnect._auth._sigv4
from aws_sdk_ssm_guiconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_ssm_guiconnect.types.client_token
    import aws_sdk_ssm_guiconnect.types.delete_connection_recording_preferences_request
    import aws_sdk_ssm_guiconnect.types.delete_connection_recording_preferences_response
    import aws_sdk_ssm_guiconnect.types.get_connection_recording_preferences_response
    from aws_sdk_ssm_guiconnect._services.async_ssm_gui_connect import (
        AsyncSSMGuiConnectClient,
        AsyncSSMGuiConnectClientConfig,
    )
    from aws_sdk_ssm_guiconnect._services.ssm_gui_connect import (
        SSMGuiConnectClient,
        SSMGuiConnectClientConfig,
    )


class ModifyRecordingPreferences:
    def __init__(self, service: SSMGuiConnectClient) -> None:
        self._service = service

    def read(
        self, *, config_overrides: Optional[SSMGuiConnectClientConfig] = None
    ) -> "aws_sdk_ssm_guiconnect.types.get_connection_recording_preferences_response.GetConnectionRecordingPreferencesResponse":
        """<p>Returns the preferences specified for recording RDP connections in the requesting Amazon Web Services account and Amazon Web Services Region.</p>

        Examples:
            Retrieves the connection recording preferences for the account

            >>> client.read()
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "aws_sdk_ssm_guiconnect.types.get_connection_recording_preferences_response.GetConnectionRecordingPreferencesResponse"
        ]:
            import aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences

            output, http_response = (
                aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences.get_connection_recording_preferences(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        *,
        config_overrides: Optional[SSMGuiConnectClientConfig] = None,
        client_token: Optional[
            "aws_sdk_ssm_guiconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_ssm_guiconnect.types.delete_connection_recording_preferences_response.DeleteConnectionRecordingPreferencesResponse":
        """<p>Deletes the preferences for recording RDP connections.</p>

        Args:
            client_token: <p>User-provided idempotency token.</p>

        Examples:
            Delete the connection recording preferences for the account

            >>> client.delete()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest]",
        ) -> OperationResponse[
            "aws_sdk_ssm_guiconnect.types.delete_connection_recording_preferences_response.DeleteConnectionRecordingPreferencesResponse"
        ]:
            import aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences

            output, http_response = (
                aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences.delete_connection_recording_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncModifyRecordingPreferences:
    def __init__(self, service: AsyncSSMGuiConnectClient) -> None:
        self._service = service

    async def read(
        self, *, config_overrides: Optional[AsyncSSMGuiConnectClientConfig] = None
    ) -> "aws_sdk_ssm_guiconnect.types.get_connection_recording_preferences_response.GetConnectionRecordingPreferencesResponse":
        """<p>Returns the preferences specified for recording RDP connections in the requesting Amazon Web Services account and Amazon Web Services Region.</p>

        Examples:
            Retrieves the connection recording preferences for the account

            >>> await client.read()
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ssm_guiconnect.types.get_connection_recording_preferences_response.GetConnectionRecordingPreferencesResponse"
        ]:
            import aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences

            (
                output,
                http_response,
            ) = await aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences.async_get_connection_recording_preferences(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        *,
        config_overrides: Optional[AsyncSSMGuiConnectClientConfig] = None,
        client_token: Optional[
            "aws_sdk_ssm_guiconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_ssm_guiconnect.types.delete_connection_recording_preferences_response.DeleteConnectionRecordingPreferencesResponse":
        """<p>Deletes the preferences for recording RDP connections.</p>

        Args:
            client_token: <p>User-provided idempotency token.</p>

        Examples:
            Delete the connection recording preferences for the account

            >>> await client.delete()
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ssm_guiconnect.types.delete_connection_recording_preferences_response.DeleteConnectionRecordingPreferencesResponse"
        ]:
            import aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences

            (
                output,
                http_response,
            ) = await aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences.async_delete_connection_recording_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
