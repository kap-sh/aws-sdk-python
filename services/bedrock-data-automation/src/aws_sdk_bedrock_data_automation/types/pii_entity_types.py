"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#PIIEntityTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.pii_entity_type

PIIEntityTypes: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.pii_entity_type.PIIEntityType"
]


# --- restJson1 ser/de ---
def serialize_json(value: PIIEntityTypes) -> list:
    import aws_sdk_bedrock_data_automation.types.pii_entity_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.pii_entity_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PIIEntityTypes:
    import aws_sdk_bedrock_data_automation.types.pii_entity_type

    out: PIIEntityTypes = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.pii_entity_type.deserialize_json(item)
        )
    return out
