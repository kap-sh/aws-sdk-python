"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentRelevanceOverrideConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.document_relevance_configuration

DocumentRelevanceOverrideConfigurationList: TypeAlias = list[
    "capo_kendra.types.document_relevance_configuration.DocumentRelevanceConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentRelevanceOverrideConfigurationList) -> list:
    import capo_kendra.types.document_relevance_configuration

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.document_relevance_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentRelevanceOverrideConfigurationList:
    import capo_kendra.types.document_relevance_configuration

    out: DocumentRelevanceOverrideConfigurationList = []
    for item in data:
        out.append(
            capo_kendra.types.document_relevance_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
