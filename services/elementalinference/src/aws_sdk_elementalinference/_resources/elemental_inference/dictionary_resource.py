from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_elementalinference._auth._signers
import aws_sdk_elementalinference._auth._sigv4
from aws_sdk_elementalinference._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.create_dictionary_request
    import aws_sdk_elementalinference.types.create_dictionary_response
    import aws_sdk_elementalinference.types.delete_dictionary_request
    import aws_sdk_elementalinference.types.delete_dictionary_response
    import aws_sdk_elementalinference.types.dictionary_entries_payload
    import aws_sdk_elementalinference.types.dictionary_id
    import aws_sdk_elementalinference.types.dictionary_language
    import aws_sdk_elementalinference.types.dictionary_summary
    import aws_sdk_elementalinference.types.export_dictionary_entries_request
    import aws_sdk_elementalinference.types.export_dictionary_entries_response
    import aws_sdk_elementalinference.types.get_dictionary_request
    import aws_sdk_elementalinference.types.get_dictionary_response
    import aws_sdk_elementalinference.types.list_dictionaries_request
    import aws_sdk_elementalinference.types.list_dictionaries_response
    import aws_sdk_elementalinference.types.resource_name
    import aws_sdk_elementalinference.types.tag_map
    import aws_sdk_elementalinference.types.update_dictionary_request
    import aws_sdk_elementalinference.types.update_dictionary_response
    from aws_sdk_elementalinference._services.async_elemental_inference import (
        AsyncElementalInferenceClient,
        AsyncElementalInferenceClientConfig,
    )
    from aws_sdk_elementalinference._services.elemental_inference import (
        ElementalInferenceClient,
        ElementalInferenceClientConfig,
    )


