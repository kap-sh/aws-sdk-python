"""Generated from Smithy shape ``com.amazonaws.backup#Conditions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.condition_parameters


class Conditions(TypedDict):
    string_equals: NotRequired[
        "aws_sdk_backup.types.condition_parameters.ConditionParameters"
    ]
    """<p>Filters the values of your tagged resources for only those resources that you tagged with the same value. Also called \"exact matching.\"</p>"""
    string_not_equals: NotRequired[
        "aws_sdk_backup.types.condition_parameters.ConditionParameters"
    ]
    """<p>Filters the values of your tagged resources for only those resources that you tagged that do not have the same value. Also called \"negated matching.\"</p>"""
    string_like: NotRequired[
        "aws_sdk_backup.types.condition_parameters.ConditionParameters"
    ]
    """<p>Filters the values of your tagged resources for matching tag values with the use of a wildcard character (*) anywhere in the string. For example, \"prod*\" or \"*rod*\" matches the tag value \"production\".</p>"""
    string_not_like: NotRequired[
        "aws_sdk_backup.types.condition_parameters.ConditionParameters"
    ]
    """<p>Filters the values of your tagged resources for non-matching tag values with the use of a wildcard character (*) anywhere in the string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Conditions) -> dict:
    out: dict = {}
    if "string_equals" in value:
        import aws_sdk_backup.types.condition_parameters

        out["StringEquals"] = aws_sdk_backup.types.condition_parameters.serialize_json(
            value["string_equals"]
        )
    if "string_not_equals" in value:
        import aws_sdk_backup.types.condition_parameters

        out["StringNotEquals"] = (
            aws_sdk_backup.types.condition_parameters.serialize_json(
                value["string_not_equals"]
            )
        )
    if "string_like" in value:
        import aws_sdk_backup.types.condition_parameters

        out["StringLike"] = aws_sdk_backup.types.condition_parameters.serialize_json(
            value["string_like"]
        )
    if "string_not_like" in value:
        import aws_sdk_backup.types.condition_parameters

        out["StringNotLike"] = aws_sdk_backup.types.condition_parameters.serialize_json(
            value["string_not_like"]
        )
    return out


def deserialize_json(data: dict) -> Conditions:
    out: Conditions = {}  # type: ignore[typeddict-item]
    if "StringEquals" in data:
        import aws_sdk_backup.types.condition_parameters

        out["string_equals"] = (
            aws_sdk_backup.types.condition_parameters.deserialize_json(
                data["StringEquals"]
            )
        )
    if "StringNotEquals" in data:
        import aws_sdk_backup.types.condition_parameters

        out["string_not_equals"] = (
            aws_sdk_backup.types.condition_parameters.deserialize_json(
                data["StringNotEquals"]
            )
        )
    if "StringLike" in data:
        import aws_sdk_backup.types.condition_parameters

        out["string_like"] = aws_sdk_backup.types.condition_parameters.deserialize_json(
            data["StringLike"]
        )
    if "StringNotLike" in data:
        import aws_sdk_backup.types.condition_parameters

        out["string_not_like"] = (
            aws_sdk_backup.types.condition_parameters.deserialize_json(
                data["StringNotLike"]
            )
        )
    return out
