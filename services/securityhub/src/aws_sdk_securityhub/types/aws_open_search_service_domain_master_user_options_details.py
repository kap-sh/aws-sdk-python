"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOpenSearchServiceDomainMasterUserOptionsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsOpenSearchServiceDomainMasterUserOptionsDetails(TypedDict):
    master_user_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) for the master user. </p>"""
    master_user_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The username for the master user. </p>"""
    master_user_password: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The password for the master user. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsOpenSearchServiceDomainMasterUserOptionsDetails) -> dict:
    out: dict = {}
    if "master_user_arn" in value:
        out["MasterUserArn"] = value["master_user_arn"]
    if "master_user_name" in value:
        out["MasterUserName"] = value["master_user_name"]
    if "master_user_password" in value:
        out["MasterUserPassword"] = value["master_user_password"]
    return out


def deserialize_json(data: dict) -> AwsOpenSearchServiceDomainMasterUserOptionsDetails:
    out: AwsOpenSearchServiceDomainMasterUserOptionsDetails = {}  # type: ignore[typeddict-item]
    if "MasterUserArn" in data:
        out["master_user_arn"] = data["MasterUserArn"]
    if "MasterUserName" in data:
        out["master_user_name"] = data["MasterUserName"]
    if "MasterUserPassword" in data:
        out["master_user_password"] = data["MasterUserPassword"]
    return out
