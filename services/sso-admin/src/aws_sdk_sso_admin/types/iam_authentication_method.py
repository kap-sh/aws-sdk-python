"""Generated from Smithy shape ``com.amazonaws.ssoadmin#IamAuthenticationMethod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.actor_policy_document


class IamAuthenticationMethod(TypedDict, closed=True):
    actor_policy: "aws_sdk_sso_admin.types.actor_policy_document.ActorPolicyDocument"
    """<p>An IAM policy document in JSON.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IamAuthenticationMethod) -> dict:
    out: dict = {}
    out["ActorPolicy"] = value["actor_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IamAuthenticationMethod:
    out: IamAuthenticationMethod = {}  # type: ignore[typeddict-item]
    if "ActorPolicy" in data:
        out["actor_policy"] = data["ActorPolicy"]
    else:
        raise DeserializationError("IamAuthenticationMethod.actor_policy required")
    return out
