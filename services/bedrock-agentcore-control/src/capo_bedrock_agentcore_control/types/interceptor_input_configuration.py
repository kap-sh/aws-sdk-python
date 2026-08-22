"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InterceptorInputConfiguration``."""

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError


class InterceptorInputConfiguration(TypedDict, closed=True):
    pass_request_headers: "bool"
    """<p>Indicates whether to pass request headers as input into the interceptor. When set to true, request headers will be passed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InterceptorInputConfiguration) -> dict:
    out: dict = {}
    out["passRequestHeaders"] = value["pass_request_headers"]
    return out


def deserialize_json(data: dict) -> InterceptorInputConfiguration:
    out: InterceptorInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("passRequestHeaders") is not None:
        out["pass_request_headers"] = data["passRequestHeaders"]
    else:
        raise DeserializationError(
            "InterceptorInputConfiguration.pass_request_headers required"
        )
    return out
