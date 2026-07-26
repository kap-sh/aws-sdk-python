"""Generated from Smithy shape ``com.amazonaws.codeconnections#SyncBlockerContextList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeconnections.types.sync_blocker_context

SyncBlockerContextList: TypeAlias = list[
    "capo_codeconnections.types.sync_blocker_context.SyncBlockerContext"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlockerContextList) -> list:
    import capo_codeconnections.types.sync_blocker_context

    out: list = []
    for item in value:
        out.append(
            capo_codeconnections.types.sync_blocker_context.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SyncBlockerContextList:
    import capo_codeconnections.types.sync_blocker_context

    out: SyncBlockerContextList = []
    for item in data:
        out.append(
            capo_codeconnections.types.sync_blocker_context.deserialize_aws_json_1_0(
                item
            )
        )
    return out
