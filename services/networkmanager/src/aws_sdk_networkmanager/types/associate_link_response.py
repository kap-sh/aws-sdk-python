"""Generated from Smithy shape ``com.amazonaws.networkmanager#AssociateLinkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.link_association


class AssociateLinkResponse(TypedDict):
    link_association: NotRequired[
        "aws_sdk_networkmanager.types.link_association.LinkAssociation"
    ]
    """<p>The link association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateLinkResponse) -> dict:
    out: dict = {}
    if "link_association" in value:
        import aws_sdk_networkmanager.types.link_association

        out["LinkAssociation"] = (
            aws_sdk_networkmanager.types.link_association.serialize_json(
                value["link_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateLinkResponse:
    out: AssociateLinkResponse = {}  # type: ignore[typeddict-item]
    if "LinkAssociation" in data:
        import aws_sdk_networkmanager.types.link_association

        out["link_association"] = (
            aws_sdk_networkmanager.types.link_association.deserialize_json(
                data["LinkAssociation"]
            )
        )
    return out
