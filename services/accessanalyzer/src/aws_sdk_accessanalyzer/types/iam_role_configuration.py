"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#IamRoleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.iam_trust_policy


class IamRoleConfiguration(TypedDict, closed=True):
    trust_policy: NotRequired[
        "aws_sdk_accessanalyzer.types.iam_trust_policy.IamTrustPolicy"
    ]
    """<p>The proposed trust policy for the IAM role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamRoleConfiguration) -> dict:
    out: dict = {}
    if "trust_policy" in value:
        out["trustPolicy"] = value["trust_policy"]
    return out


def deserialize_json(data: dict) -> IamRoleConfiguration:
    out: IamRoleConfiguration = {}  # type: ignore[typeddict-item]
    if "trustPolicy" in data:
        out["trust_policy"] = data["trustPolicy"]
    return out
