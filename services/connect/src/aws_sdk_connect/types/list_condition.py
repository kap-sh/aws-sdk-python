"""Generated from Smithy shape ``com.amazonaws.connect#ListCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.conditions
    import aws_sdk_connect.types.target_list_type


class ListCondition(TypedDict):
    target_list_type: NotRequired[
        "aws_sdk_connect.types.target_list_type.TargetListType"
    ]
    """<p>The type of target list that will be used to filter the users.</p>"""
    conditions: NotRequired["aws_sdk_connect.types.conditions.Conditions"]
    """<p>A list of Condition objects which would be applied together with an AND condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCondition) -> dict:
    out: dict = {}
    if "target_list_type" in value:
        import aws_sdk_connect.types.target_list_type

        out["TargetListType"] = aws_sdk_connect.types.target_list_type.serialize_json(
            value["target_list_type"]
        )
    if "conditions" in value:
        import aws_sdk_connect.types.conditions

        out["Conditions"] = aws_sdk_connect.types.conditions.serialize_json(
            value["conditions"]
        )
    return out


def deserialize_json(data: dict) -> ListCondition:
    out: ListCondition = {}  # type: ignore[typeddict-item]
    if "TargetListType" in data:
        import aws_sdk_connect.types.target_list_type

        out["target_list_type"] = (
            aws_sdk_connect.types.target_list_type.deserialize_json(
                data["TargetListType"]
            )
        )
    if "Conditions" in data:
        import aws_sdk_connect.types.conditions

        out["conditions"] = aws_sdk_connect.types.conditions.deserialize_json(
            data["Conditions"]
        )
    return out
