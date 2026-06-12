"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#LimitsByRole``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.instance_role
    import aws_sdk_elasticsearch_service.types.limits

LimitsByRole: TypeAlias = dict[
    "aws_sdk_elasticsearch_service.types.instance_role.InstanceRole",
    "aws_sdk_elasticsearch_service.types.limits.Limits",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LimitsByRole) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_elasticsearch_service.types.limits

        out[key] = aws_sdk_elasticsearch_service.types.limits.serialize_json(value)
    return out


def deserialize_json(data: dict) -> LimitsByRole:
    out: LimitsByRole = {}
    for key, value in data.items():
        import aws_sdk_elasticsearch_service.types.limits

        out[key] = aws_sdk_elasticsearch_service.types.limits.deserialize_json(value)
    return out
