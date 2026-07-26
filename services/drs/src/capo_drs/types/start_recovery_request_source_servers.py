"""Generated from Smithy shape ``com.amazonaws.drs#StartRecoveryRequestSourceServers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.start_recovery_request_source_server

StartRecoveryRequestSourceServers: TypeAlias = list[
    "capo_drs.types.start_recovery_request_source_server.StartRecoveryRequestSourceServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartRecoveryRequestSourceServers) -> list:
    import capo_drs.types.start_recovery_request_source_server

    out: list = []
    for item in value:
        out.append(
            capo_drs.types.start_recovery_request_source_server.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StartRecoveryRequestSourceServers:
    import capo_drs.types.start_recovery_request_source_server

    out: StartRecoveryRequestSourceServers = []
    for item in data:
        out.append(
            capo_drs.types.start_recovery_request_source_server.deserialize_json(item)
        )
    return out
