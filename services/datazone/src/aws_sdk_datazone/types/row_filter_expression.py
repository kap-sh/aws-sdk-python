"""Generated from Smithy shape ``com.amazonaws.datazone#RowFilterExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.equal_to_expression
    import aws_sdk_datazone.types.greater_than_expression
    import aws_sdk_datazone.types.greater_than_or_equal_to_expression
    import aws_sdk_datazone.types.in_expression
    import aws_sdk_datazone.types.is_not_null_expression
    import aws_sdk_datazone.types.is_null_expression
    import aws_sdk_datazone.types.less_than_expression
    import aws_sdk_datazone.types.less_than_or_equal_to_expression
    import aws_sdk_datazone.types.like_expression
    import aws_sdk_datazone.types.not_equal_to_expression
    import aws_sdk_datazone.types.not_in_expression
    import aws_sdk_datazone.types.not_like_expression


class _RowFilterExpression_equalTo(TypedDict, closed=True):
    equalTo: "aws_sdk_datazone.types.equal_to_expression.EqualToExpression"


class _RowFilterExpression_notEqualTo(TypedDict, closed=True):
    notEqualTo: "aws_sdk_datazone.types.not_equal_to_expression.NotEqualToExpression"


class _RowFilterExpression_greaterThan(TypedDict, closed=True):
    greaterThan: "aws_sdk_datazone.types.greater_than_expression.GreaterThanExpression"


class _RowFilterExpression_lessThan(TypedDict, closed=True):
    lessThan: "aws_sdk_datazone.types.less_than_expression.LessThanExpression"


class _RowFilterExpression_greaterThanOrEqualTo(TypedDict, closed=True):
    greaterThanOrEqualTo: "aws_sdk_datazone.types.greater_than_or_equal_to_expression.GreaterThanOrEqualToExpression"


class _RowFilterExpression_lessThanOrEqualTo(TypedDict, closed=True):
    lessThanOrEqualTo: "aws_sdk_datazone.types.less_than_or_equal_to_expression.LessThanOrEqualToExpression"


class _RowFilterExpression_isNull(TypedDict, closed=True):
    isNull: "aws_sdk_datazone.types.is_null_expression.IsNullExpression"


class _RowFilterExpression_isNotNull(TypedDict, closed=True):
    isNotNull: "aws_sdk_datazone.types.is_not_null_expression.IsNotNullExpression"


_RowFilterExpression_in = TypedDict(
    "_RowFilterExpression_in",
    {
        "in": "aws_sdk_datazone.types.in_expression.InExpression",
    },
    closed=True,
)


class _RowFilterExpression_notIn(TypedDict, closed=True):
    notIn: "aws_sdk_datazone.types.not_in_expression.NotInExpression"


class _RowFilterExpression_like(TypedDict, closed=True):
    like: "aws_sdk_datazone.types.like_expression.LikeExpression"


class _RowFilterExpression_notLike(TypedDict, closed=True):
    notLike: "aws_sdk_datazone.types.not_like_expression.NotLikeExpression"


RowFilterExpression: TypeAlias = (
    _RowFilterExpression_equalTo
    | _RowFilterExpression_notEqualTo
    | _RowFilterExpression_greaterThan
    | _RowFilterExpression_lessThan
    | _RowFilterExpression_greaterThanOrEqualTo
    | _RowFilterExpression_lessThanOrEqualTo
    | _RowFilterExpression_isNull
    | _RowFilterExpression_isNotNull
    | _RowFilterExpression_in
    | _RowFilterExpression_notIn
    | _RowFilterExpression_like
    | _RowFilterExpression_notLike
)


# --- restJson1 ser/de ---
def serialize_json(value: RowFilterExpression) -> dict:
    if "equalTo" in value:
        import aws_sdk_datazone.types.equal_to_expression

        return {
            "equalTo": aws_sdk_datazone.types.equal_to_expression.serialize_json(
                value["equalTo"]
            )
        }
    elif "notEqualTo" in value:
        import aws_sdk_datazone.types.not_equal_to_expression

        return {
            "notEqualTo": aws_sdk_datazone.types.not_equal_to_expression.serialize_json(
                value["notEqualTo"]
            )
        }
    elif "greaterThan" in value:
        import aws_sdk_datazone.types.greater_than_expression

        return {
            "greaterThan": aws_sdk_datazone.types.greater_than_expression.serialize_json(
                value["greaterThan"]
            )
        }
    elif "lessThan" in value:
        import aws_sdk_datazone.types.less_than_expression

        return {
            "lessThan": aws_sdk_datazone.types.less_than_expression.serialize_json(
                value["lessThan"]
            )
        }
    elif "greaterThanOrEqualTo" in value:
        import aws_sdk_datazone.types.greater_than_or_equal_to_expression

        return {
            "greaterThanOrEqualTo": aws_sdk_datazone.types.greater_than_or_equal_to_expression.serialize_json(
                value["greaterThanOrEqualTo"]
            )
        }
    elif "lessThanOrEqualTo" in value:
        import aws_sdk_datazone.types.less_than_or_equal_to_expression

        return {
            "lessThanOrEqualTo": aws_sdk_datazone.types.less_than_or_equal_to_expression.serialize_json(
                value["lessThanOrEqualTo"]
            )
        }
    elif "isNull" in value:
        import aws_sdk_datazone.types.is_null_expression

        return {
            "isNull": aws_sdk_datazone.types.is_null_expression.serialize_json(
                value["isNull"]
            )
        }
    elif "isNotNull" in value:
        import aws_sdk_datazone.types.is_not_null_expression

        return {
            "isNotNull": aws_sdk_datazone.types.is_not_null_expression.serialize_json(
                value["isNotNull"]
            )
        }
    elif "in" in value:
        import aws_sdk_datazone.types.in_expression

        return {"in": aws_sdk_datazone.types.in_expression.serialize_json(value["in"])}
    elif "notIn" in value:
        import aws_sdk_datazone.types.not_in_expression

        return {
            "notIn": aws_sdk_datazone.types.not_in_expression.serialize_json(
                value["notIn"]
            )
        }
    elif "like" in value:
        import aws_sdk_datazone.types.like_expression

        return {
            "like": aws_sdk_datazone.types.like_expression.serialize_json(value["like"])
        }
    elif "notLike" in value:
        import aws_sdk_datazone.types.not_like_expression

        return {
            "notLike": aws_sdk_datazone.types.not_like_expression.serialize_json(
                value["notLike"]
            )
        }
    else:
        raise SerializationError("RowFilterExpression: no variant present")


def deserialize_json(data: dict) -> RowFilterExpression:
    if "equalTo" in data:
        import aws_sdk_datazone.types.equal_to_expression

        return {
            "equalTo": aws_sdk_datazone.types.equal_to_expression.deserialize_json(
                data["equalTo"]
            )
        }
    elif "notEqualTo" in data:
        import aws_sdk_datazone.types.not_equal_to_expression

        return {
            "notEqualTo": aws_sdk_datazone.types.not_equal_to_expression.deserialize_json(
                data["notEqualTo"]
            )
        }
    elif "greaterThan" in data:
        import aws_sdk_datazone.types.greater_than_expression

        return {
            "greaterThan": aws_sdk_datazone.types.greater_than_expression.deserialize_json(
                data["greaterThan"]
            )
        }
    elif "lessThan" in data:
        import aws_sdk_datazone.types.less_than_expression

        return {
            "lessThan": aws_sdk_datazone.types.less_than_expression.deserialize_json(
                data["lessThan"]
            )
        }
    elif "greaterThanOrEqualTo" in data:
        import aws_sdk_datazone.types.greater_than_or_equal_to_expression

        return {
            "greaterThanOrEqualTo": aws_sdk_datazone.types.greater_than_or_equal_to_expression.deserialize_json(
                data["greaterThanOrEqualTo"]
            )
        }
    elif "lessThanOrEqualTo" in data:
        import aws_sdk_datazone.types.less_than_or_equal_to_expression

        return {
            "lessThanOrEqualTo": aws_sdk_datazone.types.less_than_or_equal_to_expression.deserialize_json(
                data["lessThanOrEqualTo"]
            )
        }
    elif "isNull" in data:
        import aws_sdk_datazone.types.is_null_expression

        return {
            "isNull": aws_sdk_datazone.types.is_null_expression.deserialize_json(
                data["isNull"]
            )
        }
    elif "isNotNull" in data:
        import aws_sdk_datazone.types.is_not_null_expression

        return {
            "isNotNull": aws_sdk_datazone.types.is_not_null_expression.deserialize_json(
                data["isNotNull"]
            )
        }
    elif "in" in data:
        import aws_sdk_datazone.types.in_expression

        return {"in": aws_sdk_datazone.types.in_expression.deserialize_json(data["in"])}
    elif "notIn" in data:
        import aws_sdk_datazone.types.not_in_expression

        return {
            "notIn": aws_sdk_datazone.types.not_in_expression.deserialize_json(
                data["notIn"]
            )
        }
    elif "like" in data:
        import aws_sdk_datazone.types.like_expression

        return {
            "like": aws_sdk_datazone.types.like_expression.deserialize_json(
                data["like"]
            )
        }
    elif "notLike" in data:
        import aws_sdk_datazone.types.not_like_expression

        return {
            "notLike": aws_sdk_datazone.types.not_like_expression.deserialize_json(
                data["notLike"]
            )
        }
    else:
        raise DeserializationError("RowFilterExpression: no recognized variant key")
