"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationCredentialList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_credential

ApplicationCredentialList: TypeAlias = list[
    "aws_sdk_ssm_sap.types.application_credential.ApplicationCredential"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationCredentialList) -> list:
    import aws_sdk_ssm_sap.types.application_credential

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_sap.types.application_credential.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationCredentialList:
    import aws_sdk_ssm_sap.types.application_credential

    out: ApplicationCredentialList = []
    for item in data:
        out.append(aws_sdk_ssm_sap.types.application_credential.deserialize_json(item))
    return out
