"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#OverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.preview_override

OverrideList: TypeAlias = list[
    "aws_sdk_ssm_contacts.types.preview_override.PreviewOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverrideList) -> list:
    import aws_sdk_ssm_contacts.types.preview_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_contacts.types.preview_override.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OverrideList:
    import aws_sdk_ssm_contacts.types.preview_override

    out: OverrideList = []
    for item in data:
        out.append(
            aws_sdk_ssm_contacts.types.preview_override.deserialize_aws_json_1_1(item)
        )
    return out