class DictionaryResource:
    def __init__(self, service: ElementalInferenceClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_elementalinference.types.resource_name.ResourceName",
        language: "aws_sdk_elementalinference.types.dictionary_language.DictionaryLanguage",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        entries: Optional[
            "aws_sdk_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
        ] = None,
        tags: Optional["aws_sdk_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_elementalinference.types.create_dictionary_response.CreateDictionaryResponse":
        """<p>Creates a custom dictionary for improving transcription accuracy. A dictionary contains custom words and phrases that the ASR engine might not recognize, such as brand names, technical terms, or proper nouns. You can reference a dictionary when configuring a smart subtitles output. </p>

        Args:
            name: <p>A user-friendly name for this dictionary.</p>
            language: <p>The language of the dictionary entries. Specify the language using an ISO 639-2/T three-letter code. Supported values: eng, fra, ita, deu, spa, por. </p>
            entries: <p>The dictionary entries payload. Contains the custom words and phrases for the dictionary. Maximum size is 40,960 characters. </p>
            tags: <p>Optional tags to associate with the dictionary.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.create_dictionary_request.CreateDictionaryRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.create_dictionary_response.CreateDictionaryResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.create_dictionary

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.create_dictionary.create_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.create_dictionary_request.CreateDictionaryRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["language"] = language
        if entries is not None:
            input_["entries"] = entries
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> (
        "aws_sdk_elementalinference.types.get_dictionary_response.GetDictionaryResponse"
    ):
        """<p>Retrieves information about the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.get_dictionary_request.GetDictionaryRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.get_dictionary_response.GetDictionaryResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.get_dictionary

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.get_dictionary.get_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.get_dictionary_request.GetDictionaryRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        name: Optional[
            "aws_sdk_elementalinference.types.resource_name.ResourceName"
        ] = None,
        language: Optional[
            "aws_sdk_elementalinference.types.dictionary_language.DictionaryLanguage"
        ] = None,
        entries: Optional[
            "aws_sdk_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
        ] = None,
    ) -> "aws_sdk_elementalinference.types.update_dictionary_response.UpdateDictionaryResponse":
        """<p>Updates the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary to update.</p>
            name: <p>A new name for the dictionary. If not specified, the name is not changed.</p>
            language: <p>A new language for the dictionary. If not specified, the language is not changed.</p>
            entries: <p>New dictionary entries. If not specified, the entries are not changed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.update_dictionary_request.UpdateDictionaryRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.update_dictionary_response.UpdateDictionaryResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.update_dictionary

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.update_dictionary.update_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.update_dictionary_request.UpdateDictionaryRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if name is not None:
            input_["name"] = name
        if language is not None:
            input_["language"] = language
        if entries is not None:
            input_["entries"] = entries

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "aws_sdk_elementalinference.types.delete_dictionary_response.DeleteDictionaryResponse":
        """<p>Deletes the specified dictionary. You cannot delete a dictionary that is referenced by a feed. You must first remove the dictionary reference from the feed's subtitling configuration. </p>

        Args:
            id: <p>The ID of the dictionary to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.delete_dictionary_request.DeleteDictionaryRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.delete_dictionary_response.DeleteDictionaryResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.delete_dictionary

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.delete_dictionary.delete_dictionary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.delete_dictionary_request.DeleteDictionaryRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_elementalinference.types.list_dictionaries_response.ListDictionariesResponse":
        """<p>Lists the dictionaries in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return per API request. Valid range: 1 to 100.</p>
            next_token: <p>The token that identifies the next batch of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.list_dictionaries_request.ListDictionariesRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.list_dictionaries_response.ListDictionariesResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.list_dictionaries

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.list_dictionaries.list_dictionaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.list_dictionaries_request.ListDictionariesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def export_dictionary_entries(
        self,
        id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "aws_sdk_elementalinference.types.export_dictionary_entries_response.ExportDictionaryEntriesResponse":
        """<p>Exports the entries from the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary whose entries you want to export.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.export_dictionary_entries_request.ExportDictionaryEntriesRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.export_dictionary_entries_response.ExportDictionaryEntriesResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.export_dictionary_entries

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.export_dictionary_entries.export_dictionary_entries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.export_dictionary_entries_request.ExportDictionaryEntriesRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDictionaryResource:
    def __init__(self, service: AsyncElementalInferenceClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_elementalinference.types.resource_name.ResourceName",
        language: "aws_sdk_elementalinference.types.dictionary_language.DictionaryLanguage",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        entries: Optional[
            "aws_sdk_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
        ] = None,
        tags: Optional["aws_sdk_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_elementalinference.types.create_dictionary_response.CreateDictionaryResponse":
        """<p>Creates a custom dictionary for improving transcription accuracy. A dictionary contains custom words and phrases that the ASR engine might not recognize, such as brand names, technical terms, or proper nouns. You can reference a dictionary when configuring a smart subtitles output. </p>

        Args:
            name: <p>A user-friendly name for this dictionary.</p>
            language: <p>The language of the dictionary entries. Specify the language using an ISO 639-2/T three-letter code. Supported values: eng, fra, ita, deu, spa, por. </p>
            entries: <p>The dictionary entries payload. Contains the custom words and phrases for the dictionary. Maximum size is 40,960 characters. </p>
            tags: <p>Optional tags to associate with the dictionary.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.create_dictionary_request.CreateDictionaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.create_dictionary_response.CreateDictionaryResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.create_dictionary

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.create_dictionary.async_create_dictionary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.create_dictionary_request.CreateDictionaryRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["language"] = language
        if entries is not None:
            input_["entries"] = entries
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> (
        "aws_sdk_elementalinference.types.get_dictionary_response.GetDictionaryResponse"
    ):
        """<p>Retrieves information about the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.get_dictionary_request.GetDictionaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.get_dictionary_response.GetDictionaryResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.get_dictionary

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.get_dictionary.async_get_dictionary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.get_dictionary_request.GetDictionaryRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        name: Optional[
            "aws_sdk_elementalinference.types.resource_name.ResourceName"
        ] = None,
        language: Optional[
            "aws_sdk_elementalinference.types.dictionary_language.DictionaryLanguage"
        ] = None,
        entries: Optional[
            "aws_sdk_elementalinference.types.dictionary_entries_payload.DictionaryEntriesPayload"
        ] = None,
    ) -> "aws_sdk_elementalinference.types.update_dictionary_response.UpdateDictionaryResponse":
        """<p>Updates the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary to update.</p>
            name: <p>A new name for the dictionary. If not specified, the name is not changed.</p>
            language: <p>A new language for the dictionary. If not specified, the language is not changed.</p>
            entries: <p>New dictionary entries. If not specified, the entries are not changed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.update_dictionary_request.UpdateDictionaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.update_dictionary_response.UpdateDictionaryResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.update_dictionary

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.update_dictionary.async_update_dictionary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.update_dictionary_request.UpdateDictionaryRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if name is not None:
            input_["name"] = name
        if language is not None:
            input_["language"] = language
        if entries is not None:
            input_["entries"] = entries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "aws_sdk_elementalinference.types.delete_dictionary_response.DeleteDictionaryResponse":
        """<p>Deletes the specified dictionary. You cannot delete a dictionary that is referenced by a feed. You must first remove the dictionary reference from the feed's subtitling configuration. </p>

        Args:
            id: <p>The ID of the dictionary to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.delete_dictionary_request.DeleteDictionaryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.delete_dictionary_response.DeleteDictionaryResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.delete_dictionary

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.delete_dictionary.async_delete_dictionary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.delete_dictionary_request.DeleteDictionaryRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_elementalinference.types.list_dictionaries_response.ListDictionariesResponse":
        """<p>Lists the dictionaries in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return per API request. Valid range: 1 to 100.</p>
            next_token: <p>The token that identifies the next batch of results to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.list_dictionaries_request.ListDictionariesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.list_dictionaries_response.ListDictionariesResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.list_dictionaries

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.list_dictionaries.async_list_dictionaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.list_dictionaries_request.ListDictionariesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def export_dictionary_entries(
        self,
        id: "aws_sdk_elementalinference.types.dictionary_id.DictionaryId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "aws_sdk_elementalinference.types.export_dictionary_entries_response.ExportDictionaryEntriesResponse":
        """<p>Exports the entries from the specified dictionary.</p>

        Args:
            id: <p>The ID of the dictionary whose entries you want to export.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.export_dictionary_entries_request.ExportDictionaryEntriesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.export_dictionary_entries_response.ExportDictionaryEntriesResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.export_dictionary_entries

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.export_dictionary_entries.async_export_dictionary_entries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_elementalinference.types.export_dictionary_entries_request.ExportDictionaryEntriesRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
