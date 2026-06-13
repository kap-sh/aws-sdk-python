"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeProtectConfigurationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_information_list


class DescribeProtectConfigurationsResult(TypedDict):
    protect_configurations: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_information_list.ProtectConfigurationInformationList"
    ]
    """<p>An array of ProtectConfigurationInformation objects that contain the details for the request. </p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeProtectConfigurationsResult) -> dict:
    out: dict = {}
    if "protect_configurations" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_information_list

        out["ProtectConfigurations"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_information_list.serialize_aws_json_1_0(
                value["protect_configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeProtectConfigurationsResult:
    out: DescribeProtectConfigurationsResult = {}  # type: ignore[typeddict-item]
    if "ProtectConfigurations" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_information_list

        out["protect_configurations"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.protect_configuration_information_list.deserialize_aws_json_1_0(
                data["ProtectConfigurations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
