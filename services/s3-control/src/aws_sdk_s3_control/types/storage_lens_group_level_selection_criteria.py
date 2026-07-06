"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensGroupLevelSelectionCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.storage_lens_group_level_exclude
    import aws_sdk_s3_control.types.storage_lens_group_level_include


class StorageLensGroupLevelSelectionCriteria(TypedDict, closed=True):
    include: NotRequired[
        "aws_sdk_s3_control.types.storage_lens_group_level_include.StorageLensGroupLevelInclude"
    ]
    """<p> Indicates which Storage Lens group ARNs to include in the Storage Lens group aggregation. </p>"""
    exclude: NotRequired[
        "aws_sdk_s3_control.types.storage_lens_group_level_exclude.StorageLensGroupLevelExclude"
    ]
    """<p> Indicates which Storage Lens group ARNs to exclude from the Storage Lens group aggregation. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StorageLensGroupLevelSelectionCriteria, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "include" in value:
        import aws_sdk_s3_control.types.storage_lens_group_level_include

        aws_sdk_s3_control.types.storage_lens_group_level_include.serialize_xml(
            value["include"], el, "Include"
        )
    if "exclude" in value:
        import aws_sdk_s3_control.types.storage_lens_group_level_exclude

        aws_sdk_s3_control.types.storage_lens_group_level_exclude.serialize_xml(
            value["exclude"], el, "Exclude"
        )


def deserialize_xml(el: Element) -> StorageLensGroupLevelSelectionCriteria:
    out: StorageLensGroupLevelSelectionCriteria = {}  # type: ignore[typeddict-item]
    child_include = el.find("Include")
    if child_include is not None:
        import aws_sdk_s3_control.types.storage_lens_group_level_include

        out["include"] = (
            aws_sdk_s3_control.types.storage_lens_group_level_include.deserialize_xml(
                child_include
            )
        )
    child_exclude = el.find("Exclude")
    if child_exclude is not None:
        import aws_sdk_s3_control.types.storage_lens_group_level_exclude

        out["exclude"] = (
            aws_sdk_s3_control.types.storage_lens_group_level_exclude.deserialize_xml(
                child_exclude
            )
        )
    return out
