"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#KmsGrantConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.kms_grant_configuration

KmsGrantConfigurationsList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.kms_grant_configuration.KmsGrantConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: KmsGrantConfigurationsList) -> list:
    import aws_sdk_accessanalyzer.types.kms_grant_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_accessanalyzer.types.kms_grant_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KmsGrantConfigurationsList:
    import aws_sdk_accessanalyzer.types.kms_grant_configuration

    out: KmsGrantConfigurationsList = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.kms_grant_configuration.deserialize_json(item)
        )
    return out
