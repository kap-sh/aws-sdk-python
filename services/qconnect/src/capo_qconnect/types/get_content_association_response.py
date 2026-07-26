"""Generated from Smithy shape ``com.amazonaws.qconnect#GetContentAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.content_association_data


class GetContentAssociationResponse(TypedDict, closed=True):
    content_association: NotRequired[
        "capo_qconnect.types.content_association_data.ContentAssociationData"
    ]
    """<p>The association between Amazon Q in Connect content and another resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContentAssociationResponse) -> dict:
    out: dict = {}
    if "content_association" in value:
        import capo_qconnect.types.content_association_data

        out["contentAssociation"] = (
            capo_qconnect.types.content_association_data.serialize_json(
                value["content_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetContentAssociationResponse:
    out: GetContentAssociationResponse = {}  # type: ignore[typeddict-item]
    if "contentAssociation" in data:
        import capo_qconnect.types.content_association_data

        out["content_association"] = (
            capo_qconnect.types.content_association_data.deserialize_json(
                data["contentAssociation"]
            )
        )
    return out
