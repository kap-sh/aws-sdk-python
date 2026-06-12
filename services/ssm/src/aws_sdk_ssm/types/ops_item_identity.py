"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemIdentity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class OpsItemIdentity(TypedDict):
    arn: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM entity that created the OpsItem event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemIdentity) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemIdentity:
    out: OpsItemIdentity = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
