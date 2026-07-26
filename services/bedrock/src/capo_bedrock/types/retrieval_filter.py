"""Generated from Smithy shape ``com.amazonaws.bedrock#RetrievalFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.filter_attribute
    import capo_bedrock.types.retrieval_filter_list


class _RetrievalFilter_equals(TypedDict, closed=True):
    equals: "capo_bedrock.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_notEquals(TypedDict, closed=True):
    notEquals: "capo_bedrock.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_greaterThan(TypedDict, closed=True):
    greaterThan: "capo_bedrock.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_greaterThanOrEquals(TypedDict, closed=True):
    greaterThanOrEquals: "capo_bedrock.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_lessThan(TypedDict, closed=True):
    lessThan: "capo_bedrock.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_lessThanOrEquals(TypedDict, closed=True):
    lessThanOrEquals: "capo_bedrock.types.filter_attribute.FilterAttribute"


_RetrievalFilter_in = TypedDict(
    "_RetrievalFilter_in",
    {
        "in": "capo_bedrock.types.filter_attribute.FilterAttribute",
    },
    closed=True,
)


class _RetrievalFilter_notIn(TypedDict, closed=True):
    notIn: "capo_bedrock.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_startsWith(TypedDict, closed=True):
    startsWith: "capo_bedrock.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_listContains(TypedDict, closed=True):
    listContains: "capo_bedrock.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_stringContains(TypedDict, closed=True):
    stringContains: "capo_bedrock.types.filter_attribute.FilterAttribute"


class _RetrievalFilter_andAll(TypedDict, closed=True):
    andAll: "capo_bedrock.types.retrieval_filter_list.RetrievalFilterList"


class _RetrievalFilter_orAll(TypedDict, closed=True):
    orAll: "capo_bedrock.types.retrieval_filter_list.RetrievalFilterList"


RetrievalFilter: TypeAlias = (
    _RetrievalFilter_equals
    | _RetrievalFilter_notEquals
    | _RetrievalFilter_greaterThan
    | _RetrievalFilter_greaterThanOrEquals
    | _RetrievalFilter_lessThan
    | _RetrievalFilter_lessThanOrEquals
    | _RetrievalFilter_in
    | _RetrievalFilter_notIn
    | _RetrievalFilter_startsWith
    | _RetrievalFilter_listContains
    | _RetrievalFilter_stringContains
    | _RetrievalFilter_andAll
    | _RetrievalFilter_orAll
)


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFilter) -> dict:
    if "equals" in value:
        import capo_bedrock.types.filter_attribute

        return {
            "equals": capo_bedrock.types.filter_attribute.serialize_json(
                value["equals"]
            )
        }
    elif "notEquals" in value:
        import capo_bedrock.types.filter_attribute

        return {
            "notEquals": capo_bedrock.types.filter_attribute.serialize_json(
                value["notEquals"]
            )
        }
    elif "greaterThan" in value:
        import capo_bedrock.types.filter_attribute

        return {
            "greaterThan": capo_bedrock.types.filter_attribute.serialize_json(
                value["greaterThan"]
            )
        }
    elif "greaterThanOrEquals" in value:
        import capo_bedrock.types.filter_attribute

        return {
            "greaterThanOrEquals": capo_bedrock.types.filter_attribute.serialize_json(
                value["greaterThanOrEquals"]
            )
        }
    elif "lessThan" in value:
        import capo_bedrock.types.filter_attribute

        return {
            "lessThan": capo_bedrock.types.filter_attribute.serialize_json(
                value["lessThan"]
            )
        }
    elif "lessThanOrEquals" in value:
        import capo_bedrock.types.filter_attribute

        return {
            "lessThanOrEquals": capo_bedrock.types.filter_attribute.serialize_json(
                value["lessThanOrEquals"]
            )
        }
    elif "in" in value:
        import capo_bedrock.types.filter_attribute

        return {"in": capo_bedrock.types.filter_attribute.serialize_json(value["in"])}
    elif "notIn" in value:
        import capo_bedrock.types.filter_attribute

        return {
            "notIn": capo_bedrock.types.filter_attribute.serialize_json(value["notIn"])
        }
    elif "startsWith" in value:
        import capo_bedrock.types.filter_attribute

        return {
            "startsWith": capo_bedrock.types.filter_attribute.serialize_json(
                value["startsWith"]
            )
        }
    elif "listContains" in value:
        import capo_bedrock.types.filter_attribute

        return {
            "listContains": capo_bedrock.types.filter_attribute.serialize_json(
                value["listContains"]
            )
        }
    elif "stringContains" in value:
        import capo_bedrock.types.filter_attribute

        return {
            "stringContains": capo_bedrock.types.filter_attribute.serialize_json(
                value["stringContains"]
            )
        }
    elif "andAll" in value:
        import capo_bedrock.types.retrieval_filter_list

        return {
            "andAll": capo_bedrock.types.retrieval_filter_list.serialize_json(
                value["andAll"]
            )
        }
    elif "orAll" in value:
        import capo_bedrock.types.retrieval_filter_list

        return {
            "orAll": capo_bedrock.types.retrieval_filter_list.serialize_json(
                value["orAll"]
            )
        }
    else:
        raise SerializationError("RetrievalFilter: no variant present")


def deserialize_json(data: dict) -> RetrievalFilter:
    if "equals" in data:
        import capo_bedrock.types.filter_attribute

        return {
            "equals": capo_bedrock.types.filter_attribute.deserialize_json(
                data["equals"]
            )
        }
    elif "notEquals" in data:
        import capo_bedrock.types.filter_attribute

        return {
            "notEquals": capo_bedrock.types.filter_attribute.deserialize_json(
                data["notEquals"]
            )
        }
    elif "greaterThan" in data:
        import capo_bedrock.types.filter_attribute

        return {
            "greaterThan": capo_bedrock.types.filter_attribute.deserialize_json(
                data["greaterThan"]
            )
        }
    elif "greaterThanOrEquals" in data:
        import capo_bedrock.types.filter_attribute

        return {
            "greaterThanOrEquals": capo_bedrock.types.filter_attribute.deserialize_json(
                data["greaterThanOrEquals"]
            )
        }
    elif "lessThan" in data:
        import capo_bedrock.types.filter_attribute

        return {
            "lessThan": capo_bedrock.types.filter_attribute.deserialize_json(
                data["lessThan"]
            )
        }
    elif "lessThanOrEquals" in data:
        import capo_bedrock.types.filter_attribute

        return {
            "lessThanOrEquals": capo_bedrock.types.filter_attribute.deserialize_json(
                data["lessThanOrEquals"]
            )
        }
    elif "in" in data:
        import capo_bedrock.types.filter_attribute

        return {"in": capo_bedrock.types.filter_attribute.deserialize_json(data["in"])}
    elif "notIn" in data:
        import capo_bedrock.types.filter_attribute

        return {
            "notIn": capo_bedrock.types.filter_attribute.deserialize_json(data["notIn"])
        }
    elif "startsWith" in data:
        import capo_bedrock.types.filter_attribute

        return {
            "startsWith": capo_bedrock.types.filter_attribute.deserialize_json(
                data["startsWith"]
            )
        }
    elif "listContains" in data:
        import capo_bedrock.types.filter_attribute

        return {
            "listContains": capo_bedrock.types.filter_attribute.deserialize_json(
                data["listContains"]
            )
        }
    elif "stringContains" in data:
        import capo_bedrock.types.filter_attribute

        return {
            "stringContains": capo_bedrock.types.filter_attribute.deserialize_json(
                data["stringContains"]
            )
        }
    elif "andAll" in data:
        import capo_bedrock.types.retrieval_filter_list

        return {
            "andAll": capo_bedrock.types.retrieval_filter_list.deserialize_json(
                data["andAll"]
            )
        }
    elif "orAll" in data:
        import capo_bedrock.types.retrieval_filter_list

        return {
            "orAll": capo_bedrock.types.retrieval_filter_list.deserialize_json(
                data["orAll"]
            )
        }
    else:
        raise DeserializationError("RetrievalFilter: no recognized variant key")
