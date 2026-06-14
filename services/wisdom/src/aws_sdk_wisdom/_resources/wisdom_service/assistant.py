from typing import TYPE_CHECKING, Optional

import aws_sdk_wisdom._auth._signers
import aws_sdk_wisdom._auth._sigv4
from aws_sdk_wisdom._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.assistant_summary
    import aws_sdk_wisdom.types.assistant_type
    import aws_sdk_wisdom.types.client_token
    import aws_sdk_wisdom.types.create_assistant_request
    import aws_sdk_wisdom.types.create_assistant_response
    import aws_sdk_wisdom.types.delete_assistant_request
    import aws_sdk_wisdom.types.delete_assistant_response
    import aws_sdk_wisdom.types.description
    import aws_sdk_wisdom.types.get_assistant_request
    import aws_sdk_wisdom.types.get_assistant_response
    import aws_sdk_wisdom.types.get_recommendations_request
    import aws_sdk_wisdom.types.get_recommendations_response
    import aws_sdk_wisdom.types.list_assistants_request
    import aws_sdk_wisdom.types.list_assistants_response
    import aws_sdk_wisdom.types.max_results
    import aws_sdk_wisdom.types.name
    import aws_sdk_wisdom.types.next_token
    import aws_sdk_wisdom.types.notify_recommendations_received_request
    import aws_sdk_wisdom.types.notify_recommendations_received_response
    import aws_sdk_wisdom.types.query_assistant_request
    import aws_sdk_wisdom.types.query_assistant_response
    import aws_sdk_wisdom.types.query_text
    import aws_sdk_wisdom.types.recommendation_id_list
    import aws_sdk_wisdom.types.result_data
    import aws_sdk_wisdom.types.search_expression
    import aws_sdk_wisdom.types.search_sessions_request
    import aws_sdk_wisdom.types.search_sessions_response
    import aws_sdk_wisdom.types.server_side_encryption_configuration
    import aws_sdk_wisdom.types.session_summary
    import aws_sdk_wisdom.types.tags
    import aws_sdk_wisdom.types.uuid_or_arn
    import aws_sdk_wisdom.types.wait_time_seconds
    from aws_sdk_wisdom._services.async_wisdom import (
        AsyncWisdomClient,
        AsyncWisdomClientConfig,
    )
    from aws_sdk_wisdom._services.wisdom import WisdomClient, WisdomClientConfig


