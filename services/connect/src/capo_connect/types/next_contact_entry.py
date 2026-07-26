"""Generated from Smithy shape ``com.amazonaws.connect#NextContactEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_contact_metadata
    import capo_connect.types.next_contact_type


class NextContactEntry(TypedDict, closed=True):
    type: NotRequired["capo_connect.types.next_contact_type.NextContactType"]
    """<p> The type of the next contact entry. </p>"""
    next_contact_metadata: NotRequired[
        "capo_connect.types.next_contact_metadata.NextContactMetadata"
    ]
    """<p> Metadata for the next contact entry. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NextContactEntry) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_connect.types.next_contact_type

        out["Type"] = capo_connect.types.next_contact_type.serialize_json(value["type"])
    if "next_contact_metadata" in value:
        import capo_connect.types.next_contact_metadata

        out["NextContactMetadata"] = (
            capo_connect.types.next_contact_metadata.serialize_json(
                value["next_contact_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> NextContactEntry:
    out: NextContactEntry = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_connect.types.next_contact_type

        out["type"] = capo_connect.types.next_contact_type.deserialize_json(
            data["Type"]
        )
    if "NextContactMetadata" in data:
        import capo_connect.types.next_contact_metadata

        out["next_contact_metadata"] = (
            capo_connect.types.next_contact_metadata.deserialize_json(
                data["NextContactMetadata"]
            )
        )
    return out
