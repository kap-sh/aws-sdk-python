"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListGroupingAttributeDefinitionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_application_signals.types.grouping_attribute_definitions
    import aws_sdk_application_signals.types.next_token


class ListGroupingAttributeDefinitionsOutput(TypedDict):
    grouping_attribute_definitions: "aws_sdk_application_signals.types.grouping_attribute_definitions.GroupingAttributeDefinitions"
    """<p>An array of structures, where each structure contains information about one grouping attribute definition, including the grouping name, source keys, and default values.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the grouping configuration was last updated. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.</p>"""
    next_token: NotRequired["aws_sdk_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get the next set of grouping attribute definitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupingAttributeDefinitionsOutput) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.grouping_attribute_definitions

    out["GroupingAttributeDefinitions"] = (
        aws_sdk_application_signals.types.grouping_attribute_definitions.serialize_json(
            value["grouping_attribute_definitions"]
        )
    )
    if "updated_at" in value:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["UpdatedAt"] = (
            aws_sdk_application_signals.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupingAttributeDefinitionsOutput:
    out: ListGroupingAttributeDefinitionsOutput = {}  # type: ignore[typeddict-item]
    if "GroupingAttributeDefinitions" in data:
        import aws_sdk_application_signals.types.grouping_attribute_definitions

        out["grouping_attribute_definitions"] = (
            aws_sdk_application_signals.types.grouping_attribute_definitions.deserialize_json(
                data["GroupingAttributeDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "ListGroupingAttributeDefinitionsOutput.grouping_attribute_definitions required"
        )
    if "UpdatedAt" in data:
        import aws_sdk_application_signals.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_application_signals.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
