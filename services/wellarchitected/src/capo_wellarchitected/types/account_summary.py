"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AccountSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.check_status
    import capo_wellarchitected.types.check_status_count

AccountSummary: TypeAlias = dict[
    "capo_wellarchitected.types.check_status.CheckStatus",
    "capo_wellarchitected.types.check_status_count.CheckStatusCount",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AccountSummary) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_wellarchitected.types.check_status

        out[capo_wellarchitected.types.check_status.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> AccountSummary:
    out: AccountSummary = {}
    for key, value in data.items():
        import capo_wellarchitected.types.check_status

        out[capo_wellarchitected.types.check_status.deserialize_json(key)] = value
    return out
