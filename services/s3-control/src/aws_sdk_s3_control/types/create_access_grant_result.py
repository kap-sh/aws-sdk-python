"""Generated from Smithy shape ``com.amazonaws.s3control#CreateAccessGrantResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.access_grant_arn
    import aws_sdk_s3_control.types.access_grant_id
    import aws_sdk_s3_control.types.access_grants_location_configuration
    import aws_sdk_s3_control.types.access_grants_location_id
    import aws_sdk_s3_control.types.creation_timestamp
    import aws_sdk_s3_control.types.grantee
    import aws_sdk_s3_control.types.identity_center_application_arn
    import aws_sdk_s3_control.types.permission
    import aws_sdk_s3_control.types.s3_prefix


class CreateAccessGrantResult(TypedDict, closed=True):
    created_at: NotRequired[
        "aws_sdk_s3_control.types.creation_timestamp.CreationTimestamp"
    ]
    """<p>The date and time when you created the access grant. </p>"""
    access_grant_id: NotRequired[
        "aws_sdk_s3_control.types.access_grant_id.AccessGrantId"
    ]
    """<p>The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access grant.</p>"""
    access_grant_arn: NotRequired[
        "aws_sdk_s3_control.types.access_grant_arn.AccessGrantArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the access grant. </p>"""
    grantee: NotRequired["aws_sdk_s3_control.types.grantee.Grantee"]
    """<p>The user, group, or role to which you are granting access. You can grant access to an IAM user or role. If you have added your corporate directory to Amazon Web Services IAM Identity Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee can also be a corporate directory user or group.</p>"""
    access_grants_location_id: NotRequired[
        "aws_sdk_s3_control.types.access_grants_location_id.AccessGrantsLocationId"
    ]
    """<p>The ID of the registered location to which you are granting access. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register. </p>"""
    access_grants_location_configuration: NotRequired[
        "aws_sdk_s3_control.types.access_grants_location_configuration.AccessGrantsLocationConfiguration"
    ]
    """<p>The configuration options of the grant location. The grant location is the S3 path to the data to which you are granting access. </p>"""
    permission: NotRequired["aws_sdk_s3_control.types.permission.Permission"]
    """<p>The type of access that you are granting to your S3 data, which can be set to one of the following values:</p> <ul> <li> <p> <code>READ</code> – Grant read-only access to the S3 data.</p> </li> <li> <p> <code>WRITE</code> – Grant write-only access to the S3 data.</p> </li> <li> <p> <code>READWRITE</code> – Grant both read and write access to the S3 data.</p> </li> </ul>"""
    application_arn: NotRequired[
        "aws_sdk_s3_control.types.identity_center_application_arn.IdentityCenterApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services IAM Identity Center application associated with your Identity Center instance. If the grant includes an application ARN, the grantee can only access the S3 data through this application. </p>"""
    grant_scope: NotRequired["aws_sdk_s3_control.types.s3_prefix.S3Prefix"]
    """<p>The S3 path of the data to which you are granting access. It is the result of appending the <code>Subprefix</code> to the location scope. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateAccessGrantResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "created_at" in value:
        import aws_sdk_s3_control.types.creation_timestamp

        aws_sdk_s3_control.types.creation_timestamp.serialize_xml(
            value["created_at"], el, "CreatedAt"
        )
    if "access_grant_id" in value:
        SubElement(el, "AccessGrantId").text = str(value["access_grant_id"])
    if "access_grant_arn" in value:
        SubElement(el, "AccessGrantArn").text = str(value["access_grant_arn"])
    if "grantee" in value:
        import aws_sdk_s3_control.types.grantee

        aws_sdk_s3_control.types.grantee.serialize_xml(value["grantee"], el, "Grantee")
    if "access_grants_location_id" in value:
        SubElement(el, "AccessGrantsLocationId").text = str(
            value["access_grants_location_id"]
        )
    if "access_grants_location_configuration" in value:
        import aws_sdk_s3_control.types.access_grants_location_configuration

        aws_sdk_s3_control.types.access_grants_location_configuration.serialize_xml(
            value["access_grants_location_configuration"],
            el,
            "AccessGrantsLocationConfiguration",
        )
    if "permission" in value:
        import aws_sdk_s3_control.types.permission

        aws_sdk_s3_control.types.permission.serialize_xml(
            value["permission"], el, "Permission"
        )
    if "application_arn" in value:
        SubElement(el, "ApplicationArn").text = str(value["application_arn"])
    if "grant_scope" in value:
        SubElement(el, "GrantScope").text = str(value["grant_scope"])


def deserialize_xml(el: Element) -> CreateAccessGrantResult:
    out: CreateAccessGrantResult = {}  # type: ignore[typeddict-item]
    child_created_at = el.find("CreatedAt")
    if child_created_at is not None:
        import aws_sdk_s3_control.types.creation_timestamp

        out["created_at"] = aws_sdk_s3_control.types.creation_timestamp.deserialize_xml(
            child_created_at
        )
    child_access_grant_id = el.find("AccessGrantId")
    if child_access_grant_id is not None:
        out["access_grant_id"] = str(child_access_grant_id.text or "")
    child_access_grant_arn = el.find("AccessGrantArn")
    if child_access_grant_arn is not None:
        out["access_grant_arn"] = str(child_access_grant_arn.text or "")
    child_grantee = el.find("Grantee")
    if child_grantee is not None:
        import aws_sdk_s3_control.types.grantee

        out["grantee"] = aws_sdk_s3_control.types.grantee.deserialize_xml(child_grantee)
    child_access_grants_location_id = el.find("AccessGrantsLocationId")
    if child_access_grants_location_id is not None:
        out["access_grants_location_id"] = str(
            child_access_grants_location_id.text or ""
        )
    child_access_grants_location_configuration = el.find(
        "AccessGrantsLocationConfiguration"
    )
    if child_access_grants_location_configuration is not None:
        import aws_sdk_s3_control.types.access_grants_location_configuration

        out["access_grants_location_configuration"] = (
            aws_sdk_s3_control.types.access_grants_location_configuration.deserialize_xml(
                child_access_grants_location_configuration
            )
        )
    child_permission = el.find("Permission")
    if child_permission is not None:
        import aws_sdk_s3_control.types.permission

        out["permission"] = aws_sdk_s3_control.types.permission.deserialize_xml(
            child_permission
        )
    child_application_arn = el.find("ApplicationArn")
    if child_application_arn is not None:
        out["application_arn"] = str(child_application_arn.text or "")
    child_grant_scope = el.find("GrantScope")
    if child_grant_scope is not None:
        out["grant_scope"] = str(child_grant_scope.text or "")
    return out
