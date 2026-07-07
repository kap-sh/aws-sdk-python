"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#Template``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pca_connector_ad.types.connector_arn
    import aws_sdk_pca_connector_ad.types.custom_object_identifier
    import aws_sdk_pca_connector_ad.types.template_arn
    import aws_sdk_pca_connector_ad.types.template_definition
    import aws_sdk_pca_connector_ad.types.template_name
    import aws_sdk_pca_connector_ad.types.template_revision
    import aws_sdk_pca_connector_ad.types.template_status


class Template(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_pca_connector_ad.types.template_arn.TemplateArn"]
    r"""<p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html\">CreateTemplate</a>.</p>"""
    connector_arn: NotRequired[
        "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn"
    ]
    r"""<p> The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>"""
    definition: NotRequired[
        "aws_sdk_pca_connector_ad.types.template_definition.TemplateDefinition"
    ]
    """<p>Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.</p>"""
    name: NotRequired["aws_sdk_pca_connector_ad.types.template_name.TemplateName"]
    """<p>Name of the templates. Template names must be unique.</p>"""
    object_identifier: NotRequired[
        "aws_sdk_pca_connector_ad.types.custom_object_identifier.CustomObjectIdentifier"
    ]
    """<p>Object identifier of a template.</p>"""
    policy_schema: NotRequired["int"]
    """<p>The template schema version. Template schema versions can be v2, v3, or v4. The template configuration options change based on the template schema version.</p>"""
    status: NotRequired["aws_sdk_pca_connector_ad.types.template_status.TemplateStatus"]
    """<p>Status of the template. Status can be creating, active, deleting, or failed.</p>"""
    revision: NotRequired[
        "aws_sdk_pca_connector_ad.types.template_revision.TemplateRevision"
    ]
    """<p>The version of the template. Template updates will increment the minor revision. Re-enrolling all certificate holders will increment the major revision.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the template was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the template was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Template) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "definition" in value:
        import aws_sdk_pca_connector_ad.types.template_definition

        out["Definition"] = (
            aws_sdk_pca_connector_ad.types.template_definition.serialize_json(
                value["definition"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "object_identifier" in value:
        out["ObjectIdentifier"] = value["object_identifier"]
    if "policy_schema" in value:
        out["PolicySchema"] = value["policy_schema"]
    if "status" in value:
        import aws_sdk_pca_connector_ad.types.template_status

        out["Status"] = aws_sdk_pca_connector_ad.types.template_status.serialize_json(
            value["status"]
        )
    if "revision" in value:
        import aws_sdk_pca_connector_ad.types.template_revision

        out["Revision"] = (
            aws_sdk_pca_connector_ad.types.template_revision.serialize_json(
                value["revision"]
            )
        )
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


def deserialize_json(data: dict) -> Template:
    out: Template = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    if "Definition" in data:
        import aws_sdk_pca_connector_ad.types.template_definition

        out["definition"] = (
            aws_sdk_pca_connector_ad.types.template_definition.deserialize_json(
                data["Definition"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    if "PolicySchema" in data:
        out["policy_schema"] = data["PolicySchema"]
    if "Status" in data:
        import aws_sdk_pca_connector_ad.types.template_status

        out["status"] = aws_sdk_pca_connector_ad.types.template_status.deserialize_json(
            data["Status"]
        )
    if "Revision" in data:
        import aws_sdk_pca_connector_ad.types.template_revision

        out["revision"] = (
            aws_sdk_pca_connector_ad.types.template_revision.deserialize_json(
                data["Revision"]
            )
        )
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
