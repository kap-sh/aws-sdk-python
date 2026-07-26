"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceStandardObjectAttachmentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_field_name
    import capo_kendra.types.data_source_to_index_field_mapping_list


class SalesforceStandardObjectAttachmentConfiguration(TypedDict, closed=True):
    document_title_field_name: NotRequired[
        "capo_kendra.types.data_source_field_name.DataSourceFieldName"
    ]
    """<p>The name of the field used for the document title.</p>"""
    field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>One or more objects that map fields in attachments to Amazon Kendra index fields.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: SalesforceStandardObjectAttachmentConfiguration,
) -> dict:
    out: dict = {}
    if "document_title_field_name" in value:
        out["DocumentTitleFieldName"] = value["document_title_field_name"]
    if "field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> SalesforceStandardObjectAttachmentConfiguration:
    out: SalesforceStandardObjectAttachmentConfiguration = {}  # type: ignore[typeddict-item]
    if "DocumentTitleFieldName" in data:
        out["document_title_field_name"] = data["DocumentTitleFieldName"]
    if "FieldMappings" in data:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FieldMappings"]
            )
        )
    return out
