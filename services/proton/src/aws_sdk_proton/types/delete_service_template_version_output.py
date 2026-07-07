"""Generated from Smithy shape ``com.amazonaws.proton#DeleteServiceTemplateVersionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_template_version


class DeleteServiceTemplateVersionOutput(TypedDict, closed=True):
    service_template_version: NotRequired[
        "aws_sdk_proton.types.service_template_version.ServiceTemplateVersion"
    ]
    """<p>The detailed data of the service template version being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteServiceTemplateVersionOutput) -> dict:
    out: dict = {}
    if "service_template_version" in value:
        import aws_sdk_proton.types.service_template_version

        out["serviceTemplateVersion"] = (
            aws_sdk_proton.types.service_template_version.serialize_aws_json_1_0(
                value["service_template_version"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteServiceTemplateVersionOutput:
    out: DeleteServiceTemplateVersionOutput = {}  # type: ignore[typeddict-item]
    if "serviceTemplateVersion" in data:
        import aws_sdk_proton.types.service_template_version

        out["service_template_version"] = (
            aws_sdk_proton.types.service_template_version.deserialize_aws_json_1_0(
                data["serviceTemplateVersion"]
            )
        )
    return out
