"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.string


class OpsItemIdentity(TypedDict, closed=True):
    arn: NotRequired["capo_ssm.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM entity that created the OpsItem event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemIdentity) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemIdentity:
    out: OpsItemIdentity = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
