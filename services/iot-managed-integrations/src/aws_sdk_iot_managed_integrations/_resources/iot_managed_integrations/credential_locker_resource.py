from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_iot_managed_integrations._auth._signers
import aws_sdk_iot_managed_integrations._auth._sigv4
from aws_sdk_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.client_token
    import aws_sdk_iot_managed_integrations.types.create_credential_locker_request
    import aws_sdk_iot_managed_integrations.types.create_credential_locker_response
    import aws_sdk_iot_managed_integrations.types.credential_locker_id
    import aws_sdk_iot_managed_integrations.types.credential_locker_name
    import aws_sdk_iot_managed_integrations.types.credential_locker_summary
    import aws_sdk_iot_managed_integrations.types.delete_credential_locker_request
    import aws_sdk_iot_managed_integrations.types.get_credential_locker_request
    import aws_sdk_iot_managed_integrations.types.get_credential_locker_response
    import aws_sdk_iot_managed_integrations.types.list_credential_lockers_request
    import aws_sdk_iot_managed_integrations.types.list_credential_lockers_response
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.tags_map
    from aws_sdk_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from aws_sdk_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class CredentialLockerResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.credential_locker_name.CredentialLockerName"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_credential_locker_response.CreateCredentialLockerResponse":
        """<p>Create a credential locker.</p> <note> <p>This operation will not trigger the creation of all the manufacturing resources.</p> </note>

        Args:
            name: <p>The name of the credential locker.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the credential locker.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_credential_locker_response.CreateCredentialLockerResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_credential_locker

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_credential_locker.create_credential_locker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.credential_locker_id.CredentialLockerId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse":
        """<p>Get information on an existing credential locker</p>

        Args:
            identifier: <p>The identifier of the credential locker.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.get_credential_locker_request.GetCredentialLockerRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_credential_locker

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_credential_locker.get_credential_locker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_credential_locker_request.GetCredentialLockerRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.credential_locker_id.CredentialLockerId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a credential locker. </p> <note> <p>This operation can't be undone and any existing device won't be able to use IoT managed integrations.</p> </note>

        Args:
            identifier: <p>The identifier of the credential locker.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.delete_credential_locker_request.DeleteCredentialLockerRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_credential_locker

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_credential_locker.delete_credential_locker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_credential_locker_request.DeleteCredentialLockerRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse":
        """<p>List information on an existing credential locker.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_iot_managed_integrations.types.list_credential_lockers_request.ListCredentialLockersRequest]",
        ) -> OperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_credential_lockers

            output, http_response = (
                aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_credential_lockers.list_credential_lockers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_credential_lockers_request.ListCredentialLockersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCredentialLockerResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "aws_sdk_iot_managed_integrations.types.credential_locker_name.CredentialLockerName"
        ] = None,
        client_token: Optional[
            "aws_sdk_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.create_credential_locker_response.CreateCredentialLockerResponse":
        """<p>Create a credential locker.</p> <note> <p>This operation will not trigger the creation of all the manufacturing resources.</p> </note>

        Args:
            name: <p>The name of the credential locker.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the credential locker.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.create_credential_locker_response.CreateCredentialLockerResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_credential_locker

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.create_credential_locker.async_create_credential_locker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.credential_locker_id.CredentialLockerId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse":
        """<p>Get information on an existing credential locker</p>

        Args:
            identifier: <p>The identifier of the credential locker.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.get_credential_locker_request.GetCredentialLockerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_credential_locker

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.get_credential_locker.async_get_credential_locker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.get_credential_locker_request.GetCredentialLockerRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identifier: "aws_sdk_iot_managed_integrations.types.credential_locker_id.CredentialLockerId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a credential locker. </p> <note> <p>This operation can't be undone and any existing device won't be able to use IoT managed integrations.</p> </note>

        Args:
            identifier: <p>The identifier of the credential locker.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.delete_credential_locker_request.DeleteCredentialLockerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_credential_locker

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.delete_credential_locker.async_delete_credential_locker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.delete_credential_locker_request.DeleteCredentialLockerRequest = {}  # type: ignore[typeddict-item]
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse":
        """<p>List information on an existing credential locker.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_iot_managed_integrations.types.list_credential_lockers_request.ListCredentialLockersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse"
        ]:
            import aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_credential_lockers

            (
                output,
                http_response,
            ) = await aws_sdk_iot_managed_integrations._operations.iot_managed_integrations.list_credential_lockers.async_list_credential_lockers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_iot_managed_integrations.types.list_credential_lockers_request.ListCredentialLockersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
