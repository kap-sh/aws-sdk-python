"""Generated from Smithy shape ``com.amazonaws.elasticache#Authentication``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.authentication_type
    import aws_sdk_elasticache.types.integer_optional


class Authentication(TypedDict):
    type: NotRequired[
        "aws_sdk_elasticache.types.authentication_type.AuthenticationType"
    ]
    """<p>Indicates whether the user requires a password to authenticate.</p>"""
    password_count: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of passwords belonging to the user. The maximum is two.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Authentication, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type" in value:
        import aws_sdk_elasticache.types.authentication_type

        aws_sdk_elasticache.types.authentication_type.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "password_count" in value:
        pairs.append((f"{prefix}.PasswordCount", str(value["password_count"])))


def deserialize_query(el: Element) -> Authentication:
    out: Authentication = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_elasticache.types.authentication_type

        out["type"] = aws_sdk_elasticache.types.authentication_type.deserialize_query(
            child_type
        )
    child_password_count = el.find("PasswordCount")
    if child_password_count is not None:
        out["password_count"] = int(child_password_count.text or "")
    return out
