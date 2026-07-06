"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ResourceConflict``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.resource_type


class ResourceConflict(TypedDict, closed=True):
    resource_id: "str"
    """<p>The unique identifier of the resource involved in a conflict.</p>"""
    resource_type: "aws_sdk_verifiedpermissions.types.resource_type.ResourceType"
    """<p>The type of the resource involved in a conflict.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceConflict) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    import aws_sdk_verifiedpermissions.types.resource_type

    out["resourceType"] = (
        aws_sdk_verifiedpermissions.types.resource_type.serialize_aws_json_1_0(
            value["resource_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceConflict:
    out: ResourceConflict = {}  # type: ignore[typeddict-item]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ResourceConflict.resource_id required")
    if "resourceType" in data:
        import aws_sdk_verifiedpermissions.types.resource_type

        out["resource_type"] = (
            aws_sdk_verifiedpermissions.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError("ResourceConflict.resource_type required")
    return out
