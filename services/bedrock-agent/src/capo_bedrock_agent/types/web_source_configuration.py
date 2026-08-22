"""Generated from Smithy shape ``com.amazonaws.bedrockagent#WebSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.url_configuration


class WebSourceConfiguration(TypedDict, closed=True):
    url_configuration: "capo_bedrock_agent.types.url_configuration.UrlConfiguration"
    """<p>The configuration of the URL/URLs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebSourceConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.url_configuration

    out["urlConfiguration"] = capo_bedrock_agent.types.url_configuration.serialize_json(
        value["url_configuration"]
    )
    return out


def deserialize_json(data: dict) -> WebSourceConfiguration:
    out: WebSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("urlConfiguration") is not None:
        import capo_bedrock_agent.types.url_configuration

        out["url_configuration"] = (
            capo_bedrock_agent.types.url_configuration.deserialize_json(
                data["urlConfiguration"]
            )
        )
    else:
        raise DeserializationError("WebSourceConfiguration.url_configuration required")
    return out
