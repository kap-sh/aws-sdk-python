"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#UntagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.resource_arn
    import aws_sdk_observabilityadmin.types.tag_key_list


class UntagResourceInput(TypedDict):
    resource_arn: "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"
    """<p> The Amazon Resource Name (ARN) of the telemetry rule resource to remove tags from. </p>"""
    tag_keys: "aws_sdk_observabilityadmin.types.tag_key_list.TagKeyList"
    """<p> The list of tag keys to remove from the telemetry rule resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_observabilityadmin.types.tag_key_list

    out["TagKeys"] = aws_sdk_observabilityadmin.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_observabilityadmin.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_observabilityadmin.types.tag_key_list.deserialize_json(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out
