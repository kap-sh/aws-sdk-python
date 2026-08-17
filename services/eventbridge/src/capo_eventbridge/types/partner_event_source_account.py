"""Generated from Smithy shape ``com.amazonaws.eventbridge#PartnerEventSourceAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.account_id
    import capo_eventbridge.types.event_source_state
    import capo_eventbridge.types.timestamp


class PartnerEventSourceAccount(TypedDict, closed=True):
    account: NotRequired["capo_eventbridge.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that the partner event source was offered to.</p>"""
    creation_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The date and time the event source was created.</p>"""
    expiration_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The date and time that the event source will expire, if the Amazon Web Services account doesn't create a matching event bus for it.</p>"""
    state: NotRequired["capo_eventbridge.types.event_source_state.EventSourceState"]
    """<p>The state of the event source. If it is ACTIVE, you have already created a matching event bus for this event source, and that event bus is active. If it is PENDING, either you haven't yet created a matching event bus, or that event bus is deactivated. If it is DELETED, you have created a matching event bus, but the event source has since been deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerEventSourceAccount) -> dict:
    out: dict = {}
    if "account" in value:
        out["Account"] = value["account"]
    if "creation_time" in value:
        import capo_eventbridge.types.timestamp

        out["CreationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "expiration_time" in value:
        import capo_eventbridge.types.timestamp

        out["ExpirationTime"] = capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
            value["expiration_time"]
        )
    if "state" in value:
        import capo_eventbridge.types.event_source_state

        out["State"] = capo_eventbridge.types.event_source_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartnerEventSourceAccount:
    out: PartnerEventSourceAccount = {}  # type: ignore[typeddict-item]
    if data.get("Account") is not None:
        out["account"] = data["Account"]
    if data.get("CreationTime") is not None:
        import capo_eventbridge.types.timestamp

        out["creation_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if data.get("ExpirationTime") is not None:
        import capo_eventbridge.types.timestamp

        out["expiration_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationTime"]
            )
        )
    if data.get("State") is not None:
        import capo_eventbridge.types.event_source_state

        out["state"] = (
            capo_eventbridge.types.event_source_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out
