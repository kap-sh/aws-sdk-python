"""Generated from Smithy shape ``com.amazonaws.dataexchange#DataExchange``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_dataexchange._auth._signers
import aws_sdk_dataexchange._auth._sigv4
from aws_sdk_dataexchange._auth._identity import Credentials
from aws_sdk_dataexchange._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_dataexchange._auth._zapros_handler import AuthMiddleware
from aws_sdk_dataexchange._pagination import resolve_path as _resolve_path
from aws_sdk_dataexchange._services._aws_config import aws_config
from aws_sdk_dataexchange._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__boolean
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.__string_min0_max4096
    import aws_sdk_dataexchange.types.__string_min0_max16384
    import aws_sdk_dataexchange.types.__string_min10_max512
    import aws_sdk_dataexchange.types.accept_data_grant_request
    import aws_sdk_dataexchange.types.accept_data_grant_response
    import aws_sdk_dataexchange.types.acceptance_state_filter_values
    import aws_sdk_dataexchange.types.action
    import aws_sdk_dataexchange.types.asset_configuration
    import aws_sdk_dataexchange.types.asset_entry
    import aws_sdk_dataexchange.types.asset_name
    import aws_sdk_dataexchange.types.asset_type
    import aws_sdk_dataexchange.types.cancel_job_request
    import aws_sdk_dataexchange.types.client_token
    import aws_sdk_dataexchange.types.create_data_grant_request
    import aws_sdk_dataexchange.types.create_data_grant_response
    import aws_sdk_dataexchange.types.create_data_set_request
    import aws_sdk_dataexchange.types.create_data_set_response
    import aws_sdk_dataexchange.types.create_event_action_request
    import aws_sdk_dataexchange.types.create_event_action_response
    import aws_sdk_dataexchange.types.create_job_request
    import aws_sdk_dataexchange.types.create_job_response
    import aws_sdk_dataexchange.types.create_revision_request
    import aws_sdk_dataexchange.types.create_revision_response
    import aws_sdk_dataexchange.types.data_grant_arn
    import aws_sdk_dataexchange.types.data_grant_id
    import aws_sdk_dataexchange.types.data_grant_name
    import aws_sdk_dataexchange.types.data_grant_summary_entry
    import aws_sdk_dataexchange.types.data_set_entry
    import aws_sdk_dataexchange.types.delete_asset_request
    import aws_sdk_dataexchange.types.delete_data_grant_request
    import aws_sdk_dataexchange.types.delete_data_set_request
    import aws_sdk_dataexchange.types.delete_event_action_request
    import aws_sdk_dataexchange.types.delete_revision_request
    import aws_sdk_dataexchange.types.description
    import aws_sdk_dataexchange.types.event
    import aws_sdk_dataexchange.types.event_action_entry
    import aws_sdk_dataexchange.types.get_asset_request
    import aws_sdk_dataexchange.types.get_asset_response
    import aws_sdk_dataexchange.types.get_data_grant_request
    import aws_sdk_dataexchange.types.get_data_grant_response
    import aws_sdk_dataexchange.types.get_data_set_request
    import aws_sdk_dataexchange.types.get_data_set_response
    import aws_sdk_dataexchange.types.get_event_action_request
    import aws_sdk_dataexchange.types.get_event_action_response
    import aws_sdk_dataexchange.types.get_job_request
    import aws_sdk_dataexchange.types.get_job_response
    import aws_sdk_dataexchange.types.get_received_data_grant_request
    import aws_sdk_dataexchange.types.get_received_data_grant_response
    import aws_sdk_dataexchange.types.get_revision_request
    import aws_sdk_dataexchange.types.get_revision_response
    import aws_sdk_dataexchange.types.grant_distribution_scope
    import aws_sdk_dataexchange.types.id
    import aws_sdk_dataexchange.types.job_entry
    import aws_sdk_dataexchange.types.list_data_grants_request
    import aws_sdk_dataexchange.types.list_data_grants_response
    import aws_sdk_dataexchange.types.list_data_set_revisions_request
    import aws_sdk_dataexchange.types.list_data_set_revisions_response
    import aws_sdk_dataexchange.types.list_data_sets_request
    import aws_sdk_dataexchange.types.list_data_sets_response
    import aws_sdk_dataexchange.types.list_event_actions_request
    import aws_sdk_dataexchange.types.list_event_actions_response
    import aws_sdk_dataexchange.types.list_jobs_request
    import aws_sdk_dataexchange.types.list_jobs_response
    import aws_sdk_dataexchange.types.list_of__string
    import aws_sdk_dataexchange.types.list_received_data_grants_request
    import aws_sdk_dataexchange.types.list_received_data_grants_response
    import aws_sdk_dataexchange.types.list_revision_assets_request
    import aws_sdk_dataexchange.types.list_revision_assets_response
    import aws_sdk_dataexchange.types.list_tags_for_resource_request
    import aws_sdk_dataexchange.types.list_tags_for_resource_response
    import aws_sdk_dataexchange.types.map_of__string
    import aws_sdk_dataexchange.types.max_results
    import aws_sdk_dataexchange.types.name
    import aws_sdk_dataexchange.types.notification_details
    import aws_sdk_dataexchange.types.notification_type
    import aws_sdk_dataexchange.types.received_data_grant_summaries_entry
    import aws_sdk_dataexchange.types.receiver_principal
    import aws_sdk_dataexchange.types.request_details
    import aws_sdk_dataexchange.types.revision_entry
    import aws_sdk_dataexchange.types.revoke_revision_request
    import aws_sdk_dataexchange.types.revoke_revision_response
    import aws_sdk_dataexchange.types.scope_details
    import aws_sdk_dataexchange.types.send_api_asset_request
    import aws_sdk_dataexchange.types.send_api_asset_response
    import aws_sdk_dataexchange.types.send_data_set_notification_request
    import aws_sdk_dataexchange.types.send_data_set_notification_response
    import aws_sdk_dataexchange.types.start_job_request
    import aws_sdk_dataexchange.types.start_job_response
    import aws_sdk_dataexchange.types.tag_resource_request
    import aws_sdk_dataexchange.types.timestamp
    import aws_sdk_dataexchange.types.type
    import aws_sdk_dataexchange.types.untag_resource_request
    import aws_sdk_dataexchange.types.update_asset_request
    import aws_sdk_dataexchange.types.update_asset_response
    import aws_sdk_dataexchange.types.update_data_set_request
    import aws_sdk_dataexchange.types.update_data_set_response
    import aws_sdk_dataexchange.types.update_event_action_request
    import aws_sdk_dataexchange.types.update_event_action_response
    import aws_sdk_dataexchange.types.update_revision_request
    import aws_sdk_dataexchange.types.update_revision_response


class DataExchangeClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class DataExchangeClient:
    """A client for the ``DataExchange`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = DataExchangeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[DataExchangeClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DataExchangeClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def accept_data_grant(
        self,
        data_grant_arn: "aws_sdk_dataexchange.types.data_grant_arn.DataGrantArn",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> (
        "aws_sdk_dataexchange.types.accept_data_grant_response.AcceptDataGrantResponse"
    ):
        """<p>This operation accepts a data grant.</p>

        Args:
            data_grant_arn: <p>The Amazon Resource Name (ARN) of the data grant to accept.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.accept_data_grant_request.AcceptDataGrantRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.accept_data_grant_response.AcceptDataGrantResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.accept_data_grant

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.accept_data_grant.accept_data_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.accept_data_grant_request.AcceptDataGrantRequest = {}  # type: ignore[typeddict-item]
        input_["data_grant_arn"] = data_grant_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_job(
        self,
        job_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation cancels a job. Jobs can be cancelled only when they are in the WAITING state.</p>

        Args:
            job_id: <p>The unique identifier for a job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.cancel_job_request.CancelJobRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_dataexchange._operations.data_exchange.cancel_job

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.cancel_job.cancel_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.cancel_job_request.CancelJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_data_grant(
        self,
        name: "aws_sdk_dataexchange.types.data_grant_name.DataGrantName",
        grant_distribution_scope: "aws_sdk_dataexchange.types.grant_distribution_scope.GrantDistributionScope",
        receiver_principal: "aws_sdk_dataexchange.types.receiver_principal.ReceiverPrincipal",
        source_data_set_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        ends_at: Optional["aws_sdk_dataexchange.types.timestamp.Timestamp"] = None,
        description: Optional[
            "aws_sdk_dataexchange.types.description.Description"
        ] = None,
        tags: Optional[
            "aws_sdk_dataexchange.types.map_of__string.MapOf__string"
        ] = None,
    ) -> (
        "aws_sdk_dataexchange.types.create_data_grant_response.CreateDataGrantResponse"
    ):
        """<p>This operation creates a data grant.</p>

        Args:
            name: <p>The name of the data grant.</p>
            grant_distribution_scope: <p>The distribution scope of the data grant.</p>
            receiver_principal: <p>The Amazon Web Services account ID of the data grant receiver.</p>
            source_data_set_id: <p>The ID of the data set used to create the data grant.</p>
            ends_at: <p>The timestamp of when access to the associated data set ends.</p>
            description: <p>The description of the data grant.</p>
            tags: <p>The tags to add to the data grant. A tag is a key-value pair.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.create_data_grant_request.CreateDataGrantRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.create_data_grant_response.CreateDataGrantResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.create_data_grant

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.create_data_grant.create_data_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.create_data_grant_request.CreateDataGrantRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["grant_distribution_scope"] = grant_distribution_scope
        input_["receiver_principal"] = receiver_principal
        input_["source_data_set_id"] = source_data_set_id
        if ends_at is not None:
            input_["ends_at"] = ends_at
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_data_set(
        self,
        asset_type: "aws_sdk_dataexchange.types.asset_type.AssetType",
        description: "aws_sdk_dataexchange.types.description.Description",
        name: "aws_sdk_dataexchange.types.name.Name",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        tags: Optional[
            "aws_sdk_dataexchange.types.map_of__string.MapOf__string"
        ] = None,
    ) -> "aws_sdk_dataexchange.types.create_data_set_response.CreateDataSetResponse":
        """<p>This operation creates a data set.</p>

        Args:
            asset_type: <p>The type of asset that is added to a data set.</p>
            description: <p>A description for the data set. This value can be up to 16,348 characters long.</p>
            name: <p>The name of the data set.</p>
            tags: <p>A data set tag is an optional label that you can assign to a data set when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.create_data_set_request.CreateDataSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.create_data_set_response.CreateDataSetResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.create_data_set

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.create_data_set.create_data_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.create_data_set_request.CreateDataSetRequest = {}  # type: ignore[typeddict-item]
        input_["asset_type"] = asset_type
        input_["description"] = description
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_event_action(
        self,
        action: "aws_sdk_dataexchange.types.action.Action",
        event: "aws_sdk_dataexchange.types.event.Event",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        tags: Optional[
            "aws_sdk_dataexchange.types.map_of__string.MapOf__string"
        ] = None,
    ) -> "aws_sdk_dataexchange.types.create_event_action_response.CreateEventActionResponse":
        """<p>This operation creates an event action.</p>

        Args:
            action: <p>What occurs after a certain event.</p>
            event: <p>What occurs to start an action.</p>
            tags: <p>Key-value pairs that you can associate with the event action.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.create_event_action_request.CreateEventActionRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.create_event_action_response.CreateEventActionResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.create_event_action

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.create_event_action.create_event_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.create_event_action_request.CreateEventActionRequest = {}  # type: ignore[typeddict-item]
        input_["action"] = action
        input_["event"] = event
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_job(
        self,
        details: "aws_sdk_dataexchange.types.request_details.RequestDetails",
        type: "aws_sdk_dataexchange.types.type.Type",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        asset_configuration: Optional[
            "aws_sdk_dataexchange.types.asset_configuration.AssetConfiguration"
        ] = None,
    ) -> "aws_sdk_dataexchange.types.create_job_response.CreateJobResponse":
        """<p>This operation creates a job.</p>

        Args:
            asset_configuration: <p>The configuration for the asset, including tags to be applied to assets created by the job.</p>
            details: <p>The details for the CreateJob request.</p>
            type: <p>The type of job to be created.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.create_job_request.CreateJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.create_job_response.CreateJobResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.create_job

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.create_job.create_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.create_job_request.CreateJobRequest = {}  # type: ignore[typeddict-item]
        if asset_configuration is not None:
            input_["asset_configuration"] = asset_configuration
        input_["details"] = details
        input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_revision(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        comment: Optional[
            "aws_sdk_dataexchange.types.__string_min0_max16384.__stringMin0Max16384"
        ] = None,
        tags: Optional[
            "aws_sdk_dataexchange.types.map_of__string.MapOf__string"
        ] = None,
    ) -> "aws_sdk_dataexchange.types.create_revision_response.CreateRevisionResponse":
        """<p>This operation creates a revision for a data set.</p>

        Args:
            comment: <p>An optional comment about the revision.</p>
            data_set_id: <p>The unique identifier for a data set.</p>
            tags: <p>A revision tag is an optional label that you can assign to a revision when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.create_revision_request.CreateRevisionRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.create_revision_response.CreateRevisionResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.create_revision

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.create_revision.create_revision(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.create_revision_request.CreateRevisionRequest = {}  # type: ignore[typeddict-item]
        if comment is not None:
            input_["comment"] = comment
        input_["data_set_id"] = data_set_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_asset(
        self,
        asset_id: "aws_sdk_dataexchange.types.id.Id",
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        revision_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation deletes an asset.</p>

        Args:
            asset_id: <p>The unique identifier for an asset.</p>
            data_set_id: <p>The unique identifier for a data set.</p>
            revision_id: <p>The unique identifier for a revision.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.delete_asset_request.DeleteAssetRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_dataexchange._operations.data_exchange.delete_asset

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.delete_asset.delete_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.delete_asset_request.DeleteAssetRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        input_["data_set_id"] = data_set_id
        input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_data_grant(
        self,
        data_grant_id: "aws_sdk_dataexchange.types.data_grant_id.DataGrantId",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation deletes a data grant.</p>

        Args:
            data_grant_id: <p>The ID of the data grant to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.delete_data_grant_request.DeleteDataGrantRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_dataexchange._operations.data_exchange.delete_data_grant

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.delete_data_grant.delete_data_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.delete_data_grant_request.DeleteDataGrantRequest = {}  # type: ignore[typeddict-item]
        input_["data_grant_id"] = data_grant_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_data_set(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation deletes a data set.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.delete_data_set_request.DeleteDataSetRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_dataexchange._operations.data_exchange.delete_data_set

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.delete_data_set.delete_data_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.delete_data_set_request.DeleteDataSetRequest = {}  # type: ignore[typeddict-item]
        input_["data_set_id"] = data_set_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_event_action(
        self,
        event_action_id: "aws_sdk_dataexchange.types.__string.__string",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation deletes the event action.</p>

        Args:
            event_action_id: <p>The unique identifier for the event action.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.delete_event_action_request.DeleteEventActionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_dataexchange._operations.data_exchange.delete_event_action

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.delete_event_action.delete_event_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.delete_event_action_request.DeleteEventActionRequest = {}  # type: ignore[typeddict-item]
        input_["event_action_id"] = event_action_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_revision(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        revision_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation deletes a revision.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            revision_id: <p>The unique identifier for a revision.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.delete_revision_request.DeleteRevisionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_dataexchange._operations.data_exchange.delete_revision

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.delete_revision.delete_revision(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.delete_revision_request.DeleteRevisionRequest = {}  # type: ignore[typeddict-item]
        input_["data_set_id"] = data_set_id
        input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_asset(
        self,
        asset_id: "aws_sdk_dataexchange.types.id.Id",
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        revision_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> "aws_sdk_dataexchange.types.get_asset_response.GetAssetResponse":
        """<p>This operation returns information about an asset.</p>

        Args:
            asset_id: <p>The unique identifier for an asset.</p>
            data_set_id: <p>The unique identifier for a data set.</p>
            revision_id: <p>The unique identifier for a revision.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.get_asset_request.GetAssetRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.get_asset_response.GetAssetResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.get_asset

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.get_asset.get_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.get_asset_request.GetAssetRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        input_["data_set_id"] = data_set_id
        input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_data_grant(
        self,
        data_grant_id: "aws_sdk_dataexchange.types.data_grant_id.DataGrantId",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> "aws_sdk_dataexchange.types.get_data_grant_response.GetDataGrantResponse":
        """<p>This operation returns information about a data grant.</p>

        Args:
            data_grant_id: <p>The ID of the data grant.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.get_data_grant_request.GetDataGrantRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.get_data_grant_response.GetDataGrantResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.get_data_grant

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.get_data_grant.get_data_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.get_data_grant_request.GetDataGrantRequest = {}  # type: ignore[typeddict-item]
        input_["data_grant_id"] = data_grant_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_data_set(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> "aws_sdk_dataexchange.types.get_data_set_response.GetDataSetResponse":
        """<p>This operation returns information about a data set.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.get_data_set_request.GetDataSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.get_data_set_response.GetDataSetResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.get_data_set

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.get_data_set.get_data_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.get_data_set_request.GetDataSetRequest = {}  # type: ignore[typeddict-item]
        input_["data_set_id"] = data_set_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_event_action(
        self,
        event_action_id: "aws_sdk_dataexchange.types.__string.__string",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> "aws_sdk_dataexchange.types.get_event_action_response.GetEventActionResponse":
        """<p>This operation retrieves information about an event action.</p>

        Args:
            event_action_id: <p>The unique identifier for the event action.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.get_event_action_request.GetEventActionRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.get_event_action_response.GetEventActionResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.get_event_action

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.get_event_action.get_event_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.get_event_action_request.GetEventActionRequest = {}  # type: ignore[typeddict-item]
        input_["event_action_id"] = event_action_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_job(
        self,
        job_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> "aws_sdk_dataexchange.types.get_job_response.GetJobResponse":
        """<p>This operation returns information about a job.</p>

        Args:
            job_id: <p>The unique identifier for a job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.get_job_request.GetJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.get_job_response.GetJobResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.get_job

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.get_job.get_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.get_job_request.GetJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_received_data_grant(
        self,
        data_grant_arn: "aws_sdk_dataexchange.types.data_grant_arn.DataGrantArn",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> "aws_sdk_dataexchange.types.get_received_data_grant_response.GetReceivedDataGrantResponse":
        """<p>This operation returns information about a received data grant.</p>

        Args:
            data_grant_arn: <p>The Amazon Resource Name (ARN) of the data grant.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.get_received_data_grant_request.GetReceivedDataGrantRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.get_received_data_grant_response.GetReceivedDataGrantResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.get_received_data_grant

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.get_received_data_grant.get_received_data_grant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.get_received_data_grant_request.GetReceivedDataGrantRequest = {}  # type: ignore[typeddict-item]
        input_["data_grant_arn"] = data_grant_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_revision(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        revision_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> "aws_sdk_dataexchange.types.get_revision_response.GetRevisionResponse":
        """<p>This operation returns information about a revision.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            revision_id: <p>The unique identifier for a revision.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.get_revision_request.GetRevisionRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.get_revision_response.GetRevisionResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.get_revision

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.get_revision.get_revision(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.get_revision_request.GetRevisionRequest = {}  # type: ignore[typeddict-item]
        input_["data_set_id"] = data_set_id
        input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_data_grants(
        self,
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "aws_sdk_dataexchange.types.list_data_grants_response.ListDataGrantsResponse":
        """<p>This operation returns information about all data grants.</p>

        Args:
            max_results: <p>The maximum number of results to be included in the next page.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.list_data_grants_request.ListDataGrantsRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.list_data_grants_response.ListDataGrantsResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.list_data_grants

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.list_data_grants.list_data_grants(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.list_data_grants_request.ListDataGrantsRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_data_grants(
        self,
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_dataexchange.types.data_grant_summary_entry.DataGrantSummaryEntry]":
        _token = next_token
        while True:
            _response = self.list_data_grants(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("data_grant_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_set_revisions(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "aws_sdk_dataexchange.types.list_data_set_revisions_response.ListDataSetRevisionsResponse":
        """<p>This operation lists a data set's revisions sorted by CreatedAt in descending order.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            max_results: <p>The maximum number of results returned by a single call.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.list_data_set_revisions_request.ListDataSetRevisionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.list_data_set_revisions_response.ListDataSetRevisionsResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.list_data_set_revisions

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.list_data_set_revisions.list_data_set_revisions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.list_data_set_revisions_request.ListDataSetRevisionsRequest = {}  # type: ignore[typeddict-item]
        input_["data_set_id"] = data_set_id
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

    def iter_list_data_set_revisions(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_dataexchange.types.revision_entry.RevisionEntry]":
        _token = next_token
        while True:
            _response = self.list_data_set_revisions(
                data_set_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("revisions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_sets(
        self,
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
        origin: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "aws_sdk_dataexchange.types.list_data_sets_response.ListDataSetsResponse":
        """<p>This operation lists your data sets. When listing by origin OWNED, results are sorted by CreatedAt in descending order. When listing by origin ENTITLED, there is no order.</p>

        Args:
            max_results: <p>The maximum number of results returned by a single call.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            origin: <p>A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.list_data_sets_request.ListDataSetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.list_data_sets_response.ListDataSetsResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.list_data_sets

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.list_data_sets.list_data_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.list_data_sets_request.ListDataSetsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if origin is not None:
            input_["origin"] = origin

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_data_sets(
        self,
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
        origin: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_dataexchange.types.data_set_entry.DataSetEntry]":
        _token = next_token
        while True:
            _response = self.list_data_sets(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                origin=origin,
            )
            _page = _resolve_path(_response, ("data_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_event_actions(
        self,
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        event_source_id: Optional[
            "aws_sdk_dataexchange.types.__string.__string"
        ] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "aws_sdk_dataexchange.types.list_event_actions_response.ListEventActionsResponse":
        """<p>This operation lists your event actions.</p>

        Args:
            event_source_id: <p>The unique identifier for the event source.</p>
            max_results: <p>The maximum number of results returned by a single call.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.list_event_actions_request.ListEventActionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.list_event_actions_response.ListEventActionsResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.list_event_actions

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.list_event_actions.list_event_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.list_event_actions_request.ListEventActionsRequest = {}  # type: ignore[typeddict-item]
        if event_source_id is not None:
            input_["event_source_id"] = event_source_id
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

    def iter_list_event_actions(
        self,
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        event_source_id: Optional[
            "aws_sdk_dataexchange.types.__string.__string"
        ] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_dataexchange.types.event_action_entry.EventActionEntry]":
        _token = next_token
        while True:
            _response = self.list_event_actions(
                config_overrides=config_overrides,
                event_source_id=event_source_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("event_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_jobs(
        self,
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        data_set_id: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
        revision_id: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "aws_sdk_dataexchange.types.list_jobs_response.ListJobsResponse":
        """<p>This operation lists your jobs sorted by CreatedAt in descending order.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            max_results: <p>The maximum number of results returned by a single call.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            revision_id: <p>The unique identifier for a revision.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.list_jobs_request.ListJobsRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.list_jobs_response.ListJobsResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.list_jobs

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.list_jobs.list_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.list_jobs_request.ListJobsRequest = {}  # type: ignore[typeddict-item]
        if data_set_id is not None:
            input_["data_set_id"] = data_set_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_jobs(
        self,
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        data_set_id: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
        revision_id: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_dataexchange.types.job_entry.JobEntry]":
        _token = next_token
        while True:
            _response = self.list_jobs(
                config_overrides=config_overrides,
                data_set_id=data_set_id,
                max_results=max_results,
                next_token=_token,
                revision_id=revision_id,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_received_data_grants(
        self,
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
        acceptance_state: Optional[
            "aws_sdk_dataexchange.types.acceptance_state_filter_values.AcceptanceStateFilterValues"
        ] = None,
    ) -> "aws_sdk_dataexchange.types.list_received_data_grants_response.ListReceivedDataGrantsResponse":
        """<p>This operation returns information about all received data grants.</p>

        Args:
            max_results: <p>The maximum number of results to be included in the next page.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            acceptance_state: <p>The acceptance state of the data grants to list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.list_received_data_grants_request.ListReceivedDataGrantsRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.list_received_data_grants_response.ListReceivedDataGrantsResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.list_received_data_grants

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.list_received_data_grants.list_received_data_grants(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.list_received_data_grants_request.ListReceivedDataGrantsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if acceptance_state is not None:
            input_["acceptance_state"] = acceptance_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_received_data_grants(
        self,
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
        acceptance_state: Optional[
            "aws_sdk_dataexchange.types.acceptance_state_filter_values.AcceptanceStateFilterValues"
        ] = None,
    ) -> "Iterator[aws_sdk_dataexchange.types.received_data_grant_summaries_entry.ReceivedDataGrantSummariesEntry]":
        _token = next_token
        while True:
            _response = self.list_received_data_grants(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                acceptance_state=acceptance_state,
            )
            _page = _resolve_path(_response, ("data_grant_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_revision_assets(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        revision_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "aws_sdk_dataexchange.types.list_revision_assets_response.ListRevisionAssetsResponse":
        """<p>This operation lists a revision's assets sorted alphabetically in descending order.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            max_results: <p>The maximum number of results returned by a single call.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            revision_id: <p>The unique identifier for a revision.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.list_revision_assets_request.ListRevisionAssetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.list_revision_assets_response.ListRevisionAssetsResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.list_revision_assets

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.list_revision_assets.list_revision_assets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.list_revision_assets_request.ListRevisionAssetsRequest = {}  # type: ignore[typeddict-item]
        input_["data_set_id"] = data_set_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_revision_assets(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        revision_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_dataexchange.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_dataexchange.types.asset_entry.AssetEntry]":
        _token = next_token
        while True:
            _response = self.list_revision_assets(
                data_set_id,
                revision_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("assets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_dataexchange.types.__string.__string",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> "aws_sdk_dataexchange.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>This operation lists the tags on the resource.</p>

        Args:
            resource_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies an AWS resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.list_tags_for_resource

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def revoke_revision(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        revision_id: "aws_sdk_dataexchange.types.id.Id",
        revocation_comment: "aws_sdk_dataexchange.types.__string_min10_max512.__stringMin10Max512",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> "aws_sdk_dataexchange.types.revoke_revision_response.RevokeRevisionResponse":
        """<p>This operation revokes subscribers' access to a revision.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            revision_id: <p>The unique identifier for a revision.</p>
            revocation_comment: <p>A required comment to inform subscribers of the reason their access to the revision was revoked.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.revoke_revision_request.RevokeRevisionRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.revoke_revision_response.RevokeRevisionResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.revoke_revision

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.revoke_revision.revoke_revision(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.revoke_revision_request.RevokeRevisionRequest = {}  # type: ignore[typeddict-item]
        input_["data_set_id"] = data_set_id
        input_["revision_id"] = revision_id
        input_["revocation_comment"] = revocation_comment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_api_asset(
        self,
        asset_id: "aws_sdk_dataexchange.types.__string.__string",
        data_set_id: "aws_sdk_dataexchange.types.__string.__string",
        revision_id: "aws_sdk_dataexchange.types.__string.__string",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        body: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
        query_string_parameters: Optional[
            "aws_sdk_dataexchange.types.map_of__string.MapOf__string"
        ] = None,
        request_headers: Optional[
            "aws_sdk_dataexchange.types.map_of__string.MapOf__string"
        ] = None,
        method: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
        path: Optional["aws_sdk_dataexchange.types.__string.__string"] = None,
    ) -> "aws_sdk_dataexchange.types.send_api_asset_response.SendApiAssetResponse":
        """<p>This operation invokes an API Gateway API asset. The request is proxied to the provider’s API Gateway API.</p>

        Args:
            body: <p>The request body.</p>
            query_string_parameters: <p>Attach query string parameters to the end of the URI (for example, /v1/examplePath?exampleParam=exampleValue).</p>
            asset_id: <p>Asset ID value for the API request.</p>
            data_set_id: <p>Data set ID value for the API request.</p>
            request_headers: <p>Any header value prefixed with x-amzn-dataexchange-header- will have that stripped before sending the Asset API request. Use this when you want to override a header that AWS Data Exchange uses. Alternatively, you can use the header without a prefix to the HTTP request.</p>
            method: <p>HTTP method value for the API request. Alternatively, you can use the appropriate verb in your request.</p>
            path: <p>URI path value for the API request. Alternatively, you can set the URI path directly by invoking /v1/{pathValue}.</p>
            revision_id: <p>Revision ID value for the API request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.send_api_asset_request.SendApiAssetRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.send_api_asset_response.SendApiAssetResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.send_api_asset

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.send_api_asset.send_api_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.send_api_asset_request.SendApiAssetRequest = {}  # type: ignore[typeddict-item]
        if body is not None:
            input_["body"] = body
        if query_string_parameters is not None:
            input_["query_string_parameters"] = query_string_parameters
        input_["asset_id"] = asset_id
        input_["data_set_id"] = data_set_id
        if request_headers is not None:
            input_["request_headers"] = request_headers
        if method is not None:
            input_["method"] = method
        if path is not None:
            input_["path"] = path
        input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def send_data_set_notification(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        type: "aws_sdk_dataexchange.types.notification_type.NotificationType",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        scope: Optional["aws_sdk_dataexchange.types.scope_details.ScopeDetails"] = None,
        client_token: Optional[
            "aws_sdk_dataexchange.types.client_token.ClientToken"
        ] = None,
        comment: Optional[
            "aws_sdk_dataexchange.types.__string_min0_max4096.__stringMin0Max4096"
        ] = None,
        details: Optional[
            "aws_sdk_dataexchange.types.notification_details.NotificationDetails"
        ] = None,
    ) -> "aws_sdk_dataexchange.types.send_data_set_notification_response.SendDataSetNotificationResponse":
        """<p>The type of event associated with the data set.</p>

        Args:
            scope: <p>Affected scope of this notification such as the underlying resources affected by the notification event.</p>
            client_token: <p>Idempotency key for the notification, this key allows us to deduplicate notifications that are sent in quick succession erroneously.</p>
            comment: <p>Free-form text field for providers to add information about their notifications.</p>
            data_set_id: <p>Affected data set of the notification.</p>
            details: <p>Extra details specific to this notification type.</p>
            type: <p>The type of the notification. Describing the kind of event the notification is alerting you to.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.send_data_set_notification_request.SendDataSetNotificationRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.send_data_set_notification_response.SendDataSetNotificationResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.send_data_set_notification

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.send_data_set_notification.send_data_set_notification(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.send_data_set_notification_request.SendDataSetNotificationRequest = {}  # type: ignore[typeddict-item]
        if scope is not None:
            input_["scope"] = scope
        if client_token is not None:
            input_["client_token"] = client_token
        if comment is not None:
            input_["comment"] = comment
        input_["data_set_id"] = data_set_id
        if details is not None:
            input_["details"] = details
        input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_job(
        self,
        job_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> "aws_sdk_dataexchange.types.start_job_response.StartJobResponse":
        """<p>This operation starts a job.</p>

        Args:
            job_id: <p>The unique identifier for a job.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.start_job_request.StartJobRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.start_job_response.StartJobResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.start_job

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.start_job.start_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.start_job_request.StartJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_dataexchange.types.__string.__string",
        tags: "aws_sdk_dataexchange.types.map_of__string.MapOf__string",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation tags a resource.</p>

        Args:
            resource_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies an AWS resource.</p>
            tags: <p>A label that consists of a customer-defined key and an optional value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_dataexchange._operations.data_exchange.tag_resource

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_dataexchange.types.__string.__string",
        tag_keys: "aws_sdk_dataexchange.types.list_of__string.ListOf__string",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> None:
        """<p>This operation removes one or more tags from a resource.</p>

        Args:
            resource_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies an AWS resource.</p>
            tag_keys: <p>The key tags.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_dataexchange._operations.data_exchange.untag_resource

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_asset(
        self,
        asset_id: "aws_sdk_dataexchange.types.id.Id",
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        name: "aws_sdk_dataexchange.types.asset_name.AssetName",
        revision_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
    ) -> "aws_sdk_dataexchange.types.update_asset_response.UpdateAssetResponse":
        r"""<p>This operation updates an asset.</p>

        Args:
            asset_id: <p>The unique identifier for an asset.</p>
            data_set_id: <p>The unique identifier for a data set.</p>
            name: <p>The name of the asset. When importing from Amazon S3, the Amazon S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target Amazon S3 object key. When importing from Amazon API Gateway API, the API name is used as the asset name. When importing from Amazon Redshift, the datashare name is used as the asset name. When importing from AWS Lake Formation, the static values of \"Database(s) included in the LF-tag policy\" or \"Table(s) included in LF-tag policy\" are used as the name.</p>
            revision_id: <p>The unique identifier for a revision.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.update_asset_request.UpdateAssetRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.update_asset_response.UpdateAssetResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.update_asset

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.update_asset.update_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.update_asset_request.UpdateAssetRequest = {}  # type: ignore[typeddict-item]
        input_["asset_id"] = asset_id
        input_["data_set_id"] = data_set_id
        input_["name"] = name
        input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_data_set(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        description: Optional[
            "aws_sdk_dataexchange.types.description.Description"
        ] = None,
        name: Optional["aws_sdk_dataexchange.types.name.Name"] = None,
    ) -> "aws_sdk_dataexchange.types.update_data_set_response.UpdateDataSetResponse":
        """<p>This operation updates a data set.</p>

        Args:
            data_set_id: <p>The unique identifier for a data set.</p>
            description: <p>The description for the data set.</p>
            name: <p>The name of the data set.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.update_data_set_request.UpdateDataSetRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.update_data_set_response.UpdateDataSetResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.update_data_set

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.update_data_set.update_data_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.update_data_set_request.UpdateDataSetRequest = {}  # type: ignore[typeddict-item]
        input_["data_set_id"] = data_set_id
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_event_action(
        self,
        event_action_id: "aws_sdk_dataexchange.types.__string.__string",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        action: Optional["aws_sdk_dataexchange.types.action.Action"] = None,
    ) -> "aws_sdk_dataexchange.types.update_event_action_response.UpdateEventActionResponse":
        """<p>This operation updates the event action.</p>

        Args:
            action: <p>What occurs after a certain event.</p>
            event_action_id: <p>The unique identifier for the event action.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.update_event_action_request.UpdateEventActionRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.update_event_action_response.UpdateEventActionResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.update_event_action

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.update_event_action.update_event_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.update_event_action_request.UpdateEventActionRequest = {}  # type: ignore[typeddict-item]
        if action is not None:
            input_["action"] = action
        input_["event_action_id"] = event_action_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_revision(
        self,
        data_set_id: "aws_sdk_dataexchange.types.id.Id",
        revision_id: "aws_sdk_dataexchange.types.id.Id",
        *,
        config_overrides: Optional[DataExchangeClientConfig] = None,
        comment: Optional[
            "aws_sdk_dataexchange.types.__string_min0_max16384.__stringMin0Max16384"
        ] = None,
        finalized: Optional["aws_sdk_dataexchange.types.__boolean.__boolean"] = None,
    ) -> "aws_sdk_dataexchange.types.update_revision_response.UpdateRevisionResponse":
        """<p>This operation updates a revision.</p>

        Args:
            comment: <p>An optional comment about the revision.</p>
            data_set_id: <p>The unique identifier for a data set.</p>
            finalized: <p>Finalizing a revision tells AWS Data Exchange that your changes to the assets in the revision are complete. After it's in this read-only state, you can publish the revision to your products.</p>
            revision_id: <p>The unique identifier for a revision.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_dataexchange.types.update_revision_request.UpdateRevisionRequest]",
        ) -> OperationResponse[
            "aws_sdk_dataexchange.types.update_revision_response.UpdateRevisionResponse"
        ]:
            import aws_sdk_dataexchange._operations.data_exchange.update_revision

            output, http_response = (
                aws_sdk_dataexchange._operations.data_exchange.update_revision.update_revision(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_dataexchange.types.update_revision_request.UpdateRevisionRequest = {}  # type: ignore[typeddict-item]
        if comment is not None:
            input_["comment"] = comment
        input_["data_set_id"] = data_set_id
        if finalized is not None:
            input_["finalized"] = finalized
        input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
