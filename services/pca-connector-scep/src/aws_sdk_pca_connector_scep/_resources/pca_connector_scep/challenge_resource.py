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
    import aws_sdk_pca_connector_scep.types.challenge_arn
    import aws_sdk_pca_connector_scep.types.challenge_metadata_summary
    import aws_sdk_pca_connector_scep.types.client_token
    import aws_sdk_pca_connector_scep.types.connector_arn
    import aws_sdk_pca_connector_scep.types.create_challenge_request
    import aws_sdk_pca_connector_scep.types.create_challenge_response
    import aws_sdk_pca_connector_scep.types.delete_challenge_request
    import aws_sdk_pca_connector_scep.types.get_challenge_metadata_request
    import aws_sdk_pca_connector_scep.types.get_challenge_metadata_response
    import aws_sdk_pca_connector_scep.types.get_challenge_password_request
    import aws_sdk_pca_connector_scep.types.get_challenge_password_response
    import aws_sdk_pca_connector_scep.types.list_challenge_metadata_request
    import aws_sdk_pca_connector_scep.types.list_challenge_metadata_response
    import aws_sdk_pca_connector_scep.types.max_results
    import aws_sdk_pca_connector_scep.types.next_token
    import aws_sdk_pca_connector_scep.types.tags
    from aws_sdk_pca_connector_scep._services.async_pca_connector_scep import (
        AsyncPcaConnectorScepClient,
        AsyncPcaConnectorScepClientConfig,
    )
    from aws_sdk_pca_connector_scep._services.pca_connector_scep import (
        PcaConnectorScepClient,
        PcaConnectorScepClientConfig,
    )


