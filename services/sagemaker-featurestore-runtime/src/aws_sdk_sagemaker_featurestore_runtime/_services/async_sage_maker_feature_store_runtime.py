"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#AmazonSageMakerFeatureStoreRuntime``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_sagemaker_featurestore_runtime._auth._signers
import aws_sdk_sagemaker_featurestore_runtime._auth._sigv4
from aws_sdk_sagemaker_featurestore_runtime._auth._identity import Credentials
from aws_sdk_sagemaker_featurestore_runtime._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_sagemaker_featurestore_runtime._auth._zapros_handler import AuthMiddleware
from aws_sdk_sagemaker_featurestore_runtime._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_identifiers
    import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_request
    import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response
    import aws_sdk_sagemaker_featurestore_runtime.types.delete_record_request
    import aws_sdk_sagemaker_featurestore_runtime.types.deletion_mode
    import aws_sdk_sagemaker_featurestore_runtime.types.expiration_time_response
    import aws_sdk_sagemaker_featurestore_runtime.types.feature_group_name_or_arn
    import aws_sdk_sagemaker_featurestore_runtime.types.feature_names
    import aws_sdk_sagemaker_featurestore_runtime.types.get_record_request
    import aws_sdk_sagemaker_featurestore_runtime.types.get_record_response
    import aws_sdk_sagemaker_featurestore_runtime.types.put_record_request
    import aws_sdk_sagemaker_featurestore_runtime.types.record
    import aws_sdk_sagemaker_featurestore_runtime.types.target_stores
    import aws_sdk_sagemaker_featurestore_runtime.types.ttl_duration
    import aws_sdk_sagemaker_featurestore_runtime.types.value_as_string


