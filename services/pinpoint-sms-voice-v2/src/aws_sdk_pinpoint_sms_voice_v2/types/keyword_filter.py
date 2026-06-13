"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#KeywordFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list
    import aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter_name


class KeywordFilter(TypedDict):
    name: "aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter_name.KeywordFilterName"
    """<p>The name of the attribute to filter on.</p>"""
    values: "aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list.FilterValueList"
    """<p>An array values to filter for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeywordFilter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list

    out["Values"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> KeywordFilter:
    out: KeywordFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("KeywordFilter.name required")
    if "Values" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list

        out["values"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.filter_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("KeywordFilter.values required")
    return out
