"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateApplicationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_id


class CreateApplicationOutput(TypedDict, closed=True):
    application_id: NotRequired["aws_sdk_codedeploy.types.application_id.ApplicationId"]
    """<p>A unique application ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationOutput) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationOutput:
    out: CreateApplicationOutput = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    return out
