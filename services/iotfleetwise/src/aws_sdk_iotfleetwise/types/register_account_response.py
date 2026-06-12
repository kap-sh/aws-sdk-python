"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#RegisterAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.iam_resources
    import aws_sdk_iotfleetwise.types.registration_status
    import aws_sdk_iotfleetwise.types.timestamp
    import aws_sdk_iotfleetwise.types.timestream_resources


class RegisterAccountResponse(TypedDict):
    register_account_status: (
        "aws_sdk_iotfleetwise.types.registration_status.RegistrationStatus"
    )
    """<p> The status of registering your Amazon Web Services account, IAM role, and Timestream resources. </p>"""
    timestream_resources: NotRequired[
        "aws_sdk_iotfleetwise.types.timestream_resources.TimestreamResources"
    ]
    iam_resources: "aws_sdk_iotfleetwise.types.iam_resources.IamResources"
    """<p> The registered IAM resource that allows Amazon Web Services IoT FleetWise to send data to Amazon Timestream. </p>"""
    creation_time: "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    """<p> The time the account was registered, in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""
    last_modification_time: "aws_sdk_iotfleetwise.types.timestamp.timestamp"
    """<p> The time this registration was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegisterAccountResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotfleetwise.types.registration_status

    out["registerAccountStatus"] = (
        aws_sdk_iotfleetwise.types.registration_status.serialize_aws_json_1_0(
            value["register_account_status"]
        )
    )
    if "timestream_resources" in value:
        import aws_sdk_iotfleetwise.types.timestream_resources

        out["timestreamResources"] = (
            aws_sdk_iotfleetwise.types.timestream_resources.serialize_aws_json_1_0(
                value["timestream_resources"]
            )
        )
    import aws_sdk_iotfleetwise.types.iam_resources

    out["iamResources"] = (
        aws_sdk_iotfleetwise.types.iam_resources.serialize_aws_json_1_0(
            value["iam_resources"]
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


def deserialize_aws_json_1_0(data: dict) -> RegisterAccountResponse:
    out: RegisterAccountResponse = {}  # type: ignore[typeddict-item]
    if "registerAccountStatus" in data:
        import aws_sdk_iotfleetwise.types.registration_status

        out["register_account_status"] = (
            aws_sdk_iotfleetwise.types.registration_status.deserialize_aws_json_1_0(
                data["registerAccountStatus"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterAccountResponse.register_account_status required"
        )
    if "timestreamResources" in data:
        import aws_sdk_iotfleetwise.types.timestream_resources

        out["timestream_resources"] = (
            aws_sdk_iotfleetwise.types.timestream_resources.deserialize_aws_json_1_0(
                data["timestreamResources"]
            )
        )
    if "iamResources" in data:
        import aws_sdk_iotfleetwise.types.iam_resources

        out["iam_resources"] = (
            aws_sdk_iotfleetwise.types.iam_resources.deserialize_aws_json_1_0(
                data["iamResources"]
            )
        )
    else:
        raise DeserializationError("RegisterAccountResponse.iam_resources required")
    if "creationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["creation_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("RegisterAccountResponse.creation_time required")
    if "lastModificationTime" in data:
        import aws_sdk_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterAccountResponse.last_modification_time required"
        )
    return out
