"""Generated from Smithy shape ``com.amazonaws.backup#ProtectedResourceConditions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.key_value_list


class ProtectedResourceConditions(TypedDict):
    string_equals: NotRequired["aws_sdk_backup.types.key_value_list.KeyValueList"]
    """<p>Filters the values of your tagged resources for only those resources that you tagged with the same value. Also called \"exact matching.\"</p>"""
    string_not_equals: NotRequired["aws_sdk_backup.types.key_value_list.KeyValueList"]
    """<p>Filters the values of your tagged resources for only those resources that you tagged that do not have the same value. Also called \"negated matching.\"</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedResourceConditions) -> dict:
    out: dict = {}
    if "string_equals" in value:
        import aws_sdk_backup.types.key_value_list

        out["StringEquals"] = aws_sdk_backup.types.key_value_list.serialize_json(
            value["string_equals"]
        )
    if "string_not_equals" in value:
        import aws_sdk_backup.types.key_value_list

        out["StringNotEquals"] = aws_sdk_backup.types.key_value_list.serialize_json(
            value["string_not_equals"]
        )
    return out


def deserialize_json(data: dict) -> ProtectedResourceConditions:
    out: ProtectedResourceConditions = {}  # type: ignore[typeddict-item]
    if "StringEquals" in data:
        import aws_sdk_backup.types.key_value_list

        out["string_equals"] = aws_sdk_backup.types.key_value_list.deserialize_json(
            data["StringEquals"]
        )
    if "StringNotEquals" in data:
        import aws_sdk_backup.types.key_value_list

        out["string_not_equals"] = aws_sdk_backup.types.key_value_list.deserialize_json(
            data["StringNotEquals"]
        )
    return out
