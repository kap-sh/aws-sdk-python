"""Generated from Smithy shape ``com.amazonaws.eventbridge#PartnerEventSourceAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.partner_event_source_account

PartnerEventSourceAccountList: TypeAlias = list[
    "capo_eventbridge.types.partner_event_source_account.PartnerEventSourceAccount"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerEventSourceAccountList) -> list:
    import capo_eventbridge.types.partner_event_source_account

    out: list = []
    for item in value:
        out.append(
            capo_eventbridge.types.partner_event_source_account.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PartnerEventSourceAccountList:
    import capo_eventbridge.types.partner_event_source_account

    out: PartnerEventSourceAccountList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_eventbridge.types.partner_event_source_account.deserialize_aws_json_1_1(
                item
            )
        )
    return out
