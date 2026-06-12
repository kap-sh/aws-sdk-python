"""Generated from Smithy shape ``com.amazonaws.iot#GetIndexingConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_group_indexing_configuration
    import aws_sdk_iot.types.thing_indexing_configuration


class GetIndexingConfigurationResponse(TypedDict):
    thing_indexing_configuration: NotRequired[
        "aws_sdk_iot.types.thing_indexing_configuration.ThingIndexingConfiguration"
    ]
    """<p>Thing indexing configuration.</p>"""
    thing_group_indexing_configuration: NotRequired[
        "aws_sdk_iot.types.thing_group_indexing_configuration.ThingGroupIndexingConfiguration"
    ]
    """<p>The index configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexingConfigurationResponse) -> dict:
    out: dict = {}
    if "thing_indexing_configuration" in value:
        import aws_sdk_iot.types.thing_indexing_configuration

        out["thingIndexingConfiguration"] = (
            aws_sdk_iot.types.thing_indexing_configuration.serialize_json(
                value["thing_indexing_configuration"]
            )
        )
    if "thing_group_indexing_configuration" in value:
        import aws_sdk_iot.types.thing_group_indexing_configuration

        out["thingGroupIndexingConfiguration"] = (
            aws_sdk_iot.types.thing_group_indexing_configuration.serialize_json(
                value["thing_group_indexing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetIndexingConfigurationResponse:
    out: GetIndexingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "thingIndexingConfiguration" in data:
        import aws_sdk_iot.types.thing_indexing_configuration

        out["thing_indexing_configuration"] = (
            aws_sdk_iot.types.thing_indexing_configuration.deserialize_json(
                data["thingIndexingConfiguration"]
            )
        )
    if "thingGroupIndexingConfiguration" in data:
        import aws_sdk_iot.types.thing_group_indexing_configuration

        out["thing_group_indexing_configuration"] = (
            aws_sdk_iot.types.thing_group_indexing_configuration.deserialize_json(
                data["thingGroupIndexingConfiguration"]
            )
        )
    return out
