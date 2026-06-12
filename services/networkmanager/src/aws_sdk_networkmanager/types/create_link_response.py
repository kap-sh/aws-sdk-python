"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateLinkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.link


class CreateLinkResponse(TypedDict):
    link: NotRequired["aws_sdk_networkmanager.types.link.Link"]
    """<p>Information about the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLinkResponse) -> dict:
    out: dict = {}
    if "link" in value:
        import aws_sdk_networkmanager.types.link

        out["Link"] = aws_sdk_networkmanager.types.link.serialize_json(value["link"])
    return out


def deserialize_json(data: dict) -> CreateLinkResponse:
    out: CreateLinkResponse = {}  # type: ignore[typeddict-item]
    if "Link" in data:
        import aws_sdk_networkmanager.types.link

        out["link"] = aws_sdk_networkmanager.types.link.deserialize_json(data["Link"])
    return out
