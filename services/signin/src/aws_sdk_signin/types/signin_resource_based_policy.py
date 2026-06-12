"""Generated from Smithy shape ``com.amazonaws.signin#SigninResourceBasedPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signin.types.policy_statements


class SigninResourceBasedPolicy(TypedDict):
    version: NotRequired["str"]
    """Policy version"""
    statement: NotRequired["aws_sdk_signin.types.policy_statements.PolicyStatements"]
    """Policy statements"""


# --- restJson1 ser/de ---
def serialize_json(value: SigninResourceBasedPolicy) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    if "statement" in value:
        import aws_sdk_signin.types.policy_statements

        out["Statement"] = aws_sdk_signin.types.policy_statements.serialize_json(
            value["statement"]
        )
    return out


def deserialize_json(data: dict) -> SigninResourceBasedPolicy:
    out: SigninResourceBasedPolicy = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Statement" in data:
        import aws_sdk_signin.types.policy_statements

        out["statement"] = aws_sdk_signin.types.policy_statements.deserialize_json(
            data["Statement"]
        )
    return out
