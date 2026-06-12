"""Generated from Smithy shape ``com.amazonaws.directoryservice#Attribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.attribute_name
    import aws_sdk_directory_service.types.attribute_value


class Attribute(TypedDict):
    name: NotRequired["aws_sdk_directory_service.types.attribute_name.AttributeName"]
    """<p>The name of the attribute.</p>"""
    value: NotRequired["aws_sdk_directory_service.types.attribute_value.AttributeValue"]
    """<p>The value of the attribute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attribute) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
