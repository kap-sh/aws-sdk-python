"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.link


class UpdateLinkResponse(TypedDict, closed=True):
    link: NotRequired["aws_sdk_networkmanager.types.link.Link"]
    """<p>Information about the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkResponse) -> dict:
    out: dict = {}
    if "link" in value:
        import aws_sdk_networkmanager.types.link

        out["Link"] = aws_sdk_networkmanager.types.link.serialize_json(value["link"])
    return out


def deserialize_json(data: dict) -> UpdateLinkResponse:
    out: UpdateLinkResponse = {}  # type: ignore[typeddict-item]
    if "Link" in data:
        import aws_sdk_networkmanager.types.link

        out["link"] = aws_sdk_networkmanager.types.link.deserialize_json(data["Link"])
    return out
