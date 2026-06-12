"""Generated from Smithy shape ``com.amazonaws.greengrass#Resource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.resource_data_container


class Resource(TypedDict):
    id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The resource ID, used to refer to a resource in the Lambda function configuration. Max length is 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This must be unique within a Greengrass group."""
    name: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The descriptive resource name, which is displayed on the AWS IoT Greengrass console. Max length 128 characters with pattern ''[a-zA-Z0-9:_-]+''. This must be unique within a Greengrass group."""
    resource_data_container: NotRequired[
        "aws_sdk_greengrass.types.resource_data_container.ResourceDataContainer"
    ]
    """A container of data for all resource types."""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "resource_data_container" in value:
        import aws_sdk_greengrass.types.resource_data_container

        out["ResourceDataContainer"] = (
            aws_sdk_greengrass.types.resource_data_container.serialize_json(
                value["resource_data_container"]
            )
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ResourceDataContainer" in data:
        import aws_sdk_greengrass.types.resource_data_container

        out["resource_data_container"] = (
            aws_sdk_greengrass.types.resource_data_container.deserialize_json(
                data["ResourceDataContainer"]
            )
        )
    return out
