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
    import aws_sdk_amplifyuibuilder.types.component
    import aws_sdk_amplifyuibuilder.types.component_summary
    import aws_sdk_amplifyuibuilder.types.create_component_data
    import aws_sdk_amplifyuibuilder.types.create_component_request
    import aws_sdk_amplifyuibuilder.types.create_component_response
    import aws_sdk_amplifyuibuilder.types.delete_component_request
    import aws_sdk_amplifyuibuilder.types.export_components_request
    import aws_sdk_amplifyuibuilder.types.export_components_response
    import aws_sdk_amplifyuibuilder.types.get_component_request
    import aws_sdk_amplifyuibuilder.types.get_component_response
    import aws_sdk_amplifyuibuilder.types.list_components_request
    import aws_sdk_amplifyuibuilder.types.list_components_response
    import aws_sdk_amplifyuibuilder.types.list_entity_limit
    import aws_sdk_amplifyuibuilder.types.update_component_data
    import aws_sdk_amplifyuibuilder.types.update_component_request
    import aws_sdk_amplifyuibuilder.types.update_component_response
    import aws_sdk_amplifyuibuilder.types.uuid
    from aws_sdk_amplifyuibuilder._services.amplify_ui_builder import (
        AmplifyUIBuilderClient,
        AmplifyUIBuilderClientConfig,
    )
    from aws_sdk_amplifyuibuilder._services.async_amplify_ui_builder import (
        AsyncAmplifyUIBuilderClient,
        AsyncAmplifyUIBuilderClientConfig,
    )


class ComponentResource:
    def __init__(self, service: AmplifyUIBuilderClient) -> None:
        self._service = service

    def create(
        self,
        app_id: str,
        environment_name: str,
        component_to_create: "aws_sdk_amplifyuibuilder.types.create_component_data.CreateComponentData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.create_component_response.CreateComponentResponse":
        """<p>Creates a new component for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to associate with the component.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            component_to_create: <p>Represents the configuration of the component to create.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.create_component_request.CreateComponentRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.create_component_response.CreateComponentResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_component

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_component.create_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.create_component_request.CreateComponentRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        if client_token is not None:
            input["client_token"] = client_token
        input["component_to_create"] = component_to_create

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
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
    ) -> "aws_sdk_amplifyuibuilder.types.get_component_response.GetComponentResponse":
        """<p>Returns an existing component for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID of the component.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.get_component_request.GetComponentRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.get_component_response.GetComponentResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_component

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_component.get_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.get_component_request.GetComponentRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        input["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        app_id: str,
        environment_name: str,
        id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid",
        updated_component: "aws_sdk_amplifyuibuilder.types.update_component_data.UpdateComponentData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.update_component_response.UpdateComponentResponse":
        """<p>Updates an existing component.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the component.</p>
            client_token: <p>The unique client token.</p>
            updated_component: <p>The configuration of the updated component.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.update_component_request.UpdateComponentRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.update_component_response.UpdateComponentResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_component

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_component.update_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.update_component_request.UpdateComponentRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        input["id"] = id
        if client_token is not None:
            input["client_token"] = client_token
        input["updated_component"] = updated_component

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
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
        """<p>Deletes a component from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the component to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the component to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.delete_component_request.DeleteComponentRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_component

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_component.delete_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.delete_component_request.DeleteComponentRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        input["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
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
    ) -> (
        "aws_sdk_amplifyuibuilder.types.list_components_response.ListComponentsResponse"
    ):
        """<p>Retrieves a list of components for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of components to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.list_components_request.ListComponentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.list_components_response.ListComponentsResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_components

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_components.list_components(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.list_components_request.ListComponentsRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def export_components(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.export_components_response.ExportComponentsResponse":
        """<p>Exports component configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export components to.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.export_components_request.ExportComponentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.export_components_response.ExportComponentsResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_components

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_components.export_components(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.export_components_request.ExportComponentsRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncComponentResource:
    def __init__(self, service: AsyncAmplifyUIBuilderClient) -> None:
        self._service = service

    async def create(
        self,
        app_id: str,
        environment_name: str,
        component_to_create: "aws_sdk_amplifyuibuilder.types.create_component_data.CreateComponentData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.create_component_response.CreateComponentResponse":
        """<p>Creates a new component for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to associate with the component.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            component_to_create: <p>Represents the configuration of the component to create.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.create_component_request.CreateComponentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.create_component_response.CreateComponentResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_component

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_component.async_create_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.create_component_request.CreateComponentRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        if client_token is not None:
            input["client_token"] = client_token
        input["component_to_create"] = component_to_create

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
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
    ) -> "aws_sdk_amplifyuibuilder.types.get_component_response.GetComponentResponse":
        """<p>Returns an existing component for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID of the component.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.get_component_request.GetComponentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.get_component_response.GetComponentResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_component

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_component.async_get_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.get_component_request.GetComponentRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        app_id: str,
        environment_name: str,
        id: "aws_sdk_amplifyuibuilder.types.uuid.Uuid",
        updated_component: "aws_sdk_amplifyuibuilder.types.update_component_data.UpdateComponentData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.update_component_response.UpdateComponentResponse":
        """<p>Updates an existing component.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the component.</p>
            client_token: <p>The unique client token.</p>
            updated_component: <p>The configuration of the updated component.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.update_component_request.UpdateComponentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.update_component_response.UpdateComponentResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_component

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_component.async_update_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.update_component_request.UpdateComponentRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        input["id"] = id
        if client_token is not None:
            input["client_token"] = client_token
        input["updated_component"] = updated_component

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
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
        """<p>Deletes a component from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the component to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the component to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.delete_component_request.DeleteComponentRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_component

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_component.async_delete_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.delete_component_request.DeleteComponentRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
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
    ) -> (
        "aws_sdk_amplifyuibuilder.types.list_components_response.ListComponentsResponse"
    ):
        """<p>Retrieves a list of components for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of components to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.list_components_request.ListComponentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.list_components_response.ListComponentsResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_components

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_components.async_list_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.list_components_request.ListComponentsRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def export_components(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.export_components_response.ExportComponentsResponse":
        """<p>Exports component configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export components to.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.export_components_request.ExportComponentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.export_components_response.ExportComponentsResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_components

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_components.async_export_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_amplifyuibuilder.types.export_components_request.ExportComponentsRequest = {}  # type: ignore[typeddict-item]
        input["app_id"] = app_id
        input["environment_name"] = environment_name
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
