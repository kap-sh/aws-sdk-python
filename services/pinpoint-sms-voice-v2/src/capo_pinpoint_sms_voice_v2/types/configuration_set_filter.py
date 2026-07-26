"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConfigurationSetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_filter_name
    import capo_pinpoint_sms_voice_v2.types.filter_value_list


class ConfigurationSetFilter(TypedDict, closed=True):
    name: "capo_pinpoint_sms_voice_v2.types.configuration_set_filter_name.ConfigurationSetFilterName"
    """<p>The name of the attribute to filter on.</p>"""
    values: "capo_pinpoint_sms_voice_v2.types.filter_value_list.FilterValueList"
    """<p>An array values to filter for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurationSetFilter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_pinpoint_sms_voice_v2.types.filter_value_list

    out["Values"] = (
        capo_pinpoint_sms_voice_v2.types.filter_value_list.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConfigurationSetFilter:
    out: ConfigurationSetFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ConfigurationSetFilter.name required")
    if "Values" in data:
        import capo_pinpoint_sms_voice_v2.types.filter_value_list

        out["values"] = (
            capo_pinpoint_sms_voice_v2.types.filter_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("ConfigurationSetFilter.values required")
    return out
