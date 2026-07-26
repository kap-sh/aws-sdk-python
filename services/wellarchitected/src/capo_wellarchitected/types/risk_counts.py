"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RiskCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.count
    import capo_wellarchitected.types.risk

RiskCounts: TypeAlias = dict[
    "capo_wellarchitected.types.risk.Risk", "capo_wellarchitected.types.count.Count"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RiskCounts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_wellarchitected.types.risk

        out[capo_wellarchitected.types.risk.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> RiskCounts:
    out: RiskCounts = {}
    for key, value in data.items():
        import capo_wellarchitected.types.risk

        out[capo_wellarchitected.types.risk.deserialize_json(key)] = value
    return out
