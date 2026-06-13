"""Generated from Smithy shape ``com.amazonaws.connecthealth#CreateSubscriptionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_connecthealth.types.domain_id
    import aws_sdk_connecthealth.types.subscription_arn
    import aws_sdk_connecthealth.types.subscription_id
    import aws_sdk_connecthealth.types.subscription_status


class CreateSubscriptionOutput(TypedDict):
    domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId"
    """<p/>"""
    subscription_id: "aws_sdk_connecthealth.types.subscription_id.SubscriptionId"
    """<p/>"""
    arn: "aws_sdk_connecthealth.types.subscription_arn.SubscriptionArn"
    """<p/>"""
    status: "aws_sdk_connecthealth.types.subscription_status.SubscriptionStatus"
    """<p/>"""
    created_at: "datetime.datetime"
    """<p/>"""
    last_updated_at: "datetime.datetime"
    """<p/>"""
    activated_at: NotRequired["datetime.datetime"]
    """<p/>"""
    deactivated_at: NotRequired["datetime.datetime"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["subscriptionId"] = value["subscription_id"]
    out["arn"] = value["arn"]
    import aws_sdk_connecthealth.types.subscription_status

    out["status"] = aws_sdk_connecthealth.types.subscription_status.serialize_json(
        value["status"]
    )
    import aws_sdk_connecthealth.types._prelude.timestamp

    out["createdAt"] = aws_sdk_connecthealth.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_connecthealth.types._prelude.timestamp

    out["lastUpdatedAt"] = (
        aws_sdk_connecthealth.types._prelude.timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    if "activated_at" in value:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["activatedAt"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.serialize_json(
                value["activated_at"]
            )
        )
    if "deactivated_at" in value:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["deactivatedAt"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.serialize_json(
                value["deactivated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSubscriptionOutput:
    out: CreateSubscriptionOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateSubscriptionOutput.domain_id required")
    if "subscriptionId" in data:
        out["subscription_id"] = data["subscriptionId"]
    else:
        raise DeserializationError("CreateSubscriptionOutput.subscription_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateSubscriptionOutput.arn required")
    if "status" in data:
        import aws_sdk_connecthealth.types.subscription_status

        out["status"] = (
            aws_sdk_connecthealth.types.subscription_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateSubscriptionOutput.status required")
    if "createdAt" in data:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateSubscriptionOutput.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("CreateSubscriptionOutput.last_updated_at required")
    if "activatedAt" in data:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["activated_at"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.deserialize_json(
                data["activatedAt"]
            )
        )
    if "deactivatedAt" in data:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["deactivated_at"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.deserialize_json(
                data["deactivatedAt"]
            )
        )
    return out
