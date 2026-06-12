from typing import TYPE_CHECKING, Optional

from aws_sdk_transfer._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_transfer.types.delete_web_app_customization_request
    import aws_sdk_transfer.types.describe_web_app_customization_request
    import aws_sdk_transfer.types.describe_web_app_customization_response
    import aws_sdk_transfer.types.update_web_app_customization_request
    import aws_sdk_transfer.types.update_web_app_customization_response
    import aws_sdk_transfer.types.web_app_favicon_file
    import aws_sdk_transfer.types.web_app_id
    import aws_sdk_transfer.types.web_app_logo_file
    import aws_sdk_transfer.types.web_app_title
    from aws_sdk_transfer._services.async_transfer import (
        AsyncTransferClient,
        AsyncTransferClientConfig,
    )
    from aws_sdk_transfer._services.transfer import TransferClient, TransferClientConfig


class WebAppCustomizationResource:
    def __init__(self, service: TransferClient) -> None:
        self._service = service

    def read(
        self,
        web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse":
        """<p>Describes the web app customization object that's identified by <code>WebAppId</code>.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.describe_web_app_customization_request.DescribeWebAppCustomizationRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_web_app_customization

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.describe_web_app_customization.describe_web_app_customization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.describe_web_app_customization_request.DescribeWebAppCustomizationRequest = {}  # type: ignore[typeddict-item]
        input["web_app_id"] = web_app_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        title: Optional["aws_sdk_transfer.types.web_app_title.WebAppTitle"] = None,
        logo_file: Optional[
            "aws_sdk_transfer.types.web_app_logo_file.WebAppLogoFile"
        ] = None,
        favicon_file: Optional[
            "aws_sdk_transfer.types.web_app_favicon_file.WebAppFaviconFile"
        ] = None,
    ) -> "aws_sdk_transfer.types.update_web_app_customization_response.UpdateWebAppCustomizationResponse":
        """<p>Assigns new customization properties to a web app. You can modify the icon file, logo file, and title.</p>

        Args:
            web_app_id: <p>Provide the identifier of the web app that you are updating.</p>
            title: <p>Provide an updated title.</p>
            logo_file: <p>Specify logo file data string (in base64 encoding).</p>
            favicon_file: <p>Specify an icon file data string (in base64 encoding).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.update_web_app_customization_response.UpdateWebAppCustomizationResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.update_web_app_customization

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.update_web_app_customization.update_web_app_customization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest = {}  # type: ignore[typeddict-item]
        input["web_app_id"] = web_app_id
        if title is not None:
            input["title"] = title
        if logo_file is not None:
            input["logo_file"] = logo_file
        if favicon_file is not None:
            input["favicon_file"] = favicon_file

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the <code>WebAppCustomization</code> object that corresponds to the web app ID specified.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app that contains the customizations that you are deleting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.delete_web_app_customization_request.DeleteWebAppCustomizationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.delete_web_app_customization

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.delete_web_app_customization.delete_web_app_customization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.delete_web_app_customization_request.DeleteWebAppCustomizationRequest = {}  # type: ignore[typeddict-item]
        input["web_app_id"] = web_app_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncWebAppCustomizationResource:
    def __init__(self, service: AsyncTransferClient) -> None:
        self._service = service

    async def read(
        self,
        web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse":
        """<p>Describes the web app customization object that's identified by <code>WebAppId</code>.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.describe_web_app_customization_request.DescribeWebAppCustomizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_web_app_customization

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.describe_web_app_customization.async_describe_web_app_customization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.describe_web_app_customization_request.DescribeWebAppCustomizationRequest = {}  # type: ignore[typeddict-item]
        input["web_app_id"] = web_app_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        title: Optional["aws_sdk_transfer.types.web_app_title.WebAppTitle"] = None,
        logo_file: Optional[
            "aws_sdk_transfer.types.web_app_logo_file.WebAppLogoFile"
        ] = None,
        favicon_file: Optional[
            "aws_sdk_transfer.types.web_app_favicon_file.WebAppFaviconFile"
        ] = None,
    ) -> "aws_sdk_transfer.types.update_web_app_customization_response.UpdateWebAppCustomizationResponse":
        """<p>Assigns new customization properties to a web app. You can modify the icon file, logo file, and title.</p>

        Args:
            web_app_id: <p>Provide the identifier of the web app that you are updating.</p>
            title: <p>Provide an updated title.</p>
            logo_file: <p>Specify logo file data string (in base64 encoding).</p>
            favicon_file: <p>Specify an icon file data string (in base64 encoding).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.update_web_app_customization_response.UpdateWebAppCustomizationResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.update_web_app_customization

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.update_web_app_customization.async_update_web_app_customization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest = {}  # type: ignore[typeddict-item]
        input["web_app_id"] = web_app_id
        if title is not None:
            input["title"] = title
        if logo_file is not None:
            input["logo_file"] = logo_file
        if favicon_file is not None:
            input["favicon_file"] = favicon_file

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the <code>WebAppCustomization</code> object that corresponds to the web app ID specified.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app that contains the customizations that you are deleting.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.delete_web_app_customization_request.DeleteWebAppCustomizationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.delete_web_app_customization

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.delete_web_app_customization.async_delete_web_app_customization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.delete_web_app_customization_request.DeleteWebAppCustomizationRequest = {}  # type: ignore[typeddict-item]
        input["web_app_id"] = web_app_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
