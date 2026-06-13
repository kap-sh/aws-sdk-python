"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetPatientInsightsJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_connecthealth.types.input_data_config
    import aws_sdk_connecthealth.types.insights_context
    import aws_sdk_connecthealth.types.insights_output
    import aws_sdk_connecthealth.types.job_arn
    import aws_sdk_connecthealth.types.job_id
    import aws_sdk_connecthealth.types.job_status
    import aws_sdk_connecthealth.types.non_empty_string
    import aws_sdk_connecthealth.types.output_data_config
    import aws_sdk_connecthealth.types.patient_insights_encounter_context
    import aws_sdk_connecthealth.types.patient_insights_patient_context
    import aws_sdk_connecthealth.types.user_context


class GetPatientInsightsJobResponse(TypedDict):
    job_id: "aws_sdk_connecthealth.types.job_id.JobId"
    """<p/>"""
    job_arn: "aws_sdk_connecthealth.types.job_arn.JobArn"
    """<p/>"""
    job_status: "aws_sdk_connecthealth.types.job_status.JobStatus"
    """<p/>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>Date and time the patient insights job was submitted.</p>"""
    updated_time: NotRequired["datetime.datetime"]
    """<p>Date and time the patient insights job was last updated.</p>"""
    insights_output: NotRequired[
        "aws_sdk_connecthealth.types.insights_output.InsightsOutput"
    ]
    """<p/>"""
    status_details: NotRequired[
        "aws_sdk_connecthealth.types.non_empty_string.NonEmptyString"
    ]
    """<p>Contains information about the status of a job.</p>"""
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


# --- restJson1 ser/de ---
def serialize_json(value: GetPatientInsightsJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["jobArn"] = value["job_arn"]
    import aws_sdk_connecthealth.types.job_status

    out["jobStatus"] = aws_sdk_connecthealth.types.job_status.serialize_json(
        value["job_status"]
    )
    if "creation_time" in value:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["creationTime"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "updated_time" in value:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["updatedTime"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.serialize_json(
                value["updated_time"]
            )
        )
    if "insights_output" in value:
        import aws_sdk_connecthealth.types.insights_output

        out["insightsOutput"] = (
            aws_sdk_connecthealth.types.insights_output.serialize_json(
                value["insights_output"]
            )
        )
    if "status_details" in value:
        out["statusDetails"] = value["status_details"]
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
    return out


def deserialize_json(data: dict) -> GetPatientInsightsJobResponse:
    out: GetPatientInsightsJobResponse = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("GetPatientInsightsJobResponse.job_id required")
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("GetPatientInsightsJobResponse.job_arn required")
    if "jobStatus" in data:
        import aws_sdk_connecthealth.types.job_status

        out["job_status"] = aws_sdk_connecthealth.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    else:
        raise DeserializationError("GetPatientInsightsJobResponse.job_status required")
    if "creationTime" in data:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "updatedTime" in data:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["updated_time"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.deserialize_json(
                data["updatedTime"]
            )
        )
    if "insightsOutput" in data:
        import aws_sdk_connecthealth.types.insights_output

        out["insights_output"] = (
            aws_sdk_connecthealth.types.insights_output.deserialize_json(
                data["insightsOutput"]
            )
        )
    if "statusDetails" in data:
        out["status_details"] = data["statusDetails"]
    if "patientContext" in data:
        import aws_sdk_connecthealth.types.patient_insights_patient_context

        out["patient_context"] = (
            aws_sdk_connecthealth.types.patient_insights_patient_context.deserialize_json(
                data["patientContext"]
            )
        )
    else:
        raise DeserializationError(
            "GetPatientInsightsJobResponse.patient_context required"
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
            "GetPatientInsightsJobResponse.insights_context required"
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
            "GetPatientInsightsJobResponse.encounter_context required"
        )
    if "userContext" in data:
        import aws_sdk_connecthealth.types.user_context

        out["user_context"] = aws_sdk_connecthealth.types.user_context.deserialize_json(
            data["userContext"]
        )
    else:
        raise DeserializationError(
            "GetPatientInsightsJobResponse.user_context required"
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
            "GetPatientInsightsJobResponse.input_data_config required"
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
            "GetPatientInsightsJobResponse.output_data_config required"
        )
    return out
