from __future__ import annotations

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
    import aws_sdk_ssm_guiconnect.types.connection_recording_preferences
    import aws_sdk_ssm_guiconnect.types.update_connection_recording_preferences_request
    import aws_sdk_ssm_guiconnect.types.update_connection_recording_preferences_response
    from aws_sdk_ssm_guiconnect._services.async_ssm_gui_connect import (
        AsyncSSMGuiConnectClient,
        AsyncSSMGuiConnectClientConfig,
    )
    from aws_sdk_ssm_guiconnect._services.ssm_gui_connect import (
        SSMGuiConnectClient,
        SSMGuiConnectClientConfig,
    )


class RecordingPreferences:
    def __init__(self, service: SSMGuiConnectClient) -> None:
        self._service = service

    def create(
        self,
        connection_recording_preferences: "aws_sdk_ssm_guiconnect.types.connection_recording_preferences.ConnectionRecordingPreferences",
        *,
        config_overrides: Optional[SSMGuiConnectClientConfig] = None,
        client_token: Optional[
            "aws_sdk_ssm_guiconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_ssm_guiconnect.types.update_connection_recording_preferences_response.UpdateConnectionRecordingPreferencesResponse":
        """<p>Updates the preferences for recording RDP connections.</p>

        Args:
            connection_recording_preferences: <p>The set of preferences used for recording RDP connections in the requesting Amazon Web Services account and Amazon Web Services Region. This includes details such as which S3 bucket recordings are stored in.</p>
            client_token: <p>User-provided idempotency token.</p>

        Raises:
            aws_sdk_ssm_guiconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_ssm_guiconnect.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            aws_sdk_ssm_guiconnect.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_ssm_guiconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            aws_sdk_ssm_guiconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota.</p>
            aws_sdk_ssm_guiconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_ssm_guiconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_ssm_guiconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Updates the connection recording preferences for the account

            >>> client.create(connection_recording_preferences={'RecordingDestinations': {'S3Buckets': [{'BucketOwner': '123456789012', 'BucketName': 'sample-connection-recording-bucket'}]}, 'KMSKeyArn': 'arn:aws:kms:region:account_id:key/sample_key_id'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ssm_guiconnect.types.update_connection_recording_preferences_request.UpdateConnectionRecordingPreferencesRequest]",
        ) -> OperationResponse[
            "aws_sdk_ssm_guiconnect.types.update_connection_recording_preferences_response.UpdateConnectionRecordingPreferencesResponse"
        ]:
            import aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.update_connection_recording_preferences

            output, http_response = (
                aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.update_connection_recording_preferences.update_connection_recording_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ssm_guiconnect.types.update_connection_recording_preferences_request.UpdateConnectionRecordingPreferencesRequest = {}  # type: ignore[typeddict-item]
        input_["connection_recording_preferences"] = connection_recording_preferences
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRecordingPreferences:
    def __init__(self, service: AsyncSSMGuiConnectClient) -> None:
        self._service = service

    async def create(
        self,
        connection_recording_preferences: "aws_sdk_ssm_guiconnect.types.connection_recording_preferences.ConnectionRecordingPreferences",
        *,
        config_overrides: Optional[AsyncSSMGuiConnectClientConfig] = None,
        client_token: Optional[
            "aws_sdk_ssm_guiconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_ssm_guiconnect.types.update_connection_recording_preferences_response.UpdateConnectionRecordingPreferencesResponse":
        """<p>Updates the preferences for recording RDP connections.</p>

        Args:
            connection_recording_preferences: <p>The set of preferences used for recording RDP connections in the requesting Amazon Web Services account and Amazon Web Services Region. This includes details such as which S3 bucket recordings are stored in.</p>
            client_token: <p>User-provided idempotency token.</p>

        Raises:
            aws_sdk_ssm_guiconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_ssm_guiconnect.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            aws_sdk_ssm_guiconnect.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            aws_sdk_ssm_guiconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            aws_sdk_ssm_guiconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota.</p>
            aws_sdk_ssm_guiconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_ssm_guiconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            aws_sdk_ssm_guiconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Updates the connection recording preferences for the account

            >>> await client.create(connection_recording_preferences={'RecordingDestinations': {'S3Buckets': [{'BucketOwner': '123456789012', 'BucketName': 'sample-connection-recording-bucket'}]}, 'KMSKeyArn': 'arn:aws:kms:region:account_id:key/sample_key_id'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_ssm_guiconnect.types.update_connection_recording_preferences_request.UpdateConnectionRecordingPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_ssm_guiconnect.types.update_connection_recording_preferences_response.UpdateConnectionRecordingPreferencesResponse"
        ]:
            import aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.update_connection_recording_preferences

            (
                output,
                http_response,
            ) = await aws_sdk_ssm_guiconnect._operations.ssm_gui_connect.update_connection_recording_preferences.async_update_connection_recording_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_ssm_guiconnect.types.update_connection_recording_preferences_request.UpdateConnectionRecordingPreferencesRequest = {}  # type: ignore[typeddict-item]
        input_["connection_recording_preferences"] = connection_recording_preferences
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
