"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#IssueDetected``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.character_offsets


class IssueDetected(TypedDict, closed=True):
    character_offsets: NotRequired[
        "capo_connect_contact_lens.types.character_offsets.CharacterOffsets"
    ]
    """<p>The offset for when the issue was detected in the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IssueDetected) -> dict:
    out: dict = {}
    if "character_offsets" in value:
        import capo_connect_contact_lens.types.character_offsets

        out["CharacterOffsets"] = (
            capo_connect_contact_lens.types.character_offsets.serialize_json(
                value["character_offsets"]
            )
        )
    return out


def deserialize_json(data: dict) -> IssueDetected:
    out: IssueDetected = {}  # type: ignore[typeddict-item]
    if "CharacterOffsets" in data:
        import capo_connect_contact_lens.types.character_offsets

        out["character_offsets"] = (
            capo_connect_contact_lens.types.character_offsets.deserialize_json(
                data["CharacterOffsets"]
            )
        )
    return out
