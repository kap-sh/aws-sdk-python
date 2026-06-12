"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ConfigureAgentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.agent_configuration


class ConfigureAgentResponse(TypedDict):
    configuration: (
        "aws_sdk_codeguruprofiler.types.agent_configuration.AgentConfiguration"
    )
    """<p> An <a href=\"https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentConfiguration.html\"> <code>AgentConfiguration</code> </a> object that specifies if an agent profiles or not and for how long to return profiling data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigureAgentResponse) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.agent_configuration

    out["configuration"] = (
        aws_sdk_codeguruprofiler.types.agent_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConfigureAgentResponse:
    out: ConfigureAgentResponse = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_codeguruprofiler.types.agent_configuration

        out["configuration"] = (
            aws_sdk_codeguruprofiler.types.agent_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("ConfigureAgentResponse.configuration required")
    return out
