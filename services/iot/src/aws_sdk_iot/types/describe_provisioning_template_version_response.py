"""Generated from Smithy shape ``com.amazonaws.iot#DescribeProvisioningTemplateVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.is_default_version
    import aws_sdk_iot.types.template_body
    import aws_sdk_iot.types.template_version_id


class DescribeProvisioningTemplateVersionResponse(TypedDict, closed=True):
    version_id: NotRequired["aws_sdk_iot.types.template_version_id.TemplateVersionId"]
    """<p>The provisioning template version ID.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date when the provisioning template version was created.</p>"""
    template_body: NotRequired["aws_sdk_iot.types.template_body.TemplateBody"]
    """<p>The JSON formatted contents of the provisioning template version.</p>"""
    is_default_version: "aws_sdk_iot.types.is_default_version.IsDefaultVersion"
    """<p>True if the provisioning template version is the default version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProvisioningTemplateVersionResponse) -> dict:
    out: dict = {}
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    if "creation_date" in value:
        import aws_sdk_iot.types.date_type

        out["creationDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    if "template_body" in value:
        out["templateBody"] = value["template_body"]
    out["isDefaultVersion"] = value.get("is_default_version", False)
    return out


def deserialize_json(data: dict) -> DescribeProvisioningTemplateVersionResponse:
    out: DescribeProvisioningTemplateVersionResponse = {}  # type: ignore[typeddict-item]
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    if "creationDate" in data:
        import aws_sdk_iot.types.date_type

        out["creation_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    if "templateBody" in data:
        out["template_body"] = data["templateBody"]
    if "isDefaultVersion" in data:
        out["is_default_version"] = data["isDefaultVersion"]
    else:
        out["is_default_version"] = False
    return out
