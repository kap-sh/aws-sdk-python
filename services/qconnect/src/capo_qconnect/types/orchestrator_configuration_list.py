"""Generated from Smithy shape ``com.amazonaws.qconnect#OrchestratorConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.orchestrator_configuration_entry

OrchestratorConfigurationList: TypeAlias = list[
    "capo_qconnect.types.orchestrator_configuration_entry.OrchestratorConfigurationEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrchestratorConfigurationList) -> list:
    import capo_qconnect.types.orchestrator_configuration_entry

    out: list = []
    for item in value:
        out.append(
            capo_qconnect.types.orchestrator_configuration_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OrchestratorConfigurationList:
    import capo_qconnect.types.orchestrator_configuration_entry

    out: OrchestratorConfigurationList = []
    for item in data:
        out.append(
            capo_qconnect.types.orchestrator_configuration_entry.deserialize_json(item)
        )
    return out
