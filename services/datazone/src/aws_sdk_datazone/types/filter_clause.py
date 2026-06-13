"""Generated from Smithy shape ``com.amazonaws.datazone#FilterClause``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.filter
    import aws_sdk_datazone.types.filter_list


class _FilterClause_filter(TypedDict):
    filter: "aws_sdk_datazone.types.filter.Filter"


_FilterClause_and = TypedDict(
    "_FilterClause_and",
    {
        "and": "aws_sdk_datazone.types.filter_list.FilterList",
    },
)


_FilterClause_or = TypedDict(
    "_FilterClause_or",
    {
        "or": "aws_sdk_datazone.types.filter_list.FilterList",
    },
)

FilterClause: TypeAlias = _FilterClause_filter | _FilterClause_and | _FilterClause_or


# --- restJson1 ser/de ---
def serialize_json(value: FilterClause) -> dict:
    if "filter" in value:
        import aws_sdk_datazone.types.filter

        return {"filter": aws_sdk_datazone.types.filter.serialize_json(value["filter"])}
    elif "and" in value:
        import aws_sdk_datazone.types.filter_list

        return {"and": aws_sdk_datazone.types.filter_list.serialize_json(value["and"])}
    elif "or" in value:
        import aws_sdk_datazone.types.filter_list

        return {"or": aws_sdk_datazone.types.filter_list.serialize_json(value["or"])}
    else:
        raise SerializationError("FilterClause: no variant present")


def deserialize_json(data: dict) -> FilterClause:
    if "filter" in data:
        import aws_sdk_datazone.types.filter

        return {
            "filter": aws_sdk_datazone.types.filter.deserialize_json(data["filter"])
        }
    elif "and" in data:
        import aws_sdk_datazone.types.filter_list

        return {"and": aws_sdk_datazone.types.filter_list.deserialize_json(data["and"])}
    elif "or" in data:
        import aws_sdk_datazone.types.filter_list

        return {"or": aws_sdk_datazone.types.filter_list.deserialize_json(data["or"])}
    else:
        raise DeserializationError("FilterClause: no recognized variant key")
