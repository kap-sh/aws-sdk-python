"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#AWSLookoutEquipmentFrontendService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_lookoutequipment._auth._signers
import aws_sdk_lookoutequipment._auth._sigv4
from aws_sdk_lookoutequipment._auth._identity import Credentials
from aws_sdk_lookoutequipment._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_lookoutequipment._auth._zapros_handler import AuthMiddleware
from aws_sdk_lookoutequipment._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.amazon_resource_arn
    import aws_sdk_lookoutequipment.types.comments
    import aws_sdk_lookoutequipment.types.create_dataset_request
    import aws_sdk_lookoutequipment.types.create_dataset_response
    import aws_sdk_lookoutequipment.types.create_inference_scheduler_request
    import aws_sdk_lookoutequipment.types.create_inference_scheduler_response
    import aws_sdk_lookoutequipment.types.create_label_group_request
    import aws_sdk_lookoutequipment.types.create_label_group_response
    import aws_sdk_lookoutequipment.types.create_label_request
    import aws_sdk_lookoutequipment.types.create_label_response
    import aws_sdk_lookoutequipment.types.create_model_request
    import aws_sdk_lookoutequipment.types.create_model_response
    import aws_sdk_lookoutequipment.types.create_retraining_scheduler_request
    import aws_sdk_lookoutequipment.types.create_retraining_scheduler_response
    import aws_sdk_lookoutequipment.types.data_delay_offset_in_minutes
    import aws_sdk_lookoutequipment.types.data_pre_processing_configuration
    import aws_sdk_lookoutequipment.types.data_upload_frequency
    import aws_sdk_lookoutequipment.types.dataset_arn
    import aws_sdk_lookoutequipment.types.dataset_identifier
    import aws_sdk_lookoutequipment.types.dataset_name
    import aws_sdk_lookoutequipment.types.dataset_schema
    import aws_sdk_lookoutequipment.types.delete_dataset_request
    import aws_sdk_lookoutequipment.types.delete_inference_scheduler_request
    import aws_sdk_lookoutequipment.types.delete_label_group_request
    import aws_sdk_lookoutequipment.types.delete_label_request
    import aws_sdk_lookoutequipment.types.delete_model_request
    import aws_sdk_lookoutequipment.types.delete_resource_policy_request
    import aws_sdk_lookoutequipment.types.delete_retraining_scheduler_request
    import aws_sdk_lookoutequipment.types.describe_data_ingestion_job_request
    import aws_sdk_lookoutequipment.types.describe_data_ingestion_job_response
    import aws_sdk_lookoutequipment.types.describe_dataset_request
    import aws_sdk_lookoutequipment.types.describe_dataset_response
    import aws_sdk_lookoutequipment.types.describe_inference_scheduler_request
    import aws_sdk_lookoutequipment.types.describe_inference_scheduler_response
    import aws_sdk_lookoutequipment.types.describe_label_group_request
    import aws_sdk_lookoutequipment.types.describe_label_group_response
    import aws_sdk_lookoutequipment.types.describe_label_request
    import aws_sdk_lookoutequipment.types.describe_label_response
    import aws_sdk_lookoutequipment.types.describe_model_request
    import aws_sdk_lookoutequipment.types.describe_model_response
    import aws_sdk_lookoutequipment.types.describe_model_version_request
    import aws_sdk_lookoutequipment.types.describe_model_version_response
    import aws_sdk_lookoutequipment.types.describe_resource_policy_request
    import aws_sdk_lookoutequipment.types.describe_resource_policy_response
    import aws_sdk_lookoutequipment.types.describe_retraining_scheduler_request
    import aws_sdk_lookoutequipment.types.describe_retraining_scheduler_response
    import aws_sdk_lookoutequipment.types.equipment
    import aws_sdk_lookoutequipment.types.fault_code
    import aws_sdk_lookoutequipment.types.fault_codes
    import aws_sdk_lookoutequipment.types.iam_role_arn
    import aws_sdk_lookoutequipment.types.idempotence_token
    import aws_sdk_lookoutequipment.types.import_dataset_request
    import aws_sdk_lookoutequipment.types.import_dataset_response
    import aws_sdk_lookoutequipment.types.import_model_version_request
    import aws_sdk_lookoutequipment.types.import_model_version_response
    import aws_sdk_lookoutequipment.types.inference_data_import_strategy
    import aws_sdk_lookoutequipment.types.inference_execution_status
    import aws_sdk_lookoutequipment.types.inference_input_configuration
    import aws_sdk_lookoutequipment.types.inference_output_configuration
    import aws_sdk_lookoutequipment.types.inference_scheduler_identifier
    import aws_sdk_lookoutequipment.types.inference_scheduler_name
    import aws_sdk_lookoutequipment.types.inference_scheduler_status
    import aws_sdk_lookoutequipment.types.ingestion_input_configuration
    import aws_sdk_lookoutequipment.types.ingestion_job_id
    import aws_sdk_lookoutequipment.types.ingestion_job_status
    import aws_sdk_lookoutequipment.types.label_group_name
    import aws_sdk_lookoutequipment.types.label_id
    import aws_sdk_lookoutequipment.types.label_rating
    import aws_sdk_lookoutequipment.types.labels_input_configuration
    import aws_sdk_lookoutequipment.types.list_data_ingestion_jobs_request
    import aws_sdk_lookoutequipment.types.list_data_ingestion_jobs_response
    import aws_sdk_lookoutequipment.types.list_datasets_request
    import aws_sdk_lookoutequipment.types.list_datasets_response
    import aws_sdk_lookoutequipment.types.list_inference_events_request
    import aws_sdk_lookoutequipment.types.list_inference_events_response
    import aws_sdk_lookoutequipment.types.list_inference_executions_request
    import aws_sdk_lookoutequipment.types.list_inference_executions_response
    import aws_sdk_lookoutequipment.types.list_inference_schedulers_request
    import aws_sdk_lookoutequipment.types.list_inference_schedulers_response
    import aws_sdk_lookoutequipment.types.list_label_groups_request
    import aws_sdk_lookoutequipment.types.list_label_groups_response
    import aws_sdk_lookoutequipment.types.list_labels_request
    import aws_sdk_lookoutequipment.types.list_labels_response
    import aws_sdk_lookoutequipment.types.list_model_versions_request
    import aws_sdk_lookoutequipment.types.list_model_versions_response
    import aws_sdk_lookoutequipment.types.list_models_request
    import aws_sdk_lookoutequipment.types.list_models_response
    import aws_sdk_lookoutequipment.types.list_retraining_schedulers_request
    import aws_sdk_lookoutequipment.types.list_retraining_schedulers_response
    import aws_sdk_lookoutequipment.types.list_sensor_statistics_request
    import aws_sdk_lookoutequipment.types.list_sensor_statistics_response
    import aws_sdk_lookoutequipment.types.list_tags_for_resource_request
    import aws_sdk_lookoutequipment.types.list_tags_for_resource_response
    import aws_sdk_lookoutequipment.types.lookback_window
    import aws_sdk_lookoutequipment.types.max_results
    import aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.model_promote_mode
    import aws_sdk_lookoutequipment.types.model_status
    import aws_sdk_lookoutequipment.types.model_version
    import aws_sdk_lookoutequipment.types.model_version_arn
    import aws_sdk_lookoutequipment.types.model_version_source_type
    import aws_sdk_lookoutequipment.types.model_version_status
    import aws_sdk_lookoutequipment.types.name_or_arn
    import aws_sdk_lookoutequipment.types.next_token
    import aws_sdk_lookoutequipment.types.off_condition
    import aws_sdk_lookoutequipment.types.policy
    import aws_sdk_lookoutequipment.types.policy_revision_id
    import aws_sdk_lookoutequipment.types.put_resource_policy_request
    import aws_sdk_lookoutequipment.types.put_resource_policy_response
    import aws_sdk_lookoutequipment.types.resource_arn
    import aws_sdk_lookoutequipment.types.retraining_frequency
    import aws_sdk_lookoutequipment.types.retraining_scheduler_status
    import aws_sdk_lookoutequipment.types.start_data_ingestion_job_request
    import aws_sdk_lookoutequipment.types.start_data_ingestion_job_response
    import aws_sdk_lookoutequipment.types.start_inference_scheduler_request
    import aws_sdk_lookoutequipment.types.start_inference_scheduler_response
    import aws_sdk_lookoutequipment.types.start_retraining_scheduler_request
    import aws_sdk_lookoutequipment.types.start_retraining_scheduler_response
    import aws_sdk_lookoutequipment.types.stop_inference_scheduler_request
    import aws_sdk_lookoutequipment.types.stop_inference_scheduler_response
    import aws_sdk_lookoutequipment.types.stop_retraining_scheduler_request
    import aws_sdk_lookoutequipment.types.stop_retraining_scheduler_response
    import aws_sdk_lookoutequipment.types.tag_key_list
    import aws_sdk_lookoutequipment.types.tag_list
    import aws_sdk_lookoutequipment.types.tag_resource_request
    import aws_sdk_lookoutequipment.types.tag_resource_response
    import aws_sdk_lookoutequipment.types.timestamp
    import aws_sdk_lookoutequipment.types.untag_resource_request
    import aws_sdk_lookoutequipment.types.untag_resource_response
    import aws_sdk_lookoutequipment.types.update_active_model_version_request
    import aws_sdk_lookoutequipment.types.update_active_model_version_response
    import aws_sdk_lookoutequipment.types.update_inference_scheduler_request
    import aws_sdk_lookoutequipment.types.update_label_group_request
    import aws_sdk_lookoutequipment.types.update_model_request
    import aws_sdk_lookoutequipment.types.update_retraining_scheduler_request


