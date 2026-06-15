from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Optional

import aws_sdk_internetmonitor._auth._signers
import aws_sdk_internetmonitor._auth._sigv4
from aws_sdk_internetmonitor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.get_internet_event_input
    import aws_sdk_internetmonitor.types.get_internet_event_output
    import aws_sdk_internetmonitor.types.internet_event_id
    import aws_sdk_internetmonitor.types.internet_event_max_results
    import aws_sdk_internetmonitor.types.internet_event_summary
    import aws_sdk_internetmonitor.types.list_internet_events_input
    import aws_sdk_internetmonitor.types.list_internet_events_output
    from aws_sdk_internetmonitor._services.async_internet_monitor import (
        AsyncInternetMonitorClient,
        AsyncInternetMonitorClientConfig,
    )
    from aws_sdk_internetmonitor._services.internet_monitor import (
        InternetMonitorClient,
        InternetMonitorClientConfig,
    )


class InternetEventResource:
    def __init__(self, service: InternetMonitorClient) -> None:
        self._service = service

    def read(
        self,
        event_id: "aws_sdk_internetmonitor.types.internet_event_id.InternetEventId",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
    ) -> (
        "aws_sdk_internetmonitor.types.get_internet_event_output.GetInternetEventOutput"
    ):
        """<p>Gets information that Amazon CloudWatch Internet Monitor has generated about an internet event. Internet Monitor displays information about recent global health events, called internet events, on a global outages map that is available to all Amazon Web Services customers. </p> <p>The information returned here includes the impacted location, when the event started and (if the event is over) ended, the type of event (<code>PERFORMANCE</code> or <code>AVAILABILITY</code>), and the status (<code>ACTIVE</code> or <code>RESOLVED</code>).</p>

        Args:
            event_id: <p>The <code>EventId</code> of the internet event to return information for. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_internetmonitor.types.get_internet_event_input.GetInternetEventInput]",
        ) -> OperationResponse[
            "aws_sdk_internetmonitor.types.get_internet_event_output.GetInternetEventOutput"
        ]:
            import aws_sdk_internetmonitor._operations.internet_monitor20210603.get_internet_event

            output, http_response = (
                aws_sdk_internetmonitor._operations.internet_monitor20210603.get_internet_event.get_internet_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_internetmonitor.types.get_internet_event_input.GetInternetEventInput = {}  # type: ignore[typeddict-item]
        input_["event_id"] = event_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_internetmonitor.types.internet_event_max_results.InternetEventMaxResults"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        event_status: Optional[str] = None,
        event_type: Optional[str] = None,
    ) -> "aws_sdk_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput":
        """<p>Lists internet events that cause performance or availability issues for client locations. Amazon CloudWatch Internet Monitor displays information about recent global health events, called internet events, on a global outages map that is available to all Amazon Web Services customers. </p> <p>You can constrain the list of internet events returned by providing a start time and end time to define a total time frame for events you want to list. Both start time and end time specify the time when an event started. End time is optional. If you don't include it, the default end time is the current time.</p> <p>You can also limit the events returned to a specific status (<code>ACTIVE</code> or <code>RESOLVED</code>) or type (<code>PERFORMANCE</code> or <code>AVAILABILITY</code>).</p>

        Args:
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of query results that you want to return with this call.</p>
            start_time: <p>The start time of the time window that you want to get a list of internet events for.</p>
            end_time: <p>The end time of the time window that you want to get a list of internet events for.</p>
            event_status: <p>The status of an internet event.</p>
            event_type: <p>The type of network impairment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_internetmonitor.types.list_internet_events_input.ListInternetEventsInput]",
        ) -> OperationResponse[
            "aws_sdk_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput"
        ]:
            import aws_sdk_internetmonitor._operations.internet_monitor20210603.list_internet_events

            output, http_response = (
                aws_sdk_internetmonitor._operations.internet_monitor20210603.list_internet_events.list_internet_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_internetmonitor.types.list_internet_events_input.ListInternetEventsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if event_status is not None:
            input_["event_status"] = event_status
        if event_type is not None:
            input_["event_type"] = event_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncInternetEventResource:
    def __init__(self, service: AsyncInternetMonitorClient) -> None:
        self._service = service

    async def read(
        self,
        event_id: "aws_sdk_internetmonitor.types.internet_event_id.InternetEventId",
        *,
        config_overrides: Optional[AsyncInternetMonitorClientConfig] = None,
    ) -> (
        "aws_sdk_internetmonitor.types.get_internet_event_output.GetInternetEventOutput"
    ):
        """<p>Gets information that Amazon CloudWatch Internet Monitor has generated about an internet event. Internet Monitor displays information about recent global health events, called internet events, on a global outages map that is available to all Amazon Web Services customers. </p> <p>The information returned here includes the impacted location, when the event started and (if the event is over) ended, the type of event (<code>PERFORMANCE</code> or <code>AVAILABILITY</code>), and the status (<code>ACTIVE</code> or <code>RESOLVED</code>).</p>

        Args:
            event_id: <p>The <code>EventId</code> of the internet event to return information for. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_internetmonitor.types.get_internet_event_input.GetInternetEventInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_internetmonitor.types.get_internet_event_output.GetInternetEventOutput"
        ]:
            import aws_sdk_internetmonitor._operations.internet_monitor20210603.get_internet_event

            (
                output,
                http_response,
            ) = await aws_sdk_internetmonitor._operations.internet_monitor20210603.get_internet_event.async_get_internet_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_internetmonitor.types.get_internet_event_input.GetInternetEventInput = {}  # type: ignore[typeddict-item]
        input_["event_id"] = event_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncInternetMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_internetmonitor.types.internet_event_max_results.InternetEventMaxResults"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        event_status: Optional[str] = None,
        event_type: Optional[str] = None,
    ) -> "aws_sdk_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput":
        """<p>Lists internet events that cause performance or availability issues for client locations. Amazon CloudWatch Internet Monitor displays information about recent global health events, called internet events, on a global outages map that is available to all Amazon Web Services customers. </p> <p>You can constrain the list of internet events returned by providing a start time and end time to define a total time frame for events you want to list. Both start time and end time specify the time when an event started. End time is optional. If you don't include it, the default end time is the current time.</p> <p>You can also limit the events returned to a specific status (<code>ACTIVE</code> or <code>RESOLVED</code>) or type (<code>PERFORMANCE</code> or <code>AVAILABILITY</code>).</p>

        Args:
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of query results that you want to return with this call.</p>
            start_time: <p>The start time of the time window that you want to get a list of internet events for.</p>
            end_time: <p>The end time of the time window that you want to get a list of internet events for.</p>
            event_status: <p>The status of an internet event.</p>
            event_type: <p>The type of network impairment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_internetmonitor.types.list_internet_events_input.ListInternetEventsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput"
        ]:
            import aws_sdk_internetmonitor._operations.internet_monitor20210603.list_internet_events

            (
                output,
                http_response,
            ) = await aws_sdk_internetmonitor._operations.internet_monitor20210603.list_internet_events.async_list_internet_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_internetmonitor.types.list_internet_events_input.ListInternetEventsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if event_status is not None:
            input_["event_status"] = event_status
        if event_type is not None:
            input_["event_type"] = event_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
