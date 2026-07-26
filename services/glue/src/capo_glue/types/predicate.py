"""Generated from Smithy shape ``com.amazonaws.glue#Predicate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.condition_list
    import capo_glue.types.logical


class Predicate(TypedDict, closed=True):
    logical: NotRequired["capo_glue.types.logical.Logical"]
    """<p>An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.</p>"""
    conditions: NotRequired["capo_glue.types.condition_list.ConditionList"]
    """<p>A list of the conditions that determine when the trigger will fire.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Predicate) -> dict:
    out: dict = {}
    if "logical" in value:
        import capo_glue.types.logical

        out["Logical"] = capo_glue.types.logical.serialize_aws_json_1_1(
            value["logical"]
        )
    if "conditions" in value:
        import capo_glue.types.condition_list

        out["Conditions"] = capo_glue.types.condition_list.serialize_aws_json_1_1(
            value["conditions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Predicate:
    out: Predicate = {}  # type: ignore[typeddict-item]
    if "Logical" in data:
        import capo_glue.types.logical

        out["logical"] = capo_glue.types.logical.deserialize_aws_json_1_1(
            data["Logical"]
        )
    if "Conditions" in data:
        import capo_glue.types.condition_list

        out["conditions"] = capo_glue.types.condition_list.deserialize_aws_json_1_1(
            data["Conditions"]
        )
    return out
