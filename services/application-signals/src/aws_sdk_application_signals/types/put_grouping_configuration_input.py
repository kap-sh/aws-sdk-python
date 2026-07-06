"""Generated from Smithy shape ``com.amazonaws.applicationsignals#PutGroupingConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.grouping_attribute_definitions


class PutGroupingConfigurationInput(TypedDict, closed=True):
    grouping_attribute_definitions: "aws_sdk_application_signals.types.grouping_attribute_definitions.GroupingAttributeDefinitions"
    """<p>An array of grouping attribute definitions that specify how services should be grouped. Each definition includes a friendly name, source keys to derive the grouping value from, and an optional default value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutGroupingConfigurationInput) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.grouping_attribute_definitions

    out["GroupingAttributeDefinitions"] = (
        aws_sdk_application_signals.types.grouping_attribute_definitions.serialize_json(
            value["grouping_attribute_definitions"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutGroupingConfigurationInput:
    out: PutGroupingConfigurationInput = {}  # type: ignore[typeddict-item]
    if "GroupingAttributeDefinitions" in data:
        import aws_sdk_application_signals.types.grouping_attribute_definitions

        out["grouping_attribute_definitions"] = (
            aws_sdk_application_signals.types.grouping_attribute_definitions.deserialize_json(
                data["GroupingAttributeDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "PutGroupingConfigurationInput.grouping_attribute_definitions required"
        )
    return out
