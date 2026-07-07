"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SynchronizationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.from_url_synchronization_configuration


class SynchronizationConfiguration(TypedDict, closed=True):
    from_url: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.from_url_synchronization_configuration.FromUrlSynchronizationConfiguration"
    ]
    """<p>Configuration for synchronizing from a URL-based source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SynchronizationConfiguration) -> dict:
    out: dict = {}
    if "from_url" in value:
        import aws_sdk_bedrock_agentcore_control.types.from_url_synchronization_configuration

        out["fromUrl"] = (
            aws_sdk_bedrock_agentcore_control.types.from_url_synchronization_configuration.serialize_json(
                value["from_url"]
            )
        )
    return out


def deserialize_json(data: dict) -> SynchronizationConfiguration:
    out: SynchronizationConfiguration = {}  # type: ignore[typeddict-item]
    if "fromUrl" in data:
        import aws_sdk_bedrock_agentcore_control.types.from_url_synchronization_configuration

        out["from_url"] = (
            aws_sdk_bedrock_agentcore_control.types.from_url_synchronization_configuration.deserialize_json(
                data["fromUrl"]
            )
        )
    return out
