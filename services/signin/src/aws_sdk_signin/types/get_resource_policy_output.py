"""Generated from Smithy shape ``com.amazonaws.signin#GetResourcePolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_signin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signin.types.signin_resource_based_policy


class GetResourcePolicyOutput(TypedDict, closed=True):
    signin_resource_based_policy: (
        "aws_sdk_signin.types.signin_resource_based_policy.SigninResourceBasedPolicy"
    )
    """The account's SignIn resource-based policy"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePolicyOutput) -> dict:
    out: dict = {}
    import aws_sdk_signin.types.signin_resource_based_policy

    out["signinResourceBasedPolicy"] = (
        aws_sdk_signin.types.signin_resource_based_policy.serialize_json(
            value["signin_resource_based_policy"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetResourcePolicyOutput:
    out: GetResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if "signinResourceBasedPolicy" in data:
        import aws_sdk_signin.types.signin_resource_based_policy

        out["signin_resource_based_policy"] = (
            aws_sdk_signin.types.signin_resource_based_policy.deserialize_json(
                data["signinResourceBasedPolicy"]
            )
        )
    else:
        raise DeserializationError(
            "GetResourcePolicyOutput.signin_resource_based_policy required"
        )
    return out
