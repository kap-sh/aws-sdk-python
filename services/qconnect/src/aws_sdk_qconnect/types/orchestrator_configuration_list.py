"""Generated from Smithy shape ``com.amazonaws.qconnect#OrchestratorConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.orchestrator_configuration_entry

OrchestratorConfigurationList: TypeAlias = list[
    "aws_sdk_qconnect.types.orchestrator_configuration_entry.OrchestratorConfigurationEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrchestratorConfigurationList) -> list:
    import aws_sdk_qconnect.types.orchestrator_configuration_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.orchestrator_configuration_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> OrchestratorConfigurationList:
    import aws_sdk_qconnect.types.orchestrator_configuration_entry

    out: OrchestratorConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.orchestrator_configuration_entry.deserialize_json(
                item
            )
        )
    return out
