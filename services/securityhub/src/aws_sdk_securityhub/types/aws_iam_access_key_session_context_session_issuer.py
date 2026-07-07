"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamAccessKeySessionContextSessionIssuer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsIamAccessKeySessionContextSessionIssuer(TypedDict, closed=True):
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of principal (user, role, or group) that created the session.</p>"""
    principal_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The principal ID of the principal (user, role, or group) that created the session.</p>"""
    arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the session.</p>"""
    account_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the Amazon Web Services account that created the session.</p>"""
    user_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the principal that created the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamAccessKeySessionContextSessionIssuer) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    return out


def deserialize_json(data: dict) -> AwsIamAccessKeySessionContextSessionIssuer:
    out: AwsIamAccessKeySessionContextSessionIssuer = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "PrincipalId" in data:
        out["principal_id"] = data["PrincipalId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    return out
