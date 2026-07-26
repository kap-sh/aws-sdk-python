"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationChangeSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.auto_approved_change_type_list


class CollaborationChangeSpecification(TypedDict, closed=True):
    auto_approved_change_types: NotRequired[
        "capo_cleanrooms.types.auto_approved_change_type_list.AutoApprovedChangeTypeList"
    ]
    """<p>Defines requested updates to properties of the collaboration. Currently, this only supports modifying which change types are auto-approved for the collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationChangeSpecification) -> dict:
    out: dict = {}
    if "auto_approved_change_types" in value:
        import capo_cleanrooms.types.auto_approved_change_type_list

        out["autoApprovedChangeTypes"] = (
            capo_cleanrooms.types.auto_approved_change_type_list.serialize_json(
                value["auto_approved_change_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> CollaborationChangeSpecification:
    out: CollaborationChangeSpecification = {}  # type: ignore[typeddict-item]
    if "autoApprovedChangeTypes" in data:
        import capo_cleanrooms.types.auto_approved_change_type_list

        out["auto_approved_change_types"] = (
            capo_cleanrooms.types.auto_approved_change_type_list.deserialize_json(
                data["autoApprovedChangeTypes"]
            )
        )
    return out
