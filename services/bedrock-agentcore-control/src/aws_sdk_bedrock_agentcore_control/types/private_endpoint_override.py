"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrivateEndpointOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint_override_domain


class PrivateEndpointOverride(TypedDict, closed=True):
    domain: "aws_sdk_bedrock_agentcore_control.types.private_endpoint_override_domain.PrivateEndpointOverrideDomain"
    """<p>The domain to override with a private endpoint.</p>"""
    private_endpoint: (
        "aws_sdk_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    )
    """<p>The private endpoint configuration for the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateEndpointOverride) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import aws_sdk_bedrock_agentcore_control.types.private_endpoint

    out["privateEndpoint"] = (
        aws_sdk_bedrock_agentcore_control.types.private_endpoint.serialize_json(
            value["private_endpoint"]
        )
    )
    return out


def deserialize_json(data: dict) -> PrivateEndpointOverride:
    out: PrivateEndpointOverride = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("PrivateEndpointOverride.domain required")
    if "privateEndpoint" in data:
        import aws_sdk_bedrock_agentcore_control.types.private_endpoint

        out["private_endpoint"] = (
            aws_sdk_bedrock_agentcore_control.types.private_endpoint.deserialize_json(
                data["privateEndpoint"]
            )
        )
    else:
        raise DeserializationError("PrivateEndpointOverride.private_endpoint required")
    return out
