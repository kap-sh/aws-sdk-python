"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreateInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn


class CreateInstanceResponse(TypedDict, closed=True):
    instance_arn: NotRequired["aws_sdk_sso_admin.types.instance_arn.InstanceArn"]
    r"""<p>The ARN of the instance of IAM Identity Center under which the operation will run. </p> <p>For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInstanceResponse) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInstanceResponse:
    out: CreateInstanceResponse = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    return out