class ChallengeResource:
    def __init__(self, service: PcaConnectorScepClient) -> None:
        self._service = service

    def create(
        self,
        connector_arn: "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pca_connector_scep.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_pca_connector_scep.types.tags.Tags"] = None,
    ) -> "aws_sdk_pca_connector_scep.types.create_challenge_response.CreateChallengeResponse":
        """<p>For general-purpose connectors. Creates a <i>challenge password</i> for the specified connector. The SCEP protocol uses a challenge password to authenticate a request before issuing a certificate from a certificate authority (CA). Your SCEP clients include the challenge password as part of their certificate request to Connector for SCEP. To retrieve the connector Amazon Resource Names (ARNs) for the connectors in your account, call <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListConnectors.html\">ListConnectors</a>.</p> <p>To create additional challenge passwords for the connector, call <code>CreateChallenge</code> again. We recommend frequently rotating your challenge passwords.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector that you want to create a challenge for.</p>
            client_token: <p>Custom string that can be used to distinguish between calls to the <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html\">CreateChallenge</a> action. Client tokens for <code>CreateChallenge</code> time out after five minutes. Therefore, if you call <code>CreateChallenge</code> multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.</p>
            tags: <p>The key-value pairs to associate with the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_scep.types.create_challenge_request.CreateChallengeRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_scep.types.create_challenge_response.CreateChallengeResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.create_challenge

            output, http_response = (
                aws_sdk_pca_connector_scep._operations.pca_connector_scep.create_challenge.create_challenge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pca_connector_scep.types.create_challenge_request.CreateChallengeRequest = {}  # type: ignore[typeddict-item]
        input_["connector_arn"] = connector_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        challenge_arn: "aws_sdk_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
    ) -> "aws_sdk_pca_connector_scep.types.get_challenge_metadata_response.GetChallengeMetadataResponse":
        """<p>Retrieves the metadata for the specified <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html\">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_scep.types.get_challenge_metadata_request.GetChallengeMetadataRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_scep.types.get_challenge_metadata_response.GetChallengeMetadataResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_challenge_metadata

            output, http_response = (
                aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_challenge_metadata.get_challenge_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pca_connector_scep.types.get_challenge_metadata_request.GetChallengeMetadataRequest = {}  # type: ignore[typeddict-item]
        input_["challenge_arn"] = challenge_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        challenge_arn: "aws_sdk_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html\">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge password to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_scep.types.delete_challenge_request.DeleteChallengeRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.delete_challenge

            output, http_response = (
                aws_sdk_pca_connector_scep._operations.pca_connector_scep.delete_challenge.delete_challenge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pca_connector_scep.types.delete_challenge_request.DeleteChallengeRequest = {}  # type: ignore[typeddict-item]
        input_["challenge_arn"] = challenge_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        connector_arn: "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
        max_results: Optional[
            "aws_sdk_pca_connector_scep.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_pca_connector_scep.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_pca_connector_scep.types.list_challenge_metadata_response.ListChallengeMetadataResponse":
        """<p>Retrieves the challenge metadata for the specified ARN.</p>

        Args:
            max_results: <p>The maximum number of objects that you want Connector for SCEP to return for this request. If more objects are available, in the response, Connector for SCEP provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_scep.types.list_challenge_metadata_request.ListChallengeMetadataRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_scep.types.list_challenge_metadata_response.ListChallengeMetadataResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.list_challenge_metadata

            output, http_response = (
                aws_sdk_pca_connector_scep._operations.pca_connector_scep.list_challenge_metadata.list_challenge_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pca_connector_scep.types.list_challenge_metadata_request.ListChallengeMetadataRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["connector_arn"] = connector_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_challenge_password(
        self,
        challenge_arn: "aws_sdk_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[PcaConnectorScepClientConfig] = None,
    ) -> "aws_sdk_pca_connector_scep.types.get_challenge_password_response.GetChallengePasswordResponse":
        """<p>Retrieves the challenge password for the specified <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html\">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_pca_connector_scep.types.get_challenge_password_request.GetChallengePasswordRequest]",
        ) -> OperationResponse[
            "aws_sdk_pca_connector_scep.types.get_challenge_password_response.GetChallengePasswordResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_challenge_password

            output, http_response = (
                aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_challenge_password.get_challenge_password(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pca_connector_scep.types.get_challenge_password_request.GetChallengePasswordRequest = {}  # type: ignore[typeddict-item]
        input_["challenge_arn"] = challenge_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncChallengeResource:
    def __init__(self, service: AsyncPcaConnectorScepClient) -> None:
        self._service = service

    async def create(
        self,
        connector_arn: "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        client_token: Optional[
            "aws_sdk_pca_connector_scep.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_pca_connector_scep.types.tags.Tags"] = None,
    ) -> "aws_sdk_pca_connector_scep.types.create_challenge_response.CreateChallengeResponse":
        """<p>For general-purpose connectors. Creates a <i>challenge password</i> for the specified connector. The SCEP protocol uses a challenge password to authenticate a request before issuing a certificate from a certificate authority (CA). Your SCEP clients include the challenge password as part of their certificate request to Connector for SCEP. To retrieve the connector Amazon Resource Names (ARNs) for the connectors in your account, call <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListConnectors.html\">ListConnectors</a>.</p> <p>To create additional challenge passwords for the connector, call <code>CreateChallenge</code> again. We recommend frequently rotating your challenge passwords.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector that you want to create a challenge for.</p>
            client_token: <p>Custom string that can be used to distinguish between calls to the <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html\">CreateChallenge</a> action. Client tokens for <code>CreateChallenge</code> time out after five minutes. Therefore, if you call <code>CreateChallenge</code> multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.</p>
            tags: <p>The key-value pairs to associate with the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_scep.types.create_challenge_request.CreateChallengeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_scep.types.create_challenge_response.CreateChallengeResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.create_challenge

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_scep._operations.pca_connector_scep.create_challenge.async_create_challenge(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pca_connector_scep.types.create_challenge_request.CreateChallengeRequest = {}  # type: ignore[typeddict-item]
        input_["connector_arn"] = connector_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        challenge_arn: "aws_sdk_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> "aws_sdk_pca_connector_scep.types.get_challenge_metadata_response.GetChallengeMetadataResponse":
        """<p>Retrieves the metadata for the specified <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html\">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_scep.types.get_challenge_metadata_request.GetChallengeMetadataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_scep.types.get_challenge_metadata_response.GetChallengeMetadataResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_challenge_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_challenge_metadata.async_get_challenge_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pca_connector_scep.types.get_challenge_metadata_request.GetChallengeMetadataRequest = {}  # type: ignore[typeddict-item]
        input_["challenge_arn"] = challenge_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        challenge_arn: "aws_sdk_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html\">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge password to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_scep.types.delete_challenge_request.DeleteChallengeRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.delete_challenge

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_scep._operations.pca_connector_scep.delete_challenge.async_delete_challenge(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pca_connector_scep.types.delete_challenge_request.DeleteChallengeRequest = {}  # type: ignore[typeddict-item]
        input_["challenge_arn"] = challenge_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        connector_arn: "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
        max_results: Optional[
            "aws_sdk_pca_connector_scep.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_pca_connector_scep.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_pca_connector_scep.types.list_challenge_metadata_response.ListChallengeMetadataResponse":
        """<p>Retrieves the challenge metadata for the specified ARN.</p>

        Args:
            max_results: <p>The maximum number of objects that you want Connector for SCEP to return for this request. If more objects are available, in the response, Connector for SCEP provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>
            next_token: <p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) of the connector.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_scep.types.list_challenge_metadata_request.ListChallengeMetadataRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_scep.types.list_challenge_metadata_response.ListChallengeMetadataResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.list_challenge_metadata

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_scep._operations.pca_connector_scep.list_challenge_metadata.async_list_challenge_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pca_connector_scep.types.list_challenge_metadata_request.ListChallengeMetadataRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["connector_arn"] = connector_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_challenge_password(
        self,
        challenge_arn: "aws_sdk_pca_connector_scep.types.challenge_arn.ChallengeArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorScepClientConfig] = None,
    ) -> "aws_sdk_pca_connector_scep.types.get_challenge_password_response.GetChallengePasswordResponse":
        """<p>Retrieves the challenge password for the specified <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html\">Challenge</a>.</p>

        Args:
            challenge_arn: <p>The Amazon Resource Name (ARN) of the challenge.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_pca_connector_scep.types.get_challenge_password_request.GetChallengePasswordRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_pca_connector_scep.types.get_challenge_password_response.GetChallengePasswordResponse"
        ]:
            import aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_challenge_password

            (
                output,
                http_response,
            ) = await aws_sdk_pca_connector_scep._operations.pca_connector_scep.get_challenge_password.async_get_challenge_password(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_pca_connector_scep.types.get_challenge_password_request.GetChallengePasswordRequest = {}  # type: ignore[typeddict-item]
        input_["challenge_arn"] = challenge_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
