"""Generated from Smithy shape ``com.amazonaws.workmail#CreateIdentityCenterApplicationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.application_arn


class CreateIdentityCenterApplicationResponse(TypedDict):
    application_arn: NotRequired[
        "aws_sdk_workmail.types.application_arn.ApplicationArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the application. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIdentityCenterApplicationResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIdentityCenterApplicationResponse:
    out: CreateIdentityCenterApplicationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    return out
