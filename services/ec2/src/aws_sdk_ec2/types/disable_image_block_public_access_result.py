"""Generated from Smithy shape ``com.amazonaws.ec2#DisableImageBlockPublicAccessResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_block_public_access_disabled_state


class DisableImageBlockPublicAccessResult(TypedDict):
    image_block_public_access_state: NotRequired[
        "aws_sdk_ec2.types.image_block_public_access_disabled_state.ImageBlockPublicAccessDisabledState"
    ]
    """<p>Returns <code>unblocked</code> if the request succeeds; otherwise, it returns an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableImageBlockPublicAccessResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "image_block_public_access_state" in value:
        import aws_sdk_ec2.types.image_block_public_access_disabled_state

        aws_sdk_ec2.types.image_block_public_access_disabled_state.serialize_ec2_query(
            value["image_block_public_access_state"],
            pairs,
            f"{prefix}.ImageBlockPublicAccessState",
        )


def deserialize_ec2_query(el: Element) -> DisableImageBlockPublicAccessResult:
    out: DisableImageBlockPublicAccessResult = {}  # type: ignore[typeddict-item]
    child_image_block_public_access_state = el.find("ImageBlockPublicAccessState")
    if child_image_block_public_access_state is not None:
        import aws_sdk_ec2.types.image_block_public_access_disabled_state

        out["image_block_public_access_state"] = (
            aws_sdk_ec2.types.image_block_public_access_disabled_state.deserialize_ec2_query(
                child_image_block_public_access_state
            )
        )
    return out
