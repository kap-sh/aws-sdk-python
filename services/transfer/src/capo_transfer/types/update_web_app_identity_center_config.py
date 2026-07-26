"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateWebAppIdentityCenterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.role


class UpdateWebAppIdentityCenterConfig(TypedDict, closed=True):
    role: NotRequired["capo_transfer.types.role.Role"]
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
