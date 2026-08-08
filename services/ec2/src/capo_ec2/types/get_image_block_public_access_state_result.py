"""Generated from Smithy shape ``com.amazonaws.ec2#GetImageBlockPublicAccessStateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.managed_by
    import capo_ec2.types.string


class GetImageBlockPublicAccessStateResult(TypedDict, closed=True):
    image_block_public_access_state: NotRequired["capo_ec2.types.string.String"]
    """<p>The current state of block public access for AMIs at the account level in the specified Amazon Web Services Region.</p> <p>Possible values:</p> <ul> <li> <p> <code>block-new-sharing</code> - Any attempt to publicly share your AMIs in the specified Region is blocked.</p> </li> <li> <p> <code>unblocked</code> - Your AMIs in the specified Region can be publicly shared.</p> </li> </ul>"""
    managed_by: NotRequired["capo_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the state for block public access for AMIs. Possible values include:</p> <ul> <li> <p> <code>account</code> - The state is managed by the account.</p> </li> <li> <p> <code>declarative-policy</code> - The state is managed by a declarative policy and can't be modified by the account.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetImageBlockPublicAccessStateResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_block_public_access_state" in value:
        pairs.append(
            (
                f"{key_prefix}ImageBlockPublicAccessState",
                str(value["image_block_public_access_state"]),
            )
        )
    if "managed_by" in value:
        import capo_ec2.types.managed_by

        capo_ec2.types.managed_by.serialize_ec2_query(
            value["managed_by"], pairs, f"{key_prefix}ManagedBy"
        )


def deserialize_ec2_query(el: Element) -> GetImageBlockPublicAccessStateResult:
    out: GetImageBlockPublicAccessStateResult = {}  # type: ignore[typeddict-item]
    child_image_block_public_access_state = el.find("imageBlockPublicAccessState")
    if child_image_block_public_access_state is not None:
        out["image_block_public_access_state"] = str(
            child_image_block_public_access_state.text or ""
        )
    child_managed_by = el.find("managedBy")
    if child_managed_by is not None:
        import capo_ec2.types.managed_by

        out["managed_by"] = capo_ec2.types.managed_by.deserialize_ec2_query(
            child_managed_by
        )
    return out
