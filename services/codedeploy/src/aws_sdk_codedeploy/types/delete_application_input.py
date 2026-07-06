"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeleteApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_name


class DeleteApplicationInput(TypedDict, closed=True):
    application_name: "aws_sdk_codedeploy.types.application_name.ApplicationName"
    """<p>The name of an CodeDeploy application associated with the user or Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationInput:
    out: DeleteApplicationInput = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    else:
        raise DeserializationError("DeleteApplicationInput.application_name required")
    return out
