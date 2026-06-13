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
    import aws_sdk_pca_connector_ad.types.certificate_authority_arn
    import aws_sdk_pca_connector_ad.types.client_token
    import aws_sdk_pca_connector_ad.types.connector_arn
    import aws_sdk_pca_connector_ad.types.connector_summary
    import aws_sdk_pca_connector_ad.types.create_connector_request
    import aws_sdk_pca_connector_ad.types.create_connector_response
    import aws_sdk_pca_connector_ad.types.delete_connector_request
    import aws_sdk_pca_connector_ad.types.directory_id
    import aws_sdk_pca_connector_ad.types.get_connector_request
    import aws_sdk_pca_connector_ad.types.get_connector_response
    import aws_sdk_pca_connector_ad.types.list_connectors_request
    import aws_sdk_pca_connector_ad.types.list_connectors_response
    import aws_sdk_pca_connector_ad.types.max_results
    import aws_sdk_pca_connector_ad.types.next_token
    import aws_sdk_pca_connector_ad.types.tags
    import aws_sdk_pca_connector_ad.types.vpc_information
    from aws_sdk_pca_connector_ad._services.async_pca_connector_ad import (
        AsyncPcaConnectorAdClient,
        AsyncPcaConnectorAdClientConfig,
    )
    from aws_sdk_pca_connector_ad._services.pca_connector_ad import (
        PcaConnectorAdClient,
        PcaConnectorAdClientConfig,
    )


class ConnectorResource:
    def __init__(self, service: PcaConnectorAdClient) -> None:
        self._service = service

    def create(
        self,
        directory_id: "aws_sdk_pca_connector_ad.types.directory_id.DirectoryId",
        certificate_authority_arn: "aws_sdk_pca_connector_ad.types.certificate_authority_arn.CertificateAuthorityArn",
        vpc_information: "aws_sdk_pca_connector_ad.types.vpc_information.VpcInformation",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_pca_connector_ad.types.tags.Tags"] = None,
    ) -> "aws_sdk_pca_connector_ad.types.create_connector_response.CreateConnectorResponse":
        """<p>Creates a connector between Amazon Web Services Private CA and an Active Directory. You must specify the private CA, directory ID, and security groups.</p>

        Args:
            directory_id: <p>The identifier of the Active Directory.</p>
            certificate_authority_arn: <p> The Amazon Resource Name (ARN) of the certificate authority being used.</p>
            vpc_information: <p>Information about your VPC and security groups used with the connector.</p>
            client_token: <p>Idempotency token.</p>
            tags: <p>Metadata assigned to a connector consisting of a key-value pair.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.create_connector_request.CreateConnectorRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_ad.types.create_connector_response.CreateConnectorResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_connector

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_connector.create_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.create_connector_request.CreateConnectorRequest = {}  # type: ignore[typeddict-item]
        input["directory_id"] = directory_id
        input["certificate_authority_arn"] = certificate_authority_arn
        input["vpc_information"] = vpc_information
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        connector_arn: "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> "aws_sdk_pca_connector_ad.types.get_connector_response.GetConnectorResponse":
        """<p>Lists information about your connector. You specify the connector on input by its ARN (Amazon Resource Name). </p>

        Args:
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.get_connector_request.GetConnectorRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_ad.types.get_connector_response.GetConnectorResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_connector

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_connector.get_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.get_connector_request.GetConnectorRequest = {}  # type: ignore[typeddict-item]
        input["connector_arn"] = connector_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        connector_arn: "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a connector for Active Directory. You must provide the Amazon Resource Name (ARN) of the connector that you want to delete. You can find the ARN by calling the <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListConnectors\">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListConnectors</a> action. Deleting a connector does not deregister your directory with Amazon Web Services Private CA. You can deregister your directory by calling the <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteDirectoryRegistration\">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteDirectoryRegistration</a> action.</p>

        Args:
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_connector

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_connector.delete_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.delete_connector_request.DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
        input["connector_arn"] = connector_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "aws_sdk_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_pca_connector_ad.types.next_token.NextToken"
        ] = None,
    ) -> (
        "aws_sdk_pca_connector_ad.types.list_connectors_response.ListConnectorsResponse"
    ):
        """<p>Lists the connectors that you created by using the <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector\">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector</a> action.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_ad.types.list_connectors_request.ListConnectorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_ad.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_connectors

            output, http_response = (
                aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_connectors.list_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.list_connectors_request.ListConnectorsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncConnectorResource:
    def __init__(self, service: AsyncPcaConnectorAdClient) -> None:
        self._service = service

    async def create(
        self,
        directory_id: "aws_sdk_pca_connector_ad.types.directory_id.DirectoryId",
        certificate_authority_arn: "aws_sdk_pca_connector_ad.types.certificate_authority_arn.CertificateAuthorityArn",
        vpc_information: "aws_sdk_pca_connector_ad.types.vpc_information.VpcInformation",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_pca_connector_ad.types.tags.Tags"] = None,
    ) -> "aws_sdk_pca_connector_ad.types.create_connector_response.CreateConnectorResponse":
        """<p>Creates a connector between Amazon Web Services Private CA and an Active Directory. You must specify the private CA, directory ID, and security groups.</p>

        Args:
            directory_id: <p>The identifier of the Active Directory.</p>
            certificate_authority_arn: <p> The Amazon Resource Name (ARN) of the certificate authority being used.</p>
            vpc_information: <p>Information about your VPC and security groups used with the connector.</p>
            client_token: <p>Idempotency token.</p>
            tags: <p>Metadata assigned to a connector consisting of a key-value pair.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.create_connector_request.CreateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_ad.types.create_connector_response.CreateConnectorResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_connector

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.create_connector.async_create_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.create_connector_request.CreateConnectorRequest = {}  # type: ignore[typeddict-item]
        input["directory_id"] = directory_id
        input["certificate_authority_arn"] = certificate_authority_arn
        input["vpc_information"] = vpc_information
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        connector_arn: "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "aws_sdk_pca_connector_ad.types.get_connector_response.GetConnectorResponse":
        """<p>Lists information about your connector. You specify the connector on input by its ARN (Amazon Resource Name). </p>

        Args:
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.get_connector_request.GetConnectorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_ad.types.get_connector_response.GetConnectorResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_connector

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.get_connector.async_get_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.get_connector_request.GetConnectorRequest = {}  # type: ignore[typeddict-item]
        input["connector_arn"] = connector_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        connector_arn: "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a connector for Active Directory. You must provide the Amazon Resource Name (ARN) of the connector that you want to delete. You can find the ARN by calling the <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListConnectors\">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListConnectors</a> action. Deleting a connector does not deregister your directory with Amazon Web Services Private CA. You can deregister your directory by calling the <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteDirectoryRegistration\">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteDirectoryRegistration</a> action.</p>

        Args:
            connector_arn: <p> The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_connector

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.delete_connector.async_delete_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.delete_connector_request.DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
        input["connector_arn"] = connector_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "aws_sdk_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_pca_connector_ad.types.next_token.NextToken"
        ] = None,
    ) -> (
        "aws_sdk_pca_connector_ad.types.list_connectors_response.ListConnectorsResponse"
    ):
        """<p>Lists the connectors that you created by using the <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector\">https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector</a> action.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_ad.types.list_connectors_request.ListConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_ad.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_connectors

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_ad._operations.pca_connector_ad.list_connectors.async_list_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_ad.types.list_connectors_request.ListConnectorsRequest = {}  # type: ignore[typeddict-item]
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
