"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteEventDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.event_destination_name


class DeleteEventDestinationRequest(TypedDict):
    configuration_set_name: "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    """<p>The name of the configuration set or the configuration set's Amazon Resource Name (ARN) to remove the event destination from. The ConfigurateSetName and ConfigurationSetArn can be found using the <a>DescribeConfigurationSets</a> action.</p>"""
    event_destination_name: "aws_sdk_pinpoint_sms_voice_v2.types.event_destination_name.EventDestinationName"
    """<p>The name of the event destination to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEventDestinationRequest) -> dict:
    out: dict = {}
    out["ConfigurationSetName"] = value["configuration_set_name"]
    out["EventDestinationName"] = value["event_destination_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEventDestinationRequest:
    out: DeleteEventDestinationRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        raise DeserializationError(
            "DeleteEventDestinationRequest.configuration_set_name required"
        )
    if "EventDestinationName" in data:
        out["event_destination_name"] = data["EventDestinationName"]
    else:
        raise DeserializationError(
            "DeleteEventDestinationRequest.event_destination_name required"
        )
    return out
