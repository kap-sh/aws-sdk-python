"""Generated from Smithy shape ``com.amazonaws.qbusiness#ContentSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.retriever_content_source


class _ContentSource_retriever(TypedDict, closed=True):
    retriever: "capo_qbusiness.types.retriever_content_source.RetrieverContentSource"


ContentSource: TypeAlias = _ContentSource_retriever


# --- restJson1 ser/de ---
def serialize_json(value: ContentSource) -> dict:
    if "retriever" in value:
        import capo_qbusiness.types.retriever_content_source

        return {
            "retriever": capo_qbusiness.types.retriever_content_source.serialize_json(
                value["retriever"]
            )
        }
    else:
        raise SerializationError("ContentSource: no variant present")


def deserialize_json(data: dict) -> ContentSource:
    if "retriever" in data:
        import capo_qbusiness.types.retriever_content_source

        return {
            "retriever": capo_qbusiness.types.retriever_content_source.deserialize_json(
                data["retriever"]
            )
        }
    else:
        raise DeserializationError("ContentSource: no recognized variant key")
