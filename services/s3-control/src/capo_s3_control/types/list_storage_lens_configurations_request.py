"""Generated from Smithy shape ``com.amazonaws.s3control#ListStorageLensConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.continuation_token


class ListStorageLensConfigurationsRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The account ID of the requester.</p>"""
    next_token: NotRequired[
        "capo_s3_control.types.continuation_token.ContinuationToken"
    ]
    """<p>A pagination token to request the next page of results.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListStorageLensConfigurationsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListStorageLensConfigurationsRequest:
    out: ListStorageLensConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
