"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutKeywordResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.keyword
    import capo_pinpoint_sms_voice_v2.types.keyword_action
    import capo_pinpoint_sms_voice_v2.types.keyword_message


class PutKeywordResult(TypedDict, closed=True):
    origination_identity_arn: NotRequired["str"]
    """<p>The PhoneNumberArn or PoolArn that the keyword was associated with.</p>"""
    origination_identity: NotRequired["str"]
    """<p>The PhoneNumberId or PoolId that the keyword was associated with.</p>"""
    keyword: NotRequired["capo_pinpoint_sms_voice_v2.types.keyword.Keyword"]
    """<p>The keyword that was added.</p>"""
    keyword_message: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.keyword_message.KeywordMessage"
    ]
    """<p>The message associated with the keyword.</p>"""
    keyword_action: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.keyword_action.KeywordAction"
    ]
    """<p>The action to perform when the keyword is used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutKeywordResult) -> dict:
    out: dict = {}
    if "origination_identity_arn" in value:
        out["OriginationIdentityArn"] = value["origination_identity_arn"]
    if "origination_identity" in value:
        out["OriginationIdentity"] = value["origination_identity"]
    if "keyword" in value:
        out["Keyword"] = value["keyword"]
    if "keyword_message" in value:
        out["KeywordMessage"] = value["keyword_message"]
    if "keyword_action" in value:
        out["KeywordAction"] = value["keyword_action"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutKeywordResult:
    out: PutKeywordResult = {}  # type: ignore[typeddict-item]
    if "OriginationIdentityArn" in data:
        out["origination_identity_arn"] = data["OriginationIdentityArn"]
    if "OriginationIdentity" in data:
        out["origination_identity"] = data["OriginationIdentity"]
    if "Keyword" in data:
        out["keyword"] = data["Keyword"]
    if "KeywordMessage" in data:
        out["keyword_message"] = data["KeywordMessage"]
    if "KeywordAction" in data:
        out["keyword_action"] = data["KeywordAction"]
    return out
