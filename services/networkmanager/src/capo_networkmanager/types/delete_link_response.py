"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.link


class DeleteLinkResponse(TypedDict, closed=True):
    link: NotRequired["capo_networkmanager.types.link.Link"]
    """<p>Information about the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLinkResponse) -> dict:
    out: dict = {}
    if "link" in value:
        import capo_networkmanager.types.link

        out["Link"] = capo_networkmanager.types.link.serialize_json(value["link"])
    return out


def deserialize_json(data: dict) -> DeleteLinkResponse:
    out: DeleteLinkResponse = {}  # type: ignore[typeddict-item]
    if "Link" in data:
        import capo_networkmanager.types.link

        out["link"] = capo_networkmanager.types.link.deserialize_json(data["Link"])
    return out
