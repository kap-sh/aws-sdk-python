"""Generated from Smithy shape ``com.amazonaws.bedrock#GetGuardrailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_arn
    import aws_sdk_bedrock.types.guardrail_automated_reasoning_policy
    import aws_sdk_bedrock.types.guardrail_blocked_messaging
    import aws_sdk_bedrock.types.guardrail_content_policy
    import aws_sdk_bedrock.types.guardrail_contextual_grounding_policy
    import aws_sdk_bedrock.types.guardrail_cross_region_details
    import aws_sdk_bedrock.types.guardrail_description
    import aws_sdk_bedrock.types.guardrail_failure_recommendations
    import aws_sdk_bedrock.types.guardrail_id
    import aws_sdk_bedrock.types.guardrail_name
    import aws_sdk_bedrock.types.guardrail_sensitive_information_policy
    import aws_sdk_bedrock.types.guardrail_status
    import aws_sdk_bedrock.types.guardrail_status_reasons
    import aws_sdk_bedrock.types.guardrail_topic_policy
    import aws_sdk_bedrock.types.guardrail_version
    import aws_sdk_bedrock.types.guardrail_word_policy
    import aws_sdk_bedrock.types.kms_key_arn
    import aws_sdk_bedrock.types.timestamp


class GetGuardrailResponse(TypedDict, closed=True):
    name: "aws_sdk_bedrock.types.guardrail_name.GuardrailName"
    """<p>The name of the guardrail.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.guardrail_description.GuardrailDescription"
    ]
    """<p>The description of the guardrail.</p>"""
    guardrail_id: "aws_sdk_bedrock.types.guardrail_id.GuardrailId"
    """<p>The unique identifier of the guardrail.</p>"""
    guardrail_arn: "aws_sdk_bedrock.types.guardrail_arn.GuardrailArn"
    """<p>The ARN of the guardrail.</p>"""
    version: "aws_sdk_bedrock.types.guardrail_version.GuardrailVersion"
    """<p>The version of the guardrail.</p>"""
    status: "aws_sdk_bedrock.types.guardrail_status.GuardrailStatus"
    """<p>The status of the guardrail.</p>"""
    topic_policy: NotRequired[
        "aws_sdk_bedrock.types.guardrail_topic_policy.GuardrailTopicPolicy"
    ]
    """<p>The topic policy that was configured for the guardrail.</p>"""
    content_policy: NotRequired[
        "aws_sdk_bedrock.types.guardrail_content_policy.GuardrailContentPolicy"
    ]
    """<p>The content policy that was configured for the guardrail.</p>"""
    word_policy: NotRequired[
        "aws_sdk_bedrock.types.guardrail_word_policy.GuardrailWordPolicy"
    ]
    """<p>The word policy that was configured for the guardrail.</p>"""
    sensitive_information_policy: NotRequired[
        "aws_sdk_bedrock.types.guardrail_sensitive_information_policy.GuardrailSensitiveInformationPolicy"
    ]
    """<p>The sensitive information policy that was configured for the guardrail.</p>"""
    contextual_grounding_policy: NotRequired[
        "aws_sdk_bedrock.types.guardrail_contextual_grounding_policy.GuardrailContextualGroundingPolicy"
    ]
    """<p>The contextual grounding policy used in the guardrail.</p>"""
    automated_reasoning_policy: NotRequired[
        "aws_sdk_bedrock.types.guardrail_automated_reasoning_policy.GuardrailAutomatedReasoningPolicy"
    ]
    """<p>The current Automated Reasoning policy configuration for the guardrail, if any is configured.</p>"""
    cross_region_details: NotRequired[
        "aws_sdk_bedrock.types.guardrail_cross_region_details.GuardrailCrossRegionDetails"
    ]
    """<p>Details about the system-defined guardrail profile that you're using with your guardrail, including the guardrail profile ID and Amazon Resource Name (ARN).</p>"""
    created_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The date and time at which the guardrail was created.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The date and time at which the guardrail was updated.</p>"""
    status_reasons: NotRequired[
        "aws_sdk_bedrock.types.guardrail_status_reasons.GuardrailStatusReasons"
    ]
    """<p>Appears if the <code>status</code> is <code>FAILED</code>. A list of reasons for why the guardrail failed to be created, updated, versioned, or deleted.</p>"""
    failure_recommendations: NotRequired[
        "aws_sdk_bedrock.types.guardrail_failure_recommendations.GuardrailFailureRecommendations"
    ]
    """<p>Appears if the <code>status</code> of the guardrail is <code>FAILED</code>. A list of recommendations to carry out before retrying the request.</p>"""
    blocked_input_messaging: (
        "aws_sdk_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging"
    )
    """<p>The message that the guardrail returns when it blocks a prompt.</p>"""
    blocked_outputs_messaging: (
        "aws_sdk_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging"
    )
    """<p>The message that the guardrail returns when it blocks a model response.</p>"""
    kms_key_arn: NotRequired["aws_sdk_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key that encrypts the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGuardrailResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["guardrailId"] = value["guardrail_id"]
    out["guardrailArn"] = value["guardrail_arn"]
    out["version"] = value["version"]
    import aws_sdk_bedrock.types.guardrail_status

    out["status"] = aws_sdk_bedrock.types.guardrail_status.serialize_json(
        value["status"]
    )
    if "topic_policy" in value:
        import aws_sdk_bedrock.types.guardrail_topic_policy

        out["topicPolicy"] = (
            aws_sdk_bedrock.types.guardrail_topic_policy.serialize_json(
                value["topic_policy"]
            )
        )
    if "content_policy" in value:
        import aws_sdk_bedrock.types.guardrail_content_policy

        out["contentPolicy"] = (
            aws_sdk_bedrock.types.guardrail_content_policy.serialize_json(
                value["content_policy"]
            )
        )
    if "word_policy" in value:
        import aws_sdk_bedrock.types.guardrail_word_policy

        out["wordPolicy"] = aws_sdk_bedrock.types.guardrail_word_policy.serialize_json(
            value["word_policy"]
        )
    if "sensitive_information_policy" in value:
        import aws_sdk_bedrock.types.guardrail_sensitive_information_policy

        out["sensitiveInformationPolicy"] = (
            aws_sdk_bedrock.types.guardrail_sensitive_information_policy.serialize_json(
                value["sensitive_information_policy"]
            )
        )
    if "contextual_grounding_policy" in value:
        import aws_sdk_bedrock.types.guardrail_contextual_grounding_policy

        out["contextualGroundingPolicy"] = (
            aws_sdk_bedrock.types.guardrail_contextual_grounding_policy.serialize_json(
                value["contextual_grounding_policy"]
            )
        )
    if "automated_reasoning_policy" in value:
        import aws_sdk_bedrock.types.guardrail_automated_reasoning_policy

        out["automatedReasoningPolicy"] = (
            aws_sdk_bedrock.types.guardrail_automated_reasoning_policy.serialize_json(
                value["automated_reasoning_policy"]
            )
        )
    if "cross_region_details" in value:
        import aws_sdk_bedrock.types.guardrail_cross_region_details

        out["crossRegionDetails"] = (
            aws_sdk_bedrock.types.guardrail_cross_region_details.serialize_json(
                value["cross_region_details"]
            )
        )
    import aws_sdk_bedrock.types.timestamp

    out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    if "status_reasons" in value:
        import aws_sdk_bedrock.types.guardrail_status_reasons

        out["statusReasons"] = (
            aws_sdk_bedrock.types.guardrail_status_reasons.serialize_json(
                value["status_reasons"]
            )
        )
    if "failure_recommendations" in value:
        import aws_sdk_bedrock.types.guardrail_failure_recommendations

        out["failureRecommendations"] = (
            aws_sdk_bedrock.types.guardrail_failure_recommendations.serialize_json(
                value["failure_recommendations"]
            )
        )
    out["blockedInputMessaging"] = value["blocked_input_messaging"]
    out["blockedOutputsMessaging"] = value["blocked_outputs_messaging"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GetGuardrailResponse:
    out: GetGuardrailResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetGuardrailResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "guardrailId" in data:
        out["guardrail_id"] = data["guardrailId"]
    else:
        raise DeserializationError("GetGuardrailResponse.guardrail_id required")
    if "guardrailArn" in data:
        out["guardrail_arn"] = data["guardrailArn"]
    else:
        raise DeserializationError("GetGuardrailResponse.guardrail_arn required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("GetGuardrailResponse.version required")
    if "status" in data:
        import aws_sdk_bedrock.types.guardrail_status

        out["status"] = aws_sdk_bedrock.types.guardrail_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetGuardrailResponse.status required")
    if "topicPolicy" in data:
        import aws_sdk_bedrock.types.guardrail_topic_policy

        out["topic_policy"] = (
            aws_sdk_bedrock.types.guardrail_topic_policy.deserialize_json(
                data["topicPolicy"]
            )
        )
    if "contentPolicy" in data:
        import aws_sdk_bedrock.types.guardrail_content_policy

        out["content_policy"] = (
            aws_sdk_bedrock.types.guardrail_content_policy.deserialize_json(
                data["contentPolicy"]
            )
        )
    if "wordPolicy" in data:
        import aws_sdk_bedrock.types.guardrail_word_policy

        out["word_policy"] = (
            aws_sdk_bedrock.types.guardrail_word_policy.deserialize_json(
                data["wordPolicy"]
            )
        )
    if "sensitiveInformationPolicy" in data:
        import aws_sdk_bedrock.types.guardrail_sensitive_information_policy

        out["sensitive_information_policy"] = (
            aws_sdk_bedrock.types.guardrail_sensitive_information_policy.deserialize_json(
                data["sensitiveInformationPolicy"]
            )
        )
    if "contextualGroundingPolicy" in data:
        import aws_sdk_bedrock.types.guardrail_contextual_grounding_policy

        out["contextual_grounding_policy"] = (
            aws_sdk_bedrock.types.guardrail_contextual_grounding_policy.deserialize_json(
                data["contextualGroundingPolicy"]
            )
        )
    if "automatedReasoningPolicy" in data:
        import aws_sdk_bedrock.types.guardrail_automated_reasoning_policy

        out["automated_reasoning_policy"] = (
            aws_sdk_bedrock.types.guardrail_automated_reasoning_policy.deserialize_json(
                data["automatedReasoningPolicy"]
            )
        )
    if "crossRegionDetails" in data:
        import aws_sdk_bedrock.types.guardrail_cross_region_details

        out["cross_region_details"] = (
            aws_sdk_bedrock.types.guardrail_cross_region_details.deserialize_json(
                data["crossRegionDetails"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetGuardrailResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GetGuardrailResponse.updated_at required")
    if "statusReasons" in data:
        import aws_sdk_bedrock.types.guardrail_status_reasons

        out["status_reasons"] = (
            aws_sdk_bedrock.types.guardrail_status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    if "failureRecommendations" in data:
        import aws_sdk_bedrock.types.guardrail_failure_recommendations

        out["failure_recommendations"] = (
            aws_sdk_bedrock.types.guardrail_failure_recommendations.deserialize_json(
                data["failureRecommendations"]
            )
        )
    if "blockedInputMessaging" in data:
        out["blocked_input_messaging"] = data["blockedInputMessaging"]
    else:
        raise DeserializationError(
            "GetGuardrailResponse.blocked_input_messaging required"
        )
    if "blockedOutputsMessaging" in data:
        out["blocked_outputs_messaging"] = data["blockedOutputsMessaging"]
    else:
        raise DeserializationError(
            "GetGuardrailResponse.blocked_outputs_messaging required"
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
