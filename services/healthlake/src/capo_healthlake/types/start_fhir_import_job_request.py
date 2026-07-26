"""Generated from Smithy shape ``com.amazonaws.healthlake#StartFHIRImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.client_token_string
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.iam_role_arn
    import capo_healthlake.types.input_data_config
    import capo_healthlake.types.job_name
    import capo_healthlake.types.output_data_config
    import capo_healthlake.types.validation_level


class StartFHIRImportJobRequest(TypedDict, closed=True):
    job_name: NotRequired["capo_healthlake.types.job_name.JobName"]
    """<p>The import job name.</p>"""
    input_data_config: "capo_healthlake.types.input_data_config.InputDataConfig"
    """<p>The input properties for the import job request.</p>"""
    job_output_data_config: "capo_healthlake.types.output_data_config.OutputDataConfig"
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    data_access_role_arn: "capo_healthlake.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) that grants access permission to AWS HealthLake.</p>"""
    client_token: NotRequired[
        "capo_healthlake.types.client_token_string.ClientTokenString"
    ]
    """<p>The optional user-provided token used for ensuring API idempotency.</p>"""
    validation_level: NotRequired[
        "capo_healthlake.types.validation_level.ValidationLevel"
    ]
    """<p>The validation level of the import job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFHIRImportJobRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import capo_healthlake.types.input_data_config

    out["InputDataConfig"] = (
        capo_healthlake.types.input_data_config.serialize_aws_json_1_0(
            value["input_data_config"]
        )
    )
    import capo_healthlake.types.output_data_config

    out["JobOutputDataConfig"] = (
        capo_healthlake.types.output_data_config.serialize_aws_json_1_0(
            value["job_output_data_config"]
        )
    )
    out["DatastoreId"] = value["datastore_id"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "validation_level" in value:
        import capo_healthlake.types.validation_level

        out["ValidationLevel"] = (
            capo_healthlake.types.validation_level.serialize_aws_json_1_0(
                value["validation_level"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartFHIRImportJobRequest:
    out: StartFHIRImportJobRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "InputDataConfig" in data:
        import capo_healthlake.types.input_data_config

        out["input_data_config"] = (
            capo_healthlake.types.input_data_config.deserialize_aws_json_1_0(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartFHIRImportJobRequest.input_data_config required"
        )
    if "JobOutputDataConfig" in data:
        import capo_healthlake.types.output_data_config

        out["job_output_data_config"] = (
            capo_healthlake.types.output_data_config.deserialize_aws_json_1_0(
                data["JobOutputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartFHIRImportJobRequest.job_output_data_config required"
        )
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    else:
        raise DeserializationError("StartFHIRImportJobRequest.datastore_id required")
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartFHIRImportJobRequest.data_access_role_arn required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ValidationLevel" in data:
        import capo_healthlake.types.validation_level

        out["validation_level"] = (
            capo_healthlake.types.validation_level.deserialize_aws_json_1_0(
                data["ValidationLevel"]
            )
        )
    return out
