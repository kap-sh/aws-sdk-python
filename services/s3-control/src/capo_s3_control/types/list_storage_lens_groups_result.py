"""Generated from Smithy shape ``com.amazonaws.s3control#ListStorageLensGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.continuation_token
    import capo_s3_control.types.storage_lens_group_list


class ListStorageLensGroupsResult(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_s3_control.types.continuation_token.ContinuationToken"
    ]
    """<p> If <code>NextToken</code> is returned, there are more Storage Lens groups results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""
    storage_lens_group_list: NotRequired[
        "capo_s3_control.types.storage_lens_group_list.StorageLensGroupList"
    ]
    """<p> The list of Storage Lens groups that exist in the specified home Region. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListStorageLensGroupsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])
    if "storage_lens_group_list" in value:
        import capo_s3_control.types.storage_lens_group_list

        capo_s3_control.types.storage_lens_group_list.serialize_xml_flat(
            value["storage_lens_group_list"], el, "StorageLensGroup"
        )


def deserialize_xml(el: Element) -> ListStorageLensGroupsResult:
    out: ListStorageLensGroupsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("StorageLensGroup") is not None:
        import capo_s3_control.types.storage_lens_group_list

        out["storage_lens_group_list"] = (
            capo_s3_control.types.storage_lens_group_list.deserialize_xml_flat(
                el, "StorageLensGroup"
            )
        )
    return out
