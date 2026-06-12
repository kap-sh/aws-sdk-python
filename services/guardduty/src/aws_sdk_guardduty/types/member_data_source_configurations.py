"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberDataSourceConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.member_data_source_configuration

MemberDataSourceConfigurations: TypeAlias = list[
    "aws_sdk_guardduty.types.member_data_source_configuration.MemberDataSourceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberDataSourceConfigurations) -> list:
    import aws_sdk_guardduty.types.member_data_source_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_guardduty.types.member_data_source_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MemberDataSourceConfigurations:
    import aws_sdk_guardduty.types.member_data_source_configuration

    out: MemberDataSourceConfigurations = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.member_data_source_configuration.deserialize_json(
                item
            )
        )
    return out
