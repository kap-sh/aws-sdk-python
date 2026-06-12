"""Generated from Smithy shape ``com.amazonaws.amplify#SubDomainSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplify.types.sub_domain_setting

SubDomainSettings: TypeAlias = list[
    "aws_sdk_amplify.types.sub_domain_setting.SubDomainSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubDomainSettings) -> list:
    import aws_sdk_amplify.types.sub_domain_setting

    out: list = []
    for item in value:
        out.append(aws_sdk_amplify.types.sub_domain_setting.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubDomainSettings:
    import aws_sdk_amplify.types.sub_domain_setting

    out: SubDomainSettings = []
    for item in data:
        out.append(aws_sdk_amplify.types.sub_domain_setting.deserialize_json(item))
    return out
