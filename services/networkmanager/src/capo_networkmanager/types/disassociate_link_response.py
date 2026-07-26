"""Generated from Smithy shape ``com.amazonaws.networkmanager#DisassociateLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.link_association


class DisassociateLinkResponse(TypedDict, closed=True):
    link_association: NotRequired[
        "capo_networkmanager.types.link_association.LinkAssociation"
    ]
    """<p>Information about the link association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateLinkResponse) -> dict:
    out: dict = {}
    if "link_association" in value:
        import capo_networkmanager.types.link_association

        out["LinkAssociation"] = (
            capo_networkmanager.types.link_association.serialize_json(
                value["link_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisassociateLinkResponse:
    out: DisassociateLinkResponse = {}  # type: ignore[typeddict-item]
    if "LinkAssociation" in data:
        import capo_networkmanager.types.link_association

        out["link_association"] = (
            capo_networkmanager.types.link_association.deserialize_json(
                data["LinkAssociation"]
            )
        )
    return out
