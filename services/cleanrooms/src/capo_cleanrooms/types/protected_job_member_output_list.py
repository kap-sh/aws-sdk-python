"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobMemberOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_single_member_output

ProtectedJobMemberOutputList: TypeAlias = list[
    "capo_cleanrooms.types.protected_job_single_member_output.ProtectedJobSingleMemberOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobMemberOutputList) -> list:
    import capo_cleanrooms.types.protected_job_single_member_output

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.protected_job_single_member_output.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProtectedJobMemberOutputList:
    import capo_cleanrooms.types.protected_job_single_member_output

    out: ProtectedJobMemberOutputList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.protected_job_single_member_output.deserialize_json(
                item
            )
        )
    return out
