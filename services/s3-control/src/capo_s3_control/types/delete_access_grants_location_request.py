"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteAccessGrantsLocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.access_grants_location_id
    import capo_s3_control.types.account_id


class DeleteAccessGrantsLocationRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>"""
    access_grants_location_id: (
        "capo_s3_control.types.access_grants_location_id.AccessGrantsLocationId"
    )
    """<p>The ID of the registered location that you are deregistering from your S3 Access Grants instance. S3 Access Grants assigned this ID when you registered the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteAccessGrantsLocationRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteAccessGrantsLocationRequest:
    out: DeleteAccessGrantsLocationRequest = {}  # type: ignore[typeddict-item]
    return out
