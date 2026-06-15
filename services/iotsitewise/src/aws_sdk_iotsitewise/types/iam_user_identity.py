"""Generated from Smithy shape ``com.amazonaws.iotsitewise#IAMUserIdentity``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.iam_arn


class IAMUserIdentity(TypedDict):
    arn: "aws_sdk_iotsitewise.types.iam_arn.IamArn"
    r"""<p>The ARN of the IAM user. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\">IAM ARNs</a> in the <i>IAM User Guide</i>.</p> <note> <p>If you delete the IAM user, access policies that contain this identity include an empty <code>arn</code>. You can delete the access policy for the IAM user that no longer exists.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: IAMUserIdentity) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> IAMUserIdentity:
    out: IAMUserIdentity = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IAMUserIdentity.arn required")
    return out
