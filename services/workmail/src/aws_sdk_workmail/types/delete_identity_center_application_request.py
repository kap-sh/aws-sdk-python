"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteIdentityCenterApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.application_arn


class DeleteIdentityCenterApplicationRequest(TypedDict):
    application_arn: "aws_sdk_workmail.types.application_arn.ApplicationArn"
    """<p> The Amazon Resource Name (ARN) of the application. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIdentityCenterApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIdentityCenterApplicationRequest:
    out: DeleteIdentityCenterApplicationRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "DeleteIdentityCenterApplicationRequest.application_arn required"
        )
    return out
