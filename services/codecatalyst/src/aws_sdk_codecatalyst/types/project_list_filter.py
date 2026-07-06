"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ProjectListFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.comparison_operator
    import aws_sdk_codecatalyst.types.filter_key
    import aws_sdk_codecatalyst.types.string_list


class ProjectListFilter(TypedDict, closed=True):
    key: "aws_sdk_codecatalyst.types.filter_key.FilterKey"
    """<p>A key that can be used to sort results.</p>"""
    values: "aws_sdk_codecatalyst.types.string_list.StringList"
    """<p>The values of the key.</p>"""
    comparison_operator: NotRequired[
        "aws_sdk_codecatalyst.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The operator used to compare the fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectListFilter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import aws_sdk_codecatalyst.types.string_list

    out["values"] = aws_sdk_codecatalyst.types.string_list.serialize_json(
        value["values"]
    )
    if "comparison_operator" in value:
        out["comparisonOperator"] = value["comparison_operator"]
    return out


def deserialize_json(data: dict) -> ProjectListFilter:
    out: ProjectListFilter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ProjectListFilter.key required")
    if "values" in data:
        import aws_sdk_codecatalyst.types.string_list

        out["values"] = aws_sdk_codecatalyst.types.string_list.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("ProjectListFilter.values required")
    if "comparisonOperator" in data:
        out["comparison_operator"] = data["comparisonOperator"]
    return out
