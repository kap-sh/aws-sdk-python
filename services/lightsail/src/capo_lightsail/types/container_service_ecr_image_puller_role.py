"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceECRImagePullerRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.string


class ContainerServiceECRImagePullerRole(TypedDict, closed=True):
    is_active: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether the role is activated.</p>"""
    principal_arn: NotRequired["capo_lightsail.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the role, if it is activated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceECRImagePullerRole) -> dict:
    out: dict = {}
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerServiceECRImagePullerRole:
    out: ContainerServiceECRImagePullerRole = {}  # type: ignore[typeddict-item]
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    return out
