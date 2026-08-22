"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SynchronizationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.from_url_synchronization_configuration


class SynchronizationConfiguration(TypedDict, closed=True):
    from_url: NotRequired[
        "capo_bedrock_agentcore_control.types.from_url_synchronization_configuration.FromUrlSynchronizationConfiguration"
    ]
    """<p>Configuration for synchronizing from a URL-based source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SynchronizationConfiguration) -> dict:
    out: dict = {}
    if "from_url" in value:
        import capo_bedrock_agentcore_control.types.from_url_synchronization_configuration

        out["fromUrl"] = (
            capo_bedrock_agentcore_control.types.from_url_synchronization_configuration.serialize_json(
                value["from_url"]
            )
        )
    return out


def deserialize_json(data: dict) -> SynchronizationConfiguration:
    out: SynchronizationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("fromUrl") is not None:
        import capo_bedrock_agentcore_control.types.from_url_synchronization_configuration

        out["from_url"] = (
            capo_bedrock_agentcore_control.types.from_url_synchronization_configuration.deserialize_json(
                data["fromUrl"]
            )
        )
    return out
