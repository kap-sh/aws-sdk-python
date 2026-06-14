"""Generated from Smithy shape ``com.amazonaws.cognitosync#AWSCognitoSyncService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_cognito_sync._auth._signers
import aws_sdk_cognito_sync._auth._sigv4
from aws_sdk_cognito_sync._auth._identity import Credentials
from aws_sdk_cognito_sync._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_cognito_sync._auth._zapros_handler import AuthMiddleware
from aws_sdk_cognito_sync._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.bulk_publish_request
    import aws_sdk_cognito_sync.types.bulk_publish_response
    import aws_sdk_cognito_sync.types.client_context
    import aws_sdk_cognito_sync.types.cognito_streams
    import aws_sdk_cognito_sync.types.dataset_name
    import aws_sdk_cognito_sync.types.delete_dataset_request
    import aws_sdk_cognito_sync.types.delete_dataset_response
    import aws_sdk_cognito_sync.types.describe_dataset_request
    import aws_sdk_cognito_sync.types.describe_dataset_response
    import aws_sdk_cognito_sync.types.describe_identity_pool_usage_request
    import aws_sdk_cognito_sync.types.describe_identity_pool_usage_response
    import aws_sdk_cognito_sync.types.describe_identity_usage_request
    import aws_sdk_cognito_sync.types.describe_identity_usage_response
    import aws_sdk_cognito_sync.types.device_id
    import aws_sdk_cognito_sync.types.events
    import aws_sdk_cognito_sync.types.get_bulk_publish_details_request
    import aws_sdk_cognito_sync.types.get_bulk_publish_details_response
    import aws_sdk_cognito_sync.types.get_cognito_events_request
    import aws_sdk_cognito_sync.types.get_cognito_events_response
    import aws_sdk_cognito_sync.types.get_identity_pool_configuration_request
    import aws_sdk_cognito_sync.types.get_identity_pool_configuration_response
    import aws_sdk_cognito_sync.types.identity_id
    import aws_sdk_cognito_sync.types.identity_pool_id
    import aws_sdk_cognito_sync.types.integer_string
    import aws_sdk_cognito_sync.types.list_datasets_request
    import aws_sdk_cognito_sync.types.list_datasets_response
    import aws_sdk_cognito_sync.types.list_identity_pool_usage_request
    import aws_sdk_cognito_sync.types.list_identity_pool_usage_response
    import aws_sdk_cognito_sync.types.list_records_request
    import aws_sdk_cognito_sync.types.list_records_response
    import aws_sdk_cognito_sync.types.long
    import aws_sdk_cognito_sync.types.platform
    import aws_sdk_cognito_sync.types.push_sync
    import aws_sdk_cognito_sync.types.push_token
    import aws_sdk_cognito_sync.types.record_patch_list
    import aws_sdk_cognito_sync.types.register_device_request
    import aws_sdk_cognito_sync.types.register_device_response
    import aws_sdk_cognito_sync.types.set_cognito_events_request
    import aws_sdk_cognito_sync.types.set_identity_pool_configuration_request
    import aws_sdk_cognito_sync.types.set_identity_pool_configuration_response
    import aws_sdk_cognito_sync.types.string
    import aws_sdk_cognito_sync.types.subscribe_to_dataset_request
    import aws_sdk_cognito_sync.types.subscribe_to_dataset_response
    import aws_sdk_cognito_sync.types.sync_session_token
    import aws_sdk_cognito_sync.types.unsubscribe_from_dataset_request
    import aws_sdk_cognito_sync.types.unsubscribe_from_dataset_response
    import aws_sdk_cognito_sync.types.update_records_request
    import aws_sdk_cognito_sync.types.update_records_response


class CognitoSyncClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class CognitoSyncClient:
    """A client for the ``CognitoSync`` service.

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
        self._config = CognitoSyncClientConfig(
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
        self, config_overrides: Optional[CognitoSyncClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CognitoSyncClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    def bulk_publish(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> "aws_sdk_cognito_sync.types.bulk_publish_response.BulkPublishResponse":
        """<p>Initiates a bulk publish of all existing datasets for an Identity Pool to the configured stream. Customers are limited to one successful bulk publish per 24 hours. Bulk publish is an asynchronous request, customers can see the status of the request via the GetBulkPublishDetails operation.</p><p>This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.</p>

        Args:
            identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.bulk_publish_request.BulkPublishRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.bulk_publish_response.BulkPublishResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.bulk_publish

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.bulk_publish.bulk_publish(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.bulk_publish_request.BulkPublishRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_dataset(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId",
        dataset_name: "aws_sdk_cognito_sync.types.dataset_name.DatasetName",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> "aws_sdk_cognito_sync.types.delete_dataset_response.DeleteDatasetResponse":
        """<p>Deletes the specific dataset. The dataset will be deleted permanently, and the action can't be undone. Datasets that this dataset was merged with will no longer report the merge. Any subsequent operation on this dataset will result in a ResourceNotFoundException.</p> <p>This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.</p>

        Args:
            identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            dataset_name: A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.delete_dataset_response.DeleteDatasetResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.delete_dataset

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.delete_dataset.delete_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.delete_dataset_request.DeleteDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id
        input_["identity_id"] = identity_id
        input_["dataset_name"] = dataset_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_dataset(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId",
        dataset_name: "aws_sdk_cognito_sync.types.dataset_name.DatasetName",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> "aws_sdk_cognito_sync.types.describe_dataset_response.DescribeDatasetResponse":
        """<p>Gets meta data about a dataset by identity and dataset name. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.</p> <p>This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.</p>

        Args:
            identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            dataset_name: A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.describe_dataset_request.DescribeDatasetRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.describe_dataset_response.DescribeDatasetResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.describe_dataset

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.describe_dataset.describe_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.describe_dataset_request.DescribeDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id
        input_["identity_id"] = identity_id
        input_["dataset_name"] = dataset_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_identity_pool_usage(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> "aws_sdk_cognito_sync.types.describe_identity_pool_usage_response.DescribeIdentityPoolUsageResponse":
        r"""<p>Gets usage details (for example, data storage) about a particular identity pool.</p> <p>This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.</p> <examples> <example> <name>DescribeIdentityPoolUsage</name> <description>The following examples have been edited for readability.</description> <request> POST / HTTP/1.1 CONTENT-TYPE: application/json X-AMZN-REQUESTID: 8dc0e749-c8cd-48bd-8520-da6be00d528b X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.DescribeIdentityPoolUsage HOST: cognito-sync.us-east-1.amazonaws.com:443 X-AMZ-DATE: 20141111T205737Z AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;host;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<signature> { \"Operation\": \"com.amazonaws.cognito.sync.model#DescribeIdentityPoolUsage\", \"Service\": \"com.amazonaws.cognito.sync.model#AWSCognitoSyncService\", \"Input\": { \"IdentityPoolId\": \"IDENTITY_POOL_ID\" } } </request> <response> 1.1 200 OK x-amzn-requestid: 8dc0e749-c8cd-48bd-8520-da6be00d528b content-type: application/json content-length: 271 date: Tue, 11 Nov 2014 20:57:37 GMT { \"Output\": { \"__type\": \"com.amazonaws.cognito.sync.model#DescribeIdentityPoolUsageResponse\", \"IdentityPoolUsage\": { \"DataStorage\": 0, \"IdentityPoolId\": \"IDENTITY_POOL_ID\", \"LastModifiedDate\": 1.413231134115E9, \"SyncSessionsCount\": null } }, \"Version\": \"1.0\" } </response> </example> </examples>

        Args:
            identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.describe_identity_pool_usage_request.DescribeIdentityPoolUsageRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.describe_identity_pool_usage_response.DescribeIdentityPoolUsageResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.describe_identity_pool_usage

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.describe_identity_pool_usage.describe_identity_pool_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.describe_identity_pool_usage_request.DescribeIdentityPoolUsageRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_identity_usage(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> "aws_sdk_cognito_sync.types.describe_identity_usage_response.DescribeIdentityUsageResponse":
        r"""<p>Gets usage information for an identity, including number of datasets and data usage.</p> <p>This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.</p> <examples> <example> <name>DescribeIdentityUsage</name> <description>The following examples have been edited for readability.</description> <request> POST / HTTP/1.1 CONTENT-TYPE: application/json X-AMZN-REQUESTID: 33f9b4e4-a177-4aad-a3bb-6edb7980b283 X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.DescribeIdentityUsage HOST: cognito-sync.us-east-1.amazonaws.com:443 X-AMZ-DATE: 20141111T215129Z AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;host;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<signature> { \"Operation\": \"com.amazonaws.cognito.sync.model#DescribeIdentityUsage\", \"Service\": \"com.amazonaws.cognito.sync.model#AWSCognitoSyncService\", \"Input\": { \"IdentityPoolId\": \"IDENTITY_POOL_ID\", \"IdentityId\": \"IDENTITY_ID\" } } </request> <response> 1.1 200 OK x-amzn-requestid: 33f9b4e4-a177-4aad-a3bb-6edb7980b283 content-type: application/json content-length: 318 date: Tue, 11 Nov 2014 21:51:29 GMT { \"Output\": { \"__type\": \"com.amazonaws.cognito.sync.model#DescribeIdentityUsageResponse\", \"IdentityUsage\": { \"DataStorage\": 16, \"DatasetCount\": 1, \"IdentityId\": \"IDENTITY_ID\", \"IdentityPoolId\": \"IDENTITY_POOL_ID\", \"LastModifiedDate\": 1.412974081336E9 } }, \"Version\": \"1.0\" } </response> </example> </examples>

        Args:
            identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.describe_identity_usage_request.DescribeIdentityUsageRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.describe_identity_usage_response.DescribeIdentityUsageResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.describe_identity_usage

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.describe_identity_usage.describe_identity_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.describe_identity_usage_request.DescribeIdentityUsageRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id
        input_["identity_id"] = identity_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_bulk_publish_details(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> "aws_sdk_cognito_sync.types.get_bulk_publish_details_response.GetBulkPublishDetailsResponse":
        """<p>Get the status of the last BulkPublish operation for an identity pool.</p><p>This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.</p>

        Args:
            identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.get_bulk_publish_details_request.GetBulkPublishDetailsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.get_bulk_publish_details_response.GetBulkPublishDetailsResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.get_bulk_publish_details

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.get_bulk_publish_details.get_bulk_publish_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.get_bulk_publish_details_request.GetBulkPublishDetailsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cognito_events(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> "aws_sdk_cognito_sync.types.get_cognito_events_response.GetCognitoEventsResponse":
        """<p>Gets the events and the corresponding Lambda functions associated with an identity pool.</p><p>This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.</p>

        Args:
            identity_pool_id: <p>The Cognito Identity Pool ID for the request</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.get_cognito_events_request.GetCognitoEventsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.get_cognito_events_response.GetCognitoEventsResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.get_cognito_events

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.get_cognito_events.get_cognito_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.get_cognito_events_request.GetCognitoEventsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_identity_pool_configuration(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> "aws_sdk_cognito_sync.types.get_identity_pool_configuration_response.GetIdentityPoolConfigurationResponse":
        r"""<p>Gets the configuration settings of an identity pool.</p><p>This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.</p> <examples> <example> <name>GetIdentityPoolConfiguration</name> <description>The following examples have been edited for readability.</description> <request> POST / HTTP/1.1 CONTENT-TYPE: application/json X-AMZN-REQUESTID: b1cfdd4b-f620-4fe4-be0f-02024a1d33da X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.GetIdentityPoolConfiguration HOST: cognito-sync.us-east-1.amazonaws.com X-AMZ-DATE: 20141004T195722Z AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;content-length;host;x-amz-date;x-amz-target, Signature=<signature> { \"Operation\": \"com.amazonaws.cognito.sync.model#GetIdentityPoolConfiguration\", \"Service\": \"com.amazonaws.cognito.sync.model#AWSCognitoSyncService\", \"Input\": { \"IdentityPoolId\": \"ID_POOL_ID\" } } </request> <response> 1.1 200 OK x-amzn-requestid: b1cfdd4b-f620-4fe4-be0f-02024a1d33da date: Sat, 04 Oct 2014 19:57:22 GMT content-type: application/json content-length: 332 { \"Output\": { \"__type\": \"com.amazonaws.cognito.sync.model#GetIdentityPoolConfigurationResponse\", \"IdentityPoolId\": \"ID_POOL_ID\", \"PushSync\": { \"ApplicationArns\": [\"PLATFORMARN1\", \"PLATFORMARN2\"], \"RoleArn\": \"ROLEARN\" } }, \"Version\": \"1.0\" } </response> </example> </examples>

        Args:
            identity_pool_id: <p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool for which to return a configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.get_identity_pool_configuration_request.GetIdentityPoolConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.get_identity_pool_configuration_response.GetIdentityPoolConfigurationResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.get_identity_pool_configuration

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.get_identity_pool_configuration.get_identity_pool_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.get_identity_pool_configuration_request.GetIdentityPoolConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_datasets(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
        next_token: Optional["aws_sdk_cognito_sync.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_cognito_sync.types.integer_string.IntegerString"
        ] = None,
    ) -> "aws_sdk_cognito_sync.types.list_datasets_response.ListDatasetsResponse":
        r"""<p>Lists datasets for an identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.</p> <p>ListDatasets can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use the Cognito Identity credentials to make this API call.</p> <examples> <example> <name>ListDatasets</name> <description>The following examples have been edited for readability.</description> <request> POST / HTTP/1.1 CONTENT-TYPE: application/json X-AMZN-REQUESTID: 15225768-209f-4078-aaed-7494ace9f2db X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.ListDatasets HOST: cognito-sync.us-east-1.amazonaws.com:443 X-AMZ-DATE: 20141111T215640Z AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;host;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<signature> { \"Operation\": \"com.amazonaws.cognito.sync.model#ListDatasets\", \"Service\": \"com.amazonaws.cognito.sync.model#AWSCognitoSyncService\", \"Input\": { \"IdentityPoolId\": \"IDENTITY_POOL_ID\", \"IdentityId\": \"IDENTITY_ID\", \"MaxResults\": \"3\" } } </request> <response> 1.1 200 OK x-amzn-requestid: 15225768-209f-4078-aaed-7494ace9f2db, 15225768-209f-4078-aaed-7494ace9f2db content-type: application/json content-length: 355 date: Tue, 11 Nov 2014 21:56:40 GMT { \"Output\": { \"__type\": \"com.amazonaws.cognito.sync.model#ListDatasetsResponse\", \"Count\": 1, \"Datasets\": [ { \"CreationDate\": 1.412974057151E9, \"DataStorage\": 16, \"DatasetName\": \"my_list\", \"IdentityId\": \"IDENTITY_ID\", \"LastModifiedBy\": \"123456789012\", \"LastModifiedDate\": 1.412974057244E9, \"NumRecords\": 1 }], \"NextToken\": null }, \"Version\": \"1.0\" } </response> </example> </examples>

        Args:
            identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            next_token: A pagination token for obtaining the next page of results.
            max_results: The maximum number of results to be returned.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.list_datasets_request.ListDatasetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.list_datasets

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.list_datasets.list_datasets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.list_datasets_request.ListDatasetsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id
        input_["identity_id"] = identity_id
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

    def list_identity_pool_usage(
        self,
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
        next_token: Optional["aws_sdk_cognito_sync.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_cognito_sync.types.integer_string.IntegerString"
        ] = None,
    ) -> "aws_sdk_cognito_sync.types.list_identity_pool_usage_response.ListIdentityPoolUsageResponse":
        r"""<p>Gets a list of identity pools registered with Cognito.</p> <p>ListIdentityPoolUsage can only be called with developer credentials. You cannot make this API call with the temporary user credentials provided by Cognito Identity.</p> <examples> <example> <name>ListIdentityPoolUsage</name> <description>The following examples have been edited for readability.</description> <request> POST / HTTP/1.1 CONTENT-TYPE: application/json X-AMZN-REQUESTID: 9be7c425-ef05-48c0-aef3-9f0ff2fe17d3 X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.ListIdentityPoolUsage HOST: cognito-sync.us-east-1.amazonaws.com:443 X-AMZ-DATE: 20141111T211414Z AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;host;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<signature> { \"Operation\": \"com.amazonaws.cognito.sync.model#ListIdentityPoolUsage\", \"Service\": \"com.amazonaws.cognito.sync.model#AWSCognitoSyncService\", \"Input\": { \"MaxResults\": \"2\" } } </request> <response> 1.1 200 OK x-amzn-requestid: 9be7c425-ef05-48c0-aef3-9f0ff2fe17d3 content-type: application/json content-length: 519 date: Tue, 11 Nov 2014 21:14:14 GMT { \"Output\": { \"__type\": \"com.amazonaws.cognito.sync.model#ListIdentityPoolUsageResponse\", \"Count\": 2, \"IdentityPoolUsages\": [ { \"DataStorage\": 0, \"IdentityPoolId\": \"IDENTITY_POOL_ID\", \"LastModifiedDate\": 1.413836234607E9, \"SyncSessionsCount\": null }, { \"DataStorage\": 0, \"IdentityPoolId\": \"IDENTITY_POOL_ID\", \"LastModifiedDate\": 1.410892165601E9, \"SyncSessionsCount\": null }], \"MaxResults\": 2, \"NextToken\": \"dXMtZWFzdC0xOjBjMWJhMDUyLWUwOTgtNDFmYS1hNzZlLWVhYTJjMTI1Zjg2MQ==\" }, \"Version\": \"1.0\" } </response> </example> </examples>

        Args:
            next_token: A pagination token for obtaining the next page of results.
            max_results: The maximum number of results to be returned.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.list_identity_pool_usage_request.ListIdentityPoolUsageRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.list_identity_pool_usage_response.ListIdentityPoolUsageResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.list_identity_pool_usage

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.list_identity_pool_usage.list_identity_pool_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.list_identity_pool_usage_request.ListIdentityPoolUsageRequest = {}  # type: ignore[typeddict-item]
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

    def list_records(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId",
        dataset_name: "aws_sdk_cognito_sync.types.dataset_name.DatasetName",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
        last_sync_count: Optional["aws_sdk_cognito_sync.types.long.Long"] = None,
        next_token: Optional["aws_sdk_cognito_sync.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_cognito_sync.types.integer_string.IntegerString"
        ] = None,
        sync_session_token: Optional[
            "aws_sdk_cognito_sync.types.sync_session_token.SyncSessionToken"
        ] = None,
    ) -> "aws_sdk_cognito_sync.types.list_records_response.ListRecordsResponse":
        r"""<p>Gets paginated records, optionally changed after a particular sync count for a dataset and identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.</p> <p>ListRecords can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.</p> <examples> <example> <name>ListRecords</name> <description>The following examples have been edited for readability.</description> <request> POST / HTTP/1.1 CONTENT-TYPE: application/json X-AMZN-REQUESTID: b3d2e31e-d6b7-4612-8e84-c9ba288dab5d X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.ListRecords HOST: cognito-sync.us-east-1.amazonaws.com:443 X-AMZ-DATE: 20141111T183230Z AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;host;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<signature> { \"Operation\": \"com.amazonaws.cognito.sync.model#ListRecords\", \"Service\": \"com.amazonaws.cognito.sync.model#AWSCognitoSyncService\", \"Input\": { \"IdentityPoolId\": \"IDENTITY_POOL_ID\", \"IdentityId\": \"IDENTITY_ID\", \"DatasetName\": \"newDataSet\" } } </request> <response> 1.1 200 OK x-amzn-requestid: b3d2e31e-d6b7-4612-8e84-c9ba288dab5d content-type: application/json content-length: 623 date: Tue, 11 Nov 2014 18:32:30 GMT { \"Output\": { \"__type\": \"com.amazonaws.cognito.sync.model#ListRecordsResponse\", \"Count\": 0, \"DatasetDeletedAfterRequestedSyncCount\": false, \"DatasetExists\": false, \"DatasetSyncCount\": 0, \"LastModifiedBy\": null, \"MergedDatasetNames\": null, \"NextToken\": null, \"Records\": [], \"SyncSessionToken\": \"SYNC_SESSION_TOKEN\" }, \"Version\": \"1.0\" } </response> </example> </examples>

        Args:
            identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            dataset_name: A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
            last_sync_count: The last server sync count for this record.
            next_token: A pagination token for obtaining the next page of results.
            max_results: The maximum number of results to be returned.
            sync_session_token: A token containing a session ID, identity ID, and expiration.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.list_records_request.ListRecordsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.list_records_response.ListRecordsResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.list_records

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.list_records.list_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.list_records_request.ListRecordsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id
        input_["identity_id"] = identity_id
        input_["dataset_name"] = dataset_name
        if last_sync_count is not None:
            input_["last_sync_count"] = last_sync_count
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sync_session_token is not None:
            input_["sync_session_token"] = sync_session_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_device(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId",
        platform: "aws_sdk_cognito_sync.types.platform.Platform",
        token: "aws_sdk_cognito_sync.types.push_token.PushToken",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> "aws_sdk_cognito_sync.types.register_device_response.RegisterDeviceResponse":
        r"""<p>Registers a device to receive push sync notifications.</p><p>This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.</p> <examples> <example> <name>RegisterDevice</name> <description>The following examples have been edited for readability.</description> <request> POST / HTTP/1.1 CONTENT-TYPE: application/json X-AMZN-REQUESTID: 368f9200-3eca-449e-93b3-7b9c08d8e185 X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.RegisterDevice HOST: cognito-sync.us-east-1.amazonaws.com X-AMZ-DATE: 20141004T194643Z X-AMZ-SECURITY-TOKEN: <securitytoken> AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;content-length;host;x-amz-date;x-amz-target, Signature=<signature> { \"Operation\": \"com.amazonaws.cognito.sync.model#RegisterDevice\", \"Service\": \"com.amazonaws.cognito.sync.model#AWSCognitoSyncService\", \"Input\": { \"IdentityPoolId\": \"ID_POOL_ID\", \"IdentityId\": \"IDENTITY_ID\", \"Platform\": \"GCM\", \"Token\": \"PUSH_TOKEN\" } } </request> <response> 1.1 200 OK x-amzn-requestid: 368f9200-3eca-449e-93b3-7b9c08d8e185 date: Sat, 04 Oct 2014 19:46:44 GMT content-type: application/json content-length: 145 { \"Output\": { \"__type\": \"com.amazonaws.cognito.sync.model#RegisterDeviceResponse\", \"DeviceId\": \"5cd28fbe-dd83-47ab-9f83-19093a5fb014\" }, \"Version\": \"1.0\" } </response> </example> </examples>

        Args:
            identity_pool_id: <p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. Here, the ID of the pool that the identity belongs to.</p>
            identity_id: <p>The unique ID for this identity.</p>
            platform: <p>The SNS platform type (e.g. GCM, SDM, APNS, APNS_SANDBOX).</p>
            token: <p>The push token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.register_device_request.RegisterDeviceRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.register_device_response.RegisterDeviceResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.register_device

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.register_device.register_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.register_device_request.RegisterDeviceRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id
        input_["identity_id"] = identity_id
        input_["platform"] = platform
        input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def set_cognito_events(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        events: "aws_sdk_cognito_sync.types.events.Events",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> None:
        """<p>Sets the AWS Lambda function for a given event type for an identity pool. This request only updates the key/value pair specified. Other key/values pairs are not updated. To remove a key value pair, pass a empty value for the particular key.</p><p>This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.</p>

        Args:
            identity_pool_id: <p>The Cognito Identity Pool to use when configuring Cognito Events</p>
            events: <p>The events to configure</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.set_cognito_events_request.SetCognitoEventsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.set_cognito_events

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.set_cognito_events.set_cognito_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.set_cognito_events_request.SetCognitoEventsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id
        input_["events"] = events

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def set_identity_pool_configuration(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
        push_sync: Optional["aws_sdk_cognito_sync.types.push_sync.PushSync"] = None,
        cognito_streams: Optional[
            "aws_sdk_cognito_sync.types.cognito_streams.CognitoStreams"
        ] = None,
    ) -> "aws_sdk_cognito_sync.types.set_identity_pool_configuration_response.SetIdentityPoolConfigurationResponse":
        r"""<p>Sets the necessary configuration for push sync.</p><p>This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.</p> <examples> <example> <name>SetIdentityPoolConfiguration</name> <description>The following examples have been edited for readability.</description> <request> POST / HTTP/1.1 CONTENT-TYPE: application/json X-AMZN-REQUESTID: a46db021-f5dd-45d6-af5b-7069fa4a211b X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.SetIdentityPoolConfiguration HOST: cognito-sync.us-east-1.amazonaws.com X-AMZ-DATE: 20141004T200006Z AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;content-length;host;x-amz-date;x-amz-target, Signature=<signature> { \"Operation\": \"com.amazonaws.cognito.sync.model#SetIdentityPoolConfiguration\", \"Service\": \"com.amazonaws.cognito.sync.model#AWSCognitoSyncService\", \"Input\": { \"IdentityPoolId\": \"ID_POOL_ID\", \"PushSync\": { \"ApplicationArns\": [\"PLATFORMARN1\", \"PLATFORMARN2\"], \"RoleArn\": \"ROLEARN\" } } } </request> <response> 1.1 200 OK x-amzn-requestid: a46db021-f5dd-45d6-af5b-7069fa4a211b date: Sat, 04 Oct 2014 20:00:06 GMT content-type: application/json content-length: 332 { \"Output\": { \"__type\": \"com.amazonaws.cognito.sync.model#SetIdentityPoolConfigurationResponse\", \"IdentityPoolId\": \"ID_POOL_ID\", \"PushSync\": { \"ApplicationArns\": [\"PLATFORMARN1\", \"PLATFORMARN2\"], \"RoleArn\": \"ROLEARN\" } }, \"Version\": \"1.0\" } </response> </example> </examples>

        Args:
            identity_pool_id: <p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool to modify.</p>
            push_sync: <p>Options to apply to this identity pool for push synchronization.</p>
            cognito_streams: Options to apply to this identity pool for Amazon Cognito streams.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.set_identity_pool_configuration_request.SetIdentityPoolConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.set_identity_pool_configuration_response.SetIdentityPoolConfigurationResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.set_identity_pool_configuration

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.set_identity_pool_configuration.set_identity_pool_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.set_identity_pool_configuration_request.SetIdentityPoolConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id
        if push_sync is not None:
            input_["push_sync"] = push_sync
        if cognito_streams is not None:
            input_["cognito_streams"] = cognito_streams

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def subscribe_to_dataset(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId",
        dataset_name: "aws_sdk_cognito_sync.types.dataset_name.DatasetName",
        device_id: "aws_sdk_cognito_sync.types.device_id.DeviceId",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> "aws_sdk_cognito_sync.types.subscribe_to_dataset_response.SubscribeToDatasetResponse":
        r"""<p>Subscribes to receive notifications when a dataset is modified by another device.</p><p>This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.</p> <examples> <example> <name>SubscribeToDataset</name> <description>The following examples have been edited for readability.</description> <request> POST / HTTP/1.1 CONTENT-TYPE: application/json X-AMZN-REQUESTID: 8b9932b7-201d-4418-a960-0a470e11de9f X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.SubscribeToDataset HOST: cognito-sync.us-east-1.amazonaws.com X-AMZ-DATE: 20141004T195350Z X-AMZ-SECURITY-TOKEN: <securitytoken> AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;content-length;host;x-amz-date;x-amz-target, Signature=<signature> { \"Operation\": \"com.amazonaws.cognito.sync.model#SubscribeToDataset\", \"Service\": \"com.amazonaws.cognito.sync.model#AWSCognitoSyncService\", \"Input\": { \"IdentityPoolId\": \"ID_POOL_ID\", \"IdentityId\": \"IDENTITY_ID\", \"DatasetName\": \"Rufus\", \"DeviceId\": \"5cd28fbe-dd83-47ab-9f83-19093a5fb014\" } } </request> <response> 1.1 200 OK x-amzn-requestid: 8b9932b7-201d-4418-a960-0a470e11de9f date: Sat, 04 Oct 2014 19:53:50 GMT content-type: application/json content-length: 99 { \"Output\": { \"__type\": \"com.amazonaws.cognito.sync.model#SubscribeToDatasetResponse\" }, \"Version\": \"1.0\" } </response> </example> </examples>

        Args:
            identity_pool_id: <p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which the identity belongs.</p>
            identity_id: <p>Unique ID for this identity.</p>
            dataset_name: <p>The name of the dataset to subcribe to.</p>
            device_id: <p>The unique ID generated for this device by Cognito.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.subscribe_to_dataset_request.SubscribeToDatasetRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.subscribe_to_dataset_response.SubscribeToDatasetResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.subscribe_to_dataset

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.subscribe_to_dataset.subscribe_to_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.subscribe_to_dataset_request.SubscribeToDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id
        input_["identity_id"] = identity_id
        input_["dataset_name"] = dataset_name
        input_["device_id"] = device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def unsubscribe_from_dataset(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId",
        dataset_name: "aws_sdk_cognito_sync.types.dataset_name.DatasetName",
        device_id: "aws_sdk_cognito_sync.types.device_id.DeviceId",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
    ) -> "aws_sdk_cognito_sync.types.unsubscribe_from_dataset_response.UnsubscribeFromDatasetResponse":
        r"""<p>Unsubscribes from receiving notifications when a dataset is modified by another device.</p><p>This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.</p> <examples> <example> <name>UnsubscribeFromDataset</name> <description>The following examples have been edited for readability.</description> <request> POST / HTTP/1.1 CONTENT-TYPE: application/json X-AMZ-REQUESTSUPERTRACE: true X-AMZN-REQUESTID: 676896d6-14ca-45b1-8029-6d36b10a077e X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.UnsubscribeFromDataset HOST: cognito-sync.us-east-1.amazonaws.com X-AMZ-DATE: 20141004T195446Z X-AMZ-SECURITY-TOKEN: <securitytoken> AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;content-length;host;x-amz-date;x-amz-target, Signature=<signature> { \"Operation\": \"com.amazonaws.cognito.sync.model#UnsubscribeFromDataset\", \"Service\": \"com.amazonaws.cognito.sync.model#AWSCognitoSyncService\", \"Input\": { \"IdentityPoolId\": \"ID_POOL_ID\", \"IdentityId\": \"IDENTITY_ID\", \"DatasetName\": \"Rufus\", \"DeviceId\": \"5cd28fbe-dd83-47ab-9f83-19093a5fb014\" } } </request> <response> 1.1 200 OK x-amzn-requestid: 676896d6-14ca-45b1-8029-6d36b10a077e date: Sat, 04 Oct 2014 19:54:46 GMT content-type: application/json content-length: 103 { \"Output\": { \"__type\": \"com.amazonaws.cognito.sync.model#UnsubscribeFromDatasetResponse\" }, \"Version\": \"1.0\" } </response> </example> </examples>

        Args:
            identity_pool_id: <p>A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which this identity belongs.</p>
            identity_id: <p>Unique ID for this identity.</p>
            dataset_name: <p>The name of the dataset from which to unsubcribe.</p>
            device_id: <p>The unique ID generated for this device by Cognito.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.unsubscribe_from_dataset_request.UnsubscribeFromDatasetRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.unsubscribe_from_dataset_response.UnsubscribeFromDatasetResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.unsubscribe_from_dataset

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.unsubscribe_from_dataset.unsubscribe_from_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.unsubscribe_from_dataset_request.UnsubscribeFromDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id
        input_["identity_id"] = identity_id
        input_["dataset_name"] = dataset_name
        input_["device_id"] = device_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_records(
        self,
        identity_pool_id: "aws_sdk_cognito_sync.types.identity_pool_id.IdentityPoolId",
        identity_id: "aws_sdk_cognito_sync.types.identity_id.IdentityId",
        dataset_name: "aws_sdk_cognito_sync.types.dataset_name.DatasetName",
        sync_session_token: "aws_sdk_cognito_sync.types.sync_session_token.SyncSessionToken",
        *,
        config_overrides: Optional[CognitoSyncClientConfig] = None,
        device_id: Optional["aws_sdk_cognito_sync.types.device_id.DeviceId"] = None,
        record_patches: Optional[
            "aws_sdk_cognito_sync.types.record_patch_list.RecordPatchList"
        ] = None,
        client_context: Optional[
            "aws_sdk_cognito_sync.types.client_context.ClientContext"
        ] = None,
    ) -> "aws_sdk_cognito_sync.types.update_records_response.UpdateRecordsResponse":
        """<p>Posts updates to records and adds and deletes records for a dataset and user.</p> <p>The sync count in the record patch is your last known sync count for that record. The server will reject an UpdateRecords request with a ResourceConflictException if you try to patch a record with a new value but a stale sync count.</p><p>For example, if the sync count on the server is 5 for a key called highScore and you try and submit a new highScore with sync count of 4, the request will be rejected. To obtain the current sync count for a record, call ListRecords. On a successful update of the record, the response returns the new sync count for that record. You should present that sync count the next time you try to update that same record. When the record does not exist, specify the sync count as 0.</p> <p>This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.</p>

        Args:
            identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
            dataset_name: A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot).
            device_id: <p>The unique ID generated for this device by Cognito.</p>
            record_patches: A list of patch operations.
            sync_session_token: The SyncSessionToken returned by a previous call to ListRecords for this dataset and identity.
            client_context: Intended to supply a device ID that will populate the lastModifiedBy field referenced in other methods. The ClientContext field is not yet implemented.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cognito_sync.types.update_records_request.UpdateRecordsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cognito_sync.types.update_records_response.UpdateRecordsResponse"
        ]:
            import aws_sdk_cognito_sync._operations.aws_cognito_sync_service.update_records

            output, http_response = (
                aws_sdk_cognito_sync._operations.aws_cognito_sync_service.update_records.update_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cognito_sync.types.update_records_request.UpdateRecordsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_pool_id"] = identity_pool_id
        input_["identity_id"] = identity_id
        input_["dataset_name"] = dataset_name
        if device_id is not None:
            input_["device_id"] = device_id
        if record_patches is not None:
            input_["record_patches"] = record_patches
        input_["sync_session_token"] = sync_session_token
        if client_context is not None:
            input_["client_context"] = client_context

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
