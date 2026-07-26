"""Generated from Smithy shape ``com.amazonaws.s3control#GetAccessPointForObjectLambdaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.object_lambda_access_point_name


class GetAccessPointForObjectLambdaRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The account ID for the account that owns the specified Object Lambda Access Point.</p>"""
    name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName"
    """<p>The name of the Object Lambda Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetAccessPointForObjectLambdaRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetAccessPointForObjectLambdaRequest:
    out: GetAccessPointForObjectLambdaRequest = {}  # type: ignore[typeddict-item]
    return out
