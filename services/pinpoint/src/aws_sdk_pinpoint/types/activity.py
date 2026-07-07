"""Generated from Smithy shape ``com.amazonaws.pinpoint#Activity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.conditional_split_activity
    import aws_sdk_pinpoint.types.contact_center_activity
    import aws_sdk_pinpoint.types.custom_message_activity
    import aws_sdk_pinpoint.types.email_message_activity
    import aws_sdk_pinpoint.types.holdout_activity
    import aws_sdk_pinpoint.types.multi_conditional_split_activity
    import aws_sdk_pinpoint.types.push_message_activity
    import aws_sdk_pinpoint.types.random_split_activity
    import aws_sdk_pinpoint.types.sms_message_activity
    import aws_sdk_pinpoint.types.wait_activity


class Activity(TypedDict, closed=True):
    custom: NotRequired[
        "aws_sdk_pinpoint.types.custom_message_activity.CustomMessageActivity"
    ]
    """<p>The settings for a custom message activity. This type of activity calls an AWS Lambda function or web hook that sends messages to participants.</p>"""
    conditional_split: NotRequired[
        "aws_sdk_pinpoint.types.conditional_split_activity.ConditionalSplitActivity"
    ]
    """<p>The settings for a yes/no split activity. This type of activity sends participants down one of two paths in a journey, based on conditions that you specify.</p>"""
    description: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The custom description of the activity.</p>"""
    email: NotRequired[
        "aws_sdk_pinpoint.types.email_message_activity.EmailMessageActivity"
    ]
    """<p>The settings for an email activity. This type of activity sends an email message to participants.</p>"""
    holdout: NotRequired["aws_sdk_pinpoint.types.holdout_activity.HoldoutActivity"]
    """<p>The settings for a holdout activity. This type of activity stops a journey for a specified percentage of participants.</p>"""
    multi_condition: NotRequired[
        "aws_sdk_pinpoint.types.multi_conditional_split_activity.MultiConditionalSplitActivity"
    ]
    """<p>The settings for a multivariate split activity. This type of activity sends participants down one of as many as five paths (including a default <i>Else</i> path) in a journey, based on conditions that you specify.</p>"""
    push: NotRequired[
        "aws_sdk_pinpoint.types.push_message_activity.PushMessageActivity"
    ]
    """<p>The settings for a push notification activity. This type of activity sends a push notification to participants.</p>"""
    random_split: NotRequired[
        "aws_sdk_pinpoint.types.random_split_activity.RandomSplitActivity"
    ]
    """<p>The settings for a random split activity. This type of activity randomly sends specified percentages of participants down one of as many as five paths in a journey, based on conditions that you specify.</p>"""
    sms: NotRequired["aws_sdk_pinpoint.types.sms_message_activity.SMSMessageActivity"]
    """<p>The settings for an SMS activity. This type of activity sends a text message to participants.</p>"""
    wait: NotRequired["aws_sdk_pinpoint.types.wait_activity.WaitActivity"]
    """<p>The settings for a wait activity. This type of activity waits for a certain amount of time or until a specific date and time before moving participants to the next activity in a journey.</p>"""
    contact_center: NotRequired[
        "aws_sdk_pinpoint.types.contact_center_activity.ContactCenterActivity"
    ]
    """<p>The settings for a connect activity. This type of activity initiates a contact center call to participants.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Activity) -> dict:
    out: dict = {}
    if "custom" in value:
        import aws_sdk_pinpoint.types.custom_message_activity

        out["CUSTOM"] = aws_sdk_pinpoint.types.custom_message_activity.serialize_json(
            value["custom"]
        )
    if "conditional_split" in value:
        import aws_sdk_pinpoint.types.conditional_split_activity

        out["ConditionalSplit"] = (
            aws_sdk_pinpoint.types.conditional_split_activity.serialize_json(
                value["conditional_split"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "email" in value:
        import aws_sdk_pinpoint.types.email_message_activity

        out["EMAIL"] = aws_sdk_pinpoint.types.email_message_activity.serialize_json(
            value["email"]
        )
    if "holdout" in value:
        import aws_sdk_pinpoint.types.holdout_activity

        out["Holdout"] = aws_sdk_pinpoint.types.holdout_activity.serialize_json(
            value["holdout"]
        )
    if "multi_condition" in value:
        import aws_sdk_pinpoint.types.multi_conditional_split_activity

        out["MultiCondition"] = (
            aws_sdk_pinpoint.types.multi_conditional_split_activity.serialize_json(
                value["multi_condition"]
            )
        )
    if "push" in value:
        import aws_sdk_pinpoint.types.push_message_activity

        out["PUSH"] = aws_sdk_pinpoint.types.push_message_activity.serialize_json(
            value["push"]
        )
    if "random_split" in value:
        import aws_sdk_pinpoint.types.random_split_activity

        out["RandomSplit"] = (
            aws_sdk_pinpoint.types.random_split_activity.serialize_json(
                value["random_split"]
            )
        )
    if "sms" in value:
        import aws_sdk_pinpoint.types.sms_message_activity

        out["SMS"] = aws_sdk_pinpoint.types.sms_message_activity.serialize_json(
            value["sms"]
        )
    if "wait" in value:
        import aws_sdk_pinpoint.types.wait_activity

        out["Wait"] = aws_sdk_pinpoint.types.wait_activity.serialize_json(value["wait"])
    if "contact_center" in value:
        import aws_sdk_pinpoint.types.contact_center_activity

        out["ContactCenter"] = (
            aws_sdk_pinpoint.types.contact_center_activity.serialize_json(
                value["contact_center"]
            )
        )
    return out


def deserialize_json(data: dict) -> Activity:
    out: Activity = {}  # type: ignore[typeddict-item]
    if "CUSTOM" in data:
        import aws_sdk_pinpoint.types.custom_message_activity

        out["custom"] = aws_sdk_pinpoint.types.custom_message_activity.deserialize_json(
            data["CUSTOM"]
        )
    if "ConditionalSplit" in data:
        import aws_sdk_pinpoint.types.conditional_split_activity

        out["conditional_split"] = (
            aws_sdk_pinpoint.types.conditional_split_activity.deserialize_json(
                data["ConditionalSplit"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "EMAIL" in data:
        import aws_sdk_pinpoint.types.email_message_activity

        out["email"] = aws_sdk_pinpoint.types.email_message_activity.deserialize_json(
            data["EMAIL"]
        )
    if "Holdout" in data:
        import aws_sdk_pinpoint.types.holdout_activity

        out["holdout"] = aws_sdk_pinpoint.types.holdout_activity.deserialize_json(
            data["Holdout"]
        )
    if "MultiCondition" in data:
        import aws_sdk_pinpoint.types.multi_conditional_split_activity

        out["multi_condition"] = (
            aws_sdk_pinpoint.types.multi_conditional_split_activity.deserialize_json(
                data["MultiCondition"]
            )
        )
    if "PUSH" in data:
        import aws_sdk_pinpoint.types.push_message_activity

        out["push"] = aws_sdk_pinpoint.types.push_message_activity.deserialize_json(
            data["PUSH"]
        )
    if "RandomSplit" in data:
        import aws_sdk_pinpoint.types.random_split_activity

        out["random_split"] = (
            aws_sdk_pinpoint.types.random_split_activity.deserialize_json(
                data["RandomSplit"]
            )
        )
    if "SMS" in data:
        import aws_sdk_pinpoint.types.sms_message_activity

        out["sms"] = aws_sdk_pinpoint.types.sms_message_activity.deserialize_json(
            data["SMS"]
        )
    if "Wait" in data:
        import aws_sdk_pinpoint.types.wait_activity

        out["wait"] = aws_sdk_pinpoint.types.wait_activity.deserialize_json(
            data["Wait"]
        )
    if "ContactCenter" in data:
        import aws_sdk_pinpoint.types.contact_center_activity

        out["contact_center"] = (
            aws_sdk_pinpoint.types.contact_center_activity.deserialize_json(
                data["ContactCenter"]
            )
        )
    return out
