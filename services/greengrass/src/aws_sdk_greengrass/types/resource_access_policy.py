"""Generated from Smithy shape ``com.amazonaws.greengrass#ResourceAccessPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.permission


class ResourceAccessPolicy(TypedDict, closed=True):
    permission: NotRequired["aws_sdk_greengrass.types.permission.Permission"]
    """The permissions that the Lambda function has to the resource. Can be one of ''rw'' (read/write) or ''ro'' (read-only)."""
    resource_id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ID of the resource. (This ID is assigned to the resource when you create the resource definiton.)"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceAccessPolicy) -> dict:
    out: dict = {}
    if "permission" in value:
        import aws_sdk_greengrass.types.permission

        out["Permission"] = aws_sdk_greengrass.types.permission.serialize_json(
            value["permission"]
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> ResourceAccessPolicy:
    out: ResourceAccessPolicy = {}  # type: ignore[typeddict-item]
    if "Permission" in data:
        import aws_sdk_greengrass.types.permission

        out["permission"] = aws_sdk_greengrass.types.permission.deserialize_json(
            data["Permission"]
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    return out
