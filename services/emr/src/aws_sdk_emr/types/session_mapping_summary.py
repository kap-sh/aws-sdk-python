"""Generated from Smithy shape ``com.amazonaws.emr#SessionMappingSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.identity_type
    import aws_sdk_emr.types.xml_string_max_len256


class SessionMappingSummary(TypedDict):
    studio_id: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The ID of the Amazon EMR Studio.</p>"""
    identity_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The globally unique identifier (GUID) of the user or group from the IAM Identity Center Identity Store.</p>"""
    identity_name: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    r"""<p>The name of the user or group. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName\">UserName</a> and <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName\">DisplayName</a> in the <i>IAM Identity Center Identity Store API Reference</i>.</p>"""
    identity_type: NotRequired["aws_sdk_emr.types.identity_type.IdentityType"]
    """<p>Specifies whether the identity mapped to the Amazon EMR Studio is a user or a group.</p>"""
    session_policy_arn: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The Amazon Resource Name (ARN) of the session policy associated with the user or group.</p>"""
    creation_time: NotRequired["aws_sdk_emr.types.date.Date"]
    """<p>The time the session mapping was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionMappingSummary) -> dict:
    out: dict = {}
    if "studio_id" in value:
        out["StudioId"] = value["studio_id"]
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "identity_name" in value:
        out["IdentityName"] = value["identity_name"]
    if "identity_type" in value:
        import aws_sdk_emr.types.identity_type

        out["IdentityType"] = aws_sdk_emr.types.identity_type.serialize_aws_json_1_1(
            value["identity_type"]
        )
    if "session_policy_arn" in value:
        out["SessionPolicyArn"] = value["session_policy_arn"]
    if "creation_time" in value:
        import aws_sdk_emr.types.date

        out["CreationTime"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionMappingSummary:
    out: SessionMappingSummary = {}  # type: ignore[typeddict-item]
    if "StudioId" in data:
        out["studio_id"] = data["StudioId"]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    if "IdentityName" in data:
        out["identity_name"] = data["IdentityName"]
    if "IdentityType" in data:
        import aws_sdk_emr.types.identity_type

        out["identity_type"] = aws_sdk_emr.types.identity_type.deserialize_aws_json_1_1(
            data["IdentityType"]
        )
    if "SessionPolicyArn" in data:
        out["session_policy_arn"] = data["SessionPolicyArn"]
    if "CreationTime" in data:
        import aws_sdk_emr.types.date

        out["creation_time"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
