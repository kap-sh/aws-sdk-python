"""Generated from Smithy shape ``com.amazonaws.iot#NonCompliantResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.resource_identifier
    import aws_sdk_iot.types.resource_type
    import aws_sdk_iot.types.string_map


class NonCompliantResource(TypedDict):
    resource_type: NotRequired["aws_sdk_iot.types.resource_type.ResourceType"]
    """<p>The type of the noncompliant resource.</p>"""
    resource_identifier: NotRequired[
        "aws_sdk_iot.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>Information that identifies the noncompliant resource.</p>"""
    additional_info: NotRequired["aws_sdk_iot.types.string_map.StringMap"]
    """<p>Other information about the noncompliant resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NonCompliantResource) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import aws_sdk_iot.types.resource_type

        out["resourceType"] = aws_sdk_iot.types.resource_type.serialize_json(
            value["resource_type"]
        )
    if "resource_identifier" in value:
        import aws_sdk_iot.types.resource_identifier

        out["resourceIdentifier"] = (
            aws_sdk_iot.types.resource_identifier.serialize_json(
                value["resource_identifier"]
            )
        )
    if "additional_info" in value:
        import aws_sdk_iot.types.string_map

        out["additionalInfo"] = aws_sdk_iot.types.string_map.serialize_json(
            value["additional_info"]
        )
    return out


def deserialize_json(data: dict) -> NonCompliantResource:
    out: NonCompliantResource = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        import aws_sdk_iot.types.resource_type

        out["resource_type"] = aws_sdk_iot.types.resource_type.deserialize_json(
            data["resourceType"]
        )
    if "resourceIdentifier" in data:
        import aws_sdk_iot.types.resource_identifier

        out["resource_identifier"] = (
            aws_sdk_iot.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
        )
    if "additionalInfo" in data:
        import aws_sdk_iot.types.string_map

        out["additional_info"] = aws_sdk_iot.types.string_map.deserialize_json(
            data["additionalInfo"]
        )
    return out
