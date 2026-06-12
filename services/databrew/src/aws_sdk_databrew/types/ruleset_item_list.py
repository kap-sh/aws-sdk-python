"""Generated from Smithy shape ``com.amazonaws.databrew#RulesetItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.ruleset_item

RulesetItemList: TypeAlias = list["aws_sdk_databrew.types.ruleset_item.RulesetItem"]


# --- restJson1 ser/de ---
def serialize_json(value: RulesetItemList) -> list:
    import aws_sdk_databrew.types.ruleset_item

    out: list = []
    for item in value:
        out.append(aws_sdk_databrew.types.ruleset_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RulesetItemList:
    import aws_sdk_databrew.types.ruleset_item

    out: RulesetItemList = []
    for item in data:
        out.append(aws_sdk_databrew.types.ruleset_item.deserialize_json(item))
    return out
