"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentMetadataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_attribute_value_type
    import aws_sdk_kendra.types.document_metadata_configuration_name
    import aws_sdk_kendra.types.relevance
    import aws_sdk_kendra.types.search


class DocumentMetadataConfiguration(TypedDict, closed=True):
    name: "aws_sdk_kendra.types.document_metadata_configuration_name.DocumentMetadataConfigurationName"
    """<p>The name of the index field.</p>"""
    type: (
        "aws_sdk_kendra.types.document_attribute_value_type.DocumentAttributeValueType"
    )
    """<p>The data type of the index field. </p>"""
    relevance: NotRequired["aws_sdk_kendra.types.relevance.Relevance"]
    """<p>Provides tuning parameters to determine how the field affects the search results.</p>"""
    search: NotRequired["aws_sdk_kendra.types.search.Search"]
    """<p>Provides information about how the field is used during a search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentMetadataConfiguration) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_kendra.types.document_attribute_value_type

    out["Type"] = (
        aws_sdk_kendra.types.document_attribute_value_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    if "relevance" in value:
        import aws_sdk_kendra.types.relevance

        out["Relevance"] = aws_sdk_kendra.types.relevance.serialize_aws_json_1_1(
            value["relevance"]
        )
    if "search" in value:
        import aws_sdk_kendra.types.search

        out["Search"] = aws_sdk_kendra.types.search.serialize_aws_json_1_1(
            value["search"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentMetadataConfiguration:
    out: DocumentMetadataConfiguration = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DocumentMetadataConfiguration.name required")
    if "Type" in data:
        import aws_sdk_kendra.types.document_attribute_value_type

        out["type"] = (
            aws_sdk_kendra.types.document_attribute_value_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("DocumentMetadataConfiguration.type required")
    if "Relevance" in data:
        import aws_sdk_kendra.types.relevance

        out["relevance"] = aws_sdk_kendra.types.relevance.deserialize_aws_json_1_1(
            data["Relevance"]
        )
    if "Search" in data:
        import aws_sdk_kendra.types.search

        out["search"] = aws_sdk_kendra.types.search.deserialize_aws_json_1_1(
            data["Search"]
        )
    return out
