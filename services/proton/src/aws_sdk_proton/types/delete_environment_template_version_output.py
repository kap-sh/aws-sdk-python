"""Generated from Smithy shape ``com.amazonaws.proton#DeleteEnvironmentTemplateVersionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_template_version


class DeleteEnvironmentTemplateVersionOutput(TypedDict, closed=True):
    environment_template_version: NotRequired[
        "aws_sdk_proton.types.environment_template_version.EnvironmentTemplateVersion"
    ]
    """<p>The detailed data of the environment template version being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentTemplateVersionOutput) -> dict:
    out: dict = {}
    if "environment_template_version" in value:
        import aws_sdk_proton.types.environment_template_version

        out["environmentTemplateVersion"] = (
            aws_sdk_proton.types.environment_template_version.serialize_aws_json_1_0(
                value["environment_template_version"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentTemplateVersionOutput:
    out: DeleteEnvironmentTemplateVersionOutput = {}  # type: ignore[typeddict-item]
    if "environmentTemplateVersion" in data:
        import aws_sdk_proton.types.environment_template_version

        out["environment_template_version"] = (
            aws_sdk_proton.types.environment_template_version.deserialize_aws_json_1_0(
                data["environmentTemplateVersion"]
            )
        )
    return out
