"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StructuredMessageDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.structured_message_field_name_and_data_type_pair

StructuredMessageDefinition: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.structured_message_field_name_and_data_type_pair.StructuredMessageFieldNameAndDataTypePair"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StructuredMessageDefinition) -> list:
    import aws_sdk_iotfleetwise.types.structured_message_field_name_and_data_type_pair

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.structured_message_field_name_and_data_type_pair.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StructuredMessageDefinition:
    import aws_sdk_iotfleetwise.types.structured_message_field_name_and_data_type_pair

    out: StructuredMessageDefinition = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.structured_message_field_name_and_data_type_pair.deserialize_aws_json_1_0(
                item
            )
        )
    return out
