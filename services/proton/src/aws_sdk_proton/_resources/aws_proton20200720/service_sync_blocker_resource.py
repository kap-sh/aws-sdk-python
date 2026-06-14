from typing import TYPE_CHECKING, Optional

from aws_sdk_proton._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_proton.types.get_service_sync_blocker_summary_input
    import aws_sdk_proton.types.get_service_sync_blocker_summary_output
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.update_service_sync_blocker_input
    import aws_sdk_proton.types.update_service_sync_blocker_output
    from aws_sdk_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig


class ServiceSyncBlockerResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def read(
        self,
        service_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        service_instance_name: Optional[
            "aws_sdk_proton.types.resource_name.ResourceName"
        ] = None,
    ) -> "aws_sdk_proton.types.get_service_sync_blocker_summary_output.GetServiceSyncBlockerSummaryOutput":
        """<p>Get detailed data for the service sync blocker summary.</p>

        Args:
            service_name: <p>The name of the service that you want to get the service sync blocker summary for. If given only the service name, all instances are blocked.</p>
            service_instance_name: <p>The name of the service instance that you want to get the service sync blocker summary for. If given bothe the instance name and the service name, only the instance is blocked.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.get_service_sync_blocker_summary_input.GetServiceSyncBlockerSummaryInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.get_service_sync_blocker_summary_output.GetServiceSyncBlockerSummaryOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_service_sync_blocker_summary

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.get_service_sync_blocker_summary.get_service_sync_blocker_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.get_service_sync_blocker_summary_input.GetServiceSyncBlockerSummaryInput = {}  # type: ignore[typeddict-item]
        input_["service_name"] = service_name
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        id: str,
        resolved_reason: str,
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.update_service_sync_blocker_output.UpdateServiceSyncBlockerOutput":
        """<p>Update the service sync blocker by resolving it.</p>

        Args:
            id: <p>The ID of the service sync blocker.</p>
            resolved_reason: <p>The reason the service sync blocker was resolved.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.update_service_sync_blocker_input.UpdateServiceSyncBlockerInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.update_service_sync_blocker_output.UpdateServiceSyncBlockerOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service_sync_blocker

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.update_service_sync_blocker.update_service_sync_blocker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.update_service_sync_blocker_input.UpdateServiceSyncBlockerInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["resolved_reason"] = resolved_reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncServiceSyncBlockerResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def read(
        self,
        service_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        service_instance_name: Optional[
            "aws_sdk_proton.types.resource_name.ResourceName"
        ] = None,
    ) -> "aws_sdk_proton.types.get_service_sync_blocker_summary_output.GetServiceSyncBlockerSummaryOutput":
        """<p>Get detailed data for the service sync blocker summary.</p>

        Args:
            service_name: <p>The name of the service that you want to get the service sync blocker summary for. If given only the service name, all instances are blocked.</p>
            service_instance_name: <p>The name of the service instance that you want to get the service sync blocker summary for. If given bothe the instance name and the service name, only the instance is blocked.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.get_service_sync_blocker_summary_input.GetServiceSyncBlockerSummaryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.get_service_sync_blocker_summary_output.GetServiceSyncBlockerSummaryOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_service_sync_blocker_summary

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.get_service_sync_blocker_summary.async_get_service_sync_blocker_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.get_service_sync_blocker_summary_input.GetServiceSyncBlockerSummaryInput = {}  # type: ignore[typeddict-item]
        input_["service_name"] = service_name
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        id: str,
        resolved_reason: str,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.update_service_sync_blocker_output.UpdateServiceSyncBlockerOutput":
        """<p>Update the service sync blocker by resolving it.</p>

        Args:
            id: <p>The ID of the service sync blocker.</p>
            resolved_reason: <p>The reason the service sync blocker was resolved.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.update_service_sync_blocker_input.UpdateServiceSyncBlockerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.update_service_sync_blocker_output.UpdateServiceSyncBlockerOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.update_service_sync_blocker

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.update_service_sync_blocker.async_update_service_sync_blocker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.update_service_sync_blocker_input.UpdateServiceSyncBlockerInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        input_["resolved_reason"] = resolved_reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
