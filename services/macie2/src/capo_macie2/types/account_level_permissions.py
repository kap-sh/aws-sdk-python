"""Generated from Smithy shape ``com.amazonaws.macie2#AccountLevelPermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.block_public_access


class AccountLevelPermissions(TypedDict, closed=True):
    block_public_access: NotRequired[
        "capo_macie2.types.block_public_access.BlockPublicAccess"
    ]
    """<p>The block public access settings for the Amazon Web Services account that owns the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountLevelPermissions) -> dict:
    out: dict = {}
    if "block_public_access" in value:
        import capo_macie2.types.block_public_access

        out["blockPublicAccess"] = capo_macie2.types.block_public_access.serialize_json(
            value["block_public_access"]
        )
    return out


def deserialize_json(data: dict) -> AccountLevelPermissions:
    out: AccountLevelPermissions = {}  # type: ignore[typeddict-item]
    if "blockPublicAccess" in data:
        import capo_macie2.types.block_public_access

        out["block_public_access"] = (
            capo_macie2.types.block_public_access.deserialize_json(
                data["blockPublicAccess"]
            )
        )
    return out
