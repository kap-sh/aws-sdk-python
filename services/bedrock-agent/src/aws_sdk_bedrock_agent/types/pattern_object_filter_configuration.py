"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PatternObjectFilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.pattern_object_filter_list


class PatternObjectFilterConfiguration(TypedDict, closed=True):
    filters: (
        "aws_sdk_bedrock_agent.types.pattern_object_filter_list.PatternObjectFilterList"
    )
    """<p>The configuration of specific filters applied to your data source content. You can filter out or include certain content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PatternObjectFilterConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.pattern_object_filter_list

    out["filters"] = (
        aws_sdk_bedrock_agent.types.pattern_object_filter_list.serialize_json(
            value["filters"]
        )
    )
    return out


def deserialize_json(data: dict) -> PatternObjectFilterConfiguration:
    out: PatternObjectFilterConfiguration = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_bedrock_agent.types.pattern_object_filter_list

        out["filters"] = (
            aws_sdk_bedrock_agent.types.pattern_object_filter_list.deserialize_json(
                data["filters"]
            )
        )
    else:
        raise DeserializationError("PatternObjectFilterConfiguration.filters required")
    return out
