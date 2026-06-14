"""Generated from Smithy shape ``com.amazonaws.ivs#AmazonInteractiveVideoService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_ivs._auth._signers
import aws_sdk_ivs._auth._sigv4
from aws_sdk_ivs._auth._identity import Credentials
from aws_sdk_ivs._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_ivs._auth._zapros_handler import AuthMiddleware
from aws_sdk_ivs._pagination import resolve_path as _resolve_path
from aws_sdk_ivs._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_ivs.types.ad_configuration_arn
    import aws_sdk_ivs.types.ad_configuration_name
    import aws_sdk_ivs.types.ad_configuration_summary
    import aws_sdk_ivs.types.ad_duration_seconds
    import aws_sdk_ivs.types.batch_get_channel_request
    import aws_sdk_ivs.types.batch_get_channel_response
    import aws_sdk_ivs.types.batch_get_stream_key_request
    import aws_sdk_ivs.types.batch_get_stream_key_response
    import aws_sdk_ivs.types.batch_start_viewer_session_revocation_request
    import aws_sdk_ivs.types.batch_start_viewer_session_revocation_response
    import aws_sdk_ivs.types.batch_start_viewer_session_revocation_viewer_session_list
    import aws_sdk_ivs.types.boolean
    import aws_sdk_ivs.types.channel_ad_configuration_arn
    import aws_sdk_ivs.types.channel_arn
    import aws_sdk_ivs.types.channel_arn_list
    import aws_sdk_ivs.types.channel_latency_mode
    import aws_sdk_ivs.types.channel_name
    import aws_sdk_ivs.types.channel_playback_restriction_policy_arn
    import aws_sdk_ivs.types.channel_recording_configuration_arn
    import aws_sdk_ivs.types.channel_type
    import aws_sdk_ivs.types.container_format
    import aws_sdk_ivs.types.create_ad_configuration_request
    import aws_sdk_ivs.types.create_ad_configuration_response
    import aws_sdk_ivs.types.create_channel_request
    import aws_sdk_ivs.types.create_channel_response
    import aws_sdk_ivs.types.create_playback_restriction_policy_request
    import aws_sdk_ivs.types.create_playback_restriction_policy_response
    import aws_sdk_ivs.types.create_recording_configuration_request
    import aws_sdk_ivs.types.create_recording_configuration_response
    import aws_sdk_ivs.types.create_stream_key_request
    import aws_sdk_ivs.types.create_stream_key_response
    import aws_sdk_ivs.types.delete_ad_configuration_request
    import aws_sdk_ivs.types.delete_channel_request
    import aws_sdk_ivs.types.delete_playback_key_pair_request
    import aws_sdk_ivs.types.delete_playback_key_pair_response
    import aws_sdk_ivs.types.delete_playback_restriction_policy_request
    import aws_sdk_ivs.types.delete_recording_configuration_request
    import aws_sdk_ivs.types.delete_stream_key_request
    import aws_sdk_ivs.types.destination_configuration
    import aws_sdk_ivs.types.get_ad_configuration_request
    import aws_sdk_ivs.types.get_ad_configuration_response
    import aws_sdk_ivs.types.get_channel_request
    import aws_sdk_ivs.types.get_channel_response
    import aws_sdk_ivs.types.get_playback_key_pair_request
    import aws_sdk_ivs.types.get_playback_key_pair_response
    import aws_sdk_ivs.types.get_playback_restriction_policy_request
    import aws_sdk_ivs.types.get_playback_restriction_policy_response
    import aws_sdk_ivs.types.get_recording_configuration_request
    import aws_sdk_ivs.types.get_recording_configuration_response
    import aws_sdk_ivs.types.get_stream_key_request
    import aws_sdk_ivs.types.get_stream_key_response
    import aws_sdk_ivs.types.get_stream_request
    import aws_sdk_ivs.types.get_stream_response
    import aws_sdk_ivs.types.get_stream_session_request
    import aws_sdk_ivs.types.get_stream_session_response
    import aws_sdk_ivs.types.import_playback_key_pair_request
    import aws_sdk_ivs.types.import_playback_key_pair_response
    import aws_sdk_ivs.types.insert_ad_break_request
    import aws_sdk_ivs.types.insert_ad_break_response
    import aws_sdk_ivs.types.list_ad_configurations_request
    import aws_sdk_ivs.types.list_ad_configurations_response
    import aws_sdk_ivs.types.list_channels_request
    import aws_sdk_ivs.types.list_channels_response
    import aws_sdk_ivs.types.list_playback_key_pairs_request
    import aws_sdk_ivs.types.list_playback_key_pairs_response
    import aws_sdk_ivs.types.list_playback_restriction_policies_request
    import aws_sdk_ivs.types.list_playback_restriction_policies_response
    import aws_sdk_ivs.types.list_recording_configurations_request
    import aws_sdk_ivs.types.list_recording_configurations_response
    import aws_sdk_ivs.types.list_stream_keys_request
    import aws_sdk_ivs.types.list_stream_keys_response
    import aws_sdk_ivs.types.list_stream_sessions_request
    import aws_sdk_ivs.types.list_stream_sessions_response
    import aws_sdk_ivs.types.list_streams_request
    import aws_sdk_ivs.types.list_streams_response
    import aws_sdk_ivs.types.list_tags_for_resource_request
    import aws_sdk_ivs.types.list_tags_for_resource_response
    import aws_sdk_ivs.types.max_ad_configuration_results
    import aws_sdk_ivs.types.max_channel_results
    import aws_sdk_ivs.types.max_playback_key_pair_results
    import aws_sdk_ivs.types.max_playback_restriction_policy_results
    import aws_sdk_ivs.types.max_recording_configuration_results
    import aws_sdk_ivs.types.max_stream_key_results
    import aws_sdk_ivs.types.max_stream_results
    import aws_sdk_ivs.types.media_tailor_playback_configurations_list
    import aws_sdk_ivs.types.multitrack_input_configuration
    import aws_sdk_ivs.types.pagination_token
    import aws_sdk_ivs.types.playback_key_pair_arn
    import aws_sdk_ivs.types.playback_key_pair_name
    import aws_sdk_ivs.types.playback_public_key_material
    import aws_sdk_ivs.types.playback_restriction_policy_allowed_country_list
    import aws_sdk_ivs.types.playback_restriction_policy_allowed_origin_list
    import aws_sdk_ivs.types.playback_restriction_policy_arn
    import aws_sdk_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement
    import aws_sdk_ivs.types.playback_restriction_policy_name
    import aws_sdk_ivs.types.put_metadata_request
    import aws_sdk_ivs.types.recording_configuration_arn
    import aws_sdk_ivs.types.recording_configuration_name
    import aws_sdk_ivs.types.recording_reconnect_window_seconds
    import aws_sdk_ivs.types.rendition_configuration
    import aws_sdk_ivs.types.resource_arn
    import aws_sdk_ivs.types.start_viewer_session_revocation_request
    import aws_sdk_ivs.types.start_viewer_session_revocation_response
    import aws_sdk_ivs.types.stop_stream_request
    import aws_sdk_ivs.types.stop_stream_response
    import aws_sdk_ivs.types.stream_filters
    import aws_sdk_ivs.types.stream_id
    import aws_sdk_ivs.types.stream_key_arn
    import aws_sdk_ivs.types.stream_key_arn_list
    import aws_sdk_ivs.types.stream_metadata
    import aws_sdk_ivs.types.tag_key_list
    import aws_sdk_ivs.types.tag_resource_request
    import aws_sdk_ivs.types.tag_resource_response
    import aws_sdk_ivs.types.tags
    import aws_sdk_ivs.types.thumbnail_configuration
    import aws_sdk_ivs.types.transcode_preset
    import aws_sdk_ivs.types.untag_resource_request
    import aws_sdk_ivs.types.untag_resource_response
    import aws_sdk_ivs.types.update_ad_configuration_request
    import aws_sdk_ivs.types.update_ad_configuration_response
    import aws_sdk_ivs.types.update_channel_request
    import aws_sdk_ivs.types.update_channel_response
    import aws_sdk_ivs.types.update_playback_restriction_policy_request
    import aws_sdk_ivs.types.update_playback_restriction_policy_response
    import aws_sdk_ivs.types.viewer_id
    import aws_sdk_ivs.types.viewer_session_version


class ivsClientConfig(TypedDict, total=False):
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


class ivsClient:
    """A client for the ``ivs`` service.

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
        self.config = ivsClientConfig(
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
        self, config_overrides: Optional[ivsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ivsClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def batch_get_channel(
        self,
        arns: "aws_sdk_ivs.types.channel_arn_list.ChannelArnList",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.batch_get_channel_response.BatchGetChannelResponse":
        """<p>Performs <a>GetChannel</a> on multiple ARNs simultaneously.</p>

        Args:
            arns: <p>Array of ARNs, one per channel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.batch_get_channel_request.BatchGetChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.batch_get_channel_response.BatchGetChannelResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.batch_get_channel

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.batch_get_channel.batch_get_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.batch_get_channel_request.BatchGetChannelRequest = {}  # type: ignore[typeddict-item]
        input_["arns"] = arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_get_stream_key(
        self,
        arns: "aws_sdk_ivs.types.stream_key_arn_list.StreamKeyArnList",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.batch_get_stream_key_response.BatchGetStreamKeyResponse":
        """<p>Performs <a>GetStreamKey</a> on multiple ARNs simultaneously.</p>

        Args:
            arns: <p>Array of ARNs, one per stream key.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.batch_get_stream_key_request.BatchGetStreamKeyRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.batch_get_stream_key_response.BatchGetStreamKeyResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.batch_get_stream_key

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.batch_get_stream_key.batch_get_stream_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.batch_get_stream_key_request.BatchGetStreamKeyRequest = {}  # type: ignore[typeddict-item]
        input_["arns"] = arns

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_start_viewer_session_revocation(
        self,
        viewer_sessions: "aws_sdk_ivs.types.batch_start_viewer_session_revocation_viewer_session_list.BatchStartViewerSessionRevocationViewerSessionList",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.batch_start_viewer_session_revocation_response.BatchStartViewerSessionRevocationResponse":
        """<p>Performs <a>StartViewerSessionRevocation</a> on multiple channel ARN and viewer ID pairs simultaneously.</p>

        Args:
            viewer_sessions: <p>Array of viewer sessions, one per channel-ARN and viewer-ID pair.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.batch_start_viewer_session_revocation_request.BatchStartViewerSessionRevocationRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.batch_start_viewer_session_revocation_response.BatchStartViewerSessionRevocationResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.batch_start_viewer_session_revocation

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.batch_start_viewer_session_revocation.batch_start_viewer_session_revocation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.batch_start_viewer_session_revocation_request.BatchStartViewerSessionRevocationRequest = {}  # type: ignore[typeddict-item]
        input_["viewer_sessions"] = viewer_sessions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_ad_configuration(
        self,
        media_tailor_playback_configurations: "aws_sdk_ivs.types.media_tailor_playback_configurations_list.MediaTailorPlaybackConfigurationsList",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional[
            "aws_sdk_ivs.types.ad_configuration_name.AdConfigurationName"
        ] = None,
        tags: Optional["aws_sdk_ivs.types.tags.Tags"] = None,
    ) -> "aws_sdk_ivs.types.create_ad_configuration_response.CreateAdConfigurationResponse":
        """<p>Creates a new ad configuration to be used for server-side ad insertion.</p>

        Args:
            name: <p>Ad configuration name. Defaults to “”.</p>
            media_tailor_playback_configurations: <p>List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see <a href=\"https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html\">Generate and Sign IVS Playback Tokens</a>.</p>
            tags: <p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.create_ad_configuration_request.CreateAdConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.create_ad_configuration_response.CreateAdConfigurationResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.create_ad_configuration

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.create_ad_configuration.create_ad_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.create_ad_configuration_request.CreateAdConfigurationRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        input_["media_tailor_playback_configurations"] = (
            media_tailor_playback_configurations
        )
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_channel(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional["aws_sdk_ivs.types.channel_name.ChannelName"] = None,
        latency_mode: Optional[
            "aws_sdk_ivs.types.channel_latency_mode.ChannelLatencyMode"
        ] = None,
        type: Optional["aws_sdk_ivs.types.channel_type.ChannelType"] = None,
        authorized: Optional["aws_sdk_ivs.types.boolean.Boolean"] = None,
        recording_configuration_arn: Optional[
            "aws_sdk_ivs.types.channel_recording_configuration_arn.ChannelRecordingConfigurationArn"
        ] = None,
        tags: Optional["aws_sdk_ivs.types.tags.Tags"] = None,
        insecure_ingest: Optional["aws_sdk_ivs.types.boolean.Boolean"] = None,
        preset: Optional["aws_sdk_ivs.types.transcode_preset.TranscodePreset"] = None,
        playback_restriction_policy_arn: Optional[
            "aws_sdk_ivs.types.channel_playback_restriction_policy_arn.ChannelPlaybackRestrictionPolicyArn"
        ] = None,
        multitrack_input_configuration: Optional[
            "aws_sdk_ivs.types.multitrack_input_configuration.MultitrackInputConfiguration"
        ] = None,
        container_format: Optional[
            "aws_sdk_ivs.types.container_format.ContainerFormat"
        ] = None,
        ad_configuration_arn: Optional[
            "aws_sdk_ivs.types.channel_ad_configuration_arn.ChannelAdConfigurationArn"
        ] = None,
    ) -> "aws_sdk_ivs.types.create_channel_response.CreateChannelResponse":
        """<p>Creates a new channel and an associated stream key to start streaming.</p>

        Args:
            name: <p>Channel name.</p>
            latency_mode: <p>Channel latency mode. Use <code>NORMAL</code> to broadcast and deliver live video up to Full HD. Use <code>LOW</code> for near-real-time interaction with viewers. Default: <code>LOW</code>.</p>
            type: <p>Channel type, which determines the allowable resolution and bitrate. <i>If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.</i> Default: <code>STANDARD</code>. For details, see <a href=\"https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/channel-types.html\">Channel Types</a>.</p>
            authorized: <p>Whether the channel is private (enabled for playback authorization). Default: <code>false</code>.</p>
            recording_configuration_arn: <p>Recording-configuration ARN. A valid ARN value here both specifies the ARN and enables recording. Default: \"\" (empty string, recording is disabled).</p>
            tags: <p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>
            insecure_ingest: <p>Whether the channel allows insecure RTMP and SRT ingest. Default: <code>false</code>.</p>
            preset: <p>Optional transcode preset for the channel. This is selectable only for <code>ADVANCED_HD</code> and <code>ADVANCED_SD</code> channel types. For those channel types, the default <code>preset</code> is <code>HIGHER_BANDWIDTH_DELIVERY</code>. For other channel types (<code>BASIC</code> and <code>STANDARD</code>), <code>preset</code> is the empty string (<code>\"\"</code>).</p>
            playback_restriction_policy_arn: <p>Playback-restriction-policy ARN. A valid ARN value here both specifies the ARN and enables playback restriction. Default: \"\" (empty string, no playback restriction policy is applied).</p>
            multitrack_input_configuration: <p>Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.</p>
            container_format: <p>Indicates which content-packaging format is used (MPEG-TS or fMP4). If <code>multitrackInputConfiguration</code> is specified and <code>enabled</code> is <code>true</code>, then <code>containerFormat</code> is required and must be set to <code>FRAGMENTED_MP4</code>. Otherwise, <code>containerFormat</code> may be set to <code>TS</code> or <code>FRAGMENTED_MP4</code>. Default: <code>TS</code>.</p>
            ad_configuration_arn: <p>ARN of the ad configuration associated with the channel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.create_channel_response.CreateChannelResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.create_channel

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.create_channel_request.CreateChannelRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        if latency_mode is not None:
            input_["latency_mode"] = latency_mode
        if type is not None:
            input_["type"] = type
        if authorized is not None:
            input_["authorized"] = authorized
        if recording_configuration_arn is not None:
            input_["recording_configuration_arn"] = recording_configuration_arn
        if tags is not None:
            input_["tags"] = tags
        if insecure_ingest is not None:
            input_["insecure_ingest"] = insecure_ingest
        if preset is not None:
            input_["preset"] = preset
        if playback_restriction_policy_arn is not None:
            input_["playback_restriction_policy_arn"] = playback_restriction_policy_arn
        if multitrack_input_configuration is not None:
            input_["multitrack_input_configuration"] = multitrack_input_configuration
        if container_format is not None:
            input_["container_format"] = container_format
        if ad_configuration_arn is not None:
            input_["ad_configuration_arn"] = ad_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_playback_restriction_policy(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        allowed_countries: Optional[
            "aws_sdk_ivs.types.playback_restriction_policy_allowed_country_list.PlaybackRestrictionPolicyAllowedCountryList"
        ] = None,
        allowed_origins: Optional[
            "aws_sdk_ivs.types.playback_restriction_policy_allowed_origin_list.PlaybackRestrictionPolicyAllowedOriginList"
        ] = None,
        enable_strict_origin_enforcement: Optional[
            "aws_sdk_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement.PlaybackRestrictionPolicyEnableStrictOriginEnforcement"
        ] = None,
        name: Optional[
            "aws_sdk_ivs.types.playback_restriction_policy_name.PlaybackRestrictionPolicyName"
        ] = None,
        tags: Optional["aws_sdk_ivs.types.tags.Tags"] = None,
    ) -> "aws_sdk_ivs.types.create_playback_restriction_policy_response.CreatePlaybackRestrictionPolicyResponse":
        """<p>Creates a new playback restriction policy, for constraining playback by countries and/or origins.</p>

        Args:
            allowed_countries: <p>A list of country codes that control geoblocking restriction. Allowed values are the officially assigned <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\">ISO 3166-1 alpha-2</a> codes. Default: All countries (an empty array).</p>
            allowed_origins: <p>A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin\">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin</a>. Default: All origins (an empty array).</p>
            enable_strict_origin_enforcement: <p>Whether channel playback is constrained by origin site. Default: <code>false</code>.</p>
            name: <p>Playback-restriction-policy name. The value does not need to be unique.</p>
            tags: <p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.create_playback_restriction_policy_request.CreatePlaybackRestrictionPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.create_playback_restriction_policy_response.CreatePlaybackRestrictionPolicyResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.create_playback_restriction_policy

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.create_playback_restriction_policy.create_playback_restriction_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.create_playback_restriction_policy_request.CreatePlaybackRestrictionPolicyRequest = {}  # type: ignore[typeddict-item]
        if allowed_countries is not None:
            input_["allowed_countries"] = allowed_countries
        if allowed_origins is not None:
            input_["allowed_origins"] = allowed_origins
        if enable_strict_origin_enforcement is not None:
            input_["enable_strict_origin_enforcement"] = (
                enable_strict_origin_enforcement
            )
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_recording_configuration(
        self,
        destination_configuration: "aws_sdk_ivs.types.destination_configuration.DestinationConfiguration",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional[
            "aws_sdk_ivs.types.recording_configuration_name.RecordingConfigurationName"
        ] = None,
        tags: Optional["aws_sdk_ivs.types.tags.Tags"] = None,
        thumbnail_configuration: Optional[
            "aws_sdk_ivs.types.thumbnail_configuration.ThumbnailConfiguration"
        ] = None,
        recording_reconnect_window_seconds: Optional[
            "aws_sdk_ivs.types.recording_reconnect_window_seconds.RecordingReconnectWindowSeconds"
        ] = None,
        rendition_configuration: Optional[
            "aws_sdk_ivs.types.rendition_configuration.RenditionConfiguration"
        ] = None,
    ) -> "aws_sdk_ivs.types.create_recording_configuration_response.CreateRecordingConfigurationResponse":
        """<p>Creates a new recording configuration, used to enable recording to Amazon S3.</p> <p> <b>Known issue:</b> In the us-east-1 region, if you use the Amazon Web Services CLI to create a recording configuration, it returns success even if the S3 bucket is in a different region. In this case, the <code>state</code> of the recording configuration is <code>CREATE_FAILED</code> (instead of <code>ACTIVE</code>). (In other regions, the CLI correctly returns failure if the bucket is in a different region.)</p> <p> <b>Workaround:</b> Ensure that your S3 bucket is in the same region as the recording configuration. If you create a recording configuration in a different region as your S3 bucket, delete that recording configuration and create a new one with an S3 bucket from the correct region.</p>

        Args:
            name: <p>Recording-configuration name. The value does not need to be unique.</p>
            destination_configuration: <p>A complex type that contains a destination configuration for where recorded video will be stored.</p>
            tags: <p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>
            thumbnail_configuration: <p>A complex type that allows you to enable/disable the recording of thumbnails for a live session and modify the interval at which thumbnails are generated for the live session.</p>
            recording_reconnect_window_seconds: <p>If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. Default: 0.</p>
            rendition_configuration: <p>Object that describes which renditions should be recorded for a stream.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.create_recording_configuration_request.CreateRecordingConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.create_recording_configuration_response.CreateRecordingConfigurationResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.create_recording_configuration

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.create_recording_configuration.create_recording_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.create_recording_configuration_request.CreateRecordingConfigurationRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        input_["destination_configuration"] = destination_configuration
        if tags is not None:
            input_["tags"] = tags
        if thumbnail_configuration is not None:
            input_["thumbnail_configuration"] = thumbnail_configuration
        if recording_reconnect_window_seconds is not None:
            input_["recording_reconnect_window_seconds"] = (
                recording_reconnect_window_seconds
            )
        if rendition_configuration is not None:
            input_["rendition_configuration"] = rendition_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_stream_key(
        self,
        channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        tags: Optional["aws_sdk_ivs.types.tags.Tags"] = None,
    ) -> "aws_sdk_ivs.types.create_stream_key_response.CreateStreamKeyResponse":
        """<p>Creates a stream key, used to initiate a stream, for the specified channel ARN.</p> <p>Note that <a>CreateChannel</a> creates a stream key. If you subsequently use CreateStreamKey on the same channel, it will fail because a stream key already exists and there is a limit of 1 stream key per channel. To reset the stream key on a channel, use <a>DeleteStreamKey</a> and then CreateStreamKey.</p>

        Args:
            channel_arn: <p>ARN of the channel for which to create the stream key.</p>
            tags: <p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.create_stream_key_request.CreateStreamKeyRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.create_stream_key_response.CreateStreamKeyResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.create_stream_key

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.create_stream_key.create_stream_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.create_stream_key_request.CreateStreamKeyRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_ad_configuration(
        self,
        arn: "aws_sdk_ivs.types.ad_configuration_arn.AdConfigurationArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified ad configuration.</p>

        Args:
            arn: <p>ARN of the ad configuration to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.delete_ad_configuration_request.DeleteAdConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.delete_ad_configuration

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.delete_ad_configuration.delete_ad_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.delete_ad_configuration_request.DeleteAdConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_channel(
        self,
        arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified channel and its associated stream keys.</p> <p>If you try to delete a live channel, you will get an error (409 ConflictException). To delete a channel that is live, call <a>StopStream</a>, wait for the Amazon EventBridge \"Stream End\" event (to verify that the stream's state is no longer Live), then call DeleteChannel. (See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html\"> Using EventBridge with Amazon IVS</a>.) </p>

        Args:
            arn: <p>ARN of the channel to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.delete_channel_request.DeleteChannelRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.delete_channel

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.delete_channel_request.DeleteChannelRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_playback_key_pair(
        self,
        arn: "aws_sdk_ivs.types.playback_key_pair_arn.PlaybackKeyPairArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.delete_playback_key_pair_response.DeletePlaybackKeyPairResponse":
        """<p>Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s <code>privateKey</code>. For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p>

        Args:
            arn: <p>ARN of the key pair to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.delete_playback_key_pair_request.DeletePlaybackKeyPairRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.delete_playback_key_pair_response.DeletePlaybackKeyPairResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.delete_playback_key_pair

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.delete_playback_key_pair.delete_playback_key_pair(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.delete_playback_key_pair_request.DeletePlaybackKeyPairRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_playback_restriction_policy(
        self,
        arn: "aws_sdk_ivs.types.playback_restriction_policy_arn.PlaybackRestrictionPolicyArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified playback restriction policy.</p>

        Args:
            arn: <p>ARN of the playback restriction policy to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.delete_playback_restriction_policy_request.DeletePlaybackRestrictionPolicyRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.delete_playback_restriction_policy

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.delete_playback_restriction_policy.delete_playback_restriction_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.delete_playback_restriction_policy_request.DeletePlaybackRestrictionPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_recording_configuration(
        self,
        arn: "aws_sdk_ivs.types.recording_configuration_arn.RecordingConfigurationArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Deletes the recording configuration for the specified ARN.</p> <p>If you try to delete a recording configuration that is associated with a channel, you will get an error (409 ConflictException). To avoid this, for all channels that reference the recording configuration, first use <a>UpdateChannel</a> to set the <code>recordingConfigurationArn</code> field to an empty string, then use DeleteRecordingConfiguration.</p>

        Args:
            arn: <p>ARN of the recording configuration to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.delete_recording_configuration_request.DeleteRecordingConfigurationRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.delete_recording_configuration

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.delete_recording_configuration.delete_recording_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.delete_recording_configuration_request.DeleteRecordingConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_stream_key(
        self,
        arn: "aws_sdk_ivs.types.stream_key_arn.StreamKeyArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Deletes the stream key for the specified ARN, so it can no longer be used to stream.</p>

        Args:
            arn: <p>ARN of the stream key to be deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.delete_stream_key_request.DeleteStreamKeyRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.delete_stream_key

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.delete_stream_key.delete_stream_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.delete_stream_key_request.DeleteStreamKeyRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_ad_configuration(
        self,
        arn: "aws_sdk_ivs.types.ad_configuration_arn.AdConfigurationArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.get_ad_configuration_response.GetAdConfigurationResponse":
        """<p>Gets the ad configuration represented by the specified ARN.</p>

        Args:
            arn: <p>ARN of the ad configuration to be retrieved.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.get_ad_configuration_request.GetAdConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.get_ad_configuration_response.GetAdConfigurationResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.get_ad_configuration

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.get_ad_configuration.get_ad_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.get_ad_configuration_request.GetAdConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_channel(
        self,
        arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.get_channel_response.GetChannelResponse":
        """<p>Gets the channel configuration for the specified channel ARN. See also <a>BatchGetChannel</a>.</p>

        Args:
            arn: <p>ARN of the channel for which the configuration is to be retrieved.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.get_channel_request.GetChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.get_channel_response.GetChannelResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.get_channel

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.get_channel.get_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.get_channel_request.GetChannelRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_playback_key_pair(
        self,
        arn: "aws_sdk_ivs.types.playback_key_pair_arn.PlaybackKeyPairArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.get_playback_key_pair_response.GetPlaybackKeyPairResponse":
        """<p>Gets a specified playback authorization key pair and returns the <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p>

        Args:
            arn: <p>ARN of the key pair to be returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.get_playback_key_pair_request.GetPlaybackKeyPairRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.get_playback_key_pair_response.GetPlaybackKeyPairResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.get_playback_key_pair

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.get_playback_key_pair.get_playback_key_pair(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.get_playback_key_pair_request.GetPlaybackKeyPairRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_playback_restriction_policy(
        self,
        arn: "aws_sdk_ivs.types.playback_restriction_policy_arn.PlaybackRestrictionPolicyArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.get_playback_restriction_policy_response.GetPlaybackRestrictionPolicyResponse":
        """<p>Gets the specified playback restriction policy.</p>

        Args:
            arn: <p>ARN of the playback restriction policy to be returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.get_playback_restriction_policy_request.GetPlaybackRestrictionPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.get_playback_restriction_policy_response.GetPlaybackRestrictionPolicyResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.get_playback_restriction_policy

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.get_playback_restriction_policy.get_playback_restriction_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.get_playback_restriction_policy_request.GetPlaybackRestrictionPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_recording_configuration(
        self,
        arn: "aws_sdk_ivs.types.recording_configuration_arn.RecordingConfigurationArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.get_recording_configuration_response.GetRecordingConfigurationResponse":
        """<p>Gets the recording configuration for the specified ARN.</p>

        Args:
            arn: <p>ARN of the recording configuration to be retrieved.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.get_recording_configuration_request.GetRecordingConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.get_recording_configuration_response.GetRecordingConfigurationResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.get_recording_configuration

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.get_recording_configuration.get_recording_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.get_recording_configuration_request.GetRecordingConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_stream(
        self,
        channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.get_stream_response.GetStreamResponse":
        """<p>Gets information about the active (live) stream on a specified channel.</p>

        Args:
            channel_arn: <p>Channel ARN for stream to be accessed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.get_stream_request.GetStreamRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.get_stream_response.GetStreamResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.get_stream

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.get_stream.get_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.get_stream_request.GetStreamRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_stream_key(
        self,
        arn: "aws_sdk_ivs.types.stream_key_arn.StreamKeyArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.get_stream_key_response.GetStreamKeyResponse":
        """<p>Gets stream-key information for a specified ARN.</p>

        Args:
            arn: <p>ARN for the stream key to be retrieved.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.get_stream_key_request.GetStreamKeyRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.get_stream_key_response.GetStreamKeyResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.get_stream_key

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.get_stream_key.get_stream_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.get_stream_key_request.GetStreamKeyRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_stream_session(
        self,
        channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        stream_id: Optional["aws_sdk_ivs.types.stream_id.StreamId"] = None,
    ) -> "aws_sdk_ivs.types.get_stream_session_response.GetStreamSessionResponse":
        """<p>Gets metadata on a specified stream.</p>

        Args:
            channel_arn: <p>ARN of the channel resource</p>
            stream_id: <p>Unique identifier for a live or previously live stream in the specified channel. If no <code>streamId</code> is provided, this returns the most recent stream session for the channel, if it exists.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.get_stream_session_request.GetStreamSessionRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.get_stream_session_response.GetStreamSessionResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.get_stream_session

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.get_stream_session.get_stream_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.get_stream_session_request.GetStreamSessionRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def import_playback_key_pair(
        self,
        public_key_material: "aws_sdk_ivs.types.playback_public_key_material.PlaybackPublicKeyMaterial",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional[
            "aws_sdk_ivs.types.playback_key_pair_name.PlaybackKeyPairName"
        ] = None,
        tags: Optional["aws_sdk_ivs.types.tags.Tags"] = None,
    ) -> "aws_sdk_ivs.types.import_playback_key_pair_response.ImportPlaybackKeyPairResponse":
        """<p>Imports the public portion of a new key pair and returns its <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> can then be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p>

        Args:
            public_key_material: <p>The public portion of a customer-generated key pair.</p>
            name: <p>Playback-key-pair name. The value does not need to be unique.</p>
            tags: <p>Any tags provided with the request are added to the playback key pair tags. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.import_playback_key_pair_request.ImportPlaybackKeyPairRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.import_playback_key_pair_response.ImportPlaybackKeyPairResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.import_playback_key_pair

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.import_playback_key_pair.import_playback_key_pair(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.import_playback_key_pair_request.ImportPlaybackKeyPairRequest = {}  # type: ignore[typeddict-item]
        input_["public_key_material"] = public_key_material
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def insert_ad_break(
        self,
        channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        duration_seconds: "aws_sdk_ivs.types.ad_duration_seconds.AdDurationSeconds",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.insert_ad_break_response.InsertAdBreakResponse":
        """<p>Inserts an ad marker in the playlist for the specified channel and duration using the ad configuration associated with the channel.</p> <p> <b>Note:</b> AWS Elemental MediaTailor (EMT), the service that handles ad requests, provides CloudWatch metrics to help you monitor the success or failure of each InsertAdBreak operation. See <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-cloudwatch-metrics.html\">Monitoring AWS Elemental MediaTailor with Amazon CloudWatch</a> metrics in the <i>AWS Elemental MediaTailor User Guide</i> for details on available metrics.</p>

        Args:
            channel_arn: <p>ARN of the channel into which the ad break is inserted.</p>
            duration_seconds: <p>Duration of the ad break, in seconds.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.insert_ad_break_request.InsertAdBreakRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.insert_ad_break_response.InsertAdBreakResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.insert_ad_break

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.insert_ad_break.insert_ad_break(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.insert_ad_break_request.InsertAdBreakRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["duration_seconds"] = duration_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_ad_configurations(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_ivs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_ivs.types.max_ad_configuration_results.MaxAdConfigurationResults"
        ] = None,
    ) -> (
        "aws_sdk_ivs.types.list_ad_configurations_response.ListAdConfigurationsResponse"
    ):
        """<p>Gets summary information about all ad configurations in your account, in the AWS region where the API request is processed.</p>

        Args:
            next_token: <p>The first ad configuration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of ad configurations to return. Default: your service quota or 100, whichever is smaller.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.list_ad_configurations_request.ListAdConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.list_ad_configurations_response.ListAdConfigurationsResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.list_ad_configurations

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.list_ad_configurations.list_ad_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.list_ad_configurations_request.ListAdConfigurationsRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_ad_configurations(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_ivs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_ivs.types.max_ad_configuration_results.MaxAdConfigurationResults"
        ] = None,
    ) -> "Iterator[aws_sdk_ivs.types.ad_configuration_summary.AdConfigurationSummary]":
        _token = next_token
        while True:
            _response = self.list_ad_configurations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("ad_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channels(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        filter_by_name: Optional["aws_sdk_ivs.types.channel_name.ChannelName"] = None,
        filter_by_recording_configuration_arn: Optional[
            "aws_sdk_ivs.types.channel_recording_configuration_arn.ChannelRecordingConfigurationArn"
        ] = None,
        filter_by_playback_restriction_policy_arn: Optional[
            "aws_sdk_ivs.types.channel_playback_restriction_policy_arn.ChannelPlaybackRestrictionPolicyArn"
        ] = None,
        filter_by_ad_configuration_arn: Optional[
            "aws_sdk_ivs.types.channel_ad_configuration_arn.ChannelAdConfigurationArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_ivs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_ivs.types.max_channel_results.MaxChannelResults"
        ] = None,
    ) -> "aws_sdk_ivs.types.list_channels_response.ListChannelsResponse":
        """<p>Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 ConflictException).</p>

        Args:
            filter_by_name: <p>Filters the channel list to match the specified name.</p>
            filter_by_recording_configuration_arn: <p>Filters the channel list to match the specified recording-configuration ARN.</p>
            filter_by_playback_restriction_policy_arn: <p>Filters the channel list to match the specified policy.</p>
            filter_by_ad_configuration_arn: <p>Filters the channel list to match the specified ad configuration ARN.</p>
            next_token: <p>The first channel to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of channels to return. Default: 100.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.list_channels_response.ListChannelsResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.list_channels

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.list_channels_request.ListChannelsRequest = {}  # type: ignore[typeddict-item]
        if filter_by_name is not None:
            input_["filter_by_name"] = filter_by_name
        if filter_by_recording_configuration_arn is not None:
            input_["filter_by_recording_configuration_arn"] = (
                filter_by_recording_configuration_arn
            )
        if filter_by_playback_restriction_policy_arn is not None:
            input_["filter_by_playback_restriction_policy_arn"] = (
                filter_by_playback_restriction_policy_arn
            )
        if filter_by_ad_configuration_arn is not None:
            input_["filter_by_ad_configuration_arn"] = filter_by_ad_configuration_arn
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

    def list_playback_key_pairs(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_ivs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_ivs.types.max_playback_key_pair_results.MaxPlaybackKeyPairResults"
        ] = None,
    ) -> "aws_sdk_ivs.types.list_playback_key_pairs_response.ListPlaybackKeyPairsResponse":
        """<p>Gets summary information about playback key pairs. For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p>

        Args:
            next_token: <p>The first key pair to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of key pairs to return. Default: your service quota or 100, whichever is smaller.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.list_playback_key_pairs_request.ListPlaybackKeyPairsRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.list_playback_key_pairs_response.ListPlaybackKeyPairsResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.list_playback_key_pairs

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.list_playback_key_pairs.list_playback_key_pairs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.list_playback_key_pairs_request.ListPlaybackKeyPairsRequest = {}  # type: ignore[typeddict-item]
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

    def list_playback_restriction_policies(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_ivs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_ivs.types.max_playback_restriction_policy_results.MaxPlaybackRestrictionPolicyResults"
        ] = None,
    ) -> "aws_sdk_ivs.types.list_playback_restriction_policies_response.ListPlaybackRestrictionPoliciesResponse":
        """<p>Gets summary information about playback restriction policies.</p>

        Args:
            next_token: <p>The first policy to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of policies to return. Default: 1.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.list_playback_restriction_policies_request.ListPlaybackRestrictionPoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.list_playback_restriction_policies_response.ListPlaybackRestrictionPoliciesResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.list_playback_restriction_policies

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.list_playback_restriction_policies.list_playback_restriction_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.list_playback_restriction_policies_request.ListPlaybackRestrictionPoliciesRequest = {}  # type: ignore[typeddict-item]
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

    def list_recording_configurations(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_ivs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_ivs.types.max_recording_configuration_results.MaxRecordingConfigurationResults"
        ] = None,
    ) -> "aws_sdk_ivs.types.list_recording_configurations_response.ListRecordingConfigurationsResponse":
        """<p>Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.</p>

        Args:
            next_token: <p>The first recording configuration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of recording configurations to return. Default: your service quota or 100, whichever is smaller. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.list_recording_configurations_request.ListRecordingConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.list_recording_configurations_response.ListRecordingConfigurationsResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.list_recording_configurations

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.list_recording_configurations.list_recording_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.list_recording_configurations_request.ListRecordingConfigurationsRequest = {}  # type: ignore[typeddict-item]
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

    def list_stream_keys(
        self,
        channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_ivs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_ivs.types.max_stream_key_results.MaxStreamKeyResults"
        ] = None,
    ) -> "aws_sdk_ivs.types.list_stream_keys_response.ListStreamKeysResponse":
        """<p>Gets summary information about stream keys for the specified channel.</p>

        Args:
            channel_arn: <p>Channel ARN used to filter the list.</p>
            next_token: <p>The first stream key to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of streamKeys to return. Default: 1.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.list_stream_keys_request.ListStreamKeysRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.list_stream_keys_response.ListStreamKeysResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.list_stream_keys

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.list_stream_keys.list_stream_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.list_stream_keys_request.ListStreamKeysRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
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

    def list_streams(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        filter_by: Optional["aws_sdk_ivs.types.stream_filters.StreamFilters"] = None,
        next_token: Optional[
            "aws_sdk_ivs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_ivs.types.max_stream_results.MaxStreamResults"
        ] = None,
    ) -> "aws_sdk_ivs.types.list_streams_response.ListStreamsResponse":
        """<p>Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.</p>

        Args:
            filter_by: <p>Filters the stream list to match the specified criterion.</p>
            next_token: <p>The first stream to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of streams to return. Default: 100.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.list_streams_request.ListStreamsRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.list_streams_response.ListStreamsResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.list_streams

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.list_streams.list_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.list_streams_request.ListStreamsRequest = {}  # type: ignore[typeddict-item]
        if filter_by is not None:
            input_["filter_by"] = filter_by
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

    def list_stream_sessions(
        self,
        channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_ivs.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_ivs.types.max_stream_results.MaxStreamResults"
        ] = None,
    ) -> "aws_sdk_ivs.types.list_stream_sessions_response.ListStreamSessionsResponse":
        """<p>Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.</p>

        Args:
            channel_arn: <p>Channel ARN used to filter the list.</p>
            next_token: <p>The first stream to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of streams to return. Default: 100.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.list_stream_sessions_request.ListStreamSessionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.list_stream_sessions_response.ListStreamSessionsResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.list_stream_sessions

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.list_stream_sessions.list_stream_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.list_stream_sessions_request.ListStreamSessionsRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_ivs.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> (
        "aws_sdk_ivs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Gets information about Amazon Web Services tags for the specified ARN.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be retrieved. The ARN must be URL-encoded.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_metadata(
        self,
        channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        metadata: "aws_sdk_ivs.types.stream_metadata.StreamMetadata",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed. Also see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/metadata.html\">Embedding Metadata within a Video Stream</a> in the <i>Amazon IVS User Guide</i>.</p>

        Args:
            channel_arn: <p>ARN of the channel into which metadata is inserted. This channel must have an active stream.</p>
            metadata: <p>Metadata to insert into the stream. Maximum: 1 KB per request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.put_metadata_request.PutMetadataRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.put_metadata

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.put_metadata.put_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.put_metadata_request.PutMetadataRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["metadata"] = metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_viewer_session_revocation(
        self,
        channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        viewer_id: "aws_sdk_ivs.types.viewer_id.ViewerId",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        viewer_session_versions_less_than_or_equal_to: Optional[
            "aws_sdk_ivs.types.viewer_session_version.ViewerSessionVersion"
        ] = None,
    ) -> "aws_sdk_ivs.types.start_viewer_session_revocation_response.StartViewerSessionRevocationResponse":
        """<p>Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version. For instructions on associating a viewer ID with a viewer session, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a>.</p>

        Args:
            channel_arn: <p>The ARN of the channel associated with the viewer session to revoke.</p>
            viewer_id: <p>The ID of the viewer associated with the viewer session to revoke. Do not use this field for personally identifying, confidential, or sensitive information.</p>
            viewer_session_versions_less_than_or_equal_to: <p>An optional filter on which versions of the viewer session to revoke. All versions less than or equal to the specified version will be revoked. Default: 0.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.start_viewer_session_revocation_request.StartViewerSessionRevocationRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.start_viewer_session_revocation_response.StartViewerSessionRevocationResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.start_viewer_session_revocation

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.start_viewer_session_revocation.start_viewer_session_revocation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.start_viewer_session_revocation_request.StartViewerSessionRevocationRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["viewer_id"] = viewer_id
        if viewer_session_versions_less_than_or_equal_to is not None:
            input_["viewer_session_versions_less_than_or_equal_to"] = (
                viewer_session_versions_less_than_or_equal_to
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_stream(
        self,
        channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.stop_stream_response.StopStreamResponse":
        """<p>Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with <a>DeleteStreamKey</a> to prevent further streaming to a channel.</p> <note> <p>Many streaming client-software libraries automatically reconnect a dropped RTMPS session, so to stop the stream permanently, you may want to first revoke the <code>streamKey</code> attached to the channel.</p> </note>

        Args:
            channel_arn: <p>ARN of the channel for which the stream is to be stopped.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.stop_stream_request.StopStreamRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.stop_stream_response.StopStreamResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.stop_stream

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.stop_stream.stop_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.stop_stream_request.StopStreamRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_ivs.types.resource_arn.ResourceArn",
        tags: "aws_sdk_ivs.types.tags.Tags",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for the Amazon Web Services resource with the specified ARN.</p>

        Args:
            resource_arn: <p>ARN of the resource for which tags are to be added or updated. The ARN must be URL-encoded.</p>
            tags: <p>Array of tags to be added or updated. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.tag_resource

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_ivs.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_ivs.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "aws_sdk_ivs.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the resource with the specified ARN.</p>

        Args:
            resource_arn: <p>ARN of the resource for which tags are to be removed. The ARN must be URL-encoded.</p>
            tag_keys: <p>Array of tag keys (strings) for the tags to be removed. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.untag_resource

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_ad_configuration(
        self,
        arn: "aws_sdk_ivs.types.ad_configuration_arn.AdConfigurationArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional[
            "aws_sdk_ivs.types.ad_configuration_name.AdConfigurationName"
        ] = None,
        media_tailor_playback_configurations: Optional[
            "aws_sdk_ivs.types.media_tailor_playback_configurations_list.MediaTailorPlaybackConfigurationsList"
        ] = None,
    ) -> "aws_sdk_ivs.types.update_ad_configuration_response.UpdateAdConfigurationResponse":
        """<p>Updates a specified ad configuration.</p>

        Args:
            arn: <p>ARN of the ad configuration to be updated.</p>
            name: <p>Ad configuration name. The value does not need to be unique.</p>
            media_tailor_playback_configurations: <p>List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see <a href=\"https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html\">Generate and Sign IVS Playback Tokens</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.update_ad_configuration_request.UpdateAdConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.update_ad_configuration_response.UpdateAdConfigurationResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.update_ad_configuration

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.update_ad_configuration.update_ad_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.update_ad_configuration_request.UpdateAdConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if media_tailor_playback_configurations is not None:
            input_["media_tailor_playback_configurations"] = (
                media_tailor_playback_configurations
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_channel(
        self,
        arn: "aws_sdk_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional["aws_sdk_ivs.types.channel_name.ChannelName"] = None,
        latency_mode: Optional[
            "aws_sdk_ivs.types.channel_latency_mode.ChannelLatencyMode"
        ] = None,
        type: Optional["aws_sdk_ivs.types.channel_type.ChannelType"] = None,
        authorized: Optional["aws_sdk_ivs.types.boolean.Boolean"] = None,
        recording_configuration_arn: Optional[
            "aws_sdk_ivs.types.channel_recording_configuration_arn.ChannelRecordingConfigurationArn"
        ] = None,
        insecure_ingest: Optional["aws_sdk_ivs.types.boolean.Boolean"] = None,
        preset: Optional["aws_sdk_ivs.types.transcode_preset.TranscodePreset"] = None,
        playback_restriction_policy_arn: Optional[
            "aws_sdk_ivs.types.channel_playback_restriction_policy_arn.ChannelPlaybackRestrictionPolicyArn"
        ] = None,
        multitrack_input_configuration: Optional[
            "aws_sdk_ivs.types.multitrack_input_configuration.MultitrackInputConfiguration"
        ] = None,
        container_format: Optional[
            "aws_sdk_ivs.types.container_format.ContainerFormat"
        ] = None,
        ad_configuration_arn: Optional[
            "aws_sdk_ivs.types.channel_ad_configuration_arn.ChannelAdConfigurationArn"
        ] = None,
    ) -> "aws_sdk_ivs.types.update_channel_response.UpdateChannelResponse":
        """<p>Updates a channel's configuration. Live channels cannot be updated. You must stop the ongoing stream, update the channel, and restart the stream for the changes to take effect.</p>

        Args:
            arn: <p>ARN of the channel to be updated.</p>
            name: <p>Channel name.</p>
            latency_mode: <p>Channel latency mode. Use <code>NORMAL</code> to broadcast and deliver live video up to Full HD. Use <code>LOW</code> for near-real-time interaction with viewers.</p>
            type: <p>Channel type, which determines the allowable resolution and bitrate. <i>If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.</i> Default: <code>STANDARD</code>. For details, see <a href=\"https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/channel-types.html\">Channel Types</a>.</p>
            authorized: <p>Whether the channel is private (enabled for playback authorization).</p>
            recording_configuration_arn: <p>Recording-configuration ARN. A valid ARN value here both specifies the ARN and enables recording. If this is set to an empty string, recording is disabled.</p>
            insecure_ingest: <p>Whether the channel allows insecure RTMP and SRT ingest. Default: <code>false</code>.</p>
            preset: <p>Optional transcode preset for the channel. This is selectable only for <code>ADVANCED_HD</code> and <code>ADVANCED_SD</code> channel types. For those channel types, the default <code>preset</code> is <code>HIGHER_BANDWIDTH_DELIVERY</code>. For other channel types (<code>BASIC</code> and <code>STANDARD</code>), <code>preset</code> is the empty string (<code>\"\"</code>).</p>
            playback_restriction_policy_arn: <p>Playback-restriction-policy ARN. A valid ARN value here both specifies the ARN and enables playback restriction. If this is set to an empty string, playback restriction policy is disabled.</p>
            multitrack_input_configuration: <p>Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.</p>
            container_format: <p>Indicates which content-packaging format is used (MPEG-TS or fMP4). If <code>multitrackInputConfiguration</code> is specified and <code>enabled</code> is <code>true</code>, then <code>containerFormat</code> is required and must be set to <code>FRAGMENTED_MP4</code>. Otherwise, <code>containerFormat</code> may be set to <code>TS</code> or <code>FRAGMENTED_MP4</code>. Default: <code>TS</code>.</p>
            ad_configuration_arn: <p>ARN of the ad configuration associated with the channel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.update_channel_request.UpdateChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.update_channel_response.UpdateChannelResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.update_channel

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.update_channel_request.UpdateChannelRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if latency_mode is not None:
            input_["latency_mode"] = latency_mode
        if type is not None:
            input_["type"] = type
        if authorized is not None:
            input_["authorized"] = authorized
        if recording_configuration_arn is not None:
            input_["recording_configuration_arn"] = recording_configuration_arn
        if insecure_ingest is not None:
            input_["insecure_ingest"] = insecure_ingest
        if preset is not None:
            input_["preset"] = preset
        if playback_restriction_policy_arn is not None:
            input_["playback_restriction_policy_arn"] = playback_restriction_policy_arn
        if multitrack_input_configuration is not None:
            input_["multitrack_input_configuration"] = multitrack_input_configuration
        if container_format is not None:
            input_["container_format"] = container_format
        if ad_configuration_arn is not None:
            input_["ad_configuration_arn"] = ad_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_playback_restriction_policy(
        self,
        arn: "aws_sdk_ivs.types.playback_restriction_policy_arn.PlaybackRestrictionPolicyArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        allowed_countries: Optional[
            "aws_sdk_ivs.types.playback_restriction_policy_allowed_country_list.PlaybackRestrictionPolicyAllowedCountryList"
        ] = None,
        allowed_origins: Optional[
            "aws_sdk_ivs.types.playback_restriction_policy_allowed_origin_list.PlaybackRestrictionPolicyAllowedOriginList"
        ] = None,
        enable_strict_origin_enforcement: Optional[
            "aws_sdk_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement.PlaybackRestrictionPolicyEnableStrictOriginEnforcement"
        ] = None,
        name: Optional[
            "aws_sdk_ivs.types.playback_restriction_policy_name.PlaybackRestrictionPolicyName"
        ] = None,
    ) -> "aws_sdk_ivs.types.update_playback_restriction_policy_response.UpdatePlaybackRestrictionPolicyResponse":
        """<p>Updates a specified playback restriction policy.</p>

        Args:
            arn: <p>ARN of the playback-restriction-policy to be updated.</p>
            allowed_countries: <p>A list of country codes that control geoblocking restriction. Allowed values are the officially assigned <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\">ISO 3166-1 alpha-2</a> codes. Default: All countries (an empty array).</p>
            allowed_origins: <p>A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin\">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin</a>. Default: All origins (an empty array).</p>
            enable_strict_origin_enforcement: <p>Whether channel playback is constrained by origin site. Default: <code>false</code>.</p>
            name: <p>Playback-restriction-policy name. The value does not need to be unique.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_ivs.types.update_playback_restriction_policy_request.UpdatePlaybackRestrictionPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_ivs.types.update_playback_restriction_policy_response.UpdatePlaybackRestrictionPolicyResponse"
        ]:
            import aws_sdk_ivs._operations.amazon_interactive_video_service.update_playback_restriction_policy

            output, http_response = (
                aws_sdk_ivs._operations.amazon_interactive_video_service.update_playback_restriction_policy.update_playback_restriction_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_ivs.types.update_playback_restriction_policy_request.UpdatePlaybackRestrictionPolicyRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if allowed_countries is not None:
            input_["allowed_countries"] = allowed_countries
        if allowed_origins is not None:
            input_["allowed_origins"] = allowed_origins
        if enable_strict_origin_enforcement is not None:
            input_["enable_strict_origin_enforcement"] = (
                enable_strict_origin_enforcement
            )
        if name is not None:
            input_["name"] = name

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
