"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Certificate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.certificate_location


class Certificate(TypedDict):
    location: "aws_sdk_bedrock_agentcore_control.types.certificate_location.CertificateLocation"
    """<p>The location of the certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Certificate) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.certificate_location

    out["location"] = (
        aws_sdk_bedrock_agentcore_control.types.certificate_location.serialize_json(
            value["location"]
        )
    )
    return out


def deserialize_json(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if "location" in data:
        import aws_sdk_bedrock_agentcore_control.types.certificate_location

        out["location"] = (
            aws_sdk_bedrock_agentcore_control.types.certificate_location.deserialize_json(
                data["location"]
            )
        )
    else:
        raise DeserializationError("Certificate.location required")
    return out
