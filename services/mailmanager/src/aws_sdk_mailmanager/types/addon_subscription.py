"""Generated from Smithy shape ``com.amazonaws.mailmanager#AddonSubscription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.addon_name
    import aws_sdk_mailmanager.types.addon_subscription_arn
    import aws_sdk_mailmanager.types.addon_subscription_id


class AddonSubscription(TypedDict):
    addon_subscription_id: NotRequired[
        "aws_sdk_mailmanager.types.addon_subscription_id.AddonSubscriptionId"
    ]
    """<p>The unique ID of the Add On subscription.</p>"""
    addon_name: NotRequired["aws_sdk_mailmanager.types.addon_name.AddonName"]
    """<p>The name of the Add On.</p>"""
    addon_subscription_arn: NotRequired[
        "aws_sdk_mailmanager.types.addon_subscription_arn.AddonSubscriptionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Add On subscription.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the Add On subscription was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddonSubscription) -> dict:
    out: dict = {}
    if "addon_subscription_id" in value:
        out["AddonSubscriptionId"] = value["addon_subscription_id"]
    if "addon_name" in value:
        out["AddonName"] = value["addon_name"]
    if "addon_subscription_arn" in value:
        out["AddonSubscriptionArn"] = value["addon_subscription_arn"]
    if "created_timestamp" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AddonSubscription:
    out: AddonSubscription = {}  # type: ignore[typeddict-item]
    if "AddonSubscriptionId" in data:
        out["addon_subscription_id"] = data["AddonSubscriptionId"]
    if "AddonName" in data:
        out["addon_name"] = data["AddonName"]
    if "AddonSubscriptionArn" in data:
        out["addon_subscription_arn"] = data["AddonSubscriptionArn"]
    if "CreatedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    return out
