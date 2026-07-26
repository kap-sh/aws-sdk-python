"""Generated from Smithy shape ``com.amazonaws.rds#CharacterSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class CharacterSet(TypedDict, closed=True):
    character_set_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the character set.</p>"""
    character_set_description: NotRequired["capo_rds.types.string.String"]
    """<p>The description of the character set.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CharacterSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "character_set_name" in value:
        pairs.append((f"{prefix}.CharacterSetName", str(value["character_set_name"])))
    if "character_set_description" in value:
        pairs.append(
            (
                f"{prefix}.CharacterSetDescription",
                str(value["character_set_description"]),
            )
        )


def deserialize_query(el: Element) -> CharacterSet:
    out: CharacterSet = {}  # type: ignore[typeddict-item]
    child_character_set_name = el.find("CharacterSetName")
    if child_character_set_name is not None:
        out["character_set_name"] = str(child_character_set_name.text or "")
    child_character_set_description = el.find("CharacterSetDescription")
    if child_character_set_description is not None:
        out["character_set_description"] = str(
            child_character_set_description.text or ""
        )
    return out
