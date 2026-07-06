"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_filter_name


class RegistrationFilter(TypedDict, closed=True):
    name: "aws_sdk_pinpoint_sms_voice_v2.types.registration_filter_name.RegistrationFilterName"
    """<p>The name of the attribute to filter on.</p>"""
    values: "aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list.FilterValueList"
    """<p>An array of values to filter on.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationFilter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list

    out["Values"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationFilter:
    out: RegistrationFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RegistrationFilter.name required")
    if "Values" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list

        out["values"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("RegistrationFilter.values required")
    return out
