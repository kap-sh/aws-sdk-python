"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.assistant_summary

AssistantList: TypeAlias = list[
    "aws_sdk_qconnect.types.assistant_summary.AssistantSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssistantList) -> list:
    import aws_sdk_qconnect.types.assistant_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.assistant_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssistantList:
    import aws_sdk_qconnect.types.assistant_summary

    out: AssistantList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.assistant_summary.deserialize_json(item))
    return out
