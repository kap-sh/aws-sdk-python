"""Generated from Smithy shape ``com.amazonaws.iam#GetAccountPasswordPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.password_policy


class GetAccountPasswordPolicyResponse(TypedDict):
    password_policy: "aws_sdk_iam.types.password_policy.PasswordPolicy"
    """<p>A structure that contains details about the account's password policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAccountPasswordPolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.password_policy

    aws_sdk_iam.types.password_policy.serialize_query(
        value["password_policy"], pairs, f"{prefix}.PasswordPolicy"
    )


def deserialize_query(el: Element) -> GetAccountPasswordPolicyResponse:
    out: GetAccountPasswordPolicyResponse = {}  # type: ignore[typeddict-item]
    child_password_policy = el.find("PasswordPolicy")
    if child_password_policy is not None:
        import aws_sdk_iam.types.password_policy

        out["password_policy"] = aws_sdk_iam.types.password_policy.deserialize_query(
            child_password_policy
        )
    else:
        raise DeserializationError(
            "GetAccountPasswordPolicyResponse.password_policy required"
        )
    return out
