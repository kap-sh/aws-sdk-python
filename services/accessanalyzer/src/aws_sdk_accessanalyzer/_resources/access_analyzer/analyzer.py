from typing import TYPE_CHECKING, Optional

import aws_sdk_accessanalyzer._auth._signers
import aws_sdk_accessanalyzer._auth._sigv4
from aws_sdk_accessanalyzer._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_configuration
    import aws_sdk_accessanalyzer.types.analyzer_name
    import aws_sdk_accessanalyzer.types.create_analyzer_request
    import aws_sdk_accessanalyzer.types.create_analyzer_response
    import aws_sdk_accessanalyzer.types.delete_analyzer_request
    import aws_sdk_accessanalyzer.types.delete_service_linked_analyzer_request
    import aws_sdk_accessanalyzer.types.get_analyzer_request
    import aws_sdk_accessanalyzer.types.get_analyzer_response
    import aws_sdk_accessanalyzer.types.inline_archive_rules_list
    import aws_sdk_accessanalyzer.types.list_analyzers_request
    import aws_sdk_accessanalyzer.types.list_analyzers_response
    import aws_sdk_accessanalyzer.types.tags_map
    import aws_sdk_accessanalyzer.types.token
    import aws_sdk_accessanalyzer.types.type
    import aws_sdk_accessanalyzer.types.update_analyzer_request
    import aws_sdk_accessanalyzer.types.update_analyzer_response
    from aws_sdk_accessanalyzer._services.access_analyzer import (
        AccessAnalyzerClient,
        AccessAnalyzerClientConfig,
    )
    from aws_sdk_accessanalyzer._services.async_access_analyzer import (
        AsyncAccessAnalyzerClient,
        AsyncAccessAnalyzerClientConfig,
    )


