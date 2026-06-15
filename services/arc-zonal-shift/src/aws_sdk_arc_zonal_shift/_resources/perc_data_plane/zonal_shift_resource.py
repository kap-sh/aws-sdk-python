from __future__ import annotations

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
    import aws_sdk_arc_zonal_shift.types.cancel_practice_run_request
    import aws_sdk_arc_zonal_shift.types.cancel_practice_run_response
    import aws_sdk_arc_zonal_shift.types.cancel_zonal_shift_request
    import aws_sdk_arc_zonal_shift.types.expires_in
    import aws_sdk_arc_zonal_shift.types.update_zonal_shift_request
    import aws_sdk_arc_zonal_shift.types.zonal_shift
    import aws_sdk_arc_zonal_shift.types.zonal_shift_comment
    import aws_sdk_arc_zonal_shift.types.zonal_shift_id
    from aws_sdk_arc_zonal_shift._services.arc_zonal_shift import (
        ARCZonalShiftClient,
        ARCZonalShiftClientConfig,
    )
    from aws_sdk_arc_zonal_shift._services.async_arc_zonal_shift import (
        AsyncARCZonalShiftClient,
        AsyncARCZonalShiftClientConfig,
    )


class ZonalShiftResource:
    def __init__(self, service: ARCZonalShiftClient) -> None:
        self._service = service

    def cancel_practice_run(
        self,
        zonal_shift_id: "aws_sdk_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.cancel_practice_run_response.CancelPracticeRunResponse":
        """<p>Cancel an in-progress practice run zonal shift in Amazon Application Recovery Controller.</p>

        Args:
            zonal_shift_id: <p>The identifier of a practice run zonal shift in Amazon Application Recovery Controller that you want to cancel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_arc_zonal_shift.types.cancel_practice_run_request.CancelPracticeRunRequest]",
        ) -> OperationResponse[
            "aws_sdk_arc_zonal_shift.types.cancel_practice_run_response.CancelPracticeRunResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.cancel_practice_run

            output, http_response = (
                aws_sdk_arc_zonal_shift._operations.perc_data_plane.cancel_practice_run.cancel_practice_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_arc_zonal_shift.types.cancel_practice_run_request.CancelPracticeRunRequest = {}  # type: ignore[typeddict-item]
        input_["zonal_shift_id"] = zonal_shift_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_zonal_shift(
        self,
        zonal_shift_id: "aws_sdk_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.zonal_shift.ZonalShift":
        """<p>Cancel a zonal shift in Amazon Application Recovery Controller. To cancel the zonal shift, specify the zonal shift ID.</p> <p>A zonal shift can be one that you've started for a resource in your Amazon Web Services account in an Amazon Web Services Region, or it can be a zonal shift started by a practice run with zonal autoshift. </p>

        Args:
            zonal_shift_id: <p>The internally-generated identifier of a zonal shift.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_arc_zonal_shift.types.cancel_zonal_shift_request.CancelZonalShiftRequest]",
        ) -> OperationResponse["aws_sdk_arc_zonal_shift.types.zonal_shift.ZonalShift"]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.cancel_zonal_shift

            output, http_response = (
                aws_sdk_arc_zonal_shift._operations.perc_data_plane.cancel_zonal_shift.cancel_zonal_shift(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_arc_zonal_shift.types.cancel_zonal_shift_request.CancelZonalShiftRequest = {}  # type: ignore[typeddict-item]
        input_["zonal_shift_id"] = zonal_shift_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_zonal_shift(
        self,
        zonal_shift_id: "aws_sdk_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
        comment: Optional[
            "aws_sdk_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment"
        ] = None,
        expires_in: Optional[
            "aws_sdk_arc_zonal_shift.types.expires_in.ExpiresIn"
        ] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.zonal_shift.ZonalShift":
        """<p>Update an active zonal shift in Amazon Application Recovery Controller in your Amazon Web Services account. You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift.</p>

        Args:
            zonal_shift_id: <p>The identifier of a zonal shift.</p>
            comment: <p>A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string.</p>
            expires_in: <p>The length of time that you want a zonal shift to be active, which ARC converts to an expiry time (expiration time). Zonal shifts are temporary. You can set a zonal shift to be active initially for up to three days (72 hours).</p> <p>If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you're ready to restore traffic to the Availability Zone.</p> <p>To set a length of time for a zonal shift to be active, specify a whole number, and then one of the following, with no space:</p> <ul> <li> <p> <b>A lowercase letter m:</b> To specify that the value is in minutes.</p> </li> <li> <p> <b>A lowercase letter h:</b> To specify that the value is in hours.</p> </li> </ul> <p>For example: <code>20h</code> means the zonal shift expires in 20 hours. <code>120m</code> means the zonal shift expires in 120 minutes (2 hours).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_arc_zonal_shift.types.update_zonal_shift_request.UpdateZonalShiftRequest]",
        ) -> OperationResponse["aws_sdk_arc_zonal_shift.types.zonal_shift.ZonalShift"]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_zonal_shift

            output, http_response = (
                aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_zonal_shift.update_zonal_shift(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_arc_zonal_shift.types.update_zonal_shift_request.UpdateZonalShiftRequest = {}  # type: ignore[typeddict-item]
        input_["zonal_shift_id"] = zonal_shift_id
        if comment is not None:
            input_["comment"] = comment
        if expires_in is not None:
            input_["expires_in"] = expires_in

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncZonalShiftResource:
    def __init__(self, service: AsyncARCZonalShiftClient) -> None:
        self._service = service

    async def cancel_practice_run(
        self,
        zonal_shift_id: "aws_sdk_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.cancel_practice_run_response.CancelPracticeRunResponse":
        """<p>Cancel an in-progress practice run zonal shift in Amazon Application Recovery Controller.</p>

        Args:
            zonal_shift_id: <p>The identifier of a practice run zonal shift in Amazon Application Recovery Controller that you want to cancel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_arc_zonal_shift.types.cancel_practice_run_request.CancelPracticeRunRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_arc_zonal_shift.types.cancel_practice_run_response.CancelPracticeRunResponse"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.cancel_practice_run

            (
                output,
                http_response,
            ) = await aws_sdk_arc_zonal_shift._operations.perc_data_plane.cancel_practice_run.async_cancel_practice_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_arc_zonal_shift.types.cancel_practice_run_request.CancelPracticeRunRequest = {}  # type: ignore[typeddict-item]
        input_["zonal_shift_id"] = zonal_shift_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_zonal_shift(
        self,
        zonal_shift_id: "aws_sdk_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.zonal_shift.ZonalShift":
        """<p>Cancel a zonal shift in Amazon Application Recovery Controller. To cancel the zonal shift, specify the zonal shift ID.</p> <p>A zonal shift can be one that you've started for a resource in your Amazon Web Services account in an Amazon Web Services Region, or it can be a zonal shift started by a practice run with zonal autoshift. </p>

        Args:
            zonal_shift_id: <p>The internally-generated identifier of a zonal shift.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_arc_zonal_shift.types.cancel_zonal_shift_request.CancelZonalShiftRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_arc_zonal_shift.types.zonal_shift.ZonalShift"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.cancel_zonal_shift

            (
                output,
                http_response,
            ) = await aws_sdk_arc_zonal_shift._operations.perc_data_plane.cancel_zonal_shift.async_cancel_zonal_shift(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_arc_zonal_shift.types.cancel_zonal_shift_request.CancelZonalShiftRequest = {}  # type: ignore[typeddict-item]
        input_["zonal_shift_id"] = zonal_shift_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_zonal_shift(
        self,
        zonal_shift_id: "aws_sdk_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
        comment: Optional[
            "aws_sdk_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment"
        ] = None,
        expires_in: Optional[
            "aws_sdk_arc_zonal_shift.types.expires_in.ExpiresIn"
        ] = None,
    ) -> "aws_sdk_arc_zonal_shift.types.zonal_shift.ZonalShift":
        """<p>Update an active zonal shift in Amazon Application Recovery Controller in your Amazon Web Services account. You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift.</p>

        Args:
            zonal_shift_id: <p>The identifier of a zonal shift.</p>
            comment: <p>A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string.</p>
            expires_in: <p>The length of time that you want a zonal shift to be active, which ARC converts to an expiry time (expiration time). Zonal shifts are temporary. You can set a zonal shift to be active initially for up to three days (72 hours).</p> <p>If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you're ready to restore traffic to the Availability Zone.</p> <p>To set a length of time for a zonal shift to be active, specify a whole number, and then one of the following, with no space:</p> <ul> <li> <p> <b>A lowercase letter m:</b> To specify that the value is in minutes.</p> </li> <li> <p> <b>A lowercase letter h:</b> To specify that the value is in hours.</p> </li> </ul> <p>For example: <code>20h</code> means the zonal shift expires in 20 hours. <code>120m</code> means the zonal shift expires in 120 minutes (2 hours).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_arc_zonal_shift.types.update_zonal_shift_request.UpdateZonalShiftRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_arc_zonal_shift.types.zonal_shift.ZonalShift"
        ]:
            import aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_zonal_shift

            (
                output,
                http_response,
            ) = await aws_sdk_arc_zonal_shift._operations.perc_data_plane.update_zonal_shift.async_update_zonal_shift(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_arc_zonal_shift.types.update_zonal_shift_request.UpdateZonalShiftRequest = {}  # type: ignore[typeddict-item]
        input_["zonal_shift_id"] = zonal_shift_id
        if comment is not None:
            input_["comment"] = comment
        if expires_in is not None:
            input_["expires_in"] = expires_in

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
