"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#VerifiedDestinationNumberFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list
    import aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_filter_name


class VerifiedDestinationNumberFilter(TypedDict):
    name: "aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_filter_name.VerifiedDestinationNumberFilterName"
    """<p>The name of the attribute to filter on.</p>"""
    values: "aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list.FilterValueList"
    """<p>An array of values to filter on.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerifiedDestinationNumberFilter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list

    out["Values"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> VerifiedDestinationNumberFilter:
    out: VerifiedDestinationNumberFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("VerifiedDestinationNumberFilter.name required")
    if "Values" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list

        out["values"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("VerifiedDestinationNumberFilter.values required")
    return out
