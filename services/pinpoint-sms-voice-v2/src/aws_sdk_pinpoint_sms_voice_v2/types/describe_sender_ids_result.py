"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeSenderIdsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information_list


class DescribeSenderIdsResult(TypedDict):
    sender_ids: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information_list.SenderIdInformationList"
    ]
    """<p>An array of SernderIdInformation objects that contain the details for the requested SenderIds.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeSenderIdsResult) -> dict:
    out: dict = {}
    if "sender_ids" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information_list

        out["SenderIds"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information_list.serialize_aws_json_1_0(
                value["sender_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeSenderIdsResult:
    out: DescribeSenderIdsResult = {}  # type: ignore[typeddict-item]
    if "SenderIds" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information_list

        out["sender_ids"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information_list.deserialize_aws_json_1_0(
                data["SenderIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
