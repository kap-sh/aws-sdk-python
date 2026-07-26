"""Generated from Smithy shape ``com.amazonaws.eventbridge#DeletePartnerEventSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.account_id
    import capo_eventbridge.types.event_source_name


class DeletePartnerEventSourceRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.event_source_name.EventSourceName"
    """<p>The name of the event source to delete.</p>"""
    account: "capo_eventbridge.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the Amazon Web Services customer that the event source was created for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePartnerEventSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Account"] = value["account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePartnerEventSourceRequest:
    out: DeletePartnerEventSourceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeletePartnerEventSourceRequest.name required")
    if "Account" in data:
        out["account"] = data["Account"]
    else:
        raise DeserializationError("DeletePartnerEventSourceRequest.account required")
    return out