class Assistant:
    def __init__(self, service: WisdomClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_wisdom.types.name.Name",
        type: "aws_sdk_wisdom.types.assistant_type.AssistantType",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
        client_token: Optional["aws_sdk_wisdom.types.client_token.ClientToken"] = None,
        description: Optional["aws_sdk_wisdom.types.description.Description"] = None,
        tags: Optional["aws_sdk_wisdom.types.tags.Tags"] = None,
        server_side_encryption_configuration: Optional[
            "aws_sdk_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
    ) -> "aws_sdk_wisdom.types.create_assistant_response.CreateAssistantResponse":
        r"""<p>Creates an Amazon Connect Wisdom assistant.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the assistant.</p>
            type: <p>The type of assistant.</p>
            description: <p>The description of the assistant.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>The customer managed key must have a policy that allows <code>kms:CreateGrant</code>, <code> kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Wisdom, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html\">Enable Amazon Connect Wisdom for your instance</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_wisdom.types.create_assistant_request.CreateAssistantRequest]",
        ) -> OperationResponse[
            "aws_sdk_wisdom.types.create_assistant_response.CreateAssistantResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.create_assistant

            output, http_response = (
                aws_sdk_wisdom._operations.wisdom_service.create_assistant.create_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.create_assistant_request.CreateAssistantRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        input_["type"] = type
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
    ) -> "aws_sdk_wisdom.types.get_assistant_response.GetAssistantResponse":
        """<p>Retrieves information about an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_wisdom.types.get_assistant_request.GetAssistantRequest]",
        ) -> OperationResponse[
            "aws_sdk_wisdom.types.get_assistant_response.GetAssistantResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.get_assistant

            output, http_response = (
                aws_sdk_wisdom._operations.wisdom_service.get_assistant.get_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.get_assistant_request.GetAssistantRequest = {}  # type: ignore[typeddict-item]
        input_["assistant_id"] = assistant_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
    ) -> "aws_sdk_wisdom.types.delete_assistant_response.DeleteAssistantResponse":
        """<p>Deletes an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_wisdom.types.delete_assistant_request.DeleteAssistantRequest]",
        ) -> OperationResponse[
            "aws_sdk_wisdom.types.delete_assistant_response.DeleteAssistantResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.delete_assistant

            output, http_response = (
                aws_sdk_wisdom._operations.wisdom_service.delete_assistant.delete_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.delete_assistant_request.DeleteAssistantRequest = {}  # type: ignore[typeddict-item]
        input_["assistant_id"] = assistant_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
        next_token: Optional["aws_sdk_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_wisdom.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_wisdom.types.list_assistants_response.ListAssistantsResponse":
        """<p>Lists information about assistants.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_wisdom.types.list_assistants_request.ListAssistantsRequest]",
        ) -> OperationResponse[
            "aws_sdk_wisdom.types.list_assistants_response.ListAssistantsResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.list_assistants

            output, http_response = (
                aws_sdk_wisdom._operations.wisdom_service.list_assistants.list_assistants(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.list_assistants_request.ListAssistantsRequest = {}  # type: ignore[typeddict-item]
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

    def get_recommendations(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        session_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
        max_results: Optional["aws_sdk_wisdom.types.max_results.MaxResults"] = None,
        wait_time_seconds: Optional[
            "aws_sdk_wisdom.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> "aws_sdk_wisdom.types.get_recommendations_response.GetRecommendationsResponse":
        r"""<p>Retrieves recommendations for the specified session. To avoid retrieving the same recommendations in subsequent calls, use <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_NotifyRecommendationsReceived.html\">NotifyRecommendationsReceived</a>. This API supports long-polling behavior with the <code>waitTimeSeconds</code> parameter. Short poll is the default behavior and only returns recommendations already available. To perform a manual query against an assistant, use <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_QueryAssistant.html\">QueryAssistant</a>.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            wait_time_seconds: <p>The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call returns successfully with an empty list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_wisdom.types.get_recommendations_request.GetRecommendationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_wisdom.types.get_recommendations_response.GetRecommendationsResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.get_recommendations

            output, http_response = (
                aws_sdk_wisdom._operations.wisdom_service.get_recommendations.get_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.get_recommendations_request.GetRecommendationsRequest = {}  # type: ignore[typeddict-item]
        input_["assistant_id"] = assistant_id
        input_["session_id"] = session_id
        if max_results is not None:
            input_["max_results"] = max_results
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def notify_recommendations_received(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        session_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        recommendation_ids: "aws_sdk_wisdom.types.recommendation_id_list.RecommendationIdList",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
    ) -> "aws_sdk_wisdom.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse":
        r"""<p>Removes the specified recommendations from the specified assistant's queue of newly available recommendations. You can use this API in conjunction with <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html\">GetRecommendations</a> and a <code>waitTimeSeconds</code> input for long-polling behavior and avoiding duplicate recommendations.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            recommendation_ids: <p>The identifiers of the recommendations.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_wisdom.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest]",
        ) -> OperationResponse[
            "aws_sdk_wisdom.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.notify_recommendations_received

            output, http_response = (
                aws_sdk_wisdom._operations.wisdom_service.notify_recommendations_received.notify_recommendations_received(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest = {}  # type: ignore[typeddict-item]
        input_["assistant_id"] = assistant_id
        input_["session_id"] = session_id
        input_["recommendation_ids"] = recommendation_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def query_assistant(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        query_text: "aws_sdk_wisdom.types.query_text.QueryText",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
        next_token: Optional["aws_sdk_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_wisdom.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_wisdom.types.query_assistant_response.QueryAssistantResponse":
        r"""<p>Performs a manual search against the specified assistant. To retrieve recommendations for an assistant, use <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html\">GetRecommendations</a>. </p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            query_text: <p>The text to search for.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_wisdom.types.query_assistant_request.QueryAssistantRequest]",
        ) -> OperationResponse[
            "aws_sdk_wisdom.types.query_assistant_response.QueryAssistantResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.query_assistant

            output, http_response = (
                aws_sdk_wisdom._operations.wisdom_service.query_assistant.query_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.query_assistant_request.QueryAssistantRequest = {}  # type: ignore[typeddict-item]
        input_["assistant_id"] = assistant_id
        input_["query_text"] = query_text
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

    def search_sessions(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        search_expression: "aws_sdk_wisdom.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
        next_token: Optional["aws_sdk_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_wisdom.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_wisdom.types.search_sessions_response.SearchSessionsResponse":
        """<p>Searches for sessions.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_wisdom.types.search_sessions_request.SearchSessionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_wisdom.types.search_sessions_response.SearchSessionsResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.search_sessions

            output, http_response = (
                aws_sdk_wisdom._operations.wisdom_service.search_sessions.search_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.search_sessions_request.SearchSessionsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["assistant_id"] = assistant_id
        input_["search_expression"] = search_expression

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAssistant:
    def __init__(self, service: AsyncWisdomClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_wisdom.types.name.Name",
        type: "aws_sdk_wisdom.types.assistant_type.AssistantType",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        client_token: Optional["aws_sdk_wisdom.types.client_token.ClientToken"] = None,
        description: Optional["aws_sdk_wisdom.types.description.Description"] = None,
        tags: Optional["aws_sdk_wisdom.types.tags.Tags"] = None,
        server_side_encryption_configuration: Optional[
            "aws_sdk_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
    ) -> "aws_sdk_wisdom.types.create_assistant_response.CreateAssistantResponse":
        r"""<p>Creates an Amazon Connect Wisdom assistant.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the assistant.</p>
            type: <p>The type of assistant.</p>
            description: <p>The description of the assistant.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>The customer managed key must have a policy that allows <code>kms:CreateGrant</code>, <code> kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Wisdom, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html\">Enable Amazon Connect Wisdom for your instance</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wisdom.types.create_assistant_request.CreateAssistantRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wisdom.types.create_assistant_response.CreateAssistantResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.create_assistant

            (
                output,
                http_response,
            ) = await aws_sdk_wisdom._operations.wisdom_service.create_assistant.async_create_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.create_assistant_request.CreateAssistantRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        input_["type"] = type
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "aws_sdk_wisdom.types.get_assistant_response.GetAssistantResponse":
        """<p>Retrieves information about an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wisdom.types.get_assistant_request.GetAssistantRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wisdom.types.get_assistant_response.GetAssistantResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.get_assistant

            (
                output,
                http_response,
            ) = await aws_sdk_wisdom._operations.wisdom_service.get_assistant.async_get_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.get_assistant_request.GetAssistantRequest = {}  # type: ignore[typeddict-item]
        input_["assistant_id"] = assistant_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "aws_sdk_wisdom.types.delete_assistant_response.DeleteAssistantResponse":
        """<p>Deletes an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wisdom.types.delete_assistant_request.DeleteAssistantRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wisdom.types.delete_assistant_response.DeleteAssistantResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.delete_assistant

            (
                output,
                http_response,
            ) = await aws_sdk_wisdom._operations.wisdom_service.delete_assistant.async_delete_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.delete_assistant_request.DeleteAssistantRequest = {}  # type: ignore[typeddict-item]
        input_["assistant_id"] = assistant_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["aws_sdk_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_wisdom.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_wisdom.types.list_assistants_response.ListAssistantsResponse":
        """<p>Lists information about assistants.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wisdom.types.list_assistants_request.ListAssistantsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wisdom.types.list_assistants_response.ListAssistantsResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.list_assistants

            (
                output,
                http_response,
            ) = await aws_sdk_wisdom._operations.wisdom_service.list_assistants.async_list_assistants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.list_assistants_request.ListAssistantsRequest = {}  # type: ignore[typeddict-item]
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

    async def get_recommendations(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        session_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        max_results: Optional["aws_sdk_wisdom.types.max_results.MaxResults"] = None,
        wait_time_seconds: Optional[
            "aws_sdk_wisdom.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> "aws_sdk_wisdom.types.get_recommendations_response.GetRecommendationsResponse":
        r"""<p>Retrieves recommendations for the specified session. To avoid retrieving the same recommendations in subsequent calls, use <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_NotifyRecommendationsReceived.html\">NotifyRecommendationsReceived</a>. This API supports long-polling behavior with the <code>waitTimeSeconds</code> parameter. Short poll is the default behavior and only returns recommendations already available. To perform a manual query against an assistant, use <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_QueryAssistant.html\">QueryAssistant</a>.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            wait_time_seconds: <p>The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call returns successfully with an empty list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wisdom.types.get_recommendations_request.GetRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wisdom.types.get_recommendations_response.GetRecommendationsResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.get_recommendations

            (
                output,
                http_response,
            ) = await aws_sdk_wisdom._operations.wisdom_service.get_recommendations.async_get_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.get_recommendations_request.GetRecommendationsRequest = {}  # type: ignore[typeddict-item]
        input_["assistant_id"] = assistant_id
        input_["session_id"] = session_id
        if max_results is not None:
            input_["max_results"] = max_results
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def notify_recommendations_received(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        session_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        recommendation_ids: "aws_sdk_wisdom.types.recommendation_id_list.RecommendationIdList",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "aws_sdk_wisdom.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse":
        r"""<p>Removes the specified recommendations from the specified assistant's queue of newly available recommendations. You can use this API in conjunction with <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html\">GetRecommendations</a> and a <code>waitTimeSeconds</code> input for long-polling behavior and avoiding duplicate recommendations.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            recommendation_ids: <p>The identifiers of the recommendations.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wisdom.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wisdom.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.notify_recommendations_received

            (
                output,
                http_response,
            ) = await aws_sdk_wisdom._operations.wisdom_service.notify_recommendations_received.async_notify_recommendations_received(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest = {}  # type: ignore[typeddict-item]
        input_["assistant_id"] = assistant_id
        input_["session_id"] = session_id
        input_["recommendation_ids"] = recommendation_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def query_assistant(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        query_text: "aws_sdk_wisdom.types.query_text.QueryText",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["aws_sdk_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_wisdom.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_wisdom.types.query_assistant_response.QueryAssistantResponse":
        r"""<p>Performs a manual search against the specified assistant. To retrieve recommendations for an assistant, use <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html\">GetRecommendations</a>. </p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            query_text: <p>The text to search for.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wisdom.types.query_assistant_request.QueryAssistantRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wisdom.types.query_assistant_response.QueryAssistantResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.query_assistant

            (
                output,
                http_response,
            ) = await aws_sdk_wisdom._operations.wisdom_service.query_assistant.async_query_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.query_assistant_request.QueryAssistantRequest = {}  # type: ignore[typeddict-item]
        input_["assistant_id"] = assistant_id
        input_["query_text"] = query_text
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

    async def search_sessions(
        self,
        assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn",
        search_expression: "aws_sdk_wisdom.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["aws_sdk_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_wisdom.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_wisdom.types.search_sessions_response.SearchSessionsResponse":
        """<p>Searches for sessions.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_wisdom.types.search_sessions_request.SearchSessionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_wisdom.types.search_sessions_response.SearchSessionsResponse"
        ]:
            import aws_sdk_wisdom._operations.wisdom_service.search_sessions

            (
                output,
                http_response,
            ) = await aws_sdk_wisdom._operations.wisdom_service.search_sessions.async_search_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_wisdom.types.search_sessions_request.SearchSessionsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["assistant_id"] = assistant_id
        input_["search_expression"] = search_expression

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
