"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#IamRegistrationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.error_message
    import aws_sdk_iotfleetwise.types.registration_status


class IamRegistrationResponse(TypedDict):
    role_arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to register.</p>"""
    registration_status: (
        "aws_sdk_iotfleetwise.types.registration_status.RegistrationStatus"
    )
    """<p>The status of registering your IAM resource. The status can be one of <code>REGISTRATION_SUCCESS</code>, <code>REGISTRATION_PENDING</code>, <code>REGISTRATION_FAILURE</code>.</p>"""
    error_message: NotRequired["aws_sdk_iotfleetwise.types.error_message.errorMessage"]
    """<p>A message associated with a registration error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IamRegistrationResponse) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    import aws_sdk_iotfleetwise.types.registration_status

    out["registrationStatus"] = (
        aws_sdk_iotfleetwise.types.registration_status.serialize_aws_json_1_0(
            value["registration_status"]
        )
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IamRegistrationResponse:
    out: IamRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("IamRegistrationResponse.role_arn required")
    if "registrationStatus" in data:
        import aws_sdk_iotfleetwise.types.registration_status

        out["registration_status"] = (
            aws_sdk_iotfleetwise.types.registration_status.deserialize_aws_json_1_0(
                data["registrationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "IamRegistrationResponse.registration_status required"
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
