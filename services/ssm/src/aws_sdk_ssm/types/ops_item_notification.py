"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemNotification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class OpsItemNotification(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of an Amazon Simple Notification Service (Amazon SNS) topic where notifications are sent when this OpsItem is edited or changed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemNotification) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemNotification:
    out: OpsItemNotification = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
