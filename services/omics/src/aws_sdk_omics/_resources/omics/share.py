from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_omics._auth._signers
import aws_sdk_omics._auth._sigv4
from aws_sdk_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_omics.types.accept_share_request
    import aws_sdk_omics.types.accept_share_response
    import aws_sdk_omics.types.create_share_request
    import aws_sdk_omics.types.create_share_response
    import aws_sdk_omics.types.delete_share_request
    import aws_sdk_omics.types.delete_share_response
    import aws_sdk_omics.types.filter
    import aws_sdk_omics.types.get_share_request
    import aws_sdk_omics.types.get_share_response
    import aws_sdk_omics.types.list_shares_request
    import aws_sdk_omics.types.list_shares_response
    import aws_sdk_omics.types.resource_owner
    import aws_sdk_omics.types.share_details
    import aws_sdk_omics.types.share_name
    from aws_sdk_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from aws_sdk_omics._services.omics import OmicsClient, OmicsClientConfig


class Share:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        resource_arn: str,
        principal_subscriber: str,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        share_name: Optional["aws_sdk_omics.types.share_name.ShareName"] = None,
    ) -> "aws_sdk_omics.types.create_share_response.CreateShareResponse":
        """<p>Creates a cross-account shared resource. The resource owner makes an offer to share the resource with the principal subscriber (an AWS user with a different account than the resource owner).</p> <p>The following resources support cross-account sharing:</p> <ul> <li> <p>HealthOmics variant stores</p> </li> <li> <p>HealthOmics annotation stores</p> </li> <li> <p>Private workflows</p> </li> </ul>

        Args:
            resource_arn: <p>The ARN of the resource to be shared.</p>
            principal_subscriber: <p>The principal subscriber is the account being offered shared access to the resource. </p>
            share_name: <p>A name that the owner defines for the share.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.create_share_request.CreateShareRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.create_share_response.CreateShareResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_share

            output, http_response = (
                aws_sdk_omics._operations.omics.create_share.create_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.create_share_request.CreateShareRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["principal_subscriber"] = principal_subscriber
        if share_name is not None:
            input_["share_name"] = share_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self, share_id: str, *, config_overrides: Optional[OmicsClientConfig] = None
    ) -> "aws_sdk_omics.types.get_share_response.GetShareResponse":
        """<p>Retrieves the metadata for the specified resource share.</p>

        Args:
            share_id: <p>The ID of the share.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.get_share_request.GetShareRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.get_share_response.GetShareResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_share

            output, http_response = aws_sdk_omics._operations.omics.get_share.get_share(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_share_request.GetShareRequest = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self, share_id: str, *, config_overrides: Optional[OmicsClientConfig] = None
    ) -> "aws_sdk_omics.types.accept_share_response.AcceptShareResponse":
        """<p>Accept a resource share request.</p>

        Args:
            share_id: <p>The ID of the resource share.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.accept_share_request.AcceptShareRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.accept_share_response.AcceptShareResponse"
        ]:
            import aws_sdk_omics._operations.omics.accept_share

            output, http_response = (
                aws_sdk_omics._operations.omics.accept_share.accept_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.accept_share_request.AcceptShareRequest = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self, share_id: str, *, config_overrides: Optional[OmicsClientConfig] = None
    ) -> "aws_sdk_omics.types.delete_share_response.DeleteShareResponse":
        """<p>Deletes a resource share. If you are the resource owner, the subscriber will no longer have access to the shared resource. If you are the subscriber, this operation deletes your access to the share.</p>

        Args:
            share_id: <p>The ID for the resource share to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.delete_share_request.DeleteShareRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.delete_share_response.DeleteShareResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_share

            output, http_response = (
                aws_sdk_omics._operations.omics.delete_share.delete_share(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_share_request.DeleteShareRequest = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        resource_owner: "aws_sdk_omics.types.resource_owner.ResourceOwner",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        filter: Optional["aws_sdk_omics.types.filter.Filter"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_omics.types.list_shares_response.ListSharesResponse":
        """<p>Retrieves the resource shares associated with an account. Use the filter parameter to retrieve a specific subset of the shares.</p>

        Args:
            resource_owner: <p>The account that owns the resource shares.</p>
            filter: <p>Attributes that you use to filter for a specific subset of resource shares.</p>
            next_token: <p>Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.</p>
            max_results: <p>The maximum number of shares to return in one page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.list_shares_request.ListSharesRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.list_shares_response.ListSharesResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_shares

            output, http_response = (
                aws_sdk_omics._operations.omics.list_shares.list_shares(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_shares_request.ListSharesRequest = {}  # type: ignore[typeddict-item]
        input_["resource_owner"] = resource_owner
        if filter is not None:
            input_["filter"] = filter
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


class AsyncShare:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        resource_arn: str,
        principal_subscriber: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        share_name: Optional["aws_sdk_omics.types.share_name.ShareName"] = None,
    ) -> "aws_sdk_omics.types.create_share_response.CreateShareResponse":
        """<p>Creates a cross-account shared resource. The resource owner makes an offer to share the resource with the principal subscriber (an AWS user with a different account than the resource owner).</p> <p>The following resources support cross-account sharing:</p> <ul> <li> <p>HealthOmics variant stores</p> </li> <li> <p>HealthOmics annotation stores</p> </li> <li> <p>Private workflows</p> </li> </ul>

        Args:
            resource_arn: <p>The ARN of the resource to be shared.</p>
            principal_subscriber: <p>The principal subscriber is the account being offered shared access to the resource. </p>
            share_name: <p>A name that the owner defines for the share.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.create_share_request.CreateShareRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.create_share_response.CreateShareResponse"
        ]:
            import aws_sdk_omics._operations.omics.create_share

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.create_share.async_create_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.create_share_request.CreateShareRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["principal_subscriber"] = principal_subscriber
        if share_name is not None:
            input_["share_name"] = share_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        share_id: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.get_share_response.GetShareResponse":
        """<p>Retrieves the metadata for the specified resource share.</p>

        Args:
            share_id: <p>The ID of the share.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.get_share_request.GetShareRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.get_share_response.GetShareResponse"
        ]:
            import aws_sdk_omics._operations.omics.get_share

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.get_share.async_get_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.get_share_request.GetShareRequest = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        share_id: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.accept_share_response.AcceptShareResponse":
        """<p>Accept a resource share request.</p>

        Args:
            share_id: <p>The ID of the resource share.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.accept_share_request.AcceptShareRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.accept_share_response.AcceptShareResponse"
        ]:
            import aws_sdk_omics._operations.omics.accept_share

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.accept_share.async_accept_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.accept_share_request.AcceptShareRequest = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        share_id: str,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.delete_share_response.DeleteShareResponse":
        """<p>Deletes a resource share. If you are the resource owner, the subscriber will no longer have access to the shared resource. If you are the subscriber, this operation deletes your access to the share.</p>

        Args:
            share_id: <p>The ID for the resource share to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.delete_share_request.DeleteShareRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.delete_share_response.DeleteShareResponse"
        ]:
            import aws_sdk_omics._operations.omics.delete_share

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.delete_share.async_delete_share(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.delete_share_request.DeleteShareRequest = {}  # type: ignore[typeddict-item]
        input_["share_id"] = share_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        resource_owner: "aws_sdk_omics.types.resource_owner.ResourceOwner",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        filter: Optional["aws_sdk_omics.types.filter.Filter"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_omics.types.list_shares_response.ListSharesResponse":
        """<p>Retrieves the resource shares associated with an account. Use the filter parameter to retrieve a specific subset of the shares.</p>

        Args:
            resource_owner: <p>The account that owns the resource shares.</p>
            filter: <p>Attributes that you use to filter for a specific subset of resource shares.</p>
            next_token: <p>Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.</p>
            max_results: <p>The maximum number of shares to return in one page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.list_shares_request.ListSharesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.list_shares_response.ListSharesResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_shares

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.list_shares.async_list_shares(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_shares_request.ListSharesRequest = {}  # type: ignore[typeddict-item]
        input_["resource_owner"] = resource_owner
        if filter is not None:
            input_["filter"] = filter
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
