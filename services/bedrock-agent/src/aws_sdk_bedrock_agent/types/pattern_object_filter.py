"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PatternObjectFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.filter_list
    import aws_sdk_bedrock_agent.types.filtered_object_type


class PatternObjectFilter(TypedDict):
    object_type: "aws_sdk_bedrock_agent.types.filtered_object_type.FilteredObjectType"
    """<p>The supported object type or content type of the data source.</p>"""
    inclusion_filters: NotRequired["aws_sdk_bedrock_agent.types.filter_list.FilterList"]
    """<p>A list of one or more inclusion regular expression patterns to include certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isn’t crawled.</p>"""
    exclusion_filters: NotRequired["aws_sdk_bedrock_agent.types.filter_list.FilterList"]
    """<p>A list of one or more exclusion regular expression patterns to exclude certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isn’t crawled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PatternObjectFilter) -> dict:
    out: dict = {}
    out["objectType"] = value["object_type"]
    if "inclusion_filters" in value:
        import aws_sdk_bedrock_agent.types.filter_list

        out["inclusionFilters"] = (
            aws_sdk_bedrock_agent.types.filter_list.serialize_json(
                value["inclusion_filters"]
            )
        )
    if "exclusion_filters" in value:
        import aws_sdk_bedrock_agent.types.filter_list

        out["exclusionFilters"] = (
            aws_sdk_bedrock_agent.types.filter_list.serialize_json(
                value["exclusion_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> PatternObjectFilter:
    out: PatternObjectFilter = {}  # type: ignore[typeddict-item]
    if "objectType" in data:
        out["object_type"] = data["objectType"]
    else:
        raise DeserializationError("PatternObjectFilter.object_type required")
    if "inclusionFilters" in data:
        import aws_sdk_bedrock_agent.types.filter_list

        out["inclusion_filters"] = (
            aws_sdk_bedrock_agent.types.filter_list.deserialize_json(
                data["inclusionFilters"]
            )
        )
    if "exclusionFilters" in data:
        import aws_sdk_bedrock_agent.types.filter_list

        out["exclusion_filters"] = (
            aws_sdk_bedrock_agent.types.filter_list.deserialize_json(
                data["exclusionFilters"]
            )
        )
    return out
