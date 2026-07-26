"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListOperationEventsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.next_token
    import capo_ssm_sap.types.operation_event_list


class ListOperationEventsOutput(TypedDict, closed=True):
    operation_events: NotRequired[
        "capo_ssm_sap.types.operation_event_list.OperationEventList"
    ]
    """<p>A returned list of operation events that meet the filter criteria.</p>"""
    next_token: NotRequired["capo_ssm_sap.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOperationEventsOutput) -> dict:
    out: dict = {}
    if "operation_events" in value:
        import capo_ssm_sap.types.operation_event_list

        out["OperationEvents"] = capo_ssm_sap.types.operation_event_list.serialize_json(
            value["operation_events"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOperationEventsOutput:
    out: ListOperationEventsOutput = {}  # type: ignore[typeddict-item]
    if "OperationEvents" in data:
        import capo_ssm_sap.types.operation_event_list

        out["operation_events"] = (
            capo_ssm_sap.types.operation_event_list.deserialize_json(
                data["OperationEvents"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
