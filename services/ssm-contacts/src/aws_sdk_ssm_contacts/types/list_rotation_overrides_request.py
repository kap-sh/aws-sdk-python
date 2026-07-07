"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListRotationOverridesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.max_results
    import aws_sdk_ssm_contacts.types.pagination_token
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class ListRotationOverridesRequest(TypedDict, closed=True):
    rotation_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the rotation to retrieve information about.</p>"""
    start_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The date and time for the beginning of a time range for listing overrides.</p>"""
    end_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The date and time for the end of a time range for listing overrides.</p>"""
    next_token: NotRequired[
        "aws_sdk_ssm_contacts.types.pagination_token.PaginationToken"
    ]
    """<p>A token to start the list. Use this token to get the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_ssm_contacts.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRotationOverridesRequest) -> dict:
    out: dict = {}
    out["RotationId"] = value["rotation_id"]
    import aws_sdk_ssm_contacts.types.date_time

    out["StartTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["start_time"]
    )
    import aws_sdk_ssm_contacts.types.date_time

    out["EndTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["end_time"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRotationOverridesRequest:
    out: ListRotationOverridesRequest = {}  # type: ignore[typeddict-item]
    if "RotationId" in data:
        out["rotation_id"] = data["RotationId"]
    else:
        raise DeserializationError("ListRotationOverridesRequest.rotation_id required")
    if "StartTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["start_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    else:
        raise DeserializationError("ListRotationOverridesRequest.start_time required")
    if "EndTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["end_time"] = aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    else:
        raise DeserializationError("ListRotationOverridesRequest.end_time required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
