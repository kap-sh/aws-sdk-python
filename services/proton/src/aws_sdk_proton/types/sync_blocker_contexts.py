"""Generated from Smithy shape ``com.amazonaws.proton#SyncBlockerContexts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.sync_blocker_context

SyncBlockerContexts: TypeAlias = list[
    "aws_sdk_proton.types.sync_blocker_context.SyncBlockerContext"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlockerContexts) -> list:
    import aws_sdk_proton.types.sync_blocker_context

    out: list = []
    for item in value:
        out.append(
            aws_sdk_proton.types.sync_blocker_context.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SyncBlockerContexts:
    import aws_sdk_proton.types.sync_blocker_context

    out: SyncBlockerContexts = []
    for item in data:
        out.append(
            aws_sdk_proton.types.sync_blocker_context.deserialize_aws_json_1_0(item)
        )
    return out
