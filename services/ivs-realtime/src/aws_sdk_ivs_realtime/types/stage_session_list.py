"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StageSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.stage_session_summary

StageSessionList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.stage_session_summary.StageSessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StageSessionList) -> list:
    import aws_sdk_ivs_realtime.types.stage_session_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs_realtime.types.stage_session_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StageSessionList:
    import aws_sdk_ivs_realtime.types.stage_session_summary

    out: StageSessionList = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.stage_session_summary.deserialize_json(item)
        )
    return out
