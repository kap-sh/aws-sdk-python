"""Generated from Smithy shape ``com.amazonaws.s3control#GetMultiRegionAccessPointRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.multi_region_access_point_id


class GetMultiRegionAccessPointRoutesRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>"""
    mrap: "capo_s3_control.types.multi_region_access_point_id.MultiRegionAccessPointId"
    """<p>The Multi-Region Access Point ARN.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetMultiRegionAccessPointRoutesRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetMultiRegionAccessPointRoutesRequest:
    out: GetMultiRegionAccessPointRoutesRequest = {}  # type: ignore[typeddict-item]
    return out
