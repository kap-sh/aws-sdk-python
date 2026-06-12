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
    import aws_sdk_transfer.types.create_web_app_request
    import aws_sdk_transfer.types.create_web_app_response
    import aws_sdk_transfer.types.delete_web_app_request
    import aws_sdk_transfer.types.describe_web_app_request
    import aws_sdk_transfer.types.describe_web_app_response
    import aws_sdk_transfer.types.list_web_apps_request
    import aws_sdk_transfer.types.list_web_apps_response
    import aws_sdk_transfer.types.listed_web_app
    import aws_sdk_transfer.types.max_results
    import aws_sdk_transfer.types.next_token
    import aws_sdk_transfer.types.tags
    import aws_sdk_transfer.types.update_web_app_endpoint_details
    import aws_sdk_transfer.types.update_web_app_identity_provider_details
    import aws_sdk_transfer.types.update_web_app_request
    import aws_sdk_transfer.types.update_web_app_response
    import aws_sdk_transfer.types.web_app_access_endpoint
    import aws_sdk_transfer.types.web_app_endpoint_details
    import aws_sdk_transfer.types.web_app_endpoint_policy
    import aws_sdk_transfer.types.web_app_id
    import aws_sdk_transfer.types.web_app_identity_provider_details
    import aws_sdk_transfer.types.web_app_units
    from aws_sdk_transfer._services.async_transfer import (
        AsyncTransferClient,
        AsyncTransferClientConfig,
    )
    from aws_sdk_transfer._services.transfer import TransferClient, TransferClientConfig


