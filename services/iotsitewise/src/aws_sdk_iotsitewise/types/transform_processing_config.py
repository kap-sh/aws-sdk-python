"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TransformProcessingConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.compute_location
    import aws_sdk_iotsitewise.types.forwarding_config


class TransformProcessingConfig(TypedDict):
    compute_location: "aws_sdk_iotsitewise.types.compute_location.ComputeLocation"
    """<p>The compute location for the given transform property. </p>"""
    forwarding_config: NotRequired[
        "aws_sdk_iotsitewise.types.forwarding_config.ForwardingConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: TransformProcessingConfig) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.compute_location

    out["computeLocation"] = aws_sdk_iotsitewise.types.compute_location.serialize_json(
        value["compute_location"]
    )
    if "forwarding_config" in value:
        import aws_sdk_iotsitewise.types.forwarding_config

        out["forwardingConfig"] = (
            aws_sdk_iotsitewise.types.forwarding_config.serialize_json(
                value["forwarding_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransformProcessingConfig:
    out: TransformProcessingConfig = {}  # type: ignore[typeddict-item]
    if "computeLocation" in data:
        import aws_sdk_iotsitewise.types.compute_location

        out["compute_location"] = (
            aws_sdk_iotsitewise.types.compute_location.deserialize_json(
                data["computeLocation"]
            )
        )
    else:
        raise DeserializationError(
            "TransformProcessingConfig.compute_location required"
        )
    if "forwardingConfig" in data:
        import aws_sdk_iotsitewise.types.forwarding_config

        out["forwarding_config"] = (
            aws_sdk_iotsitewise.types.forwarding_config.deserialize_json(
                data["forwardingConfig"]
            )
        )
    return out
