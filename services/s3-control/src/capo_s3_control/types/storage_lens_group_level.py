"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensGroupLevel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.storage_lens_group_level_selection_criteria


class StorageLensGroupLevel(TypedDict, closed=True):
    selection_criteria: NotRequired[
        "capo_s3_control.types.storage_lens_group_level_selection_criteria.StorageLensGroupLevelSelectionCriteria"
    ]
    """<p> Indicates which Storage Lens group ARNs to include or exclude in the Storage Lens group aggregation. If this value is left null, then all Storage Lens groups are selected. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: StorageLensGroupLevel, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "selection_criteria" in value:
        import capo_s3_control.types.storage_lens_group_level_selection_criteria

        capo_s3_control.types.storage_lens_group_level_selection_criteria.serialize_xml(
            value["selection_criteria"], el, "SelectionCriteria"
        )


def deserialize_xml(el: Element) -> StorageLensGroupLevel:
    out: StorageLensGroupLevel = {}  # type: ignore[typeddict-item]
    child_selection_criteria = el.find("SelectionCriteria")
    if child_selection_criteria is not None:
        import capo_s3_control.types.storage_lens_group_level_selection_criteria

        out["selection_criteria"] = (
            capo_s3_control.types.storage_lens_group_level_selection_criteria.deserialize_xml(
                child_selection_criteria
            )
        )
    return out