class WebAppResource:
    def __init__(self, service: TransferClient) -> None:
        self._service = service

    def create(
        self,
        identity_provider_details: "aws_sdk_transfer.types.web_app_identity_provider_details.WebAppIdentityProviderDetails",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        access_endpoint: Optional[
            "aws_sdk_transfer.types.web_app_access_endpoint.WebAppAccessEndpoint"
        ] = None,
        web_app_units: Optional[
            "aws_sdk_transfer.types.web_app_units.WebAppUnits"
        ] = None,
        tags: Optional["aws_sdk_transfer.types.tags.Tags"] = None,
        web_app_endpoint_policy: Optional[
            "aws_sdk_transfer.types.web_app_endpoint_policy.WebAppEndpointPolicy"
        ] = None,
        endpoint_details: Optional[
            "aws_sdk_transfer.types.web_app_endpoint_details.WebAppEndpointDetails"
        ] = None,
    ) -> "aws_sdk_transfer.types.create_web_app_response.CreateWebAppResponse":
        """<p>Creates a web app based on specified parameters, and returns the ID for the new web app. You can configure the web app to be publicly accessible or hosted within a VPC.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html\">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            identity_provider_details: <p>You can provide a structure that contains the details for the identity provider to use with your web app.</p> <p>For more details about this parameter, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/webapp-identity-center.html\">Configure your identity provider for Transfer Family web apps</a>.</p>
            access_endpoint: <p>The <code>AccessEndpoint</code> is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.</p> <p>Before you enter a custom URL for this parameter, follow the steps described in <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/webapp-customize.html\">Update your access endpoint with a custom URL</a>.</p>
            web_app_units: <p>A union that contains the value for number of concurrent connections or the user sessions on your web app.</p>
            tags: <p>Key-value pairs that can be used to group and search for web apps.</p>
            web_app_endpoint_policy: <p> Setting for the type of endpoint policy for the web app. The default value is <code>STANDARD</code>. </p> <p>If you are creating the web app in an Amazon Web Services GovCloud (US) Region, you can set this parameter to <code>FIPS</code>.</p>
            endpoint_details: <p>The endpoint configuration for the web app. You can specify whether the web app endpoint is publicly accessible or hosted within a VPC.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.create_web_app_request.CreateWebAppRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.create_web_app_response.CreateWebAppResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.create_web_app

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.create_web_app.create_web_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.create_web_app_request.CreateWebAppRequest = {}  # type: ignore[typeddict-item]
        input["identity_provider_details"] = identity_provider_details
        if access_endpoint is not None:
            input["access_endpoint"] = access_endpoint
        if web_app_units is not None:
            input["web_app_units"] = web_app_units
        if tags is not None:
            input["tags"] = tags
        if web_app_endpoint_policy is not None:
            input["web_app_endpoint_policy"] = web_app_endpoint_policy
        if endpoint_details is not None:
            input["endpoint_details"] = endpoint_details

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_web_app_response.DescribeWebAppResponse":
        """<p>Describes the web app that's identified by <code>WebAppId</code>. The response includes endpoint configuration details such as whether the web app is publicly accessible or VPC hosted.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html\">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.describe_web_app_request.DescribeWebAppRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.describe_web_app_response.DescribeWebAppResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_web_app

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.describe_web_app.describe_web_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.describe_web_app_request.DescribeWebAppRequest = {}  # type: ignore[typeddict-item]
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
        identity_provider_details: Optional[
            "aws_sdk_transfer.types.update_web_app_identity_provider_details.UpdateWebAppIdentityProviderDetails"
        ] = None,
        access_endpoint: Optional[
            "aws_sdk_transfer.types.web_app_access_endpoint.WebAppAccessEndpoint"
        ] = None,
        web_app_units: Optional[
            "aws_sdk_transfer.types.web_app_units.WebAppUnits"
        ] = None,
        endpoint_details: Optional[
            "aws_sdk_transfer.types.update_web_app_endpoint_details.UpdateWebAppEndpointDetails"
        ] = None,
    ) -> "aws_sdk_transfer.types.update_web_app_response.UpdateWebAppResponse":
        """<p>Assigns new properties to a web app. You can modify the access point, identity provider details, endpoint configuration, and the web app units.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html\">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            web_app_id: <p>Provide the identifier of the web app that you are updating.</p>
            identity_provider_details: <p>Provide updated identity provider values in a <code>WebAppIdentityProviderDetails</code> object.</p>
            access_endpoint: <p>The <code>AccessEndpoint</code> is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.</p>
            web_app_units: <p>A union that contains the value for number of concurrent connections or the user sessions on your web app.</p>
            endpoint_details: <p>The updated endpoint configuration for the web app. You can modify the endpoint type and VPC configuration settings.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.update_web_app_request.UpdateWebAppRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.update_web_app_response.UpdateWebAppResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.update_web_app

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.update_web_app.update_web_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.update_web_app_request.UpdateWebAppRequest = {}  # type: ignore[typeddict-item]
        input["web_app_id"] = web_app_id
        if identity_provider_details is not None:
            input["identity_provider_details"] = identity_provider_details
        if access_endpoint is not None:
            input["access_endpoint"] = access_endpoint
        if web_app_units is not None:
            input["web_app_units"] = web_app_units
        if endpoint_details is not None:
            input["endpoint_details"] = endpoint_details

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
        """<p>Deletes the specified web app.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app that you are deleting.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.delete_web_app_request.DeleteWebAppRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.delete_web_app

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.delete_web_app.delete_web_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.delete_web_app_request.DeleteWebAppRequest = {}  # type: ignore[typeddict-item]
        input["web_app_id"] = web_app_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_transfer.types.list_web_apps_response.ListWebAppsResponse":
        """<p>Lists all web apps associated with your Amazon Web Services account for your current region. The response includes the endpoint type for each web app, showing whether it is publicly accessible or VPC hosted.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html\">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>Returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional web apps.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.list_web_apps_request.ListWebAppsRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.list_web_apps_response.ListWebAppsResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_web_apps

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.list_web_apps.list_web_apps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.list_web_apps_request.ListWebAppsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncWebAppResource:
    def __init__(self, service: AsyncTransferClient) -> None:
        self._service = service

    async def create(
        self,
        identity_provider_details: "aws_sdk_transfer.types.web_app_identity_provider_details.WebAppIdentityProviderDetails",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        access_endpoint: Optional[
            "aws_sdk_transfer.types.web_app_access_endpoint.WebAppAccessEndpoint"
        ] = None,
        web_app_units: Optional[
            "aws_sdk_transfer.types.web_app_units.WebAppUnits"
        ] = None,
        tags: Optional["aws_sdk_transfer.types.tags.Tags"] = None,
        web_app_endpoint_policy: Optional[
            "aws_sdk_transfer.types.web_app_endpoint_policy.WebAppEndpointPolicy"
        ] = None,
        endpoint_details: Optional[
            "aws_sdk_transfer.types.web_app_endpoint_details.WebAppEndpointDetails"
        ] = None,
    ) -> "aws_sdk_transfer.types.create_web_app_response.CreateWebAppResponse":
        """<p>Creates a web app based on specified parameters, and returns the ID for the new web app. You can configure the web app to be publicly accessible or hosted within a VPC.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html\">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            identity_provider_details: <p>You can provide a structure that contains the details for the identity provider to use with your web app.</p> <p>For more details about this parameter, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/webapp-identity-center.html\">Configure your identity provider for Transfer Family web apps</a>.</p>
            access_endpoint: <p>The <code>AccessEndpoint</code> is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.</p> <p>Before you enter a custom URL for this parameter, follow the steps described in <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/webapp-customize.html\">Update your access endpoint with a custom URL</a>.</p>
            web_app_units: <p>A union that contains the value for number of concurrent connections or the user sessions on your web app.</p>
            tags: <p>Key-value pairs that can be used to group and search for web apps.</p>
            web_app_endpoint_policy: <p> Setting for the type of endpoint policy for the web app. The default value is <code>STANDARD</code>. </p> <p>If you are creating the web app in an Amazon Web Services GovCloud (US) Region, you can set this parameter to <code>FIPS</code>.</p>
            endpoint_details: <p>The endpoint configuration for the web app. You can specify whether the web app endpoint is publicly accessible or hosted within a VPC.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.create_web_app_request.CreateWebAppRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.create_web_app_response.CreateWebAppResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.create_web_app

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.create_web_app.async_create_web_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.create_web_app_request.CreateWebAppRequest = {}  # type: ignore[typeddict-item]
        input["identity_provider_details"] = identity_provider_details
        if access_endpoint is not None:
            input["access_endpoint"] = access_endpoint
        if web_app_units is not None:
            input["web_app_units"] = web_app_units
        if tags is not None:
            input["tags"] = tags
        if web_app_endpoint_policy is not None:
            input["web_app_endpoint_policy"] = web_app_endpoint_policy
        if endpoint_details is not None:
            input["endpoint_details"] = endpoint_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_web_app_response.DescribeWebAppResponse":
        """<p>Describes the web app that's identified by <code>WebAppId</code>. The response includes endpoint configuration details such as whether the web app is publicly accessible or VPC hosted.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html\">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.describe_web_app_request.DescribeWebAppRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.describe_web_app_response.DescribeWebAppResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_web_app

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.describe_web_app.async_describe_web_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.describe_web_app_request.DescribeWebAppRequest = {}  # type: ignore[typeddict-item]
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
        identity_provider_details: Optional[
            "aws_sdk_transfer.types.update_web_app_identity_provider_details.UpdateWebAppIdentityProviderDetails"
        ] = None,
        access_endpoint: Optional[
            "aws_sdk_transfer.types.web_app_access_endpoint.WebAppAccessEndpoint"
        ] = None,
        web_app_units: Optional[
            "aws_sdk_transfer.types.web_app_units.WebAppUnits"
        ] = None,
        endpoint_details: Optional[
            "aws_sdk_transfer.types.update_web_app_endpoint_details.UpdateWebAppEndpointDetails"
        ] = None,
    ) -> "aws_sdk_transfer.types.update_web_app_response.UpdateWebAppResponse":
        """<p>Assigns new properties to a web app. You can modify the access point, identity provider details, endpoint configuration, and the web app units.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html\">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            web_app_id: <p>Provide the identifier of the web app that you are updating.</p>
            identity_provider_details: <p>Provide updated identity provider values in a <code>WebAppIdentityProviderDetails</code> object.</p>
            access_endpoint: <p>The <code>AccessEndpoint</code> is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.</p>
            web_app_units: <p>A union that contains the value for number of concurrent connections or the user sessions on your web app.</p>
            endpoint_details: <p>The updated endpoint configuration for the web app. You can modify the endpoint type and VPC configuration settings.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.update_web_app_request.UpdateWebAppRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.update_web_app_response.UpdateWebAppResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.update_web_app

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.update_web_app.async_update_web_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.update_web_app_request.UpdateWebAppRequest = {}  # type: ignore[typeddict-item]
        input["web_app_id"] = web_app_id
        if identity_provider_details is not None:
            input["identity_provider_details"] = identity_provider_details
        if access_endpoint is not None:
            input["access_endpoint"] = access_endpoint
        if web_app_units is not None:
            input["web_app_units"] = web_app_units
        if endpoint_details is not None:
            input["endpoint_details"] = endpoint_details

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
        """<p>Deletes the specified web app.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app that you are deleting.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.delete_web_app_request.DeleteWebAppRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.delete_web_app

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.delete_web_app.async_delete_web_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.delete_web_app_request.DeleteWebAppRequest = {}  # type: ignore[typeddict-item]
        input["web_app_id"] = web_app_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_transfer.types.list_web_apps_response.ListWebAppsResponse":
        """<p>Lists all web apps associated with your Amazon Web Services account for your current region. The response includes the endpoint type for each web app, showing whether it is publicly accessible or VPC hosted.</p> <p>For more information about using VPC endpoints with Transfer Family, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/create-webapp-in-vpc.html\">Create a Transfer Family web app in a VPC</a>.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>Returns the <code>NextToken</code> parameter in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional web apps.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.list_web_apps_request.ListWebAppsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.list_web_apps_response.ListWebAppsResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_web_apps

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.list_web_apps.async_list_web_apps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_transfer.types.list_web_apps_request.ListWebAppsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
