from typing import TYPE_CHECKING, Optional

import aws_sdk_pca_connector_ad._auth._signers
import aws_sdk_pca_connector_ad._auth._sigv4
from aws_sdk_pca_connector_ad._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.client_token
    import aws_sdk_pca_connector_ad.types.connector_arn
    import aws_sdk_pca_connector_ad.types.create_service_principal_name_request
    import aws_sdk_pca_connector_ad.types.delete_service_principal_name_request
    import aws_sdk_pca_connector_ad.types.directory_registration_arn
    import aws_sdk_pca_connector_ad.types.get_service_principal_name_request
    import aws_sdk_pca_connector_ad.types.get_service_principal_name_response
    import aws_sdk_pca_connector_ad.types.list_service_principal_names_request
    import aws_sdk_pca_connector_ad.types.list_service_principal_names_response
    import aws_sdk_pca_connector_ad.types.max_results
    import aws_sdk_pca_connector_ad.types.next_token
    import aws_sdk_pca_connector_ad.types.service_principal_name_summary
    from aws_sdk_pca_connector_ad._services.async_pca_connector_ad import (
        AsyncPcaConnectorAdClient,
        AsyncPcaConnectorAdClientConfig,
    )
    from aws_sdk_pca_connector_ad._services.pca_connector_ad import (
        PcaConnectorAdClient,
        PcaConnectorAdClientConfig,
    )


class ServicePrincipalNameResource:
    def __init__(self, service: PcaConnectorAdClient) -> None:
        self._service = service

    def put(
        self,
        directory_registration_arn: "aws_sdk_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Creates a service principal name (SPN) for the service account in Active Directory. Kerberos authentication uses SPNs to associate a service instance with a service sign-in account.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html\">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>
            client_token: <p>Idempotency token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.create_service_principal_name_request.CreateServicePrincipalNameRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_service_principal_name

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_service_principal_name.create_service_principal_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.create_service_principal_name_request.CreateServicePrincipalNameRequest = {}  # type: ignore[typeddict-item]
        input["directory_registration_arn"] = directory_registration_arn
        input["connector_arn"] = connector_arn
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        directory_registration_arn: "aws_sdk_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> "aws_sdk_pca_connector_ad.types.get_service_principal_name_response.GetServicePrincipalNameResponse":
        """<p>Lists the service principal name that the connector uses to authenticate with Active Directory.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html\">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.get_service_principal_name_request.GetServicePrincipalNameRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_ad.types.get_service_principal_name_response.GetServicePrincipalNameResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_service_principal_name

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_service_principal_name.get_service_principal_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.get_service_principal_name_request.GetServicePrincipalNameRequest = {}  # type: ignore[typeddict-item]
        input["directory_registration_arn"] = directory_registration_arn
        input["connector_arn"] = connector_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        directory_registration_arn: "aws_sdk_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes the service principal name (SPN) used by a connector to authenticate with your Active Directory.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html\">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.delete_service_principal_name_request.DeleteServicePrincipalNameRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_service_principal_name

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_service_principal_name.delete_service_principal_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.delete_service_principal_name_request.DeleteServicePrincipalNameRequest = {}  # type: ignore[typeddict-item]
        input["directory_registration_arn"] = directory_registration_arn
        input["connector_arn"] = connector_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        directory_registration_arn: "aws_sdk_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "aws_sdk_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_pca_connector_ad.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_pca_connector_ad.types.list_service_principal_names_response.ListServicePrincipalNamesResponse":
        """<p>Lists the service principal names that the connector uses to authenticate with Active Directory.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html\">CreateDirectoryRegistration</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.list_service_principal_names_request.ListServicePrincipalNamesRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_ad.types.list_service_principal_names_response.ListServicePrincipalNamesResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_service_principal_names

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_service_principal_names.list_service_principal_names(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.list_service_principal_names_request.ListServicePrincipalNamesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["directory_registration_arn"] = directory_registration_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncServicePrincipalNameResource:
    def __init__(self, service: AsyncPcaConnectorAdClient) -> None:
        self._service = service

    async def put(
        self,
        directory_registration_arn: "aws_sdk_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Creates a service principal name (SPN) for the service account in Active Directory. Kerberos authentication uses SPNs to associate a service instance with a service sign-in account.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html\">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>
            client_token: <p>Idempotency token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.create_service_principal_name_request.CreateServicePrincipalNameRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_service_principal_name

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_service_principal_name.async_create_service_principal_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.create_service_principal_name_request.CreateServicePrincipalNameRequest = {}  # type: ignore[typeddict-item]
        input["directory_registration_arn"] = directory_registration_arn
        input["connector_arn"] = connector_arn
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        directory_registration_arn: "aws_sdk_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "aws_sdk_pca_connector_ad.types.get_service_principal_name_response.GetServicePrincipalNameResponse":
        """<p>Lists the service principal name that the connector uses to authenticate with Active Directory.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html\">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.get_service_principal_name_request.GetServicePrincipalNameRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_ad.types.get_service_principal_name_response.GetServicePrincipalNameResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_service_principal_name

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_service_principal_name.async_get_service_principal_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.get_service_principal_name_request.GetServicePrincipalNameRequest = {}  # type: ignore[typeddict-item]
        input["directory_registration_arn"] = directory_registration_arn
        input["connector_arn"] = connector_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        directory_registration_arn: "aws_sdk_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        connector_arn: "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes the service principal name (SPN) used by a connector to authenticate with your Active Directory.</p>

        Args:
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html\">CreateDirectoryRegistration</a>.</p>
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.delete_service_principal_name_request.DeleteServicePrincipalNameRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_service_principal_name

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_service_principal_name.async_delete_service_principal_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.delete_service_principal_name_request.DeleteServicePrincipalNameRequest = {}  # type: ignore[typeddict-item]
        input["directory_registration_arn"] = directory_registration_arn
        input["connector_arn"] = connector_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        directory_registration_arn: "aws_sdk_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "aws_sdk_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_pca_connector_ad.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_pca_connector_ad.types.list_service_principal_names_response.ListServicePrincipalNamesResponse":
        """<p>Lists the service principal names that the connector uses to authenticate with Active Directory.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
            directory_registration_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html\">CreateDirectoryRegistration</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.list_service_principal_names_request.ListServicePrincipalNamesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_ad.types.list_service_principal_names_response.ListServicePrincipalNamesResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_service_principal_names

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_service_principal_names.async_list_service_principal_names(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.list_service_principal_names_request.ListServicePrincipalNamesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["directory_registration_arn"] = directory_registration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
