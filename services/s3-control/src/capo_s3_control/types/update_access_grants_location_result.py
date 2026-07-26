"""Generated from Smithy shape ``com.amazonaws.s3control#UpdateAccessGrantsLocationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.access_grants_location_arn
    import capo_s3_control.types.access_grants_location_id
    import capo_s3_control.types.creation_timestamp
    import capo_s3_control.types.iam_role_arn
    import capo_s3_control.types.s3_prefix


class UpdateAccessGrantsLocationResult(TypedDict, closed=True):
    created_at: NotRequired[
        "capo_s3_control.types.creation_timestamp.CreationTimestamp"
    ]
    """<p>The date and time when you registered the location. </p>"""
    access_grants_location_id: NotRequired[
        "capo_s3_control.types.access_grants_location_id.AccessGrantsLocationId"
    ]
    """<p>The ID of the registered location to which you are granting access. S3 Access Grants assigned this ID when you registered the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register. </p>"""
    access_grants_location_arn: NotRequired[
        "capo_s3_control.types.access_grants_location_arn.AccessGrantsLocationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the registered location that you are updating. </p>"""
    location_scope: NotRequired["capo_s3_control.types.s3_prefix.S3Prefix"]
    """<p>The S3 URI path of the location that you are updating. You cannot update the scope of the registered location. The location scope can be the default S3 location <code>s3://</code>, the S3 path to a bucket <code>s3://<bucket></code>, or the S3 path to a bucket and prefix <code>s3://<bucket>/<prefix></code>. </p>"""
    iam_role_arn: NotRequired["capo_s3_control.types.iam_role_arn.IAMRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role of the registered location. S3 Access Grants assumes this role to manage access to the registered location. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateAccessGrantsLocationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "created_at" in value:
        import capo_s3_control.types.creation_timestamp

        capo_s3_control.types.creation_timestamp.serialize_xml(
            value["created_at"], el, "CreatedAt"
        )
    if "access_grants_location_id" in value:
        SubElement(el, "AccessGrantsLocationId").text = str(
            value["access_grants_location_id"]
        )
    if "access_grants_location_arn" in value:
        SubElement(el, "AccessGrantsLocationArn").text = str(
            value["access_grants_location_arn"]
        )
    if "location_scope" in value:
        SubElement(el, "LocationScope").text = str(value["location_scope"])
    if "iam_role_arn" in value:
        SubElement(el, "IAMRoleArn").text = str(value["iam_role_arn"])


def deserialize_xml(el: Element) -> UpdateAccessGrantsLocationResult:
    out: UpdateAccessGrantsLocationResult = {}  # type: ignore[typeddict-item]
    child_created_at = el.find("CreatedAt")
    if child_created_at is not None:
        import capo_s3_control.types.creation_timestamp

        out["created_at"] = capo_s3_control.types.creation_timestamp.deserialize_xml(
            child_created_at
        )
    child_access_grants_location_id = el.find("AccessGrantsLocationId")
    if child_access_grants_location_id is not None:
        out["access_grants_location_id"] = str(
            child_access_grants_location_id.text or ""
        )
    child_access_grants_location_arn = el.find("AccessGrantsLocationArn")
    if child_access_grants_location_arn is not None:
        out["access_grants_location_arn"] = str(
            child_access_grants_location_arn.text or ""
        )
    child_location_scope = el.find("LocationScope")
    if child_location_scope is not None:
        out["location_scope"] = str(child_location_scope.text or "")
    child_iam_role_arn = el.find("IAMRoleArn")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    return out
