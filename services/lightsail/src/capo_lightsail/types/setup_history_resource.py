"""Generated from Smithy shape ``com.amazonaws.lightsail#SetupHistoryResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type


class SetupHistoryResource(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the Lightsail resource.</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the Lightsail resource.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp for when the resource was created.</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type. For example, <code>Instance</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetupHistoryResource) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetupHistoryResource:
    out: SetupHistoryResource = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "location" in data:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if "resourceType" in data:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    return out
