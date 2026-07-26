"""Generated from Smithy shape ``com.amazonaws.configservice#StartResourceEvaluationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.client_token
    import capo_config_service.types.evaluation_context
    import capo_config_service.types.evaluation_mode
    import capo_config_service.types.evaluation_timeout
    import capo_config_service.types.resource_details


class StartResourceEvaluationRequest(TypedDict, closed=True):
    resource_details: "capo_config_service.types.resource_details.ResourceDetails"
    """<p>Returns a <code>ResourceDetails</code> object.</p>"""
    evaluation_context: NotRequired[
        "capo_config_service.types.evaluation_context.EvaluationContext"
    ]
    """<p>Returns an <code>EvaluationContext</code> object.</p>"""
    evaluation_mode: "capo_config_service.types.evaluation_mode.EvaluationMode"
    """<p>The mode of an evaluation.</p> <note> <p>The only valid value for this API is <code>PROACTIVE</code>.</p> </note>"""
    evaluation_timeout: "capo_config_service.types.evaluation_timeout.EvaluationTimeout"
    """<p>The timeout for an evaluation. The default is 900 seconds. You cannot specify a number greater than 3600. If you specify 0, Config uses the default.</p>"""
    client_token: NotRequired["capo_config_service.types.client_token.ClientToken"]
    """<p>A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request.</p> <note> <p>Avoid reusing the same client token for other API requests. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, other than the Region or Availability Zone, the retry fails with an IdempotentParameterMismatch error.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartResourceEvaluationRequest) -> dict:
    out: dict = {}
    import capo_config_service.types.resource_details

    out["ResourceDetails"] = (
        capo_config_service.types.resource_details.serialize_aws_json_1_1(
            value["resource_details"]
        )
    )
    if "evaluation_context" in value:
        import capo_config_service.types.evaluation_context

        out["EvaluationContext"] = (
            capo_config_service.types.evaluation_context.serialize_aws_json_1_1(
                value["evaluation_context"]
            )
        )
    import capo_config_service.types.evaluation_mode

    out["EvaluationMode"] = (
        capo_config_service.types.evaluation_mode.serialize_aws_json_1_1(
            value["evaluation_mode"]
        )
    )
    out["EvaluationTimeout"] = value.get("evaluation_timeout", 0)
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartResourceEvaluationRequest:
    out: StartResourceEvaluationRequest = {}  # type: ignore[typeddict-item]
    if "ResourceDetails" in data:
        import capo_config_service.types.resource_details

        out["resource_details"] = (
            capo_config_service.types.resource_details.deserialize_aws_json_1_1(
                data["ResourceDetails"]
            )
        )
    else:
        raise DeserializationError(
            "StartResourceEvaluationRequest.resource_details required"
        )
    if "EvaluationContext" in data:
        import capo_config_service.types.evaluation_context

        out["evaluation_context"] = (
            capo_config_service.types.evaluation_context.deserialize_aws_json_1_1(
                data["EvaluationContext"]
            )
        )
    if "EvaluationMode" in data:
        import capo_config_service.types.evaluation_mode

        out["evaluation_mode"] = (
            capo_config_service.types.evaluation_mode.deserialize_aws_json_1_1(
                data["EvaluationMode"]
            )
        )
    else:
        raise DeserializationError(
            "StartResourceEvaluationRequest.evaluation_mode required"
        )
    if "EvaluationTimeout" in data:
        out["evaluation_timeout"] = data["EvaluationTimeout"]
    else:
        out["evaluation_timeout"] = 0
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
