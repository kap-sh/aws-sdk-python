"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetRegisterAccountStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.customer_account_id
    import aws_sdk_iotfleetwise.types.iam_registration_response
    import aws_sdk_iotfleetwise.types.registration_status
    import aws_sdk_iotfleetwise.types.timestamp
    import aws_sdk_iotfleetwise.types.timestream_registration_response


class GetRegisterAccountStatusResponse(TypedDict, closed=True):
    customer_account_id: (
        "aws_sdk_iotfleetwise.types.customer_account_id.customerAccountId"
    )
    """<p> The unique ID of the Amazon Web Services account, provided at account creation. </p>"""
    account_status: "aws_sdk_iotfleetwise.types.registration_status.RegistrationStatus"
    """<p> The status of registering your account and resources. The status can be one of:</p> <ul> <li> <p> <code>REGISTRATION_SUCCESS</code> - The Amazon Web Services resource is successfully registered.</p> </li> <li> <p> <code>REGISTRATION_PENDING</code> - Amazon Web Services IoT FleetWise is processing the registration request. This process takes approximately five minutes to complete.</p> </li> <li> <p> <code>REGISTRATION_FAILURE</code> - Amazon Web Services IoT FleetWise can't register the AWS resource. Try again later.</p> </li> </ul>"""
    timestream_registration_response: NotRequired[
        "aws_sdk_iotfleetwise.types.timestream_registration_response.TimestreamRegistrationResponse"
    ]
    """<p> Information about the registered Amazon Timestream resources or errors, if any.</p>"""
    iam_registration_response: (
        "aws_sdk_iotfleetwise.types.iam_registration_response.IamRegistrationResponse"
    )
    """<p> Information about the registered IAM resources or errors, if any. </p>"""
    creation_time: "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    """<p> The time the account was registered, in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    last_modification_time: "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    """<p> The time this registration was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRegisterAccountStatusResponse) -> dict:
    out: dict = {}
    out["customerAccountId"] = value["customer_account_id"]
    import aws_sdk_iotfleetwise.types.registration_status

    out["accountStatus"] = (
        aws_sdk_iotfleetwise.types.registration_status.serialize_aws_json_1_0(
            value["account_status"]
        )
    )
    if "timestream_registration_response" in value:
        import aws_sdk_iotfleetwise.types.timestream_registration_response

        out["timestreamRegistrationResponse"] = (
            aws_sdk_iotfleetwise.types.timestream_registration_response.serialize_aws_json_1_0(
                value["timestream_registration_response"]
            )
        )
    import aws_sdk_iotfleetwise.types.iam_registration_response

    out["iamRegistrationResponse"] = (
        aws_sdk_iotfleetwise.types.iam_registration_response.serialize_aws_json_1_0(
            value["iam_registration_response"]
        )
    )
    import aws_sdk_iotfleetwise.types.timestamp

    out["creationTime"] = aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
        value["creation_time"]
    )
    import aws_sdk_iotfleetwise.types.timestamp

    out["lastModificationTime"] = (
        aws_sdk_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["last_modification_time"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRegisterAccountStatusResponse:
    out: GetRegisterAccountStatusResponse = {}  # type: ignore[typeddict-item]
    if "customerAccountId" in data:
        out["customer_account_id"] = data["customerAccountId"]
    else:
        raise DeserializationError(
            "GetRegisterAccountStatusResponse.customer_account_id required"
        )
    if "accountStatus" in data:
        import aws_sdk_iotfleetwise.types.registration_status

        out["account_status"] = (
            aws_sdk_iotfleetwise.types.registration_status.deserialize_aws_json_1_0(
                data["accountStatus"]
            )
        )
    else:
        raise DeserializationError(
            "GetRegisterAccountStatusResponse.account_status required"
        )
    if "timestreamRegistrationResponse" in data:
        import aws_sdk_iotfleetwise.types.timestream_registration_response

        out["timestream_registration_response"] = (
            aws_sdk_iotfleetwise.types.timestream_registration_response.deserialize_aws_json_1_0(
                data["timestreamRegistrationResponse"]
            )
        )
    if "iamRegistrationResponse" in data:
        import aws_sdk_iotfleetwise.types.iam_registration_response

        out["iam_registration_response"] = (
            aws_sdk_iotfleetwise.types.iam_registration_response.deserialize_aws_json_1_0(
                data["iamRegistrationResponse"]
            )
        )
    else:
        raise DeserializationError(
            "GetRegisterAccountStatusResponse.iam_registration_response required"
        )
    if "creationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creation_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetRegisterAccountStatusResponse.creation_time required"
        )
    if "lastModificationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetRegisterAccountStatusResponse.last_modification_time required"
        )
    return out
