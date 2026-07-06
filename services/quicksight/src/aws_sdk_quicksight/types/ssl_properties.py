"""Generated from Smithy shape ``com.amazonaws.quicksight#SslProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean


class SslProperties(TypedDict, closed=True):
    disable_ssl: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A Boolean option to control whether SSL should be disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SslProperties) -> dict:
    out: dict = {}
    out["DisableSsl"] = value.get("disable_ssl", False)
    return out


def deserialize_json(data: dict) -> SslProperties:
    out: SslProperties = {}  # type: ignore[typeddict-item]
    if "DisableSsl" in data:
        out["disable_ssl"] = data["DisableSsl"]
    else:
        out["disable_ssl"] = False
    return out
