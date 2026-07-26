"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteAccessGrantsInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id


class DeleteAccessGrantsInstanceRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteAccessGrantsInstanceRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteAccessGrantsInstanceRequest:
    out: DeleteAccessGrantsInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
