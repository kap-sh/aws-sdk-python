"""Generated from Smithy shape ``com.amazonaws.eventbridge#PartnerEventSourceAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.account_id
    import aws_sdk_eventbridge.types.event_source_state
    import aws_sdk_eventbridge.types.timestamp


class PartnerEventSourceAccount(TypedDict, closed=True):
    account: NotRequired["aws_sdk_eventbridge.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that the partner event source was offered to.</p>"""
    creation_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>The date and time the event source was created.</p>"""
    expiration_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>The date and time that the event source will expire, if the Amazon Web Services account doesn't create a matching event bus for it.</p>"""
    state: NotRequired["aws_sdk_eventbridge.types.event_source_state.EventSourceState"]
    """<p>The state of the event source. If it is ACTIVE, you have already created a matching event bus for this event source, and that event bus is active. If it is PENDING, either you haven't yet created a matching event bus, or that event bus is deactivated. If it is DELETED, you have created a matching event bus, but the event source has since been deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerEventSourceAccount) -> dict:
    out: dict = {}
    if "account" in value:
        out["Account"] = value["account"]
    if "creation_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["CreationTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "expiration_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["ExpirationTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["expiration_time"]
            )
        )
    if "state" in value:
        import aws_sdk_eventbridge.types.event_source_state

        out["State"] = (
            aws_sdk_eventbridge.types.event_source_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PartnerEventSourceAccount:
    out: PartnerEventSourceAccount = {}  # type: ignore[typeddict-item]
    if "Account" in data:
        out["account"] = data["Account"]
    if "CreationTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["creation_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "ExpirationTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["expiration_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationTime"]
            )
        )
    if "State" in data:
        import aws_sdk_eventbridge.types.event_source_state

        out["state"] = (
            aws_sdk_eventbridge.types.event_source_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out
