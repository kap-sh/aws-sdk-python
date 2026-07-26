"""Generated from Smithy shape ``com.amazonaws.s3control#ListStorageLensGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.continuation_token


class ListStorageLensGroupsRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID that owns the Storage Lens groups. </p>"""
    next_token: NotRequired[
        "capo_s3_control.types.continuation_token.ContinuationToken"
    ]
    """<p>The token for the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListStorageLensGroupsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListStorageLensGroupsRequest:
    out: ListStorageLensGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
