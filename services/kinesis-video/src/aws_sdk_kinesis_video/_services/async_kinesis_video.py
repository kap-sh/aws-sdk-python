"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#KinesisVideo_20170930``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_kinesis_video._auth._signers
import aws_sdk_kinesis_video._auth._sigv4
from aws_sdk_kinesis_video._auth._identity import Credentials
from aws_sdk_kinesis_video._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_kinesis_video._auth._zapros_handler import AuthMiddleware
from aws_sdk_kinesis_video._pagination import resolve_path as _resolve_path
from aws_sdk_kinesis_video._services._aws_config import aaws_config
from aws_sdk_kinesis_video._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.api_name
    import aws_sdk_kinesis_video.types.channel_info
    import aws_sdk_kinesis_video.types.channel_name
    import aws_sdk_kinesis_video.types.channel_name_condition
    import aws_sdk_kinesis_video.types.channel_type
    import aws_sdk_kinesis_video.types.create_signaling_channel_input
    import aws_sdk_kinesis_video.types.create_signaling_channel_output
    import aws_sdk_kinesis_video.types.create_stream_input
    import aws_sdk_kinesis_video.types.create_stream_output
    import aws_sdk_kinesis_video.types.data_retention_change_in_hours
    import aws_sdk_kinesis_video.types.data_retention_in_hours
    import aws_sdk_kinesis_video.types.delete_edge_configuration_input
    import aws_sdk_kinesis_video.types.delete_edge_configuration_output
    import aws_sdk_kinesis_video.types.delete_signaling_channel_input
    import aws_sdk_kinesis_video.types.delete_signaling_channel_output
    import aws_sdk_kinesis_video.types.delete_stream_input
    import aws_sdk_kinesis_video.types.delete_stream_output
    import aws_sdk_kinesis_video.types.describe_edge_configuration_input
    import aws_sdk_kinesis_video.types.describe_edge_configuration_output
    import aws_sdk_kinesis_video.types.describe_image_generation_configuration_input
    import aws_sdk_kinesis_video.types.describe_image_generation_configuration_output
    import aws_sdk_kinesis_video.types.describe_mapped_resource_configuration_input
    import aws_sdk_kinesis_video.types.describe_mapped_resource_configuration_output
    import aws_sdk_kinesis_video.types.describe_media_storage_configuration_input
    import aws_sdk_kinesis_video.types.describe_media_storage_configuration_output
    import aws_sdk_kinesis_video.types.describe_notification_configuration_input
    import aws_sdk_kinesis_video.types.describe_notification_configuration_output
    import aws_sdk_kinesis_video.types.describe_signaling_channel_input
    import aws_sdk_kinesis_video.types.describe_signaling_channel_output
    import aws_sdk_kinesis_video.types.describe_stream_input
    import aws_sdk_kinesis_video.types.describe_stream_output
    import aws_sdk_kinesis_video.types.describe_stream_storage_configuration_input
    import aws_sdk_kinesis_video.types.describe_stream_storage_configuration_output
    import aws_sdk_kinesis_video.types.device_name
    import aws_sdk_kinesis_video.types.edge_config
    import aws_sdk_kinesis_video.types.get_data_endpoint_input
    import aws_sdk_kinesis_video.types.get_data_endpoint_output
    import aws_sdk_kinesis_video.types.get_signaling_channel_endpoint_input
    import aws_sdk_kinesis_video.types.get_signaling_channel_endpoint_output
    import aws_sdk_kinesis_video.types.hub_device_arn
    import aws_sdk_kinesis_video.types.image_generation_configuration
    import aws_sdk_kinesis_video.types.kms_key_id
    import aws_sdk_kinesis_video.types.list_edge_agent_configurations_edge_config
    import aws_sdk_kinesis_video.types.list_edge_agent_configurations_input
    import aws_sdk_kinesis_video.types.list_edge_agent_configurations_input_limit
    import aws_sdk_kinesis_video.types.list_edge_agent_configurations_output
    import aws_sdk_kinesis_video.types.list_signaling_channels_input
    import aws_sdk_kinesis_video.types.list_signaling_channels_output
    import aws_sdk_kinesis_video.types.list_streams_input
    import aws_sdk_kinesis_video.types.list_streams_input_limit
    import aws_sdk_kinesis_video.types.list_streams_output
    import aws_sdk_kinesis_video.types.list_tags_for_resource_input
    import aws_sdk_kinesis_video.types.list_tags_for_resource_output
    import aws_sdk_kinesis_video.types.list_tags_for_stream_input
    import aws_sdk_kinesis_video.types.list_tags_for_stream_output
    import aws_sdk_kinesis_video.types.mapped_resource_configuration_list_item
    import aws_sdk_kinesis_video.types.mapped_resource_configuration_list_limit
    import aws_sdk_kinesis_video.types.media_storage_configuration
    import aws_sdk_kinesis_video.types.media_type
    import aws_sdk_kinesis_video.types.next_token
    import aws_sdk_kinesis_video.types.notification_configuration
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.resource_tags
    import aws_sdk_kinesis_video.types.single_master_channel_endpoint_configuration
    import aws_sdk_kinesis_video.types.single_master_configuration
    import aws_sdk_kinesis_video.types.start_edge_configuration_update_input
    import aws_sdk_kinesis_video.types.start_edge_configuration_update_output
    import aws_sdk_kinesis_video.types.stream_info
    import aws_sdk_kinesis_video.types.stream_name
    import aws_sdk_kinesis_video.types.stream_name_condition
    import aws_sdk_kinesis_video.types.stream_storage_configuration
    import aws_sdk_kinesis_video.types.tag_key_list
    import aws_sdk_kinesis_video.types.tag_list
    import aws_sdk_kinesis_video.types.tag_on_create_list
    import aws_sdk_kinesis_video.types.tag_resource_input
    import aws_sdk_kinesis_video.types.tag_resource_output
    import aws_sdk_kinesis_video.types.tag_stream_input
    import aws_sdk_kinesis_video.types.tag_stream_output
    import aws_sdk_kinesis_video.types.untag_resource_input
    import aws_sdk_kinesis_video.types.untag_resource_output
    import aws_sdk_kinesis_video.types.untag_stream_input
    import aws_sdk_kinesis_video.types.untag_stream_output
    import aws_sdk_kinesis_video.types.update_data_retention_input
    import aws_sdk_kinesis_video.types.update_data_retention_operation
    import aws_sdk_kinesis_video.types.update_data_retention_output
    import aws_sdk_kinesis_video.types.update_image_generation_configuration_input
    import aws_sdk_kinesis_video.types.update_image_generation_configuration_output
    import aws_sdk_kinesis_video.types.update_media_storage_configuration_input
    import aws_sdk_kinesis_video.types.update_media_storage_configuration_output
    import aws_sdk_kinesis_video.types.update_notification_configuration_input
    import aws_sdk_kinesis_video.types.update_notification_configuration_output
    import aws_sdk_kinesis_video.types.update_signaling_channel_input
    import aws_sdk_kinesis_video.types.update_signaling_channel_output
    import aws_sdk_kinesis_video.types.update_stream_input
    import aws_sdk_kinesis_video.types.update_stream_output
    import aws_sdk_kinesis_video.types.update_stream_storage_configuration_input
    import aws_sdk_kinesis_video.types.update_stream_storage_configuration_output
    import aws_sdk_kinesis_video.types.version


class AsyncKinesisVideoClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncKinesisVideoClient:
    """A client for the ``KinesisVideo`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncKinesisVideoClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncKinesisVideoClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncKinesisVideoClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def create_signaling_channel(
        self,
        channel_name: "aws_sdk_kinesis_video.types.channel_name.ChannelName",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        channel_type: Optional[
            "aws_sdk_kinesis_video.types.channel_type.ChannelType"
        ] = None,
        single_master_configuration: Optional[
            "aws_sdk_kinesis_video.types.single_master_configuration.SingleMasterConfiguration"
        ] = None,
        tags: Optional[
            "aws_sdk_kinesis_video.types.tag_on_create_list.TagOnCreateList"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.create_signaling_channel_output.CreateSignalingChannelOutput":
        """<p>Creates a signaling channel. </p> <p> <code>CreateSignalingChannel</code> is an asynchronous operation.</p>

        Args:
            channel_name: <p>A name for the signaling channel that you are creating. It must be unique for each Amazon Web Services account and Amazon Web Services Region.</p>
            channel_type: <p>A type of the signaling channel that you are creating. Currently, <code>SINGLE_MASTER</code> is the only supported channel type. </p>
            single_master_configuration: <p>A structure containing the configuration for the <code>SINGLE_MASTER</code> channel type. The default configuration for the channel message's time to live is 60 seconds (1 minute).</p>
            tags: <p>A set of tags (key-value pairs) that you want to associate with this channel.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.account_channel_limit_exceeded_exception.AccountChannelLimitExceededException: <p>You have reached the maximum limit of active signaling channels for this Amazon Web Services account in this region.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.tags_per_resource_exceeded_limit_exception.TagsPerResourceExceededLimitException: <p>You have exceeded the limit of tags that you can associate with the resource. A Kinesis video stream can support up to 50 tags. </p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.create_signaling_channel_input.CreateSignalingChannelInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.create_signaling_channel_output.CreateSignalingChannelOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.create_signaling_channel

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.create_signaling_channel.async_create_signaling_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.create_signaling_channel_input.CreateSignalingChannelInput = {}  # type: ignore[typeddict-item]
        input_["channel_name"] = channel_name
        if channel_type is not None:
            input_["channel_type"] = channel_type
        if single_master_configuration is not None:
            input_["single_master_configuration"] = single_master_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_stream(
        self,
        stream_name: "aws_sdk_kinesis_video.types.stream_name.StreamName",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        device_name: Optional[
            "aws_sdk_kinesis_video.types.device_name.DeviceName"
        ] = None,
        media_type: Optional["aws_sdk_kinesis_video.types.media_type.MediaType"] = None,
        kms_key_id: Optional["aws_sdk_kinesis_video.types.kms_key_id.KmsKeyId"] = None,
        data_retention_in_hours: Optional[
            "aws_sdk_kinesis_video.types.data_retention_in_hours.DataRetentionInHours"
        ] = None,
        tags: Optional["aws_sdk_kinesis_video.types.resource_tags.ResourceTags"] = None,
        stream_storage_configuration: Optional[
            "aws_sdk_kinesis_video.types.stream_storage_configuration.StreamStorageConfiguration"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.create_stream_output.CreateStreamOutput":
        r"""<p>Creates a new Kinesis video stream. </p> <p>When you create a new stream, Kinesis Video Streams assigns it a version number. When you change the stream's metadata, Kinesis Video Streams updates the version. </p> <p> <code>CreateStream</code> is an asynchronous operation.</p> <p>For information about how the service works, see <a href=\"https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-works.html\">How it Works</a>. </p> <p>You must have permissions for the <code>KinesisVideo:CreateStream</code> action.</p>

        Args:
            device_name: <p>The name of the device that is writing to the stream. </p> <note> <p>In the current implementation, Kinesis Video Streams doesn't use this name.</p> </note>
            stream_name: <p>A name for the stream that you are creating.</p> <p>The stream name is an identifier for the stream, and must be unique for each account and region.</p>
            media_type: <p>The media type of the stream. Consumers of the stream can use this information when processing the stream. For more information about media types, see <a href=\"http://www.iana.org/assignments/media-types/media-types.xhtml\">Media Types</a>. If you choose to specify the <code>MediaType</code>, see <a href=\"https://tools.ietf.org/html/rfc6838#section-4.2\">Naming Requirements</a> for guidelines.</p> <p>Example valid values include \"video/h264\" and \"video/h264,audio/aac\".</p> <p>This parameter is optional; the default value is <code>null</code> (or empty in JSON).</p>
            kms_key_id: <p>The ID of the Key Management Service (KMS) key that you want Kinesis Video Streams to use to encrypt stream data.</p> <p>If no key ID is specified, the default, Kinesis Video-managed key (<code>aws/kinesisvideo</code>) is used.</p> <p> For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters\">DescribeKey</a>. </p>
            data_retention_in_hours: <p>The number of hours that you want to retain the data in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream.</p> <p>The default value is 0, indicating that the stream does not persist data. The minimum is 1 hour.</p> <p>When the <code>DataRetentionInHours</code> value is 0, consumers can still consume the fragments that remain in the service host buffer, which has a retention time limit of 5 minutes and a retention memory limit of 200 MB. Fragments are removed from the buffer when either limit is reached.</p>
            tags: <p>A list of tags to associate with the specified stream. Each tag is a key-value pair (the value is optional).</p>
            stream_storage_configuration: <p>The configuration for the stream's storage, including the default storage tier for stream data. This configuration determines how stream data is stored and accessed, with different tiers offering varying levels of performance and cost optimization.</p> <p>If not specified, the stream will use the default storage configuration with HOT tier for optimal performance.</p>

        Raises:
            aws_sdk_kinesis_video.errors.account_stream_limit_exceeded_exception.AccountStreamLimitExceededException: <p>The number of streams created for the account is too high.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.device_stream_limit_exceeded_exception.DeviceStreamLimitExceededException: <p>Not implemented. </p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.invalid_device_exception.InvalidDeviceException: <p>Not implemented.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.tags_per_resource_exceeded_limit_exception.TagsPerResourceExceededLimitException: <p>You have exceeded the limit of tags that you can associate with the resource. A Kinesis video stream can support up to 50 tags. </p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.create_stream_input.CreateStreamInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.create_stream_output.CreateStreamOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.create_stream

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.create_stream.async_create_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.create_stream_input.CreateStreamInput = {}  # type: ignore[typeddict-item]
        if device_name is not None:
            input_["device_name"] = device_name
        input_["stream_name"] = stream_name
        if media_type is not None:
            input_["media_type"] = media_type
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if data_retention_in_hours is not None:
            input_["data_retention_in_hours"] = data_retention_in_hours
        if tags is not None:
            input_["tags"] = tags
        if stream_storage_configuration is not None:
            input_["stream_storage_configuration"] = stream_storage_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_edge_configuration(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.delete_edge_configuration_output.DeleteEdgeConfigurationOutput":
        """<p>An asynchronous API that deletes a stream’s existing edge configuration, as well as the corresponding media from the Edge Agent.</p> <p>When you invoke this API, the sync status is set to <code>DELETING</code>. A deletion process starts, in which active edge jobs are stopped and all media is deleted from the edge device. The time to delete varies, depending on the total amount of stored media. If the deletion process fails, the sync status changes to <code>DELETE_FAILED</code>. You will need to re-try the deletion.</p> <p>When the deletion process has completed successfully, the edge configuration is no longer accessible.</p>

        Args:
            stream_name: <p>The name of the stream from which to delete the edge configuration. Specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream. Specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.stream_edge_configuration_not_found_exception.StreamEdgeConfigurationNotFoundException: <p>The Exception rendered when the Amazon Kinesis Video Stream can't find a stream's edge configuration that you specified. </p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.delete_edge_configuration_input.DeleteEdgeConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.delete_edge_configuration_output.DeleteEdgeConfigurationOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.delete_edge_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.delete_edge_configuration.async_delete_edge_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.delete_edge_configuration_input.DeleteEdgeConfigurationInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_signaling_channel(
        self,
        channel_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        current_version: Optional["aws_sdk_kinesis_video.types.version.Version"] = None,
    ) -> "aws_sdk_kinesis_video.types.delete_signaling_channel_output.DeleteSignalingChannelOutput":
        """<p>Deletes a specified signaling channel. <code>DeleteSignalingChannel</code> is an asynchronous operation. If you don't specify the channel's current version, the most recent version is deleted.</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the signaling channel that you want to delete.</p>
            current_version: <p>The current version of the signaling channel that you want to delete. You can obtain the current version by invoking the <code>DescribeSignalingChannel</code> or <code>ListSignalingChannels</code> API operations.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.version_mismatch_exception.VersionMismatchException: <p>The stream version that you specified is not the latest version. To get the latest version, use the <a href=\"https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html\">DescribeStream</a> API.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.delete_signaling_channel_input.DeleteSignalingChannelInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.delete_signaling_channel_output.DeleteSignalingChannelOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.delete_signaling_channel

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.delete_signaling_channel.async_delete_signaling_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.delete_signaling_channel_input.DeleteSignalingChannelInput = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if current_version is not None:
            input_["current_version"] = current_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_stream(
        self,
        stream_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        current_version: Optional["aws_sdk_kinesis_video.types.version.Version"] = None,
    ) -> "aws_sdk_kinesis_video.types.delete_stream_output.DeleteStreamOutput":
        """<p>Deletes a Kinesis video stream and the data contained in the stream. </p> <p>This method marks the stream for deletion, and makes the data in the stream inaccessible immediately.</p> <p> </p> <p> To ensure that you have the latest version of the stream before deleting it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the <code>DescribeStream</code> API. </p> <p>This operation requires permission for the <code>KinesisVideo:DeleteStream</code> action.</p>

        Args:
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream that you want to delete. </p>
            current_version: <p>Optional: The version of the stream that you want to delete. </p> <p>Specify the version as a safeguard to ensure that your are deleting the correct stream. To get the stream version, use the <code>DescribeStream</code> API.</p> <p>If not specified, only the <code>CreationTime</code> is checked before deleting the stream.</p>

        Raises:
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.not_authorized_exception.NotAuthorizedException: <p>The caller is not authorized to perform this operation.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.version_mismatch_exception.VersionMismatchException: <p>The stream version that you specified is not the latest version. To get the latest version, use the <a href=\"https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html\">DescribeStream</a> API.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.delete_stream_input.DeleteStreamInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.delete_stream_output.DeleteStreamOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.delete_stream

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.delete_stream.async_delete_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.delete_stream_input.DeleteStreamInput = {}  # type: ignore[typeddict-item]
        input_["stream_arn"] = stream_arn
        if current_version is not None:
            input_["current_version"] = current_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_edge_configuration(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.describe_edge_configuration_output.DescribeEdgeConfigurationOutput":
        """<p>Describes a stream’s edge configuration that was set using the <code>StartEdgeConfigurationUpdate</code> API and the latest status of the edge agent's recorder and uploader jobs. Use this API to get the status of the configuration to determine if the configuration is in sync with the Edge Agent. Use this API to evaluate the health of the Edge Agent.</p>

        Args:
            stream_name: <p>The name of the stream whose edge configuration you want to update. Specify either the <code>StreamName</code> or the <code>StreamARN</code>. </p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream. Specify either the <code>StreamName</code>or the <code>StreamARN</code>.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.stream_edge_configuration_not_found_exception.StreamEdgeConfigurationNotFoundException: <p>The Exception rendered when the Amazon Kinesis Video Stream can't find a stream's edge configuration that you specified. </p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.describe_edge_configuration_input.DescribeEdgeConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.describe_edge_configuration_output.DescribeEdgeConfigurationOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_edge_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_edge_configuration.async_describe_edge_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.describe_edge_configuration_input.DescribeEdgeConfigurationInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_image_generation_configuration(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.describe_image_generation_configuration_output.DescribeImageGenerationConfigurationOutput":
        """<p>Gets the <code>ImageGenerationConfiguration</code> for a given Kinesis video stream.</p>

        Args:
            stream_name: <p>The name of the stream from which to retrieve the image generation configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>. </p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the Kinesis video stream from which to retrieve the image generation configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.describe_image_generation_configuration_input.DescribeImageGenerationConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.describe_image_generation_configuration_output.DescribeImageGenerationConfigurationOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_image_generation_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_image_generation_configuration.async_describe_image_generation_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.describe_image_generation_configuration_input.DescribeImageGenerationConfigurationInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_mapped_resource_configuration(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
        max_results: Optional[
            "aws_sdk_kinesis_video.types.mapped_resource_configuration_list_limit.MappedResourceConfigurationListLimit"
        ] = None,
        next_token: Optional["aws_sdk_kinesis_video.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_kinesis_video.types.describe_mapped_resource_configuration_output.DescribeMappedResourceConfigurationOutput":
        """<p>Returns the most current information about the stream. The <code>streamName</code> or <code>streamARN</code> should be provided in the input.</p>

        Args:
            stream_name: <p>The name of the stream.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>The token to provide in your next request, to get another batch of results.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.describe_mapped_resource_configuration_input.DescribeMappedResourceConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.describe_mapped_resource_configuration_output.DescribeMappedResourceConfigurationOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_mapped_resource_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_mapped_resource_configuration.async_describe_mapped_resource_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.describe_mapped_resource_configuration_input.DescribeMappedResourceConfigurationInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
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

    async def iter_describe_mapped_resource_configuration(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
        max_results: Optional[
            "aws_sdk_kinesis_video.types.mapped_resource_configuration_list_limit.MappedResourceConfigurationListLimit"
        ] = None,
        next_token: Optional["aws_sdk_kinesis_video.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_kinesis_video.types.mapped_resource_configuration_list_item.MappedResourceConfigurationListItem]":
        _token = next_token
        while True:
            _response = await self.describe_mapped_resource_configuration(
                config_overrides=config_overrides,
                stream_name=stream_name,
                stream_arn=stream_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("mapped_resource_configuration_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_media_storage_configuration(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        channel_name: Optional[
            "aws_sdk_kinesis_video.types.channel_name.ChannelName"
        ] = None,
        channel_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.describe_media_storage_configuration_output.DescribeMediaStorageConfigurationOutput":
        """<p>Returns the most current information about the channel. Specify the <code>ChannelName</code> or <code>ChannelARN</code> in the input.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            channel_arn: <p>The Amazon Resource Name (ARN) of the channel.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.describe_media_storage_configuration_input.DescribeMediaStorageConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.describe_media_storage_configuration_output.DescribeMediaStorageConfigurationOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_media_storage_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_media_storage_configuration.async_describe_media_storage_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.describe_media_storage_configuration_input.DescribeMediaStorageConfigurationInput = {}  # type: ignore[typeddict-item]
        if channel_name is not None:
            input_["channel_name"] = channel_name
        if channel_arn is not None:
            input_["channel_arn"] = channel_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_notification_configuration(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.describe_notification_configuration_output.DescribeNotificationConfigurationOutput":
        """<p>Gets the <code>NotificationConfiguration</code> for a given Kinesis video stream.</p>

        Args:
            stream_name: <p>The name of the stream from which to retrieve the notification configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the Kinesis video stream from where you want to retrieve the notification configuration. You must specify either the <code>StreamName</code> or the StreamARN.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.describe_notification_configuration_input.DescribeNotificationConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.describe_notification_configuration_output.DescribeNotificationConfigurationOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_notification_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_notification_configuration.async_describe_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.describe_notification_configuration_input.DescribeNotificationConfigurationInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_signaling_channel(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        channel_name: Optional[
            "aws_sdk_kinesis_video.types.channel_name.ChannelName"
        ] = None,
        channel_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.describe_signaling_channel_output.DescribeSignalingChannelOutput":
        """<p>Returns the most current information about the signaling channel. You must specify either the name or the Amazon Resource Name (ARN) of the channel that you want to describe.</p>

        Args:
            channel_name: <p>The name of the signaling channel that you want to describe.</p>
            channel_arn: <p>The ARN of the signaling channel that you want to describe.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.describe_signaling_channel_input.DescribeSignalingChannelInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.describe_signaling_channel_output.DescribeSignalingChannelOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_signaling_channel

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_signaling_channel.async_describe_signaling_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.describe_signaling_channel_input.DescribeSignalingChannelInput = {}  # type: ignore[typeddict-item]
        if channel_name is not None:
            input_["channel_name"] = channel_name
        if channel_arn is not None:
            input_["channel_arn"] = channel_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_stream(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.describe_stream_output.DescribeStreamOutput":
        """<p>Returns the most current information about the specified stream. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>. </p>

        Args:
            stream_name: <p>The name of the stream.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream.</p>

        Raises:
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.not_authorized_exception.NotAuthorizedException: <p>The caller is not authorized to perform this operation.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.describe_stream_input.DescribeStreamInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.describe_stream_output.DescribeStreamOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_stream

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_stream.async_describe_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.describe_stream_input.DescribeStreamInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_stream_storage_configuration(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.describe_stream_storage_configuration_output.DescribeStreamStorageConfigurationOutput":
        """<p>Retrieves the current storage configuration for the specified Kinesis video stream.</p> <p>In the request, you must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p> <p>You must have permissions for the <code>KinesisVideo:DescribeStreamStorageConfiguration</code> action.</p>

        Args:
            stream_name: <p>The name of the stream for which you want to retrieve the storage configuration.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream for which you want to retrieve the storage configuration.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.describe_stream_storage_configuration_input.DescribeStreamStorageConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.describe_stream_storage_configuration_output.DescribeStreamStorageConfigurationOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_stream_storage_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.describe_stream_storage_configuration.async_describe_stream_storage_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.describe_stream_storage_configuration_input.DescribeStreamStorageConfigurationInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_endpoint(
        self,
        api_name: "aws_sdk_kinesis_video.types.api_name.APIName",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.get_data_endpoint_output.GetDataEndpointOutput":
        """<p>Gets an endpoint for a specified stream for either reading or writing. Use this endpoint in your application to read from the specified stream (using the <code>GetMedia</code> or <code>GetMediaForFragmentList</code> operations) or write to it (using the <code>PutMedia</code> operation). </p> <note> <p>The returned endpoint does not have the API name appended. The client needs to add the API name to the returned endpoint.</p> </note> <p>In the request, specify the stream either by <code>StreamName</code> or <code>StreamARN</code>.</p>

        Args:
            stream_name: <p>The name of the stream that you want to get the endpoint for. You must specify either this parameter or a <code>StreamARN</code> in the request.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream that you want to get the endpoint for. You must specify either this parameter or a <code>StreamName</code> in the request. </p>
            api_name: <p>The name of the API action for which to get an endpoint.</p>

        Raises:
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.not_authorized_exception.NotAuthorizedException: <p>The caller is not authorized to perform this operation.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.get_data_endpoint_input.GetDataEndpointInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.get_data_endpoint_output.GetDataEndpointOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.get_data_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.get_data_endpoint.async_get_data_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.get_data_endpoint_input.GetDataEndpointInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        input_["api_name"] = api_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_signaling_channel_endpoint(
        self,
        channel_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        single_master_channel_endpoint_configuration: Optional[
            "aws_sdk_kinesis_video.types.single_master_channel_endpoint_configuration.SingleMasterChannelEndpointConfiguration"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.get_signaling_channel_endpoint_output.GetSignalingChannelEndpointOutput":
        """<p>Provides an endpoint for the specified signaling channel to send and receive messages. This API uses the <code>SingleMasterChannelEndpointConfiguration</code> input parameter, which consists of the <code>Protocols</code> and <code>Role</code> properties.</p> <p> <code>Protocols</code> is used to determine the communication mechanism. For example, if you specify <code>WSS</code> as the protocol, this API produces a secure websocket endpoint. If you specify <code>HTTPS</code> as the protocol, this API generates an HTTPS endpoint. If you specify <code>WEBRTC</code> as the protocol, but the signaling channel isn't configured for ingestion, you will receive the error <code>InvalidArgumentException</code>.</p> <p> <code>Role</code> determines the messaging permissions. A <code>MASTER</code> role results in this API generating an endpoint that a client can use to communicate with any of the viewers on the channel. A <code>VIEWER</code> role results in this API generating an endpoint that a client can use to communicate only with a <code>MASTER</code>. </p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the signalling channel for which you want to get an endpoint.</p>
            single_master_channel_endpoint_configuration: <p>A structure containing the endpoint configuration for the <code>SINGLE_MASTER</code> channel type.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.get_signaling_channel_endpoint_input.GetSignalingChannelEndpointInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.get_signaling_channel_endpoint_output.GetSignalingChannelEndpointOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.get_signaling_channel_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.get_signaling_channel_endpoint.async_get_signaling_channel_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.get_signaling_channel_endpoint_input.GetSignalingChannelEndpointInput = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if single_master_channel_endpoint_configuration is not None:
            input_["single_master_channel_endpoint_configuration"] = (
                single_master_channel_endpoint_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_edge_agent_configurations(
        self,
        hub_device_arn: "aws_sdk_kinesis_video.types.hub_device_arn.HubDeviceArn",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        max_results: Optional[
            "aws_sdk_kinesis_video.types.list_edge_agent_configurations_input_limit.ListEdgeAgentConfigurationsInputLimit"
        ] = None,
        next_token: Optional["aws_sdk_kinesis_video.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_kinesis_video.types.list_edge_agent_configurations_output.ListEdgeAgentConfigurationsOutput":
        r"""<p>Returns an array of edge configurations associated with the specified Edge Agent.</p> <p>In the request, you must specify the Edge Agent <code>HubDeviceArn</code>.</p>

        Args:
            hub_device_arn: <p>The \"Internet of Things (IoT) Thing\" Arn of the edge agent.</p>
            max_results: <p>The maximum number of edge configurations to return in the response. The default is 5.</p>
            next_token: <p>If you specify this parameter, when the result of a <code>ListEdgeAgentConfigurations</code> operation is truncated, the call returns the <code>NextToken</code> in the response. To get another batch of edge configurations, provide this token in your next request. </p>

        Raises:
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.not_authorized_exception.NotAuthorizedException: <p>The caller is not authorized to perform this operation.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.list_edge_agent_configurations_input.ListEdgeAgentConfigurationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.list_edge_agent_configurations_output.ListEdgeAgentConfigurationsOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.list_edge_agent_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.list_edge_agent_configurations.async_list_edge_agent_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.list_edge_agent_configurations_input.ListEdgeAgentConfigurationsInput = {}  # type: ignore[typeddict-item]
        input_["hub_device_arn"] = hub_device_arn
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

    async def iter_list_edge_agent_configurations(
        self,
        hub_device_arn: "aws_sdk_kinesis_video.types.hub_device_arn.HubDeviceArn",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        max_results: Optional[
            "aws_sdk_kinesis_video.types.list_edge_agent_configurations_input_limit.ListEdgeAgentConfigurationsInputLimit"
        ] = None,
        next_token: Optional["aws_sdk_kinesis_video.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_kinesis_video.types.list_edge_agent_configurations_edge_config.ListEdgeAgentConfigurationsEdgeConfig]":
        _token = next_token
        while True:
            _response = await self.list_edge_agent_configurations(
                hub_device_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("edge_configs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_signaling_channels(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        max_results: Optional[
            "aws_sdk_kinesis_video.types.list_streams_input_limit.ListStreamsInputLimit"
        ] = None,
        next_token: Optional["aws_sdk_kinesis_video.types.next_token.NextToken"] = None,
        channel_name_condition: Optional[
            "aws_sdk_kinesis_video.types.channel_name_condition.ChannelNameCondition"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.list_signaling_channels_output.ListSignalingChannelsOutput":
        """<p>Returns an array of <code>ChannelInfo</code> objects. Each object describes a signaling channel. To retrieve only those channels that satisfy a specific condition, you can specify a <code>ChannelNameCondition</code>.</p>

        Args:
            max_results: <p>The maximum number of channels to return in the response. The default is 500.</p>
            next_token: <p>If you specify this parameter, when the result of a <code>ListSignalingChannels</code> operation is truncated, the call returns the <code>NextToken</code> in the response. To get another batch of channels, provide this token in your next request.</p>
            channel_name_condition: <p>Optional: Returns only the channels that satisfy a specific condition.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.list_signaling_channels_input.ListSignalingChannelsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.list_signaling_channels_output.ListSignalingChannelsOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.list_signaling_channels

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.list_signaling_channels.async_list_signaling_channels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.list_signaling_channels_input.ListSignalingChannelsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if channel_name_condition is not None:
            input_["channel_name_condition"] = channel_name_condition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_signaling_channels(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        max_results: Optional[
            "aws_sdk_kinesis_video.types.list_streams_input_limit.ListStreamsInputLimit"
        ] = None,
        next_token: Optional["aws_sdk_kinesis_video.types.next_token.NextToken"] = None,
        channel_name_condition: Optional[
            "aws_sdk_kinesis_video.types.channel_name_condition.ChannelNameCondition"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_kinesis_video.types.channel_info.ChannelInfo]":
        _token = next_token
        while True:
            _response = await self.list_signaling_channels(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                channel_name_condition=channel_name_condition,
            )
            _page = _resolve_path(_response, ("channel_info_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_streams(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        max_results: Optional[
            "aws_sdk_kinesis_video.types.list_streams_input_limit.ListStreamsInputLimit"
        ] = None,
        next_token: Optional["aws_sdk_kinesis_video.types.next_token.NextToken"] = None,
        stream_name_condition: Optional[
            "aws_sdk_kinesis_video.types.stream_name_condition.StreamNameCondition"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.list_streams_output.ListStreamsOutput":
        """<p>Returns an array of <code>StreamInfo</code> objects. Each object describes a stream. To retrieve only streams that satisfy a specific condition, you can specify a <code>StreamNameCondition</code>. </p>

        Args:
            max_results: <p>The maximum number of streams to return in the response. The default is 10,000.</p>
            next_token: <p>If you specify this parameter, when the result of a <code>ListStreams</code> operation is truncated, the call returns the <code>NextToken</code> in the response. To get another batch of streams, provide this token in your next request.</p>
            stream_name_condition: <p>Optional: Returns only streams that satisfy a specific condition. Currently, you can specify only the prefix of a stream name as a condition. </p>

        Raises:
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.list_streams_input.ListStreamsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.list_streams_output.ListStreamsOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.list_streams

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.list_streams.async_list_streams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.list_streams_input.ListStreamsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if stream_name_condition is not None:
            input_["stream_name_condition"] = stream_name_condition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_streams(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        max_results: Optional[
            "aws_sdk_kinesis_video.types.list_streams_input_limit.ListStreamsInputLimit"
        ] = None,
        next_token: Optional["aws_sdk_kinesis_video.types.next_token.NextToken"] = None,
        stream_name_condition: Optional[
            "aws_sdk_kinesis_video.types.stream_name_condition.StreamNameCondition"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_kinesis_video.types.stream_info.StreamInfo]":
        _token = next_token
        while True:
            _response = await self.list_streams(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                stream_name_condition=stream_name_condition,
            )
            _page = _resolve_path(_response, ("stream_info_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        next_token: Optional["aws_sdk_kinesis_video.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_kinesis_video.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns a list of tags associated with the specified signaling channel.</p>

        Args:
            next_token: <p>If you specify this parameter and the result of a <code>ListTagsForResource</code> call is truncated, the response includes a token that you can use in the next request to fetch the next batch of tags. </p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the signaling channel for which you want to list tags.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_stream(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        next_token: Optional["aws_sdk_kinesis_video.types.next_token.NextToken"] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.list_tags_for_stream_output.ListTagsForStreamOutput":
        """<p>Returns a list of tags associated with the specified stream.</p> <p>In the request, you must specify either the <code>StreamName</code> or the <code>StreamARN</code>. </p>

        Args:
            next_token: <p>If you specify this parameter and the result of a <code>ListTagsForStream</code> call is truncated, the response includes a token that you can use in the next request to fetch the next batch of tags.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream that you want to list tags for.</p>
            stream_name: <p>The name of the stream that you want to list tags for.</p>

        Raises:
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.invalid_resource_format_exception.InvalidResourceFormatException: <p>The format of the <code>StreamARN</code> is invalid.</p>
            aws_sdk_kinesis_video.errors.not_authorized_exception.NotAuthorizedException: <p>The caller is not authorized to perform this operation.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.list_tags_for_stream_input.ListTagsForStreamInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.list_tags_for_stream_output.ListTagsForStreamOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.list_tags_for_stream

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.list_tags_for_stream.async_list_tags_for_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.list_tags_for_stream_input.ListTagsForStreamInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_name is not None:
            input_["stream_name"] = stream_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_edge_configuration_update(
        self,
        edge_config: "aws_sdk_kinesis_video.types.edge_config.EdgeConfig",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.start_edge_configuration_update_output.StartEdgeConfigurationUpdateOutput":
        """<p>An asynchronous API that updates a stream’s existing edge configuration. The Kinesis Video Stream will sync the stream’s edge configuration with the Edge Agent IoT Greengrass component that runs on an IoT Hub Device, setup at your premise. The time to sync can vary and depends on the connectivity of the Hub Device. The <code>SyncStatus</code> will be updated as the edge configuration is acknowledged, and synced with the Edge Agent. </p> <p>If this API is invoked for the first time, a new edge configuration will be created for the stream, and the sync status will be set to <code>SYNCING</code>. You will have to wait for the sync status to reach a terminal state such as: <code>IN_SYNC</code>, or <code>SYNC_FAILED</code>, before using this API again. If you invoke this API during the syncing process, a <code>ResourceInUseException</code> will be thrown. The connectivity of the stream’s edge configuration and the Edge Agent will be retried for 15 minutes. After 15 minutes, the status will transition into the <code>SYNC_FAILED</code> state.</p> <p>To move an edge configuration from one device to another, use <a>DeleteEdgeConfiguration</a> to delete the current edge configuration. You can then invoke StartEdgeConfigurationUpdate with an updated Hub Device ARN.</p>

        Args:
            stream_name: <p>The name of the stream whose edge configuration you want to update. Specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            stream_arn: <p> The Amazon Resource Name (ARN) of the stream. Specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            edge_config: <p>The edge configuration details required to invoke the update process.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.no_data_retention_exception.NoDataRetentionException: <p>The Stream data retention in hours is equal to zero.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.start_edge_configuration_update_input.StartEdgeConfigurationUpdateInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.start_edge_configuration_update_output.StartEdgeConfigurationUpdateOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.start_edge_configuration_update

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.start_edge_configuration_update.async_start_edge_configuration_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.start_edge_configuration_update_input.StartEdgeConfigurationUpdateInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        input_["edge_config"] = edge_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN",
        tags: "aws_sdk_kinesis_video.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
    ) -> "aws_sdk_kinesis_video.types.tag_resource_output.TagResourceOutput":
        r"""<p>Adds one or more tags to a signaling channel. A <i>tag</i> is a key-value pair (the value is optional) that you can define and assign to Amazon Web Services resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. For more information, see <a href=\"https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\">Using Cost Allocation Tags</a> in the <i>Billing and Cost Management and Cost Management User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the signaling channel to which you want to add tags.</p>
            tags: <p>A list of tags to associate with the specified signaling channel. Each tag is a key-value pair.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.tags_per_resource_exceeded_limit_exception.TagsPerResourceExceededLimitException: <p>You have exceeded the limit of tags that you can associate with the resource. A Kinesis video stream can support up to 50 tags. </p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_stream(
        self,
        tags: "aws_sdk_kinesis_video.types.resource_tags.ResourceTags",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.tag_stream_output.TagStreamOutput":
        r"""<p>Adds one or more tags to a stream. A <i>tag</i> is a key-value pair (the value is optional) that you can define and assign to Amazon Web Services resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. For more information, see <a href=\"https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\">Using Cost Allocation Tags</a> in the <i>Billing and Cost Management and Cost Management User Guide</i>. </p> <p>You must provide either the <code>StreamName</code> or the <code>StreamARN</code>.</p> <p>This operation requires permission for the <code>KinesisVideo:TagStream</code> action.</p> <p>A Kinesis video stream can support up to 50 tags.</p>

        Args:
            stream_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to add the tag or tags to.</p>
            stream_name: <p>The name of the stream that you want to add the tag or tags to.</p>
            tags: <p>A list of tags to associate with the specified stream. Each tag is a key-value pair (the value is optional).</p>

        Raises:
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.invalid_resource_format_exception.InvalidResourceFormatException: <p>The format of the <code>StreamARN</code> is invalid.</p>
            aws_sdk_kinesis_video.errors.not_authorized_exception.NotAuthorizedException: <p>The caller is not authorized to perform this operation.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.tags_per_resource_exceeded_limit_exception.TagsPerResourceExceededLimitException: <p>You have exceeded the limit of tags that you can associate with the resource. A Kinesis video stream can support up to 50 tags. </p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.tag_stream_input.TagStreamInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.tag_stream_output.TagStreamOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.tag_stream

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.tag_stream.async_tag_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.tag_stream_input.TagStreamInput = {}  # type: ignore[typeddict-item]
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_name is not None:
            input_["stream_name"] = stream_name
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN",
        tag_key_list: "aws_sdk_kinesis_video.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
    ) -> "aws_sdk_kinesis_video.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tags from a signaling channel. In the request, specify only a tag key or keys; don't specify the value. If you specify a tag key that does not exist, it's ignored.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the signaling channel from which you want to remove tags.</p>
            tag_key_list: <p>A list of the keys of the tags that you want to remove.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_key_list"] = tag_key_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_stream(
        self,
        tag_key_list: "aws_sdk_kinesis_video.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.untag_stream_output.UntagStreamOutput":
        """<p>Removes one or more tags from a stream. In the request, specify only a tag key or keys; don't specify the value. If you specify a tag key that does not exist, it's ignored.</p> <p>In the request, you must provide the <code>StreamName</code> or <code>StreamARN</code>.</p>

        Args:
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream that you want to remove tags from.</p>
            stream_name: <p>The name of the stream that you want to remove tags from.</p>
            tag_key_list: <p>A list of the keys of the tags that you want to remove.</p>

        Raises:
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.invalid_resource_format_exception.InvalidResourceFormatException: <p>The format of the <code>StreamARN</code> is invalid.</p>
            aws_sdk_kinesis_video.errors.not_authorized_exception.NotAuthorizedException: <p>The caller is not authorized to perform this operation.</p>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.untag_stream_input.UntagStreamInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.untag_stream_output.UntagStreamOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.untag_stream

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.untag_stream.async_untag_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.untag_stream_input.UntagStreamInput = {}  # type: ignore[typeddict-item]
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if stream_name is not None:
            input_["stream_name"] = stream_name
        input_["tag_key_list"] = tag_key_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_data_retention(
        self,
        current_version: "aws_sdk_kinesis_video.types.version.Version",
        operation: "aws_sdk_kinesis_video.types.update_data_retention_operation.UpdateDataRetentionOperation",
        data_retention_change_in_hours: "aws_sdk_kinesis_video.types.data_retention_change_in_hours.DataRetentionChangeInHours",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.update_data_retention_output.UpdateDataRetentionOutput":
        """<p>Increases or decreases the stream's data retention period by the value that you specify. To indicate whether you want to increase or decrease the data retention period, specify the <code>Operation</code> parameter in the request body. In the request, you must specify either the <code>StreamName</code> or the <code>StreamARN</code>. </p> <p>This operation requires permission for the <code>KinesisVideo:UpdateDataRetention</code> action.</p> <p>Changing the data retention period affects the data in the stream as follows:</p> <ul> <li> <p>If the data retention period is increased, existing data is retained for the new retention period. For example, if the data retention period is increased from one hour to seven hours, all existing data is retained for seven hours.</p> </li> <li> <p>If the data retention period is decreased, existing data is retained for the new retention period. For example, if the data retention period is decreased from seven hours to one hour, all existing data is retained for one hour, and any data older than one hour is deleted immediately.</p> </li> </ul>

        Args:
            stream_name: <p>The name of the stream whose retention period you want to change.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream whose retention period you want to change.</p>
            current_version: <p>The version of the stream whose retention period you want to change. To get the version, call either the <code>DescribeStream</code> or the <code>ListStreams</code> API.</p>
            operation: <p>Indicates whether you want to increase or decrease the retention period.</p>
            data_retention_change_in_hours: <p>The number of hours to adjust the current retention by. The value you specify is added to or subtracted from the current value, depending on the <code>operation</code>.</p> <p>The minimum value for data retention is 0 and the maximum value is 87600 (ten years).</p>

        Raises:
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.not_authorized_exception.NotAuthorizedException: <p>The caller is not authorized to perform this operation.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.version_mismatch_exception.VersionMismatchException: <p>The stream version that you specified is not the latest version. To get the latest version, use the <a href=\"https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html\">DescribeStream</a> API.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.update_data_retention_input.UpdateDataRetentionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.update_data_retention_output.UpdateDataRetentionOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_data_retention

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_data_retention.async_update_data_retention(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.update_data_retention_input.UpdateDataRetentionInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        input_["current_version"] = current_version
        input_["operation"] = operation
        input_["data_retention_change_in_hours"] = data_retention_change_in_hours

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_image_generation_configuration(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
        image_generation_configuration: Optional[
            "aws_sdk_kinesis_video.types.image_generation_configuration.ImageGenerationConfiguration"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.update_image_generation_configuration_output.UpdateImageGenerationConfigurationOutput":
        """<p>Updates the <code>StreamInfo</code> and <code>ImageProcessingConfiguration</code> fields.</p>

        Args:
            stream_name: <p>The name of the stream from which to update the image generation configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the Kinesis video stream from where you want to update the image generation configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            image_generation_configuration: <p>The structure that contains the information required for the KVS images delivery. If the structure is null, the configuration will be deleted from the stream.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.no_data_retention_exception.NoDataRetentionException: <p>The Stream data retention in hours is equal to zero.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.update_image_generation_configuration_input.UpdateImageGenerationConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.update_image_generation_configuration_output.UpdateImageGenerationConfigurationOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_image_generation_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_image_generation_configuration.async_update_image_generation_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.update_image_generation_configuration_input.UpdateImageGenerationConfigurationInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if image_generation_configuration is not None:
            input_["image_generation_configuration"] = image_generation_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_media_storage_configuration(
        self,
        channel_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN",
        media_storage_configuration: "aws_sdk_kinesis_video.types.media_storage_configuration.MediaStorageConfiguration",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
    ) -> "aws_sdk_kinesis_video.types.update_media_storage_configuration_output.UpdateMediaStorageConfigurationOutput":
        """<p>Associates a <code>SignalingChannel</code> to a stream to store the media. There are two signaling modes that you can specify :</p> <ul> <li> <p>If <code>StorageStatus</code> is enabled, the data will be stored in the <code>StreamARN</code> provided. In order for WebRTC Ingestion to work, the stream must have data retention enabled.</p> </li> <li> <p>If <code>StorageStatus</code> is disabled, no data will be stored, and the <code>StreamARN</code> parameter will not be needed. </p> </li> </ul> <important> <p>If <code>StorageStatus</code> is enabled, direct peer-to-peer (master-viewer) connections no longer occur. Peers connect directly to the storage session. You must call the <code>JoinStorageSession</code> API to trigger an SDP offer send and establish a connection between a peer and the storage session. </p> </important>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the channel.</p>
            media_storage_configuration: <p>A structure that encapsulates, or contains, the media storage configuration properties.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.no_data_retention_exception.NoDataRetentionException: <p>The Stream data retention in hours is equal to zero.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.update_media_storage_configuration_input.UpdateMediaStorageConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.update_media_storage_configuration_output.UpdateMediaStorageConfigurationOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_media_storage_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_media_storage_configuration.async_update_media_storage_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.update_media_storage_configuration_input.UpdateMediaStorageConfigurationInput = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["media_storage_configuration"] = media_storage_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_notification_configuration(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
        notification_configuration: Optional[
            "aws_sdk_kinesis_video.types.notification_configuration.NotificationConfiguration"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.update_notification_configuration_output.UpdateNotificationConfigurationOutput":
        """<p>Updates the notification information for a stream.</p>

        Args:
            stream_name: <p>The name of the stream from which to update the notification configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the Kinesis video stream from where you want to update the notification configuration. You must specify either the <code>StreamName</code> or the <code>StreamARN</code>.</p>
            notification_configuration: <p>The structure containing the information required for notifications. If the structure is null, the configuration will be deleted from the stream.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.no_data_retention_exception.NoDataRetentionException: <p>The Stream data retention in hours is equal to zero.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.update_notification_configuration_input.UpdateNotificationConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.update_notification_configuration_output.UpdateNotificationConfigurationOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_notification_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_notification_configuration.async_update_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.update_notification_configuration_input.UpdateNotificationConfigurationInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        if notification_configuration is not None:
            input_["notification_configuration"] = notification_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_signaling_channel(
        self,
        channel_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN",
        current_version: "aws_sdk_kinesis_video.types.version.Version",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        single_master_configuration: Optional[
            "aws_sdk_kinesis_video.types.single_master_configuration.SingleMasterConfiguration"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.update_signaling_channel_output.UpdateSignalingChannelOutput":
        """<p>Updates the existing signaling channel. This is an asynchronous operation and takes time to complete. </p> <p>If the <code>MessageTtlSeconds</code> value is updated (either increased or reduced), it only applies to new messages sent via this channel after it's been updated. Existing messages are still expired as per the previous <code>MessageTtlSeconds</code> value.</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the signaling channel that you want to update.</p>
            current_version: <p>The current version of the signaling channel that you want to update.</p>
            single_master_configuration: <p>The structure containing the configuration for the <code>SINGLE_MASTER</code> type of the signaling channel that you want to update. This parameter and the channel message's time-to-live are required for channels with the <code>SINGLE_MASTER</code> channel type.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.version_mismatch_exception.VersionMismatchException: <p>The stream version that you specified is not the latest version. To get the latest version, use the <a href=\"https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html\">DescribeStream</a> API.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.update_signaling_channel_input.UpdateSignalingChannelInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.update_signaling_channel_output.UpdateSignalingChannelOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_signaling_channel

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_signaling_channel.async_update_signaling_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.update_signaling_channel_input.UpdateSignalingChannelInput = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["current_version"] = current_version
        if single_master_configuration is not None:
            input_["single_master_configuration"] = single_master_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_stream(
        self,
        current_version: "aws_sdk_kinesis_video.types.version.Version",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
        device_name: Optional[
            "aws_sdk_kinesis_video.types.device_name.DeviceName"
        ] = None,
        media_type: Optional["aws_sdk_kinesis_video.types.media_type.MediaType"] = None,
    ) -> "aws_sdk_kinesis_video.types.update_stream_output.UpdateStreamOutput":
        r"""<p>Updates stream metadata, such as the device name and media type.</p> <p>You must provide the stream name or the Amazon Resource Name (ARN) of the stream.</p> <p>To make sure that you have the latest version of the stream before updating it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the <code>DescribeStream</code> API. </p> <p> <code>UpdateStream</code> is an asynchronous operation, and takes time to complete.</p>

        Args:
            stream_name: <p>The name of the stream whose metadata you want to update.</p> <p>The stream name is an identifier for the stream, and must be unique for each account and region.</p>
            stream_arn: <p>The ARN of the stream whose metadata you want to update.</p>
            current_version: <p>The version of the stream whose metadata you want to update.</p>
            device_name: <p>The name of the device that is writing to the stream. </p> <note> <p> In the current implementation, Kinesis Video Streams does not use this name. </p> </note>
            media_type: <p>The stream's media type. Use <code>MediaType</code> to specify the type of content that the stream contains to the consumers of the stream. For more information about media types, see <a href=\"http://www.iana.org/assignments/media-types/media-types.xhtml\">Media Types</a>. If you choose to specify the <code>MediaType</code>, see <a href=\"https://tools.ietf.org/html/rfc6838#section-4.2\">Naming Requirements</a>.</p> <p>To play video on the console, you must specify the correct video type. For example, if the video in the stream is H.264, specify <code>video/h264</code> as the <code>MediaType</code>.</p>

        Raises:
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.not_authorized_exception.NotAuthorizedException: <p>The caller is not authorized to perform this operation.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.version_mismatch_exception.VersionMismatchException: <p>The stream version that you specified is not the latest version. To get the latest version, use the <a href=\"https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html\">DescribeStream</a> API.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.update_stream_input.UpdateStreamInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.update_stream_output.UpdateStreamOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_stream

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_stream.async_update_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.update_stream_input.UpdateStreamInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        input_["current_version"] = current_version
        if device_name is not None:
            input_["device_name"] = device_name
        if media_type is not None:
            input_["media_type"] = media_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_stream_storage_configuration(
        self,
        current_version: "aws_sdk_kinesis_video.types.version.Version",
        stream_storage_configuration: "aws_sdk_kinesis_video.types.stream_storage_configuration.StreamStorageConfiguration",
        *,
        config_overrides: Optional[AsyncKinesisVideoClientConfig] = None,
        stream_name: Optional[
            "aws_sdk_kinesis_video.types.stream_name.StreamName"
        ] = None,
        stream_arn: Optional[
            "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
        ] = None,
    ) -> "aws_sdk_kinesis_video.types.update_stream_storage_configuration_output.UpdateStreamStorageConfigurationOutput":
        """<p>Updates the storage configuration for an existing Kinesis video stream.</p> <p>This operation allows you to modify the storage tier settings for a stream, enabling you to optimize storage costs and performance based on your access patterns.</p> <p> <code>UpdateStreamStorageConfiguration</code> is an asynchronous operation.</p> <p>You must have permissions for the <code>KinesisVideo:UpdateStreamStorageConfiguration</code> action.</p>

        Args:
            stream_name: <p>The name of the stream for which you want to update the storage configuration.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) of the stream for which you want to update the storage configuration.</p>
            current_version: <p>The version of the stream whose storage configuration you want to change. To get the version, call either the <code>DescribeStream</code> or the <code>ListStreams</code> API.</p>
            stream_storage_configuration: <p>The new storage configuration for the stream. This includes the default storage tier that determines how stream data is stored and accessed.</p> <p>Different storage tiers offer varying levels of performance and cost optimization to match your specific use case requirements.</p>

        Raises:
            aws_sdk_kinesis_video.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            aws_sdk_kinesis_video.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            aws_sdk_kinesis_video.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            aws_sdk_kinesis_video.errors.resource_in_use_exception.ResourceInUseException: <p>When the input <code>StreamARN</code> or <code>ChannelARN</code> in <code>CLOUD_STORAGE_MODE</code> is already mapped to a different Kinesis Video Stream resource, or if the provided input <code>StreamARN</code> or <code>ChannelARN</code> is not in Active status, try one of the following : </p> <ol> <li> <p>The <code>DescribeMediaStorageConfiguration</code> API to determine what the stream given channel is mapped to. </p> </li> <li> <p>The <code>DescribeMappedResourceConfiguration</code> API to determine the channel that the given stream is mapped to. </p> </li> <li> <p>The <code>DescribeStream</code> or <code>DescribeSignalingChannel</code> API to determine the status of the resource. </p> </li> </ol>
            aws_sdk_kinesis_video.errors.resource_not_found_exception.ResourceNotFoundException: <p>Amazon Kinesis Video Streams can't find the stream that you specified.</p>
            aws_sdk_kinesis_video.errors.version_mismatch_exception.VersionMismatchException: <p>The stream version that you specified is not the latest version. To get the latest version, use the <a href=\"https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html\">DescribeStream</a> API.</p>
            aws_sdk_kinesis_video.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_kinesis_video.types.update_stream_storage_configuration_input.UpdateStreamStorageConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_kinesis_video.types.update_stream_storage_configuration_output.UpdateStreamStorageConfigurationOutput"
        ]:
            import aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_stream_storage_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_kinesis_video._operations.kinesis_video_20170930.update_stream_storage_configuration.async_update_stream_storage_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_kinesis_video.types.update_stream_storage_configuration_input.UpdateStreamStorageConfigurationInput = {}  # type: ignore[typeddict-item]
        if stream_name is not None:
            input_["stream_name"] = stream_name
        if stream_arn is not None:
            input_["stream_arn"] = stream_arn
        input_["current_version"] = current_version
        input_["stream_storage_configuration"] = stream_storage_configuration

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
