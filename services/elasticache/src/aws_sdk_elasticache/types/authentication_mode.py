"""Generated from Smithy shape ``com.amazonaws.elasticache#AuthenticationMode``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.input_authentication_type
    import aws_sdk_elasticache.types.password_list_input


class AuthenticationMode(TypedDict):
    type: NotRequired[
        "aws_sdk_elasticache.types.input_authentication_type.InputAuthenticationType"
    ]
    """<p>Specifies the authentication type. Possible options are IAM authentication, password and no password.</p>"""
    passwords: NotRequired[
        "aws_sdk_elasticache.types.password_list_input.PasswordListInput"
    ]
    """<p>Specifies the passwords to use for authentication if <code>Type</code> is set to <code>password</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthenticationMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type" in value:
        import aws_sdk_elasticache.types.input_authentication_type

        aws_sdk_elasticache.types.input_authentication_type.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "passwords" in value:
        import aws_sdk_elasticache.types.password_list_input

        aws_sdk_elasticache.types.password_list_input.serialize_query(
            value["passwords"], pairs, f"{prefix}.Passwords"
        )


def deserialize_query(el: Element) -> AuthenticationMode:
    out: AuthenticationMode = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_elasticache.types.input_authentication_type

        out["type"] = (
            aws_sdk_elasticache.types.input_authentication_type.deserialize_query(
                child_type
            )
        )
    child_passwords = el.find("Passwords")
    if child_passwords is not None:
        import aws_sdk_elasticache.types.password_list_input

        out["passwords"] = (
            aws_sdk_elasticache.types.password_list_input.deserialize_query(
                child_passwords
            )
        )
    return out
