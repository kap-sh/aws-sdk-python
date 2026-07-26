"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TimestreamRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.error_message
    import capo_iotfleetwise.types.registration_status
    import capo_iotfleetwise.types.timestream_database_name
    import capo_iotfleetwise.types.timestream_table_name


class TimestreamRegistrationResponse(TypedDict, closed=True):
    timestream_database_name: (
        "capo_iotfleetwise.types.timestream_database_name.TimestreamDatabaseName"
    )
    """<p>The name of the Timestream database.</p>"""
    timestream_table_name: (
        "capo_iotfleetwise.types.timestream_table_name.TimestreamTableName"
    )
    """<p>The name of the Timestream database table.</p>"""
    timestream_database_arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The Amazon Resource Name (ARN) of the Timestream database.</p>"""
    timestream_table_arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The ARN of the Timestream database table.</p>"""
    registration_status: (
        "capo_iotfleetwise.types.registration_status.RegistrationStatus"
    )
    """<p>The status of registering your Amazon Timestream resources. The status can be one of <code>REGISTRATION_SUCCESS</code>, <code>REGISTRATION_PENDING</code>, <code>REGISTRATION_FAILURE</code>.</p>"""
    error_message: NotRequired["capo_iotfleetwise.types.error_message.errorMessage"]
    """<p>A message associated with a registration error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimestreamRegistrationResponse) -> dict:
    out: dict = {}
    out["timestreamDatabaseName"] = value["timestream_database_name"]
    out["timestreamTableName"] = value["timestream_table_name"]
    if "timestream_database_arn" in value:
        out["timestreamDatabaseArn"] = value["timestream_database_arn"]
    if "timestream_table_arn" in value:
        out["timestreamTableArn"] = value["timestream_table_arn"]
    import capo_iotfleetwise.types.registration_status

    out["registrationStatus"] = (
        capo_iotfleetwise.types.registration_status.serialize_aws_json_1_0(
            value["registration_status"]
        )
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimestreamRegistrationResponse:
    out: TimestreamRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "timestreamDatabaseName" in data:
        out["timestream_database_name"] = data["timestreamDatabaseName"]
    else:
        raise DeserializationError(
            "TimestreamRegistrationResponse.timestream_database_name required"
        )
    if "timestreamTableName" in data:
        out["timestream_table_name"] = data["timestreamTableName"]
    else:
        raise DeserializationError(
            "TimestreamRegistrationResponse.timestream_table_name required"
        )
    if "timestreamDatabaseArn" in data:
        out["timestream_database_arn"] = data["timestreamDatabaseArn"]
    if "timestreamTableArn" in data:
        out["timestream_table_arn"] = data["timestreamTableArn"]
    if "registrationStatus" in data:
        import capo_iotfleetwise.types.registration_status

        out["registration_status"] = (
            capo_iotfleetwise.types.registration_status.deserialize_aws_json_1_0(
                data["registrationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "TimestreamRegistrationResponse.registration_status required"
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
