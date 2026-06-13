from typing import TYPE_CHECKING, Optional

import aws_sdk_pca_connector_scep._auth._signers
import aws_sdk_pca_connector_scep._auth._sigv4
from aws_sdk_pca_connector_scep._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.certificate_authority_arn
    import aws_sdk_pca_connector_scep.types.client_token
    import aws_sdk_pca_connector_scep.types.connector_arn
    import aws_sdk_pca_connector_scep.types.connector_summary
    import aws_sdk_pca_connector_scep.types.create_connector_request
    import aws_sdk_pca_connector_scep.types.create_connector_response
    import aws_sdk_pca_connector_scep.types.delete_connector_request
    import aws_sdk_pca_connector_scep.types.get_connector_request
    import aws_sdk_pca_connector_scep.types.get_connector_response
    import aws_sdk_pca_connector_scep.types.list_connectors_request
    import aws_sdk_pca_connector_scep.types.list_connectors_response
    import aws_sdk_pca_connector_scep.types.max_results
    import aws_sdk_pca_connector_scep.types.mobile_device_management
    import aws_sdk_pca_connector_scep.types.next_token
    import aws_sdk_pca_connector_scep.types.tags
    import aws_sdk_pca_connector_scep.types.vpc_endpoint_id
    from aws_sdk_pca_connector_scep._services.async_pca_connector_scep import (
        AsyncPcaConnectorScepClient,
        AsyncPcaConnectorScepClientConfig,
    )
    from aws_sdk_pca_connector_scep._services.pca_connector_scep import (
        PcaConnectorScepClient,
        PcaConnectorScepClientConfig,
    )


