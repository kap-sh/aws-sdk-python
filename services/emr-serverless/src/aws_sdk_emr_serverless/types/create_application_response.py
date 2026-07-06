"""Generated from Smithy shape ``com.amazonaws.emrserverless#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_arn
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.application_name


class CreateApplicationResponse(TypedDict, closed=True):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The output contains the application ID.</p>"""
    name: NotRequired["aws_sdk_emr_serverless.types.application_name.ApplicationName"]
    """<p>The output contains the name of the application.</p>"""
    arn: "aws_sdk_emr_serverless.types.application_arn.ApplicationArn"
    """<p>The output contains the ARN of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    if "name" in value:
        out["name"] = value["name"]
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("CreateApplicationResponse.application_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateApplicationResponse.arn required")
    return out
