"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationSectionDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.max_results
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type
    import aws_sdk_pinpoint_sms_voice_v2.types.section_path_list


class DescribeRegistrationSectionDefinitionsRequest(TypedDict):
    registration_type: (
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_type.RegistrationType"
    )
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    section_paths: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.section_path_list.SectionPathList"
    ]
    """<p>An array of paths for the registration form section.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: DescribeRegistrationSectionDefinitionsRequest,
) -> dict:
    out: dict = {}
    out["RegistrationType"] = value["registration_type"]
    if "section_paths" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.section_path_list

        out["SectionPaths"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.section_path_list.serialize_aws_json_1_0(
                value["section_paths"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> DescribeRegistrationSectionDefinitionsRequest:
    out: DescribeRegistrationSectionDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if "RegistrationType" in data:
        out["registration_type"] = data["RegistrationType"]
    else:
        raise DeserializationError(
            "DescribeRegistrationSectionDefinitionsRequest.registration_type required"
        )
    if "SectionPaths" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.section_path_list

        out["section_paths"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.section_path_list.deserialize_aws_json_1_0(
                data["SectionPaths"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
