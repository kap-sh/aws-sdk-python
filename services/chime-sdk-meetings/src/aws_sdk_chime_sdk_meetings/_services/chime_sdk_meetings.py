"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ChimeMeetingsSDKService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_chime_sdk_meetings._auth._signers
import aws_sdk_chime_sdk_meetings._auth._sigv4
from aws_sdk_chime_sdk_meetings._auth._identity import Credentials
from aws_sdk_chime_sdk_meetings._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_chime_sdk_meetings._auth._zapros_handler import AuthMiddleware
from aws_sdk_chime_sdk_meetings._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.amazon_resource_name
    import aws_sdk_chime_sdk_meetings.types.attendee_capabilities
    import aws_sdk_chime_sdk_meetings.types.attendee_ids_list
    import aws_sdk_chime_sdk_meetings.types.batch_create_attendee_request
    import aws_sdk_chime_sdk_meetings.types.batch_create_attendee_response
    import aws_sdk_chime_sdk_meetings.types.batch_update_attendee_capabilities_except_request
    import aws_sdk_chime_sdk_meetings.types.client_request_token
    import aws_sdk_chime_sdk_meetings.types.create_attendee_request
    import aws_sdk_chime_sdk_meetings.types.create_attendee_request_item_list
    import aws_sdk_chime_sdk_meetings.types.create_attendee_response
    import aws_sdk_chime_sdk_meetings.types.create_meeting_request
    import aws_sdk_chime_sdk_meetings.types.create_meeting_response
    import aws_sdk_chime_sdk_meetings.types.create_meeting_with_attendees_request
    import aws_sdk_chime_sdk_meetings.types.create_meeting_with_attendees_request_item_list
    import aws_sdk_chime_sdk_meetings.types.create_meeting_with_attendees_response
    import aws_sdk_chime_sdk_meetings.types.delete_attendee_request
    import aws_sdk_chime_sdk_meetings.types.delete_meeting_request
    import aws_sdk_chime_sdk_meetings.types.external_meeting_id
    import aws_sdk_chime_sdk_meetings.types.external_user_id
    import aws_sdk_chime_sdk_meetings.types.get_attendee_request
    import aws_sdk_chime_sdk_meetings.types.get_attendee_response
    import aws_sdk_chime_sdk_meetings.types.get_meeting_request
    import aws_sdk_chime_sdk_meetings.types.get_meeting_response
    import aws_sdk_chime_sdk_meetings.types.guid_string
    import aws_sdk_chime_sdk_meetings.types.list_attendees_request
    import aws_sdk_chime_sdk_meetings.types.list_attendees_response
    import aws_sdk_chime_sdk_meetings.types.list_tags_for_resource_request
    import aws_sdk_chime_sdk_meetings.types.list_tags_for_resource_response
    import aws_sdk_chime_sdk_meetings.types.media_placement_network_type
    import aws_sdk_chime_sdk_meetings.types.media_region
    import aws_sdk_chime_sdk_meetings.types.meeting_features_configuration
    import aws_sdk_chime_sdk_meetings.types.notifications_configuration
    import aws_sdk_chime_sdk_meetings.types.primary_meeting_id
    import aws_sdk_chime_sdk_meetings.types.result_max
    import aws_sdk_chime_sdk_meetings.types.start_meeting_transcription_request
    import aws_sdk_chime_sdk_meetings.types.stop_meeting_transcription_request
    import aws_sdk_chime_sdk_meetings.types.string
    import aws_sdk_chime_sdk_meetings.types.tag_key_list
    import aws_sdk_chime_sdk_meetings.types.tag_list
    import aws_sdk_chime_sdk_meetings.types.tag_resource_request
    import aws_sdk_chime_sdk_meetings.types.tag_resource_response
    import aws_sdk_chime_sdk_meetings.types.tenant_id_list
    import aws_sdk_chime_sdk_meetings.types.transcription_configuration
    import aws_sdk_chime_sdk_meetings.types.untag_resource_request
    import aws_sdk_chime_sdk_meetings.types.untag_resource_response
    import aws_sdk_chime_sdk_meetings.types.update_attendee_capabilities_request
    import aws_sdk_chime_sdk_meetings.types.update_attendee_capabilities_response


class ChimeSDKMeetingsClientConfig(TypedDict, total=False):
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


