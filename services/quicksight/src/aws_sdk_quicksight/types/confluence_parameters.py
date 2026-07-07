"""Generated from Smithy shape ``com.amazonaws.quicksight#ConfluenceParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.site_base_url


class ConfluenceParameters(TypedDict, closed=True):
    confluence_url: "aws_sdk_quicksight.types.site_base_url.SiteBaseUrl"
    """<p>The URL of the Confluence site to connect to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceParameters) -> dict:
    out: dict = {}
    out["ConfluenceUrl"] = value["confluence_url"]
    return out


def deserialize_json(data: dict) -> ConfluenceParameters:
    out: ConfluenceParameters = {}  # type: ignore[typeddict-item]
    if "ConfluenceUrl" in data:
        out["confluence_url"] = data["ConfluenceUrl"]
    else:
        raise DeserializationError("ConfluenceParameters.confluence_url required")
    return out
