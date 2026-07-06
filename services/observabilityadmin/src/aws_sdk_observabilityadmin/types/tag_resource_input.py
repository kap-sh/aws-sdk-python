"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.resource_arn
    import aws_sdk_observabilityadmin.types.tag_map_input


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"
    """<p> The Amazon Resource Name (ARN) of the telemetry rule resource to tag. </p>"""
    tags: "aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"
    """<p> The key-value pairs to add or update for the telemetry rule resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_observabilityadmin.types.tag_map_input

    out["Tags"] = aws_sdk_observabilityadmin.types.tag_map_input.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "Tags" in data:
        import aws_sdk_observabilityadmin.types.tag_map_input

        out["tags"] = aws_sdk_observabilityadmin.types.tag_map_input.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
