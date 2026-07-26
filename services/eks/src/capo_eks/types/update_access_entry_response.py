"""Generated from Smithy shape ``com.amazonaws.eks#UpdateAccessEntryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.access_entry


class UpdateAccessEntryResponse(TypedDict, closed=True):
    access_entry: NotRequired["capo_eks.types.access_entry.AccessEntry"]
    """<p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessEntryResponse) -> dict:
    out: dict = {}
    if "access_entry" in value:
        import capo_eks.types.access_entry

        out["accessEntry"] = capo_eks.types.access_entry.serialize_json(
            value["access_entry"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAccessEntryResponse:
    out: UpdateAccessEntryResponse = {}  # type: ignore[typeddict-item]
    if "accessEntry" in data:
        import capo_eks.types.access_entry

        out["access_entry"] = capo_eks.types.access_entry.deserialize_json(
            data["accessEntry"]
        )
    return out
