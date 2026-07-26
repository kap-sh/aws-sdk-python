"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateMeetingWithAttendeesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.client_request_token
    import capo_chime_sdk_meetings.types.create_meeting_with_attendees_request_item_list
    import capo_chime_sdk_meetings.types.external_meeting_id
    import capo_chime_sdk_meetings.types.external_user_id
    import capo_chime_sdk_meetings.types.media_placement_network_type
    import capo_chime_sdk_meetings.types.media_region
    import capo_chime_sdk_meetings.types.meeting_features_configuration
    import capo_chime_sdk_meetings.types.notifications_configuration
    import capo_chime_sdk_meetings.types.primary_meeting_id
    import capo_chime_sdk_meetings.types.tag_list
    import capo_chime_sdk_meetings.types.tenant_id_list


class CreateMeetingWithAttendeesRequest(TypedDict, closed=True):
    client_request_token: (
        "capo_chime_sdk_meetings.types.client_request_token.ClientRequestToken"
    )
    """<p>The unique identifier for the client request. Use a different token for different meetings.</p>"""
    media_region: "capo_chime_sdk_meetings.types.media_region.MediaRegion"
    """<p>The Region in which to create the meeting.</p> <p> Available values: <code>af-south-1</code>, <code>ap-northeast-1</code>, <code>ap-northeast-2</code>, <code>ap-south-1</code>, <code>ap-southeast-1</code>, <code>ap-southeast-2</code>, <code>ca-central-1</code>, <code>eu-central-1</code>, <code>eu-north-1</code>, <code>eu-south-1</code>, <code>eu-west-1</code>, <code>eu-west-2</code>, <code>eu-west-3</code>, <code>sa-east-1</code>, <code>us-east-1</code>, <code>us-east-2</code>, <code>us-west-1</code>, <code>us-west-2</code>. </p> <p>Available values in Amazon Web Services GovCloud (US) Regions: <code>us-gov-east-1</code>, <code>us-gov-west-1</code>.</p>"""
    meeting_host_id: NotRequired[
        "capo_chime_sdk_meetings.types.external_user_id.ExternalUserId"
    ]
    """<p>Reserved.</p>"""
    external_meeting_id: (
        "capo_chime_sdk_meetings.types.external_meeting_id.ExternalMeetingId"
    )
    r"""<p>The external meeting ID.</p> <p>Pattern: <code>[-_&@+=,(){}\[\]\/«».:|'\"#a-zA-Z0-9À-ÿ\s]*</code> </p> <p>Values that begin with <code>aws:</code> are reserved. You can't configure a value that uses this prefix. Case insensitive.</p>"""
    meeting_features: NotRequired[
        "capo_chime_sdk_meetings.types.meeting_features_configuration.MeetingFeaturesConfiguration"
    ]
    """<p>Lists the audio and video features enabled for a meeting, such as echo reduction.</p>"""
    notifications_configuration: NotRequired[
        "capo_chime_sdk_meetings.types.notifications_configuration.NotificationsConfiguration"
    ]
    """<p>The configuration for resource targets to receive notifications when meeting and attendee events occur.</p>"""
    attendees: "capo_chime_sdk_meetings.types.create_meeting_with_attendees_request_item_list.CreateMeetingWithAttendeesRequestItemList"
    """<p>The attendee information, including attendees' IDs and join tokens.</p>"""
    primary_meeting_id: NotRequired[
        "capo_chime_sdk_meetings.types.primary_meeting_id.PrimaryMeetingId"
    ]
    """<p>When specified, replicates the media from the primary meeting to the new meeting.</p>"""
    tenant_ids: NotRequired["capo_chime_sdk_meetings.types.tenant_id_list.TenantIdList"]
    """<p>A consistent and opaque identifier, created and maintained by the builder to represent a segment of their users.</p>"""
    tags: NotRequired["capo_chime_sdk_meetings.types.tag_list.TagList"]
    """<p>The tags in the request.</p>"""
    media_placement_network_type: NotRequired[
        "capo_chime_sdk_meetings.types.media_placement_network_type.MediaPlacementNetworkType"
    ]
    """<p>The type of network for the media placement. Either IPv4 only or dual-stack (IPv4 and IPv6).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMeetingWithAttendeesRequest) -> dict:
    out: dict = {}
    out["ClientRequestToken"] = value["client_request_token"]
    out["MediaRegion"] = value["media_region"]
    if "meeting_host_id" in value:
        out["MeetingHostId"] = value["meeting_host_id"]
    out["ExternalMeetingId"] = value["external_meeting_id"]
    if "meeting_features" in value:
        import capo_chime_sdk_meetings.types.meeting_features_configuration

        out["MeetingFeatures"] = (
            capo_chime_sdk_meetings.types.meeting_features_configuration.serialize_json(
                value["meeting_features"]
            )
        )
    if "notifications_configuration" in value:
        import capo_chime_sdk_meetings.types.notifications_configuration

        out["NotificationsConfiguration"] = (
            capo_chime_sdk_meetings.types.notifications_configuration.serialize_json(
                value["notifications_configuration"]
            )
        )
    import capo_chime_sdk_meetings.types.create_meeting_with_attendees_request_item_list

    out["Attendees"] = (
        capo_chime_sdk_meetings.types.create_meeting_with_attendees_request_item_list.serialize_json(
            value["attendees"]
        )
    )
    if "primary_meeting_id" in value:
        out["PrimaryMeetingId"] = value["primary_meeting_id"]
    if "tenant_ids" in value:
        import capo_chime_sdk_meetings.types.tenant_id_list

        out["TenantIds"] = capo_chime_sdk_meetings.types.tenant_id_list.serialize_json(
            value["tenant_ids"]
        )
    if "tags" in value:
        import capo_chime_sdk_meetings.types.tag_list

        out["Tags"] = capo_chime_sdk_meetings.types.tag_list.serialize_json(
            value["tags"]
        )
    if "media_placement_network_type" in value:
        import capo_chime_sdk_meetings.types.media_placement_network_type

        out["MediaPlacementNetworkType"] = (
            capo_chime_sdk_meetings.types.media_placement_network_type.serialize_json(
                value["media_placement_network_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMeetingWithAttendeesRequest:
    out: CreateMeetingWithAttendeesRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError(
            "CreateMeetingWithAttendeesRequest.client_request_token required"
        )
    if "MediaRegion" in data:
        out["media_region"] = data["MediaRegion"]
    else:
        raise DeserializationError(
            "CreateMeetingWithAttendeesRequest.media_region required"
        )
    if "MeetingHostId" in data:
        out["meeting_host_id"] = data["MeetingHostId"]
    if "ExternalMeetingId" in data:
        out["external_meeting_id"] = data["ExternalMeetingId"]
    else:
        raise DeserializationError(
            "CreateMeetingWithAttendeesRequest.external_meeting_id required"
        )
    if "MeetingFeatures" in data:
        import capo_chime_sdk_meetings.types.meeting_features_configuration

        out["meeting_features"] = (
            capo_chime_sdk_meetings.types.meeting_features_configuration.deserialize_json(
                data["MeetingFeatures"]
            )
        )
    if "NotificationsConfiguration" in data:
        import capo_chime_sdk_meetings.types.notifications_configuration

        out["notifications_configuration"] = (
            capo_chime_sdk_meetings.types.notifications_configuration.deserialize_json(
                data["NotificationsConfiguration"]
            )
        )
    if "Attendees" in data:
        import capo_chime_sdk_meetings.types.create_meeting_with_attendees_request_item_list

        out["attendees"] = (
            capo_chime_sdk_meetings.types.create_meeting_with_attendees_request_item_list.deserialize_json(
                data["Attendees"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMeetingWithAttendeesRequest.attendees required"
        )
    if "PrimaryMeetingId" in data:
        out["primary_meeting_id"] = data["PrimaryMeetingId"]
    if "TenantIds" in data:
        import capo_chime_sdk_meetings.types.tenant_id_list

        out["tenant_ids"] = (
            capo_chime_sdk_meetings.types.tenant_id_list.deserialize_json(
                data["TenantIds"]
            )
        )
    if "Tags" in data:
        import capo_chime_sdk_meetings.types.tag_list

        out["tags"] = capo_chime_sdk_meetings.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "MediaPlacementNetworkType" in data:
        import capo_chime_sdk_meetings.types.media_placement_network_type

        out["media_placement_network_type"] = (
            capo_chime_sdk_meetings.types.media_placement_network_type.deserialize_json(
                data["MediaPlacementNetworkType"]
            )
        )
    return out
