"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MemoryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.enabled_memory_types
    import aws_sdk_bedrock_agent.types.session_summary_configuration
    import aws_sdk_bedrock_agent.types.storage_days


class MemoryConfiguration(TypedDict):
    enabled_memory_types: (
        "aws_sdk_bedrock_agent.types.enabled_memory_types.EnabledMemoryTypes"
    )
    """<p>The type of memory that is stored. </p>"""
    storage_days: "aws_sdk_bedrock_agent.types.storage_days.StorageDays"
    """<p>The number of days the agent is configured to retain the conversational context.</p>"""
    session_summary_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.session_summary_configuration.SessionSummaryConfiguration"
    ]
    """<p>Contains the configuration for SESSION_SUMMARY memory type enabled for the agent. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.enabled_memory_types

    out["enabledMemoryTypes"] = (
        aws_sdk_bedrock_agent.types.enabled_memory_types.serialize_json(
            value["enabled_memory_types"]
        )
    )
    out["storageDays"] = value.get("storage_days", 30)
    if "session_summary_configuration" in value:
        import aws_sdk_bedrock_agent.types.session_summary_configuration

        out["sessionSummaryConfiguration"] = (
            aws_sdk_bedrock_agent.types.session_summary_configuration.serialize_json(
                value["session_summary_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryConfiguration:
    out: MemoryConfiguration = {}  # type: ignore[typeddict-item]
    if "enabledMemoryTypes" in data:
        import aws_sdk_bedrock_agent.types.enabled_memory_types

        out["enabled_memory_types"] = (
            aws_sdk_bedrock_agent.types.enabled_memory_types.deserialize_json(
                data["enabledMemoryTypes"]
            )
        )
    else:
        raise DeserializationError("MemoryConfiguration.enabled_memory_types required")
    if "storageDays" in data:
        out["storage_days"] = data["storageDays"]
    else:
        out["storage_days"] = 30
    if "sessionSummaryConfiguration" in data:
        import aws_sdk_bedrock_agent.types.session_summary_configuration

        out["session_summary_configuration"] = (
            aws_sdk_bedrock_agent.types.session_summary_configuration.deserialize_json(
                data["sessionSummaryConfiguration"]
            )
        )
    return out
