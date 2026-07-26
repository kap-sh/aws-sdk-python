"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#OverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_contacts.types.preview_override

OverrideList: TypeAlias = list[
    "capo_ssm_contacts.types.preview_override.PreviewOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverrideList) -> list:
    import capo_ssm_contacts.types.preview_override

    out: list = []
    for item in value:
        out.append(
            capo_ssm_contacts.types.preview_override.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OverrideList:
    import capo_ssm_contacts.types.preview_override

    out: OverrideList = []
    for item in data:
        out.append(
            capo_ssm_contacts.types.preview_override.deserialize_aws_json_1_1(item)
        )
    return out
