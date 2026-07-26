"""Generated from Smithy shape ``com.amazonaws.opensearch#LimitsByRole``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.instance_role
    import capo_opensearch.types.limits

LimitsByRole: TypeAlias = dict[
    "capo_opensearch.types.instance_role.InstanceRole",
    "capo_opensearch.types.limits.Limits",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LimitsByRole) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_opensearch.types.limits

        out[key] = capo_opensearch.types.limits.serialize_json(value)
    return out


def deserialize_json(data: dict) -> LimitsByRole:
    out: LimitsByRole = {}
    for key, value in data.items():
        import capo_opensearch.types.limits

        out[key] = capo_opensearch.types.limits.deserialize_json(value)
    return out
