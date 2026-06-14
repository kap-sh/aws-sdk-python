"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.application_name
    import aws_sdk_qbusiness.types.description
    import aws_sdk_qbusiness.types.document_attribute_configurations
    import aws_sdk_qbusiness.types.index_capacity_configuration
    import aws_sdk_qbusiness.types.index_id


class UpdateIndexRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application connected to the index.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the Amazon Q Business index.</p>"""
    display_name: NotRequired[
        "aws_sdk_qbusiness.types.application_name.ApplicationName"
    ]
    """<p>The name of the Amazon Q Business index.</p>"""
    description: NotRequired["aws_sdk_qbusiness.types.description.Description"]
    """<p>The description of the Amazon Q Business index.</p>"""
    capacity_configuration: NotRequired[
        "aws_sdk_qbusiness.types.index_capacity_configuration.IndexCapacityConfiguration"
    ]
    """<p>The storage capacity units you want to provision for your Amazon Q Business index. You can add and remove capacity to fit your usage needs.</p>"""
    document_attribute_configurations: NotRequired[
        "aws_sdk_qbusiness.types.document_attribute_configurations.DocumentAttributeConfigurations"
    ]
    r"""<p>Configuration information for document metadata or fields. Document metadata are fields or attributes associated with your documents. For example, the company department name associated with each document. For more information, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/business-use-dg/doc-attributes-types.html#doc-attributes\">Understanding document attributes</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIndexRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "capacity_configuration" in value:
        import aws_sdk_qbusiness.types.index_capacity_configuration

        out["capacityConfiguration"] = (
            aws_sdk_qbusiness.types.index_capacity_configuration.serialize_json(
                value["capacity_configuration"]
            )
        )
    if "document_attribute_configurations" in value:
        import aws_sdk_qbusiness.types.document_attribute_configurations

        out["documentAttributeConfigurations"] = (
            aws_sdk_qbusiness.types.document_attribute_configurations.serialize_json(
                value["document_attribute_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateIndexRequest:
    out: UpdateIndexRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "capacityConfiguration" in data:
        import aws_sdk_qbusiness.types.index_capacity_configuration

        out["capacity_configuration"] = (
            aws_sdk_qbusiness.types.index_capacity_configuration.deserialize_json(
                data["capacityConfiguration"]
            )
        )
    if "documentAttributeConfigurations" in data:
        import aws_sdk_qbusiness.types.document_attribute_configurations

        out["document_attribute_configurations"] = (
            aws_sdk_qbusiness.types.document_attribute_configurations.deserialize_json(
                data["documentAttributeConfigurations"]
            )
        )
    return out
