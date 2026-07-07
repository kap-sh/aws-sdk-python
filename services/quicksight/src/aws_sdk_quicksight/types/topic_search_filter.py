"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.topic_filter_attribute
    import aws_sdk_quicksight.types.topic_filter_operator


class TopicSearchFilter(TypedDict, closed=True):
    operator: "aws_sdk_quicksight.types.topic_filter_operator.TopicFilterOperator"
    """<p>The operator like equals or like.</p>"""
    name: "aws_sdk_quicksight.types.topic_filter_attribute.TopicFilterAttribute"
    """<p>The name of the topic search filter.</p>"""
    value: "aws_sdk_quicksight.types.string.String"
    """<p>The value of the topic search filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicSearchFilter) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.topic_filter_operator

    out["Operator"] = aws_sdk_quicksight.types.topic_filter_operator.serialize_json(
        value["operator"]
    )
    import aws_sdk_quicksight.types.topic_filter_attribute

    out["Name"] = aws_sdk_quicksight.types.topic_filter_attribute.serialize_json(
        value["name"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TopicSearchFilter:
    out: TopicSearchFilter = {}  # type: ignore[typeddict-item]
    if "Operator" in data:
        import aws_sdk_quicksight.types.topic_filter_operator

        out["operator"] = (
            aws_sdk_quicksight.types.topic_filter_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("TopicSearchFilter.operator required")
    if "Name" in data:
        import aws_sdk_quicksight.types.topic_filter_attribute

        out["name"] = aws_sdk_quicksight.types.topic_filter_attribute.deserialize_json(
            data["Name"]
        )
    else:
        raise DeserializationError("TopicSearchFilter.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("TopicSearchFilter.value required")
    return out
