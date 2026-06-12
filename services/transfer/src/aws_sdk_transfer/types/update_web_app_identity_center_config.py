"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateWebAppIdentityCenterConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transfer.types.role


class UpdateWebAppIdentityCenterConfig(TypedDict):
    role: NotRequired["aws_sdk_transfer.types.role.Role"]
    """<p>The IAM role used to access IAM Identity Center.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebAppIdentityCenterConfig) -> dict:
    out: dict = {}
    if "role" in value:
        out["Role"] = value["role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWebAppIdentityCenterConfig:
    out: UpdateWebAppIdentityCenterConfig = {}  # type: ignore[typeddict-item]
    if "Role" in data:
        out["role"] = data["Role"]
    return out
