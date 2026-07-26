"""Generated from Smithy shape ``com.amazonaws.qconnect#DataDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.case_summarization_chunk_data_details
    import capo_qconnect.types.content_data_details
    import capo_qconnect.types.email_generative_answer_chunk_data_details
    import capo_qconnect.types.email_overview_chunk_data_details
    import capo_qconnect.types.email_response_chunk_data_details
    import capo_qconnect.types.generative_chunk_data_details
    import capo_qconnect.types.generative_data_details
    import capo_qconnect.types.intent_detected_data_details
    import capo_qconnect.types.notes_chunk_data_details
    import capo_qconnect.types.notes_data_details
    import capo_qconnect.types.source_content_data_details
    import capo_qconnect.types.suggested_message_data_details


class _DataDetails_contentData(TypedDict, closed=True):
    contentData: "capo_qconnect.types.content_data_details.ContentDataDetails"


class _DataDetails_generativeData(TypedDict, closed=True):
    generativeData: "capo_qconnect.types.generative_data_details.GenerativeDataDetails"


class _DataDetails_intentDetectedData(TypedDict, closed=True):
    intentDetectedData: (
        "capo_qconnect.types.intent_detected_data_details.IntentDetectedDataDetails"
    )


class _DataDetails_sourceContentData(TypedDict, closed=True):
    sourceContentData: (
        "capo_qconnect.types.source_content_data_details.SourceContentDataDetails"
    )


class _DataDetails_generativeChunkData(TypedDict, closed=True):
    generativeChunkData: (
        "capo_qconnect.types.generative_chunk_data_details.GenerativeChunkDataDetails"
    )


class _DataDetails_emailResponseChunkData(TypedDict, closed=True):
    emailResponseChunkData: "capo_qconnect.types.email_response_chunk_data_details.EmailResponseChunkDataDetails"


class _DataDetails_emailOverviewChunkData(TypedDict, closed=True):
    emailOverviewChunkData: "capo_qconnect.types.email_overview_chunk_data_details.EmailOverviewChunkDataDetails"


class _DataDetails_emailGenerativeAnswerChunkData(TypedDict, closed=True):
    emailGenerativeAnswerChunkData: "capo_qconnect.types.email_generative_answer_chunk_data_details.EmailGenerativeAnswerChunkDataDetails"


class _DataDetails_caseSummarizationChunkData(TypedDict, closed=True):
    caseSummarizationChunkData: "capo_qconnect.types.case_summarization_chunk_data_details.CaseSummarizationChunkDataDetails"


class _DataDetails_suggestedMessageData(TypedDict, closed=True):
    suggestedMessageData: (
        "capo_qconnect.types.suggested_message_data_details.SuggestedMessageDataDetails"
    )


class _DataDetails_notesData(TypedDict, closed=True):
    notesData: "capo_qconnect.types.notes_data_details.NotesDataDetails"


class _DataDetails_notesChunkData(TypedDict, closed=True):
    notesChunkData: "capo_qconnect.types.notes_chunk_data_details.NotesChunkDataDetails"


DataDetails: TypeAlias = (
    _DataDetails_contentData
    | _DataDetails_generativeData
    | _DataDetails_intentDetectedData
    | _DataDetails_sourceContentData
    | _DataDetails_generativeChunkData
    | _DataDetails_emailResponseChunkData
    | _DataDetails_emailOverviewChunkData
    | _DataDetails_emailGenerativeAnswerChunkData
    | _DataDetails_caseSummarizationChunkData
    | _DataDetails_suggestedMessageData
    | _DataDetails_notesData
    | _DataDetails_notesChunkData
)


# --- restJson1 ser/de ---
def serialize_json(value: DataDetails) -> dict:
    if "contentData" in value:
        import capo_qconnect.types.content_data_details

        return {
            "contentData": capo_qconnect.types.content_data_details.serialize_json(
                value["contentData"]
            )
        }
    elif "generativeData" in value:
        import capo_qconnect.types.generative_data_details

        return {
            "generativeData": capo_qconnect.types.generative_data_details.serialize_json(
                value["generativeData"]
            )
        }
    elif "intentDetectedData" in value:
        import capo_qconnect.types.intent_detected_data_details

        return {
            "intentDetectedData": capo_qconnect.types.intent_detected_data_details.serialize_json(
                value["intentDetectedData"]
            )
        }
    elif "sourceContentData" in value:
        import capo_qconnect.types.source_content_data_details

        return {
            "sourceContentData": capo_qconnect.types.source_content_data_details.serialize_json(
                value["sourceContentData"]
            )
        }
    elif "generativeChunkData" in value:
        import capo_qconnect.types.generative_chunk_data_details

        return {
            "generativeChunkData": capo_qconnect.types.generative_chunk_data_details.serialize_json(
                value["generativeChunkData"]
            )
        }
    elif "emailResponseChunkData" in value:
        import capo_qconnect.types.email_response_chunk_data_details

        return {
            "emailResponseChunkData": capo_qconnect.types.email_response_chunk_data_details.serialize_json(
                value["emailResponseChunkData"]
            )
        }
    elif "emailOverviewChunkData" in value:
        import capo_qconnect.types.email_overview_chunk_data_details

        return {
            "emailOverviewChunkData": capo_qconnect.types.email_overview_chunk_data_details.serialize_json(
                value["emailOverviewChunkData"]
            )
        }
    elif "emailGenerativeAnswerChunkData" in value:
        import capo_qconnect.types.email_generative_answer_chunk_data_details

        return {
            "emailGenerativeAnswerChunkData": capo_qconnect.types.email_generative_answer_chunk_data_details.serialize_json(
                value["emailGenerativeAnswerChunkData"]
            )
        }
    elif "caseSummarizationChunkData" in value:
        import capo_qconnect.types.case_summarization_chunk_data_details

        return {
            "caseSummarizationChunkData": capo_qconnect.types.case_summarization_chunk_data_details.serialize_json(
                value["caseSummarizationChunkData"]
            )
        }
    elif "suggestedMessageData" in value:
        import capo_qconnect.types.suggested_message_data_details

        return {
            "suggestedMessageData": capo_qconnect.types.suggested_message_data_details.serialize_json(
                value["suggestedMessageData"]
            )
        }
    elif "notesData" in value:
        import capo_qconnect.types.notes_data_details

        return {
            "notesData": capo_qconnect.types.notes_data_details.serialize_json(
                value["notesData"]
            )
        }
    elif "notesChunkData" in value:
        import capo_qconnect.types.notes_chunk_data_details

        return {
            "notesChunkData": capo_qconnect.types.notes_chunk_data_details.serialize_json(
                value["notesChunkData"]
            )
        }
    else:
        raise SerializationError("DataDetails: no variant present")


def deserialize_json(data: dict) -> DataDetails:
    if "contentData" in data:
        import capo_qconnect.types.content_data_details

        return {
            "contentData": capo_qconnect.types.content_data_details.deserialize_json(
                data["contentData"]
            )
        }
    elif "generativeData" in data:
        import capo_qconnect.types.generative_data_details

        return {
            "generativeData": capo_qconnect.types.generative_data_details.deserialize_json(
                data["generativeData"]
            )
        }
    elif "intentDetectedData" in data:
        import capo_qconnect.types.intent_detected_data_details

        return {
            "intentDetectedData": capo_qconnect.types.intent_detected_data_details.deserialize_json(
                data["intentDetectedData"]
            )
        }
    elif "sourceContentData" in data:
        import capo_qconnect.types.source_content_data_details

        return {
            "sourceContentData": capo_qconnect.types.source_content_data_details.deserialize_json(
                data["sourceContentData"]
            )
        }
    elif "generativeChunkData" in data:
        import capo_qconnect.types.generative_chunk_data_details

        return {
            "generativeChunkData": capo_qconnect.types.generative_chunk_data_details.deserialize_json(
                data["generativeChunkData"]
            )
        }
    elif "emailResponseChunkData" in data:
        import capo_qconnect.types.email_response_chunk_data_details

        return {
            "emailResponseChunkData": capo_qconnect.types.email_response_chunk_data_details.deserialize_json(
                data["emailResponseChunkData"]
            )
        }
    elif "emailOverviewChunkData" in data:
        import capo_qconnect.types.email_overview_chunk_data_details

        return {
            "emailOverviewChunkData": capo_qconnect.types.email_overview_chunk_data_details.deserialize_json(
                data["emailOverviewChunkData"]
            )
        }
    elif "emailGenerativeAnswerChunkData" in data:
        import capo_qconnect.types.email_generative_answer_chunk_data_details

        return {
            "emailGenerativeAnswerChunkData": capo_qconnect.types.email_generative_answer_chunk_data_details.deserialize_json(
                data["emailGenerativeAnswerChunkData"]
            )
        }
    elif "caseSummarizationChunkData" in data:
        import capo_qconnect.types.case_summarization_chunk_data_details

        return {
            "caseSummarizationChunkData": capo_qconnect.types.case_summarization_chunk_data_details.deserialize_json(
                data["caseSummarizationChunkData"]
            )
        }
    elif "suggestedMessageData" in data:
        import capo_qconnect.types.suggested_message_data_details

        return {
            "suggestedMessageData": capo_qconnect.types.suggested_message_data_details.deserialize_json(
                data["suggestedMessageData"]
            )
        }
    elif "notesData" in data:
        import capo_qconnect.types.notes_data_details

        return {
            "notesData": capo_qconnect.types.notes_data_details.deserialize_json(
                data["notesData"]
            )
        }
    elif "notesChunkData" in data:
        import capo_qconnect.types.notes_chunk_data_details

        return {
            "notesChunkData": capo_qconnect.types.notes_chunk_data_details.deserialize_json(
                data["notesChunkData"]
            )
        }
    else:
        raise DeserializationError("DataDetails: no recognized variant key")
