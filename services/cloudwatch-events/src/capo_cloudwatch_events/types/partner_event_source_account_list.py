"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PartnerEventSourceAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.partner_event_source_account

PartnerEventSourceAccountList: TypeAlias = list[
    "capo_cloudwatch_events.types.partner_event_source_account.PartnerEventSourceAccount"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerEventSourceAccountList) -> list:
    import capo_cloudwatch_events.types.partner_event_source_account

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_events.types.partner_event_source_account.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PartnerEventSourceAccountList:
    import capo_cloudwatch_events.types.partner_event_source_account

    out: PartnerEventSourceAccountList = []
    for item in data:
        out.append(
            capo_cloudwatch_events.types.partner_event_source_account.deserialize_aws_json_1_1(
                item
            )
        )
    return out
