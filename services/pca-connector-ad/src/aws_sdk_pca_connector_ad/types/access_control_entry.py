"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#AccessControlEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pca_connector_ad.types.access_rights
    import aws_sdk_pca_connector_ad.types.display_name
    import aws_sdk_pca_connector_ad.types.group_security_identifier
    import aws_sdk_pca_connector_ad.types.template_arn


class AccessControlEntry(TypedDict, closed=True):
    group_display_name: NotRequired[
        "aws_sdk_pca_connector_ad.types.display_name.DisplayName"
    ]
    """<p>Name of the Active Directory group. This name does not need to match the group name in Active Directory.</p>"""
    group_security_identifier: NotRequired[
        "aws_sdk_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier"
    ]
    r"""<p>Security identifier (SID) of the group object from Active Directory. The SID starts with \"S-\".</p>"""
    access_rights: NotRequired[
        "aws_sdk_pca_connector_ad.types.access_rights.AccessRights"
    ]
    """<p>Permissions to allow or deny an Active Directory group to enroll or autoenroll certificates issued against a template.</p>"""
    template_arn: NotRequired["aws_sdk_pca_connector_ad.types.template_arn.TemplateArn"]
    r"""<p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the Access Control Entry was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the Access Control Entry was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessControlEntry) -> dict:
    out: dict = {}
    if "group_display_name" in value:
        out["GroupDisplayName"] = value["group_display_name"]
    if "group_security_identifier" in value:
        out["GroupSecurityIdentifier"] = value["group_security_identifier"]
    if "access_rights" in value:
        import aws_sdk_pca_connector_ad.types.access_rights

        out["AccessRights"] = (
            aws_sdk_pca_connector_ad.types.access_rights.serialize_json(
                value["access_rights"]
            )
        )
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    if "created_at" in value:
        import aws_sdk_pca_connector_ad.types._prelude.timestamp

        out["CreatedAt"] = (
            aws_sdk_pca_connector_ad.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_pca_connector_ad.types._prelude.timestamp

        out["UpdatedAt"] = (
            aws_sdk_pca_connector_ad.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccessControlEntry:
    out: AccessControlEntry = {}  # type: ignore[typeddict-item]
    if "GroupDisplayName" in data:
        out["group_display_name"] = data["GroupDisplayName"]
    if "GroupSecurityIdentifier" in data:
        out["group_security_identifier"] = data["GroupSecurityIdentifier"]
    if "AccessRights" in data:
        import aws_sdk_pca_connector_ad.types.access_rights

        out["access_rights"] = (
            aws_sdk_pca_connector_ad.types.access_rights.deserialize_json(
                data["AccessRights"]
            )
        )
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    if "CreatedAt" in data:
        import aws_sdk_pca_connector_ad.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_pca_connector_ad.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_pca_connector_ad.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_pca_connector_ad.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    return out
