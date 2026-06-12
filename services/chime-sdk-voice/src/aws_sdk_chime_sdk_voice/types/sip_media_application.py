"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipMediaApplication``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.iso8601_timestamp
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list
    import aws_sdk_chime_sdk_voice.types.sip_media_application_name
    import aws_sdk_chime_sdk_voice.types.string


class SipMediaApplication(TypedDict):
    sip_media_application_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>A SIP media application's ID.</p>"""
    aws_region: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The AWS Region in which the SIP media application is created.</p>"""
    name: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sip_media_application_name.SipMediaApplicationName"
    ]
    """<p>The SIP media application's name.</p>"""
    endpoints: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list.SipMediaApplicationEndpointList"
    ]
    """<p>List of endpoints for a SIP media application. Currently, only one endpoint per SIP media application is permitted.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The SIP media application creation timestamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the SIP media application was updated.</p>"""
    sip_media_application_arn: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SipMediaApplication) -> dict:
    out: dict = {}
    if "sip_media_application_id" in value:
        out["SipMediaApplicationId"] = value["sip_media_application_id"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    if "name" in value:
        out["Name"] = value["name"]
    if "endpoints" in value:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["Endpoints"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list.serialize_json(
                value["endpoints"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "sip_media_application_arn" in value:
        out["SipMediaApplicationArn"] = value["sip_media_application_arn"]
    return out


def deserialize_json(data: dict) -> SipMediaApplication:
    out: SipMediaApplication = {}  # type: ignore[typeddict-item]
    if "SipMediaApplicationId" in data:
        out["sip_media_application_id"] = data["SipMediaApplicationId"]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Endpoints" in data:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["endpoints"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list.deserialize_json(
                data["Endpoints"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if "SipMediaApplicationArn" in data:
        out["sip_media_application_arn"] = data["SipMediaApplicationArn"]
    return out
