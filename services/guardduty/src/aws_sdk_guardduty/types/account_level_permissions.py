"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountLevelPermissions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.block_public_access


class AccountLevelPermissions(TypedDict):
    block_public_access: NotRequired[
        "aws_sdk_guardduty.types.block_public_access.BlockPublicAccess"
    ]
    """<p>Describes the S3 Block Public Access settings of the bucket's parent account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountLevelPermissions) -> dict:
    out: dict = {}
    if "block_public_access" in value:
        import aws_sdk_guardduty.types.block_public_access

        out["blockPublicAccess"] = (
            aws_sdk_guardduty.types.block_public_access.serialize_json(
                value["block_public_access"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountLevelPermissions:
    out: AccountLevelPermissions = {}  # type: ignore[typeddict-item]
    if "blockPublicAccess" in data:
        import aws_sdk_guardduty.types.block_public_access

        out["block_public_access"] = (
            aws_sdk_guardduty.types.block_public_access.deserialize_json(
                data["blockPublicAccess"]
            )
        )
    return out
