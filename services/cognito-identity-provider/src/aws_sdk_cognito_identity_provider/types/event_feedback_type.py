"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EventFeedbackType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.date_type
    import aws_sdk_cognito_identity_provider.types.feedback_value_type
    import aws_sdk_cognito_identity_provider.types.string_type


class EventFeedbackType(TypedDict):
    feedback_value: (
        "aws_sdk_cognito_identity_provider.types.feedback_value_type.FeedbackValueType"
    )
    """<p>Your feedback to the authentication event. When you provide a <code>FeedbackValue</code> value of <code>valid</code>, you tell Amazon Cognito that you trust a user session where Amazon Cognito has evaluated some level of risk. When you provide a <code>FeedbackValue</code> value of <code>invalid</code>, you tell Amazon Cognito that you don't trust a user session, or you don't believe that Amazon Cognito evaluated a high-enough risk level.</p>"""
    provider: "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    """<p>The submitter of the event feedback. For example, if you submit event feedback in the Amazon Cognito console, this value is <code>Admin</code>.</p>"""
    feedback_date: NotRequired[
        "aws_sdk_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date that you or your user submitted the feedback.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventFeedbackType) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.feedback_value_type

    out["FeedbackValue"] = (
        aws_sdk_cognito_identity_provider.types.feedback_value_type.serialize_aws_json_1_1(
            value["feedback_value"]
        )
    )
    out["Provider"] = value["provider"]
    if "feedback_date" in value:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["FeedbackDate"] = (
            aws_sdk_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["feedback_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventFeedbackType:
    out: EventFeedbackType = {}  # type: ignore[typeddict-item]
    if "FeedbackValue" in data:
        import aws_sdk_cognito_identity_provider.types.feedback_value_type

        out["feedback_value"] = (
            aws_sdk_cognito_identity_provider.types.feedback_value_type.deserialize_aws_json_1_1(
                data["FeedbackValue"]
            )
        )
    else:
        raise DeserializationError("EventFeedbackType.feedback_value required")
    if "Provider" in data:
        out["provider"] = data["Provider"]
    else:
        raise DeserializationError("EventFeedbackType.provider required")
    if "FeedbackDate" in data:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["feedback_date"] = (
            aws_sdk_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["FeedbackDate"]
            )
        )
    return out
