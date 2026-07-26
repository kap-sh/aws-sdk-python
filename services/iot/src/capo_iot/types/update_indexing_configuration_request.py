"""Generated from Smithy shape ``com.amazonaws.iot#UpdateIndexingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.thing_group_indexing_configuration
    import capo_iot.types.thing_indexing_configuration


class UpdateIndexingConfigurationRequest(TypedDict, closed=True):
    thing_indexing_configuration: NotRequired[
        "capo_iot.types.thing_indexing_configuration.ThingIndexingConfiguration"
    ]
    """<p>Thing indexing configuration.</p>"""
    thing_group_indexing_configuration: NotRequired[
        "capo_iot.types.thing_group_indexing_configuration.ThingGroupIndexingConfiguration"
    ]
    """<p>Thing group indexing configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexingConfigurationRequest) -> dict:
    out: dict = {}
    if "thing_indexing_configuration" in value:
        import capo_iot.types.thing_indexing_configuration

        out["thingIndexingConfiguration"] = (
            capo_iot.types.thing_indexing_configuration.serialize_json(
                value["thing_indexing_configuration"]
            )
        )
    if "thing_group_indexing_configuration" in value:
        import capo_iot.types.thing_group_indexing_configuration

        out["thingGroupIndexingConfiguration"] = (
            capo_iot.types.thing_group_indexing_configuration.serialize_json(
                value["thing_group_indexing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateIndexingConfigurationRequest:
    out: UpdateIndexingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "thingIndexingConfiguration" in data:
        import capo_iot.types.thing_indexing_configuration

        out["thing_indexing_configuration"] = (
            capo_iot.types.thing_indexing_configuration.deserialize_json(
                data["thingIndexingConfiguration"]
            )
        )
    if "thingGroupIndexingConfiguration" in data:
        import capo_iot.types.thing_group_indexing_configuration

        out["thing_group_indexing_configuration"] = (
            capo_iot.types.thing_group_indexing_configuration.deserialize_json(
                data["thingGroupIndexingConfiguration"]
            )
        )
    return out
