"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CredentialLockerListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.credential_locker_summary

CredentialLockerListDefinition: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.credential_locker_summary.CredentialLockerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialLockerListDefinition) -> list:
    import aws_sdk_iot_managed_integrations.types.credential_locker_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.credential_locker_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CredentialLockerListDefinition:
    import aws_sdk_iot_managed_integrations.types.credential_locker_summary

    out: CredentialLockerListDefinition = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.credential_locker_summary.deserialize_json(
                item
            )
        )
    return out
