"""Generated from Smithy shape ``com.amazonaws.connect#DataTableValueEvaluationSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.attribute_name_list
    import aws_sdk_connect.types.primary_values_set


class DataTableValueEvaluationSet(TypedDict, closed=True):
    primary_values: NotRequired[
        "aws_sdk_connect.types.primary_values_set.PrimaryValuesSet"
    ]
    """<p>The set's primary values.</p>"""
    attribute_names: "aws_sdk_connect.types.attribute_name_list.AttributeNameList"
    """<p>The set's attribute names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataTableValueEvaluationSet) -> dict:
    out: dict = {}
    if "primary_values" in value:
        import aws_sdk_connect.types.primary_values_set

        out["PrimaryValues"] = aws_sdk_connect.types.primary_values_set.serialize_json(
            value["primary_values"]
        )
    import aws_sdk_connect.types.attribute_name_list

    out["AttributeNames"] = aws_sdk_connect.types.attribute_name_list.serialize_json(
        value["attribute_names"]
    )
    return out


def deserialize_json(data: dict) -> DataTableValueEvaluationSet:
    out: DataTableValueEvaluationSet = {}  # type: ignore[typeddict-item]
    if "PrimaryValues" in data:
        import aws_sdk_connect.types.primary_values_set

        out["primary_values"] = (
            aws_sdk_connect.types.primary_values_set.deserialize_json(
                data["PrimaryValues"]
            )
        )
    if "AttributeNames" in data:
        import aws_sdk_connect.types.attribute_name_list

        out["attribute_names"] = (
            aws_sdk_connect.types.attribute_name_list.deserialize_json(
                data["AttributeNames"]
            )
        )
    else:
        raise DeserializationError(
            "DataTableValueEvaluationSet.attribute_names required"
        )
    return out
