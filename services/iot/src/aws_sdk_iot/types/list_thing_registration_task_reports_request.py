"""Generated from Smithy shape ``com.amazonaws.iot#ListThingRegistrationTaskReportsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.registry_max_results
    import aws_sdk_iot.types.report_type
    import aws_sdk_iot.types.task_id


class ListThingRegistrationTaskReportsRequest(TypedDict):
    task_id: "aws_sdk_iot.types.task_id.TaskId"
    """<p>The id of the task.</p>"""
    report_type: "aws_sdk_iot.types.report_type.ReportType"
    """<p>The type of task report.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot.types.registry_max_results.RegistryMaxResults"
    ]
    """<p>The maximum number of results to return per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingRegistrationTaskReportsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThingRegistrationTaskReportsRequest:
    out: ListThingRegistrationTaskReportsRequest = {}  # type: ignore[typeddict-item]
    return out
