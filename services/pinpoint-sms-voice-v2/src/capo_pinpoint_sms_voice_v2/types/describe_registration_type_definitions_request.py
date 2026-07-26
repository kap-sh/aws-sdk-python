"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationTypeDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.registration_type_filter_list
    import capo_pinpoint_sms_voice_v2.types.registration_type_list


class DescribeRegistrationTypeDefinitionsRequest(TypedDict, closed=True):
    registration_types: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.registration_type_list.RegistrationTypeList"
    ]
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    filters: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.registration_type_filter_list.RegistrationTypeFilterList"
    ]
    """<p>An array of RegistrationFilter objects to filter the results.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationTypeDefinitionsRequest) -> dict:
    out: dict = {}
    if "registration_types" in value:
        import capo_pinpoint_sms_voice_v2.types.registration_type_list

        out["RegistrationTypes"] = (
            capo_pinpoint_sms_voice_v2.types.registration_type_list.serialize_aws_json_1_0(
                value["registration_types"]
            )
        )
    if "filters" in value:
        import capo_pinpoint_sms_voice_v2.types.registration_type_filter_list

        out["Filters"] = (
            capo_pinpoint_sms_voice_v2.types.registration_type_filter_list.serialize_aws_json_1_0(
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
        import capo_pinpoint_sms_voice_v2.types.registration_type_list

        out["registration_types"] = (
            capo_pinpoint_sms_voice_v2.types.registration_type_list.deserialize_aws_json_1_0(
                data["RegistrationTypes"]
            )
        )
    if "Filters" in data:
        import capo_pinpoint_sms_voice_v2.types.registration_type_filter_list

        out["filters"] = (
            capo_pinpoint_sms_voice_v2.types.registration_type_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
