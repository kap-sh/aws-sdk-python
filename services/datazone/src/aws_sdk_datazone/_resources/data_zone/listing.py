from typing import Optional, TYPE_CHECKING
from aws_sdk_datazone._services.async_data_zone import ensure_async_iterator
from aws_sdk_datazone._services.data_zone import ensure_sync_iterator
import datetime
from aws_sdk_datazone._services._pipeline import (
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
)
import aws_sdk_datazone._auth._signers
import aws_sdk_datazone._auth._sigv4

if TYPE_CHECKING:
    from aws_sdk_datazone._services.data_zone import (
        DataZoneClient,
        DataZoneClientConfig,
    )
    from aws_sdk_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    import aws_sdk_datazone.types.delete_listing_input
    import aws_sdk_datazone.types.delete_listing_output
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.get_listing_input
    import aws_sdk_datazone.types.get_listing_output
    import aws_sdk_datazone.types.listing_id
    import aws_sdk_datazone.types.revision


class Listing:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.listing_id.ListingId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        listing_revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
    ) -> "aws_sdk_datazone.types.get_listing_output.GetListingOutput":
        """<p>Gets a listing (a record of an asset at a given time). If you specify a listing version, only details that are specific to that version are returned.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            identifier: <p>The ID of the listing.</p>
            listing_revision: <p>The revision of the listing.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.get_listing_input.GetListingInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.get_listing_output.GetListingOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_listing

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.get_listing.get_listing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_listing_input.GetListingInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if listing_revision is not None:
            input_["listing_revision"] = listing_revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.listing_id.ListingId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_listing_output.DeleteListingOutput":
        """<p>Deletes a listing (a record of an asset at a given time).</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            identifier: <p>The ID of the listing to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_datazone.types.delete_listing_input.DeleteListingInput]",
        ) -> OperationResponse[
            "aws_sdk_datazone.types.delete_listing_output.DeleteListingOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_listing

            output, http_response = (
                aws_sdk_datazone._operations.data_zone.delete_listing.delete_listing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_listing_input.DeleteListingInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncListing:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def read(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.listing_id.ListingId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        listing_revision: Optional["aws_sdk_datazone.types.revision.Revision"] = None,
    ) -> "aws_sdk_datazone.types.get_listing_output.GetListingOutput":
        """<p>Gets a listing (a record of an asset at a given time). If you specify a listing version, only details that are specific to that version are returned.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            identifier: <p>The ID of the listing.</p>
            listing_revision: <p>The revision of the listing.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.get_listing_input.GetListingInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.get_listing_output.GetListingOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.get_listing

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.get_listing.async_get_listing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.get_listing_input.GetListingInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier
        if listing_revision is not None:
            input_["listing_revision"] = listing_revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId",
        identifier: "aws_sdk_datazone.types.listing_id.ListingId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "aws_sdk_datazone.types.delete_listing_output.DeleteListingOutput":
        """<p>Deletes a listing (a record of an asset at a given time).</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            identifier: <p>The ID of the listing to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_datazone.types.delete_listing_input.DeleteListingInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_datazone.types.delete_listing_output.DeleteListingOutput"
        ]:
            import aws_sdk_datazone._operations.data_zone.delete_listing

            (
                output,
                http_response,
            ) = await aws_sdk_datazone._operations.data_zone.delete_listing.async_delete_listing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_datazone.types.delete_listing_input.DeleteListingInput = {}  # type: ignore[typeddict-item]
        input_["domain_identifier"] = domain_identifier
        input_["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
