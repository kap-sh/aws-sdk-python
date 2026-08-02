"""Generated from Smithy shape ``com.amazonaws.iam#GetAccountPasswordPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.password_policy


class GetAccountPasswordPolicyResponse(TypedDict, closed=True):
    password_policy: "capo_iam.types.password_policy.PasswordPolicy"
    """<p>A structure that contains details about the account's password policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetAccountPasswordPolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.password_policy

    capo_iam.types.password_policy.serialize_query(
        value["password_policy"], pairs, f"{key_prefix}PasswordPolicy"
    )


def deserialize_query(el: Element) -> GetAccountPasswordPolicyResponse:
    out: GetAccountPasswordPolicyResponse = {}  # type: ignore[typeddict-item]
    child_password_policy = el.find("PasswordPolicy")
    if child_password_policy is not None:
        import capo_iam.types.password_policy

        out["password_policy"] = capo_iam.types.password_policy.deserialize_query(
            child_password_policy
        )
    else:
        raise DeserializationError(
            "GetAccountPasswordPolicyResponse.password_policy required"
        )
    return out