class AsyncSageMakerFeatureStoreRuntimeClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncSageMakerFeatureStoreRuntimeClient:
    """A client for the ``SageMakerFeatureStoreRuntime`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncSageMakerFeatureStoreRuntimeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[
            AsyncSageMakerFeatureStoreRuntimeClientConfig
        ] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSageMakerFeatureStoreRuntimeClientConfig = (
            config_overrides or {}
        )
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def batch_get_record(
        self,
        identifiers: "aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_identifiers.BatchGetRecordIdentifiers",
        *,
        config_overrides: Optional[
            AsyncSageMakerFeatureStoreRuntimeClientConfig
        ] = None,
        expiration_time_response: Optional[
            "aws_sdk_sagemaker_featurestore_runtime.types.expiration_time_response.ExpirationTimeResponse"
        ] = None,
    ) -> "aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response.BatchGetRecordResponse":
        """<p>Retrieves a batch of <code>Records</code> from a <code>FeatureGroup</code>.</p>

        Args:
            identifiers: <p>A list containing the name or Amazon Resource Name (ARN) of the <code>FeatureGroup</code>, the list of names of <code>Feature</code>s to be retrieved, and the corresponding <code>RecordIdentifier</code> values as strings.</p>
            expiration_time_response: <p>Parameter to request <code>ExpiresAt</code> in response. If <code>Enabled</code>, <code>BatchGetRecord</code> will return the value of <code>ExpiresAt</code>, if it is not null. If <code>Disabled</code> and null, <code>BatchGetRecord</code> will return null.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_request.BatchGetRecordRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_response.BatchGetRecordResponse"
        ]:
            import aws_sdk_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.batch_get_record

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.batch_get_record.async_batch_get_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_request.BatchGetRecordRequest = {}  # type: ignore[typeddict-item]
        input_["identifiers"] = identifiers
        if expiration_time_response is not None:
            input_["expiration_time_response"] = expiration_time_response

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_record(
        self,
        feature_group_name: "aws_sdk_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn",
        record_identifier_value_as_string: "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString",
        event_time: "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString",
        *,
        config_overrides: Optional[
            AsyncSageMakerFeatureStoreRuntimeClientConfig
        ] = None,
        target_stores: Optional[
            "aws_sdk_sagemaker_featurestore_runtime.types.target_stores.TargetStores"
        ] = None,
        deletion_mode: Optional[
            "aws_sdk_sagemaker_featurestore_runtime.types.deletion_mode.DeletionMode"
        ] = None,
    ) -> None:
        """<p>Deletes a <code>Record</code> from a <code>FeatureGroup</code> in the <code>OnlineStore</code>. Feature Store supports both <code>SoftDelete</code> and <code>HardDelete</code>. For <code>SoftDelete</code> (default), feature columns are set to <code>null</code> and the record is no longer retrievable by <code>GetRecord</code> or <code>BatchGetRecord</code>. For <code>HardDelete</code>, the complete <code>Record</code> is removed from the <code>OnlineStore</code>. In both cases, Feature Store appends the deleted record marker to the <code>OfflineStore</code>. The deleted record marker is a record with the same <code>RecordIdentifer</code> as the original, but with <code>is_deleted</code> value set to <code>True</code>, <code>EventTime</code> set to the delete input <code>EventTime</code>, and other feature values set to <code>null</code>.</p> <p>Note that the <code>EventTime</code> specified in <code>DeleteRecord</code> should be set later than the <code>EventTime</code> of the existing record in the <code>OnlineStore</code> for that <code>RecordIdentifer</code>. If it is not, the deletion does not occur:</p> <ul> <li> <p>For <code>SoftDelete</code>, the existing (not deleted) record remains in the <code>OnlineStore</code>, though the delete record marker is still written to the <code>OfflineStore</code>.</p> </li> <li> <p> <code>HardDelete</code> returns <code>EventTime</code>: <code>400 ValidationException</code> to indicate that the delete operation failed. No delete record marker is written to the <code>OfflineStore</code>.</p> </li> </ul> <p>When a record is deleted from the <code>OnlineStore</code>, the deleted record marker is appended to the <code>OfflineStore</code>. If you have the Iceberg table format enabled for your <code>OfflineStore</code>, you can remove all history of a record from the <code>OfflineStore</code> using Amazon Athena or Apache Spark. For information on how to hard delete a record from the <code>OfflineStore</code> with the Iceberg table format enabled, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-delete-records-offline-store.html#feature-store-delete-records-offline-store\">Delete records from the offline store</a>.</p>

        Args:
            feature_group_name: <p>The name or Amazon Resource Name (ARN) of the feature group to delete the record from. </p>
            record_identifier_value_as_string: <p>The value for the <code>RecordIdentifier</code> that uniquely identifies the record, in string format. </p>
            event_time: <p>Timestamp indicating when the deletion event occurred. <code>EventTime</code> can be used to query data at a certain point in time.</p>
            target_stores: <p>A list of stores from which you're deleting the record. By default, Feature Store deletes the record from all of the stores that you're using for the <code>FeatureGroup</code>.</p>
            deletion_mode: <p>The name of the deletion mode for deleting the record. By default, the deletion mode is set to <code>SoftDelete</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_featurestore_runtime.types.delete_record_request.DeleteRecordRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.delete_record

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.delete_record.async_delete_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_featurestore_runtime.types.delete_record_request.DeleteRecordRequest = {}  # type: ignore[typeddict-item]
        input_["feature_group_name"] = feature_group_name
        input_["record_identifier_value_as_string"] = record_identifier_value_as_string
        input_["event_time"] = event_time
        if target_stores is not None:
            input_["target_stores"] = target_stores
        if deletion_mode is not None:
            input_["deletion_mode"] = deletion_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_record(
        self,
        feature_group_name: "aws_sdk_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn",
        record_identifier_value_as_string: "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString",
        *,
        config_overrides: Optional[
            AsyncSageMakerFeatureStoreRuntimeClientConfig
        ] = None,
        feature_names: Optional[
            "aws_sdk_sagemaker_featurestore_runtime.types.feature_names.FeatureNames"
        ] = None,
        expiration_time_response: Optional[
            "aws_sdk_sagemaker_featurestore_runtime.types.expiration_time_response.ExpirationTimeResponse"
        ] = None,
    ) -> "aws_sdk_sagemaker_featurestore_runtime.types.get_record_response.GetRecordResponse":
        """<p>Use for <code>OnlineStore</code> serving from a <code>FeatureStore</code>. Only the latest records stored in the <code>OnlineStore</code> can be retrieved. If no Record with <code>RecordIdentifierValue</code> is found, then an empty result is returned. </p>

        Args:
            feature_group_name: <p>The name or Amazon Resource Name (ARN) of the feature group from which you want to retrieve a record.</p>
            record_identifier_value_as_string: <p>The value that corresponds to <code>RecordIdentifier</code> type and uniquely identifies the record in the <code>FeatureGroup</code>. </p>
            feature_names: <p>List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned.</p>
            expiration_time_response: <p>Parameter to request <code>ExpiresAt</code> in response. If <code>Enabled</code>, <code>GetRecord</code> will return the value of <code>ExpiresAt</code>, if it is not null. If <code>Disabled</code> and null, <code>GetRecord</code> will return null.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_featurestore_runtime.types.get_record_request.GetRecordRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_featurestore_runtime.types.get_record_response.GetRecordResponse"
        ]:
            import aws_sdk_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.get_record

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.get_record.async_get_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_featurestore_runtime.types.get_record_request.GetRecordRequest = {}  # type: ignore[typeddict-item]
        input_["feature_group_name"] = feature_group_name
        input_["record_identifier_value_as_string"] = record_identifier_value_as_string
        if feature_names is not None:
            input_["feature_names"] = feature_names
        if expiration_time_response is not None:
            input_["expiration_time_response"] = expiration_time_response

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_record(
        self,
        feature_group_name: "aws_sdk_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn",
        record: "aws_sdk_sagemaker_featurestore_runtime.types.record.Record",
        *,
        config_overrides: Optional[
            AsyncSageMakerFeatureStoreRuntimeClientConfig
        ] = None,
        target_stores: Optional[
            "aws_sdk_sagemaker_featurestore_runtime.types.target_stores.TargetStores"
        ] = None,
        ttl_duration: Optional[
            "aws_sdk_sagemaker_featurestore_runtime.types.ttl_duration.TtlDuration"
        ] = None,
    ) -> None:
        """<p>The <code>PutRecord</code> API is used to ingest a list of <code>Records</code> into your feature group. </p> <p>If a new record’s <code>EventTime</code> is greater, the new record is written to both the <code>OnlineStore</code> and <code>OfflineStore</code>. Otherwise, the record is a historic record and it is written only to the <code>OfflineStore</code>. </p> <p>You can specify the ingestion to be applied to the <code>OnlineStore</code>, <code>OfflineStore</code>, or both by using the <code>TargetStores</code> request parameter. </p> <p>You can set the ingested record to expire at a given time to live (TTL) duration after the record’s event time, <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>, by specifying the <code>TtlDuration</code> parameter. A record level <code>TtlDuration</code> is set when specifying the <code>TtlDuration</code> parameter using the <code>PutRecord</code> API call. If the input <code>TtlDuration</code> is <code>null</code> or unspecified, <code>TtlDuration</code> is set to the default feature group level <code>TtlDuration</code>. A record level <code>TtlDuration</code> supersedes the group level <code>TtlDuration</code>.</p>

        Args:
            feature_group_name: <p>The name or Amazon Resource Name (ARN) of the feature group that you want to insert the record into.</p>
            record: <p>List of FeatureValues to be inserted. This will be a full over-write. If you only want to update few of the feature values, do the following:</p> <ul> <li> <p>Use <code>GetRecord</code> to retrieve the latest record.</p> </li> <li> <p>Update the record returned from <code>GetRecord</code>. </p> </li> <li> <p>Use <code>PutRecord</code> to update feature values.</p> </li> </ul>
            target_stores: <p>A list of stores to which you're adding the record. By default, Feature Store adds the record to all of the stores that you're using for the <code>FeatureGroup</code>.</p>
            ttl_duration: <p>Time to live duration, where the record is hard deleted after the expiration time is reached; <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>. For information on HardDelete, see the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html\">DeleteRecord</a> API in the Amazon SageMaker API Reference guide.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_featurestore_runtime.types.put_record_request.PutRecordRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.put_record

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_featurestore_runtime._operations.amazon_sage_maker_feature_store_runtime.put_record.async_put_record(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_featurestore_runtime.types.put_record_request.PutRecordRequest = {}  # type: ignore[typeddict-item]
        input_["feature_group_name"] = feature_group_name
        input_["record"] = record
        if target_stores is not None:
            input_["target_stores"] = target_stores
        if ttl_duration is not None:
            input_["ttl_duration"] = ttl_duration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
