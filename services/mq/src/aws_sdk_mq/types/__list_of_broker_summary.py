"""Generated from Smithy shape ``com.amazonaws.mq#__listOfBrokerSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mq.types.broker_summary

__listOfBrokerSummary: TypeAlias = list["aws_sdk_mq.types.broker_summary.BrokerSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBrokerSummary) -> list:
    import aws_sdk_mq.types.broker_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_mq.types.broker_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBrokerSummary:
    import aws_sdk_mq.types.broker_summary

    out: __listOfBrokerSummary = []
    for item in data:
        out.append(aws_sdk_mq.types.broker_summary.deserialize_json(item))
    return out
