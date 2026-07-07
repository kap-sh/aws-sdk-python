"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetApplicationRevisionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codedeploy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_name
    import aws_sdk_codedeploy.types.revision_location


class GetApplicationRevisionInput(TypedDict, closed=True):
    application_name: "aws_sdk_codedeploy.types.application_name.ApplicationName"
    """<p>The name of the application that corresponds to the revision.</p>"""
    revision: "aws_sdk_codedeploy.types.revision_location.RevisionLocation"
    """<p>Information about the application revision to get, including type and location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationRevisionInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    import aws_sdk_codedeploy.types.revision_location

    out["revision"] = aws_sdk_codedeploy.types.revision_location.serialize_aws_json_1_1(
        value["revision"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationRevisionInput:
    out: GetApplicationRevisionInput = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    else:
        raise DeserializationError(
            "GetApplicationRevisionInput.application_name required"
        )
    if "revision" in data:
        import aws_sdk_codedeploy.types.revision_location

        out["revision"] = (
            aws_sdk_codedeploy.types.revision_location.deserialize_aws_json_1_1(
                data["revision"]
            )
        )
    else:
        raise DeserializationError("GetApplicationRevisionInput.revision required")
    return out
