"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SearchField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.search_field_key
    import aws_sdk_chime_sdk_messaging.types.search_field_operator
    import aws_sdk_chime_sdk_messaging.types.search_field_values


class SearchField(TypedDict):
    key: "aws_sdk_chime_sdk_messaging.types.search_field_key.SearchFieldKey"
    """<p>An <code>enum</code> value that indicates the key to search the channel on. <code>MEMBERS</code> allows you to search channels based on memberships. You can use it with the <code>EQUALS</code> operator to get channels whose memberships are equal to the specified values, and with the <code>INCLUDES</code> operator to get channels whose memberships include the specified values.</p>"""
    values: "aws_sdk_chime_sdk_messaging.types.search_field_values.SearchFieldValues"
    """<p>The values that you want to search for, a list of strings. The values must be <code>AppInstanceUserArns</code> specified as a list of strings.</p> <note> <p>This operation isn't supported for <code>AppInstanceUsers</code> with a large number of memberships.</p> </note>"""
    operator: (
        "aws_sdk_chime_sdk_messaging.types.search_field_operator.SearchFieldOperator"
    )
    """<p>The operator used to compare field values, currently <code>EQUALS</code> or <code>INCLUDES</code>. Use the <code>EQUALS</code> operator to find channels whose memberships equal the specified values. Use the <code>INCLUDES</code> operator to find channels whose memberships include the specified values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchField) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_messaging.types.search_field_key

    out["Key"] = aws_sdk_chime_sdk_messaging.types.search_field_key.serialize_json(
        value["key"]
    )
    import aws_sdk_chime_sdk_messaging.types.search_field_values

    out["Values"] = (
        aws_sdk_chime_sdk_messaging.types.search_field_values.serialize_json(
            value["values"]
        )
    )
    import aws_sdk_chime_sdk_messaging.types.search_field_operator

    out["Operator"] = (
        aws_sdk_chime_sdk_messaging.types.search_field_operator.serialize_json(
            value["operator"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchField:
    out: SearchField = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_chime_sdk_messaging.types.search_field_key

        out["key"] = (
            aws_sdk_chime_sdk_messaging.types.search_field_key.deserialize_json(
                data["Key"]
            )
        )
    else:
        raise DeserializationError("SearchField.key required")
    if "Values" in data:
        import aws_sdk_chime_sdk_messaging.types.search_field_values

        out["values"] = (
            aws_sdk_chime_sdk_messaging.types.search_field_values.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("SearchField.values required")
    if "Operator" in data:
        import aws_sdk_chime_sdk_messaging.types.search_field_operator

        out["operator"] = (
            aws_sdk_chime_sdk_messaging.types.search_field_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("SearchField.operator required")
    return out
