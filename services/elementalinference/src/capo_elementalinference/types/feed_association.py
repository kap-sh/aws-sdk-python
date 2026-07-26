"""Generated from Smithy shape ``com.amazonaws.elementalinference#FeedAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elementalinference.types.associated_resource_name


class FeedAssociation(TypedDict, closed=True):
    associated_resource_name: (
        "capo_elementalinference.types.associated_resource_name.AssociatedResourceName"
    )
    """<p>The name of the associated resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FeedAssociation) -> dict:
    out: dict = {}
    out["associatedResourceName"] = value["associated_resource_name"]
    return out


def deserialize_json(data: dict) -> FeedAssociation:
    out: FeedAssociation = {}  # type: ignore[typeddict-item]
    if "associatedResourceName" in data:
        out["associated_resource_name"] = data["associatedResourceName"]
    else:
        raise DeserializationError("FeedAssociation.associated_resource_name required")
    return out
