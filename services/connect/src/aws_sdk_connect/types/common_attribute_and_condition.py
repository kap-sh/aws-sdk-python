"""Generated from Smithy shape ``com.amazonaws.connect#CommonAttributeAndCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.tag_and_condition_list


class CommonAttributeAndCondition(TypedDict):
    tag_conditions: NotRequired[
        "aws_sdk_connect.types.tag_and_condition_list.TagAndConditionList"
    ]
    """<p>A leaf node condition which can be used to specify a tag condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommonAttributeAndCondition) -> dict:
    out: dict = {}
    if "tag_conditions" in value:
        import aws_sdk_connect.types.tag_and_condition_list

        out["TagConditions"] = (
            aws_sdk_connect.types.tag_and_condition_list.serialize_json(
                value["tag_conditions"]
            )
        )
    return out


def deserialize_json(data: dict) -> CommonAttributeAndCondition:
    out: CommonAttributeAndCondition = {}  # type: ignore[typeddict-item]
    if "TagConditions" in data:
        import aws_sdk_connect.types.tag_and_condition_list

        out["tag_conditions"] = (
            aws_sdk_connect.types.tag_and_condition_list.deserialize_json(
                data["TagConditions"]
            )
        )
    return out
