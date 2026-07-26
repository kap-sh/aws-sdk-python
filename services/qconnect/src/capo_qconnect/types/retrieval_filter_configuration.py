"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrievalFilterConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.filter_attribute
    import capo_qconnect.types.retrieval_filter_list


class _RetrievalFilterConfiguration_andAll(TypedDict, closed=True):
    andAll: "capo_qconnect.types.retrieval_filter_list.RetrievalFilterList"


class _RetrievalFilterConfiguration_equals(TypedDict, closed=True):
    equals: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_greaterThan(TypedDict, closed=True):
    greaterThan: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_greaterThanOrEquals(TypedDict, closed=True):
    greaterThanOrEquals: "capo_qconnect.types.filter_attribute.FilterAttribute"


_RetrievalFilterConfiguration_in = TypedDict(
    "_RetrievalFilterConfiguration_in",
    {
        "in": "capo_qconnect.types.filter_attribute.FilterAttribute",
    },
    closed=True,
)


class _RetrievalFilterConfiguration_lessThan(TypedDict, closed=True):
    lessThan: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_lessThanOrEquals(TypedDict, closed=True):
    lessThanOrEquals: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_listContains(TypedDict, closed=True):
    listContains: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_notEquals(TypedDict, closed=True):
    notEquals: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_notIn(TypedDict, closed=True):
    notIn: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_orAll(TypedDict, closed=True):
    orAll: "capo_qconnect.types.retrieval_filter_list.RetrievalFilterList"


class _RetrievalFilterConfiguration_startsWith(TypedDict, closed=True):
    startsWith: "capo_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_stringContains(TypedDict, closed=True):
    stringContains: "capo_qconnect.types.filter_attribute.FilterAttribute"


RetrievalFilterConfiguration: TypeAlias = (
    _RetrievalFilterConfiguration_andAll
    | _RetrievalFilterConfiguration_equals
    | _RetrievalFilterConfiguration_greaterThan
    | _RetrievalFilterConfiguration_greaterThanOrEquals
    | _RetrievalFilterConfiguration_in
    | _RetrievalFilterConfiguration_lessThan
    | _RetrievalFilterConfiguration_lessThanOrEquals
    | _RetrievalFilterConfiguration_listContains
    | _RetrievalFilterConfiguration_notEquals
    | _RetrievalFilterConfiguration_notIn
    | _RetrievalFilterConfiguration_orAll
    | _RetrievalFilterConfiguration_startsWith
    | _RetrievalFilterConfiguration_stringContains
)


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFilterConfiguration) -> dict:
    if "andAll" in value:
        import capo_qconnect.types.retrieval_filter_list

        return {
            "andAll": capo_qconnect.types.retrieval_filter_list.serialize_json(
                value["andAll"]
            )
        }
    elif "equals" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "equals": capo_qconnect.types.filter_attribute.serialize_json(
                value["equals"]
            )
        }
    elif "greaterThan" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "greaterThan": capo_qconnect.types.filter_attribute.serialize_json(
                value["greaterThan"]
            )
        }
    elif "greaterThanOrEquals" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "greaterThanOrEquals": capo_qconnect.types.filter_attribute.serialize_json(
                value["greaterThanOrEquals"]
            )
        }
    elif "in" in value:
        import capo_qconnect.types.filter_attribute

        return {"in": capo_qconnect.types.filter_attribute.serialize_json(value["in"])}
    elif "lessThan" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "lessThan": capo_qconnect.types.filter_attribute.serialize_json(
                value["lessThan"]
            )
        }
    elif "lessThanOrEquals" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "lessThanOrEquals": capo_qconnect.types.filter_attribute.serialize_json(
                value["lessThanOrEquals"]
            )
        }
    elif "listContains" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "listContains": capo_qconnect.types.filter_attribute.serialize_json(
                value["listContains"]
            )
        }
    elif "notEquals" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "notEquals": capo_qconnect.types.filter_attribute.serialize_json(
                value["notEquals"]
            )
        }
    elif "notIn" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "notIn": capo_qconnect.types.filter_attribute.serialize_json(value["notIn"])
        }
    elif "orAll" in value:
        import capo_qconnect.types.retrieval_filter_list

        return {
            "orAll": capo_qconnect.types.retrieval_filter_list.serialize_json(
                value["orAll"]
            )
        }
    elif "startsWith" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "startsWith": capo_qconnect.types.filter_attribute.serialize_json(
                value["startsWith"]
            )
        }
    elif "stringContains" in value:
        import capo_qconnect.types.filter_attribute

        return {
            "stringContains": capo_qconnect.types.filter_attribute.serialize_json(
                value["stringContains"]
            )
        }
    else:
        raise SerializationError("RetrievalFilterConfiguration: no variant present")


def deserialize_json(data: dict) -> RetrievalFilterConfiguration:
    if "andAll" in data:
        import capo_qconnect.types.retrieval_filter_list

        return {
            "andAll": capo_qconnect.types.retrieval_filter_list.deserialize_json(
                data["andAll"]
            )
        }
    elif "equals" in data:
        import capo_qconnect.types.filter_attribute

        return {
            "equals": capo_qconnect.types.filter_attribute.deserialize_json(
                data["equals"]
            )
        }
    elif "greaterThan" in data:
        import capo_qconnect.types.filter_attribute

        return {
            "greaterThan": capo_qconnect.types.filter_attribute.deserialize_json(
                data["greaterThan"]
            )
        }
    elif "greaterThanOrEquals" in data:
        import capo_qconnect.types.filter_attribute

        return {
            "greaterThanOrEquals": capo_qconnect.types.filter_attribute.deserialize_json(
                data["greaterThanOrEquals"]
            )
        }
    elif "in" in data:
        import capo_qconnect.types.filter_attribute

        return {"in": capo_qconnect.types.filter_attribute.deserialize_json(data["in"])}
    elif "lessThan" in data:
        import capo_qconnect.types.filter_attribute

        return {
            "lessThan": capo_qconnect.types.filter_attribute.deserialize_json(
                data["lessThan"]
            )
        }
    elif "lessThanOrEquals" in data:
        import capo_qconnect.types.filter_attribute

        return {
            "lessThanOrEquals": capo_qconnect.types.filter_attribute.deserialize_json(
                data["lessThanOrEquals"]
            )
        }
    elif "listContains" in data:
        import capo_qconnect.types.filter_attribute

        return {
            "listContains": capo_qconnect.types.filter_attribute.deserialize_json(
                data["listContains"]
            )
        }
    elif "notEquals" in data:
        import capo_qconnect.types.filter_attribute

        return {
            "notEquals": capo_qconnect.types.filter_attribute.deserialize_json(
                data["notEquals"]
            )
        }
    elif "notIn" in data:
        import capo_qconnect.types.filter_attribute

        return {
            "notIn": capo_qconnect.types.filter_attribute.deserialize_json(
                data["notIn"]
            )
        }
    elif "orAll" in data:
        import capo_qconnect.types.retrieval_filter_list

        return {
            "orAll": capo_qconnect.types.retrieval_filter_list.deserialize_json(
                data["orAll"]
            )
        }
    elif "startsWith" in data:
        import capo_qconnect.types.filter_attribute

        return {
            "startsWith": capo_qconnect.types.filter_attribute.deserialize_json(
                data["startsWith"]
            )
        }
    elif "stringContains" in data:
        import capo_qconnect.types.filter_attribute

        return {
            "stringContains": capo_qconnect.types.filter_attribute.deserialize_json(
                data["stringContains"]
            )
        }
    else:
        raise DeserializationError(
            "RetrievalFilterConfiguration: no recognized variant key"
        )
