"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RiskCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.count
    import aws_sdk_wellarchitected.types.risk

RiskCounts: TypeAlias = dict[
    "aws_sdk_wellarchitected.types.risk.Risk",
    "aws_sdk_wellarchitected.types.count.Count",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RiskCounts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_wellarchitected.types.risk

        out[aws_sdk_wellarchitected.types.risk.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> RiskCounts:
    out: RiskCounts = {}
    for key, value in data.items():
        import aws_sdk_wellarchitected.types.risk

        out[aws_sdk_wellarchitected.types.risk.deserialize_json(key)] = value
    return out
