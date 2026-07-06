"""Generated from Smithy shape ``com.amazonaws.auditmanager#URL``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.hyperlink_name
    import aws_sdk_auditmanager.types.url_link


class URL(TypedDict, closed=True):
    hyperlink_name: NotRequired[
        "aws_sdk_auditmanager.types.hyperlink_name.HyperlinkName"
    ]
    """<p> The name or word that's used as a hyperlink to the URL. </p>"""
    link: NotRequired["aws_sdk_auditmanager.types.url_link.UrlLink"]
    """<p> The unique identifier for the internet resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: URL) -> dict:
    out: dict = {}
    if "hyperlink_name" in value:
        out["hyperlinkName"] = value["hyperlink_name"]
    if "link" in value:
        out["link"] = value["link"]
    return out


def deserialize_json(data: dict) -> URL:
    out: URL = {}  # type: ignore[typeddict-item]
    if "hyperlinkName" in data:
        out["hyperlink_name"] = data["hyperlinkName"]
    if "link" in data:
        out["link"] = data["link"]
    return out
