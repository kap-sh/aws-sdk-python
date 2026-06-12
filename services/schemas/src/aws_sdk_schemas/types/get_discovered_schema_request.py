"""Generated from Smithy shape ``com.amazonaws.schemas#GetDiscoveredSchemaRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__list_of_get_discovered_schema_version_item_input
    import aws_sdk_schemas.types.type


class GetDiscoveredSchemaRequest(TypedDict):
    events: NotRequired[
        "aws_sdk_schemas.types.__list_of_get_discovered_schema_version_item_input.__listOfGetDiscoveredSchemaVersionItemInput"
    ]
    """<p>An array of strings where each string is a JSON event. These are the events that were used to generate the schema. The array includes a single type of event and has a maximum size of 10 events.</p>"""
    type: NotRequired["aws_sdk_schemas.types.type.Type"]
    """<p>The type of event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDiscoveredSchemaRequest) -> dict:
    out: dict = {}
    if "events" in value:
        import aws_sdk_schemas.types.__list_of_get_discovered_schema_version_item_input

        out["Events"] = (
            aws_sdk_schemas.types.__list_of_get_discovered_schema_version_item_input.serialize_json(
                value["events"]
            )
        )
    if "type" in value:
        import aws_sdk_schemas.types.type

        out["Type"] = aws_sdk_schemas.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> GetDiscoveredSchemaRequest:
    out: GetDiscoveredSchemaRequest = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import aws_sdk_schemas.types.__list_of_get_discovered_schema_version_item_input

        out["events"] = (
            aws_sdk_schemas.types.__list_of_get_discovered_schema_version_item_input.deserialize_json(
                data["Events"]
            )
        )
    if "Type" in data:
        import aws_sdk_schemas.types.type

        out["type"] = aws_sdk_schemas.types.type.deserialize_json(data["Type"])
    return out
