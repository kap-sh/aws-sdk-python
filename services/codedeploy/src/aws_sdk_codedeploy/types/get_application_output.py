"""Generated from Smithy shape ``com.amazonaws.codedeploy#GetApplicationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.application_info


class GetApplicationOutput(TypedDict):
    application: NotRequired[
        "aws_sdk_codedeploy.types.application_info.ApplicationInfo"
    ]
    """<p>Information about the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationOutput) -> dict:
    out: dict = {}
    if "application" in value:
        import aws_sdk_codedeploy.types.application_info

        out["application"] = (
            aws_sdk_codedeploy.types.application_info.serialize_aws_json_1_1(
                value["application"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationOutput:
    out: GetApplicationOutput = {}  # type: ignore[typeddict-item]
    if "application" in data:
        import aws_sdk_codedeploy.types.application_info

        out["application"] = (
            aws_sdk_codedeploy.types.application_info.deserialize_aws_json_1_1(
                data["application"]
            )
        )
    return out
