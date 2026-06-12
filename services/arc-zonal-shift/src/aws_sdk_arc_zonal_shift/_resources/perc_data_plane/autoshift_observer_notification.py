from typing import TYPE_CHECKING, Optional

import aws_sdk_arc_zonal_shift._auth._signers
import aws_sdk_arc_zonal_shift._auth._sigv4
from aws_sdk_arc_zonal_shift._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status
    import aws_sdk_arc_zonal_shift.types.get_autoshift_observer_notification_status_request
    import aws_sdk_arc_zonal_shift.types.get_autoshift_observer_notification_status_response
    import aws_sdk_arc_zonal_shift.types.update_autoshift_observer_notification_status_request
    import aws_sdk_arc_zonal_shift.types.update_autoshift_observer_notification_status_response
    from aws_sdk_arc_zonal_shift._services.arc_zonal_shift import (
        ARCZonalShiftClient,
        ARCZonalShiftClientConfig,
    )
    from aws_sdk_arc_zonal_shift._services.async_arc_zonal_shift import (
        AsyncARCZonalShiftClient,
        AsyncARCZonalShiftClientConfig,
    )


class AutoshiftObserverNotification:
    def __init__(self, service: ARCZonalShiftClient) -> None:
        self._service = service

    def get_autoshift_observer_notification_status(
        self, *, config_overrides: Optional[ARCZonalShiftClientConfig] = None
    ) -> "aws_sdk_arc_zonal_shift.types.get_autoshift_observer_notification_status_response.GetAutoshiftObserverNotificationStatusResponse":
        """<p>Returns the status of the autoshift observer notification. Autoshift observer notifications notify you through Amazon EventBridge when there is an autoshift event for zonal autoshift. The status can be <code>ENABLED</code> or <code>DISABLED</code>. When <code>ENABLED</code>, a notification is sent when an autoshift is triggered. When <code>DISABLED</code>, notifications are not sent. </p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_arc_zonal_shift.types.get_autoshift_observer_notification_status_request.GetAutoshiftObserverNotificationStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_arc_zonal_shift.types.get_autoshift_observer_notification_status_response.GetAutoshiftObserverNotificationStatusResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.get_autoshift_observer_notification_status

            output, http_response = (
                aws_sdk_arc_zonal_shift._operations.perc_data_plane.get_autoshift_observer_notification_status.get_autoshift_observer_notification_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_arc_zonal_shift.types.get_autoshift_observer_notification_status_request.GetAutoshiftObserverNotificationStatusRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_autoshift_observer_notification_status(
        self,
        status: "aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status.AutoshiftObserverNotificationStatus",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.update_autoshift_observer_notification_status_response.UpdateAutoshiftObserverNotificationStatusResponse":
        """<p>Update the status of autoshift observer notification. Autoshift observer notification enables you to be notified, through Amazon EventBridge, when there is an autoshift event for zonal autoshift.</p> <p>If the status is <code>ENABLED</code>, ARC includes all autoshift events when you use the EventBridge pattern <code>Autoshift In Progress</code>. When the status is <code>DISABLED</code>, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html#ZAShiftNotification\"> Notifications for practice runs and autoshifts</a> in the Amazon Application Recovery Controller Developer Guide.</p>

        Args:
            status: <p>The status to set for autoshift observer notification. If the status is <code>ENABLED</code>, ARC includes all autoshift events when you use the Amazon EventBridge pattern <code>Autoshift In Progress</code>. When the status is <code>DISABLED</code>, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_arc_zonal_shift.types.update_autoshift_observer_notification_status_request.UpdateAutoshiftObserverNotificationStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_arc_zonal_shift.types.update_autoshift_observer_notification_status_response.UpdateAutoshiftObserverNotificationStatusResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_autoshift_observer_notification_status

            output, http_response = (
                aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_autoshift_observer_notification_status.update_autoshift_observer_notification_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_arc_zonal_shift.types.update_autoshift_observer_notification_status_request.UpdateAutoshiftObserverNotificationStatusRequest = {}  # type: ignore[typeddict-item]
        input["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAutoshiftObserverNotification:
    def __init__(self, service: AsyncARCZonalShiftClient) -> None:
        self._service = service

    async def get_autoshift_observer_notification_status(
        self, *, config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None
    ) -> "aws_sdk_arc_zonal_shift.types.get_autoshift_observer_notification_status_response.GetAutoshiftObserverNotificationStatusResponse":
        """<p>Returns the status of the autoshift observer notification. Autoshift observer notifications notify you through Amazon EventBridge when there is an autoshift event for zonal autoshift. The status can be <code>ENABLED</code> or <code>DISABLED</code>. When <code>ENABLED</code>, a notification is sent when an autoshift is triggered. When <code>DISABLED</code>, notifications are not sent. </p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_arc_zonal_shift.types.get_autoshift_observer_notification_status_request.GetAutoshiftObserverNotificationStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_arc_zonal_shift.types.get_autoshift_observer_notification_status_response.GetAutoshiftObserverNotificationStatusResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.get_autoshift_observer_notification_status

            (
                output,
                http_response,
            ) = await aws_sdk_arc_zonal_shift._operations.perc_data_plane.get_autoshift_observer_notification_status.async_get_autoshift_observer_notification_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_arc_zonal_shift.types.get_autoshift_observer_notification_status_request.GetAutoshiftObserverNotificationStatusRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_autoshift_observer_notification_status(
        self,
        status: "aws_sdk_arc_zonal_shift.types.autoshift_observer_notification_status.AutoshiftObserverNotificationStatus",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.update_autoshift_observer_notification_status_response.UpdateAutoshiftObserverNotificationStatusResponse":
        """<p>Update the status of autoshift observer notification. Autoshift observer notification enables you to be notified, through Amazon EventBridge, when there is an autoshift event for zonal autoshift.</p> <p>If the status is <code>ENABLED</code>, ARC includes all autoshift events when you use the EventBridge pattern <code>Autoshift In Progress</code>. When the status is <code>DISABLED</code>, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html#ZAShiftNotification\"> Notifications for practice runs and autoshifts</a> in the Amazon Application Recovery Controller Developer Guide.</p>

        Args:
            status: <p>The status to set for autoshift observer notification. If the status is <code>ENABLED</code>, ARC includes all autoshift events when you use the Amazon EventBridge pattern <code>Autoshift In Progress</code>. When the status is <code>DISABLED</code>, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_arc_zonal_shift.types.update_autoshift_observer_notification_status_request.UpdateAutoshiftObserverNotificationStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_arc_zonal_shift.types.update_autoshift_observer_notification_status_response.UpdateAutoshiftObserverNotificationStatusResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_autoshift_observer_notification_status

            (
                output,
                http_response,
            ) = await aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_autoshift_observer_notification_status.async_update_autoshift_observer_notification_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_arc_zonal_shift.types.update_autoshift_observer_notification_status_request.UpdateAutoshiftObserverNotificationStatusRequest = {}  # type: ignore[typeddict-item]
        input["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
