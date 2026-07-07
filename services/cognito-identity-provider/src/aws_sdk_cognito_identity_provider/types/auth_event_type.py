"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AuthEventType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.challenge_response_list_type
    import aws_sdk_cognito_identity_provider.types.date_type
    import aws_sdk_cognito_identity_provider.types.event_context_data_type
    import aws_sdk_cognito_identity_provider.types.event_feedback_type
    import aws_sdk_cognito_identity_provider.types.event_response_type
    import aws_sdk_cognito_identity_provider.types.event_risk_type
    import aws_sdk_cognito_identity_provider.types.event_type
    import aws_sdk_cognito_identity_provider.types.string_type


class AuthEventType(TypedDict, closed=True):
    event_id: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The event ID.</p>"""
    event_type: NotRequired[
        "aws_sdk_cognito_identity_provider.types.event_type.EventType"
    ]
    """<p>The type of authentication event.</p>"""
    creation_date: NotRequired[
        "aws_sdk_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    event_response: NotRequired[
        "aws_sdk_cognito_identity_provider.types.event_response_type.EventResponseType"
    ]
    """<p>The event response.</p>"""
    event_risk: NotRequired[
        "aws_sdk_cognito_identity_provider.types.event_risk_type.EventRiskType"
    ]
    """<p>The threat evaluation from your user pool about an event. Contains information about whether your user pool detected compromised credentials, whether the event triggered an automated response, and the level of risk.</p>"""
    challenge_responses: NotRequired[
        "aws_sdk_cognito_identity_provider.types.challenge_response_list_type.ChallengeResponseListType"
    ]
    """<p>A list of the challenges that the user was requested to answer, for example <code>Password</code>, and the result, for example <code>Success</code>.</p>"""
    event_context_data: NotRequired[
        "aws_sdk_cognito_identity_provider.types.event_context_data_type.EventContextDataType"
    ]
    """<p>The user context data captured at the time of an event request. This value provides additional information about the client from which event the request is received.</p>"""
    event_feedback: NotRequired[
        "aws_sdk_cognito_identity_provider.types.event_feedback_type.EventFeedbackType"
    ]
    """<p>The <code>UpdateAuthEventFeedback</code> or <code>AdminUpdateAuthEventFeedback</code> feedback that you or your user provided in response to the event. A value of <code>Valid</code> indicates that you disagreed with the level of risk that your user pool assigned, and evaluated a session to be valid, or likely safe. A value of <code>Invalid</code> indicates that you agreed with the user pool risk level and evaluated a session to be invalid, or likely malicious.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthEventType) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["EventId"] = value["event_id"]
    if "event_type" in value:
        import aws_sdk_cognito_identity_provider.types.event_type

        out["EventType"] = (
            aws_sdk_cognito_identity_provider.types.event_type.serialize_aws_json_1_1(
                value["event_type"]
            )
        )
    if "creation_date" in value:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["CreationDate"] = (
            aws_sdk_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "event_response" in value:
        import aws_sdk_cognito_identity_provider.types.event_response_type

        out["EventResponse"] = (
            aws_sdk_cognito_identity_provider.types.event_response_type.serialize_aws_json_1_1(
                value["event_response"]
            )
        )
    if "event_risk" in value:
        import aws_sdk_cognito_identity_provider.types.event_risk_type

        out["EventRisk"] = (
            aws_sdk_cognito_identity_provider.types.event_risk_type.serialize_aws_json_1_1(
                value["event_risk"]
            )
        )
    if "challenge_responses" in value:
        import aws_sdk_cognito_identity_provider.types.challenge_response_list_type

        out["ChallengeResponses"] = (
            aws_sdk_cognito_identity_provider.types.challenge_response_list_type.serialize_aws_json_1_1(
                value["challenge_responses"]
            )
        )
    if "event_context_data" in value:
        import aws_sdk_cognito_identity_provider.types.event_context_data_type

        out["EventContextData"] = (
            aws_sdk_cognito_identity_provider.types.event_context_data_type.serialize_aws_json_1_1(
                value["event_context_data"]
            )
        )
    if "event_feedback" in value:
        import aws_sdk_cognito_identity_provider.types.event_feedback_type

        out["EventFeedback"] = (
            aws_sdk_cognito_identity_provider.types.event_feedback_type.serialize_aws_json_1_1(
                value["event_feedback"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthEventType:
    out: AuthEventType = {}  # type: ignore[typeddict-item]
    if "EventId" in data:
        out["event_id"] = data["EventId"]
    if "EventType" in data:
        import aws_sdk_cognito_identity_provider.types.event_type

        out["event_type"] = (
            aws_sdk_cognito_identity_provider.types.event_type.deserialize_aws_json_1_1(
                data["EventType"]
            )
        )
    if "CreationDate" in data:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            aws_sdk_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    if "EventResponse" in data:
        import aws_sdk_cognito_identity_provider.types.event_response_type

        out["event_response"] = (
            aws_sdk_cognito_identity_provider.types.event_response_type.deserialize_aws_json_1_1(
                data["EventResponse"]
            )
        )
    if "EventRisk" in data:
        import aws_sdk_cognito_identity_provider.types.event_risk_type

        out["event_risk"] = (
            aws_sdk_cognito_identity_provider.types.event_risk_type.deserialize_aws_json_1_1(
                data["EventRisk"]
            )
        )
    if "ChallengeResponses" in data:
        import aws_sdk_cognito_identity_provider.types.challenge_response_list_type

        out["challenge_responses"] = (
            aws_sdk_cognito_identity_provider.types.challenge_response_list_type.deserialize_aws_json_1_1(
                data["ChallengeResponses"]
            )
        )
    if "EventContextData" in data:
        import aws_sdk_cognito_identity_provider.types.event_context_data_type

        out["event_context_data"] = (
            aws_sdk_cognito_identity_provider.types.event_context_data_type.deserialize_aws_json_1_1(
                data["EventContextData"]
            )
        )
    if "EventFeedback" in data:
        import aws_sdk_cognito_identity_provider.types.event_feedback_type

        out["event_feedback"] = (
            aws_sdk_cognito_identity_provider.types.event_feedback_type.deserialize_aws_json_1_1(
                data["EventFeedback"]
            )
        )
    return out
