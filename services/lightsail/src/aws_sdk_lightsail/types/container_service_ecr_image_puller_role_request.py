"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceECRImagePullerRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean


class ContainerServiceECRImagePullerRoleRequest(TypedDict, closed=True):
    is_active: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether to activate the role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceECRImagePullerRoleRequest) -> dict:
    out: dict = {}
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServiceECRImagePullerRoleRequest:
    out: ContainerServiceECRImagePullerRoleRequest = {}  # type: ignore[typeddict-item]
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    return out
