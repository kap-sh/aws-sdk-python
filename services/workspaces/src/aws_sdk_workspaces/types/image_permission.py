"""Generated from Smithy shape ``com.amazonaws.workspaces#ImagePermission``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.aws_account


class ImagePermission(TypedDict):
    shared_account_id: NotRequired["aws_sdk_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the Amazon Web Services account that an image has been shared with.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImagePermission) -> dict:
    out: dict = {}
    if "shared_account_id" in value:
        out["SharedAccountId"] = value["shared_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImagePermission:
    out: ImagePermission = {}  # type: ignore[typeddict-item]
    if "SharedAccountId" in data:
        out["shared_account_id"] = data["SharedAccountId"]
    return out
