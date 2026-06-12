"""Generated from Smithy shape ``com.amazonaws.health#entityStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.count
    import aws_sdk_health.types.entity_status_code

entityStatuses: TypeAlias = dict[
    "aws_sdk_health.types.entity_status_code.entityStatusCode",
    "aws_sdk_health.types.count.count",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: entityStatuses) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_health.types.entity_status_code

        out[aws_sdk_health.types.entity_status_code.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> entityStatuses:
    out: entityStatuses = {}
    for key, value in data.items():
        import aws_sdk_health.types.entity_status_code

        out[aws_sdk_health.types.entity_status_code.deserialize_aws_json_1_1(key)] = (
            value
        )
    return out
