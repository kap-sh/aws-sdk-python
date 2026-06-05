"""Generated from Smithy shape ``com.amazonaws.ec2#EnableImageBlockPublicAccessRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_block_public_access_enabled_state


class EnableImageBlockPublicAccessRequest(TypedDict):
    image_block_public_access_state: NotRequired[
        "aws_sdk_ec2.types.image_block_public_access_enabled_state.ImageBlockPublicAccessEnabledState"
    ]
    """<p>Specify <code>block-new-sharing</code> to enable block public access for AMIs at the account level in the specified Region. This will block any attempt to publicly share your AMIs in the specified Region.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableImageBlockPublicAccessRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "image_block_public_access_state" in value:
        import aws_sdk_ec2.types.image_block_public_access_enabled_state

        aws_sdk_ec2.types.image_block_public_access_enabled_state.serialize_ec2_query(
            value["image_block_public_access_state"],
            pairs,
            f"{prefix}.ImageBlockPublicAccessState",
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> EnableImageBlockPublicAccessRequest:
    out: EnableImageBlockPublicAccessRequest = {}  # type: ignore[typeddict-item]
    child_image_block_public_access_state = el.find("ImageBlockPublicAccessState")
    if child_image_block_public_access_state is not None:
        import aws_sdk_ec2.types.image_block_public_access_enabled_state

        out["image_block_public_access_state"] = (
            aws_sdk_ec2.types.image_block_public_access_enabled_state.deserialize_ec2_query(
                child_image_block_public_access_state
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
