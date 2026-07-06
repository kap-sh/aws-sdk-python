"""Generated from Smithy shape ``com.amazonaws.mq#ConfigurationId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__integer
    import aws_sdk_mq.types.__string


class ConfigurationId(TypedDict, closed=True):
    id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Required. The unique ID that Amazon MQ generates for the configuration.</p>"""
    revision: NotRequired["aws_sdk_mq.types.__integer.__integer"]
    """<p>The revision number of the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationId) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "revision" in value:
        out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> ConfigurationId:
    out: ConfigurationId = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "revision" in data:
        out["revision"] = data["revision"]
    return out