class AsyncLookoutEquipmentClientConfig(TypedDict, total=False):
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


class AsyncLookoutEquipmentClient:
    """A client for the ``LookoutEquipment`` service.

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
        self._config = AsyncLookoutEquipmentClientConfig(
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
        self, config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncLookoutEquipmentClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def create_dataset(
        self,
        dataset_name: "aws_sdk_lookoutequipment.types.dataset_name.DatasetName",
        client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        dataset_schema: Optional[
            "aws_sdk_lookoutequipment.types.dataset_schema.DatasetSchema"
        ] = None,
        server_side_kms_key_id: Optional[
            "aws_sdk_lookoutequipment.types.name_or_arn.NameOrArn"
        ] = None,
        tags: Optional["aws_sdk_lookoutequipment.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_lookoutequipment.types.create_dataset_response.CreateDatasetResponse":
        """<p>Creates a container for a collection of data being ingested for analysis. The dataset contains the metadata describing where the data is and what the data actually looks like. For example, it contains the location of the data source, the data schema, and other information. A dataset also contains any tags associated with the ingested data. </p>

        Args:
            dataset_name: <p>The name of the dataset being created. </p>
            dataset_schema: <p>A JSON description of the data that is in each time series dataset, including names, column names, and data types. </p>
            server_side_kms_key_id: <p>Provides the identifier of the KMS key used to encrypt dataset data by Amazon Lookout for Equipment. </p>
            client_token: <p> A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
            tags: <p>Any tags associated with the ingested data described in the dataset. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.create_dataset_request.CreateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_dataset.async_create_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.create_dataset_request.CreateDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_name"] = dataset_name
        if dataset_schema is not None:
            input_["dataset_schema"] = dataset_schema
        if server_side_kms_key_id is not None:
            input_["server_side_kms_key_id"] = server_side_kms_key_id
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_inference_scheduler(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        inference_scheduler_name: "aws_sdk_lookoutequipment.types.inference_scheduler_name.InferenceSchedulerName",
        data_upload_frequency: "aws_sdk_lookoutequipment.types.data_upload_frequency.DataUploadFrequency",
        data_input_configuration: "aws_sdk_lookoutequipment.types.inference_input_configuration.InferenceInputConfiguration",
        data_output_configuration: "aws_sdk_lookoutequipment.types.inference_output_configuration.InferenceOutputConfiguration",
        role_arn: "aws_sdk_lookoutequipment.types.iam_role_arn.IamRoleArn",
        client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        data_delay_offset_in_minutes: Optional[
            "aws_sdk_lookoutequipment.types.data_delay_offset_in_minutes.DataDelayOffsetInMinutes"
        ] = None,
        server_side_kms_key_id: Optional[
            "aws_sdk_lookoutequipment.types.name_or_arn.NameOrArn"
        ] = None,
        tags: Optional["aws_sdk_lookoutequipment.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_lookoutequipment.types.create_inference_scheduler_response.CreateInferenceSchedulerResponse":
        r"""<p> Creates a scheduled inference. Scheduling an inference is setting up a continuous real-time inference plan to analyze new measurement data. When setting up the schedule, you provide an S3 bucket location for the input data, assign it a delimiter between separate entries in the data, set an offset delay if desired, and set the frequency of inferencing. You must also provide an S3 bucket location for the output data. </p>

        Args:
            model_name: <p>The name of the previously trained machine learning model being used to create the inference scheduler. </p>
            inference_scheduler_name: <p>The name of the inference scheduler being created. </p>
            data_delay_offset_in_minutes: <p>The interval (in minutes) of planned delay at the start of each inference segment. For example, if inference is set to run every ten minutes, the delay is set to five minutes and the time is 09:08. The inference scheduler will wake up at the configured interval (which, without a delay configured, would be 09:10) plus the additional five minute delay time (so 09:15) to check your Amazon S3 bucket. The delay provides a buffer for you to upload data at the same frequency, so that you don't have to stop and restart the scheduler when uploading new data.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-inference-process.html\">Understanding the inference process</a>.</p>
            data_upload_frequency: <p> How often data is uploaded to the source Amazon S3 bucket for the input data. The value chosen is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment runs inference on your data.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-inference-process.html\">Understanding the inference process</a>.</p>
            data_input_configuration: <p>Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location. </p>
            data_output_configuration: <p>Specifies configuration information for the output results for the inference scheduler, including the S3 location for the output. </p>
            role_arn: <p>The Amazon Resource Name (ARN) of a role with permission to access the data source being used for the inference. </p>
            server_side_kms_key_id: <p>Provides the identifier of the KMS key used to encrypt inference scheduler data by Amazon Lookout for Equipment. </p>
            client_token: <p> A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
            tags: <p>Any tags associated with the inference scheduler. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.create_inference_scheduler_request.CreateInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.create_inference_scheduler_response.CreateInferenceSchedulerResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_inference_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_inference_scheduler.async_create_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.create_inference_scheduler_request.CreateInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name
        input_["inference_scheduler_name"] = inference_scheduler_name
        if data_delay_offset_in_minutes is not None:
            input_["data_delay_offset_in_minutes"] = data_delay_offset_in_minutes
        input_["data_upload_frequency"] = data_upload_frequency
        input_["data_input_configuration"] = data_input_configuration
        input_["data_output_configuration"] = data_output_configuration
        input_["role_arn"] = role_arn
        if server_side_kms_key_id is not None:
            input_["server_side_kms_key_id"] = server_side_kms_key_id
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_label(
        self,
        label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName",
        start_time: "aws_sdk_lookoutequipment.types.timestamp.Timestamp",
        end_time: "aws_sdk_lookoutequipment.types.timestamp.Timestamp",
        rating: "aws_sdk_lookoutequipment.types.label_rating.LabelRating",
        client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        fault_code: Optional[
            "aws_sdk_lookoutequipment.types.fault_code.FaultCode"
        ] = None,
        notes: Optional["aws_sdk_lookoutequipment.types.comments.Comments"] = None,
        equipment: Optional[
            "aws_sdk_lookoutequipment.types.equipment.Equipment"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.create_label_response.CreateLabelResponse":
        """<p> Creates a label for an event. </p>

        Args:
            label_group_name: <p> The name of a group of labels. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>
            start_time: <p> The start time of the labeled event. </p>
            end_time: <p> The end time of the labeled event. </p>
            rating: <p> Indicates whether a labeled event represents an anomaly. </p>
            fault_code: <p> Provides additional information about the label. The fault code must be defined in the FaultCodes attribute of the label group.</p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>
            notes: <p> Metadata providing additional information about the label. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>
            equipment: <p> Indicates that a label pertains to a particular piece of equipment. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>
            client_token: <p> A unique identifier for the request to create a label. If you do not set the client request token, Lookout for Equipment generates one. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.create_label_request.CreateLabelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.create_label_response.CreateLabelResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_label

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_label.async_create_label(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.create_label_request.CreateLabelRequest = {}  # type: ignore[typeddict-item]
        input_["label_group_name"] = label_group_name
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        input_["rating"] = rating
        if fault_code is not None:
            input_["fault_code"] = fault_code
        if notes is not None:
            input_["notes"] = notes
        if equipment is not None:
            input_["equipment"] = equipment
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_label_group(
        self,
        label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName",
        client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        fault_codes: Optional[
            "aws_sdk_lookoutequipment.types.fault_codes.FaultCodes"
        ] = None,
        tags: Optional["aws_sdk_lookoutequipment.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_lookoutequipment.types.create_label_group_response.CreateLabelGroupResponse":
        """<p> Creates a group of labels. </p>

        Args:
            label_group_name: <p> Names a group of labels.</p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>
            fault_codes: <p> The acceptable fault codes (indicating the type of anomaly associated with the label) that can be used with this label group.</p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>
            client_token: <p> A unique identifier for the request to create a label group. If you do not set the client request token, Lookout for Equipment generates one. </p>
            tags: <p> Tags that provide metadata about the label group you are creating. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.create_label_group_request.CreateLabelGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.create_label_group_response.CreateLabelGroupResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_label_group

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_label_group.async_create_label_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.create_label_group_request.CreateLabelGroupRequest = {}  # type: ignore[typeddict-item]
        input_["label_group_name"] = label_group_name
        if fault_codes is not None:
            input_["fault_codes"] = fault_codes
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_model(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        dataset_name: "aws_sdk_lookoutequipment.types.dataset_identifier.DatasetIdentifier",
        client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        dataset_schema: Optional[
            "aws_sdk_lookoutequipment.types.dataset_schema.DatasetSchema"
        ] = None,
        labels_input_configuration: Optional[
            "aws_sdk_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
        ] = None,
        training_data_start_time: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        training_data_end_time: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        evaluation_data_start_time: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        evaluation_data_end_time: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        role_arn: Optional[
            "aws_sdk_lookoutequipment.types.iam_role_arn.IamRoleArn"
        ] = None,
        data_pre_processing_configuration: Optional[
            "aws_sdk_lookoutequipment.types.data_pre_processing_configuration.DataPreProcessingConfiguration"
        ] = None,
        server_side_kms_key_id: Optional[
            "aws_sdk_lookoutequipment.types.name_or_arn.NameOrArn"
        ] = None,
        tags: Optional["aws_sdk_lookoutequipment.types.tag_list.TagList"] = None,
        off_condition: Optional[
            "aws_sdk_lookoutequipment.types.off_condition.OffCondition"
        ] = None,
        model_diagnostics_output_configuration: Optional[
            "aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration.ModelDiagnosticsOutputConfiguration"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.create_model_response.CreateModelResponse":
        r"""<p>Creates a machine learning model for data inference. </p> <p>A machine-learning (ML) model is a mathematical model that finds patterns in your data. In Amazon Lookout for Equipment, the model learns the patterns of normal behavior and detects abnormal behavior that could be potential equipment failure (or maintenance events). The models are made by analyzing normal data and abnormalities in machine behavior that have already occurred.</p> <p>Your model is trained using a portion of the data from your dataset and uses that data to learn patterns of normal behavior and abnormal patterns that lead to equipment failure. Another portion of the data is used to evaluate the model's accuracy. </p>

        Args:
            model_name: <p>The name for the machine learning model to be created.</p>
            dataset_name: <p>The name of the dataset for the machine learning model being created. </p>
            dataset_schema: <p>The data schema for the machine learning model being created. </p>
            labels_input_configuration: <p>The input configuration for the labels being used for the machine learning model that's being created. </p>
            client_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
            training_data_start_time: <p>Indicates the time reference in the dataset that should be used to begin the subset of training data for the machine learning model. </p>
            training_data_end_time: <p>Indicates the time reference in the dataset that should be used to end the subset of training data for the machine learning model. </p>
            evaluation_data_start_time: <p>Indicates the time reference in the dataset that should be used to begin the subset of evaluation data for the machine learning model. </p>
            evaluation_data_end_time: <p> Indicates the time reference in the dataset that should be used to end the subset of evaluation data for the machine learning model. </p>
            role_arn: <p> The Amazon Resource Name (ARN) of a role with permission to access the data source being used to create the machine learning model. </p>
            data_pre_processing_configuration: <p>The configuration is the <code>TargetSamplingRate</code>, which is the sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been collected at a 1 second level and you want the system to resample the data at a 1 minute rate before training, the <code>TargetSamplingRate</code> is 1 minute.</p> <p>When providing a value for the <code>TargetSamplingRate</code>, you must attach the prefix \"PT\" to the rate you want. The value for a 1 second rate is therefore <i>PT1S</i>, the value for a 15 minute rate is <i>PT15M</i>, and the value for a 1 hour rate is <i>PT1H</i> </p>
            server_side_kms_key_id: <p>Provides the identifier of the KMS key used to encrypt model data by Amazon Lookout for Equipment. </p>
            tags: <p> Any tags associated with the machine learning model being created. </p>
            off_condition: <p>Indicates that the asset associated with this sensor has been shut off. As long as this condition is met, Lookout for Equipment will not use data from this asset for training, evaluation, or inference.</p>
            model_diagnostics_output_configuration: <p>The Amazon S3 location where you want Amazon Lookout for Equipment to save the pointwise model diagnostics. You must also specify the <code>RoleArn</code> request parameter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.create_model_request.CreateModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.create_model_response.CreateModelResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_model

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_model.async_create_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.create_model_request.CreateModelRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name
        input_["dataset_name"] = dataset_name
        if dataset_schema is not None:
            input_["dataset_schema"] = dataset_schema
        if labels_input_configuration is not None:
            input_["labels_input_configuration"] = labels_input_configuration
        input_["client_token"] = client_token
        if training_data_start_time is not None:
            input_["training_data_start_time"] = training_data_start_time
        if training_data_end_time is not None:
            input_["training_data_end_time"] = training_data_end_time
        if evaluation_data_start_time is not None:
            input_["evaluation_data_start_time"] = evaluation_data_start_time
        if evaluation_data_end_time is not None:
            input_["evaluation_data_end_time"] = evaluation_data_end_time
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if data_pre_processing_configuration is not None:
            input_["data_pre_processing_configuration"] = (
                data_pre_processing_configuration
            )
        if server_side_kms_key_id is not None:
            input_["server_side_kms_key_id"] = server_side_kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if off_condition is not None:
            input_["off_condition"] = off_condition
        if model_diagnostics_output_configuration is not None:
            input_["model_diagnostics_output_configuration"] = (
                model_diagnostics_output_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_retraining_scheduler(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        retraining_frequency: "aws_sdk_lookoutequipment.types.retraining_frequency.RetrainingFrequency",
        lookback_window: "aws_sdk_lookoutequipment.types.lookback_window.LookbackWindow",
        client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        retraining_start_date: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        promote_mode: Optional[
            "aws_sdk_lookoutequipment.types.model_promote_mode.ModelPromoteMode"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.create_retraining_scheduler_response.CreateRetrainingSchedulerResponse":
        r"""<p>Creates a retraining scheduler on the specified model. </p>

        Args:
            model_name: <p>The name of the model to add the retraining scheduler to. </p>
            retraining_start_date: <p>The start date for the retraining scheduler. Lookout for Equipment truncates the time you provide to the nearest UTC day.</p>
            retraining_frequency: <p>This parameter uses the <a href=\"https://en.wikipedia.org/wiki/ISO_8601#Durations\">ISO 8601</a> standard to set the frequency at which you want retraining to occur in terms of Years, Months, and/or Days (note: other parameters like Time are not currently supported). The minimum value is 30 days (P30D) and the maximum value is 1 year (P1Y). For example, the following values are valid:</p> <ul> <li> <p>P3M15D – Every 3 months and 15 days</p> </li> <li> <p>P2M – Every 2 months</p> </li> <li> <p>P150D – Every 150 days</p> </li> </ul>
            lookback_window: <p>The number of past days of data that will be used for retraining.</p>
            promote_mode: <p>Indicates how the service will use new models. In <code>MANAGED</code> mode, new models will automatically be used for inference if they have better performance than the current model. In <code>MANUAL</code> mode, the new models will not be used <a href=\"https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/versioning-model.html#model-activation\">until they are manually activated</a>.</p>
            client_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>

        Examples:
            Creates a retraining scheduler with a specific start date

            >>> await client.create_retraining_scheduler(model_name='sample-model', retraining_start_date='2024-01-01T00:00:00Z', retraining_frequency='P1M', lookback_window='P360D', client_token='sample-client-token')
            Creates a retraining scheduler with manual promote mode

            >>> await client.create_retraining_scheduler(model_name='sample-model', retraining_frequency='P1M', lookback_window='P360D', promote_mode='MANUAL', client_token='sample-client-token')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.create_retraining_scheduler_request.CreateRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.create_retraining_scheduler_response.CreateRetrainingSchedulerResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_retraining_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.create_retraining_scheduler.async_create_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.create_retraining_scheduler_request.CreateRetrainingSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name
        if retraining_start_date is not None:
            input_["retraining_start_date"] = retraining_start_date
        input_["retraining_frequency"] = retraining_frequency
        input_["lookback_window"] = lookback_window
        if promote_mode is not None:
            input_["promote_mode"] = promote_mode
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_dataset(
        self,
        dataset_name: "aws_sdk_lookoutequipment.types.dataset_identifier.DatasetIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p> Deletes a dataset and associated artifacts. The operation will check to see if any inference scheduler or data ingestion job is currently using the dataset, and if there isn't, the dataset, its metadata, and any associated data stored in S3 will be deleted. This does not affect any models that used this dataset for training and evaluation, but does prevent it from being used in the future. </p>

        Args:
            dataset_name: <p>The name of the dataset to be deleted. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_dataset.async_delete_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.delete_dataset_request.DeleteDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_name"] = dataset_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_inference_scheduler(
        self,
        inference_scheduler_name: "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p>Deletes an inference scheduler that has been set up. Prior inference results will not be deleted.</p>

        Args:
            inference_scheduler_name: <p>The name of the inference scheduler to be deleted. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.delete_inference_scheduler_request.DeleteInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_inference_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_inference_scheduler.async_delete_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.delete_inference_scheduler_request.DeleteInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["inference_scheduler_name"] = inference_scheduler_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_label(
        self,
        label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName",
        label_id: "aws_sdk_lookoutequipment.types.label_id.LabelId",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p> Deletes a label. </p>

        Args:
            label_group_name: <p> The name of the label group that contains the label that you want to delete. Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>
            label_id: <p> The ID of the label that you want to delete. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.delete_label_request.DeleteLabelRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_label

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_label.async_delete_label(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.delete_label_request.DeleteLabelRequest = {}  # type: ignore[typeddict-item]
        input_["label_group_name"] = label_group_name
        input_["label_id"] = label_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_label_group(
        self,
        label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p> Deletes a group of labels. </p>

        Args:
            label_group_name: <p> The name of the label group that you want to delete. Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.delete_label_group_request.DeleteLabelGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_label_group

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_label_group.async_delete_label_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.delete_label_group_request.DeleteLabelGroupRequest = {}  # type: ignore[typeddict-item]
        input_["label_group_name"] = label_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_model(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p>Deletes a machine learning model currently available for Amazon Lookout for Equipment. This will prevent it from being used with an inference scheduler, even one that is already set up. </p>

        Args:
            model_name: <p>The name of the machine learning model to be deleted. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.delete_model_request.DeleteModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_model

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_model.async_delete_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.delete_model_request.DeleteModelRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_lookoutequipment.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p>Deletes the resource policy attached to the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which the resource policy should be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_retraining_scheduler(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> None:
        """<p>Deletes a retraining scheduler from a model. The retraining scheduler must be in the <code>STOPPED</code> status. </p>

        Args:
            model_name: <p>The name of the model whose retraining scheduler you want to delete. </p>

        Examples:
            Deletes a retraining scheduler

            >>> await client.delete_retraining_scheduler(model_name='sample-model')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.delete_retraining_scheduler_request.DeleteRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_retraining_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.delete_retraining_scheduler.async_delete_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.delete_retraining_scheduler_request.DeleteRetrainingSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_data_ingestion_job(
        self,
        job_id: "aws_sdk_lookoutequipment.types.ingestion_job_id.IngestionJobId",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.describe_data_ingestion_job_response.DescribeDataIngestionJobResponse":
        """<p>Provides information on a specific data ingestion job such as creation time, dataset ARN, and status.</p>

        Args:
            job_id: <p>The job ID of the data ingestion job. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.describe_data_ingestion_job_request.DescribeDataIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.describe_data_ingestion_job_response.DescribeDataIngestionJobResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_data_ingestion_job

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_data_ingestion_job.async_describe_data_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.describe_data_ingestion_job_request.DescribeDataIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input_["job_id"] = job_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_dataset(
        self,
        dataset_name: "aws_sdk_lookoutequipment.types.dataset_identifier.DatasetIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.describe_dataset_response.DescribeDatasetResponse":
        """<p>Provides a JSON description of the data in each time series dataset, including names, column names, and data types.</p>

        Args:
            dataset_name: <p>The name of the dataset to be described. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.describe_dataset_request.DescribeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.describe_dataset_response.DescribeDatasetResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_dataset.async_describe_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.describe_dataset_request.DescribeDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_name"] = dataset_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_inference_scheduler(
        self,
        inference_scheduler_name: "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.describe_inference_scheduler_response.DescribeInferenceSchedulerResponse":
        """<p> Specifies information about the inference scheduler being used, including name, model, status, and associated metadata </p>

        Args:
            inference_scheduler_name: <p>The name of the inference scheduler being described. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.describe_inference_scheduler_request.DescribeInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.describe_inference_scheduler_response.DescribeInferenceSchedulerResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_inference_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_inference_scheduler.async_describe_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.describe_inference_scheduler_request.DescribeInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["inference_scheduler_name"] = inference_scheduler_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_label(
        self,
        label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName",
        label_id: "aws_sdk_lookoutequipment.types.label_id.LabelId",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.describe_label_response.DescribeLabelResponse":
        """<p> Returns the name of the label. </p>

        Args:
            label_group_name: <p> Returns the name of the group containing the label. </p>
            label_id: <p> Returns the ID of the label. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.describe_label_request.DescribeLabelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.describe_label_response.DescribeLabelResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_label

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_label.async_describe_label(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.describe_label_request.DescribeLabelRequest = {}  # type: ignore[typeddict-item]
        input_["label_group_name"] = label_group_name
        input_["label_id"] = label_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_label_group(
        self,
        label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.describe_label_group_response.DescribeLabelGroupResponse":
        """<p> Returns information about the label group. </p>

        Args:
            label_group_name: <p> Returns the name of the label group. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.describe_label_group_request.DescribeLabelGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.describe_label_group_response.DescribeLabelGroupResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_label_group

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_label_group.async_describe_label_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.describe_label_group_request.DescribeLabelGroupRequest = {}  # type: ignore[typeddict-item]
        input_["label_group_name"] = label_group_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_model(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.describe_model_response.DescribeModelResponse":
        """<p>Provides a JSON containing the overall information about a specific machine learning model, including model name and ARN, dataset, training and evaluation information, status, and so on. </p>

        Args:
            model_name: <p>The name of the machine learning model to be described. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.describe_model_request.DescribeModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.describe_model_response.DescribeModelResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_model

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_model.async_describe_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.describe_model_request.DescribeModelRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_model_version(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        model_version: "aws_sdk_lookoutequipment.types.model_version.ModelVersion",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.describe_model_version_response.DescribeModelVersionResponse":
        """<p>Retrieves information about a specific machine learning model version.</p>

        Args:
            model_name: <p>The name of the machine learning model that this version belongs to.</p>
            model_version: <p>The version of the machine learning model.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.describe_model_version_request.DescribeModelVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.describe_model_version_response.DescribeModelVersionResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_model_version

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_model_version.async_describe_model_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.describe_model_version_request.DescribeModelVersionRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name
        input_["model_version"] = model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_resource_policy(
        self,
        resource_arn: "aws_sdk_lookoutequipment.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.describe_resource_policy_response.DescribeResourcePolicyResponse":
        """<p>Provides the details of a resource policy attached to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that is associated with the resource policy.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.describe_resource_policy_request.DescribeResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.describe_resource_policy_response.DescribeResourcePolicyResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_resource_policy.async_describe_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.describe_resource_policy_request.DescribeResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_retraining_scheduler(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.describe_retraining_scheduler_response.DescribeRetrainingSchedulerResponse":
        """<p>Provides a description of the retraining scheduler, including information such as the model name and retraining parameters. </p>

        Args:
            model_name: <p>The name of the model that the retraining scheduler is attached to. </p>

        Examples:
            Describes a retraining scheduler

            >>> await client.describe_retraining_scheduler(model_name='sample-model')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.describe_retraining_scheduler_request.DescribeRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.describe_retraining_scheduler_response.DescribeRetrainingSchedulerResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_retraining_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.describe_retraining_scheduler.async_describe_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.describe_retraining_scheduler_request.DescribeRetrainingSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_dataset(
        self,
        source_dataset_arn: "aws_sdk_lookoutequipment.types.dataset_arn.DatasetArn",
        client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        dataset_name: Optional[
            "aws_sdk_lookoutequipment.types.dataset_name.DatasetName"
        ] = None,
        server_side_kms_key_id: Optional[
            "aws_sdk_lookoutequipment.types.name_or_arn.NameOrArn"
        ] = None,
        tags: Optional["aws_sdk_lookoutequipment.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_lookoutequipment.types.import_dataset_response.ImportDatasetResponse":
        """<p>Imports a dataset.</p>

        Args:
            source_dataset_arn: <p>The Amazon Resource Name (ARN) of the dataset to import.</p>
            dataset_name: <p>The name of the machine learning dataset to be created. If the dataset already exists, Amazon Lookout for Equipment overwrites the existing dataset. If you don't specify this field, it is filled with the name of the source dataset.</p>
            client_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
            server_side_kms_key_id: <p>Provides the identifier of the KMS key key used to encrypt model data by Amazon Lookout for Equipment. </p>
            tags: <p>Any tags associated with the dataset to be created.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.import_dataset_request.ImportDatasetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.import_dataset_response.ImportDatasetResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.import_dataset

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.import_dataset.async_import_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.import_dataset_request.ImportDatasetRequest = {}  # type: ignore[typeddict-item]
        input_["source_dataset_arn"] = source_dataset_arn
        if dataset_name is not None:
            input_["dataset_name"] = dataset_name
        input_["client_token"] = client_token
        if server_side_kms_key_id is not None:
            input_["server_side_kms_key_id"] = server_side_kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_model_version(
        self,
        source_model_version_arn: "aws_sdk_lookoutequipment.types.model_version_arn.ModelVersionArn",
        dataset_name: "aws_sdk_lookoutequipment.types.dataset_identifier.DatasetIdentifier",
        client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        model_name: Optional[
            "aws_sdk_lookoutequipment.types.model_name.ModelName"
        ] = None,
        labels_input_configuration: Optional[
            "aws_sdk_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
        ] = None,
        role_arn: Optional[
            "aws_sdk_lookoutequipment.types.iam_role_arn.IamRoleArn"
        ] = None,
        server_side_kms_key_id: Optional[
            "aws_sdk_lookoutequipment.types.name_or_arn.NameOrArn"
        ] = None,
        tags: Optional["aws_sdk_lookoutequipment.types.tag_list.TagList"] = None,
        inference_data_import_strategy: Optional[
            "aws_sdk_lookoutequipment.types.inference_data_import_strategy.InferenceDataImportStrategy"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.import_model_version_response.ImportModelVersionResponse":
        """<p>Imports a model that has been trained successfully.</p>

        Args:
            source_model_version_arn: <p>The Amazon Resource Name (ARN) of the model version to import.</p>
            model_name: <p>The name for the machine learning model to be created. If the model already exists, Amazon Lookout for Equipment creates a new version. If you do not specify this field, it is filled with the name of the source model.</p>
            dataset_name: <p>The name of the dataset for the machine learning model being imported. </p>
            client_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
            role_arn: <p>The Amazon Resource Name (ARN) of a role with permission to access the data source being used to create the machine learning model. </p>
            server_side_kms_key_id: <p>Provides the identifier of the KMS key key used to encrypt model data by Amazon Lookout for Equipment. </p>
            tags: <p>The tags associated with the machine learning model to be created. </p>
            inference_data_import_strategy: <p>Indicates how to import the accumulated inference data when a model version is imported. The possible values are as follows:</p> <ul> <li> <p>NO_IMPORT – Don't import the data.</p> </li> <li> <p>ADD_WHEN_EMPTY – Only import the data from the source model if there is no existing data in the target model.</p> </li> <li> <p>OVERWRITE – Import the data from the source model and overwrite the existing data in the target model.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.import_model_version_request.ImportModelVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.import_model_version_response.ImportModelVersionResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.import_model_version

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.import_model_version.async_import_model_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.import_model_version_request.ImportModelVersionRequest = {}  # type: ignore[typeddict-item]
        input_["source_model_version_arn"] = source_model_version_arn
        if model_name is not None:
            input_["model_name"] = model_name
        input_["dataset_name"] = dataset_name
        if labels_input_configuration is not None:
            input_["labels_input_configuration"] = labels_input_configuration
        input_["client_token"] = client_token
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if server_side_kms_key_id is not None:
            input_["server_side_kms_key_id"] = server_side_kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if inference_data_import_strategy is not None:
            input_["inference_data_import_strategy"] = inference_data_import_strategy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_data_ingestion_jobs(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        dataset_name: Optional[
            "aws_sdk_lookoutequipment.types.dataset_name.DatasetName"
        ] = None,
        next_token: Optional[
            "aws_sdk_lookoutequipment.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        status: Optional[
            "aws_sdk_lookoutequipment.types.ingestion_job_status.IngestionJobStatus"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_data_ingestion_jobs_response.ListDataIngestionJobsResponse":
        """<p>Provides a list of all data ingestion jobs, including dataset name and ARN, S3 location of the input data, status, and so on. </p>

        Args:
            dataset_name: <p>The name of the dataset being used for the data ingestion job. </p>
            next_token: <p>An opaque pagination token indicating where to continue the listing of data ingestion jobs. </p>
            max_results: <p> Specifies the maximum number of data ingestion jobs to list. </p>
            status: <p>Indicates the status of the data ingestion job. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_data_ingestion_jobs_request.ListDataIngestionJobsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_data_ingestion_jobs_response.ListDataIngestionJobsResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_data_ingestion_jobs

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_data_ingestion_jobs.async_list_data_ingestion_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_data_ingestion_jobs_request.ListDataIngestionJobsRequest = {}  # type: ignore[typeddict-item]
        if dataset_name is not None:
            input_["dataset_name"] = dataset_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional[
            "aws_sdk_lookoutequipment.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        dataset_name_begins_with: Optional[
            "aws_sdk_lookoutequipment.types.dataset_name.DatasetName"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_datasets_response.ListDatasetsResponse":
        """<p>Lists all datasets currently available in your account, filtering on the dataset name. </p>

        Args:
            next_token: <p> An opaque pagination token indicating where to continue the listing of datasets. </p>
            max_results: <p> Specifies the maximum number of datasets to list. </p>
            dataset_name_begins_with: <p>The beginning of the name of the datasets to be listed. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_datasets_request.ListDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_datasets

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_datasets.async_list_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_datasets_request.ListDatasetsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if dataset_name_begins_with is not None:
            input_["dataset_name_begins_with"] = dataset_name_begins_with

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_inference_events(
        self,
        inference_scheduler_name: "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        interval_start_time: "aws_sdk_lookoutequipment.types.timestamp.Timestamp",
        interval_end_time: "aws_sdk_lookoutequipment.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional[
            "aws_sdk_lookoutequipment.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_inference_events_response.ListInferenceEventsResponse":
        """<p> Lists all inference events that have been found for the specified inference scheduler. </p>

        Args:
            next_token: <p>An opaque pagination token indicating where to continue the listing of inference events.</p>
            max_results: <p>Specifies the maximum number of inference events to list. </p>
            inference_scheduler_name: <p>The name of the inference scheduler for the inference events listed. </p>
            interval_start_time: <p> Lookout for Equipment will return all the inference events with an end time equal to or greater than the start time given.</p>
            interval_end_time: <p>Returns all the inference events with an end start time equal to or greater than less than the end time given.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_inference_events_request.ListInferenceEventsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_inference_events_response.ListInferenceEventsResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_events

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_events.async_list_inference_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_inference_events_request.ListInferenceEventsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["inference_scheduler_name"] = inference_scheduler_name
        input_["interval_start_time"] = interval_start_time
        input_["interval_end_time"] = interval_end_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_inference_executions(
        self,
        inference_scheduler_name: "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional[
            "aws_sdk_lookoutequipment.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        data_start_time_after: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        data_end_time_before: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        status: Optional[
            "aws_sdk_lookoutequipment.types.inference_execution_status.InferenceExecutionStatus"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_inference_executions_response.ListInferenceExecutionsResponse":
        """<p> Lists all inference executions that have been performed by the specified inference scheduler. </p>

        Args:
            next_token: <p>An opaque pagination token indicating where to continue the listing of inference executions.</p>
            max_results: <p>Specifies the maximum number of inference executions to list. </p>
            inference_scheduler_name: <p>The name of the inference scheduler for the inference execution listed. </p>
            data_start_time_after: <p>The time reference in the inferenced dataset after which Amazon Lookout for Equipment started the inference execution. </p>
            data_end_time_before: <p>The time reference in the inferenced dataset before which Amazon Lookout for Equipment stopped the inference execution. </p>
            status: <p>The status of the inference execution. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_inference_executions_request.ListInferenceExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_inference_executions_response.ListInferenceExecutionsResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_executions

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_executions.async_list_inference_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_inference_executions_request.ListInferenceExecutionsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        input_["inference_scheduler_name"] = inference_scheduler_name
        if data_start_time_after is not None:
            input_["data_start_time_after"] = data_start_time_after
        if data_end_time_before is not None:
            input_["data_end_time_before"] = data_end_time_before
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_inference_schedulers(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional[
            "aws_sdk_lookoutequipment.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        inference_scheduler_name_begins_with: Optional[
            "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
        ] = None,
        model_name: Optional[
            "aws_sdk_lookoutequipment.types.model_name.ModelName"
        ] = None,
        status: Optional[
            "aws_sdk_lookoutequipment.types.inference_scheduler_status.InferenceSchedulerStatus"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_inference_schedulers_response.ListInferenceSchedulersResponse":
        """<p>Retrieves a list of all inference schedulers currently available for your account. </p>

        Args:
            next_token: <p> An opaque pagination token indicating where to continue the listing of inference schedulers. </p>
            max_results: <p> Specifies the maximum number of inference schedulers to list. </p>
            inference_scheduler_name_begins_with: <p>The beginning of the name of the inference schedulers to be listed. </p>
            model_name: <p>The name of the machine learning model used by the inference scheduler to be listed. </p>
            status: <p>Specifies the current status of the inference schedulers.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_inference_schedulers_request.ListInferenceSchedulersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_inference_schedulers_response.ListInferenceSchedulersResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_schedulers

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_inference_schedulers.async_list_inference_schedulers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_inference_schedulers_request.ListInferenceSchedulersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if inference_scheduler_name_begins_with is not None:
            input_["inference_scheduler_name_begins_with"] = (
                inference_scheduler_name_begins_with
            )
        if model_name is not None:
            input_["model_name"] = model_name
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_label_groups(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        label_group_name_begins_with: Optional[
            "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName"
        ] = None,
        next_token: Optional[
            "aws_sdk_lookoutequipment.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_label_groups_response.ListLabelGroupsResponse":
        """<p> Returns a list of the label groups. </p>

        Args:
            label_group_name_begins_with: <p> The beginning of the name of the label groups to be listed. </p>
            next_token: <p> An opaque pagination token indicating where to continue the listing of label groups. </p>
            max_results: <p> Specifies the maximum number of label groups to list. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_label_groups_request.ListLabelGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_label_groups_response.ListLabelGroupsResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_label_groups

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_label_groups.async_list_label_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_label_groups_request.ListLabelGroupsRequest = {}  # type: ignore[typeddict-item]
        if label_group_name_begins_with is not None:
            input_["label_group_name_begins_with"] = label_group_name_begins_with
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

    async def list_labels(
        self,
        label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        interval_start_time: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        interval_end_time: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        fault_code: Optional[
            "aws_sdk_lookoutequipment.types.fault_code.FaultCode"
        ] = None,
        equipment: Optional[
            "aws_sdk_lookoutequipment.types.equipment.Equipment"
        ] = None,
        next_token: Optional[
            "aws_sdk_lookoutequipment.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_labels_response.ListLabelsResponse":
        """<p> Provides a list of labels. </p>

        Args:
            label_group_name: <p> Returns the name of the label group. </p>
            interval_start_time: <p> Returns all the labels with a end time equal to or later than the start time given. </p>
            interval_end_time: <p> Returns all labels with a start time earlier than the end time given. </p>
            fault_code: <p> Returns labels with a particular fault code. </p>
            equipment: <p> Lists the labels that pertain to a particular piece of equipment. </p>
            next_token: <p> An opaque pagination token indicating where to continue the listing of label groups. </p>
            max_results: <p> Specifies the maximum number of labels to list. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_labels_request.ListLabelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_labels_response.ListLabelsResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_labels

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_labels.async_list_labels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_labels_request.ListLabelsRequest = {}  # type: ignore[typeddict-item]
        input_["label_group_name"] = label_group_name
        if interval_start_time is not None:
            input_["interval_start_time"] = interval_start_time
        if interval_end_time is not None:
            input_["interval_end_time"] = interval_end_time
        if fault_code is not None:
            input_["fault_code"] = fault_code
        if equipment is not None:
            input_["equipment"] = equipment
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

    async def list_models(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional[
            "aws_sdk_lookoutequipment.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        status: Optional[
            "aws_sdk_lookoutequipment.types.model_status.ModelStatus"
        ] = None,
        model_name_begins_with: Optional[
            "aws_sdk_lookoutequipment.types.model_name.ModelName"
        ] = None,
        dataset_name_begins_with: Optional[
            "aws_sdk_lookoutequipment.types.dataset_name.DatasetName"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_models_response.ListModelsResponse":
        """<p>Generates a list of all models in the account, including model name and ARN, dataset, and status. </p>

        Args:
            next_token: <p> An opaque pagination token indicating where to continue the listing of machine learning models. </p>
            max_results: <p> Specifies the maximum number of machine learning models to list. </p>
            status: <p>The status of the machine learning model. </p>
            model_name_begins_with: <p>The beginning of the name of the machine learning models being listed. </p>
            dataset_name_begins_with: <p>The beginning of the name of the dataset of the machine learning models to be listed. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_models_request.ListModelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_models_response.ListModelsResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_models

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_models.async_list_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_models_request.ListModelsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status
        if model_name_begins_with is not None:
            input_["model_name_begins_with"] = model_name_begins_with
        if dataset_name_begins_with is not None:
            input_["dataset_name_begins_with"] = dataset_name_begins_with

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_model_versions(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        next_token: Optional[
            "aws_sdk_lookoutequipment.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        status: Optional[
            "aws_sdk_lookoutequipment.types.model_version_status.ModelVersionStatus"
        ] = None,
        source_type: Optional[
            "aws_sdk_lookoutequipment.types.model_version_source_type.ModelVersionSourceType"
        ] = None,
        created_at_end_time: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        created_at_start_time: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        max_model_version: Optional[
            "aws_sdk_lookoutequipment.types.model_version.ModelVersion"
        ] = None,
        min_model_version: Optional[
            "aws_sdk_lookoutequipment.types.model_version.ModelVersion"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_model_versions_response.ListModelVersionsResponse":
        """<p>Generates a list of all model versions for a given model, including the model version, model version ARN, and status. To list a subset of versions, use the <code>MaxModelVersion</code> and <code>MinModelVersion</code> fields.</p>

        Args:
            model_name: <p>Then name of the machine learning model for which the model versions are to be listed.</p>
            next_token: <p>If the total number of results exceeds the limit that the response can display, the response returns an opaque pagination token indicating where to continue the listing of machine learning model versions. Use this token in the <code>NextToken</code> field in the request to list the next page of results.</p>
            max_results: <p>Specifies the maximum number of machine learning model versions to list.</p>
            status: <p>Filter the results based on the current status of the model version.</p>
            source_type: <p>Filter the results based on the way the model version was generated.</p>
            created_at_end_time: <p>Filter results to return all the model versions created before this time.</p>
            created_at_start_time: <p>Filter results to return all the model versions created after this time.</p>
            max_model_version: <p>Specifies the highest version of the model to return in the list.</p>
            min_model_version: <p>Specifies the lowest version of the model to return in the list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_model_versions_request.ListModelVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_model_versions_response.ListModelVersionsResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_model_versions

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_model_versions.async_list_model_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_model_versions_request.ListModelVersionsRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status
        if source_type is not None:
            input_["source_type"] = source_type
        if created_at_end_time is not None:
            input_["created_at_end_time"] = created_at_end_time
        if created_at_start_time is not None:
            input_["created_at_start_time"] = created_at_start_time
        if max_model_version is not None:
            input_["max_model_version"] = max_model_version
        if min_model_version is not None:
            input_["min_model_version"] = min_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_retraining_schedulers(
        self,
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        model_name_begins_with: Optional[
            "aws_sdk_lookoutequipment.types.model_name.ModelName"
        ] = None,
        status: Optional[
            "aws_sdk_lookoutequipment.types.retraining_scheduler_status.RetrainingSchedulerStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_lookoutequipment.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_lookoutequipment.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_retraining_schedulers_response.ListRetrainingSchedulersResponse":
        """<p>Lists all retraining schedulers in your account, filtering by model name prefix and status. </p>

        Args:
            model_name_begins_with: <p>Specify this field to only list retraining schedulers whose machine learning models begin with the value you specify. </p>
            status: <p>Specify this field to only list retraining schedulers whose status matches the value you specify. </p>
            next_token: <p>If the number of results exceeds the maximum, a pagination token is returned. Use the token in the request to show the next page of retraining schedulers.</p>
            max_results: <p>Specifies the maximum number of retraining schedulers to list. </p>

        Examples:
            Listing retraining schedulers

            >>> await client.list_retraining_schedulers(max_results=50)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_retraining_schedulers_request.ListRetrainingSchedulersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_retraining_schedulers_response.ListRetrainingSchedulersResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_retraining_schedulers

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_retraining_schedulers.async_list_retraining_schedulers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_retraining_schedulers_request.ListRetrainingSchedulersRequest = {}  # type: ignore[typeddict-item]
        if model_name_begins_with is not None:
            input_["model_name_begins_with"] = model_name_begins_with
        if status is not None:
            input_["status"] = status
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

    async def list_sensor_statistics(
        self,
        dataset_name: "aws_sdk_lookoutequipment.types.dataset_name.DatasetName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        ingestion_job_id: Optional[
            "aws_sdk_lookoutequipment.types.ingestion_job_id.IngestionJobId"
        ] = None,
        max_results: Optional[
            "aws_sdk_lookoutequipment.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_lookoutequipment.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_sensor_statistics_response.ListSensorStatisticsResponse":
        """<p> Lists statistics about the data collected for each of the sensors that have been successfully ingested in the particular dataset. Can also be used to retreive Sensor Statistics for a previous ingestion job. </p>

        Args:
            dataset_name: <p> The name of the dataset associated with the list of Sensor Statistics. </p>
            ingestion_job_id: <p> The ingestion job id associated with the list of Sensor Statistics. To get sensor statistics for a particular ingestion job id, both dataset name and ingestion job id must be submitted as inputs. </p>
            max_results: <p>Specifies the maximum number of sensors for which to retrieve statistics. </p>
            next_token: <p>An opaque pagination token indicating where to continue the listing of sensor statistics. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_sensor_statistics_request.ListSensorStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_sensor_statistics_response.ListSensorStatisticsResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_sensor_statistics

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_sensor_statistics.async_list_sensor_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_sensor_statistics_request.ListSensorStatisticsRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_name"] = dataset_name
        if ingestion_job_id is not None:
            input_["ingestion_job_id"] = ingestion_job_id
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_lookoutequipment.types.amazon_resource_arn.AmazonResourceArn",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all the tags for a specified resource, including key and value. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource (such as the dataset or model) that is the focus of the <code>ListTagsForResource</code> operation. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "aws_sdk_lookoutequipment.types.resource_arn.ResourceArn",
        resource_policy: "aws_sdk_lookoutequipment.types.policy.Policy",
        client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        policy_revision_id: Optional[
            "aws_sdk_lookoutequipment.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> "aws_sdk_lookoutequipment.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Creates a resource control policy for a given resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which the policy is being created.</p>
            resource_policy: <p>The JSON-formatted resource policy to create.</p>
            policy_revision_id: <p>A unique identifier for a revision of the resource policy.</p>
            client_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.put_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["resource_policy"] = resource_policy
        if policy_revision_id is not None:
            input_["policy_revision_id"] = policy_revision_id
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_data_ingestion_job(
        self,
        dataset_name: "aws_sdk_lookoutequipment.types.dataset_identifier.DatasetIdentifier",
        ingestion_input_configuration: "aws_sdk_lookoutequipment.types.ingestion_input_configuration.IngestionInputConfiguration",
        role_arn: "aws_sdk_lookoutequipment.types.iam_role_arn.IamRoleArn",
        client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.start_data_ingestion_job_response.StartDataIngestionJobResponse":
        """<p>Starts a data ingestion job. Amazon Lookout for Equipment returns the job status. </p>

        Args:
            dataset_name: <p>The name of the dataset being used by the data ingestion job. </p>
            ingestion_input_configuration: <p> Specifies information for the input data for the data ingestion job, including dataset S3 location. </p>
            role_arn: <p> The Amazon Resource Name (ARN) of a role with permission to access the data source for the data ingestion job. </p>
            client_token: <p> A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.start_data_ingestion_job_request.StartDataIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.start_data_ingestion_job_response.StartDataIngestionJobResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_data_ingestion_job

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_data_ingestion_job.async_start_data_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.start_data_ingestion_job_request.StartDataIngestionJobRequest = {}  # type: ignore[typeddict-item]
        input_["dataset_name"] = dataset_name
        input_["ingestion_input_configuration"] = ingestion_input_configuration
        input_["role_arn"] = role_arn
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_inference_scheduler(
        self,
        inference_scheduler_name: "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.start_inference_scheduler_response.StartInferenceSchedulerResponse":
        """<p>Starts an inference scheduler. </p>

        Args:
            inference_scheduler_name: <p>The name of the inference scheduler to be started. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.start_inference_scheduler_request.StartInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.start_inference_scheduler_response.StartInferenceSchedulerResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_inference_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_inference_scheduler.async_start_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.start_inference_scheduler_request.StartInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["inference_scheduler_name"] = inference_scheduler_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_retraining_scheduler(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.start_retraining_scheduler_response.StartRetrainingSchedulerResponse":
        """<p>Starts a retraining scheduler. </p>

        Args:
            model_name: <p>The name of the model whose retraining scheduler you want to start.</p>

        Examples:
            Starts a retraining scheduler

            >>> await client.start_retraining_scheduler(model_name='sample-model')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.start_retraining_scheduler_request.StartRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.start_retraining_scheduler_response.StartRetrainingSchedulerResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_retraining_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.start_retraining_scheduler.async_start_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.start_retraining_scheduler_request.StartRetrainingSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_inference_scheduler(
        self,
        inference_scheduler_name: "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.stop_inference_scheduler_response.StopInferenceSchedulerResponse":
        """<p>Stops an inference scheduler. </p>

        Args:
            inference_scheduler_name: <p>The name of the inference scheduler to be stopped. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.stop_inference_scheduler_request.StopInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.stop_inference_scheduler_response.StopInferenceSchedulerResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.stop_inference_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.stop_inference_scheduler.async_stop_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.stop_inference_scheduler_request.StopInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["inference_scheduler_name"] = inference_scheduler_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_retraining_scheduler(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.stop_retraining_scheduler_response.StopRetrainingSchedulerResponse":
        """<p>Stops a retraining scheduler. </p>

        Args:
            model_name: <p>The name of the model whose retraining scheduler you want to stop.</p>

        Examples:
            Stops a retraining scheduler

            >>> await client.stop_retraining_scheduler(model_name='sample-model')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.stop_retraining_scheduler_request.StopRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.stop_retraining_scheduler_response.StopRetrainingSchedulerResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.stop_retraining_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.stop_retraining_scheduler.async_stop_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.stop_retraining_scheduler_request.StopRetrainingSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_lookoutequipment.types.amazon_resource_arn.AmazonResourceArn",
        tags: "aws_sdk_lookoutequipment.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.tag_resource_response.TagResourceResponse":
        """<p>Associates a given tag to a resource in your account. A tag is a key-value pair which can be added to an Amazon Lookout for Equipment resource as metadata. Tags can be used for organizing your resources as well as helping you to search and filter by tag. Multiple tags can be added to a resource, either when you create it, or later. Up to 50 tags can be associated with each resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the specific resource to which the tag should be associated. </p>
            tags: <p>The tag or tags to be associated with a specific resource. Both the tag key and value are specified. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_lookoutequipment.types.amazon_resource_arn.AmazonResourceArn",
        tag_keys: "aws_sdk_lookoutequipment.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a specific tag from a given resource. The tag is specified by its key. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which the tag is currently associated. </p>
            tag_keys: <p>Specifies the key of the tag to be removed from a specified resource. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_active_model_version(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        model_version: "aws_sdk_lookoutequipment.types.model_version.ModelVersion",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
    ) -> "aws_sdk_lookoutequipment.types.update_active_model_version_response.UpdateActiveModelVersionResponse":
        """<p>Sets the active model version for a given machine learning model.</p>

        Args:
            model_name: <p>The name of the machine learning model for which the active model version is being set.</p>
            model_version: <p>The version of the machine learning model for which the active model version is being set.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.update_active_model_version_request.UpdateActiveModelVersionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_lookoutequipment.types.update_active_model_version_response.UpdateActiveModelVersionResponse"
        ]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_active_model_version

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_active_model_version.async_update_active_model_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.update_active_model_version_request.UpdateActiveModelVersionRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name
        input_["model_version"] = model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_inference_scheduler(
        self,
        inference_scheduler_name: "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        data_delay_offset_in_minutes: Optional[
            "aws_sdk_lookoutequipment.types.data_delay_offset_in_minutes.DataDelayOffsetInMinutes"
        ] = None,
        data_upload_frequency: Optional[
            "aws_sdk_lookoutequipment.types.data_upload_frequency.DataUploadFrequency"
        ] = None,
        data_input_configuration: Optional[
            "aws_sdk_lookoutequipment.types.inference_input_configuration.InferenceInputConfiguration"
        ] = None,
        data_output_configuration: Optional[
            "aws_sdk_lookoutequipment.types.inference_output_configuration.InferenceOutputConfiguration"
        ] = None,
        role_arn: Optional[
            "aws_sdk_lookoutequipment.types.iam_role_arn.IamRoleArn"
        ] = None,
    ) -> None:
        """<p>Updates an inference scheduler. </p>

        Args:
            inference_scheduler_name: <p>The name of the inference scheduler to be updated. </p>
            data_delay_offset_in_minutes: <p> A period of time (in minutes) by which inference on the data is delayed after the data starts. For instance, if you select an offset delay time of five minutes, inference will not begin on the data until the first data measurement after the five minute mark. For example, if five minutes is selected, the inference scheduler will wake up at the configured frequency with the additional five minute delay time to check the customer S3 bucket. The customer can upload data at the same frequency and they don't need to stop and restart the scheduler when uploading new data.</p>
            data_upload_frequency: <p>How often data is uploaded to the source S3 bucket for the input data. The value chosen is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment starts a scheduled inference on your data. In this example, it starts once every 5 minutes. </p>
            data_input_configuration: <p> Specifies information for the input data for the inference scheduler, including delimiter, format, and dataset location. </p>
            data_output_configuration: <p> Specifies information for the output results from the inference scheduler, including the output S3 location. </p>
            role_arn: <p> The Amazon Resource Name (ARN) of a role with permission to access the data source for the inference scheduler. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.update_inference_scheduler_request.UpdateInferenceSchedulerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_inference_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_inference_scheduler.async_update_inference_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.update_inference_scheduler_request.UpdateInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["inference_scheduler_name"] = inference_scheduler_name
        if data_delay_offset_in_minutes is not None:
            input_["data_delay_offset_in_minutes"] = data_delay_offset_in_minutes
        if data_upload_frequency is not None:
            input_["data_upload_frequency"] = data_upload_frequency
        if data_input_configuration is not None:
            input_["data_input_configuration"] = data_input_configuration
        if data_output_configuration is not None:
            input_["data_output_configuration"] = data_output_configuration
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_label_group(
        self,
        label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        fault_codes: Optional[
            "aws_sdk_lookoutequipment.types.fault_codes.FaultCodes"
        ] = None,
    ) -> None:
        """<p> Updates the label group. </p>

        Args:
            label_group_name: <p> The name of the label group to be updated. </p>
            fault_codes: <p> Updates the code indicating the type of anomaly associated with the label. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.update_label_group_request.UpdateLabelGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_label_group

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_label_group.async_update_label_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.update_label_group_request.UpdateLabelGroupRequest = {}  # type: ignore[typeddict-item]
        input_["label_group_name"] = label_group_name
        if fault_codes is not None:
            input_["fault_codes"] = fault_codes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_model(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        labels_input_configuration: Optional[
            "aws_sdk_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
        ] = None,
        role_arn: Optional[
            "aws_sdk_lookoutequipment.types.iam_role_arn.IamRoleArn"
        ] = None,
        model_diagnostics_output_configuration: Optional[
            "aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration.ModelDiagnosticsOutputConfiguration"
        ] = None,
    ) -> None:
        """<p>Updates a model in the account.</p>

        Args:
            model_name: <p>The name of the model to update.</p>
            role_arn: <p>The ARN of the model to update.</p>
            model_diagnostics_output_configuration: <p>The Amazon S3 location where you want Amazon Lookout for Equipment to save the pointwise model diagnostics for the model. You must also specify the <code>RoleArn</code> request parameter.</p>

        Examples:
            Updates a model

            >>> await client.update_model(model_name='sample-model', labels_input_configuration={'LabelGroupName': 'sample-label-group'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.update_model_request.UpdateModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_model

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_model.async_update_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.update_model_request.UpdateModelRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name
        if labels_input_configuration is not None:
            input_["labels_input_configuration"] = labels_input_configuration
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if model_diagnostics_output_configuration is not None:
            input_["model_diagnostics_output_configuration"] = (
                model_diagnostics_output_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_retraining_scheduler(
        self,
        model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncLookoutEquipmentClientConfig] = None,
        retraining_start_date: Optional[
            "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
        ] = None,
        retraining_frequency: Optional[
            "aws_sdk_lookoutequipment.types.retraining_frequency.RetrainingFrequency"
        ] = None,
        lookback_window: Optional[
            "aws_sdk_lookoutequipment.types.lookback_window.LookbackWindow"
        ] = None,
        promote_mode: Optional[
            "aws_sdk_lookoutequipment.types.model_promote_mode.ModelPromoteMode"
        ] = None,
    ) -> None:
        r"""<p>Updates a retraining scheduler. </p>

        Args:
            model_name: <p>The name of the model whose retraining scheduler you want to update. </p>
            retraining_start_date: <p>The start date for the retraining scheduler. Lookout for Equipment truncates the time you provide to the nearest UTC day.</p>
            retraining_frequency: <p>This parameter uses the <a href=\"https://en.wikipedia.org/wiki/ISO_8601#Durations\">ISO 8601</a> standard to set the frequency at which you want retraining to occur in terms of Years, Months, and/or Days (note: other parameters like Time are not currently supported). The minimum value is 30 days (P30D) and the maximum value is 1 year (P1Y). For example, the following values are valid:</p> <ul> <li> <p>P3M15D – Every 3 months and 15 days</p> </li> <li> <p>P2M – Every 2 months</p> </li> <li> <p>P150D – Every 150 days</p> </li> </ul>
            lookback_window: <p>The number of past days of data that will be used for retraining.</p>
            promote_mode: <p>Indicates how the service will use new models. In <code>MANAGED</code> mode, new models will automatically be used for inference if they have better performance than the current model. In <code>MANUAL</code> mode, the new models will not be used <a href=\"https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/versioning-model.html#model-activation\">until they are manually activated</a>.</p>

        Examples:
            Updates a retraining scheduler

            >>> await client.update_retraining_scheduler(model_name='sample-model', retraining_start_date='2024-01-01T00:00:00Z', retraining_frequency='P1Y')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_lookoutequipment.types.update_retraining_scheduler_request.UpdateRetrainingSchedulerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_retraining_scheduler

            (
                output,
                http_response,
            ) = await aws_sdk_lookoutequipment._operations.aws_lookout_equipment_frontend_service.update_retraining_scheduler.async_update_retraining_scheduler(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_lookoutequipment.types.update_retraining_scheduler_request.UpdateRetrainingSchedulerRequest = {}  # type: ignore[typeddict-item]
        input_["model_name"] = model_name
        if retraining_start_date is not None:
            input_["retraining_start_date"] = retraining_start_date
        if retraining_frequency is not None:
            input_["retraining_frequency"] = retraining_frequency
        if lookback_window is not None:
            input_["lookback_window"] = lookback_window
        if promote_mode is not None:
            input_["promote_mode"] = promote_mode

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
