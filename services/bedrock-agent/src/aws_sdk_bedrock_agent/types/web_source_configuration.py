"""Generated from Smithy shape ``com.amazonaws.bedrockagent#WebSourceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.url_configuration


class WebSourceConfiguration(TypedDict):
    url_configuration: "aws_sdk_bedrock_agent.types.url_configuration.UrlConfiguration"
    """<p>The configuration of the URL/URLs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebSourceConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.url_configuration

    out["urlConfiguration"] = (
        aws_sdk_bedrock_agent.types.url_configuration.serialize_json(
            value["url_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> WebSourceConfiguration:
    out: WebSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "urlConfiguration" in data:
        import aws_sdk_bedrock_agent.types.url_configuration

        out["url_configuration"] = (
            aws_sdk_bedrock_agent.types.url_configuration.deserialize_json(
                data["urlConfiguration"]
            )
        )
    else:
        raise DeserializationError("WebSourceConfiguration.url_configuration required")
    return out
