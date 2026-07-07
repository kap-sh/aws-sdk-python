"""Generated from Smithy shape ``com.amazonaws.applicationsignals#PutGroupingConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.grouping_configuration


class PutGroupingConfigurationOutput(TypedDict, closed=True):
    grouping_configuration: (
        "aws_sdk_application_signals.types.grouping_configuration.GroupingConfiguration"
    )
    """<p>A structure containing the updated grouping configuration, including all grouping attribute definitions and the timestamp when it was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutGroupingConfigurationOutput) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.grouping_configuration

    out["GroupingConfiguration"] = (
        aws_sdk_application_signals.types.grouping_configuration.serialize_json(
            value["grouping_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutGroupingConfigurationOutput:
    out: PutGroupingConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "GroupingConfiguration" in data:
        import aws_sdk_application_signals.types.grouping_configuration

        out["grouping_configuration"] = (
            aws_sdk_application_signals.types.grouping_configuration.deserialize_json(
                data["GroupingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutGroupingConfigurationOutput.grouping_configuration required"
        )
    return out
