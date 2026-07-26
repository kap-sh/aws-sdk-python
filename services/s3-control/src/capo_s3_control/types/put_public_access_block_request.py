"""Generated from Smithy shape ``com.amazonaws.s3control#PutPublicAccessBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.public_access_block_configuration


class PutPublicAccessBlockRequest(TypedDict, closed=True):
    public_access_block_configuration: "capo_s3_control.types.public_access_block_configuration.PublicAccessBlockConfiguration"
    """<p>The <code>PublicAccessBlock</code> configuration that you want to apply to the specified Amazon Web Services account.</p>"""
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The account ID for the Amazon Web Services account whose <code>PublicAccessBlock</code> configuration you want to set.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutPublicAccessBlockRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.public_access_block_configuration

    capo_s3_control.types.public_access_block_configuration.serialize_xml(
        value["public_access_block_configuration"], el, "PublicAccessBlockConfiguration"
    )


def deserialize_xml(el: Element) -> PutPublicAccessBlockRequest:
    out: PutPublicAccessBlockRequest = {}  # type: ignore[typeddict-item]
    child_public_access_block_configuration = el.find("PublicAccessBlockConfiguration")
    if child_public_access_block_configuration is not None:
        import capo_s3_control.types.public_access_block_configuration

        out["public_access_block_configuration"] = (
            capo_s3_control.types.public_access_block_configuration.deserialize_xml(
                child_public_access_block_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutPublicAccessBlockRequest.public_access_block_configuration required"
        )
    return out
