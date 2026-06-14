"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedIamPrincipalInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.iam_principal_arn


class SubscribedIamPrincipalInput(TypedDict):
    identifier: NotRequired["aws_sdk_datazone.types.iam_principal_arn.IamPrincipalArn"]
    """<p>The ARN of the subscribed IAM principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedIamPrincipalInput) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> SubscribedIamPrincipalInput:
    out: SubscribedIamPrincipalInput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    return out
