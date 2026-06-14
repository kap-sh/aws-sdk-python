"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ParentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.entity_identifier

ParentList: TypeAlias = list[
    "aws_sdk_verifiedpermissions.types.entity_identifier.EntityIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParentList) -> list:
    import aws_sdk_verifiedpermissions.types.entity_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ParentList:
    import aws_sdk_verifiedpermissions.types.entity_identifier

    out: ParentList = []
    for item in data:
        out.append(
            aws_sdk_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                item
            )
        )
    return out
