"""Generated from Smithy shape ``com.amazonaws.wafv2#JsonPointerPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.json_pointer_path

JsonPointerPaths: TypeAlias = list["capo_wafv2.types.json_pointer_path.JsonPointerPath"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JsonPointerPaths) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> JsonPointerPaths:
    return list(data)
