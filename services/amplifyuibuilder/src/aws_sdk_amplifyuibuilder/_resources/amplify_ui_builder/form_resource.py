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
    import aws_sdk_amplifyuibuilder.types.create_form_data
    import aws_sdk_amplifyuibuilder.types.create_form_request
    import aws_sdk_amplifyuibuilder.types.create_form_response
    import aws_sdk_amplifyuibuilder.types.delete_form_request
    import aws_sdk_amplifyuibuilder.types.export_forms_request
    import aws_sdk_amplifyuibuilder.types.export_forms_response
    import aws_sdk_amplifyuibuilder.types.form
    import aws_sdk_amplifyuibuilder.types.form_summary
    import aws_sdk_amplifyuibuilder.types.get_form_request
    import aws_sdk_amplifyuibuilder.types.get_form_response
    import aws_sdk_amplifyuibuilder.types.list_entity_limit
    import aws_sdk_amplifyuibuilder.types.list_forms_request
    import aws_sdk_amplifyuibuilder.types.list_forms_response
    import aws_sdk_amplifyuibuilder.types.update_form_data
    import aws_sdk_amplifyuibuilder.types.update_form_request
    import aws_sdk_amplifyuibuilder.types.update_form_response
    import aws_sdk_amplifyuibuilder.types.uuid
    from aws_sdk_amplifyuibuilder._services.amplify_ui_builder import (
        AmplifyUIBuilderClient,
        AmplifyUIBuilderClientConfig,
    )
    from aws_sdk_amplifyuibuilder._services.async_amplify_ui_builder import (
        AsyncAmplifyUIBuilderClient,
        AsyncAmplifyUIBuilderClientConfig,
    )


class FormResource:
    def __init__(self, service: AmplifyUIBuilderClient) -> None:
        self._service = service

    def create(
        self,
        app_id: str,
        environment_name: str,
        form_to_create: "aws_sdk_amplifyuibuilder.types.create_form_data.CreateFormData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.create_form_response.CreateFormResponse":
        """<p>Creates a new form for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to associate with the form.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            form_to_create: <p>Represents the configuration of the form to create.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.create_form_request.CreateFormRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.create_form_response.CreateFormResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_form

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_form.create_form(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.create_form_request.CreateFormRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if client_token is not None:
            input_["client_token"] = client_token
        input_["form_to_create"] = form_to_create

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
    ) -> "aws_sdk_amplifyuibuilder.types.get_form_response.GetFormResponse":
        """<p>Returns an existing form for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID of the form.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.get_form_request.GetFormRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.get_form_response.GetFormResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_form

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_form.get_form(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.get_form_request.GetFormRequest = {}  # type: ignore[typeddict-item]
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
        updated_form: "aws_sdk_amplifyuibuilder.types.update_form_data.UpdateFormData",
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.update_form_response.UpdateFormResponse":
        """<p>Updates an existing form.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the form.</p>
            client_token: <p>The unique client token.</p>
            updated_form: <p>The request accepts the following data in JSON format.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.update_form_request.UpdateFormRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.update_form_response.UpdateFormResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_form

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_form.update_form(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.update_form_request.UpdateFormRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        input_["id"] = id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["updated_form"] = updated_form

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
        """<p>Deletes a form from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the form to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the form to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.delete_form_request.DeleteFormRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_form

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_form.delete_form(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.delete_form_request.DeleteFormRequest = {}  # type: ignore[typeddict-item]
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
    ) -> "aws_sdk_amplifyuibuilder.types.list_forms_response.ListFormsResponse":
        """<p>Retrieves a list of forms for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of forms to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.list_forms_request.ListFormsRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.list_forms_response.ListFormsResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_forms

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_forms.list_forms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.list_forms_request.ListFormsRequest = {}  # type: ignore[typeddict-item]
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

    def export_forms(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.export_forms_response.ExportFormsResponse":
        """<p>Exports form configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export forms to.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_amplifyuibuilder.types.export_forms_request.ExportFormsRequest]",
        ) -> OperationResponse[
            "aws_sdk_amplifyuibuilder.types.export_forms_response.ExportFormsResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_forms

            output, http_response = (
                aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_forms.export_forms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.export_forms_request.ExportFormsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncFormResource:
    def __init__(self, service: AsyncAmplifyUIBuilderClient) -> None:
        self._service = service

    async def create(
        self,
        app_id: str,
        environment_name: str,
        form_to_create: "aws_sdk_amplifyuibuilder.types.create_form_data.CreateFormData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.create_form_response.CreateFormResponse":
        """<p>Creates a new form for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to associate with the form.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            form_to_create: <p>Represents the configuration of the form to create.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.create_form_request.CreateFormRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.create_form_response.CreateFormResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_form

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.create_form.async_create_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.create_form_request.CreateFormRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        if client_token is not None:
            input_["client_token"] = client_token
        input_["form_to_create"] = form_to_create

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
    ) -> "aws_sdk_amplifyuibuilder.types.get_form_response.GetFormResponse":
        """<p>Returns an existing form for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID of the form.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.get_form_request.GetFormRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.get_form_response.GetFormResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_form

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.get_form.async_get_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.get_form_request.GetFormRequest = {}  # type: ignore[typeddict-item]
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
        updated_form: "aws_sdk_amplifyuibuilder.types.update_form_data.UpdateFormData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.update_form_response.UpdateFormResponse":
        """<p>Updates an existing form.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the form.</p>
            client_token: <p>The unique client token.</p>
            updated_form: <p>The request accepts the following data in JSON format.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.update_form_request.UpdateFormRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.update_form_response.UpdateFormResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_form

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.update_form.async_update_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.update_form_request.UpdateFormRequest = {}  # type: ignore[typeddict-item]
        input_["app_id"] = app_id
        input_["environment_name"] = environment_name
        input_["id"] = id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["updated_form"] = updated_form

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
        """<p>Deletes a form from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the form to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the form to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.delete_form_request.DeleteFormRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_form

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.delete_form.async_delete_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.delete_form_request.DeleteFormRequest = {}  # type: ignore[typeddict-item]
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
    ) -> "aws_sdk_amplifyuibuilder.types.list_forms_response.ListFormsResponse":
        """<p>Retrieves a list of forms for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of forms to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.list_forms_request.ListFormsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.list_forms_response.ListFormsResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_forms

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.list_forms.async_list_forms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.list_forms_request.ListFormsRequest = {}  # type: ignore[typeddict-item]
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

    async def export_forms(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_amplifyuibuilder.types.export_forms_response.ExportFormsResponse":
        """<p>Exports form configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export forms to.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_amplifyuibuilder.types.export_forms_request.ExportFormsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_amplifyuibuilder.types.export_forms_response.ExportFormsResponse"
        ]:
            import aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_forms

            (
                output,
                http_response,
            ) = await aws_sdk_amplifyuibuilder._operations.amplify_ui_builder.export_forms.async_export_forms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_amplifyuibuilder.types.export_forms_request.ExportFormsRequest = {}  # type: ignore[typeddict-item]
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