class Analyzer:
    def __init__(self, service: AccessAnalyzerClient) -> None:
        self._service = service

    def put(
        self,
        analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName",
        type: "aws_sdk_accessanalyzer.types.type.Type",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        archive_rules: Optional[
            "aws_sdk_accessanalyzer.types.inline_archive_rules_list.InlineArchiveRulesList"
        ] = None,
        tags: Optional["aws_sdk_accessanalyzer.types.tags_map.TagsMap"] = None,
        client_token: Optional[str] = None,
        configuration: Optional[
            "aws_sdk_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
        ] = None,
    ) -> "aws_sdk_accessanalyzer.types.create_analyzer_response.CreateAnalyzerResponse":
        """<p>Creates an analyzer for your account.</p>

        Args:
            analyzer_name: <p>The name of the analyzer to create.</p>
            type: <p>The type of analyzer to create. You can create only one analyzer per account per Region. You can create up to 5 analyzers per organization per Region.</p>
            archive_rules: <p>Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.</p>
            tags: <p>An array of key-value pairs to apply to the analyzer. You can use the set of Unicode letters, digits, whitespace, <code>_</code>, <code>.</code>, <code>/</code>, <code>=</code>, <code>+</code>, and <code>-</code>.</p> <p>For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with <code>aws:</code>.</p> <p>For the tag value, you can specify a value that is 0 to 256 characters in length.</p>
            client_token: <p>A client token.</p>
            configuration: <p>Specifies the configuration of the analyzer. If the analyzer is an unused access analyzer, the specified scope of unused access is used for the configuration. If the analyzer is an internal access analyzer, the specified internal access analysis rules are used for the configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_accessanalyzer.types.create_analyzer_request.CreateAnalyzerRequest]",
        ) -> OperationResponse[
            "aws_sdk_accessanalyzer.types.create_analyzer_response.CreateAnalyzerResponse"
        ]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.create_analyzer

            output, http_response = (
                aws_sdk_accessanalyzer._operations.access_analyzer.create_analyzer.create_analyzer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.create_analyzer_request.CreateAnalyzerRequest = {}  # type: ignore[typeddict-item]
        input_["analyzer_name"] = analyzer_name
        input_["type"] = type
        if archive_rules is not None:
            input_["archive_rules"] = archive_rules
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
    ) -> "aws_sdk_accessanalyzer.types.get_analyzer_response.GetAnalyzerResponse":
        """<p>Retrieves information about the specified analyzer.</p>

        Args:
            analyzer_name: <p>The name of the analyzer retrieved.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_accessanalyzer.types.get_analyzer_request.GetAnalyzerRequest]",
        ) -> OperationResponse[
            "aws_sdk_accessanalyzer.types.get_analyzer_response.GetAnalyzerResponse"
        ]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.get_analyzer

            output, http_response = (
                aws_sdk_accessanalyzer._operations.access_analyzer.get_analyzer.get_analyzer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.get_analyzer_request.GetAnalyzerRequest = {}  # type: ignore[typeddict-item]
        input_["analyzer_name"] = analyzer_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        configuration: Optional[
            "aws_sdk_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
        ] = None,
    ) -> "aws_sdk_accessanalyzer.types.update_analyzer_response.UpdateAnalyzerResponse":
        """<p>Modifies the configuration of an existing analyzer.</p> <note> <p>This action is not supported for external access analyzers.</p> </note>

        Args:
            analyzer_name: <p>The name of the analyzer to modify.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_accessanalyzer.types.update_analyzer_request.UpdateAnalyzerRequest]",
        ) -> OperationResponse[
            "aws_sdk_accessanalyzer.types.update_analyzer_response.UpdateAnalyzerResponse"
        ]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.update_analyzer

            output, http_response = (
                aws_sdk_accessanalyzer._operations.access_analyzer.update_analyzer.update_analyzer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.update_analyzer_request.UpdateAnalyzerRequest = {}  # type: ignore[typeddict-item]
        input_["analyzer_name"] = analyzer_name
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> None:
        """<p>Deletes the specified analyzer. When you delete an analyzer, IAM Access Analyzer is disabled for the account or organization in the current or specific Region. All findings that were generated by the analyzer are deleted. You cannot undo this action.</p>

        Args:
            analyzer_name: <p>The name of the analyzer to delete.</p>
            client_token: <p>A client token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_accessanalyzer.types.delete_analyzer_request.DeleteAnalyzerRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.delete_analyzer

            output, http_response = (
                aws_sdk_accessanalyzer._operations.access_analyzer.delete_analyzer.delete_analyzer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.delete_analyzer_request.DeleteAnalyzerRequest = {}  # type: ignore[typeddict-item]
        input_["analyzer_name"] = analyzer_name
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        next_token: Optional["aws_sdk_accessanalyzer.types.token.Token"] = None,
        max_results: Optional[int] = None,
        type: Optional["aws_sdk_accessanalyzer.types.type.Type"] = None,
    ) -> "aws_sdk_accessanalyzer.types.list_analyzers_response.ListAnalyzersResponse":
        """<p>Retrieves a list of analyzers.</p>

        Args:
            next_token: <p>A token used for pagination of results returned.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            type: <p>The type of analyzer.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_accessanalyzer.types.list_analyzers_request.ListAnalyzersRequest]",
        ) -> OperationResponse[
            "aws_sdk_accessanalyzer.types.list_analyzers_response.ListAnalyzersResponse"
        ]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.list_analyzers

            output, http_response = (
                aws_sdk_accessanalyzer._operations.access_analyzer.list_analyzers.list_analyzers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.list_analyzers_request.ListAnalyzersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_service_linked_analyzer(
        self,
        analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AccessAnalyzerClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> None:
        """<p>Deletes a service-linked analyzer. This operation can be invoked by both authorized Amazon Web Services services and customers.</p> <p>When invoked by a customer, IAM Access Analyzer performs a callback to the managing service to verify whether the analyzer is still in use and can be deleted. If the service indicates the analyzer is still in use, the deletion is rejected with <code>ConflictException</code>.</p>

        Args:
            analyzer_name: <p>The name of the service-linked analyzer to delete. Service-linked analyzer names follow the format <code>_AccessAnalyzerFor{ServiceName}-{Id}</code>.</p>
            client_token: <p>A client token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_accessanalyzer.types.delete_service_linked_analyzer_request.DeleteServiceLinkedAnalyzerRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.delete_service_linked_analyzer

            output, http_response = (
                aws_sdk_accessanalyzer._operations.access_analyzer.delete_service_linked_analyzer.delete_service_linked_analyzer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.delete_service_linked_analyzer_request.DeleteServiceLinkedAnalyzerRequest = {}  # type: ignore[typeddict-item]
        input_["analyzer_name"] = analyzer_name
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAnalyzer:
    def __init__(self, service: AsyncAccessAnalyzerClient) -> None:
        self._service = service

    async def put(
        self,
        analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName",
        type: "aws_sdk_accessanalyzer.types.type.Type",
        *,
        config_overrides: Optional[AsyncAccessAnalyzerClientConfig] = None,
        archive_rules: Optional[
            "aws_sdk_accessanalyzer.types.inline_archive_rules_list.InlineArchiveRulesList"
        ] = None,
        tags: Optional["aws_sdk_accessanalyzer.types.tags_map.TagsMap"] = None,
        client_token: Optional[str] = None,
        configuration: Optional[
            "aws_sdk_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
        ] = None,
    ) -> "aws_sdk_accessanalyzer.types.create_analyzer_response.CreateAnalyzerResponse":
        """<p>Creates an analyzer for your account.</p>

        Args:
            analyzer_name: <p>The name of the analyzer to create.</p>
            type: <p>The type of analyzer to create. You can create only one analyzer per account per Region. You can create up to 5 analyzers per organization per Region.</p>
            archive_rules: <p>Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.</p>
            tags: <p>An array of key-value pairs to apply to the analyzer. You can use the set of Unicode letters, digits, whitespace, <code>_</code>, <code>.</code>, <code>/</code>, <code>=</code>, <code>+</code>, and <code>-</code>.</p> <p>For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with <code>aws:</code>.</p> <p>For the tag value, you can specify a value that is 0 to 256 characters in length.</p>
            client_token: <p>A client token.</p>
            configuration: <p>Specifies the configuration of the analyzer. If the analyzer is an unused access analyzer, the specified scope of unused access is used for the configuration. If the analyzer is an internal access analyzer, the specified internal access analysis rules are used for the configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_accessanalyzer.types.create_analyzer_request.CreateAnalyzerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_accessanalyzer.types.create_analyzer_response.CreateAnalyzerResponse"
        ]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.create_analyzer

            (
                output,
                http_response,
            ) = await aws_sdk_accessanalyzer._operations.access_analyzer.create_analyzer.async_create_analyzer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.create_analyzer_request.CreateAnalyzerRequest = {}  # type: ignore[typeddict-item]
        input_["analyzer_name"] = analyzer_name
        input_["type"] = type
        if archive_rules is not None:
            input_["archive_rules"] = archive_rules
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token
        if configuration is not None:
            input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AsyncAccessAnalyzerClientConfig] = None,
    ) -> "aws_sdk_accessanalyzer.types.get_analyzer_response.GetAnalyzerResponse":
        """<p>Retrieves information about the specified analyzer.</p>

        Args:
            analyzer_name: <p>The name of the analyzer retrieved.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_accessanalyzer.types.get_analyzer_request.GetAnalyzerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_accessanalyzer.types.get_analyzer_response.GetAnalyzerResponse"
        ]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.get_analyzer

            (
                output,
                http_response,
            ) = await aws_sdk_accessanalyzer._operations.access_analyzer.get_analyzer.async_get_analyzer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.get_analyzer_request.GetAnalyzerRequest = {}  # type: ignore[typeddict-item]
        input_["analyzer_name"] = analyzer_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AsyncAccessAnalyzerClientConfig] = None,
        configuration: Optional[
            "aws_sdk_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
        ] = None,
    ) -> "aws_sdk_accessanalyzer.types.update_analyzer_response.UpdateAnalyzerResponse":
        """<p>Modifies the configuration of an existing analyzer.</p> <note> <p>This action is not supported for external access analyzers.</p> </note>

        Args:
            analyzer_name: <p>The name of the analyzer to modify.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_accessanalyzer.types.update_analyzer_request.UpdateAnalyzerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_accessanalyzer.types.update_analyzer_response.UpdateAnalyzerResponse"
        ]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.update_analyzer

            (
                output,
                http_response,
            ) = await aws_sdk_accessanalyzer._operations.access_analyzer.update_analyzer.async_update_analyzer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.update_analyzer_request.UpdateAnalyzerRequest = {}  # type: ignore[typeddict-item]
        input_["analyzer_name"] = analyzer_name
        if configuration is not None:
            input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AsyncAccessAnalyzerClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> None:
        """<p>Deletes the specified analyzer. When you delete an analyzer, IAM Access Analyzer is disabled for the account or organization in the current or specific Region. All findings that were generated by the analyzer are deleted. You cannot undo this action.</p>

        Args:
            analyzer_name: <p>The name of the analyzer to delete.</p>
            client_token: <p>A client token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_accessanalyzer.types.delete_analyzer_request.DeleteAnalyzerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.delete_analyzer

            (
                output,
                http_response,
            ) = await aws_sdk_accessanalyzer._operations.access_analyzer.delete_analyzer.async_delete_analyzer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.delete_analyzer_request.DeleteAnalyzerRequest = {}  # type: ignore[typeddict-item]
        input_["analyzer_name"] = analyzer_name
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncAccessAnalyzerClientConfig] = None,
        next_token: Optional["aws_sdk_accessanalyzer.types.token.Token"] = None,
        max_results: Optional[int] = None,
        type: Optional["aws_sdk_accessanalyzer.types.type.Type"] = None,
    ) -> "aws_sdk_accessanalyzer.types.list_analyzers_response.ListAnalyzersResponse":
        """<p>Retrieves a list of analyzers.</p>

        Args:
            next_token: <p>A token used for pagination of results returned.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            type: <p>The type of analyzer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_accessanalyzer.types.list_analyzers_request.ListAnalyzersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_accessanalyzer.types.list_analyzers_response.ListAnalyzersResponse"
        ]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.list_analyzers

            (
                output,
                http_response,
            ) = await aws_sdk_accessanalyzer._operations.access_analyzer.list_analyzers.async_list_analyzers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.list_analyzers_request.ListAnalyzersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_service_linked_analyzer(
        self,
        analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName",
        *,
        config_overrides: Optional[AsyncAccessAnalyzerClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> None:
        """<p>Deletes a service-linked analyzer. This operation can be invoked by both authorized Amazon Web Services services and customers.</p> <p>When invoked by a customer, IAM Access Analyzer performs a callback to the managing service to verify whether the analyzer is still in use and can be deleted. If the service indicates the analyzer is still in use, the deletion is rejected with <code>ConflictException</code>.</p>

        Args:
            analyzer_name: <p>The name of the service-linked analyzer to delete. Service-linked analyzer names follow the format <code>_AccessAnalyzerFor{ServiceName}-{Id}</code>.</p>
            client_token: <p>A client token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_accessanalyzer.types.delete_service_linked_analyzer_request.DeleteServiceLinkedAnalyzerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_accessanalyzer._operations.access_analyzer.delete_service_linked_analyzer

            (
                output,
                http_response,
            ) = await aws_sdk_accessanalyzer._operations.access_analyzer.delete_service_linked_analyzer.async_delete_service_linked_analyzer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_accessanalyzer.types.delete_service_linked_analyzer_request.DeleteServiceLinkedAnalyzerRequest = {}  # type: ignore[typeddict-item]
        input_["analyzer_name"] = analyzer_name
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
