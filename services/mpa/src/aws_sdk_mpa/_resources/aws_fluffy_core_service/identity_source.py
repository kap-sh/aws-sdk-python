from __future__ import annotations

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
    import aws_sdk_mpa.types.create_identity_source_request
    import aws_sdk_mpa.types.create_identity_source_response
    import aws_sdk_mpa.types.delete_identity_source_request
    import aws_sdk_mpa.types.get_identity_source_request
    import aws_sdk_mpa.types.get_identity_source_response
    import aws_sdk_mpa.types.identity_source_for_list
    import aws_sdk_mpa.types.identity_source_parameters
    import aws_sdk_mpa.types.list_identity_sources_request
    import aws_sdk_mpa.types.list_identity_sources_response
    import aws_sdk_mpa.types.max_results
    import aws_sdk_mpa.types.string
    import aws_sdk_mpa.types.tags
    import aws_sdk_mpa.types.token
    from aws_sdk_mpa._services.async_mpa import AsyncMPAClient, AsyncMPAClientConfig
    from aws_sdk_mpa._services.mpa import MPAClient, MPAClientConfig


class IdentitySource:
    def __init__(self, service: MPAClient) -> None:
        self._service = service

    def create(
        self,
        identity_source_parameters: "aws_sdk_mpa.types.identity_source_parameters.IdentitySourceParameters",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        client_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
        tags: Optional["aws_sdk_mpa.types.tags.Tags"] = None,
    ) -> (
        "aws_sdk_mpa.types.create_identity_source_response.CreateIdentitySourceResponse"
    ):
        r"""<p>Creates a new identity source. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            identity_source_parameters: <p>A <code> IdentitySourceParameters</code> object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services populates this field.</p> <note> <p> <b>What is idempotency?</b> </p> <p>When you make a mutating API request, the request typically returns a result before the operation's asynchronous workflows have completed. Operations might also time out or encounter other server issues before they complete, even though the request has already returned a result. This could make it difficult to determine whether the request succeeded or not, and could lead to multiple retries to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation is completed multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p> </note>
            tags: <p>Tag you want to attach to the identity source.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mpa.types.create_identity_source_request.CreateIdentitySourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mpa.types.create_identity_source_response.CreateIdentitySourceResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.create_identity_source

            output, http_response = (
                aws_sdk_mpa._operations.aws_fluffy_core_service.create_identity_source.create_identity_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.create_identity_source_request.CreateIdentitySourceRequest = {}  # type: ignore[typeddict-item]
        input_["identity_source_parameters"] = identity_source_parameters
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
        identity_source_arn: "aws_sdk_mpa.types.string.String",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> "aws_sdk_mpa.types.get_identity_source_response.GetIdentitySourceResponse":
        r"""<p>Returns details for an identity source. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            identity_source_arn: <p>Amazon Resource Name (ARN) for the identity source.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mpa.types.get_identity_source_request.GetIdentitySourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mpa.types.get_identity_source_response.GetIdentitySourceResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.get_identity_source

            output, http_response = (
                aws_sdk_mpa._operations.aws_fluffy_core_service.get_identity_source.get_identity_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.get_identity_source_request.GetIdentitySourceRequest = {}  # type: ignore[typeddict-item]
        input_["identity_source_arn"] = identity_source_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identity_source_arn: "aws_sdk_mpa.types.string.String",
        *,
        config_overrides: Optional[MPAClientConfig] = None,
    ) -> None:
        r"""<p>Deletes an identity source. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            identity_source_arn: <p>Amazon Resource Name (ARN) for identity source.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mpa.types.delete_identity_source_request.DeleteIdentitySourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.delete_identity_source

            output, http_response = (
                aws_sdk_mpa._operations.aws_fluffy_core_service.delete_identity_source.delete_identity_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.delete_identity_source_request.DeleteIdentitySourceRequest = {}  # type: ignore[typeddict-item]
        input_["identity_source_arn"] = identity_source_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MPAClientConfig] = None,
        max_results: Optional["aws_sdk_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
    ) -> "aws_sdk_mpa.types.list_identity_sources_response.ListIdentitySourcesResponse":
        r"""<p>Returns a list of identity sources. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mpa.types.list_identity_sources_request.ListIdentitySourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mpa.types.list_identity_sources_response.ListIdentitySourcesResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.list_identity_sources

            output, http_response = (
                aws_sdk_mpa._operations.aws_fluffy_core_service.list_identity_sources.list_identity_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.list_identity_sources_request.ListIdentitySourcesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncIdentitySource:
    def __init__(self, service: AsyncMPAClient) -> None:
        self._service = service

    async def create(
        self,
        identity_source_parameters: "aws_sdk_mpa.types.identity_source_parameters.IdentitySourceParameters",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        client_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
        tags: Optional["aws_sdk_mpa.types.tags.Tags"] = None,
    ) -> (
        "aws_sdk_mpa.types.create_identity_source_response.CreateIdentitySourceResponse"
    ):
        r"""<p>Creates a new identity source. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            identity_source_parameters: <p>A <code> IdentitySourceParameters</code> object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services populates this field.</p> <note> <p> <b>What is idempotency?</b> </p> <p>When you make a mutating API request, the request typically returns a result before the operation's asynchronous workflows have completed. Operations might also time out or encounter other server issues before they complete, even though the request has already returned a result. This could make it difficult to determine whether the request succeeded or not, and could lead to multiple retries to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation is completed multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p> </note>
            tags: <p>Tag you want to attach to the identity source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.create_identity_source_request.CreateIdentitySourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.create_identity_source_response.CreateIdentitySourceResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.create_identity_source

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.create_identity_source.async_create_identity_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.create_identity_source_request.CreateIdentitySourceRequest = {}  # type: ignore[typeddict-item]
        input_["identity_source_parameters"] = identity_source_parameters
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
        identity_source_arn: "aws_sdk_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> "aws_sdk_mpa.types.get_identity_source_response.GetIdentitySourceResponse":
        r"""<p>Returns details for an identity source. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            identity_source_arn: <p>Amazon Resource Name (ARN) for the identity source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.get_identity_source_request.GetIdentitySourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.get_identity_source_response.GetIdentitySourceResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.get_identity_source

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.get_identity_source.async_get_identity_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.get_identity_source_request.GetIdentitySourceRequest = {}  # type: ignore[typeddict-item]
        input_["identity_source_arn"] = identity_source_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identity_source_arn: "aws_sdk_mpa.types.string.String",
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
    ) -> None:
        r"""<p>Deletes an identity source. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            identity_source_arn: <p>Amazon Resource Name (ARN) for identity source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.delete_identity_source_request.DeleteIdentitySourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.delete_identity_source

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.delete_identity_source.async_delete_identity_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.delete_identity_source_request.DeleteIdentitySourceRequest = {}  # type: ignore[typeddict-item]
        input_["identity_source_arn"] = identity_source_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMPAClientConfig] = None,
        max_results: Optional["aws_sdk_mpa.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_mpa.types.token.Token"] = None,
    ) -> "aws_sdk_mpa.types.list_identity_sources_response.ListIdentitySourcesResponse":
        r"""<p>Returns a list of identity sources. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html\">Identity Source</a> in the <i>Multi-party approval User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>
            next_token: <p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mpa.types.list_identity_sources_request.ListIdentitySourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mpa.types.list_identity_sources_response.ListIdentitySourcesResponse"
        ]:
            import aws_sdk_mpa._operations.aws_fluffy_core_service.list_identity_sources

            (
                output,
                http_response,
            ) = await aws_sdk_mpa._operations.aws_fluffy_core_service.list_identity_sources.async_list_identity_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mpa.types.list_identity_sources_request.ListIdentitySourcesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
