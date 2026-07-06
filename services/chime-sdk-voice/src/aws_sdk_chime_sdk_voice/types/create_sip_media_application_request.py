"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateSipMediaApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list
    import aws_sdk_chime_sdk_voice.types.sip_media_application_name
    import aws_sdk_chime_sdk_voice.types.string
    import aws_sdk_chime_sdk_voice.types.tag_list


class CreateSipMediaApplicationRequest(TypedDict, closed=True):
    aws_region: "aws_sdk_chime_sdk_voice.types.string.String"
    """<p>The AWS Region assigned to the SIP media application.</p>"""
    name: "aws_sdk_chime_sdk_voice.types.sip_media_application_name.SipMediaApplicationName"
    """<p>The SIP media application's name.</p>"""
    endpoints: "aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list.SipMediaApplicationEndpointList"
    """<p>List of endpoints (Lambda ARNs) specified for the SIP media application.</p>"""
    tags: NotRequired["aws_sdk_chime_sdk_voice.types.tag_list.TagList"]
    """<p>The tags assigned to the SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSipMediaApplicationRequest) -> dict:
    out: dict = {}
    out["AwsRegion"] = value["aws_region"]
    out["Name"] = value["name"]
    import aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list

    out["Endpoints"] = (
        aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list.serialize_json(
            value["endpoints"]
        )
    )
    if "tags" in value:
        import aws_sdk_chime_sdk_voice.types.tag_list

        out["Tags"] = aws_sdk_chime_sdk_voice.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateSipMediaApplicationRequest:
    out: CreateSipMediaApplicationRequest = {}  # type: ignore[typeddict-item]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    else:
        raise DeserializationError(
            "CreateSipMediaApplicationRequest.aws_region required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateSipMediaApplicationRequest.name required")
    if "Endpoints" in data:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list

        out["endpoints"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_endpoint_list.deserialize_json(
                data["Endpoints"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSipMediaApplicationRequest.endpoints required"
        )
    if "Tags" in data:
        import aws_sdk_chime_sdk_voice.types.tag_list

        out["tags"] = aws_sdk_chime_sdk_voice.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out
