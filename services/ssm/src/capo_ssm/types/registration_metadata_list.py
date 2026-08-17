"""Generated from Smithy shape ``com.amazonaws.ssm#RegistrationMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.registration_metadata_item

RegistrationMetadataList: TypeAlias = list[
    "capo_ssm.types.registration_metadata_item.RegistrationMetadataItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistrationMetadataList) -> list:
    import capo_ssm.types.registration_metadata_item

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.registration_metadata_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RegistrationMetadataList:
    import capo_ssm.types.registration_metadata_item

    out: RegistrationMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.registration_metadata_item.deserialize_aws_json_1_1(item)
        )
    return out
