from typing import TYPE_CHECKING, Optional

from aws_sdk_sso_admin._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_arn
    import aws_sdk_sso_admin.types.authentication_method
    import aws_sdk_sso_admin.types.authentication_method_item
    import aws_sdk_sso_admin.types.authentication_method_type
    import aws_sdk_sso_admin.types.delete_application_authentication_method_request
    import aws_sdk_sso_admin.types.get_application_authentication_method_request
    import aws_sdk_sso_admin.types.get_application_authentication_method_response
    import aws_sdk_sso_admin.types.list_application_authentication_methods_request
    import aws_sdk_sso_admin.types.list_application_authentication_methods_response
    import aws_sdk_sso_admin.types.put_application_authentication_method_request
    import aws_sdk_sso_admin.types.token
    from aws_sdk_sso_admin._services.async_sso_admin import (
        AsyncSSOAdminClient,
        AsyncSSOAdminClientConfig,
    )
    from aws_sdk_sso_admin._services.sso_admin import (
        SSOAdminClient,
        SSOAdminClientConfig,
    )


class ApplicationAuthenticationMethodResource:
    def __init__(self, service: SSOAdminClient) -> None:
        self._service = service

    def put(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        authentication_method_type: "aws_sdk_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        authentication_method: "aws_sdk_sso_admin.types.authentication_method.AuthenticationMethod",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> None:
        """<p>Adds or updates an authentication method for an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication method to add or update.</p>
            authentication_method_type: <p>Specifies the type of the authentication method that you want to add or update.</p>
            authentication_method: <p>Specifies a structure that describes the authentication method to add or update. The structure type you provide is determined by the <code>AuthenticationMethodType</code> parameter.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.put_application_authentication_method_request.PutApplicationAuthenticationMethodRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_sso_admin._operations.swb_external_service.put_application_authentication_method

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.put_application_authentication_method.put_application_authentication_method(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.put_application_authentication_method_request.PutApplicationAuthenticationMethodRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        input_["authentication_method_type"] = authentication_method_type
        input_["authentication_method"] = authentication_method

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        authentication_method_type: "aws_sdk_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.get_application_authentication_method_response.GetApplicationAuthenticationMethodResponse":
        """<p>Retrieves details about an authentication method used by an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application.</p>
            authentication_method_type: <p>Specifies the type of authentication method for which you want details.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.get_application_authentication_method_request.GetApplicationAuthenticationMethodRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.get_application_authentication_method_response.GetApplicationAuthenticationMethodResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.get_application_authentication_method

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.get_application_authentication_method.get_application_authentication_method(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.get_application_authentication_method_request.GetApplicationAuthenticationMethodRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        input_["authentication_method_type"] = authentication_method_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        authentication_method_type: "aws_sdk_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes an authentication method from an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication method to delete.</p>
            authentication_method_type: <p>Specifies the authentication method type to delete from the application.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.delete_application_authentication_method_request.DeleteApplicationAuthenticationMethodRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_application_authentication_method

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.delete_application_authentication_method.delete_application_authentication_method(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.delete_application_authentication_method_request.DeleteApplicationAuthenticationMethodRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        input_["authentication_method_type"] = authentication_method_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_application_authentication_methods_response.ListApplicationAuthenticationMethodsResponse":
        """<p>Lists all of the authentication methods supported by the specified application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication methods you want to list.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sso_admin.types.list_application_authentication_methods_request.ListApplicationAuthenticationMethodsRequest]",
        ) -> OperationResponse[
            "aws_sdk_sso_admin.types.list_application_authentication_methods_response.ListApplicationAuthenticationMethodsResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_application_authentication_methods

            output, http_response = (
                aws_sdk_sso_admin._operations.swb_external_service.list_application_authentication_methods.list_application_authentication_methods(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_application_authentication_methods_request.ListApplicationAuthenticationMethodsRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncApplicationAuthenticationMethodResource:
    def __init__(self, service: AsyncSSOAdminClient) -> None:
        self._service = service

    async def put(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        authentication_method_type: "aws_sdk_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        authentication_method: "aws_sdk_sso_admin.types.authentication_method.AuthenticationMethod",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
    ) -> None:
        """<p>Adds or updates an authentication method for an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication method to add or update.</p>
            authentication_method_type: <p>Specifies the type of the authentication method that you want to add or update.</p>
            authentication_method: <p>Specifies a structure that describes the authentication method to add or update. The structure type you provide is determined by the <code>AuthenticationMethodType</code> parameter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sso_admin.types.put_application_authentication_method_request.PutApplicationAuthenticationMethodRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_sso_admin._operations.swb_external_service.put_application_authentication_method

            (
                output,
                http_response,
            ) = await aws_sdk_sso_admin._operations.swb_external_service.put_application_authentication_method.async_put_application_authentication_method(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.put_application_authentication_method_request.PutApplicationAuthenticationMethodRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        input_["authentication_method_type"] = authentication_method_type
        input_["authentication_method"] = authentication_method

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        authentication_method_type: "aws_sdk_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
    ) -> "aws_sdk_sso_admin.types.get_application_authentication_method_response.GetApplicationAuthenticationMethodResponse":
        """<p>Retrieves details about an authentication method used by an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application.</p>
            authentication_method_type: <p>Specifies the type of authentication method for which you want details.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sso_admin.types.get_application_authentication_method_request.GetApplicationAuthenticationMethodRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sso_admin.types.get_application_authentication_method_response.GetApplicationAuthenticationMethodResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.get_application_authentication_method

            (
                output,
                http_response,
            ) = await aws_sdk_sso_admin._operations.swb_external_service.get_application_authentication_method.async_get_application_authentication_method(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.get_application_authentication_method_request.GetApplicationAuthenticationMethodRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        input_["authentication_method_type"] = authentication_method_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        authentication_method_type: "aws_sdk_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes an authentication method from an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication method to delete.</p>
            authentication_method_type: <p>Specifies the authentication method type to delete from the application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sso_admin.types.delete_application_authentication_method_request.DeleteApplicationAuthenticationMethodRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_sso_admin._operations.swb_external_service.delete_application_authentication_method

            (
                output,
                http_response,
            ) = await aws_sdk_sso_admin._operations.swb_external_service.delete_application_authentication_method.async_delete_application_authentication_method(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.delete_application_authentication_method_request.DeleteApplicationAuthenticationMethodRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        input_["authentication_method_type"] = authentication_method_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        application_arn: "aws_sdk_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
        next_token: Optional["aws_sdk_sso_admin.types.token.Token"] = None,
    ) -> "aws_sdk_sso_admin.types.list_application_authentication_methods_response.ListApplicationAuthenticationMethodsResponse":
        """<p>Lists all of the authentication methods supported by the specified application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication methods you want to list.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sso_admin.types.list_application_authentication_methods_request.ListApplicationAuthenticationMethodsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sso_admin.types.list_application_authentication_methods_response.ListApplicationAuthenticationMethodsResponse"
        ]:
            import aws_sdk_sso_admin._operations.swb_external_service.list_application_authentication_methods

            (
                output,
                http_response,
            ) = await aws_sdk_sso_admin._operations.swb_external_service.list_application_authentication_methods.async_list_application_authentication_methods(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sso_admin.types.list_application_authentication_methods_request.ListApplicationAuthenticationMethodsRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
