from typing import TYPE_CHECKING, Optional

import aws_sdk_codecatalyst._auth._signers
import aws_sdk_codecatalyst._auth._sigv4
from aws_sdk_codecatalyst._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.access_token_id
    import aws_sdk_codecatalyst.types.access_token_name
    import aws_sdk_codecatalyst.types.access_token_summary
    import aws_sdk_codecatalyst.types.create_access_token_request
    import aws_sdk_codecatalyst.types.create_access_token_response
    import aws_sdk_codecatalyst.types.delete_access_token_request
    import aws_sdk_codecatalyst.types.delete_access_token_response
    import aws_sdk_codecatalyst.types.list_access_tokens_request
    import aws_sdk_codecatalyst.types.list_access_tokens_response
    import aws_sdk_codecatalyst.types.timestamp
    from aws_sdk_codecatalyst._services.async_code_catalyst import (
        AsyncCodeCatalystClient,
        AsyncCodeCatalystClientConfig,
    )
    from aws_sdk_codecatalyst._services.code_catalyst import (
        CodeCatalystClient,
        CodeCatalystClientConfig,
    )


class AccessToken:
    def __init__(self, service: CodeCatalystClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_codecatalyst.types.access_token_name.AccessTokenName",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        expires_time: Optional["aws_sdk_codecatalyst.types.timestamp.Timestamp"] = None,
    ) -> "aws_sdk_codecatalyst.types.create_access_token_response.CreateAccessTokenResponse":
        """<p>Creates a personal access token (PAT) for the current user. A personal access token (PAT) is similar to a password. It is associated with your user identity for use across all spaces and projects in Amazon CodeCatalyst. You use PATs to access CodeCatalyst from resources that include integrated development environments (IDEs) and Git-based source repositories. PATs represent you in Amazon CodeCatalyst and you can manage them in your user settings.For more information, see <a href=\"https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-tokens-keys.html\">Managing personal access tokens in Amazon CodeCatalyst</a>.</p>

        Args:
            name: <p>The friendly name of the personal access token.</p>
            expires_time: <p>The date and time the personal access token expires, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codecatalyst.types.create_access_token_request.CreateAccessTokenRequest]",
        ) -> OperationResponse[
            "aws_sdk_codecatalyst.types.create_access_token_response.CreateAccessTokenResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.create_access_token

            output, http_response = (
                aws_sdk_codecatalyst._operations.code_catalyst.create_access_token.create_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_codecatalyst.types.create_access_token_request.CreateAccessTokenRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if expires_time is not None:
            input["expires_time"] = expires_time

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        id: "aws_sdk_codecatalyst.types.access_token_id.AccessTokenId",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "aws_sdk_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse":
        """<p>Deletes a specified personal access token (PAT). A personal access token can only be deleted by the user who created it.</p>

        Args:
            id: <p>The ID of the personal access token to delete. You can find the IDs of all PATs associated with your Amazon Web Services Builder ID in a space by calling <a>ListAccessTokens</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codecatalyst.types.delete_access_token_request.DeleteAccessTokenRequest]",
        ) -> OperationResponse[
            "aws_sdk_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.delete_access_token

            output, http_response = (
                aws_sdk_codecatalyst._operations.code_catalyst.delete_access_token.delete_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_codecatalyst.types.delete_access_token_request.DeleteAccessTokenRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_codecatalyst.types.list_access_tokens_response.ListAccessTokensResponse":
        """<p>Lists all personal access tokens (PATs) associated with the user who calls the API. You can only list PATs associated with your Amazon Web Services Builder ID.</p>

        Args:
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_codecatalyst.types.list_access_tokens_request.ListAccessTokensRequest]",
        ) -> OperationResponse[
            "aws_sdk_codecatalyst.types.list_access_tokens_response.ListAccessTokensResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.list_access_tokens

            output, http_response = (
                aws_sdk_codecatalyst._operations.code_catalyst.list_access_tokens.list_access_tokens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_codecatalyst.types.list_access_tokens_request.ListAccessTokensRequest = {}  # type: ignore[typeddict-item]
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


class AsyncAccessToken:
    def __init__(self, service: AsyncCodeCatalystClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_codecatalyst.types.access_token_name.AccessTokenName",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
        expires_time: Optional["aws_sdk_codecatalyst.types.timestamp.Timestamp"] = None,
    ) -> "aws_sdk_codecatalyst.types.create_access_token_response.CreateAccessTokenResponse":
        """<p>Creates a personal access token (PAT) for the current user. A personal access token (PAT) is similar to a password. It is associated with your user identity for use across all spaces and projects in Amazon CodeCatalyst. You use PATs to access CodeCatalyst from resources that include integrated development environments (IDEs) and Git-based source repositories. PATs represent you in Amazon CodeCatalyst and you can manage them in your user settings.For more information, see <a href=\"https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-tokens-keys.html\">Managing personal access tokens in Amazon CodeCatalyst</a>.</p>

        Args:
            name: <p>The friendly name of the personal access token.</p>
            expires_time: <p>The date and time the personal access token expires, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecatalyst.types.create_access_token_request.CreateAccessTokenRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecatalyst.types.create_access_token_response.CreateAccessTokenResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.create_access_token

            (
                output,
                http_response,
            ) = await aws_sdk_codecatalyst._operations.code_catalyst.create_access_token.async_create_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_codecatalyst.types.create_access_token_request.CreateAccessTokenRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if expires_time is not None:
            input["expires_time"] = expires_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        id: "aws_sdk_codecatalyst.types.access_token_id.AccessTokenId",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
    ) -> "aws_sdk_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse":
        """<p>Deletes a specified personal access token (PAT). A personal access token can only be deleted by the user who created it.</p>

        Args:
            id: <p>The ID of the personal access token to delete. You can find the IDs of all PATs associated with your Amazon Web Services Builder ID in a space by calling <a>ListAccessTokens</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecatalyst.types.delete_access_token_request.DeleteAccessTokenRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.delete_access_token

            (
                output,
                http_response,
            ) = await aws_sdk_codecatalyst._operations.code_catalyst.delete_access_token.async_delete_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_codecatalyst.types.delete_access_token_request.DeleteAccessTokenRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_codecatalyst.types.list_access_tokens_response.ListAccessTokensResponse":
        """<p>Lists all personal access tokens (PATs) associated with the user who calls the API. You can only list PATs associated with your Amazon Web Services Builder ID.</p>

        Args:
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_codecatalyst.types.list_access_tokens_request.ListAccessTokensRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_codecatalyst.types.list_access_tokens_response.ListAccessTokensResponse"
        ]:
            import aws_sdk_codecatalyst._operations.code_catalyst.list_access_tokens

            (
                output,
                http_response,
            ) = await aws_sdk_codecatalyst._operations.code_catalyst.list_access_tokens.async_list_access_tokens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_codecatalyst.types.list_access_tokens_request.ListAccessTokensRequest = {}  # type: ignore[typeddict-item]
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
