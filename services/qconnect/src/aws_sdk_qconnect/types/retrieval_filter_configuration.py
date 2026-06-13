"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrievalFilterConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.filter_attribute
    import aws_sdk_qconnect.types.retrieval_filter_list


class _RetrievalFilterConfiguration_andAll(TypedDict):
    andAll: "aws_sdk_qconnect.types.retrieval_filter_list.RetrievalFilterList"


class _RetrievalFilterConfiguration_equals(TypedDict):
    equals: "aws_sdk_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_greaterThan(TypedDict):
    greaterThan: "aws_sdk_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_greaterThanOrEquals(TypedDict):
    greaterThanOrEquals: "aws_sdk_qconnect.types.filter_attribute.FilterAttribute"


_RetrievalFilterConfiguration_in = TypedDict(
    "_RetrievalFilterConfiguration_in",
    {
        "in": "aws_sdk_qconnect.types.filter_attribute.FilterAttribute",
    },
)


class _RetrievalFilterConfiguration_lessThan(TypedDict):
    lessThan: "aws_sdk_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_lessThanOrEquals(TypedDict):
    lessThanOrEquals: "aws_sdk_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_listContains(TypedDict):
    listContains: "aws_sdk_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_notEquals(TypedDict):
    notEquals: "aws_sdk_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_notIn(TypedDict):
    notIn: "aws_sdk_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_orAll(TypedDict):
    orAll: "aws_sdk_qconnect.types.retrieval_filter_list.RetrievalFilterList"


class _RetrievalFilterConfiguration_startsWith(TypedDict):
    startsWith: "aws_sdk_qconnect.types.filter_attribute.FilterAttribute"


class _RetrievalFilterConfiguration_stringContains(TypedDict):
    stringContains: "aws_sdk_qconnect.types.filter_attribute.FilterAttribute"


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
        import aws_sdk_qconnect.types.retrieval_filter_list

        return {
            "andAll": aws_sdk_qconnect.types.retrieval_filter_list.serialize_json(
                value["andAll"]
            )
        }
    elif "equals" in value:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "equals": aws_sdk_qconnect.types.filter_attribute.serialize_json(
                value["equals"]
            )
        }
    elif "greaterThan" in value:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "greaterThan": aws_sdk_qconnect.types.filter_attribute.serialize_json(
                value["greaterThan"]
            )
        }
    elif "greaterThanOrEquals" in value:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "greaterThanOrEquals": aws_sdk_qconnect.types.filter_attribute.serialize_json(
                value["greaterThanOrEquals"]
            )
        }
    elif "in" in value:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "in": aws_sdk_qconnect.types.filter_attribute.serialize_json(value["in"])
        }
    elif "lessThan" in value:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "lessThan": aws_sdk_qconnect.types.filter_attribute.serialize_json(
                value["lessThan"]
            )
        }
    elif "lessThanOrEquals" in value:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "lessThanOrEquals": aws_sdk_qconnect.types.filter_attribute.serialize_json(
                value["lessThanOrEquals"]
            )
        }
    elif "listContains" in value:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "listContains": aws_sdk_qconnect.types.filter_attribute.serialize_json(
                value["listContains"]
            )
        }
    elif "notEquals" in value:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "notEquals": aws_sdk_qconnect.types.filter_attribute.serialize_json(
                value["notEquals"]
            )
        }
    elif "notIn" in value:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "notIn": aws_sdk_qconnect.types.filter_attribute.serialize_json(
                value["notIn"]
            )
        }
    elif "orAll" in value:
        import aws_sdk_qconnect.types.retrieval_filter_list

        return {
            "orAll": aws_sdk_qconnect.types.retrieval_filter_list.serialize_json(
                value["orAll"]
            )
        }
    elif "startsWith" in value:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "startsWith": aws_sdk_qconnect.types.filter_attribute.serialize_json(
                value["startsWith"]
            )
        }
    elif "stringContains" in value:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "stringContains": aws_sdk_qconnect.types.filter_attribute.serialize_json(
                value["stringContains"]
            )
        }
    else:
        raise SerializationError("RetrievalFilterConfiguration: no variant present")


def deserialize_json(data: dict) -> RetrievalFilterConfiguration:
    if "andAll" in data:
        import aws_sdk_qconnect.types.retrieval_filter_list

        return {
            "andAll": aws_sdk_qconnect.types.retrieval_filter_list.deserialize_json(
                data["andAll"]
            )
        }
    elif "equals" in data:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "equals": aws_sdk_qconnect.types.filter_attribute.deserialize_json(
                data["equals"]
            )
        }
    elif "greaterThan" in data:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "greaterThan": aws_sdk_qconnect.types.filter_attribute.deserialize_json(
                data["greaterThan"]
            )
        }
    elif "greaterThanOrEquals" in data:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "greaterThanOrEquals": aws_sdk_qconnect.types.filter_attribute.deserialize_json(
                data["greaterThanOrEquals"]
            )
        }
    elif "in" in data:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "in": aws_sdk_qconnect.types.filter_attribute.deserialize_json(data["in"])
        }
    elif "lessThan" in data:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "lessThan": aws_sdk_qconnect.types.filter_attribute.deserialize_json(
                data["lessThan"]
            )
        }
    elif "lessThanOrEquals" in data:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "lessThanOrEquals": aws_sdk_qconnect.types.filter_attribute.deserialize_json(
                data["lessThanOrEquals"]
            )
        }
    elif "listContains" in data:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "listContains": aws_sdk_qconnect.types.filter_attribute.deserialize_json(
                data["listContains"]
            )
        }
    elif "notEquals" in data:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "notEquals": aws_sdk_qconnect.types.filter_attribute.deserialize_json(
                data["notEquals"]
            )
        }
    elif "notIn" in data:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "notIn": aws_sdk_qconnect.types.filter_attribute.deserialize_json(
                data["notIn"]
            )
        }
    elif "orAll" in data:
        import aws_sdk_qconnect.types.retrieval_filter_list

        return {
            "orAll": aws_sdk_qconnect.types.retrieval_filter_list.deserialize_json(
                data["orAll"]
            )
        }
    elif "startsWith" in data:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "startsWith": aws_sdk_qconnect.types.filter_attribute.deserialize_json(
                data["startsWith"]
            )
        }
    elif "stringContains" in data:
        import aws_sdk_qconnect.types.filter_attribute

        return {
            "stringContains": aws_sdk_qconnect.types.filter_attribute.deserialize_json(
                data["stringContains"]
            )
        }
    else:
        raise DeserializationError(
            "RetrievalFilterConfiguration: no recognized variant key"
        )
