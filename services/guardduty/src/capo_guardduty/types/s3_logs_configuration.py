"""Generated from Smithy shape ``com.amazonaws.guardduty#S3LogsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean


class S3LogsConfiguration(TypedDict, closed=True):
    enable: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p> The status of S3 data event logs as a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3LogsConfiguration) -> dict:
    out: dict = {}
    if "enable" in value:
        out["enable"] = value["enable"]
    return out


def deserialize_json(data: dict) -> S3LogsConfiguration:
    out: S3LogsConfiguration = {}  # type: ignore[typeddict-item]
    if "enable" in data:
        out["enable"] = data["enable"]
    return out
