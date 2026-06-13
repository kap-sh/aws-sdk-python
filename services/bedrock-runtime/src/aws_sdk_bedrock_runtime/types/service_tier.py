"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ServiceTier``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.service_tier_type


class ServiceTier(TypedDict):
    type: "aws_sdk_bedrock_runtime.types.service_tier_type.ServiceTierType"
    """<p>Specifies the processing tier type used for serving the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceTier) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_runtime.types.service_tier_type

    out["type"] = aws_sdk_bedrock_runtime.types.service_tier_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> ServiceTier:
    out: ServiceTier = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_runtime.types.service_tier_type

        out["type"] = aws_sdk_bedrock_runtime.types.service_tier_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ServiceTier.type required")
    return out
