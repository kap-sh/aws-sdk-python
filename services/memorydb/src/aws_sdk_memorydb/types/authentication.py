"""Generated from Smithy shape ``com.amazonaws.memorydb#Authentication``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.authentication_type
    import aws_sdk_memorydb.types.integer_optional


class Authentication(TypedDict):
    type: NotRequired["aws_sdk_memorydb.types.authentication_type.AuthenticationType"]
    """<p>Indicates whether the user requires a password to authenticate.</p>"""
    password_count: NotRequired[
        "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of passwords belonging to the user. The maximum is two.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Authentication) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_memorydb.types.authentication_type

        out["Type"] = aws_sdk_memorydb.types.authentication_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "password_count" in value:
        out["PasswordCount"] = value["password_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Authentication:
    out: Authentication = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_memorydb.types.authentication_type

        out["type"] = (
            aws_sdk_memorydb.types.authentication_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "PasswordCount" in data:
        out["password_count"] = data["PasswordCount"]
    return out
