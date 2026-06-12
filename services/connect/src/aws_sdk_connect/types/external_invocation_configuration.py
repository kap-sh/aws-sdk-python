"""Generated from Smithy shape ``com.amazonaws.connect#ExternalInvocationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean


class ExternalInvocationConfiguration(TypedDict):
    enabled: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Enable external invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalInvocationConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> ExternalInvocationConfiguration:
    out: ExternalInvocationConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
