"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedIamPrincipal``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.iam_principal_arn


class SubscribedIamPrincipal(TypedDict):
    principal_arn: NotRequired[
        "aws_sdk_datazone.types.iam_principal_arn.IamPrincipalArn"
    ]
    """<p>The ARN of the subscribed IAM principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedIamPrincipal) -> dict:
    out: dict = {}
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    return out


def deserialize_json(data: dict) -> SubscribedIamPrincipal:
    out: SubscribedIamPrincipal = {}  # type: ignore[typeddict-item]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    return out
