from typing import TYPE_CHECKING, Optional

import aws_sdk_mpa._auth._signers
import aws_sdk_mpa._auth._sigv4
from aws_sdk_mpa._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mpa.types.approval_team_arn
    import aws_sdk_mpa.types.cancel_session_request
    import aws_sdk_mpa.types.cancel_session_response
    import aws_sdk_mpa.types.filters
    import aws_sdk_mpa.types.get_session_request
    import aws_sdk_mpa.types.get_session_response
    import aws_sdk_mpa.types.list_sessions_request
    import aws_sdk_mpa.types.list_sessions_response
    import aws_sdk_mpa.types.list_sessions_response_session
    import aws_sdk_mpa.types.max_results
    import aws_sdk_mpa.types.session_arn
    import aws_sdk_mpa.types.token
    from aws_sdk_mpa._services.async_mpa import AsyncMPAClient, AsyncMPAClientConfig
    from aws_sdk_mpa._services.mpa import MPAClient, MPAClientConfig


class Session:
    def __init__(self, service: MPAClient) -> None:
        self._service = service

    def read(
        self,
        session_arn: "aws_sdk_mpa.types.session_arn.SessionArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "aws_sdk_mpa.types.get_session_response.GetSessionResponse":
        """<p>Returns details for an approval session. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            session_arn: <p>Amazon Resource Name (ARN) for the session.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mpa.types.get_session_request.GetSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mpa.types.get_session_response.GetSessionResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.get_session

            output, http_response = (
                aws_sdk_mpa._operations.aws_fluffy_core_service.get_session.get_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mpa.types.get_session_request.GetSessionRequest = {}  # type: ignore[typeddict-item]
        input["session_arn"] = session_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        session_arn: "aws_sdk_mpa.types.session_arn.SessionArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "aws_sdk_mpa.types.cancel_session_response.CancelSessionResponse":
        """<p>Cancels an approval session. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            session_arn: <p>Amazon Resource Name (ARN) for the session.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mpa.types.cancel_session_request.CancelSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_mpa.types.cancel_session_response.CancelSessionResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.cancel_session

            output, http_response = (
                aws_sdk_mpa._operations.aws_fluffy_core_service.cancel_session.cancel_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mpa.types.cancel_session_request.CancelSessionRequest = {}  # type: ignore[typeddict-item]
        input["session_arn"] = session_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        approval_team_arn: "aws_sdk_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        max_results: Optional["aws_sdk_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
        filters: Optional["aws_sdk_mpa.types.filters.Filters"] = None,
    ) -> "aws_sdk_mpa.types.list_sessions_response.ListSessionsResponse":
        """<p>Returns a list of approval sessions. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            approval_team_arn: <p>Amazon Resource Name (ARN) for the approval team.</p>
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>
            filters: <p>An array of <code>Filter</code> objects. Contains the filter to apply when listing sessions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mpa.types.list_sessions_request.ListSessionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mpa.types.list_sessions_response.ListSessionsResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.list_sessions

            output, http_response = (
                aws_sdk_mpa._operations.aws_fluffy_core_service.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mpa.types.list_sessions_request.ListSessionsRequest = {}  # type: ignore[typeddict-item]
        input["approval_team_arn"] = approval_team_arn
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncSession:
    def __init__(self, service: AsyncMPAClient) -> None:
        self._service = service

    async def read(
        self,
        session_arn: "aws_sdk_mpa.types.session_arn.SessionArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "aws_sdk_mpa.types.get_session_response.GetSessionResponse":
        """<p>Returns details for an approval session. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            session_arn: <p>Amazon Resource Name (ARN) for the session.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.get_session_response.GetSessionResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.get_session

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mpa.types.get_session_request.GetSessionRequest = {}  # type: ignore[typeddict-item]
        input["session_arn"] = session_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        session_arn: "aws_sdk_mpa.types.session_arn.SessionArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "aws_sdk_mpa.types.cancel_session_response.CancelSessionResponse":
        """<p>Cancels an approval session. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            session_arn: <p>Amazon Resource Name (ARN) for the session.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.cancel_session_request.CancelSessionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.cancel_session_response.CancelSessionResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.cancel_session

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.cancel_session.async_cancel_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mpa.types.cancel_session_request.CancelSessionRequest = {}  # type: ignore[typeddict-item]
        input["session_arn"] = session_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        approval_team_arn: "aws_sdk_mpa.types.approval_team_arn.ApprovalTeamArn",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["aws_sdk_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
        filters: Optional["aws_sdk_mpa.types.filters.Filters"] = None,
    ) -> "aws_sdk_mpa.types.list_sessions_response.ListSessionsResponse":
        """<p>Returns a list of approval sessions. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Session</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            approval_team_arn: <p>Amazon Resource Name (ARN) for the approval team.</p>
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>
            filters: <p>An array of <code>Filter</code> objects. Contains the filter to apply when listing sessions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.list_sessions_request.ListSessionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.list_sessions_response.ListSessionsResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.list_sessions

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mpa.types.list_sessions_request.ListSessionsRequest = {}  # type: ignore[typeddict-item]
        input["approval_team_arn"] = approval_team_arn
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
