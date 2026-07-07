"""Generated from Smithy shape ``com.amazonaws.qbusiness#SamlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.role_arn
    import aws_sdk_qbusiness.types.saml_attribute
    import aws_sdk_qbusiness.types.saml_metadata_xml


class SamlConfiguration(TypedDict, closed=True):
    metadata_xml: "aws_sdk_qbusiness.types.saml_metadata_xml.SamlMetadataXML"
    """<p>The metadata XML that your IdP generated.</p>"""
    role_arn: "aws_sdk_qbusiness.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role assumed by users when they authenticate into their Amazon Q Business web experience, containing the relevant Amazon Q Business permissions for conversing with Amazon Q Business.</p>"""
    user_id_attribute: "aws_sdk_qbusiness.types.saml_attribute.SamlAttribute"
    """<p>The user attribute name in your IdP that maps to the user email.</p>"""
    user_group_attribute: NotRequired[
        "aws_sdk_qbusiness.types.saml_attribute.SamlAttribute"
    ]
    """<p>The group attribute name in your IdP that maps to user groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamlConfiguration) -> dict:
    out: dict = {}
    out["metadataXML"] = value["metadata_xml"]
    out["roleArn"] = value["role_arn"]
    out["userIdAttribute"] = value["user_id_attribute"]
    if "user_group_attribute" in value:
        out["userGroupAttribute"] = value["user_group_attribute"]
    return out


def deserialize_json(data: dict) -> SamlConfiguration:
    out: SamlConfiguration = {}  # type: ignore[typeddict-item]
    if "metadataXML" in data:
        out["metadata_xml"] = data["metadataXML"]
    else:
        raise DeserializationError("SamlConfiguration.metadata_xml required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("SamlConfiguration.role_arn required")
    if "userIdAttribute" in data:
        out["user_id_attribute"] = data["userIdAttribute"]
    else:
        raise DeserializationError("SamlConfiguration.user_id_attribute required")
    if "userGroupAttribute" in data:
        out["user_group_attribute"] = data["userGroupAttribute"]
    return out