class ChimeSDKMeetingsClient:
    """A client for the ``ChimeSDKMeetings`` service.

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
        self._config = ChimeSDKMeetingsClientConfig(
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
        self, config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ChimeSDKMeetingsClientConfig = config_overrides or {}
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

    def batch_create_attendee(
        self,
        meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        attendees: "aws_sdk_chime_sdk_meetings.types.create_attendee_request_item_list.CreateAttendeeRequestItemList",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_meetings.types.batch_create_attendee_response.BatchCreateAttendeeResponse":
        r"""<p>Creates up to 100 attendees for an active Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\">Using the Amazon Chime SDK</a> in the <i>Amazon Chime Developer Guide</i>.</p>

        Args:
            meeting_id: <p>The Amazon Chime SDK ID of the meeting to which you're adding attendees.</p>
            attendees: <p>The attendee information, including attendees' IDs and join tokens.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.batch_create_attendee_request.BatchCreateAttendeeRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_meetings.types.batch_create_attendee_response.BatchCreateAttendeeResponse"
        ]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.batch_create_attendee

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.batch_create_attendee.batch_create_attendee(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.batch_create_attendee_request.BatchCreateAttendeeRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id
        input_["attendees"] = attendees

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_attendee_capabilities_except(
        self,
        meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        excluded_attendee_ids: "aws_sdk_chime_sdk_meetings.types.attendee_ids_list.AttendeeIdsList",
        capabilities: "aws_sdk_chime_sdk_meetings.types.attendee_capabilities.AttendeeCapabilities",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> None:
        """<p>Updates <code>AttendeeCapabilities</code> except the capabilities listed in an <code>ExcludedAttendeeIds</code> table.</p> <note> <p>You use the capabilities with a set of values that control what the capabilities can do, such as <code>SendReceive</code> data. For more information about those values, see .</p> </note> <p>When using capabilities, be aware of these corner cases:</p> <ul> <li> <p>If you specify <code>MeetingFeatures:Video:MaxResolution:None</code> when you create a meeting, all API requests that include <code>SendReceive</code>, <code>Send</code>, or <code>Receive</code> for <code>AttendeeCapabilities:Video</code> will be rejected with <code>ValidationError 400</code>.</p> </li> <li> <p>If you specify <code>MeetingFeatures:Content:MaxResolution:None</code> when you create a meeting, all API requests that include <code>SendReceive</code>, <code>Send</code>, or <code>Receive</code> for <code>AttendeeCapabilities:Content</code> will be rejected with <code>ValidationError 400</code>.</p> </li> <li> <p>You can't set <code>content</code> capabilities to <code>SendReceive</code> or <code>Receive</code> unless you also set <code>video</code> capabilities to <code>SendReceive</code> or <code>Receive</code>. If you don't set the <code>video</code> capability to receive, the response will contain an HTTP 400 Bad Request status code. However, you can set your <code>video</code> capability to receive and you set your <code>content</code> capability to not receive.</p> </li> <li> <p>If meeting features is defined as <code>Video:MaxResolution:None</code> but <code>Content:MaxResolution</code> is defined as something other than <code>None</code> and attendee capabilities are not defined in the API request, then the default attendee video capability is set to <code>Receive</code> and attendee content capability is set to <code>SendReceive</code>. This is because content <code>SendReceive</code> requires video to be at least <code>Receive</code>.</p> </li> <li> <p>When you change an <code>audio</code> capability from <code>None</code> or <code>Receive</code> to <code>Send</code> or <code>SendReceive</code> , and if the attendee left their microphone unmuted, audio will flow from the attendee to the other meeting participants.</p> </li> <li> <p>When you change a <code>video</code> or <code>content</code> capability from <code>None</code> or <code>Receive</code> to <code>Send</code> or <code>SendReceive</code> , and if the attendee turned on their video or content streams, remote attendees can receive those streams, but only after media renegotiation between the client and the Amazon Chime back-end server.</p> </li> </ul>

        Args:
            meeting_id: <p>The ID of the meeting associated with the update request.</p>
            excluded_attendee_ids: <p>The <code>AttendeeIDs</code> that you want to exclude from one or more capabilities.</p>
            capabilities: <p>The capabilities (<code>audio</code>, <code>video</code>, or <code>content</code>) that you want to update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.batch_update_attendee_capabilities_except_request.BatchUpdateAttendeeCapabilitiesExceptRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.batch_update_attendee_capabilities_except

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.batch_update_attendee_capabilities_except.batch_update_attendee_capabilities_except(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.batch_update_attendee_capabilities_except_request.BatchUpdateAttendeeCapabilitiesExceptRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id
        input_["excluded_attendee_ids"] = excluded_attendee_ids
        input_["capabilities"] = capabilities

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_attendee(
        self,
        meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        external_user_id: "aws_sdk_chime_sdk_meetings.types.external_user_id.ExternalUserId",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
        capabilities: Optional[
            "aws_sdk_chime_sdk_meetings.types.attendee_capabilities.AttendeeCapabilities"
        ] = None,
    ) -> "aws_sdk_chime_sdk_meetings.types.create_attendee_response.CreateAttendeeResponse":
        r"""<p> Creates a new attendee for an active Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\">Using the Amazon Chime SDK</a> in the <i>Amazon Chime Developer Guide</i>. </p>

        Args:
            meeting_id: <p>The unique ID of the meeting.</p>
            external_user_id: <p>The Amazon Chime SDK external user ID. An idempotency token. Links the attendee to an identity managed by a builder application.</p> <p>Pattern: <code>[-_&@+=,(){}\[\]\/«».:|'\"#a-zA-Z0-9À-ÿ\s]*</code> </p> <p>Values that begin with <code>aws:</code> are reserved. You can't configure a value that uses this prefix.</p>
            capabilities: <p>The capabilities (<code>audio</code>, <code>video</code>, or <code>content</code>) that you want to grant an attendee. If you don't specify capabilities, all users have send and receive capabilities on all media channels by default.</p> <note> <p>You use the capabilities with a set of values that control what the capabilities can do, such as <code>SendReceive</code> data. For more information about those values, see .</p> </note> <p>When using capabilities, be aware of these corner cases:</p> <ul> <li> <p>If you specify <code>MeetingFeatures:Video:MaxResolution:None</code> when you create a meeting, all API requests that include <code>SendReceive</code>, <code>Send</code>, or <code>Receive</code> for <code>AttendeeCapabilities:Video</code> will be rejected with <code>ValidationError 400</code>.</p> </li> <li> <p>If you specify <code>MeetingFeatures:Content:MaxResolution:None</code> when you create a meeting, all API requests that include <code>SendReceive</code>, <code>Send</code>, or <code>Receive</code> for <code>AttendeeCapabilities:Content</code> will be rejected with <code>ValidationError 400</code>.</p> </li> <li> <p>You can't set <code>content</code> capabilities to <code>SendReceive</code> or <code>Receive</code> unless you also set <code>video</code> capabilities to <code>SendReceive</code> or <code>Receive</code>. If you don't set the <code>video</code> capability to receive, the response will contain an HTTP 400 Bad Request status code. However, you can set your <code>video</code> capability to receive and you set your <code>content</code> capability to not receive.</p> </li> <li> <p>If meeting features is defined as <code>Video:MaxResolution:None</code> but <code>Content:MaxResolution</code> is defined as something other than <code>None</code> and attendee capabilities are not defined in the API request, then the default attendee video capability is set to <code>Receive</code> and attendee content capability is set to <code>SendReceive</code>. This is because content <code>SendReceive</code> requires video to be at least <code>Receive</code>.</p> </li> <li> <p>When you change an <code>audio</code> capability from <code>None</code> or <code>Receive</code> to <code>Send</code> or <code>SendReceive</code> , and if the attendee left their microphone unmuted, audio will flow from the attendee to the other meeting participants.</p> </li> <li> <p>When you change a <code>video</code> or <code>content</code> capability from <code>None</code> or <code>Receive</code> to <code>Send</code> or <code>SendReceive</code> , and if the attendee turned on their video or content streams, remote attendees can receive those streams, but only after media renegotiation between the client and the Amazon Chime back-end server.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.create_attendee_request.CreateAttendeeRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_meetings.types.create_attendee_response.CreateAttendeeResponse"
        ]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.create_attendee

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.create_attendee.create_attendee(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.create_attendee_request.CreateAttendeeRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id
        input_["external_user_id"] = external_user_id
        if capabilities is not None:
            input_["capabilities"] = capabilities

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_meeting(
        self,
        client_request_token: "aws_sdk_chime_sdk_meetings.types.client_request_token.ClientRequestToken",
        media_region: "aws_sdk_chime_sdk_meetings.types.media_region.MediaRegion",
        external_meeting_id: "aws_sdk_chime_sdk_meetings.types.external_meeting_id.ExternalMeetingId",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
        meeting_host_id: Optional[
            "aws_sdk_chime_sdk_meetings.types.external_user_id.ExternalUserId"
        ] = None,
        notifications_configuration: Optional[
            "aws_sdk_chime_sdk_meetings.types.notifications_configuration.NotificationsConfiguration"
        ] = None,
        meeting_features: Optional[
            "aws_sdk_chime_sdk_meetings.types.meeting_features_configuration.MeetingFeaturesConfiguration"
        ] = None,
        primary_meeting_id: Optional[
            "aws_sdk_chime_sdk_meetings.types.primary_meeting_id.PrimaryMeetingId"
        ] = None,
        tenant_ids: Optional[
            "aws_sdk_chime_sdk_meetings.types.tenant_id_list.TenantIdList"
        ] = None,
        tags: Optional["aws_sdk_chime_sdk_meetings.types.tag_list.TagList"] = None,
        media_placement_network_type: Optional[
            "aws_sdk_chime_sdk_meetings.types.media_placement_network_type.MediaPlacementNetworkType"
        ] = None,
    ) -> (
        "aws_sdk_chime_sdk_meetings.types.create_meeting_response.CreateMeetingResponse"
    ):
        r"""<p>Creates a new Amazon Chime SDK meeting in the specified media Region with no initial attendees. For more information about specifying media Regions, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions\">Available Regions</a> and <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/chime-sdk-meetings-regions.html\">Using meeting Regions</a>, both in the <i>Amazon Chime SDK Developer Guide</i>. For more information about the Amazon Chime SDK, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\">Using the Amazon Chime SDK</a> in the <i>Amazon Chime SDK Developer Guide</i>. </p> <note> <p>If you use this API in conjuction with the and APIs, and you don't specify the <code>MeetingFeatures.Content.MaxResolution</code> or <code>MeetingFeatures.Video.MaxResolution</code> parameters, the following defaults are used:</p> <ul> <li> <p>Content.MaxResolution: FHD</p> </li> <li> <p>Video.MaxResolution: HD</p> </li> </ul> </note>

        Args:
            client_request_token: <p>The unique identifier for the client request. Use a different token for different meetings.</p>
            media_region: <p>The Region in which to create the meeting.</p> <p> Available values: <code>af-south-1</code>, <code>ap-northeast-1</code>, <code>ap-northeast-2</code>, <code>ap-south-1</code>, <code>ap-southeast-1</code>, <code>ap-southeast-2</code>, <code>ca-central-1</code>, <code>eu-central-1</code>, <code>eu-north-1</code>, <code>eu-south-1</code>, <code>eu-west-1</code>, <code>eu-west-2</code>, <code>eu-west-3</code>, <code>sa-east-1</code>, <code>us-east-1</code>, <code>us-east-2</code>, <code>us-west-1</code>, <code>us-west-2</code>. </p> <p>Available values in Amazon Web Services GovCloud (US) Regions: <code>us-gov-east-1</code>, <code>us-gov-west-1</code>.</p>
            meeting_host_id: <p>Reserved.</p>
            external_meeting_id: <p>The external meeting ID.</p> <p>Pattern: <code>[-_&@+=,(){}\[\]\/«».:|'\"#a-zA-Z0-9À-ÿ\s]*</code> </p> <p>Values that begin with <code>aws:</code> are reserved. You can't configure a value that uses this prefix. Case insensitive.</p>
            notifications_configuration: <p>The configuration for resource targets to receive notifications when meeting and attendee events occur.</p>
            meeting_features: <p>Lists the audio and video features enabled for a meeting, such as echo reduction.</p>
            primary_meeting_id: <p>When specified, replicates the media from the primary meeting to the new meeting.</p>
            tenant_ids: <p>A consistent and opaque identifier, created and maintained by the builder to represent a segment of their users.</p>
            tags: <p>Applies one or more tags to an Amazon Chime SDK meeting. Note the following:</p> <ul> <li> <p>Not all resources have tags. For a list of services with resources that support tagging using this operation, see <a href=\"https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html\">Services that support the Resource Groups Tagging API</a>. If the resource doesn't yet support this operation, the resource's service might support tagging using its own API operations. For more information, refer to the documentation for that service.</p> </li> <li> <p>Each resource can have up to 50 tags. For other limits, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions\">Tag Naming and Usage Conventions</a> in the <i>AWS General Reference</i>.</p> </li> <li> <p>You can only tag resources that are located in the specified Amazon Web Services Region for the Amazon Web Services account.</p> </li> <li> <p>To add tags to a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for adding tags. For more information, see the documentation for each service.</p> </li> </ul> <important> <p>Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.</p> </important> <p> <b>Minimum permissions</b> </p> <p>In addition to the <code>tag:TagResources</code> permission required by this operation, you must also have the tagging permission defined by the service that created the resource. For example, to tag a <code>ChimeSDKMeetings</code> instance using the <code>TagResources</code> operation, you must have both of the following permissions:</p> <p> <code>tag:TagResources</code> </p> <p> <code>ChimeSDKMeetings:CreateTags</code> </p> <note> <p>Some services might have specific requirements for tagging some resources. For example, to tag an Amazon S3 bucket, you must also have the <code>s3:GetBucketTagging</code> permission. If the expected minimum permissions don't work, check the documentation for that service's tagging APIs for more information.</p> </note>
            media_placement_network_type: <p>The type of network for the media placement. Either IPv4 only or dual-stack (IPv4 and IPv6).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.create_meeting_request.CreateMeetingRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_meetings.types.create_meeting_response.CreateMeetingResponse"
        ]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.create_meeting

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.create_meeting.create_meeting(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.create_meeting_request.CreateMeetingRequest = {}  # type: ignore[typeddict-item]
        input_["client_request_token"] = client_request_token
        input_["media_region"] = media_region
        if meeting_host_id is not None:
            input_["meeting_host_id"] = meeting_host_id
        input_["external_meeting_id"] = external_meeting_id
        if notifications_configuration is not None:
            input_["notifications_configuration"] = notifications_configuration
        if meeting_features is not None:
            input_["meeting_features"] = meeting_features
        if primary_meeting_id is not None:
            input_["primary_meeting_id"] = primary_meeting_id
        if tenant_ids is not None:
            input_["tenant_ids"] = tenant_ids
        if tags is not None:
            input_["tags"] = tags
        if media_placement_network_type is not None:
            input_["media_placement_network_type"] = media_placement_network_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_meeting_with_attendees(
        self,
        client_request_token: "aws_sdk_chime_sdk_meetings.types.client_request_token.ClientRequestToken",
        media_region: "aws_sdk_chime_sdk_meetings.types.media_region.MediaRegion",
        external_meeting_id: "aws_sdk_chime_sdk_meetings.types.external_meeting_id.ExternalMeetingId",
        attendees: "aws_sdk_chime_sdk_meetings.types.create_meeting_with_attendees_request_item_list.CreateMeetingWithAttendeesRequestItemList",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
        meeting_host_id: Optional[
            "aws_sdk_chime_sdk_meetings.types.external_user_id.ExternalUserId"
        ] = None,
        meeting_features: Optional[
            "aws_sdk_chime_sdk_meetings.types.meeting_features_configuration.MeetingFeaturesConfiguration"
        ] = None,
        notifications_configuration: Optional[
            "aws_sdk_chime_sdk_meetings.types.notifications_configuration.NotificationsConfiguration"
        ] = None,
        primary_meeting_id: Optional[
            "aws_sdk_chime_sdk_meetings.types.primary_meeting_id.PrimaryMeetingId"
        ] = None,
        tenant_ids: Optional[
            "aws_sdk_chime_sdk_meetings.types.tenant_id_list.TenantIdList"
        ] = None,
        tags: Optional["aws_sdk_chime_sdk_meetings.types.tag_list.TagList"] = None,
        media_placement_network_type: Optional[
            "aws_sdk_chime_sdk_meetings.types.media_placement_network_type.MediaPlacementNetworkType"
        ] = None,
    ) -> "aws_sdk_chime_sdk_meetings.types.create_meeting_with_attendees_response.CreateMeetingWithAttendeesResponse":
        r"""<p> Creates a new Amazon Chime SDK meeting in the specified media Region, with attendees. For more information about specifying media Regions, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions\">Available Regions</a> and <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/chime-sdk-meetings-regions.html\">Using meeting Regions</a>, both in the <i>Amazon Chime SDK Developer Guide</i>. For more information about the Amazon Chime SDK, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\">Using the Amazon Chime SDK</a> in the <i>Amazon Chime SDK Developer Guide</i>. </p> <note> <p>If you use this API in conjuction with the and APIs, and you don't specify the <code>MeetingFeatures.Content.MaxResolution</code> or <code>MeetingFeatures.Video.MaxResolution</code> parameters, the following defaults are used:</p> <ul> <li> <p>Content.MaxResolution: FHD</p> </li> <li> <p>Video.MaxResolution: HD</p> </li> </ul> </note>

        Args:
            client_request_token: <p>The unique identifier for the client request. Use a different token for different meetings.</p>
            media_region: <p>The Region in which to create the meeting.</p> <p> Available values: <code>af-south-1</code>, <code>ap-northeast-1</code>, <code>ap-northeast-2</code>, <code>ap-south-1</code>, <code>ap-southeast-1</code>, <code>ap-southeast-2</code>, <code>ca-central-1</code>, <code>eu-central-1</code>, <code>eu-north-1</code>, <code>eu-south-1</code>, <code>eu-west-1</code>, <code>eu-west-2</code>, <code>eu-west-3</code>, <code>sa-east-1</code>, <code>us-east-1</code>, <code>us-east-2</code>, <code>us-west-1</code>, <code>us-west-2</code>. </p> <p>Available values in Amazon Web Services GovCloud (US) Regions: <code>us-gov-east-1</code>, <code>us-gov-west-1</code>.</p>
            meeting_host_id: <p>Reserved.</p>
            external_meeting_id: <p>The external meeting ID.</p> <p>Pattern: <code>[-_&@+=,(){}\[\]\/«».:|'\"#a-zA-Z0-9À-ÿ\s]*</code> </p> <p>Values that begin with <code>aws:</code> are reserved. You can't configure a value that uses this prefix. Case insensitive.</p>
            meeting_features: <p>Lists the audio and video features enabled for a meeting, such as echo reduction.</p>
            notifications_configuration: <p>The configuration for resource targets to receive notifications when meeting and attendee events occur.</p>
            attendees: <p>The attendee information, including attendees' IDs and join tokens.</p>
            primary_meeting_id: <p>When specified, replicates the media from the primary meeting to the new meeting.</p>
            tenant_ids: <p>A consistent and opaque identifier, created and maintained by the builder to represent a segment of their users.</p>
            tags: <p>The tags in the request.</p>
            media_placement_network_type: <p>The type of network for the media placement. Either IPv4 only or dual-stack (IPv4 and IPv6).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.create_meeting_with_attendees_request.CreateMeetingWithAttendeesRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_meetings.types.create_meeting_with_attendees_response.CreateMeetingWithAttendeesResponse"
        ]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.create_meeting_with_attendees

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.create_meeting_with_attendees.create_meeting_with_attendees(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.create_meeting_with_attendees_request.CreateMeetingWithAttendeesRequest = {}  # type: ignore[typeddict-item]
        input_["client_request_token"] = client_request_token
        input_["media_region"] = media_region
        if meeting_host_id is not None:
            input_["meeting_host_id"] = meeting_host_id
        input_["external_meeting_id"] = external_meeting_id
        if meeting_features is not None:
            input_["meeting_features"] = meeting_features
        if notifications_configuration is not None:
            input_["notifications_configuration"] = notifications_configuration
        input_["attendees"] = attendees
        if primary_meeting_id is not None:
            input_["primary_meeting_id"] = primary_meeting_id
        if tenant_ids is not None:
            input_["tenant_ids"] = tenant_ids
        if tags is not None:
            input_["tags"] = tags
        if media_placement_network_type is not None:
            input_["media_placement_network_type"] = media_placement_network_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_attendee(
        self,
        meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        attendee_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> None:
        r"""<p>Deletes an attendee from the specified Amazon Chime SDK meeting and deletes their <code>JoinToken</code>. Attendees are automatically deleted when a Amazon Chime SDK meeting is deleted. For more information about the Amazon Chime SDK, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\">Using the Amazon Chime SDK</a> in the <i>Amazon Chime Developer Guide</i>.</p>

        Args:
            meeting_id: <p>The Amazon Chime SDK meeting ID.</p>
            attendee_id: <p>The Amazon Chime SDK attendee ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.delete_attendee_request.DeleteAttendeeRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.delete_attendee

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.delete_attendee.delete_attendee(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.delete_attendee_request.DeleteAttendeeRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id
        input_["attendee_id"] = attendee_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_meeting(
        self,
        meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> None:
        r"""<p>Deletes the specified Amazon Chime SDK meeting. The operation deletes all attendees, disconnects all clients, and prevents new clients from joining the meeting. For more information about the Amazon Chime SDK, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\">Using the Amazon Chime SDK</a> in the <i>Amazon Chime Developer Guide</i>.</p>

        Args:
            meeting_id: <p>The Amazon Chime SDK meeting ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.delete_meeting_request.DeleteMeetingRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.delete_meeting

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.delete_meeting.delete_meeting(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.delete_meeting_request.DeleteMeetingRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_attendee(
        self,
        meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        attendee_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_meetings.types.get_attendee_response.GetAttendeeResponse":
        r"""<p> Gets the Amazon Chime SDK attendee details for a specified meeting ID and attendee ID. For more information about the Amazon Chime SDK, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\">Using the Amazon Chime SDK</a> in the <i>Amazon Chime Developer Guide</i>. </p>

        Args:
            meeting_id: <p>The Amazon Chime SDK meeting ID.</p>
            attendee_id: <p>The Amazon Chime SDK attendee ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.get_attendee_request.GetAttendeeRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_meetings.types.get_attendee_response.GetAttendeeResponse"
        ]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.get_attendee

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.get_attendee.get_attendee(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.get_attendee_request.GetAttendeeRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id
        input_["attendee_id"] = attendee_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_meeting(
        self,
        meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_meetings.types.get_meeting_response.GetMeetingResponse":
        r"""<p>Gets the Amazon Chime SDK meeting details for the specified meeting ID. For more information about the Amazon Chime SDK, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\">Using the Amazon Chime SDK</a> in the <i>Amazon Chime Developer Guide</i>.</p>

        Args:
            meeting_id: <p>The Amazon Chime SDK meeting ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.get_meeting_request.GetMeetingRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_meetings.types.get_meeting_response.GetMeetingResponse"
        ]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.get_meeting

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.get_meeting.get_meeting(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.get_meeting_request.GetMeetingRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_attendees(
        self,
        meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
        next_token: Optional["aws_sdk_chime_sdk_meetings.types.string.String"] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_meetings.types.result_max.ResultMax"
        ] = None,
    ) -> (
        "aws_sdk_chime_sdk_meetings.types.list_attendees_response.ListAttendeesResponse"
    ):
        r"""<p> Lists the attendees for the specified Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\">Using the Amazon Chime SDK</a> in the <i>Amazon Chime Developer Guide</i>. </p>

        Args:
            meeting_id: <p>The Amazon Chime SDK meeting ID.</p>
            next_token: <p>The token to use to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.list_attendees_request.ListAttendeesRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_meetings.types.list_attendees_response.ListAttendeesResponse"
        ]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.list_attendees

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.list_attendees.list_attendees(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.list_attendees_request.ListAttendeesRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id
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
        resource_arn: "aws_sdk_chime_sdk_meetings.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_meetings.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of the tags available for the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_meetings.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_meeting_transcription(
        self,
        meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        transcription_configuration: "aws_sdk_chime_sdk_meetings.types.transcription_configuration.TranscriptionConfiguration",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> None:
        r"""<p>Starts transcription for the specified <code>meetingId</code>. For more information, refer to <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-transcription.html\"> Using Amazon Chime SDK live transcription </a> in the <i>Amazon Chime SDK Developer Guide</i>.</p> <p>If you specify an invalid configuration, a <code>TranscriptFailed</code> event will be sent with the contents of the <code>BadRequestException</code> generated by Amazon Transcribe. For more information on each parameter and which combinations are valid, refer to the <a href=\"https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html\">StartStreamTranscription</a> API in the <i>Amazon Transcribe Developer Guide</i>.</p> <note> <p>By default, Amazon Transcribe may use and store audio content processed by the service to develop and improve Amazon Web Services AI/ML services as further described in section 50 of the <a href=\"https://aws.amazon.com/service-terms/\">Amazon Web Services Service Terms</a>. Using Amazon Transcribe may be subject to federal and state laws or regulations regarding the recording or interception of electronic communications. It is your and your end users’ responsibility to comply with all applicable laws regarding the recording, including properly notifying all participants in a recorded session or communication that the session or communication is being recorded, and obtaining all necessary consents. You can opt out from Amazon Web Services using audio content to develop and improve AWS AI/ML services by configuring an AI services opt out policy using Amazon Web Services Organizations.</p> </note>

        Args:
            meeting_id: <p>The unique ID of the meeting being transcribed.</p>
            transcription_configuration: <p>The configuration for the current transcription operation. Must contain <code>EngineTranscribeSettings</code> or <code>EngineTranscribeMedicalSettings</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.start_meeting_transcription_request.StartMeetingTranscriptionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.start_meeting_transcription

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.start_meeting_transcription.start_meeting_transcription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.start_meeting_transcription_request.StartMeetingTranscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id
        input_["transcription_configuration"] = transcription_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_meeting_transcription(
        self,
        meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> None:
        r"""<p>Stops transcription for the specified <code>meetingId</code>. For more information, refer to <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-transcription.html\"> Using Amazon Chime SDK live transcription </a> in the <i>Amazon Chime SDK Developer Guide</i>.</p> <important> <p>By default, Amazon Transcribe may use and store audio content processed by the service to develop and improve Amazon Web Services AI/ML services as further described in section 50 of the <a href=\"https://aws.amazon.com/service-terms/\">Amazon Web Services Service Terms</a>. Using Amazon Transcribe may be subject to federal and state laws or regulations regarding the recording or interception of electronic communications. It is your and your end users’ responsibility to comply with all applicable laws regarding the recording, including properly notifying all participants in a recorded session or communication that the session or communication is being recorded, and obtaining all necessary consents. You can opt out from Amazon Web Services using audio content to develop and improve Amazon Web Services AI/ML services by configuring an AI services opt out policy using Amazon Web Services Organizations.</p> </important>

        Args:
            meeting_id: <p>The unique ID of the meeting for which you stop transcription.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.stop_meeting_transcription_request.StopMeetingTranscriptionRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.stop_meeting_transcription

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.stop_meeting_transcription.stop_meeting_transcription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.stop_meeting_transcription_request.StopMeetingTranscriptionRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_chime_sdk_meetings.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_chime_sdk_meetings.types.tag_list.TagList",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_meetings.types.tag_resource_response.TagResourceResponse":
        """<p>The resource that supports tags.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>Lists the requested tags.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_meetings.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.tag_resource

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_chime_sdk_meetings.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_chime_sdk_meetings.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> (
        "aws_sdk_chime_sdk_meetings.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>Removes the specified tags from the specified resources. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from a resource that were already removed. Note the following:</p> <ul> <li> <p>To remove tags from a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for removing tags. For more information, see the documentation for the service whose resource you want to untag.</p> </li> <li> <p>You can only tag resources that are located in the specified Amazon Web Services Region for the calling Amazon Web Services account.</p> </li> </ul> <p> <b>Minimum permissions</b> </p> <p>In addition to the <code>tag:UntagResources</code> permission required by this operation, you must also have the remove tags permission defined by the service that created the resource. For example, to remove the tags from an Amazon EC2 instance using the <code>UntagResources</code> operation, you must have both of the following permissions:</p> <p> <code>tag:UntagResource</code> </p> <p> <code>ChimeSDKMeetings:DeleteTags</code> </p>

        Args:
            resource_arn: <p>The ARN of the resource that you're removing tags from.</p>
            tag_keys: <p>The tag keys being removed from the resources.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_meetings.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.untag_resource

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_attendee_capabilities(
        self,
        meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        attendee_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString",
        capabilities: "aws_sdk_chime_sdk_meetings.types.attendee_capabilities.AttendeeCapabilities",
        *,
        config_overrides: Optional[ChimeSDKMeetingsClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_meetings.types.update_attendee_capabilities_response.UpdateAttendeeCapabilitiesResponse":
        """<p>The capabilities that you want to update.</p> <note> <p>You use the capabilities with a set of values that control what the capabilities can do, such as <code>SendReceive</code> data. For more information about those values, see .</p> </note> <p>When using capabilities, be aware of these corner cases:</p> <ul> <li> <p>If you specify <code>MeetingFeatures:Video:MaxResolution:None</code> when you create a meeting, all API requests that include <code>SendReceive</code>, <code>Send</code>, or <code>Receive</code> for <code>AttendeeCapabilities:Video</code> will be rejected with <code>ValidationError 400</code>.</p> </li> <li> <p>If you specify <code>MeetingFeatures:Content:MaxResolution:None</code> when you create a meeting, all API requests that include <code>SendReceive</code>, <code>Send</code>, or <code>Receive</code> for <code>AttendeeCapabilities:Content</code> will be rejected with <code>ValidationError 400</code>.</p> </li> <li> <p>You can't set <code>content</code> capabilities to <code>SendReceive</code> or <code>Receive</code> unless you also set <code>video</code> capabilities to <code>SendReceive</code> or <code>Receive</code>. If you don't set the <code>video</code> capability to receive, the response will contain an HTTP 400 Bad Request status code. However, you can set your <code>video</code> capability to receive and you set your <code>content</code> capability to not receive.</p> </li> <li> <p>If meeting features is defined as <code>Video:MaxResolution:None</code> but <code>Content:MaxResolution</code> is defined as something other than <code>None</code> and attendee capabilities are not defined in the API request, then the default attendee video capability is set to <code>Receive</code> and attendee content capability is set to <code>SendReceive</code>. This is because content <code>SendReceive</code> requires video to be at least <code>Receive</code>.</p> </li> <li> <p>When you change an <code>audio</code> capability from <code>None</code> or <code>Receive</code> to <code>Send</code> or <code>SendReceive</code> , and if the attendee left their microphone unmuted, audio will flow from the attendee to the other meeting participants.</p> </li> <li> <p>When you change a <code>video</code> or <code>content</code> capability from <code>None</code> or <code>Receive</code> to <code>Send</code> or <code>SendReceive</code> , and if the attendee turned on their video or content streams, remote attendees can receive those streams, but only after media renegotiation between the client and the Amazon Chime back-end server.</p> </li> </ul>

        Args:
            meeting_id: <p>The ID of the meeting associated with the update request.</p>
            attendee_id: <p>The ID of the attendee associated with the update request.</p>
            capabilities: <p>The capabilities that you want to update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_meetings.types.update_attendee_capabilities_request.UpdateAttendeeCapabilitiesRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_meetings.types.update_attendee_capabilities_response.UpdateAttendeeCapabilitiesResponse"
        ]:
            import aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.update_attendee_capabilities

            output, http_response = (
                aws_sdk_chime_sdk_meetings._operations.chime_meetings_sdk_service.update_attendee_capabilities.update_attendee_capabilities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_meetings.types.update_attendee_capabilities_request.UpdateAttendeeCapabilitiesRequest = {}  # type: ignore[typeddict-item]
        input_["meeting_id"] = meeting_id
        input_["attendee_id"] = attendee_id
        input_["capabilities"] = capabilities

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
