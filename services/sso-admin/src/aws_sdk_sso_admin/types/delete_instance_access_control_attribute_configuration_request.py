"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DeleteInstanceAccessControlAttributeConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn


class DeleteInstanceAccessControlAttributeConfigurationRequest(TypedDict):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteInstanceAccessControlAttributeConfigurationRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteInstanceAccessControlAttributeConfigurationRequest:
    out: DeleteInstanceAccessControlAttributeConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "DeleteInstanceAccessControlAttributeConfigurationRequest.instance_arn required"
        )
    return out
