from typing import TYPE_CHECKING, Optional

import aws_sdk_amplifyuibuilder._auth._signers
import aws_sdk_amplifyuibuilder._auth._sigv4
from aws_sdk_amplifyuibuilder._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.create_theme_data
    import aws_sdk_amplifyuibuilder.types.create_theme_request
    import aws_sdk_amplifyuibuilder.types.create_theme_response
    import aws_sdk_amplifyuibuilder.types.delete_theme_request
    import aws_sdk_amplifyuibuilder.types.export_themes_request
    import aws_sdk_amplifyuibuilder.types.export_themes_response
    import aws_sdk_amplifyuibuilder.types.get_theme_request
    import aws_sdk_amplifyuibuilder.types.get_theme_response
    import aws_sdk_amplifyuibuilder.types.list_entity_limit
    import aws_sdk_amplifyuibuilder.types.list_themes_request
    import aws_sdk_amplifyuibuilder.types.list_themes_response
    import aws_sdk_amplifyuibuilder.types.theme
    import aws_sdk_amplifyuibuilder.types.theme_summary
    import aws_sdk_amplifyuibuilder.types.update_theme_data
    import aws_sdk_amplifyuibuilder.types.update_theme_request
    import aws_sdk_amplifyuibuilder.types.update_theme_response
    import aws_sdk_amplifyuibuilder.types.uuid
    from aws_sdk_amplifyuibuilder._services.amplify_ui_builder import (
        AmplifyUIBuilderClient,
        AmplifyUIBuilderClientConfig,
    )
    from aws_sdk_amplifyuibuilder._services.async_amplify_ui_builder import (
        AsyncAmplifyUIBuilderClient,
        AsyncAmplifyUIBuilderClientConfig,
    )


class ThemeResource:
    def __init__(self, service: AmplifyUIBuilderClient) -> None:
        self._service = service

    def create(
        self,
        app_id: str,
        environment_name: str,
        theme_to_create: "aws_sdk_amplifyuibuilder.types.create_theme_data.CreateThemeData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.create_theme_response.CreateThemeResponse":
        """<p>Creates a theme to apply to the components in an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the theme.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            theme_to_create: <p>Represents the configuration of the theme to create.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.create_theme_request.CreateThemeRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.create_theme_response.CreateThemeResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_theme

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_theme.create_theme(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.create_theme_request.CreateThemeRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if client_token is not None:
            input_["client_token"] = client_token
        input_["theme_to_create"] = theme_to_create

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        app_id: str,
        environment_name: str,
        id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.get_theme_response.GetThemeResponse":
        """<p>Returns an existing theme for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the theme.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.get_theme_request.GetThemeRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.get_theme_response.GetThemeResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_theme

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_theme.get_theme(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.get_theme_request.GetThemeRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        app_id: str,
        environment_name: str,
        id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid",
        updated_theme: "aws_sdk_amplifyuibuilder.types.update_theme_data.UpdateThemeData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.update_theme_response.UpdateThemeResponse":
        """<p>Updates an existing theme.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the theme.</p>
            client_token: <p>The unique client token.</p>
            updated_theme: <p>The configuration of the updated theme.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.update_theme_request.UpdateThemeRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.update_theme_response.UpdateThemeResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_theme

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_theme.update_theme(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.update_theme_request.UpdateThemeRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        input_["id"] = id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["updated_theme"] = updated_theme

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        app_id: str,
        environment_name: str,
        id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
    ) -> None:
        """<p>Deletes a theme from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the theme to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the theme to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.delete_theme_request.DeleteThemeRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_theme

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_theme.delete_theme(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.delete_theme_request.DeleteThemeRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_amplifyuibuilder.types.list_entity_limit.ListEntityLimit"
        ] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.list_themes_response.ListThemesResponse":
        """<p>Retrieves a list of themes for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of theme results to return in the response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.list_themes_request.ListThemesRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.list_themes_response.ListThemesResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_themes

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_themes.list_themes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.list_themes_request.ListThemesRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def export_themes(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.export_themes_response.ExportThemesResponse":
        """<p>Exports theme configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export the themes to.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.export_themes_request.ExportThemesRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.export_themes_response.ExportThemesResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_themes

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_themes.export_themes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.export_themes_request.ExportThemesRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncThemeResource:
    def __init__(self, service: AsyncAmplifyUIBuilderClient) -> None:
        self._service = service

    async def create(
        self,
        app_id: str,
        environment_name: str,
        theme_to_create: "aws_sdk_amplifyuibuilder.types.create_theme_data.CreateThemeData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.create_theme_response.CreateThemeResponse":
        """<p>Creates a theme to apply to the components in an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the theme.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            theme_to_create: <p>Represents the configuration of the theme to create.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.create_theme_request.CreateThemeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.create_theme_response.CreateThemeResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_theme

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_theme.async_create_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.create_theme_request.CreateThemeRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if client_token is not None:
            input_["client_token"] = client_token
        input_["theme_to_create"] = theme_to_create

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        app_id: str,
        environment_name: str,
        id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.get_theme_response.GetThemeResponse":
        """<p>Returns an existing theme for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the theme.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.get_theme_request.GetThemeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.get_theme_response.GetThemeResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_theme

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_theme.async_get_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.get_theme_request.GetThemeRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        app_id: str,
        environment_name: str,
        id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid",
        updated_theme: "aws_sdk_amplifyuibuilder.types.update_theme_data.UpdateThemeData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.update_theme_response.UpdateThemeResponse":
        """<p>Updates an existing theme.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the theme.</p>
            client_token: <p>The unique client token.</p>
            updated_theme: <p>The configuration of the updated theme.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.update_theme_request.UpdateThemeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.update_theme_response.UpdateThemeResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_theme

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_theme.async_update_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.update_theme_request.UpdateThemeRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        input_["id"] = id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["updated_theme"] = updated_theme

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        app_id: str,
        environment_name: str,
        id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> None:
        """<p>Deletes a theme from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the theme to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the theme to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.delete_theme_request.DeleteThemeRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_theme

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_theme.async_delete_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.delete_theme_request.DeleteThemeRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_amplifyuibuilder.types.list_entity_limit.ListEntityLimit"
        ] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.list_themes_response.ListThemesResponse":
        """<p>Retrieves a list of themes for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of theme results to return in the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.list_themes_request.ListThemesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.list_themes_response.ListThemesResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_themes

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_themes.async_list_themes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.list_themes_request.ListThemesRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def export_themes(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.export_themes_response.ExportThemesResponse":
        """<p>Exports theme configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export the themes to.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.export_themes_request.ExportThemesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.export_themes_response.ExportThemesResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_themes

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_themes.async_export_themes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.export_themes_request.ExportThemesRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
