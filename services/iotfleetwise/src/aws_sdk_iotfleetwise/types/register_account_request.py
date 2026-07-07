"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#RegisterAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.iam_resources
    import aws_sdk_iotfleetwise.types.timestream_resources


class RegisterAccountRequest(TypedDict, closed=True):
    timestream_resources: NotRequired[
        "aws_sdk_iotfleetwise.types.timestream_resources.TimestreamResources"
    ]
    iam_resources: NotRequired["aws_sdk_iotfleetwise.types.iam_resources.IamResources"]
    """<p>The IAM resource that allows Amazon Web Services IoT FleetWise to send data to Amazon Timestream.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegisterAccountRequest) -> dict:
    out: dict = {}
    if "timestream_resources" in value:
        import aws_sdk_iotfleetwise.types.timestream_resources

        out["timestreamResources"] = (
            aws_sdk_iotfleetwise.types.timestream_resources.serialize_aws_json_1_0(
                value["timestream_resources"]
            )
        )
    if "iam_resources" in value:
        import aws_sdk_iotfleetwise.types.iam_resources

        out["iamResources"] = (
            aws_sdk_iotfleetwise.types.iam_resources.serialize_aws_json_1_0(
                value["iam_resources"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegisterAccountRequest:
    out: RegisterAccountRequest = {}  # type: ignore[typeddict-item]
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
    return out
