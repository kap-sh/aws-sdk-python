"""Generated from Smithy shape ``com.amazonaws.glue#SortCriterion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.sort
    import aws_sdk_glue.types.value_string


class SortCriterion(TypedDict, closed=True):
    field_name: NotRequired["aws_sdk_glue.types.value_string.ValueString"]
    """<p>The name of the field on which to sort.</p>"""
    sort: NotRequired["aws_sdk_glue.types.sort.Sort"]
    """<p>An ascending or descending sort.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortCriterion) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "sort" in value:
        import aws_sdk_glue.types.sort

        out["Sort"] = aws_sdk_glue.types.sort.serialize_aws_json_1_1(value["sort"])
    return out


def deserialize_aws_json_1_1(data: dict) -> SortCriterion:
    out: SortCriterion = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "Sort" in data:
        import aws_sdk_glue.types.sort

        out["sort"] = aws_sdk_glue.types.sort.deserialize_aws_json_1_1(data["Sort"])
    return out
