"""Generated from Smithy shape ``com.amazonaws.managedblockchain#LogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.enabled


class LogConfiguration(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_managedblockchain.types.enabled.Enabled"]
    """<p>Indicates whether logging is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> LogConfiguration:
    out: LogConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
