"""Generated from Smithy shape ``com.amazonaws.glue#Predicate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.condition_list
    import aws_sdk_glue.types.logical


class Predicate(TypedDict):
    logical: NotRequired["aws_sdk_glue.types.logical.Logical"]
    """<p>An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.</p>"""
    conditions: NotRequired["aws_sdk_glue.types.condition_list.ConditionList"]
    """<p>A list of the conditions that determine when the trigger will fire.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Predicate) -> dict:
    out: dict = {}
    if "logical" in value:
        import aws_sdk_glue.types.logical

        out["Logical"] = aws_sdk_glue.types.logical.serialize_aws_json_1_1(
            value["logical"]
        )
    if "conditions" in value:
        import aws_sdk_glue.types.condition_list

        out["Conditions"] = aws_sdk_glue.types.condition_list.serialize_aws_json_1_1(
            value["conditions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Predicate:
    out: Predicate = {}  # type: ignore[typeddict-item]
    if "Logical" in data:
        import aws_sdk_glue.types.logical

        out["logical"] = aws_sdk_glue.types.logical.deserialize_aws_json_1_1(
            data["Logical"]
        )
    if "Conditions" in data:
        import aws_sdk_glue.types.condition_list

        out["conditions"] = aws_sdk_glue.types.condition_list.deserialize_aws_json_1_1(
            data["Conditions"]
        )
    return out
