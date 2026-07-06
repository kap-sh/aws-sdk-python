"""Generated from Smithy shape ``com.amazonaws.migrationhub#ResourceAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.resource_attribute_type
    import aws_sdk_migration_hub.types.resource_attribute_value


class ResourceAttribute(TypedDict, closed=True):
    type: "aws_sdk_migration_hub.types.resource_attribute_type.ResourceAttributeType"
    """<p>Type of resource.</p>"""
    value: "aws_sdk_migration_hub.types.resource_attribute_value.ResourceAttributeValue"
    """<p>Value of the resource type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAttribute) -> dict:
    out: dict = {}
    import aws_sdk_migration_hub.types.resource_attribute_type

    out["Type"] = (
        aws_sdk_migration_hub.types.resource_attribute_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceAttribute:
    out: ResourceAttribute = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_migration_hub.types.resource_attribute_type

        out["type"] = (
            aws_sdk_migration_hub.types.resource_attribute_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("ResourceAttribute.type required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("ResourceAttribute.value required")
    return out
