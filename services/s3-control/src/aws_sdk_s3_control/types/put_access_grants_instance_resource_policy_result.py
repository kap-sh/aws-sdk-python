"""Generated from Smithy shape ``com.amazonaws.s3control#PutAccessGrantsInstanceResourcePolicyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.creation_timestamp
    import aws_sdk_s3_control.types.organization
    import aws_sdk_s3_control.types.policy_document


class PutAccessGrantsInstanceResourcePolicyResult(TypedDict, closed=True):
    policy: NotRequired["aws_sdk_s3_control.types.policy_document.PolicyDocument"]
    """<p>The updated resource policy of the S3 Access Grants instance.</p>"""
    organization: NotRequired["aws_sdk_s3_control.types.organization.Organization"]
    """<p>The Organization of the resource policy of the S3 Access Grants instance.</p>"""
    created_at: NotRequired[
        "aws_sdk_s3_control.types.creation_timestamp.CreationTimestamp"
    ]
    """<p>The date and time when you created the S3 Access Grants instance resource policy. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutAccessGrantsInstanceResourcePolicyResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "policy" in value:
        SubElement(el, "Policy").text = str(value["policy"])
    if "organization" in value:
        SubElement(el, "Organization").text = str(value["organization"])
    if "created_at" in value:
        import aws_sdk_s3_control.types.creation_timestamp

        aws_sdk_s3_control.types.creation_timestamp.serialize_xml(
            value["created_at"], el, "CreatedAt"
        )


def deserialize_xml(el: Element) -> PutAccessGrantsInstanceResourcePolicyResult:
    out: PutAccessGrantsInstanceResourcePolicyResult = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    child_organization = el.find("Organization")
    if child_organization is not None:
        out["organization"] = str(child_organization.text or "")
    child_created_at = el.find("CreatedAt")
    if child_created_at is not None:
        import aws_sdk_s3_control.types.creation_timestamp

        out["created_at"] = aws_sdk_s3_control.types.creation_timestamp.deserialize_xml(
            child_created_at
        )
    return out
