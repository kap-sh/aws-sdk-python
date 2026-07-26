"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListPoolOriginationIdentitiesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.origination_identity_metadata_list


class ListPoolOriginationIdentitiesResult(TypedDict, closed=True):
    pool_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the pool.</p>"""
    pool_id: NotRequired["str"]
    """<p>The unique PoolId of the pool.</p>"""
    origination_identities: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.origination_identity_metadata_list.OriginationIdentityMetadataList"
    ]
    """<p>An array of any OriginationIdentityMetadata objects.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPoolOriginationIdentitiesResult) -> dict:
    out: dict = {}
    if "pool_arn" in value:
        out["PoolArn"] = value["pool_arn"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "origination_identities" in value:
        import capo_pinpoint_sms_voice_v2.types.origination_identity_metadata_list

        out["OriginationIdentities"] = (
            capo_pinpoint_sms_voice_v2.types.origination_identity_metadata_list.serialize_aws_json_1_0(
                value["origination_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPoolOriginationIdentitiesResult:
    out: ListPoolOriginationIdentitiesResult = {}  # type: ignore[typeddict-item]
    if "PoolArn" in data:
        out["pool_arn"] = data["PoolArn"]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    if "OriginationIdentities" in data:
        import capo_pinpoint_sms_voice_v2.types.origination_identity_metadata_list

        out["origination_identities"] = (
            capo_pinpoint_sms_voice_v2.types.origination_identity_metadata_list.deserialize_aws_json_1_0(
                data["OriginationIdentities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
