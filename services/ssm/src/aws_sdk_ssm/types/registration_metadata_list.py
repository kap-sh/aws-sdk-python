"""Generated from Smithy shape ``com.amazonaws.ssm#RegistrationMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.registration_metadata_item

RegistrationMetadataList: TypeAlias = list[
    "aws_sdk_ssm.types.registration_metadata_item.RegistrationMetadataItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistrationMetadataList) -> list:
    import aws_sdk_ssm.types.registration_metadata_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.registration_metadata_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RegistrationMetadataList:
    import aws_sdk_ssm.types.registration_metadata_item

    out: RegistrationMetadataList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.registration_metadata_item.deserialize_aws_json_1_1(item)
        )
    return out
