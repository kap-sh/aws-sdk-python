"""Generated from Smithy shape ``com.amazonaws.securityhub#KeywordFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class KeywordFilter(TypedDict):
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A value for the keyword.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeywordFilter) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> KeywordFilter:
    out: KeywordFilter = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
