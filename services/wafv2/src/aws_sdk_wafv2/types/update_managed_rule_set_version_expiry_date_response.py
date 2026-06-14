"""Generated from Smithy shape ``com.amazonaws.wafv2#UpdateManagedRuleSetVersionExpiryDateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.lock_token
    import aws_sdk_wafv2.types.timestamp
    import aws_sdk_wafv2.types.version_key_string


class UpdateManagedRuleSetVersionExpiryDateResponse(TypedDict):
    expiring_version: NotRequired[
        "aws_sdk_wafv2.types.version_key_string.VersionKeyString"
    ]
    """<p>The version that is set to expire. </p>"""
    expiry_timestamp: NotRequired["aws_sdk_wafv2.types.timestamp.Timestamp"]
    r"""<p>The time that the version will expire. </p> <p>Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, \"2016-09-27T14:50Z\". </p>"""
    next_lock_token: NotRequired["aws_sdk_wafv2.types.lock_token.LockToken"]
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateManagedRuleSetVersionExpiryDateResponse,
) -> dict:
    out: dict = {}
    if "expiring_version" in value:
        out["ExpiringVersion"] = value["expiring_version"]
    if "expiry_timestamp" in value:
        import aws_sdk_wafv2.types.timestamp

        out["ExpiryTimestamp"] = aws_sdk_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["expiry_timestamp"]
        )
    if "next_lock_token" in value:
        out["NextLockToken"] = value["next_lock_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateManagedRuleSetVersionExpiryDateResponse:
    out: UpdateManagedRuleSetVersionExpiryDateResponse = {}  # type: ignore[typeddict-item]
    if "ExpiringVersion" in data:
        out["expiring_version"] = data["ExpiringVersion"]
    if "ExpiryTimestamp" in data:
        import aws_sdk_wafv2.types.timestamp

        out["expiry_timestamp"] = (
            aws_sdk_wafv2.types.timestamp.deserialize_aws_json_1_1(
                data["ExpiryTimestamp"]
            )
        )
    if "NextLockToken" in data:
        out["next_lock_token"] = data["NextLockToken"]
    return out
