"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentRelevanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.document_metadata_configuration_name
    import aws_sdk_kendra.types.relevance


class DocumentRelevanceConfiguration(TypedDict, closed=True):
    name: "aws_sdk_kendra.types.document_metadata_configuration_name.DocumentMetadataConfigurationName"
    """<p>The name of the index field.</p>"""
    relevance: "aws_sdk_kendra.types.relevance.Relevance"
    """<p>Provides information for tuning the relevance of a field in a search. When a query includes terms that match the field, the results are given a boost in the response based on these tuning parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentRelevanceConfiguration) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_kendra.types.relevance

    out["Relevance"] = aws_sdk_kendra.types.relevance.serialize_aws_json_1_1(
        value["relevance"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentRelevanceConfiguration:
    out: DocumentRelevanceConfiguration = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DocumentRelevanceConfiguration.name required")
    if "Relevance" in data:
        import aws_sdk_kendra.types.relevance

        out["relevance"] = aws_sdk_kendra.types.relevance.deserialize_aws_json_1_1(
            data["Relevance"]
        )
    else:
        raise DeserializationError("DocumentRelevanceConfiguration.relevance required")
    return out
