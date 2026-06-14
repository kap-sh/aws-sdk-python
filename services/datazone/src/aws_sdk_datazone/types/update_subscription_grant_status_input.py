"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateSubscriptionGrantStatusInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.failure_cause
    import aws_sdk_datazone.types.subscription_grant_id
    import aws_sdk_datazone.types.subscription_grant_status


class UpdateSubscriptionGrantStatusInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a subscription grant status is to be updated.</p>"""
    identifier: "aws_sdk_datazone.types.subscription_grant_id.SubscriptionGrantId"
    """<p>The identifier of the subscription grant the status of which is to be updated.</p>"""
    asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The identifier of the asset the subscription grant status of which is to be updated.</p>"""
    status: "aws_sdk_datazone.types.subscription_grant_status.SubscriptionGrantStatus"
    """<p>The status to be updated as part of the <code>UpdateSubscriptionGrantStatus</code> action.</p>"""
    failure_cause: NotRequired["aws_sdk_datazone.types.failure_cause.FailureCause"]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    target_name: NotRequired["str"]
    """<p>The target name to be updated as part of the <code>UpdateSubscriptionGrantStatus</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriptionGrantStatusInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.subscription_grant_status

    out["status"] = aws_sdk_datazone.types.subscription_grant_status.serialize_json(
        value["status"]
    )
    if "failure_cause" in value:
        import aws_sdk_datazone.types.failure_cause

        out["failureCause"] = aws_sdk_datazone.types.failure_cause.serialize_json(
            value["failure_cause"]
        )
    if "target_name" in value:
        out["targetName"] = value["target_name"]
    return out


def deserialize_json(data: dict) -> UpdateSubscriptionGrantStatusInput:
    out: UpdateSubscriptionGrantStatusInput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_datazone.types.subscription_grant_status

        out["status"] = (
            aws_sdk_datazone.types.subscription_grant_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateSubscriptionGrantStatusInput.status required")
    if "failureCause" in data:
        import aws_sdk_datazone.types.failure_cause

        out["failure_cause"] = aws_sdk_datazone.types.failure_cause.deserialize_json(
            data["failureCause"]
        )
    if "targetName" in data:
        out["target_name"] = data["targetName"]
    return out
