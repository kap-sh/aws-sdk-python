"""Generated from Smithy shape ``com.amazonaws.connecthealth#StartPatientInsightsJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.domain_id
    import aws_sdk_connecthealth.types.input_data_config
    import aws_sdk_connecthealth.types.insights_context
    import aws_sdk_connecthealth.types.non_empty_string
    import aws_sdk_connecthealth.types.output_data_config
    import aws_sdk_connecthealth.types.patient_insights_encounter_context
    import aws_sdk_connecthealth.types.patient_insights_patient_context
    import aws_sdk_connecthealth.types.user_context


class StartPatientInsightsJobRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_connecthealth.types.domain_id.DomainId"
    """<p/>"""
    patient_context: "aws_sdk_connecthealth.types.patient_insights_patient_context.PatientInsightsPatientContext"
    """<p/>"""
    insights_context: "aws_sdk_connecthealth.types.insights_context.InsightsContext"
    """<p/>"""
    encounter_context: "aws_sdk_connecthealth.types.patient_insights_encounter_context.PatientInsightsEncounterContext"
    """<p/>"""
    user_context: "aws_sdk_connecthealth.types.user_context.UserContext"
    """<p/>"""
    input_data_config: "aws_sdk_connecthealth.types.input_data_config.InputDataConfig"
    """<p/>"""
    output_data_config: (
        "aws_sdk_connecthealth.types.output_data_config.OutputDataConfig"
    )
    """<p/>"""
    client_token: NotRequired[
        "aws_sdk_connecthealth.types.non_empty_string.NonEmptyString"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPatientInsightsJobRequest) -> dict:
    out: dict = {}
    import aws_sdk_connecthealth.types.patient_insights_patient_context

    out["patientContext"] = (
        aws_sdk_connecthealth.types.patient_insights_patient_context.serialize_json(
            value["patient_context"]
        )
    )
    import aws_sdk_connecthealth.types.insights_context

    out["insightsContext"] = (
        aws_sdk_connecthealth.types.insights_context.serialize_json(
            value["insights_context"]
        )
    )
    import aws_sdk_connecthealth.types.patient_insights_encounter_context

    out["encounterContext"] = (
        aws_sdk_connecthealth.types.patient_insights_encounter_context.serialize_json(
            value["encounter_context"]
        )
    )
    import aws_sdk_connecthealth.types.user_context

    out["userContext"] = aws_sdk_connecthealth.types.user_context.serialize_json(
        value["user_context"]
    )
    import aws_sdk_connecthealth.types.input_data_config

    out["inputDataConfig"] = (
        aws_sdk_connecthealth.types.input_data_config.serialize_json(
            value["input_data_config"]
        )
    )
    import aws_sdk_connecthealth.types.output_data_config

    out["outputDataConfig"] = (
        aws_sdk_connecthealth.types.output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartPatientInsightsJobRequest:
    out: StartPatientInsightsJobRequest = {}  # type: ignore[typeddict-item]
    if "patientContext" in data:
        import aws_sdk_connecthealth.types.patient_insights_patient_context

        out["patient_context"] = (
            aws_sdk_connecthealth.types.patient_insights_patient_context.deserialize_json(
                data["patientContext"]
            )
        )
    else:
        raise DeserializationError(
            "StartPatientInsightsJobRequest.patient_context required"
        )
    if "insightsContext" in data:
        import aws_sdk_connecthealth.types.insights_context

        out["insights_context"] = (
            aws_sdk_connecthealth.types.insights_context.deserialize_json(
                data["insightsContext"]
            )
        )
    else:
        raise DeserializationError(
            "StartPatientInsightsJobRequest.insights_context required"
        )
    if "encounterContext" in data:
        import aws_sdk_connecthealth.types.patient_insights_encounter_context

        out["encounter_context"] = (
            aws_sdk_connecthealth.types.patient_insights_encounter_context.deserialize_json(
                data["encounterContext"]
            )
        )
    else:
        raise DeserializationError(
            "StartPatientInsightsJobRequest.encounter_context required"
        )
    if "userContext" in data:
        import aws_sdk_connecthealth.types.user_context

        out["user_context"] = aws_sdk_connecthealth.types.user_context.deserialize_json(
            data["userContext"]
        )
    else:
        raise DeserializationError(
            "StartPatientInsightsJobRequest.user_context required"
        )
    if "inputDataConfig" in data:
        import aws_sdk_connecthealth.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_connecthealth.types.input_data_config.deserialize_json(
                data["inputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartPatientInsightsJobRequest.input_data_config required"
        )
    if "outputDataConfig" in data:
        import aws_sdk_connecthealth.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_connecthealth.types.output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartPatientInsightsJobRequest.output_data_config required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
