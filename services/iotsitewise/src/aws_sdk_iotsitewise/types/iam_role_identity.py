"""Generated from Smithy shape ``com.amazonaws.iotsitewise#IAMRoleIdentity``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.iam_arn


class IAMRoleIdentity(TypedDict):
    arn: "aws_sdk_iotsitewise.types.iam_arn.IamArn"
    r"""<p>The ARN of the IAM role. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM ARNs</a> in the <i>IAM User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IAMRoleIdentity) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> IAMRoleIdentity:
    out: IAMRoleIdentity = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IAMRoleIdentity.arn required")
    return out
