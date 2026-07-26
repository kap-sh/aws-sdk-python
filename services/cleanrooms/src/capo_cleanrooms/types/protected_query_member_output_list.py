"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryMemberOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_query_single_member_output

ProtectedQueryMemberOutputList: TypeAlias = list[
    "capo_cleanrooms.types.protected_query_single_member_output.ProtectedQuerySingleMemberOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryMemberOutputList) -> list:
    import capo_cleanrooms.types.protected_query_single_member_output

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.protected_query_single_member_output.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProtectedQueryMemberOutputList:
    import capo_cleanrooms.types.protected_query_single_member_output

    out: ProtectedQueryMemberOutputList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.protected_query_single_member_output.deserialize_json(
                item
            )
        )
    return out
