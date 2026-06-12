"""Generated from Smithy shape ``com.amazonaws.ses#ConnectAction``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.connect_instance_arn
    import aws_sdk_ses.types.iam_role_arn


class ConnectAction(TypedDict):
    instance_arn: "aws_sdk_ses.types.connect_instance_arn.ConnectInstanceArn"
    """<p>The Amazon Resource Name (ARN) for the Amazon Connect instance that Amazon SES integrates with for starting email contacts.</p> <p>For more information about Amazon Connect instances, see the <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html\">Amazon Connect Administrator Guide</a> </p>"""
    iam_role_arn: "aws_sdk_ses.types.iam_role_arn.IAMRoleARN"
    """<p> The Amazon Resource Name (ARN) of the IAM role to be used by Amazon Simple Email Service while starting email contacts to the Amazon Connect instance. This role should have permission to invoke <code>connect:StartEmailContact</code> for the given Amazon Connect instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConnectAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.InstanceARN", str(value["instance_arn"])))
    pairs.append((f"{prefix}.IAMRoleARN", str(value["iam_role_arn"])))


def deserialize_query(el: Element) -> ConnectAction:
    out: ConnectAction = {}  # type: ignore[typeddict-item]
    child_instance_arn = el.find("InstanceARN")
    if child_instance_arn is not None:
        out["instance_arn"] = str(child_instance_arn.text or "")
    else:
        raise DeserializationError("ConnectAction.instance_arn required")
    child_iam_role_arn = el.find("IAMRoleARN")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    else:
        raise DeserializationError("ConnectAction.iam_role_arn required")
    return out
