"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationLocation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.document_char_location
    import aws_sdk_bedrock_runtime.types.document_chunk_location
    import aws_sdk_bedrock_runtime.types.document_page_location
    import aws_sdk_bedrock_runtime.types.search_result_location
    import aws_sdk_bedrock_runtime.types.web_location


class _CitationLocation_web(TypedDict, closed=True):
    web: "aws_sdk_bedrock_runtime.types.web_location.WebLocation"


class _CitationLocation_documentChar(TypedDict, closed=True):
    documentChar: (
        "aws_sdk_bedrock_runtime.types.document_char_location.DocumentCharLocation"
    )


class _CitationLocation_documentPage(TypedDict, closed=True):
    documentPage: (
        "aws_sdk_bedrock_runtime.types.document_page_location.DocumentPageLocation"
    )


class _CitationLocation_documentChunk(TypedDict, closed=True):
    documentChunk: (
        "aws_sdk_bedrock_runtime.types.document_chunk_location.DocumentChunkLocation"
    )


class _CitationLocation_searchResultLocation(TypedDict, closed=True):
    searchResultLocation: (
        "aws_sdk_bedrock_runtime.types.search_result_location.SearchResultLocation"
    )


CitationLocation: TypeAlias = (
    _CitationLocation_web
    | _CitationLocation_documentChar
    | _CitationLocation_documentPage
    | _CitationLocation_documentChunk
    | _CitationLocation_searchResultLocation
)


# --- restJson1 ser/de ---
def serialize_json(value: CitationLocation) -> dict:
    if "web" in value:
        import aws_sdk_bedrock_runtime.types.web_location

        return {
            "web": aws_sdk_bedrock_runtime.types.web_location.serialize_json(
                value["web"]
            )
        }
    elif "documentChar" in value:
        import aws_sdk_bedrock_runtime.types.document_char_location

        return {
            "documentChar": aws_sdk_bedrock_runtime.types.document_char_location.serialize_json(
                value["documentChar"]
            )
        }
    elif "documentPage" in value:
        import aws_sdk_bedrock_runtime.types.document_page_location

        return {
            "documentPage": aws_sdk_bedrock_runtime.types.document_page_location.serialize_json(
                value["documentPage"]
            )
        }
    elif "documentChunk" in value:
        import aws_sdk_bedrock_runtime.types.document_chunk_location

        return {
            "documentChunk": aws_sdk_bedrock_runtime.types.document_chunk_location.serialize_json(
                value["documentChunk"]
            )
        }
    elif "searchResultLocation" in value:
        import aws_sdk_bedrock_runtime.types.search_result_location

        return {
            "searchResultLocation": aws_sdk_bedrock_runtime.types.search_result_location.serialize_json(
                value["searchResultLocation"]
            )
        }
    else:
        raise SerializationError("CitationLocation: no variant present")


def deserialize_json(data: dict) -> CitationLocation:
    if "web" in data:
        import aws_sdk_bedrock_runtime.types.web_location

        return {
            "web": aws_sdk_bedrock_runtime.types.web_location.deserialize_json(
                data["web"]
            )
        }
    elif "documentChar" in data:
        import aws_sdk_bedrock_runtime.types.document_char_location

        return {
            "documentChar": aws_sdk_bedrock_runtime.types.document_char_location.deserialize_json(
                data["documentChar"]
            )
        }
    elif "documentPage" in data:
        import aws_sdk_bedrock_runtime.types.document_page_location

        return {
            "documentPage": aws_sdk_bedrock_runtime.types.document_page_location.deserialize_json(
                data["documentPage"]
            )
        }
    elif "documentChunk" in data:
        import aws_sdk_bedrock_runtime.types.document_chunk_location

        return {
            "documentChunk": aws_sdk_bedrock_runtime.types.document_chunk_location.deserialize_json(
                data["documentChunk"]
            )
        }
    elif "searchResultLocation" in data:
        import aws_sdk_bedrock_runtime.types.search_result_location

        return {
            "searchResultLocation": aws_sdk_bedrock_runtime.types.search_result_location.deserialize_json(
                data["searchResultLocation"]
            )
        }
    else:
        raise DeserializationError("CitationLocation: no recognized variant key")
