"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#LimitsByRole``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.instance_role
    import capo_elasticsearch_service.types.limits

LimitsByRole: TypeAlias = dict[
    "capo_elasticsearch_service.types.instance_role.InstanceRole",
    "capo_elasticsearch_service.types.limits.Limits",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LimitsByRole) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_elasticsearch_service.types.limits

        out[key] = capo_elasticsearch_service.types.limits.serialize_json(value)
    return out


def deserialize_json(data: dict) -> LimitsByRole:
    out: LimitsByRole = {}
    for key, value in data.items():
        import capo_elasticsearch_service.types.limits

        out[key] = capo_elasticsearch_service.types.limits.deserialize_json(value)
    return out
