"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationTypeDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.max_results
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_filter_list
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_list


class DescribeRegistrationTypeDefinitionsRequest(TypedDict):
    registration_types: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_type_list.RegistrationTypeList"
    ]
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    filters: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_type_filter_list.RegistrationTypeFilterList"
    ]
    """<p>An array of RegistrationFilter objects to filter the results.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationTypeDefinitionsRequest) -> dict:
    out: dict = {}
    if "registration_types" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_list

        out["RegistrationTypes"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_type_list.serialize_aws_json_1_0(
                value["registration_types"]
            )
        )
    if "filters" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_filter_list

        out["Filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_type_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationTypeDefinitionsRequest:
    out: DescribeRegistrationTypeDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if "RegistrationTypes" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_list

        out["registration_types"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_type_list.deserialize_aws_json_1_0(
                data["RegistrationTypes"]
            )
        )
    if "Filters" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_filter_list

        out["filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_type_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
