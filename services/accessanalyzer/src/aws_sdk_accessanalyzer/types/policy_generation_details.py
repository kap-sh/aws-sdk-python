"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#PolicyGenerationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.principal_arn


class PolicyGenerationDetails(TypedDict):
    principal_arn: "aws_sdk_accessanalyzer.types.principal_arn.PrincipalArn"
    """<p>The ARN of the IAM entity (user or role) for which you are generating a policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationDetails) -> dict:
    out: dict = {}
    out["principalArn"] = value["principal_arn"]
    return out


def deserialize_json(data: dict) -> PolicyGenerationDetails:
    out: PolicyGenerationDetails = {}  # type: ignore[typeddict-item]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    else:
        raise DeserializationError("PolicyGenerationDetails.principal_arn required")
    return out