class ConnectorResource:
    def __init__(self, service: PcaConnectorScepClient) -> None:
        self._service = service

    def create(
        self,
        certificate_authority_arn: "aws_sdk_pca_connector_scep.types.certificate_authority_arn.CertificateAuthorityArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
        mobile_device_management: Optional[
            "aws_sdk_pca_connector_scep.types.mobile_device_management.MobileDeviceManagement"
        ] = None,
        vpc_endpoint_id: Optional[
            "aws_sdk_pca_connector_scep.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        client_token: Optional[
            "aws_sdk_pca_connector_scep.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_pca_connector_scep.types.tags.Tags"] = None,
    ) -> "aws_sdk_pca_connector_scep.types.create_connector_response.CreateConnectorResponse":
        """<p>Creates a SCEP connector. A SCEP connector links Amazon Web Services Private Certificate Authority to your SCEP-compatible devices and mobile device management (MDM) systems. Before you create a connector, you must complete a set of prerequisites, including creation of a private certificate authority (CA) to use with this connector. For more information, see <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-prerequisites.html\">Connector for SCEP prerequisites</a>.</p>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Private Certificate Authority certificate authority to use with this connector. Due to security vulnerabilities present in the SCEP protocol, we recommend using a private CA that's dedicated for use with the connector.</p> <p>To retrieve the private CAs associated with your account, you can call <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html\">ListCertificateAuthorities</a> using the Amazon Web Services Private CA API.</p>
            mobile_device_management: <p>If you don't supply a value, by default Connector for SCEP creates a connector for general-purpose use. A general-purpose connector is designed to work with clients or endpoints that support the SCEP protocol, except Connector for SCEP for Microsoft Intune. With connectors for general-purpose use, you manage SCEP challenge passwords using Connector for SCEP. For information about considerations and limitations with using Connector for SCEP, see <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlc4scep-considerations-limitations.html\">Considerations and Limitations</a>.</p> <p>If you provide an <code>IntuneConfiguration</code>, Connector for SCEP creates a connector for use with Microsoft Intune, and you manage the challenge passwords using Microsoft Intune. For more information, see <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html\">Using Connector for SCEP for Microsoft Intune</a>.</p>
            vpc_endpoint_id: <p>If you don't supply a value, by default Connector for SCEP creates a connector accessible over the public internet. If you provide a VPC endpoint ID, creates a connector accessible only through that specific VPC endpoint.</p>
            client_token: <p>Custom string that can be used to distinguish between calls to the <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html\">CreateChallenge</a> action. Client tokens for <code>CreateChallenge</code> time out after five minutes. Therefore, if you call <code>CreateChallenge</code> multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.</p>
            tags: <p>The key-value pairs to associate with the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_scep.types.create_connector_request.CreateConnectorRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_scep.types.create_connector_response.CreateConnectorResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.create_connector

            output, http_response = (
                aws_sdk_pca_connector_scep._operations.pca_connector_scep.create_connector.create_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_scep.types.create_connector_request.CreateConnectorRequest = {}  # type: ignore[typeddict-item]
        input["certificate_authority_arn"] = certificate_authority_arn
        if mobile_device_management is not None:
            input["mobile_device_management"] = mobile_device_management
        if vpc_endpoint_id is not None:
            input["vpc_endpoint_id"] = vpc_endpoint_id
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
        connector_arn: "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
    ) -> "aws_sdk_pca_connector_scep.types.get_connector_response.GetConnectorResponse":
        """<p>Retrieves details about the specified <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Connector.html\">Connector</a>. Calling this action returns important details about the connector, such as the public SCEP URL where your clients can request certificates.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_scep.types.get_connector_request.GetConnectorRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_scep.types.get_connector_response.GetConnectorResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_connector

            output, http_response = (
                aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_connector.get_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_scep.types.get_connector_request.GetConnectorRequest = {}  # type: ignore[typeddict-item]
        input["connector_arn"] = connector_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        connector_arn: "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Connector.html\">Connector</a>. This operation also deletes any challenges associated with the connector.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_scep.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.delete_connector

            output, http_response = (
                aws_sdk_pca_connector_scep._operations.pca_connector_scep.delete_connector.delete_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_scep.types.delete_connector_request.DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
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
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
        max_results: Optional[
            "aws_sdk_pca_connector_scep.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_pca_connector_scep.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_pca_connector_scep.types.list_connectors_response.ListConnectorsResponse":
        """<p>Lists the connectors belonging to your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of objects that you want Connector for SCEP to return for this request. If more objects are available, in the response, Connector for SCEP provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_scep.types.list_connectors_request.ListConnectorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_scep.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.list_connectors

            output, http_response = (
                aws_sdk_pca_connector_scep._operations.pca_connector_scep.list_connectors.list_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_scep.types.list_connectors_request.ListConnectorsRequest = {}  # type: ignore[typeddict-item]
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
    def __init__(self, service: AsyncPcaConnectorScepClient) -> None:
        self._service = service

    async def create(
        self,
        certificate_authority_arn: "aws_sdk_pca_connector_scep.types.certificate_authority_arn.CertificateAuthorityArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        mobile_device_management: Optional[
            "aws_sdk_pca_connector_scep.types.mobile_device_management.MobileDeviceManagement"
        ] = None,
        vpc_endpoint_id: Optional[
            "aws_sdk_pca_connector_scep.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        client_token: Optional[
            "aws_sdk_pca_connector_scep.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_pca_connector_scep.types.tags.Tags"] = None,
    ) -> "aws_sdk_pca_connector_scep.types.create_connector_response.CreateConnectorResponse":
        """<p>Creates a SCEP connector. A SCEP connector links Amazon Web Services Private Certificate Authority to your SCEP-compatible devices and mobile device management (MDM) systems. Before you create a connector, you must complete a set of prerequisites, including creation of a private certificate authority (CA) to use with this connector. For more information, see <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-prerequisites.html\">Connector for SCEP prerequisites</a>.</p>

        Args:
            certificate_authority_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Private Certificate Authority certificate authority to use with this connector. Due to security vulnerabilities present in the SCEP protocol, we recommend using a private CA that's dedicated for use with the connector.</p> <p>To retrieve the private CAs associated with your account, you can call <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html\">ListCertificateAuthorities</a> using the Amazon Web Services Private CA API.</p>
            mobile_device_management: <p>If you don't supply a value, by default Connector for SCEP creates a connector for general-purpose use. A general-purpose connector is designed to work with clients or endpoints that support the SCEP protocol, except Connector for SCEP for Microsoft Intune. With connectors for general-purpose use, you manage SCEP challenge passwords using Connector for SCEP. For information about considerations and limitations with using Connector for SCEP, see <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlc4scep-considerations-limitations.html\">Considerations and Limitations</a>.</p> <p>If you provide an <code>IntuneConfiguration</code>, Connector for SCEP creates a connector for use with Microsoft Intune, and you manage the challenge passwords using Microsoft Intune. For more information, see <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html\">Using Connector for SCEP for Microsoft Intune</a>.</p>
            vpc_endpoint_id: <p>If you don't supply a value, by default Connector for SCEP creates a connector accessible over the public internet. If you provide a VPC endpoint ID, creates a connector accessible only through that specific VPC endpoint.</p>
            client_token: <p>Custom string that can be used to distinguish between calls to the <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html\">CreateChallenge</a> action. Client tokens for <code>CreateChallenge</code> time out after five minutes. Therefore, if you call <code>CreateChallenge</code> multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.</p>
            tags: <p>The key-value pairs to associate with the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_scep.types.create_connector_request.CreateConnectorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_scep.types.create_connector_response.CreateConnectorResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.create_connector

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_scep._operations.pca_connector_scep.create_connector.async_create_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_scep.types.create_connector_request.CreateConnectorRequest = {}  # type: ignore[typeddict-item]
        input["certificate_authority_arn"] = certificate_authority_arn
        if mobile_device_management is not None:
            input["mobile_device_management"] = mobile_device_management
        if vpc_endpoint_id is not None:
            input["vpc_endpoint_id"] = vpc_endpoint_id
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
        connector_arn: "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> "aws_sdk_pca_connector_scep.types.get_connector_response.GetConnectorResponse":
        """<p>Retrieves details about the specified <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Connector.html\">Connector</a>. Calling this action returns important details about the connector, such as the public SCEP URL where your clients can request certificates.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_scep.types.get_connector_request.GetConnectorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_scep.types.get_connector_response.GetConnectorResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_connector

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_connector.async_get_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_scep.types.get_connector_request.GetConnectorRequest = {}  # type: ignore[typeddict-item]
        input["connector_arn"] = connector_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        connector_arn: "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Connector.html\">Connector</a>. This operation also deletes any challenges associated with the connector.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_scep.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.delete_connector

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_scep._operations.pca_connector_scep.delete_connector.async_delete_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_scep.types.delete_connector_request.DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
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
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        max_results: Optional[
            "aws_sdk_pca_connector_scep.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_pca_connector_scep.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_pca_connector_scep.types.list_connectors_response.ListConnectorsResponse":
        """<p>Lists the connectors belonging to your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of objects that you want Connector for SCEP to return for this request. If more objects are available, in the response, Connector for SCEP provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_scep.types.list_connectors_request.ListConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_scep.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.list_connectors

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_scep._operations.pca_connector_scep.list_connectors.async_list_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_pca_connector_scep.types.list_connectors_request.ListConnectorsRequest = {}  # type: ignore[typeddict-item]
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
