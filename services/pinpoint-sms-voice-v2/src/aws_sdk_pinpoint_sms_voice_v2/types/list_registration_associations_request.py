"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListRegistrationAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.max_results
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_association_filter_list
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_id_or_arn


class ListRegistrationAssociationsRequest(TypedDict, closed=True):
    registration_id: (
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""
    filters: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_association_filter_list.RegistrationAssociationFilterList"
    ]
    """<p>An array of RegistrationAssociationFilter to apply to the results that are returned.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRegistrationAssociationsRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    if "filters" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_association_filter_list

        out["Filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_association_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRegistrationAssociationsRequest:
    out: ListRegistrationAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "ListRegistrationAssociationsRequest.registration_id required"
        )
    if "Filters" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_association_filter_list

        out["filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_association_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
