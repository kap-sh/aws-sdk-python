"""Generated from Smithy shape ``com.amazonaws.aiops#CrossAccountConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_aiops.types.role_arn


class CrossAccountConfiguration(TypedDict, closed=True):
    source_role_arn: NotRequired["aws_sdk_aiops.types.role_arn.RoleArn"]
    """<p>The ARN of an existing role which will be used to do investigations on your behalf. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossAccountConfiguration) -> dict:
    out: dict = {}
    if "source_role_arn" in value:
        out["sourceRoleArn"] = value["source_role_arn"]
    return out


def deserialize_json(data: dict) -> CrossAccountConfiguration:
    out: CrossAccountConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceRoleArn" in data:
        out["source_role_arn"] = data["sourceRoleArn"]
    return out
