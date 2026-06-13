"""Generated from Smithy shape ``com.amazonaws.drs#StartRecoveryRequestSourceServers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.start_recovery_request_source_server

StartRecoveryRequestSourceServers: TypeAlias = list[
    "aws_sdk_drs.types.start_recovery_request_source_server.StartRecoveryRequestSourceServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartRecoveryRequestSourceServers) -> list:
    import aws_sdk_drs.types.start_recovery_request_source_server

    out: list = []
    for item in value:
        out.append(
            aws_sdk_drs.types.start_recovery_request_source_server.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StartRecoveryRequestSourceServers:
    import aws_sdk_drs.types.start_recovery_request_source_server

    out: StartRecoveryRequestSourceServers = []
    for item in data:
        out.append(
            aws_sdk_drs.types.start_recovery_request_source_server.deserialize_json(
                item
            )
        )
    return out
