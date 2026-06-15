"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupIndexingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.fields
    import aws_sdk_iot.types.thing_group_indexing_mode


class ThingGroupIndexingConfiguration(TypedDict):
    thing_group_indexing_mode: (
        "aws_sdk_iot.types.thing_group_indexing_mode.ThingGroupIndexingMode"
    )
    """<p>Thing group indexing mode.</p>"""
    managed_fields: NotRequired["aws_sdk_iot.types.fields.Fields"]
    r"""<p>Contains fields that are indexed and whose types are already known by the Fleet Indexing service. This is an optional field. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html#managed-field\">Managed fields</a> in the <i>Amazon Web Services IoT Core Developer Guide</i>.</p> <note> <p>You can't modify managed fields by updating fleet indexing configuration.</p> </note>"""
    custom_fields: NotRequired["aws_sdk_iot.types.fields.Fields"]
    """<p>A list of thing group fields to index. This list cannot contain any managed fields. Use the GetIndexingConfiguration API to get a list of managed fields.</p> <p>Contains custom field names and their data type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingGroupIndexingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.thing_group_indexing_mode

    out["thingGroupIndexingMode"] = (
        aws_sdk_iot.types.thing_group_indexing_mode.serialize_json(
            value["thing_group_indexing_mode"]
        )
    )
    if "managed_fields" in value:
        import aws_sdk_iot.types.fields

        out["managedFields"] = aws_sdk_iot.types.fields.serialize_json(
            value["managed_fields"]
        )
    if "custom_fields" in value:
        import aws_sdk_iot.types.fields

        out["customFields"] = aws_sdk_iot.types.fields.serialize_json(
            value["custom_fields"]
        )
    return out


def deserialize_json(data: dict) -> ThingGroupIndexingConfiguration:
    out: ThingGroupIndexingConfiguration = {}  # type: ignore[typeddict-item]
    if "thingGroupIndexingMode" in data:
        import aws_sdk_iot.types.thing_group_indexing_mode

        out["thing_group_indexing_mode"] = (
            aws_sdk_iot.types.thing_group_indexing_mode.deserialize_json(
                data["thingGroupIndexingMode"]
            )
        )
    else:
        raise DeserializationError(
            "ThingGroupIndexingConfiguration.thing_group_indexing_mode required"
        )
    if "managedFields" in data:
        import aws_sdk_iot.types.fields

        out["managed_fields"] = aws_sdk_iot.types.fields.deserialize_json(
            data["managedFields"]
        )
    if "customFields" in data:
        import aws_sdk_iot.types.fields

        out["custom_fields"] = aws_sdk_iot.types.fields.deserialize_json(
            data["customFields"]
        )
    return out
