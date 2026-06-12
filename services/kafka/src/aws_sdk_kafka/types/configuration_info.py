"""Generated from Smithy shape ``com.amazonaws.kafka#ConfigurationInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__long
    import aws_sdk_kafka.types.__string


class ConfigurationInfo(TypedDict):
    arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>ARN of the configuration to use.</p>"""
    revision: NotRequired["aws_sdk_kafka.types.__long.__long"]
    """<p>The revision of the configuration to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationInfo) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "revision" in value:
        out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> ConfigurationInfo:
    out: ConfigurationInfo = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "revision" in data:
        out["revision"] = data["revision"]
    return out
