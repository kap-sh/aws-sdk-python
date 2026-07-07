"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#EntityFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.entity_filter_name
    import aws_sdk_iotthingsgraph.types.entity_filter_values


class EntityFilter(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_iotthingsgraph.types.entity_filter_name.EntityFilterName"
    ]
    """<p>The name of the entity search filter field. <code>REFERENCED_ENTITY_ID</code> filters on entities that are used by the entity in the result set. For example, you can filter on the ID of a property that is used in a state.</p>"""
    value: NotRequired[
        "aws_sdk_iotthingsgraph.types.entity_filter_values.EntityFilterValues"
    ]
    """<p>An array of string values for the search filter field. Multiple values function as AND criteria in the search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_iotthingsgraph.types.entity_filter_name

        out["name"] = (
            aws_sdk_iotthingsgraph.types.entity_filter_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "value" in value:
        import aws_sdk_iotthingsgraph.types.entity_filter_values

        out["value"] = (
            aws_sdk_iotthingsgraph.types.entity_filter_values.serialize_aws_json_1_1(
                value["value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityFilter:
    out: EntityFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_iotthingsgraph.types.entity_filter_name

        out["name"] = (
            aws_sdk_iotthingsgraph.types.entity_filter_name.deserialize_aws_json_1_1(
                data["name"]
            )
        )
    if "value" in data:
        import aws_sdk_iotthingsgraph.types.entity_filter_values

        out["value"] = (
            aws_sdk_iotthingsgraph.types.entity_filter_values.deserialize_aws_json_1_1(
                data["value"]
            )
        )
    return out
