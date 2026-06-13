"""Generated from Smithy shape ``com.amazonaws.proton#GetEnvironmentTemplateVersionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_template_version


class GetEnvironmentTemplateVersionOutput(TypedDict):
    environment_template_version: (
        "aws_sdk_proton.types.environment_template_version.EnvironmentTemplateVersion"
    )
    """<p>The detailed data of the requested environment template version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnvironmentTemplateVersionOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.environment_template_version

    out["environmentTemplateVersion"] = (
        aws_sdk_proton.types.environment_template_version.serialize_aws_json_1_0(
            value["environment_template_version"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnvironmentTemplateVersionOutput:
    out: GetEnvironmentTemplateVersionOutput = {}  # type: ignore[typeddict-item]
    if "environmentTemplateVersion" in data:
        import aws_sdk_proton.types.environment_template_version

        out["environment_template_version"] = (
            aws_sdk_proton.types.environment_template_version.deserialize_aws_json_1_0(
                data["environmentTemplateVersion"]
            )
        )
    else:
        raise DeserializationError(
            "GetEnvironmentTemplateVersionOutput.environment_template_version required"
        )
    return out
