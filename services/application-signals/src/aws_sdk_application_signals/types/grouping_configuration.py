"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GroupingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.grouping_attribute_definitions


class GroupingConfiguration(TypedDict):
    grouping_attribute_definitions: "aws_sdk_application_signals.types.grouping_attribute_definitions.GroupingAttributeDefinitions"
    """<p>An array of grouping attribute definitions that specify how services should be grouped based on various attributes and source keys.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when this grouping configuration was last updated. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.grouping_attribute_definitions

    out["GroupingAttributeDefinitions"] = (
        aws_sdk_application_signals.types.grouping_attribute_definitions.serialize_json(
            value["grouping_attribute_definitions"]
        )
    )
    import aws_sdk_application_signals.types._prelude.timestamp

    out["UpdatedAt"] = (
        aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> GroupingConfiguration:
    out: GroupingConfiguration = {}  # type: ignore[typeddict-item]
    if "GroupingAttributeDefinitions" in data:
        import aws_sdk_application_signals.types.grouping_attribute_definitions

        out["grouping_attribute_definitions"] = (
            aws_sdk_application_signals.types.grouping_attribute_definitions.deserialize_json(
                data["GroupingAttributeDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "GroupingConfiguration.grouping_attribute_definitions required"
        )
    if "UpdatedAt" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    else:
        raise DeserializationError("GroupingConfiguration.updated_at required")
    return out
