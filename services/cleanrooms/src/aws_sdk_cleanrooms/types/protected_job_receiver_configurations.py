"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobReceiverConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_receiver_configuration

ProtectedJobReceiverConfigurations: TypeAlias = list[
    "aws_sdk_cleanrooms.types.protected_job_receiver_configuration.ProtectedJobReceiverConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobReceiverConfigurations) -> list:
    import aws_sdk_cleanrooms.types.protected_job_receiver_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.protected_job_receiver_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProtectedJobReceiverConfigurations:
    import aws_sdk_cleanrooms.types.protected_job_receiver_configuration

    out: ProtectedJobReceiverConfigurations = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.protected_job_receiver_configuration.deserialize_json(
                item
            )
        )
    return out
