"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSearchFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.knowledge_base_search_filter_name
    import aws_sdk_quicksight.types.knowledge_base_search_operator


class KnowledgeBaseSearchFilter(TypedDict):
    name: "aws_sdk_quicksight.types.knowledge_base_search_filter_name.KnowledgeBaseSearchFilterName"
    """<p>The name of the field to filter on.</p>"""
    operator: "aws_sdk_quicksight.types.knowledge_base_search_operator.KnowledgeBaseSearchOperator"
    """<p>The comparison operator to use for the filter.</p>"""
    value: "str"
    """<p>The value to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSearchFilter) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.knowledge_base_search_filter_name

    out["name"] = (
        aws_sdk_quicksight.types.knowledge_base_search_filter_name.serialize_json(
            value["name"]
        )
    )
    import aws_sdk_quicksight.types.knowledge_base_search_operator

    out["operator"] = (
        aws_sdk_quicksight.types.knowledge_base_search_operator.serialize_json(
            value["operator"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> KnowledgeBaseSearchFilter:
    out: KnowledgeBaseSearchFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_quicksight.types.knowledge_base_search_filter_name

        out["name"] = (
            aws_sdk_quicksight.types.knowledge_base_search_filter_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("KnowledgeBaseSearchFilter.name required")
    if "operator" in data:
        import aws_sdk_quicksight.types.knowledge_base_search_operator

        out["operator"] = (
            aws_sdk_quicksight.types.knowledge_base_search_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("KnowledgeBaseSearchFilter.operator required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("KnowledgeBaseSearchFilter.value required")
    return out
